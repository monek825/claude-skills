---
name: site-seo
description: Build-time SEO + AI-search (GEO/AEO) implementation for Bray's custom websites — what every page and every deploy must ship so the site is indexed by Google/Bing and cited by ChatGPT, Claude, Perplexity, Gemini, Copilot and Google AI Overviews/AI Mode. Use BEFORE and WHILE building or editing any website (static HTML, Flask, Vite/React, Next), when writing titles/meta/headings, adding robots.txt, sitemap.xml, llms.txt, JSON-LD schema, or when the user says "SEO", "make it searchable", "show up in ChatGPT/AI search", "GEO", "AEO", "AI Overviews". Pair with conversion-copywriting for the words. For auditing a LIVE URL use the `seo` skill (claude-seo) instead.
---

# Site SEO (build-time, AI-search ready)

Goal: every custom site ships crawlable, indexable, citable. `seo` (claude-seo) audits live URLs; this skill is the build checklist + templates. Research basis and evidence grades: [references/sources.md](references/sources.md).

## The one model to hold

AI search is search with a retrieval step. ChatGPT search retrieves mostly via Bing's index + OAI-SearchBot, Copilot via Bing, AI Overviews/AI Mode/Gemini via Google's index, Perplexity via PerplexityBot, Claude via Claude-SearchBot (+ Brave). So the order of work is:

1. **Reachable** — bots not blocked (robots.txt AND CDN/host firewall), content in the raw HTML (most AI crawlers do not run JS).
2. **Indexed** — Google Search Console + Bing Webmaster Tools verified, sitemap submitted, IndexNow pinging Bing.
3. **Understood** — one clear topic per page, title/H1/meta aligned with real queries, JSON-LD matching visible text, entity facts (name, address, what you do) consistent everywhere.
4. **Chosen/cited** — passages that answer a question in the first lines, specific facts with sources, real expertise, a brand that's mentioned on other sites. This is where most of the win is; files alone don't get you cited.

Never promise rankings or citations. No invented stats, reviews, ratings, or "trusted by" claims — that's also a Google spam-policy risk. Unknown facts → `CONTENT-GAPS.md`.

## Build workflow

Read only the reference the step needs.

1. **Brief** (before copy): site type, location/language (most Bray sites: Indonesian, local), 1 primary query cluster per page, the questions buyers ask an AI ("best X in Surabaya", "how much does Y cost"). → [references/content.md](references/content.md)
2. **Copy**: run `conversion-copywriting` for persuasion; apply content.md's citability rules on top. Title/meta/H1 per page from content.md formulas.
3. **Technical baseline**: robots.txt, sitemap.xml, canonical, meta, lang, OG, 404, redirects, headers, server-rendered content. → [references/technical.md](references/technical.md)
4. **Schema**: JSON-LD per site type, only for facts visible on the page. → [references/schema.md](references/schema.md)
5. **AI-search layer**: bot policy, CDN check, Bing + IndexNow, optional llms.txt / markdown, off-site entity work. → [references/ai-search.md](references/ai-search.md)
6. **Verify locally and after deploy**:
   ```bash
   python3 ~/.claude/skills/site-seo/scripts/check_seo.py https://example.com
   ```
   It fetches robots.txt, sitemap, and each sitemap URL (cap 25), as a browser AND as GPTBot / OAI-SearchBot / ClaudeBot / PerplexityBot, and flags: blocked bots, status/UA mismatches (CDN blocking), missing/duplicate title/meta/H1/canonical/lang, broken JSON-LD, thin raw-HTML text (= JS-only content), noindex. Fix every FAIL before calling the site done. For a deeper live audit afterwards: `/seo audit <url>`.
7. **Launch tasks for the user** (Claude can't do these — they need account logins): verify GSC + Bing Webmaster Tools, submit sitemap, set Cloudflare AI Crawl Control "Search" bots to Allow if on Cloudflare, create/claim Google Business Profile for local businesses.

## Non-negotiables per page

- Unique `<title>` (≈50–60 chars, primary topic first, brand last) and meta description (≈140–160 chars, answers the query, no keyword list).
- Exactly one `<h1>` matching the page's promise; logical H2/H3 that read like the questions people ask.
- `<html lang="id">` (or `en`); `rel=canonical` absolute self URL; hreflang only if real translations exist.
- Main content present in server HTML. Hydrating is fine; injecting the text client-side is not.
- Real internal links (`<a href>`) to every indexable page; no orphan pages; no JS-only nav.
- Images: descriptive `alt`, explicit width/height, WebP/AVIF, meaningful filenames.
- Visible "last updated" date where content is time-sensitive; matches `dateModified`.
- Fast: follow `web-perf` (LCP < 2.5s, INP < 200ms, CLS < 0.1).

## What NOT to spend time on

- llms.txt as a ranking lever — no major engine has committed to reading it; server-log studies show near-zero AI fetches. Ship it only because it costs 5 minutes (ai-search.md).
- FAQ schema for rich results — Google limited FAQ rich results to authoritative gov/health sites in 2023. Visible FAQ *content* still helps AI answers.
- Meta keywords, keyword density, "AI-optimised" hidden text, auto-generated location doorway pages (spam policy: scaled content abuse).
- Schema as a citation hack — a 2026 Ahrefs matched-control study (1,885 pages) found no measurable AI-citation lift from adding JSON-LD alone. Do it for correctness and rich results, not magic.
