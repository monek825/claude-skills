# JSON-LD schema

Rules (Google structured-data guidelines):
- Only mark up what's visible on the page. Hidden or contradicting schema = manual-action risk, and Google says AI features need "structured data matches the visible text".
- One `@graph` per page, linked by `@id`s. Put Organization/WebSite in every page's graph (or at least home).
- No fake `aggregateRating`/`review` — self-serving reviews of your own business aren't eligible for stars anyway.
- Validate: https://validator.schema.org and Google Rich Results Test. `check_seo.py` only checks the JSON parses.
- Expect correctness + rich results + entity clarity (Bing says it helps Copilot understand pages), not a citation boost by itself.

## Base graph (every site)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#org",
      "name": "Brand Name",
      "url": "https://example.com/",
      "logo": "https://example.com/logo.png",
      "description": "Factual one-liner, same as About page.",
      "sameAs": [
        "https://www.instagram.com/brand",
        "https://www.linkedin.com/company/brand",
        "https://maps.google.com/?cid=XXXXXXXX"
      ],
      "contactPoint": {"@type": "ContactPoint", "telephone": "+62-812-0000-0000", "contactType": "customer service", "availableLanguage": ["id","en"]}
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com/",
      "name": "Brand Name",
      "inLanguage": "id-ID",
      "publisher": {"@id": "https://example.com/#org"}
    },
    {
      "@type": "WebPage",
      "@id": "https://example.com/page/#webpage",
      "url": "https://example.com/page/",
      "name": "Page title",
      "isPartOf": {"@id": "https://example.com/#website"},
      "about": {"@id": "https://example.com/#org"},
      "dateModified": "2026-10-05"
    }
  ]
}
</script>
```

`sameAs` is the entity glue: every real profile (Instagram, LinkedIn, GBP, Tokopedia, YouTube, Wikidata if any). It's how engines connect off-site mentions to this site.

## Swap Organization for a more specific type when it fits

Local business (has premises/serves an area) — use the most specific subtype: `Restaurant`, `CafeOrCoffeeShop`, `Bakery`, `MovingCompany`, `AutoRepair`, `SportsActivityLocation`, `NGO`, etc.

```json
{
  "@type": "Restaurant",
  "@id": "https://example.com/#org",
  "name": "Brand Name",
  "image": "https://example.com/photos/storefront.jpg",
  "address": {"@type": "PostalAddress", "streetAddress": "Jl. Contoh No. 1", "addressLocality": "Surabaya", "addressRegion": "Jawa Timur", "postalCode": "60000", "addressCountry": "ID"},
  "geo": {"@type": "GeoCoordinates", "latitude": -7.25, "longitude": 112.75},
  "telephone": "+62-812-0000-0000",
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "21:00"}],
  "priceRange": "Rp25.000–Rp80.000",
  "servesCuisine": "Indonesian",
  "menu": "https://example.com/menu/",
  "url": "https://example.com/"
}
```

Nonprofit: `NGO` (or `Organization` + `nonprofitStatus`), add `foundingDate`, `founder`, `areaServed`.

## Per page type

Service page:
```json
{"@type": "Service", "name": "Jasa Pengiriman Kargo Surabaya–Jakarta", "provider": {"@id": "https://example.com/#org"}, "areaServed": "Indonesia", "serviceType": "Freight shipping", "description": "Same as visible intro."}
```
Add `offers` with `price`/`priceCurrency: "IDR"` only if the price is on the page.

Product: `Product` with `name`, `image`, `description`, `brand`, `offers` (`price`, `priceCurrency`, `availability`). Needed for merchant listings.

Article/blog: `Article` or `BlogPosting` with `headline`, `datePublished`, `dateModified`, `author` (`Person` with `url` to an author page), `image`.

Breadcrumbs (any page below level 1):
```json
{"@type": "BreadcrumbList", "itemListElement": [
  {"@type": "ListItem", "position": 1, "name": "Beranda", "item": "https://example.com/"},
  {"@type": "ListItem", "position": 2, "name": "Layanan", "item": "https://example.com/layanan/"}
]}
```

FAQ: `FAQPage` markup is fine to keep (harmless, machine-readable) but Google shows FAQ rich results only for well-known government/health sites since Aug 2023. The visible Q&A is what matters.

Events: `Event` with `startDate`, `location`, `offers` — gets event rich results; worth it for clubs/venues (Whitestone, BRIDGE-type events).

Video: `VideoObject` with `name`, `description`, `thumbnailUrl`, `uploadDate`, `contentUrl` or `embedUrl`.

Skip: `HowTo` (rich result removed 2023), `SpecialAnnouncement`, `sitelinks searchbox` (retired 2024).
