---
name: hero-layouts
description: Choose researched hero layouts and compose brand-fitting visuals for Bray's website demos. Use before hero design or review; Breq F&B work requires approved-reference visual/UX QC, source-grounded assets within current permissions, varied layouts and typography.
---

# Hero layouts

Design composition and imagery together. For Breq's F&B outreach, a good grey-box layout or a pack on an empty colour field is not enough: the visual scene must meet Bray's approved food-hero standard.

## Mandatory Breq F&B quality gate

7 October production update: follow HERO-UX-GATE.md's current daily-F&B permission for product-referenced generated campaign backgrounds and food pieces. Use the imagegen skill/tool when generating or editing raster scenes. Inspect the visual BEFORE implementation; choose a clean, softly lit studio stage with relevant pieces or a restrained realistic scene, not a weak pack on an empty colour field. Reserve photographic whitespace for copy on both sizes. Require actual approved-reference comparisons, mobile art direction and batch layout/font variation; technical rendering alone cannot pass. This supersedes older real-only and batch-only advice within the documented F&B scope, not truthfulness or human send approval.

For Breq hero copy, navigation, CTA or mobile changes, also read `/Users/brayden/Documents/Website Business/design/hero-layouts/HERO-UX-GATE.md`. Enforce task clarity, verified destinations, mobile browsing, contrast/touch/focus checks and optimized scene delivery separately from visual approval. It records Bray's current generated-F&B-scene permission; older real-only advice yields only within that documented scope.

Read `/Users/brayden/Documents/Website Business/design/hero-layouts/FNB-QUALITY-CONTROL.md` and open its approved desktop/mobile reference PNGs before food-demo work. Follow its scene, real-asset, layout/font variation and side-by-side review gates before calling a hero finished. It overrides older advice below when they conflict. The 4 October Lanting pilot is rejected, not an approved benchmark. Do not count unfinished or visually weak demos toward the daily completed quota.

Before reporting a hero demo as internally passed, also run the `slop-judge` agent on its HTML (it captures 1440/375 and compares against the Supahero tier-A and Minimal Gallery food boards). Its verdict is evidence for internal QC, not a substitute for Bray's approval.

## Where it is
```
/Users/brayden/design-library/hero-layouts/
  CATALOG.md            ← the taxonomy: ID, skeleton, sources, asset needs, industry fit. READ FIRST.
  templates/hl-NN-*.html ← one self-contained file per layout (CSS only, tokens, [data-slot] pieces)
  thumbs/hl-NN-{desktop,mobile}.png, thumbs/_sheet.png ← previews
  TEMPLATE-CONTRACT.md  ← how templates are built (tokens, retune rule, mobile rule)
  research/records/*.json + research/shots/ ← the 112 measured source heroes (evidence)
  user-concepts/        ← Bray's original 8 Canva concepts (taste reference)
render: cd …/hero-layouts && ~/.venvs/scrapling/bin/python render_thumbs.py hl-NN [--sheet]
sync_hub.py + VERIFIED.txt ← publishes verified templates to the component hub gallery (add an id to VERIFIED.txt, re-run)
```
Also browsable in the component hub gallery (http://localhost:4177/gallery.html, filter "hero layout").

## Read first
`~/design-library/hero-layouts/LAYOUT-FIT.md` — which layout fits which industry, the image-grade gate, font/colour by company vibe, and Bray's review of batch 2 (only Indoprima v3 passed). It overrides CATALOG.md's Fit column.

## What is usable
Only ids listed in `VERIFIED.txt` are reviewed (desktop + mobile checked). CATALOG.md also lists rows above HL-39 from a later expansion — many have no template yet, and built ones are unreviewed until added to VERIFIED.txt. Pick from verified ids; if an unverified row is the best fit, render its thumbs and review it against the house rules first.

## Picking (do this, don't freehand)
1. **Inventory the client's real assets** — cutout/transparent product (C)? landscape photo (P)? portrait (Pt)? ≥4 SKUs (R)? ≥6 photos (G)? nothing (T)? A logo that works huge? Brand name length? Plan only around assets available or a permitted campaign scene you will produce and inspect before implementation.
2. Filter CATALOG by Assets, then by Fit.
3. Shortlist two distinct, asset-fitting compositions. For F&B, follow the quality-control batch variation plan rather than repeating a default layout. Suggestions, subject to the image-grade gate:
   - Snack / F&B with pack shots: HL-11 product-through-word, HL-25 pedestal, HL-22 colour bands (flavours) / HL-38 product grid half / HL-12 panel+cutout.
   - F&B with only kitchen/founder photos: HL-09 masthead+portrait, HL-10 wordmark band+photo, HL-37 colour half+card.
   - Logistics / trucking / industrial: HL-03 band, HL-13 bottom-bleed over photo, HL-33 inset frame+rail, HL-29 oversize crop, HL-19 staircase.
   - Software / ERP: HL-39 device triptych, HL-31 hairline grid, HL-32 crosshair, HL-14 clipped wordmark.
   - No usable photos: research permissible assets or produce an authorized product-referenced campaign scene; hold if product identity cannot be verified. Do not substitute type-only heroes.
4. Record layout/source, font rationale, scene route and the closest approved quality benchmark.

## Adapting a template
1. Copy the template into the project; keep the header comment until done.
2. Set tokens: `--ground --ink --accent --field-*` from the client's logo/packaging (extract, don't guess); fonts via `--font-display/--font-body` (≤2 families).
3. **Retune the wordmark** for the real name using the rule in the header (font-size vw ≈ span ÷ (ink_em − tracking×(letters−1))). It must span the same width as the template and never wrap. Long names (>12 letters): use the short form or a layout that tolerates it (see CATALOG rule 3).
4. Replace every `.ph` with the real asset at the same box; cutouts must be real transparent PNG/WebP (strip baked shadows).
5. Real copy only (facts from the client's own pages). Placeholder GreenLeaf text must be gone — grep `GreenLeaf`.
6. Check 1440×900, 1280×800, 1920×1080, 390×844. Signature element must survive on mobile.
7. Load `website-house-rules` before calling it done.

## Rules
- Layouts are skeletons: never copy a source site's content, logo, colours, imagery or brand font.
- No universal default font pairing. Select licensed typefaces appropriate to the brand, vary display treatments across the batch, and preserve readability. Agrandir requires a suitable commercial licence.
- Awards/laurels (HL-07/08) only with real awards or certifications — otherwise delete that row.
- Motion is separate: pair with component-hub entries (feather word reveal, hero letter rise, WD fixed banner) only after the static layout is right. No WebGL in the hero if anything else heavy is on the page.
- New layout found? Add a record to research/records/, a row to CATALOG.md, a template + thumbs, and a hub entry (component-hub skill "adding an entry").
