#!/usr/bin/env python3
"""Build/deploy SEO + AI-crawler check. Stdlib only.

usage: check_seo.py <base-url> [--max N]
Works on a local dev server (http://localhost:8000) or a live site.
Exit 1 if any FAIL.
"""
import json
import re
import sys
import urllib.error
import urllib.request
import urllib.robotparser
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

BROWSER = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
# ponytail: UA strings approximate the real bots; good enough to catch CDN UA rules, not IP-verified bot rules.
BOTS = {
    "Googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Bingbot": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "OAI-SearchBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot",
    "GPTBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbot",
    "ChatGPT-User": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot",
    "ClaudeBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +claudebot@anthropic.com)",
    "Claude-SearchBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-SearchBot/1.0; +https://www.anthropic.com)",
    "PerplexityBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)",
    "Applebot": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)",
}
SEARCH_BOTS = {"Googlebot", "Bingbot", "OAI-SearchBot", "Claude-SearchBot", "PerplexityBot", "Applebot"}
CHALLENGE = re.compile(r"cf-chl|challenge-platform|Just a moment\.\.\.|Attention Required", re.I)
MIN_WORDS = 120

results = []  # (level, where, msg)


def report(level, where, msg):
    results.append((level, where, msg))


def fetch(url, ua=BROWSER):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, dict(r.headers), r.read(3_000_000).decode("utf-8", "replace"), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read(200_000).decode("utf-8", "replace"), url
    except Exception as e:  # network/DNS/TLS
        return None, {}, str(e), url


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.desc, self.canonical, self.lang = None, None, None, None
        self.robots, self.h1, self.jsonld, self.text = "", 0, [], []
        self._in, self._skip = None, 0

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in, self.title = "title", ""
        elif tag == "meta":
            name = a.get("name", "").lower()
            if name == "description":
                self.desc = a.get("content", "")
            elif name == "robots":
                self.robots += a.get("content", "").lower()
        elif tag == "link" and "canonical" in a.get("rel", "").lower().split():
            self.canonical = a.get("href")
        elif tag == "h1":
            self.h1 += 1
        elif tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self._in = "ld"
            self.jsonld.append("")
        if tag in ("script", "style", "noscript", "template"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("title", "script"):
            self._in = None
        if tag in ("script", "style", "noscript", "template") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in == "title":
            self.title += data
        elif self._in == "ld":
            self.jsonld[-1] += data
        elif not self._skip:
            self.text.append(data)


def check_robots(base):
    url = urljoin(base, "/robots.txt")
    status, _, body, _ = fetch(url)
    if status != 200:
        report("FAIL", "robots.txt", f"status {status} — ship one (technical.md)")
        return [], None
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(body.splitlines())
    for bot in BOTS:
        if not rp.can_fetch(bot, urljoin(base, "/")):
            level = "FAIL" if bot in SEARCH_BOTS else "INFO"
            report(level, "robots.txt", f"{bot} disallowed from / ({'search visibility lost' if level == 'FAIL' else 'training opt-out'})")
    sitemaps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", body)
    if not sitemaps:
        report("WARN", "robots.txt", "no Sitemap: line")
    return sitemaps, rp


def sitemap_urls(base, sitemaps, limit):
    queue, urls, seen = list(sitemaps) or [urljoin(base, "/sitemap.xml")], [], set()
    while queue and len(urls) < limit:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        status, _, body, _ = fetch(sm)
        if status != 200:
            report("FAIL", "sitemap", f"{sm} status {status}")
            continue
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", body)
        if "<sitemapindex" in body:
            queue += locs
        else:
            urls += locs
    if not urls:
        report("FAIL", "sitemap", "no URLs found — falling back to home page only")
    return urls[:limit] or [base]


def check_page(url, rp):
    status, headers, body, final = fetch(url)
    if status != 200:
        report("FAIL", url, f"status {status}")
        return None
    if final.rstrip("/") != url.rstrip("/"):
        report("WARN", url, f"redirects to {final} — sitemap should list final URLs")
    p = Page()
    p.feed(body)
    title = (p.title or "").strip()
    xrobots = {k.lower(): v for k, v in headers.items()}.get("x-robots-tag", "").lower()
    if "noindex" in p.robots or "noindex" in xrobots:
        report("FAIL", url, "noindex set (meta or X-Robots-Tag) but URL is in sitemap")
    if not title:
        report("FAIL", url, "missing <title>")
    elif not 15 <= len(title) <= 65:
        report("WARN", url, f"title length {len(title)}: {title!r}")
    if not p.desc:
        report("FAIL", url, "missing meta description")
    elif not 70 <= len(p.desc) <= 170:
        report("WARN", url, f"meta description length {len(p.desc)}")
    if p.h1 != 1:
        report("FAIL" if p.h1 == 0 else "WARN", url, f"{p.h1} <h1> tags (want 1)")
    if not p.lang:
        report("FAIL", url, "<html> has no lang")
    if not p.canonical:
        report("WARN", url, "no rel=canonical")
    elif urljoin(url, p.canonical).rstrip("/") != final.rstrip("/"):
        report("WARN", url, f"canonical points elsewhere: {p.canonical}")
    if not p.jsonld:
        report("WARN", url, "no JSON-LD")
    for i, blob in enumerate(p.jsonld):
        try:
            json.loads(blob)
        except ValueError as e:
            report("FAIL", url, f"JSON-LD block {i} invalid: {e}")
    words = len(" ".join(p.text).split())
    if words < MIN_WORDS:
        report("WARN", url, f"only {words} words in raw HTML — JS-rendered or thin; AI crawlers won't see client-side text")
    if rp:
        for bot in SEARCH_BOTS:
            if not rp.can_fetch(bot, url):
                report("FAIL", url, f"robots.txt blocks {bot}")
    return title, (p.desc or "").strip()


def check_bot_access(url):
    b_status, _, b_body, _ = fetch(url)
    for bot, ua in BOTS.items():
        status, _, body, _ = fetch(url, ua)
        level = "FAIL" if bot in SEARCH_BOTS else "WARN"
        if status != b_status:
            report(level, f"edge:{bot}", f"status {status} vs browser {b_status} — CDN/firewall treats this bot differently")
        elif CHALLENGE.search(body) and not CHALLENGE.search(b_body):
            report(level, f"edge:{bot}", "served a bot challenge page")


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        sys.exit(__doc__)
    base = args[0] if "://" in args[0] else "https://" + args[0]
    base = f"{urlparse(base).scheme}://{urlparse(base).netloc}/"
    limit = int(args[args.index("--max") + 1]) if "--max" in args else 25

    sitemaps, rp = check_robots(base)
    urls = sitemap_urls(base, sitemaps, limit)
    pages = {u: check_page(u, rp) for u in urls}
    check_bot_access(base)
    s, _, _, _ = fetch(urljoin(base, "/llms.txt"))
    report("INFO", "llms.txt", "present" if s == 200 else "absent (optional, low impact — ai-search.md)")

    for i, field in ((0, "title"), (1, "meta description")):
        dupes = Counter(v[i] for v in pages.values() if v and v[i])
        for val, n in dupes.items():
            if n > 1:
                report("WARN", "site", f"{n} pages share the same {field}: {val[:60]!r}")

    order = {"FAIL": 0, "WARN": 1, "INFO": 2}
    for level, where, msg in sorted(results, key=lambda r: order[r[0]]):
        print(f"{level:4}  {where}  {msg}")
    fails = sum(r[0] == "FAIL" for r in results)
    print(f"\n{len(urls)} URL(s) checked, {fails} FAIL, {sum(r[0] == 'WARN' for r in results)} WARN")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
