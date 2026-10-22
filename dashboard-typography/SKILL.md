---
name: dashboard-typography
description: Research-backed font selection and type-scale setup for dashboards, data-dense UIs, and general websites. Use when starting a new site/dashboard, choosing fonts, defining a type scale, or auditing existing typography for readability. Triggers on "font size", "type scale", "typography", "which font", "text too small", "dashboard fonts".
---

# Dashboard & Web Typography

Evidence-based rules for picking typefaces and sizes. Sources: NN/g glanceable-text research, WCAG 2.2, Material Design 3, IBM Carbon, Apple HIG, PMC legibility meta-review (2023), Kolokolov dashboard standards. Full citations at bottom.

## Step 1 — Classify the surface

| Surface | Base body size | Why |
|---|---|---|
| Data-dense dashboard / admin tool | **14px** | Carbon "productive" set base; density matters |
| Marketing / editorial site | **16–18px** | Sustained reading; NN/g + WCAG industry practice |
| Mobile-first | **16px min** | Prevents iOS zoom-on-focus; Apple HIG 17pt body |
| Wall display / TV | scale by distance | Visual angle ≥0.3°: size_pt ≈ distance_cm × 0.05 per the VAF formula (5.73 × size/distance) |

## Step 2 — Pick fonts (2 max, 3 absolute ceiling)

**Hard rules from research:**
- Sans-serif, **regular width** — condensed faces cost +11.2% reading time (NN/g); never use condensed/narrow fonts for body, labels, or numbers.
- Regular (400) body weight — never thin/light in dense layouts.
- Numbers that align in columns need **tabular figures** (`font-variant-numeric: tabular-nums`) or a mono font.

**Proven picks (all free, Google Fonts unless noted):**
| Role | First choice | Alternatives |
|---|---|---|
| Data UI / dashboard | **Inter** | IBM Plex Sans, Public Sans, Roboto |
| Numbers / plates / IDs | IBM Plex Mono | JetBrains Mono, tabular-nums on the sans |
| Editorial headings | Fraunces, Newsreader | Source Serif 4 |
| Zero-download (perf) | system stack: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` | fine for body; research endorses system fonts |

Pairing rule: one workhorse sans for UI + one contrast font (mono for data UIs, serif for editorial). Load only needed weights (400/500/600/700 max), `display=swap`, preload only the critical file.

## Step 3 — Type scale (define as CSS tokens, rem units)

Dashboard/productive scale (px shown; write as rem, ÷16):

| Token | px | Use |
|---|---|---|
| fs-12 | 12 | **Floor.** Axis ticks, legends, fine print. Nothing below 12px except chart-internal axis labels (11px absolute floor per Kolokolov's 8pt = screen-edge case, avoid). |
| fs-13 | 13 | Secondary labels, table headers, captions |
| fs-14 | 14 | Body, table cells, feed text (Carbon base) |
| fs-16 | 16 | Card/section headers, emphasized body |
| fs-20 | 20 | Panel titles, small stat numbers |
| fs-24–28 | 24–28 | KPI card numbers (Kolokolov 24–28pt) |
| fs-32–48 | 32–48 | Page hero number / display (consensus 28–48) |

Editorial sites: same idea, base 16–18, ratio 1.2–1.25 up the scale.

**Line-height:** 1.5–1.6 body (WCAG floor 1.5), 1.3–1.4 headings, 1.1–1.2 big KPI numbers.
**Weights:** 400 body, 500 labels/emphasis, 600–700 headings and KPI numbers.
**Case:** sentence case default. ALL-CAPS only for very short labels (≤2 words, with letter-spacing). Never long all-caps or all-lowercase glanceable text (26% slower, NN/g).

## Step 4 — Verify (do, not skim)

- [ ] No text below 12px (grep the CSS for the tokens; check computed sizes in charts)
- [ ] Body line-height ≥1.5; rem/em units throughout (WCAG 1.4.4: must survive 200% zoom without loss)
- [ ] Text contrast ≥4.5:1 (AA); large text (≥24px or ≥18.66px bold) ≥3:1
- [ ] Columns of numbers use tabular figures
- [ ] No condensed/thin fonts anywhere users read at a glance
- [ ] Screenshot at 1440 and 375; nothing truncates after size bumps

## Sources

- NN/g glanceable fonts: https://www.nngroup.com/articles/glanceable-fonts/
- WCAG resize text: https://www.w3.org/WAI/WCAG21/Understanding/resize-text.html
- Material 3 type scale: https://m3.material.io/styles/typography/type-scale-tokens
- IBM Carbon type sets: https://carbondesignsystem.com/guidelines/typography/type-sets/
- Apple HIG typography: https://developer.apple.com/design/human-interface-guidelines/typography
- Legibility meta-review (visual angle): https://pmc.ncbi.nlm.nih.gov/articles/PMC9376262/
- Data-viz font choice (Muth): https://nightingaledvs.com/choosing-fonts-for-your-data-visualization/
- Kolokolov dashboard sizes: https://www.linkedin.com/posts/askolokolov_how-to-choose-font-size-for-dashboard-activity-7308118437740883969-GFYH
- Raw research notes: references/research-notes.md
