---
name: site-director
description: One conductor for a full website production run — brief → research → design direction → imagery → component plan → build → visual audit. Coordinates the Research Hub, Font Hub, /site-research, /site-build, the local component library, and the ECC web rules WITHOUT merging or duplicating them. Trigger on /site-director <project-path>, "produce this website end to end", "run the full site workflow".
---

# site-director

Conductor, not a builder. It owns the **order of operations, the approval gates, and the
per-project paper trail**. Every phase delegates to a system that already exists; site-director
never re-implements research, token extraction, or the build+verify loop.

Each system stays its own source of truth. On conflict: a measured **kit** > a **hub** blueprint
> this skill's prose. Do not copy content between systems — reference it.

## Roles (fixed)

- **Opus 4.8 = orchestrator.** Runs this file, writes the brief/direction/audit judgments,
  operates the approval gates, gives final visual approval. Judgment is never delegated.
- **GPT-5.6 Codex** (`mcp__codex__codex`, `sandbox: workspace-write`, `cwd: <project>`) =
  implementer. Inspects the repo, writes files, builds the site, processes assets, captures
  screenshots. Give it the order sheet / token values; it does the mechanical work.
- **≤1 research scout** (Explore or a Haiku `general-purpose` agent) — only when fresh web or
  image research is genuinely needed. No Fable, no agent councils.

## Systems it calls (detect once, at start)

| System | Where | Used in phase |
|---|---|---|
| Website Research Hub | `~/design-library/hub/` (refs/patterns/blueprints; server `research-hub`) | 2 direction |
| Font/Typography Hub | `dashboard-typography` skill + `~/design-library/library/foundations/typography.md` (6 presets) + `specimen/fonts/*.woff2` | 2 direction |
| `/site-research` | skill — produces a measured kit in `~/design-library/kits/<slug>/` | 2 (required when no suitable measured kit exists) |
| `/site-build` | skill — kit → target build + verify at 375/768/1440 | 5 build, 6 audit |
| Local component library | `~/design-library/library/` (empty until ≥3 kits) + any project-local components | 4 component plan |
| `marketing-skills:copywriting` | plugin skill (+ `stop-slop`, `marketing-skills:copy-editing`) | 1 gaps, **4.5 copy** |
| ECC web rules | `~/.claude/rules/ecc/web/{coding-style,performance,security,design-quality,testing}.md` | 4, 5, 6 |
| shadcn | project `components.json` (present in `~/Documents/Website Business/Tier-A*`) | 4 component plan |
| Astryx | detect only; **not installed → never mention again** | 4 (skip) |

At start, run the detect step: check for a project `components.json` (shadcn), an `astryx` dep,
existing `src/components`, and `.claude/launch.json`. Record findings in `PROJECT-BRIEF.md` §Stack.

### Optional tool adapters (detect-only — never auto-install, never required)
site-director works fully without any of these. If one is **already installed** and clearly
earns its place, it may be used as a helper — its output inspected, never trusted on marketing:

| Tool | If present, used for | Guardrail |
|---|---|---|
| Impeccable | design-critique pass | advisory only; Opus's audit (Phase 6) still decides |
| Taste Skill | reference/aesthetic scoring | a lens, never overrides the approved direction |
| image-gen MCP | Phase 3 candidate generation | candidates only; Gate B + Asset Gate still apply |
| 21st.dev / component sources | Phase 4 component structure | structure/behaviour only; restyle to project tokens |

Rules: never install any of them here (like Astryx); do not require them; **never run multiple
overlapping design skills by default** — pick one helper for one job or none. The Research Hub
and the approved direction remain the single source of truth; a tool's output is a candidate to
inspect, not an answer to accept.

## Outputs (all under `<project>/site-director/`, except build artifacts)

```
<project>/site-director/PROJECT-BRIEF.md
<project>/site-director/CONTENT-GAPS.md
<project>/site-director/DESIGN-DIRECTION.md
<project>/site-director/DESIGN-PROVENANCE.md
<project>/site-director/DESIGN-TOKENS.json
<project>/site-director/IMAGE-PLAN.md
<project>/site-director/IMAGE-MANIFEST.json
<project>/site-director/COMPONENT-PLAN.md
<project>/site-director/PAGE-COPY.md
<project>/site-director/FINAL-AUDIT.md
<project>/site-director/comparison/   # TEMP direction/variation board — deleted before Phase 6
<project>/assets/image-inbox/     # user drop zone for manual/licensed assets
<project>/assets/images/          # optimized, in-use assets
<project>/evals/                  # /site-build writes order-sheet.md, screenshots, verdict.md here
```

Screenshots for the audit are `/site-build`'s `evals/full-{375,768,1440}.png` — do not duplicate.

---

## Phase 1 — Intake  →  PROJECT-BRIEF.md, CONTENT-GAPS.md

Determine: business + audience + **one** conversion goal; pages and real content; brand
personality (3–5 words); available assets (logos/photos/copy — inventory what actually exists);
technical constraints (framework, host, perf budget, launch.json). Codex inspects the repo; Opus
writes the brief.

- `PROJECT-BRIEF.md`: Business / Audience / Conversion goal / Pages / Brand personality /
  Assets on hand / Stack (detect results) / Constraints.
- `CONTENT-GAPS.md`: every piece of copy or fact the site needs but the project does not yet
  have — one row per gap, marked `blocking` or `fill-with-placeholder`. Never invent facts to
  paper a gap; list it.

## Phase 2 — Design direction (iteration ladder A→B→C)  →  DESIGN-DIRECTION.md, DESIGN-PROVENANCE.md, DESIGN-TOKENS.json  ·  🚦 GATE A, 🚦 GATE A2

Open the Research Hub (`cd ~/design-library/hub && node build-data.js && preview server
research-hub`). **Never one-shot from direction to final site.** Direction is a three-stage
ladder: broad directions → variations of the chosen one → refinement. Each of Stage A and Stage B
ends at a comparison board and a hard stop.

**Structured design input — every direction/variation documents these four, explicitly labeled:**
- **Aesthetic:** intended visual family + emotional tone.
- **References:** exact Hub reference IDs and URLs — and, per §"Reference-led body" below, which
  page region each reference informs (not just the hero).
- **Intent:** audience, the ONE conversion goal, and the required user action.
- **Guardrails:** required visual decisions and forbidden ones (what must not be copied/done).

**Reference-led body (applies to every direction):** references must cover the WHOLE page, not
just the hero. For each direction document a reference/pattern for each relevant region present:
navigation · hero · section transitions · long-form body rhythm · image galleries ·
curriculum/features · proof · CTA · footer · responsive behaviour. A strong hero over a generic
body fails the audit — Phase 6 checks this.

Font Hub: rate the brand on the 8-axis Font Brief rubric in `typography.md` §Font Brief
Personality Rating and pick the closest-distance preset — never a vibe pick. Each direction
uses ONE preset (heading + body + optional mono, ≤3 families). Copy its verbatim CSS stack,
weights, and clamp sizes. Use `dashboard-typography` to sanity-check base size vs surface
(14px dense / 16–18px marketing). Fonts come from `specimen/fonts/`. Log the 8 brand scores
and the winning preset's distance in `DESIGN-PROVENANCE.md`.

### Stage A — three broad directions  ·  🚦 GATE A
Produce **THREE genuinely different directions** — genuinely different composition, typography,
and imagery, not three flavors of one idea. Each includes the four structured fields above plus:
blueprint ID + pattern IDs, one Font Hub preset, layout structure, image/media direction, and one
lightweight visual composition/moodboard. Render them on the **comparison board** (see below).

**🚦 GATE A — stop. Present all three on the board and require explicit user approval of ONE
before Stage B. The agent MUST NEVER self-approve Gate A unless explicitly running in unattended
mode (user said so). Obvious fit is not approval.**

### Stage B — three variations of the approved direction  ·  🚦 GATE A2
Hold the approved direction's aesthetic, palette, and font preset fixed. Produce **THREE
variations** that differ in **section rhythm, layout structure, image scale, and typographic
treatment** — **never superficial color swaps** (same tokens, different composition). Render all
three on the comparison board, desktop + mobile.

**🚦 GATE A2 — stop. Present all three variations and require explicit user approval of ONE
before imagery (Phase 3) or refinement. Same self-approval rule as Gate A.**

### Stage C — refinement
Refine the approved variation only (spacing, scale, crops, motion weight). The optional **tweak
panel** (see below) may drive this; its final values are written into `DESIGN-TOKENS.json`. Then
proceed to Phase 3 imagery → Phase 5 build. No new composition invented here.

Kit vs blueprint (decides Phase 5's build path):
- Suitable MEASURED `kits/<slug>/` for the approved direction → validate completeness ≥7/10
  against `_shared/verification.md` §B, then build via `/site-build`. State the slug.
- No suitable measured kit → invoke `/site-research` for a project-specific kit and validate it
  to the same threshold **before** `/site-build`.
- Blueprint-only builds are allowed only as clearly labeled **rough prototypes**. They can never
  receive a premium or final PASS verdict.

- `DESIGN-DIRECTION.md`: all three directions, the approved direction + build path, then all three
  variations and the approved variation.
- `DESIGN-PROVENANCE.md`: references consulted; blueprint/pattern/font IDs used **plus the
  Font Brief 8-axis brand scores and the winning preset's distance**; the decision derived
  from **each** source, per page region; rejected references + reasons.
- `DESIGN-TOKENS.json`: `{ fonts, type_scale, color, space, radius, motion }` — real values only
  (hex, clamp(), rem, ms), each traceable to the blueprint/kit/preset it came from. Composition
  knobs that vary per Stage-B variation live here; final values are set after Stage C.

### Visual comparison board (temporary tooling, reused in Stage A and Stage B)
A throwaway local page at `<project>/site-director/comparison/index.html` showing every
direction/variant in ONE view. Requirements:
- Each preview in a **sandboxed `srcdoc` iframe** so its CSS cannot leak (mirror the Design
  Gallery's isolation pattern in `~/design-library/hub/gallery.*` — do not reinvent it).
- **Desktop + mobile** frame per option (1440 scaled + 375).
- For each option: exact reference IDs and the tokens used; **strengths, risks, implementation
  complexity**; a selection control (radio/label — records the pick, does not need a backend).
- Regenerated per stage. **Deleted before Phase 6** (the audit checks it is gone).

### Tweak panel (optional, Stage C only, dev-only)
Only if refinement needs live tuning. A dev-only control panel exposing **only meaningful design
decisions** — heading font/size, body measure, section spacing, image scale + focal crop, accent
color, border/radius, motion weight + reveal distance, content density. Rules: expose the few
knobs that matter, **not dozens of arbitrary controls**; **never ship it in production**; on
approval, write final values into `DESIGN-TOKENS.json`; **remove the panel before the Phase 6
audit** (audit checks both removal and that panel choices became real tokens).

## Phase 3 — Image direction  →  IMAGE-PLAN.md, IMAGE-MANIFEST.json  ·  🚦 GATE B

**Sequence (strict):** no final imagery is generated or sourced during Stage A/B exploration —
directions and variations use designed placeholders only. Only after the Stage B variation is
approved: (1) write the image brief per image, (2) generate/source **multiple** candidates,
(3) show the candidates **in context** (dropped into the approved layout, not as loose tiles),
(4) approve ONE, (5) optimize and integrate locally. Real owned imagery stays preferred;
Pinterest/Dribbble/Behance are inspiration-only unless usage rights are confirmed.

Create `assets/image-inbox/` and `assets/images/`. For **each** image define: purpose + subject,
visual tone, aspect ratio, focal point / crop, desktop vs mobile treatment, exact filename,
source + licence status, essential | optional.

Sourcing priority — walk down until satisfied:
1. Client-owned assets (from Phase 1 inventory).
2. Licensed stock / public-domain (verify licence).
3. Manually supplied images.
4. Designed placeholders (CSS/SVG — built in Phase 5).

Pinterest / Behance = mood reference only, never shipped.

- `IMAGE-PLAN.md`: one section per image with the fields above + the priority tier chosen.
- `IMAGE-MANIFEST.json`: array of `{ filename, purpose, aspect, focal, desktop, mobile, source,
  licence, essential }`.

**🚦 GATE B — stop.** If suitable licensed/public-domain assets can be sourced safely, present a
**shortlist for approval before downloading anything**. Otherwise give the user exact
instructions: what to supply, the filename to save it as, and to drop it in
`assets/image-inbox/`. Designed placeholders may proceed without a download.

**🚦 ASSET GATE — before build, require ONE:** real product screenshots/video; owned brand
imagery; approved licensed assets; or an exact manual capture/download plan. For product sites,
prefer real product evidence over stock. Inspect the actual product app and request its needed
real states (for WhisperFlow: recording, transcription result, text pasted into a real writing
app, menu-bar state). **No emoji as production icons; no fabricated UI that misrepresents the
product; no generic terminal/dashboard decoration used as filler.**

## Phase 4 — Component plan  →  COMPONENT-PLAN.md

Source priority (pick ONE primary strategy for the project):
1. Existing project components.
2. Local component library (`~/design-library/library/` — empty until synthesis; skip if so).
3. shadcn — only if already set up (`components.json`) and compatible.
4. Astryx — only if already installed AND clearly suitable. **Never install it here.**
5. Custom components.

Rules: one primary strategy; do not mix shadcn + Astryx without a written reason; libraries give
structure/behaviour, the **blueprint controls visual direction**; no duplicate primitives, no
unused deps; every adopted component gets **restyled to the project tokens** (strip the library's
own theme). Follow ECC `coding-style.md` (tokens-first) and `design-quality.md` (anti-template).

- `COMPONENT-PLAN.md`: chosen strategy + why; component inventory (nav, hero, cards, buttons,
  code/kbd, footer…) each mapped to its source (existing / library / shadcn / custom) and the
  tokens it uses.

**🚦 GATE C — any new dependency or stack change (installing shadcn, adding a framework) is
presented for approval first. Never silently install tools.**

## Phase 4.5 — Copy  →  PAGE-COPY.md  ·  🚦 GATE D

Nothing user-facing gets written by the builder. Copy is produced here, approved, then handed to
Phase 5 as fixed content. Invoke `marketing-skills:copywriting` (Opus writes; never delegate copy
judgment to Codex) with PROJECT-BRIEF.md §Audience/§Conversion goal as its context — it covers
the gathering questions, so do not re-ask what the brief already answers.

Per page, in section order matching the approved variation: hero headline + subhead + primary CTA,
each section's one idea, body, CTA copy, plus `<title>` / meta description. One conversion goal
per page, one idea per section, specific over vague, customer language over company language.

Rules:
- **Copy is fixed before build.** Codex pastes `PAGE-COPY.md` verbatim; it invents no prose,
  no headline variants, no filler. Text the copy does not cover = a CONTENT-GAPS row, not an
  improvisation.
- **No fabricated proof.** Numbers, testimonials, logos, case studies, awards: sourced from the
  brief or listed `blocking` in CONTENT-GAPS.md. Never generated.
- Run `stop-slop` over the draft before presenting — no AI tells.
- Copy length constrains layout, not the reverse. Where the approved variation's section cannot
  hold the real copy, the section changes (note it in PAGE-COPY.md §Layout impact).
- Existing copy being rewritten → `marketing-skills:copy-editing` instead.

- `PAGE-COPY.md`: one section per page, copy blocks in section order, each annotated with the
  section it fills; a §Layout impact list; alternatives for the hero headline only.

**🚦 GATE D — stop. Present PAGE-COPY.md for approval before Phase 5. Copy is user-facing brand
voice; the agent never self-approves it outside explicit unattended mode.**

## Phase 5 — Build  →  source code (invoke /site-build)

Implementation cannot begin without `DESIGN-PROVENANCE.md` or before the Asset Gate passes. Approved
`PAGE-COPY.md` is equally a precondition — no lorem, no builder-invented headlines.

- **Kit path:** use the approved direction's suitable MEASURED kit, or invoke `/site-research`
  to create one. Validate completeness ≥7/10 per `_shared/verification.md` §B, then invoke
  `/site-build <project-path> <kit-slug>`. Hand it DESIGN-DIRECTION and COMPONENT-PLAN.
- **Blueprint-only path:** build directly from the blueprint + DESIGN-TOKENS.json only as a
  clearly labeled rough prototype, following `/site-build`'s layer order and hard rules.

Translate the blueprint into a project-specific site — never paste preview/gallery HTML.
Requirements (from ECC web rules + /site-build): semantic + accessible; responsive at
1440/768/375; local optimized imagery with deliberate mobile crops; lazy-load + fallbacks;
`prefers-reduced-motion`; ≤2 main fonts + optional mono; no unnecessary framework/deps; no
generic AI-template styling. Codex builds; Opus reviews each layer before the next.

## Phase 6 — Audit  →  FINAL-AUDIT.md  ·  Opus final approval

Codex captures fresh same-session desktop/tablet/mobile screenshots (reuse `/site-build`'s
`evals/full-{1440,768,375}.png`). Opus compares them **directly against the approved-direction
references** and judges, axis by axis:
brand fit · hierarchy · typography · imagery + cropping · component consistency · originality ·
conversion clarity · accessibility · mobile quality · **does it still look AI-generated**.
Score against `~/design-library/_shared/rubric.md` and `conversion-principles.md`.

**Run the `slop-judge` agent first** (target = built page, project = this project). Its
`evals/slop-judge.md` is required evidence: a FAIL there is a FAIL here, and its section scores
and board comparisons feed the "does it still look AI-generated" axis. Re-run it after every
repair iteration.

- Run the anti-AI-slop checklist and flag every hit: black+neon SaaS defaults; excessive empty
  space; giant generic headlines; repeated identical rounded cards; emoji icons; fake
  dashboards; purposeless monospace; generic gradient backgrounds; weak imagery;
  superficial/decorative blueprint use.
- Process-integrity checks (the iteration ladder must have actually happened):
  - Were the Stage A directions and Stage B variations **genuinely different** (composition/
    rhythm/scale/type-treatment), not recolors? If the final looks one-shot, fail it.
  - Did references influence the **whole page**, not just the hero (per §Reference-led body)?
  - Is generated/sourced imagery **masking a weak layout** — would the section still read with a
    grey box in place of the image? If not, the layout is the problem.
  - Does the shipped text match **approved `PAGE-COPY.md` verbatim**, with no builder-invented
    prose, lorem survivors, or fabricated proof (numbers/testimonials/logos)?
  - Are **component-library defaults** still visible (shadcn/21st.dev theme not restyled to
    tokens)?
  - Does the page resemble a **known AI-template family** (Vercel-dark, generic-Tailwind-marketing)?
  - Were **tweak-panel choices correctly written into `DESIGN-TOKENS.json`** (panel values ==
    shipped values)?
  - Is all **temporary tooling removed** — `site-director/comparison/` and any tweak panel gone
    from the build?
- Codex fixes only **evidence-backed** problems (cite the screenshot). Max 3 repair iterations
  (per `_shared/verification.md`); after 3, the honest verdict stands — never inflate a score.
- `FINAL-AUDIT.md`: per-axis findings with screenshot citations, weakest section named with
  px-level specifics, checklist hits, fixes applied, and exactly one verdict:
  **PASS | PASS WITH LIMITATIONS | FAIL**. No visual evidence means no premium claim or PASS;
  no fresh same-session screenshots means FAIL. A blueprint-only prototype is capped at
  PASS WITH LIMITATIONS.
- **Opus picks that verdict and gives final visual approval** — the one check this whole skill
  exists to enforce.

---

## Hard rules

- Coordinate, don't duplicate. Each system is edited only through its own skill; site-director
  never rewrites kits, hub data, or the font presets.
- Approval gates A (one of three directions), A2 (one of three variations), B (images), Asset
  (build evidence), C (stack change), D (page copy) are mandatory stops. Never one-shot past a gate; never
  install a tool or download an asset without approval.
- Feed back only **proven** discoveries: a new site worth measuring → `/site-research` kit; a
  recurring pattern seen in ≥2 references → hub `patterns/` (per hub promotion rules). Never push
  unverified guesses into the hubs.
- Keep it compact and operational: the 9 output files are the contract, not decoration.
- Numbers over adjectives in every artifact — hex, clamp(), rem, ms.

## Workflow

```
brief ─► 3 directions ─🚦A─► 3 variations ─🚦A2─► refine ─► imagery ─🚦B─► asset gate ─► components ─🚦C─► copy ─🚦D─► build ─► audit ─► ✅ Opus
(P1)     (P2·A Hub+Fonts)      (P2·B)              (P2·C)    (P3)       (P3)          (P4)          (P5)     (P6)
                └─ comparison board (temp) ─┘                                                        remove temp tooling ┘
```
