# Art direction — the gap between a good photograph and an advertisement

Written 2026-09-18 after a direct head-to-head: adgod's own seven-prompt Olaplex Nº.7 deck against our
thirty-one prompts for the same product. His deck is in `corpus.md` under **Deck: Olaplex Nº.7 Bonding Oil**.
This is the only place in the library where his work and ours exist for the *same* product, so it is the
cleanest evidence available about what we were missing.

Verdict from the user, unprompted: *"adgod's is way better than ours, by a margin."* They were right, and the
cause is not craft. Our renders are clean, correctly proportioned, correctly printed and physically
believable. They are also **twenty variations of one picture.**

## The counted diff

adgod n=7, ours n=31 (24 launch grid + 7 narrative). Both decks for the same product.

| Feature | adgod | ours |
|---|---|---|
| Stated colour-**grading** recipe | **83%** | **0%** |
| HDR / 8K / retouching finish tail | **100%** | **0%** |
| Dark or saturated colour field | 50% | 6% |
| A person in frame | 50% | 6% |
| Product NOT upright on a surface | 50% | 23% |
| The product's own liquid staged as an event | 33% | 16% |
| Top-down / overhead / flat lay | 17% | 0% |
| More than one unit | 17% | 6% |

And the range measure, across his whole 97-prompt corpus rather than one deck:

| | distinct background colour words |
|---|---|
| adgod, mean per **seven-frame** deck | **6.4** (range 3–11) |
| ours, across **twenty-four** frames | **4** |

Per frame that is **0.91 against 0.17 — five times less colour range.** His Nothing deck alone carries eleven
background colours in seven frames; his Dior deck ten.

One more: **his prompts are shorter than ours.** 297–403 words, median 367, against our 452–502 and 729–842.
He spends his word budget on art direction. We spent ours on locks and contact physics.

## The missing piece, in one line

**We were prompting for a photograph. He is prompting for a photograph that has been art-directed, lit for
drama, and graded in post.**

Everything below follows from that.

## Three things we removed, and why each removal was wrong

### 1. The grade

We name a palette — *"Palette is golden-amber, bone-white and warm grey"* — which describes **what is in the
frame**. He names a grade — *"Colour grading should be refined luxury beauty advertising style with deep navy
tones, polished silver reflections, crisp contrast, clean whites, rich product colour reproduction, and
ultra-premium editorial finish"* — which describes **what was done to the file afterwards**. 83% against 0%.

A palette is inventory. A grade is a look. Write the grade.

### 2. The finish

The realism gate stripped `HDR`, `retouching` and `8K` from every prompt we wrote, on the evidence that HDR
plus soft light flattened the VT PDRN deck. **That inference was wrong, or at least over-general.** adgod
carries that tail in 7 of 7 Olaplex prompts and 67–70 of 97 corpus-wide, and his output is the standard we
are chasing. What flattened VT was a *sourceless soft rig on a render plate*, not the token `HDR`.

Restore the finish tail whenever a real product photograph is attached. Keep it off only for text-only work
until that is tested separately.

### 3. The range

`SKILL.md` said: *"choose one palette family and one lighting logic that all images share. Varying these per
image is what makes a deck look like stock."* Taken literally across 24 frames, that produced bone-white
plaster, warm side light and a white block, twenty times.

**His own practice contradicts the rule as written.** He does not lock the field. He locks the *production
value* — the camera body, the finish tail, the "no CGI" assertion, the product's fidelity — and lets the
world change completely from frame to frame: charcoal-to-black, deep navy, seamless white, warm off-white,
ivory, a dark wall of hair.

Corrected rule, now in `SKILL.md`: **lock the product and the production value; vary the world.**

## Two creative deficits the counts also expose

**Gravity.** Half his frames float, hang, submerge or lay the product down; 77% of ours stand it upright and
dead level on a block. Standing a bottle on a plinth is the single most available composition and therefore
the least interesting one.

**People.** Half his frames contain a person; 6% of ours do. We built a whole aliveness system and then
produced a product deck with nobody in it.

## The pattern underneath all of it

Look at his seven and one shape repeats: **one spectacle, and an otherwise empty field.**

A hand generously coated in the product's own oil, dripping, against plain off-white. Three units on a
polished chrome tray against flat navy. The bottle submerged behind a layer of liquid glass with its own
typography refracted, on seamless white. Two oil beads and a diagonal spotlight beam on a silver-to-black
gradient.

In every case: one engineered optical event involving the product's own substance or a reflective set piece,
placed in a field with nothing else in it. Nothing competes, so the event reads as expensive.

Ours: a correct product on a textured surface in a real room. Competent, and nothing is happening.

**The working question for any frame: what is the one thing happening here, and is the rest of the frame
empty enough to let it read?**

## What is off limits

His seven Olaplex scenes are now published work for this exact product, so they join the do-not-restage list
in `signature.md`: the floating diagonal with two beads under a spotlight beam · the oil-coated hand with the
bottle hanging from it · three units on an oval chrome tray on navy · the hand beneath a chin with the eyes
cropped · the bottle submerged behind liquid glass with refracted type · the two-glass-shelf bathroom set ·
the shot from behind with the bottle at the ear.

Copy the method. The grade, the finish, the range, the gravity, the people, the one-spectacle-and-a-void
structure — all craft, all transferable. The scenes are his.

## Correction to the realism gate

The gate's hard fail on **counted decorative droplets** fires on adgod's own Olaplex prompt 01, which says
*"Place two translucent glossy serum/oil droplets around the product, one near the upper left side and one
near the lower right side"* — and that frame is one the user singled out as high quality.

The rule was calibrated on the VT deck, where counted beads sat on dry surfaces under sourceless light. It
does not generalise. **Counted droplets are legitimate when they are staged as designed objects in a studio
frame**; they fail when they pretend to be incidental realism. Judge by intent, not by the count.
