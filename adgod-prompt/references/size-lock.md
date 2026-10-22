# Size lock — one geometry for the product in every frame

Without this, the model re-estimates every dimension the prompt leaves unstated, separately in each frame.
The product then comes out short in one image and long in the next, and a viewer notices at once when the set
sits side by side.

## The failure, measured

2026-09-14, VT PDRN 100 rebuild deck, text-only. Upright frames were read off gridded full-resolution crops and
compared against a pixel-probed, straight-on product render. All ratios are in body widths:

| | Overall height | Cap height |
|---|---|---|
| Real product (render) | 2.72 | 0.47 |
| Frame 01 | 3.04 | 0.72 |
| Frame 03 | 3.26 | 0.88 |
| Frame 04 | 3.01 | 0.91 |
| Frame 05 | 3.01 | 0.82 |

Overall height ran 11–20% tall, and every cap came out 53–94% too tall. The cap is the dominant error.

Three causes:
- **Absolute centimetres with no ratios.** Centimetres don't survive a change of crop or camera distance.
- **A size adjective.** The prompt said `oversized overcap`, and the model applied it to height.
- **No scale anchor in the scene.**

## The fix, measured

| Version | Cap height error | Overall height |
|---|---|---|
| v1, no lock | +53–94% | +11–20% |
| v2, lock "half a body width tall, clearly wider than it is tall" (2 frames) | +13–23% | −3% to +10% |
| v3, lock "less than half a body width tall, nearly twice as wide as it is tall" + render attached (8 frames) | −17% to +17%, median about +8% | −12% to +12% |

In v3, 4 of 7 upright frames are within 10% on both measures. The remaining misses:
- **Body runs long in hand-held frames** (+15%).
- **A tilted bottle foreshortens the cap** (−17%).
- **Top-down lying bottles come out short**, −3% to −12% across v2 and v3.

Attaching the render did not tighten proportions (v2 A/B: ±10%). It did copy the label layout exactly (line
breaks, weights, the flat band), which text alone never achieved, and it cost no visible realism.

**Size against people is not fixed.** In v3's model frames the bottle held against a cheek came out 40–50% too
large relative to the face, despite `about half as tall as her face from chin to hairline`.

## Procedure

**1. Build a size card once per product, before any prompt.** Save it next to the product photos as
`<product>-size-card.md`. Take dimensions from the first source available:

1. **Published dimensions** from the brand or a retailer spec sheet.
2. **Measured from a straight-on front photo or render** (long lens, no perspective). **Use a pixel probe or a
   gridded full-resolution crop, never an eyeballed downscaled view.** The first VT readings done by eye were
   off by 4–6% on the render and by up to 14% on the frames. Record the cap top, cap bottom, shoulder, base, and
   body left and right edges, then divide by body width.
3. **An estimate**, made once from the volume and closure size and marked *unconfirmed*. Never re-estimate per
   frame.

The card records: overall height, body height, neck or closure height, cap height and width, and the position
of any band or label, all in units of the widest body dimension. It also records absolute centimetres with
their source, and a list of scale anchors.

**2. Write the proportion lock and paste it verbatim into every prompt**, inside the fidelity lock (P9):

- Give each part as a ratio in body widths, rounded toward the true value, never away from it. "Half a body
  width" for a real 0.47 produced 0.54–0.58.
- For each part the model gets wrong, add a relation it can see within that part. `The cap is nearly twice as
  wide as it is tall` compares the cap's own width and height, and it pulled the cap from +13–23% to a median of
  about +8%. Check each relation against the measured numbers before using it.
- **Use no size adjectives**: oversized, tall, slim, petite, chunky. The model applies them to the wrong axis.

**3. Give each scene one scale anchor**: an object with a known real size, related by **geometry, not
comparison**. For example, `her fingers wrap about halfway around the body`, or `each bottle about two-thirds
the length of 14-centimetre scissors`.

For the product against a person, a comparison with the face is ignored. Measured:
`about half as tall as her face` came out at 0.70–0.76. Use a span the face already contains, e.g. `resting
against her cheek, the bottle reaches from just below her cheekbone to her jawline and no further`. That
wording is untested.

**Decoded from the adgod and FASHIONNN prompts (2026-09-14): how they size a product held to a face.**
- **adgod never states size relative to a face in words.** Its 23 hand- and face-held prompts attach a real style
  plate in which a real hand already holds a similar object, so scale is inherited from the photograph (P1).
- **The text names only the contact point:** `against the upper cheekbone/temple area` (Rhode 06),
  `between the cheek and temple area, lightly touching the skin` (Crown Affair 03), `the top portion lightly
  touches the underside of the chin` (Chanel 02).
- **It fixes the face's size with a crop:** `cropped from forehead to chin` (Oakley 04).
- **It names the failure:** `so it appears naturally held rather than artificially enlarged or reduced`
  (Chanel 02). Grip adapts: `adjust finger spacing, grip pressure, wrist angle`.
- **FASHIONNN gives position only** (`held close to the face, slightly angled toward camera`). The 28 prompts
  added 2026-09-17 confirm it. None states a held object's size, yet every held object renders at plausible
  scale, because every one is a familiar type: phone, paperback, teacup, handbag, dog. The corpus never tests
  an unfamiliar product, so it is a boundary condition, not a fix. Contact-point language works when the
  model already knows the object's size. An unfamiliar product still needs the ratio lock plus a carrier.
  Source: `~/Documents/adgod-prompts/refs/fashionnn/REVERSE-ENGINEERING-2026-09-17.md` §5.
- **What this means for text-only work:** with no style plate, the landmarks have to carry size as well as
  position. Put the cap and base on named facial landmarks, keep the product at the face's depth, add a
  finger-width relation, and keep adgod's anti-enlargement negation.
- **Tested in v4, n=1 per frame, measured as bottle height ÷ pupil-to-chin:**
  - Target: about 0.86 at the unconfirmed 9.5 cm.
  - v3 (face comparison): 1.29 and 1.20.
  - v4 (landmark span): 1.43, 1.02 and about 1.0.
  - Two of three moved toward scale and none reached the target. The model honoured one landmark at most and
    ran the bottle from about eye level to below the jaw.
  - A held-product size prior survives both comparisons and landmark spans.
- **Next to test:** frame-fraction numbers for the product and the face, or a real non-adgod photograph of a
  hand holding a similar bottle to a face, attached as Image 1 so scale is inherited (P1), as adgod does.

**HAND GEOMETRY — DIRECTIONALLY SUPPORTED, NOT ESTABLISHED. 2026-09-18, OLAPLEX Nº.7, n=1 per arm.**
Three arms, same model and frame, product plate attached, one variable: no size language (control) / hand
geometry / hand geometry plus frame fractions.

**What is solid — proportions.** Measured on the golden-oil body with a hue mask, verified by eye against a
mask overlay, and calibrated on the reference pack shot with the same mask (reference height ÷ median width
= 1.660, matching the card's 1.65):

| Frame | oil-body H ÷ median W | vs reference |
|---|---|---|
| reference pack shot | 1.660 | — |
| arm 1 | 1.717 | +3.4% |
| arm 2 | 1.723 | +3.8% |
| arm 3 | 1.708 | +2.9% |

**All three inside 4%.** This is the best proportion result the project has produced — v3 ran a median cap
error of about +8% with 4 of 7 frames inside 10%. The proportion lock plus an attached plate holds shape.

**What is NOT established — scale against the hand.** Do not trust the first reading of this test, including
the one written here before measurement. Two failures:

- **The three renders are framed differently**, so comparing apparent bottle size across them by eye is
  invalid. That is how the first (wrong) ranking was produced.
- **Every cross-image normaliser tried was too noisy to use.** No finger crosses the bottle's centre, so a
  finger-width probe finds nothing. A hand-breadth probe on rows below the base returned medians of 114, 129
  and 239 px with within-image spreads of 81–157, 85–207 and 132–241 — it is catching wrist and forearm at
  different rows. Those medians happen to rank the arms the same way the eye did, and the third lands almost
  exactly on the real 0.50 body-width-to-hand and 0.76 height-to-hand, but with that spread it is not evidence.

**To settle it, the re-run must control framing.** Fix the crop identically in every arm, and put one object
of known size in frame at the same depth as the product — a credit-card-sized card is 8.56 cm long against
this bottle's 8.7 cm, so the two should read as almost the same length. Then the ratio is measurable inside a
single image and no cross-image normaliser is needed.

**The wording under test, unchanged:**

> The product is a little taller than her palm is wide across the knuckles, and its body is exactly as wide
> as her index and middle fingers held side by side, so her curled fingers reach most of the way around it
> and the tip of her middle finger does not meet her thumb.

Replace the two ratios with the product's own, taken from its size card. Frame-fraction numbers are worth
dropping regardless: in arm 3 they coincided with visible scene drift — a rug appeared and the model printed
words on a prop tote despite a `no text` negative.

**4. Attach the product image whenever one exists, for print fidelity.** In Codex, pass it as
`referenced_image_paths` to `image_gen`. If the image is a render, attach it with this disclaimer:

> `Image 1 is a studio render of this exact product, attached only for its shape, proportions and printing:
> match its silhouette, cap proportions and every letter exactly, and ignore its white background, lighting and
> reflections, because this is a location photograph and every reflection comes from the scene.`

Keep the text lock as well. The attached image fixes the print; the lock fixes the proportions.

**5. Check every render against the card.** For upright frames, measure overall height ÷ body width and cap
height ÷ body width on a gridded crop. Reject a render that is more than 10% off either value. For tilted,
lying or angled bottles the reading is only good to about ±10%, so judge the cap's squatness by eye as well.
For frames with a person, also check the product's size against a body part at the same depth.

## Props get a size too, or they eat the product

**2026-09-19.** The comb frame rendered with the product's own proportions correct and **the comb roughly four
times too big** — each tine about half the bottle's body width. A real wide-tooth comb has tines about 5 mm
across against this bottle's 38 mm body, so a tine should be **about a fifth of the body width**.

Cause: the size card locks the product and nothing else. Everything unstated is re-estimated, and that is P15
applied to the set, not just the hero. The model had no reason to think a comb was smaller than a rake.

**Rule: every prop in contact with the product gets its size stated as a ratio to the product.** One clause
each, in the scene sentence:

> `a wide-tooth horn comb whose tines are each about one fifth of the bottle's body width and whose spine is
> about twice the bottle's length`

Do the arithmetic from real dimensions before writing. Common ones against this 8.7 x 3.8 cm bottle:

| Prop | Real size | As a ratio |
|---|---|---|
| Wide-tooth comb tine | 5 mm | 1/8 of the body width |
| Wide-tooth comb, overall | 19 cm | just over twice the bottle's height |
| Flat iron, overall | 30 cm | three and a half bottle heights |
| Flat iron plate width | 3 cm | four fifths of the body width |
| Kirby grip | 5 cm | half the bottle's height |
| Round brush barrel | 5 cm | one and a third body widths |
| Claw clip | 9 cm | about the bottle's height |

## Can it actually rest there?

The composition rule says give the product a relationship. A relationship still has to obey gravity.

**2026-09-19:** a frame asked for the bottle balanced across the closed plates of a flat iron. A cylinder on a
narrow convex surface rolls off, and the render reads as impossible — the user's words were "it realistically
can't balance there."

Before writing a placement, name the support and check it:

- **What is holding it up, and at how many points?** A cylinder needs a cradle, a groove, several parallel
  supports, or a flat face. One convex surface is not a support.
- **Would it roll, slide or tip?** If yes, restage: open the flat iron so the plates form a V and lay the
  bottle in it; lay the bottle across five or six comb tines instead of balancing it on two.
- **Where is any liquid coming from?** Both comb renders show oil running off a bottle whose **cap is still
  on**. If oil is in the frame, the cap must be off and in shot, or the oil must already be on the surface
  with the bottle set down into it.

**Word budget:** the lock plus the reference contract adds about 90 words, which pushes frames to 620–730
words. The corpus's 570-word cap is copy residue (`principles.md`) and the lock is measured, so the lock wins.
Trim the scene before cutting the lock.

## Upright means a flat surface. There is no third option.

**2026-09-19, third failure of the same kind.** Renders rejected for an impossible support three times now:
a bottle balanced on the closed convex plates of a flat iron, a bottle standing on the splayed bristle face
of a round brush lying on its side (*"there's no way the bottle can stand like that"*), and a bottle wedged
between two comb tines. Each time the support had a name, so the existing "name the support" rule passed it.
Naming is not enough.

**The test is not whether the support has a name. It is whether it would survive a nudge.**

| The product is | Only legal support |
|---|---|
| **Upright** | a flat horizontal surface at least as wide as its base — a table, a shelf, a tray, a tile ledge, the floor of a glass |
| **Lying down** | a groove, a cradle, or three or more parallel supports carrying its weight along its length |
| **Anything else** | **a hand**, or suspended in mid-air from a hand |

Bristles, tines, a heap, a convex back, a curved surface, a rope of hair, a folded cloth: none of these hold
a cylinder upright. They can hold it **lying down**, and that is all.

**The hand is the safest support in the corpus** and the most used — it cannot be physically wrong, it adapts
to any product, and it adds the human that 43% of adgod's frames carry. When a placement feels
uncertain, put it in a hand.

## A soft pack has no fixed shape — name the state it is in

**2026-09-20, generalised from the bottle's fill line.** A bottle proves it holds liquid by its headspace
staying level with the horizon. **A flexible pack — a doypack, a crisp bag, a tube, a sachet, a paper sack —
proves it is real by deforming.** Drawn as a rigid geometric solid it reads instantly as CGI.

A rigid pack has one shape and the size card is enough. A soft pack has four, and the prompt must say which:

| State | Write |
|---|---|
| **Sealed and full** | taut, gusset splayed into a flat oval base, face slightly domed, fin seal dead straight |
| **Opened** | fin seal torn along one edge leaving a ragged crimped strip, top corners flopping outward, walls slumping inward below the tear |
| **Being reached into / held** | deep soft creases radiating from every point of contact, the far wall bulging, the base lifting off the surface |
| **Near empty** | collapsed flat from the shoulders up, standing only on its gusset, deep vertical wrinkles |

**Reject:** a pouch with perfectly straight sides · a hand gripping a bag with no compression under the
fingers · an opened bag whose top is a clean cut rather than a torn crimp · the same creases repeated in
two frames of a deck.

## Two kinds of popcorn, and the same trap for any granular product

**2026-09-20.** A deck rendered caramel popcorn as walnuts. Cause: the lock said *"every piece is an
irregular craggy cluster … none is spherical or smooth."* Rituals uses **mushroom-type** popcorn — compact
round balls — because that is the type that survives caramel coating. Butterfly-type is the winged, irregular
kind you get at a cinema. **They look nothing alike, and I described the wrong one from memory.**

The pack's own illustration showed round balls. The evidence was in the file I had already opened.

**Rule: a product made of many small units needs its unit described from a photograph of the units, not
from the category.** Coffee beans, granola, cereal, pasta, nuts, sweets, tablets, crisps, ice cubes,
flakes — the category word carries a default shape, and the default is wrong about half the time.

**And: attach a second reference image of the material itself.** A pack shot proves the packaging, not the
contents. When the product is a container of many units, Image 1 is the pack and Image 2 is the units, with
both roles named in the reference contract:

> `using Image 1 as the PRODUCT IDENTITY reference for the pouch and Image 2 as the MATERIAL reference for
> the popcorn itself — every piece in this frame must match the shape, roundness, size, lobed surface and
> caramel colour of the popcorn in Image 2 exactly.`
