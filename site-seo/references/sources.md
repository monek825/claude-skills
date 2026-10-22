# Sources and evidence grades

Researched 2026-10-05. Grade: **A** = first-party docs / peer-reviewed; **B** = large-sample industry study (correlational); **C** = practitioner consensus / small study. Re-check A-grade docs yearly; bot names and CDN defaults change.

## Official docs (A)
- Google — AI features and your website: https://developers.google.com/search/docs/appearance/ai-features (eligibility = indexed + snippet-eligible; no special markup; controls: nosnippet/data-nosnippet/max-snippet/noindex; AI traffic inside GSC "Web")
- Google — Succeeding in AI search (May 2025): https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search
- Google — SEO Starter Guide, Search Essentials, spam policies, structured data guidelines, robots.txt spec (developers.google.com/search)
- Google — Search Quality Rater Guidelines (E-E-A-T; PDF, updated periodically)
- OpenAI bots: https://developers.openai.com/api/docs/bots (GPTBot / OAI-SearchBot / ChatGPT-User)
- Anthropic bots: ClaudeBot / Claude-SearchBot / Claude-User, all honour robots.txt (Anthropic help center; SEJ write-up https://www.searchenginejournal.com/anthropics-claude-bots-make-robots-txt-decisions-more-granular/568253/)
- Perplexity bots: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Bing Webmaster Tools AI Performance report (Feb 2026): https://www.searchengineworld.com/bing-introduces-ai-performance-reporting-in-webmaster-tools
- IndexNow: https://www.indexnow.org
- Microsoft (Fabrice Canel) — schema helps Copilot: https://www.seroundtable.com/schema-llms-copilot-bing-microsoft-39093.html
- Cloudflare AI crawler defaults / Markdown for Agents: https://www.theregister.com/2026/02/13/cloudflare_markdown_for_ai_crawlers/ , https://llmrefs.com/blog/cloudflare-blocks-ai-crawlers
- llms.txt proposal: https://llmstxt.org

## Research (A)
- Aggarwal et al., "GEO: Generative Engine Optimization", KDD 2024: https://arxiv.org/abs/2311.09735 — quotations, statistics, cite-sources top methods (up to ~40% visibility gain); keyword stuffing ineffective. Caveat: benchmark of synthetic edits; real engines change.
- US v. Google trial testimony (Pandu Nayak) + 2024 Google API doc leak — NavBoost click signals: https://en.wikipedia.org/wiki/2024_Google_Search_documentation_leak

## Industry studies (B)
- Vercel × MERJ — AI crawlers don't execute JS (500M+ GPTBot fetches), Dec 2024.
- Ahrefs — 75k brands: brand mentions 0.664 vs backlinks 0.218 correlation with AI Overview visibility; YouTube mentions ~0.737 (Dec 2025).
- Ahrefs — AI Overview citations from top-10 pages fell 76% → 38%: https://ahrefs.com/blog/ai-overview-citations-top-10
- Ahrefs — schema added to 1,885 pages vs 4,000 controls: no significant AI-citation lift (2026): https://authoritytech.io/curated/schema-markup-ai-citations-ahrefs-study-2026
- Ahrefs — llms.txt, 137k domains, 97% zero requests (2026): https://nohacks.co/episode/229-does-llmstxt-work-what-137000-domains-server-logs-show
- Seer Interactive — 87% SearchGPT citations match Bing top results (2024).
- OtterlyAI 1M+ citations; 5W 680M citations; ~11% ChatGPT/Perplexity domain overlap (2026): https://otterly.ai/blog/the-ai-citations-report-2026/

## Small studies (C)
- llms.txt server-log studies: https://saaslinks.net/blog/llms-txt-server-log-study , https://wp.awrshift.com/llms-txt-in-practice/
- Mark Williams-Cook (Feb 2026): ChatGPT/Perplexity read JSON-LD as plain text.

## Books (for the human, not loaded by the skill)
- *The Art of SEO*, 4th ed. — Enge, Spencer, Stricchiola (O'Reilly, 2023). The reference textbook: crawling, architecture, technical.
- *Product-Led SEO* — Eli Schwartz (2021). Strategy: build pages around what users actually need, not keyword lists.
- *SEO Workbook* — Jason McDonald (yearly editions). Practical checklists.
- Google's *SEO Starter Guide* + *Search Quality Rater Guidelines* — free, primary, more authoritative than any book on what Google wants.

## Skills / tools landscape
- **claude-seo** (AgriciDaniel, MIT, ~18k★, v2.4.2 Oct 2026) — most-starred SEO skill; live-URL audits incl. `/seo geo` and `/seo agentic`. Installed locally as `seo` but an OLD copy (Mar 2026, 3 of 26+ sub-skills). Update: `/plugin marketplace add AgriciDaniel/claude-seo` then `/plugin install claude-seo@agricidaniel-claude-seo`.
- **geo-seo-claude** (zubair-trabzada, ~11k★) — GEO-first audits.
- **marketingskills** (Corey Haines) — installed: `marketing-skills:ai-seo`, `seo-audit`, `schema`, `programmatic-seo`, `site-architecture`.
