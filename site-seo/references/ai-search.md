# AI-search layer (GEO / AEO)

## Where each engine gets pages

| Engine | Retrieval source | Bot(s) that must reach you | Robots token honoured? |
|---|---|---|---|
| Google AI Overviews / AI Mode / Gemini | Google index | `Googlebot` | yes — eligibility = indexed + snippet-eligible, nothing extra (Google docs) |
| ChatGPT search | Bing index + own index | `OAI-SearchBot` (index), `Bingbot`, `ChatGPT-User` (live fetch) | OAI-SearchBot yes; ChatGPT-User: OpenAI removed robots.txt commitment (user-initiated) |
| Microsoft Copilot | Bing index | `Bingbot` | yes |
| Claude | Claude-SearchBot index + web search provider (Brave, reported) | `Claude-SearchBot`, `Claude-User` | all three Anthropic bots honour robots.txt |
| Perplexity | own index | `PerplexityBot`, `Perplexity-User` | Bot yes; User generally no |
| Apple Intelligence / Siri | Applebot | `Applebot` | yes |

Training-only tokens (blocking them does NOT remove you from AI search): `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `Meta-ExternalAgent`, `Bytespider`.

Google-specific: `Google-Extended` does not affect AI Overviews/AI Mode. To limit what Google's AI features quote, use `nosnippet`, `data-nosnippet`, `max-snippet`, or `noindex` — which also hurt normal search.

Implication: **Bing matters again.** Seer Interactive found ~87% of SearchGPT citations matched Bing top results (2024). Most Indonesian SMB sites never verify Bing — easy edge.

## The silent blocker: CDN / host firewalls

robots.txt is irrelevant if the edge returns 403.
- **Cloudflare**: new domains have blocked AI crawlers by default since 1 Jul 2025. Since 15 Sep 2026 AI Crawl Control splits bots into Search / Training / Agent; Search allowed by default, Training + Agent blocked by default on pages with ads (reported). Check *Security → Bots → AI Crawl Control* and "Bot Fight Mode" / "Block AI bots"; set Search + Agent to Allow. Also the managed robots.txt option can prepend Disallow rules — inspect the live `/robots.txt`, not the repo file.
- Vercel / Netlify: Vercel "Bot Protection"/Attack Challenge mode can challenge crawlers. Check firewall logs.
- Verify with `scripts/check_seo.py` (fetches as each bot UA; a 403/challenge only for bot UAs = edge block).

## Indexing pipes (do at launch)

1. Google Search Console: verify (DNS TXT), submit sitemap, URL-inspect the home page. AI Overview/AI Mode traffic is folded into Performance → Web; no separate report.
2. Bing Webmaster Tools: verify (can import from GSC), submit sitemap. Its **AI Performance** report (launched Feb 2026) shows Copilot citations, cited pages and grounding queries — the only first-party AI-citation data available.
3. IndexNow: put a key file at `/<key>.txt` and ping on deploy. Bing, Yandex, Naver, Seznam, Yep use it; Google does not.
   ```bash
   curl -s "https://api.indexnow.org/indexnow?url=https://example.com/changed-page/&key=<KEY>"
   ```
   For several URLs POST JSON `{"host","key","keyLocation","urlList":[...]}` to the same endpoint. Hook it into the deploy script; Cloudflare has a one-click "Crawler Hints" that does it for you.
4. Google Business Profile (local businesses): Maps + local AI answers draw on it. Name/address/phone must match the site exactly.

## llms.txt — honest status

Proposal (llmstxt.org, Sep 2024): markdown file at `/llms.txt` listing key pages with one-line descriptions.
- Google: does not use it (Illyes, Mueller — "like the keywords meta tag").
- Server logs: Ahrefs, ~137k domains (May 2026) — 97% got zero requests; other studies: OpenAI fetched it 7 times vs ~4,000 robots.txt fetches across 83 sites in 3 months.
- Useful for: coding agents and tools that look for it (docs sites, devtools), and claude-seo's / Lighthouse agentic checks.

Decision: ship a short one (5 min, zero risk), never treat it as a visibility lever, never put content in it that isn't on the site.

```md
# Brand Name

> One-sentence factual description: what, for whom, where.

## Key pages
- [Services](https://example.com/layanan/): what's offered, price ranges if public
- [About](https://example.com/tentang/): who runs it, since when, location
- [Contact](https://example.com/kontak/): WhatsApp, address, hours
```

## Markdown for agents (optional)

Agents (Claude Code, OpenCode) send `Accept: text/markdown`. Cloudflare "Markdown for Agents" (Feb 2026) converts pages at the edge — toggle it on if the site is on Cloudflare. Don't build custom markdown endpoints for a brochure site.

## What actually moves citations (graded — see sources.md)

1. **Rank/index first.** AI Overviews cite top-10 pages less than before (Ahrefs: 76% → 38% after query fan-out), but you still need to be in the index for the sub-queries. Cover the sub-questions a buyer would ask on separate, clear passages or pages.
2. **Brand mentions off-site** — Ahrefs, 75k brands: branded web mentions correlate 0.664 with AI Overview visibility vs 0.218 for backlinks; YouTube mentions ~0.737 (Dec 2025 follow-up). Correlation, not proof — but it's the strongest signal measured. For clients: directories, local press, marketplace listings (Tokopedia/GoFood/Google Maps), YouTube, Reddit/forum threads where real.
3. **Content that is easy to quote** — GEO paper (Princeton/IIT Delhi, KDD 2024, tested incl. Perplexity): adding quotations, statistics, and cited sources raised visibility in generative answers up to ~40%; keyword stuffing did nothing/hurt. See content.md.
4. **Freshness** — Microsoft (Canel) says gen-AI systems value fresh content; Perplexity skews recent. Keep real `dateModified`, update key pages, don't fake dates.
5. **Each platform cites different sources** — only ~11% domain overlap ChatGPT vs Perplexity (2026 studies). Don't optimise for one engine.
6. **Clicks still drive Google** — DOJ trial testimony confirmed NavBoost uses 13 months of click data; titles/snippets that earn the click and pages that satisfy matter.

## Measuring

- GSC Performance (AI features included), Bing AI Performance (Copilot citations).
- Analytics: segment referrers `chatgpt.com`, `perplexity.ai`, `copilot.microsoft.com`, `gemini.google.com`, `claude.ai`; ChatGPT adds `utm_source=chatgpt.com`.
- Monthly manual prompt check: ask each engine the 5 buyer questions from the brief, note if/how the brand is cited. Log it; don't promise results from it.
