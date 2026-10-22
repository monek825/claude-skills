# Technical baseline

Ship all of this on every site. Templates are copy-ready; replace `example.com`.

## robots.txt (site root)

Default for Bray's business sites: allow everything, including AI search AND training (visibility is the goal; small businesses gain from being in model knowledge). Only switch training off if the client asks.

```txt
# Search + AI search/answer bots: allowed (default *)
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /*?*sort=
# Keep CSS/JS crawlable — Google renders pages with them.

Sitemap: https://example.com/sitemap.xml
```

Opt-out of model TRAINING only, keep AI search visibility:

```txt
User-agent: GPTBot
Disallow: /
User-agent: ClaudeBot
Disallow: /
User-agent: Google-Extended
Disallow: /
User-agent: Applebot-Extended
Disallow: /
User-agent: CCBot
Disallow: /
User-agent: Meta-ExternalAgent
Disallow: /

User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

Never put these in a Disallow if you want AI visibility: `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `Googlebot`, `Bingbot`, `Applebot`. Full bot table: ai-search.md.

Rules:
- robots.txt controls crawling, not indexing. To keep a page out of results use `<meta name="robots" content="noindex">` and let it be crawled.
- Don't block a URL you also noindex — the bot never sees the noindex.
- Staging/preview deploys: `noindex` header (`X-Robots-Tag: noindex`) or auth, never the production robots.txt.

## sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2026-10-05</lastmod>
  </url>
</urlset>
```

- Only canonical, 200, indexable URLs. No redirects, no noindex, no params.
- `lastmod` = real content change date (Google uses it only if it's consistently accurate). Skip `priority`/`changefreq` — Google ignores them.
- Generate it from the route list at build time (Flask: a `/sitemap.xml` route over known URLs; static: a small script; Next: `app/sitemap.ts`). Don't hand-maintain past ~10 pages.

## `<head>` per page

```html
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Primary topic — Qualifier | Brand</title>
  <meta name="description" content="One or two sentences that answer the query and say why this page.">
  <link rel="canonical" href="https://example.com/page/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Primary topic — Qualifier">
  <meta property="og:description" content="Same promise as meta description.">
  <meta property="og:url" content="https://example.com/page/">
  <meta property="og:image" content="https://example.com/og/page.jpg"><!-- 1200x630 -->
  <meta property="og:locale" content="id_ID">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="icon" href="/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <script type="application/ld+json">{ ... see schema.md ... }</script>
</head>
```

Favicon matters: Google shows it next to results; AI answers show it next to citations.

## Rendering (the AI-crawler trap)

Vercel × MERJ (500M+ GPTBot fetches) found no major AI crawler executes JavaScript — GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Meta, Bytespider. Googlebot (and so Gemini/AI Overviews) and Applebot do render.

- Static HTML / Flask templates: fine by default.
- Vite/React SPA: prerender every route (`vite-plugin-prerender`/`vite-ssg`, or `react-snap`-style), or move to SSR/SSG (Next/Astro). An empty `<div id="root">` = invisible to ChatGPT/Claude/Perplexity.
- Content in tabs/accordions/carousels: put it in the HTML, hide with CSS — not fetched on click.
- Test: `curl -s URL | sed 's/<[^>]*>//g' | wc -w` should show the page's real copy. check_seo.py does this.

## URLs, status codes, redirects

- Short, lowercase, hyphenated, human words: `/jasa-pengiriman-surabaya/` not `/page?id=7`.
- Pick one host (`https://` + www or apex) and 301 the others. One trailing-slash style.
- Real 404 status for missing pages (not a 200 "not found" page). Custom 404 with links home.
- Moving a page: 301 old → new, update internal links and sitemap.

## Headers worth setting (host config: `_headers`, `vercel.json`, Flask `after_request`)

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Content-Signal: search=yes, ai-input=yes, ai-train=yes   # optional, Cloudflare's content-signals proposal; not a standard
```

Cache static assets long (`Cache-Control: public, max-age=31536000, immutable` on hashed files), HTML short.

## Images and media

- `alt` describes the image for someone who can't see it; include the subject naturally, no stuffing.
- Hero/LCP image: `fetchpriority="high"`, no lazy-load. Everything else `loading="lazy"`.
- Real photos of the real business beat stock — they're also E-E-A-T evidence.
- Video: host on YouTube too (YouTube mentions were the strongest single AI-visibility correlate in Ahrefs' Dec 2025 data) and embed with `VideoObject` schema.

## International / bilingual (Indonesian + English sites)

Only if both languages are real full translations:

```html
<link rel="alternate" hreflang="id" href="https://example.com/">
<link rel="alternate" hreflang="en" href="https://example.com/en/">
<link rel="alternate" hreflang="x-default" href="https://example.com/">
```

Every page lists all variants including itself, both directions. Separate URLs per language (subfolders); never swap language with JS on one URL.
