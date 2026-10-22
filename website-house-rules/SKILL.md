---
name: website-house-rules
description: The user's standing website rules, distilled from repeated complaints across the Rituals Popcorn build (Sep 2026) and earlier sites. Load BEFORE building, redesigning, or editing any website, landing page, section, or hero — and again before saying a website change is "done". Covers banned AI-tell patterns (eyebrow/kicker text above headings, "01 · Label" numbering, dot headers), fades/seams, sticky/scroll layering, performance, content accuracy, scope, and the fix-verification loop. Triggers on any web/site/section/hero/landing work, "make it look less AI", "fix the site", or a user complaint about a site.
---

# Website house rules

Every rule below is a complaint the user had to make **more than once**. Treat them as hard defaults. Only break one when the user explicitly asks for that exact thing in this session.

A PostToolUse hook (`~/.claude/hooks/web-house-lint.py`) greps edited HTML/JSX/CSS for the mechanical ones and prints `WEB-HOUSE-LINT` warnings. When one fires, fix it before replying. Don't argue with it unless the user asked for that element.

## 1. Banned AI-tell patterns (8+ complaints, the #1 issue)

- **No small text above headings.** Also called eyebrow, kicker, overline, pre-title, section label or tagline chip. Examples: "BUKTI TEKSTUR", "Our story", "— Since 2019". The heading stands alone. The user has asked for this removal in almost every site session.
- **No floating micro-labels** or annotation captions sitting on or under drawings, images or mascots.
- **No numbered-dot labels:** "01 · Lapisan", "02 — Flavours", "No. 3". The user's words: *a number then a floating dot is a clear indicator of AI*.
- **No dot/period headers:** "Crunchy. Salty. Yours.", "Real corn · Real butter". No two-clause-with-period slogans as H1/H2.
- **No template sections:** stat strips, "why choose us" 3-card grids, fake testimonials, generic feature bento.
- **What to do instead:** copy a **real reference site's structure 1:1**, then adapt it with the real content. Sources for that, per section, are in the `design-sources` skill (Refero DESIGN.md tokens, Kage structure, Supahero/Minimal Gallery boards, Kinetics/MicroKit interaction states). The user names it (Graza, white-desert, Hermès macro hero). If none is named, ask which site to follow before inventing a layout. The component hub (`component-hub` skill) has 1:1 rebuilds; use those over freehand sections.

## 2. Transitions, fades, seams

- **No fade / gradient-to-transparent edges / feathered masks** between sections, layers or images unless asked. The user wants hard, clean cuts. They once had to say *there literally shouldn't be any fade effects anymore* twice.
- **No visible crop lines or seams** in stacked or tiled image bands. This recurred twice after "fixed". Check the exact pixel row at 1440 and 375.
- **No gaps between grouped images.** Background showing between images reads as a bug. Tighten until they touch or overlap.
- **No leftover blank space** after the hero or between sections. Scroll the whole page and look.
- Word spacing and letter-spacing stay normal. Text-reveal animations are slow and readable, not snappy.

## 3. Sticky, scroll and layering

- **Default everything to static.** Nothing sticky or pinned unless the user asked. Say exactly where it pins (e.g. "sticks at the very top from load"). A carousel that should "just stay in place" and a layer that should "act as a barrier" were both wrongly sticky.
- **Navbar:** sticky if the reference site's is. Check the reference, don't guess.
- **Sections are hard boundaries.** Text or layers from section N must never show over section N+1 after its scroll ends. Nothing may "just disappear" mid-scroll.
- Parallax pieces are placed individually. Never move whole rectangle strips in and out as units, which shows as layers popping in and out.

## 4. Performance (3 "it's laggy" complaints in a row)

- At most **one WebGL context** per page. Never stack WebGL + GSAP + a big parallax set in the hero.
- Every rAF loop, canvas or WebGL render pauses off-screen with `IntersectionObserver`. No forever-loops.
- After adding any effect, scroll through it with real input and check smoothness. Prefer deleting an effect over shipping lag. The user will ask for it removed anyway.
- Load the `web-perf` skill for the build patterns.

## 5. Content accuracy

- Show the **real product line**, e.g. all 5 flavours, not just the bestseller.
- **Founder ≠ mascot.** Never put a real person in a mascot/character section, or the reverse.
- **Every visual must match its copy.** Before finishing, list each image beside the text it sits next to, and swap anything unrelated.
- **No pack-label or compliance clutter** in consumer copy: halal cert numbers, SKU or gram codes, "jagung mushroom · bukan butterfly". The user's words: *nobody needs to know that*.
- **No invented facts:** prices, ratings, reviews, flavour names, nutrition. Unknowns go to `CONTENT-GAPS.md` or get flagged inline.
- **Links must work.** No `href="#"` left on shipped nav or CTAs.

## 6. Scope

- **Don't add sections or features the user didn't ask for.** Showcase sections with no content purpose were cut. A full buy/shop flow was cut ("I won't do that much for a free site").
- Anything heavier than a section (cart, CMS, auth, booking): ask first. Mention the project size.

## 7. The fix loop: "you didn't do what I asked"

This caused the angriest messages: *"don't ignore me"*, *"you didn't do one number that I requested"*, *"I literally told you not to"*.

1. **Number every request** in the user's message, including ones buried mid-paragraph. Screenshots count as requests.
2. **Fix every instance, not the first one.** Grep the whole project for the pattern: every file, prompt and variant, e.g. every "butterfly" in every prompt file.
3. **Verify each item at the exact spot the user pointed to.** Take a fresh screenshot at that scroll position at 1440 and 375, using real scrolling and clicks, not `element.click()`. First confirm the new code is actually loaded (hard reload, no stale cache).
4. **End the reply with a per-item status table:** `# | request | done/not done | proof`. Never write "fixed" without a screenshot taken after the change.
5. If the same item fails twice, **stop patching**. Remove the effect, simplify, or copy the reference 1:1, and say so. Piling on changes made things worse every time (the image-prompt sessions went 8 rounds and ended in "maybe we should give up").
6. If the user asks for a thing (a prompt, a file, an answer), deliver it **in that reply**, before anything else.

## Pre-ship checklist (run before saying "done")

- [ ] No eyebrow or kicker text, micro-labels, numbered dots or dot headers (hook clean)
- [ ] No fades or feathered edges, seams, image gaps or blank bands. Scrolled top to bottom at 1440 and 375
- [ ] Nothing sticky that wasn't asked for; sections end cleanly
- [ ] Smooth scroll through every animated section; one WebGL max; off-screen loops paused
- [ ] Every image matches its copy; full product line shown; no invented facts; no label clutter
- [ ] No unrequested sections or features
- [ ] Per-item status table with fresh-screenshot proof
- [ ] **slop-judge agent run on the finished page → `<project>/evals/slop-judge.md` says PASS** (or PASS WITH LIMITATIONS: ≤2 sections at 3, each with a named fix). Quote the verdict line. No judge run = not done. A Stop hook (`slop-judge-gate.py`) reminds you.
