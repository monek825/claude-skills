---
name: component-hub
description: Find, read and extend the user's UI component hub — 60+ saved paste-ready component prompts and single-file code components (incl. 22 1:1 white-desert.com rebuilds) plus installed UI libraries (with preview images and hover videos) at /Users/Shared/second-brain/memory, browsable as gallery.html. Use whenever a task needs a UI component, section, effect or animation (hero, carousel, gallery, bento, dock, slider, timeline, accordion, gooey/liquid, glass, gradient, beams, testimonial, card fan), whenever the user says "component hub", "the hub", "the gallery", "saved prompts", or before generating a new UI component from scratch — check what is already saved first. Also use when adding a newly found or installed component to the hub.
---

# Component hub

The user's store of reusable UI components. **Check it before writing or generating any UI component** — most asks are already covered, with the source's bugs already documented.

## Where it is

Canonical path (world-readable, use this one from any tool or account):

```
/Users/Shared/second-brain/memory/
```

`~/.claude/projects/-Users-brayden/memory` is a symlink to it. Both work from this machine's `brayden` account; prefer the `/Users/Shared` path in scripts.

| File | What it is |
| --- | --- |
| `ui-components-hub.md` | The index. One line per component: what it is, what it is good for, and its known gotchas. **Read this first** — the one-liners usually answer the question without opening anything else. |
| `prompt-<slug>.md` | One entry per component: preview, best-fit analysis, keywords, the verbatim source/prompt, and a source-verified gotcha list. |
| `assets/<slug>.png` / `.mp4` | Preview image, and a showcase video for entries whose value is in motion. |
| `gallery.html` | Generated visual browser over every entry — preview, description, keywords, copy-prompt button, full prompt inline, filter box. Cards with a video play it on hover. |
| `build-gallery.py` | Regenerates `gallery.html`. Stdlib only, no deps. |
| `build/` | Local render harnesses used to produce previews (`<slug>.html` + `<slug>.js`, plus any locally generated image assets). |

## Reading it

```sh
# the index — start here
sed -n '1,80p' /Users/Shared/second-brain/memory/ui-components-hub.md

# find entries by topic
grep -il "carousel\|gallery" /Users/Shared/second-brain/memory/prompt-*.md

# browse visually — always-on via launchd (com.secondbrain.componenthub), no manual launch needed
open http://localhost:4177/gallery.html
```

A `brain` CLI also indexes this directory and prints evidence from at most two files:

```sh
~/.claude/bin/brain search "gooey liquid merge effect"
```

## Two kinds of entry

Most entries are **paste-ready generation prompts** — hand the prompt to a model, or lift the source out of the file. A few are **installed libraries** (currently `prompt-liquid-gooey.md`, npm `liquid-gooey`): those are installed with a package manager, not pasted, and the entry says so in its first line.

Design sources (2026-10-10): six `prompt-source-*` entries + `prompt-slop-judge` cover Refero DESIGN.md tokens, Kage (MCP), Supahero / Minimal Gallery boards, Kinetics (153 effects) and MicroKit (49 effects); their files live in `~/design-library/_shared/sources/` and the `design-sources` skill says how to use them per section.

Related but separate: `~/design-library/_shared/scouted/` holds already-extracted component **source** (React and vanilla), with its own `INDEX.md`. This hub stores generation prompts; that store stores source. Entries that exist in both cross-reference each other.

## Rules when using an entry

1. **Read the gotcha list before pasting.** Nearly every entry documents real bugs in its source — missing CSS, dead props, wrong Tailwind class names, missing `prefers-reduced-motion` guards, images on hosts that have already gone dead. They are recorded, not fixed: the files store sources verbatim.
2. **Check the status note.** Some entries are already shipped somewhere (PPfinal, Whitestone, Greenpact) — go look at the live port before re-implementing.
3. **Most of the user's sites are vanilla HTML/CSS/JS** (PPfinal is Flask/Jinja; Greenpact and Whitestone are static; FleetView is Flask). React/Next/shadcn entries get **ported**, not pasted. Entries note when a port is cheap and when it is not.

## Rules when adding an entry

1. Write `prompt-<slug>.md` with frontmatter (`name`, `description`, `metadata.type: reference`), a `Linked from [[ui-components-hub]].` line, an analysis section (best fit + keywords + when to reuse), the verbatim source, and a source-verified gotcha list.
   **The gallery's copy button only exists for two headings:** `## Exact prompt…` / `## Full prompt…` (copies the rest of the file — for generation prompts) or `## Paste-ready code…` (copies the **first fenced block** under it — for code). Code entries must use `## Paste-ready code` with ONE fenced block holding a complete, self-contained file: no relative asset paths (use `http://localhost:4177/build/...` or CDN URLs), no second block the first depends on. Test it: write the parsed block to a new file outside the hub, open it from `file://`, zero errors. Entries that used `## Verbatim source` / `## Full source` headings silently had no copy button until 2026-09-11.
2. Add one line to `ui-components-hub.md`, and one line to `MEMORY.md`.
3. Add a preview to `assets/<slug>.png` (plus `<slug>.mp4` when the effect only exists in motion). Render it from the entry's own archived source so the preview matches what is stored — keep the harness in `build/`.
4. **Regenerate the gallery**, always:

```sh
python3 /Users/Shared/second-brain/memory/build-gallery.py
```

It prints which entries still have no preview image.
