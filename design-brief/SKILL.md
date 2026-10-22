---
name: design-brief
description: |
  Persist and restore visual design context across Claude Code sessions.
  Trigger on: "design brief", "/design-brief", "save design context",
  "update the brief", "update design brief", or at the END of any session
  where significant visual/CSS/component decisions were made.
---

## Purpose

Prevent design context loss between sessions. One file per project captures
direction, tokens, decisions, and open feedback so any future session can
pick up without re-explanation.

## On trigger

1. Identify the active project root. If ambiguous, ask which project.
2. Look for `design-brief.md` in that root. Create it if absent.
3. If creating: scaffold all sections below with placeholder values.
4. If updating: append only — never rewrite existing entries.

## File structure (`design-brief.md`)

```markdown
## Direction
<!-- Style direction (e.g. "dark luxury", "neo-brutalism"). References (URLs or image paths). -->

## Tokens
<!-- Palette, type scale, spacing in use. Always cite source file path, e.g. src/styles/theme.css. -->

## Components
<!-- List of designed components and their states, e.g. "PricingCard — default, hover, selected" -->

## Decisions
<!-- Dated log: what was chosen, why, what was rejected and why.
     Format: YYYY-MM-DD: [choice] — [rationale]. Rejected: [alt] — [reason]. -->

## Open feedback
<!-- Unresolved user/design feedback verbatim, dated.
     Format: YYYY-MM-DD: "[exact quote or description]" -->

### Archive
<!-- Pruned stale entries go here. Keep main sections under 200 lines total. -->
```

## Update rules

- Decisions and Open feedback: append new entries, never edit old ones.
- When feedback is resolved: move its line from Open feedback into Decisions
  with a note on what was done.
- Keep the whole file under 200 lines. Prune oldest resolved entries into
  `### Archive` at the bottom when the limit approaches.

## Session-start behavior

When beginning work on a project that has `design-brief.md`:
1. Read it before proposing or making any visual changes.
2. Confirm you've absorbed the current direction — do not suggest changes
   that contradict recorded decisions unless the user explicitly overrides.

## Example decision entry

```
2026-07-03: Switched hero background from gradient blob to dark noise texture —
felt more premium. Rejected: gradient blob — looked like default shadcn demo.
```
