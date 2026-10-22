---
name: design-sources
description: The user's six vetted design sources made usable by Claude — Refero Styles DESIGN.md files (real brands' tokens), Kage (MCP: real page/component prompts), Supahero + Minimal Gallery reference boards (the taste bar), Kinetics (153 spring micro-interactions) and MicroKit UI (49 hover/click effects) — plus the slop-judge agent that checks a site against them. Use while building or redesigning ANY website, landing page, section or hero: pick tokens from a DESIGN.md, structure from Kage/hero-layouts, interaction states from Kinetics/MicroKit, and run slop-judge before calling it done. Triggers on "design.md", "refero", "kage", "supahero", "minimal gallery", "kinetics", "microkit", "micro-interaction", "does this look AI", "AI slop", "make it look less generic", and any web build.
---

# Design sources + slop judge

Everything lives in `~/design-library/_shared/`:

| Path | What |
|---|---|
| `sources/README.md` | **Read first.** Per-section playbook: for hero / nav / features / proof / gallery / CTA / footer, which board to look at, where structure, tokens and interaction states come from. |
| `design-md/refero/INDEX.md` | 32 Refero DESIGN.md files grouped by project type (F&B, snacks/drinks, sport, nonprofit, logistics, finance, studio, hospitality). |
| `sources/boards/` | Calibration images: `supahero-tierA.jpg` (the bar), `supahero-tierC-template-family.jpg` (never build this), Minimal Gallery boards by industry, `kage-structure-<section>.jpg`. |
| `sources/kinetics/INDEX.md` | 153 spring effects; full CSS/React/prompt in `effects.json`, working demo code in `_vendor/kinetics/public/`. |
| `sources/microkit/INDEX.md` | 49 effects; code (React + plain CSS + Tailwind) in `microkit/code/<name>.txt`. |
| `slop-judge/CRITERIA.md` + `capture.py` | The judge's per-section criteria and its evidence capture. |
| Kage MCP (`kage`) | `search_designs`, `get_design`, `get_component`, `design_brief`. Structure only. |

## While building
1. Load `website-house-rules` (it wins over everything) and check the component hub (`component-hub` skill) before generating any component.
2. Choose tokens: 1–2 files from `design-md/refero/INDEX.md` (or the project's kit in `~/design-library/kits/`). Copy the *system* (scale ratios, palette roles, radius scale), re-derive values from the client's real brand. Fonts: use the file's `Substitute:` unless licensed.
3. For each section, follow its row in `sources/README.md`. Look at the board before writing code — the target is "would not look out of place on the board".
4. Interaction: give each role one designed state from Kinetics/MicroKit (CTA, nav link, input). Never the same `translateY + shadow` lift on everything; honour `prefers-reduced-motion`; vanilla sites port the CSS and a few lines of JS (no React).

## Before saying done — mandatory
Spawn the **slop-judge** agent with the URL (localhost fine) or HTML path and the project root.
It writes `<project>/evals/slop-judge.md`. Fix what it names, re-run until **PASS** (or PASS WITH
LIMITATIONS: ≤2 sections at 3, each with a named fix). Report the verdict line to the user.
A Stop hook (`~/.claude/hooks/slop-judge-gate.py`) reminds you if web files changed and the judge has not run.

## Do not
- Treat Kage or Supahero membership as proof of quality (both contain template-family entries).
- Ship another brand's palette, fonts, copy or images from a DESIGN.md / Kage prompt as the client's own.
