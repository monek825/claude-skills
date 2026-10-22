---
name: site-build
description: Build or upgrade a target website project to premium quality using one research kit from ~/design-library/kits/ (single-kit path; synthesis library does not exist yet). Trigger on /site-build <project-path> [kit-slug], "apply the <slug> kit", "make this site premium using the kit". Enforces tokens-first layer order, mandatory browser verification at 375/768/1440, and UNVERIFIED status until fresh screenshots exist.
---

# site-build

Take a target website project and one research kit from `~/design-library/kits/<slug>/` and
implement the target to the kit's premium quality bar — then verify visually. This exists
because agents read good research prose and still ship generic "AI-looking" sites, then call it
done without looking at the result. Looking at the result is not optional here.

Single-kit path only: the design-library synthesis layer (cross-kit pattern merging) does not
exist yet. If the user hands you multiple kit slugs, pick the one closest to the target's
archetype and say so — do not attempt to merge kits.

Archetype not decided yet? See `_shared/inspiration-intake.md` before picking a kit — mood
references only, never a substitute for a kit's measured evidence.

## Phase 1 — Understand (no code yet)

1. **Inspect target**: framework/build system, CSS architecture (files, methodology, existing
   custom properties), how styles load and in what order, existing sections/components
   inventory. If a preview server will be needed later, read the project's `.claude/launch.json`
   for exact server names now — never guess server names, that's a hard rule, not a suggestion.
2. **Kit gate**: read `kits/<slug>/manifest.json`. Completeness score below 7/10, or
   `motion.md`/`screenshots/` missing → stop, tell the user to run `/site-research` (upgrade
   mode) on that kit first. Do not proceed on an incomplete kit and hope for the best.
2a. **Archetype match check**: read the kit's `primary_style_archetype` (and any
   `secondary_style_archetypes`) from the manifest against `_shared/style-archetypes.md`.
   Compare it to the target's actual business goal/brand (from the brief, existing content, or
   the user's stated intent). Close or complementary match → proceed, no comment needed. Real
   mismatch (e.g. a warm community-trust brand built from a pure Jensen-Huang enterprise-SaaS
   kit) → this must be named in the order sheet (step 4) before any code, with an explicit
   decision: adapt tone/warmth while keeping only the kit's structural/technical patterns, or
   proceed as-is because the user confirmed the mismatch is intentional.
2b. **Font Hub resolution** (always run, not optional). Font Hub = `library/foundations/
   typography.md`.
   - Signal source: target's brief/existing content/stated brand words (preferred). Fall back
     to the kit's `design.md` character description only if the target gave nothing to go on.
   - If the kit's own font is (a) free and already self-hosted as a `.woff2` under
     `specimen/fonts/`, (b) not one of the licence-flagged demo faces below, and (c) fits the
     target's brand words on a quick sanity check → reuse it verbatim, no further Hub work.
     Note "kit font reused, licence clear" in the order sheet and stop here.
   - Otherwise (kit font is licensed/scraped/missing, or mismatched to the target's actual
     brand) → run `typography.md` §Font Brief Personality Rating: score the target's brand
     words -2..+2 on the 8 axes, show the scores for a one-line confirm, compute distance to
     each of the 6 presets, take the lowest, then pick a pairing from that archetype's Approved
     Font Pools/Pairing Matrix (first-listed row is the default unless you name a reason to pick
     another).
   - **Hard exclusion — never select any file sitting in `specimen/fonts/` or `hub/fonts/` that
     is not a row in the Pairing Matrix.** That specifically rules out `Gero-Demo`,
     `Kunatic-Demo`, `Veggie-Demo`, `UnekoBold-Demo`, and `Orion-Regular` — all demo/
     personal-use-only faces per typography.md §Installed display faces. A client build is
     commercial use; their licences bar that outright, no exceptions.
   - Log in the order sheet: the brand's 8 axis scores, winning preset + distance, chosen
     pairing ID, and why — same provenance rigor as `/site-director`'s `DESIGN-PROVENANCE.md`.
3. **Kit read order** (trust order, read in this sequence and justify why in one line to
   yourself before moving on):
   1. `manifest.json` — what's actually in the kit and its completeness gaps
   2. `uncertainties.md` — read this FIRST of the content files, so you know what NOT to
      trust before you read anything that sounds like a fact
   3. `tokens.css` — real numeric values
   4. `design.md` — measured foundations (type scale, spacing scale, grid, palette)
   5. `motion.md` — numeric motion spec
   6. `media.md` — art-direction rules
   7. `components.md` — recurring component measurements
   8. `sections/*.md` — only the sections relevant to the target's actual pages
   Values marked `UNSOURCED` in tokens.css/design.md, or listed in `uncertainties.md`, are
   **not implementable as fact**. Either verify them live (open the kit's source URL, inspect
   computed styles) or choose a defensible default — and log which you did in the final verdict.
4. **Write the order sheet before any code**: `<target>/evals/order-sheet.md`. This is the
   mapping file — no code changes happen without it existing first.
   - Which kit tokens map to which target selectors/files (name the target file).
   - Which target sections adopt which kit section patterns.
   - Which kit `motion.md` rows apply where in the target.
   - What in the target stays untouched, and why.
   - If step 2a found an archetype mismatch, state it here first, with the decision made.
   - Step 2b's font resolution: axis scores, winning preset + distance, chosen pairing ID.
   - State the buyer-type depth call per `_shared/conversion-principles.md` (simplify
     aggressively for a simple/cheap offer vs. allow more proof/sections for expensive/B2B/
     medical/enterprise) — this can override the kit's default density, say so if it does.
   - Every entry cites kit values verbatim — numbers, not adjectives ("hero gap
     `clamp(6rem, 4rem + 8vw, 12rem)` from kit design.md §Spacing", not "generous spacing").
   No order sheet = no build. If you find yourself editing CSS before this file exists, stop
   and go write it.

## Phase 2 — Build (strict layer order; verify each layer holds before starting the next)

1. **Tokens first.** Port kit tokens into the target's token layer. Adapt names to the
   target's existing conventions; keep values verbatim from the kit's `tokens.css`. Respect the
   kit's breakpoint model exactly (e.g. Vantara kit: mobile-first `min-width: 768px/1200px`, not
   desktop-first `max-width`) — mixing breakpoint models silently breaks the cascade.
2. **CSS conflict sweep before injecting anything.** Grep the target for: colliding
   custom-property names, selectors that already target the same elements, higher-specificity
   rules that would swallow the new styles, import/cascade order issues. Fix collisions by
   namespacing or consolidating the property — never by reaching for `!important`.
3. **Components second.** Buttons, links, cards, nav primitives, built on the new tokens.
   Hover/focus/active states designed per the kit (e.g. multi-speed hover patterns) — a
   component that only has a default state is unfinished, not "good enough for now." Optional:
   scout an existing implementation first (21st.dev, CodePen, shadcn) — see
   `_shared/component-scouting.md`. Strip its tokens and rebuild from the kit's numbers; never
   paste it in with its own theme intact.
4. **Sections third.** Recompose target sections per the kit's section patterns: layout grid,
   spacing rhythm, type-scale contrast, section-flow/surface alternation. Adapt to the target's
   real content — never force a kit's content shape (e.g. a 4-image collage) onto content that
   doesn't have four images. Note misfits in the verdict instead of inventing filler content.
5. **Motion fourth.** Implement from `motion.md` rows verbatim: durations, easings, staggers,
   triggers. Must add `prefers-reduced-motion` handling even if the kit's source site never had
   it — that gap doesn't carry forward. Animate compositor-friendly properties only
   (`transform`, `opacity`, `clip-path`); no `width`/`height`/`top`/`left` animation.
6. **Media/art-direction.** Apply the kit's treatment rules — overlay/scrim alpha values,
   full-bleed vs. contained, type-over-media rules, aspect ratios — to the target's *own*
   imagery. See the theft rule below before touching any asset. If the target's imagery can't
   meet the kit's bar, see `_shared/visual-storytelling.md` before defaulting to generic stock.

## Hard rules

- **Adapt, don't clone.** The kit supplies measurements, patterns, and a quality bar. The
  target keeps its own brand, copy, imagery, logo, voice. Never copy the kit's source-site copy
  verbatim, never reuse its logos/photos/videos, never redistribute a scraped/licensed font
  (e.g. Vantara's `gt_ultra_median_light.woff2` is licensed) — resolve the replacement through
  step 2b's Font Hub process, not an ad hoc guess, and say what was substituted in the verdict.
- **Kit is read-only.** Never edit files under `kits/<slug>/` during a build.
- **Copy is content, not layout filler.** Use the target's real copy, or `site-director/PAGE-COPY.md`
  when it exists. If a section needs text that does not exist, invoke `marketing-skills:copywriting`
  (brief it with the target's audience + one conversion goal) and run `stop-slop` on the draft —
  never lorem, never a kit-shaped headline written to fill a slot, never invented numbers,
  testimonials or logos. Unfillable copy is a verdict note, not an improvisation.
- **Site name stays short.** `<title>`, header wordmark, and footer credit use the business
  name only — a few words, no em-dash tagline (`Brand — Category, City`). Category/location
  descriptors belong in `<meta name="description">` or the hero subhead, not the name itself.
- **Anti-generic gate.** Before moving from Phase 2 into Phase 3, self-check the build against
  the anti-pattern checklist in `_shared/rubric.md`. Any hit gets fixed now, not explained away
  in the verdict later.
- **Conversion gate.** Same checkpoint, also run the checklist in `_shared/conversion-principles.md`
  (hero clarity, CTA visibility/specificity, social proof placement, motion not competing with
  the CTA, load speed, buyer-type depth). **Clarity wins** — a build that scores well on
  `rubric.md` but fails this checklist is not ready for Phase 3; fix the conversion problem
  first, don't let premium visuals ship over it.
- **Uncertain values stay uncertain.** Nothing listed in the kit's `uncertainties.md` gets
  implemented as if it were a measured fact.
- **3D/WebGL/shaders are out of scope.** Frontier-tier, not part of this skill. If a kit's
  source site uses them, note the gap in the verdict — don't attempt mid-build.

## Phase 3 — Verify

Follow `_shared/verification.md` protocol A exactly — do not re-derive or paraphrase it here:

- Fresh, same-session screenshots at 375/768/1440px into `<target>/evals/`.
- Run the `slop-judge` agent on the built page; its `evals/slop-judge.md` verdict must be PASS
  (or PASS WITH LIMITATIONS) before this build can be VERIFIED. Cite it in `evals/verdict.md`.
- Score every section against `_shared/rubric.md`, axis by axis.
- Write `evals/verdict.md` using the rubric's verdict template: name the weakest section with
  px-level specifics, list remaining gaps, cite screenshot evidence against the kit's own
  `kits/<slug>/screenshots/` as the comparison baseline.
- Repair loop: max 3 iterations, per `verification.md`. After 3, the honest verdict stands —
  do not inflate a score to close the loop.

**Status vocabulary: UNVERIFIED or VERIFIED. Nothing else.** No fresh screenshots taken this
session = UNVERIFIED = the words "done" and "finished" are banned in your response. Say so
bluntly rather than softening it.

## Outputs in target project

- `evals/order-sheet.md`
- `evals/full-{375,768,1440}.png` (+ per-section shots as needed)
- `evals/verdict.md`
- The actual code changes (tokens, components, sections, motion, media).

## Subagent routing (frugal-fable style)

| Slice | Model | Why |
|---|---|---|
| Kit selection, order sheet, final verdict | Orchestrator | Judgment calls, not delegable |
| Bounded component/section implementation from the order sheet | Sonnet | Mechanical once the order sheet is written |
| Screenshot capture | Haiku/Sonnet | Mechanical browser driving |
| Final visual judgment + repair decisions | Orchestrator | Never delegate — this is the check the whole skill exists to enforce |
