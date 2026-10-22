# adgod prompt anatomy

Derived from all 62 prompts in `corpus.md`. Every prompt is **one unbroken paragraph** of declarative
present-tense sentences, 250–450 words, no bullets, no line breaks, no markdown, no headings, no
"please", no second person. Blocks always appear in this order. Skipping a block is what makes an
imitation read wrong.

---

## Block 1 — Reference contract (mandatory, first sentence)

Declares what each uploaded image is for. Three canonical modes; pick by how many references exist.

**Mode A — product-only (1 image).** No style plate. You author the scene from scratch.
> `Use the uploaded product image as the sole product identity reference.`
> `Using the uploaded product image as the sole product reference, ...`
> `Create an ultra-premium <genre> using the product provided in the reference panel as the exact product identity.`

**Mode B — style plate + product plate (2 images).** Most common. Style image is the look; product image is the identity.
> `Using the uploaded image as the STYLE REFERENCE and the product image in Reference Image 2 as the PRODUCT REFERENCE, recreate the scene with the product from Image 2 naturally integrated into the composition.`
> `Using Reference Image 1 as the master style/composition reference and Product Image 2 as the product reference, recreate this exact <genre> while replacing the original product with the product from Image 2.`
> `Use the uploaded reference image only as a style and composition reference, and use the uploaded product image in the reference panel as the ONLY source for the hero product.`

**Mode C — master-DNA lock (2 images, maximum-fidelity recreation).** Uppercase the inherited attributes; this is the strongest style-transfer form in the corpus.
> `Using Image 1 as the MASTER STYLE, COMPOSITION, LIGHTING, CAMERA ANGLE, FRAMING, MATERIAL RESPONSE, CONDENSATION, LIQUID PHYSICS, GLASS DISTORTION, REFLECTIONS, HIGHLIGHTS, DEPTH OF FIELD, COLOR GRADING, and OVERALL VISUAL DNA. Replace the original product completely with the product shown in Image 2 while preserving the exact photographic setup and visual structure of the reference.`

**Mode A-S — symbolic, no product plate (service brands, concept ads).** No reference image at all. The
fidelity lock has nothing to lock onto, so it is *replaced* by a subject-fidelity clause that forces the
invented object to render as a photographed thing rather than an illustration:
> `There is no uploaded product reference; the subject is built entirely from this description and must be
> rendered as a real physical object photographed on set, with authentic material identity, correct
> real-world scale, honest surface wear and manufacturing detail, never as an illustration, a
> three-dimensional render, or a stylised icon.`
Everything else — composition, lighting, physics, palette, tech tail, negatives — is unchanged. Use for
brands whose product is software or a service, where the hero must be a symbolic object. Ban text and
numerals in the negative list so no unapproved claim can be baked into the pixels.

**Variant opener (Mode A only).** Some prompts front-load the genre as a bare noun phrase, then give the
contract in sentence two:
> `Ultra-premium commercial product photography, vertical 4:5 composition, clean luxury studio setup on seamless pure white background... Use the uploaded product image as the exact product identity reference and preserve every physical detail...`

---

## Block 2 — Fidelity lock (mandatory, immediately after the contract)

A long comma-run of every attribute of the product that must survive. **The list is category-specific.**
This is the single highest-leverage block: it is what stops the model redesigning packaging.

Universal spine, always present:
> `Preserve the product exactly as provided, including its authentic shape, proportions, dimensions, silhouette, construction, materials, texture, ... branding placement and every unique design detail.`

Append the category enumeration:

| Category | Enumerate |
|---|---|
| Softgoods / bags | stitching, hardware, straps, cords, buckles, zippers, seams, pockets, colour blocking, fabric characteristics |
| Beverage can / bottle | cap or closure details, label artwork, typography, embossing, printing details, transparency level, liquid fill level, metallic finishes |
| Cylindrical tin | brushed aluminium finish, rolled metal lid, label proportions, cylindrical label wrap, machining lines, micro-scratches |
| Cosmetics | cap structure, applicator, packaging thickness, curves, gloss level, embossing, label details, colour accuracy |
| Watch / horology | case shape, bezel, dial, hands, indices, crown, crystal, bracelet or strap, links, clasp, engravings, polished and brushed finishes |
| Eyewear | frame geometry, lens curvature, lens colour, hinges, temple arms, finishes |
| Consumer electronics | transparent elements, internal architecture, speaker mesh, vents, microphones, buttons, ports, seams, hinges, glossy and matte materials |
| Food / produce | surface texture, natural irregularity, colour saturation, gloss, moisture |

Fidelity lock always ends with a no-redesign clause:
> `...without redesigning, slimming, stretching, reshaping, distorting, or modifying any physical characteristic.`

Two verbs worth adding to that clause, because they name failures the corpus does not: **beautify** and **add gloss** —
models improve packaging unbidden more often than they distort it. And a crisp summary line for campaign work, where one
product must survive many scenes:
> `The environment may change; the product itself must remain visually consistent.`

**Add the proportion lock (`size-lock.md`).** The category enumeration names the product's parts but not their
sizes, so the model re-estimates them in every frame. Measured: every cap came out 53–94% too tall. Append the
product's ratios in body widths verbatim, and never describe a part with a size adjective such as `oversized`.

**For a deck, hoist the lock above the prompts.** Two images in the reference library are not campaign frames
but identity spec sheets — `FUTER DEATH` and `OAKLEY META BRAND KIT` — which fix the enumerated attribute list,
the hex palette in compound colour words, the typography and a DO / DON'T list *before* any prompt is written.
Every frame then inherits the same list verbatim and cannot drift between images. Build that sheet first for
any multi-frame set, and for anything automated that generates many prompts from one product. See
`library.md`.

---

## Block 3 — Adaptive scale clause (mandatory whenever a style plate exists)

Lets the model fit a differently-shaped product into a borrowed composition without warping it.
> `Automatically resize the replacement product according to its real-world dimensions while maintaining the exact composition, orientation, and perspective of the reference.`
> `Automatically adapt the entire composition to the uploaded product's exact dimensions while maintaining the same visual balance, spacing, perspective, and premium aesthetic. If the uploaded product differs in size or shape, intelligently resize and reposition every element while preserving the original composition.`

For held / worn products, extend it to the human interface:
> `...intelligently adjust finger spacing, grip pressure, wrist angle, and product position so the interaction appears naturally photographed instead of edited or pasted.`

---

## Block 3b — Affordance override (mandatory when the product's interaction differs from the style plate)

A style plate carries the *previous* product's interaction baked into its pose. Left unstated, the model
reads "worn on the back" off a backpack reference and applies it to a tote. Break that inheritance
explicitly, then rewrite the pose and physics from the new product's own affordance (`adaptation.md` §1).

> `Do not inherit the carrying method, grip, or placement from the style reference. The product is a
> <product type>, which is naturally <affordance>; restage the subject's pose, hand position, and body
> contact accordingly while preserving the reference's camera angle, framing, crop, lighting design,
> background, palette, and colour grading exactly.`

If the reference's action is physically impossible for the new product, also negate the old action in the
negative list (`no drinking gesture`, `no shoulder straps`, `no beverage container`) — otherwise a ghost of
the original object survives into the render.

---

## Block 4 — Scene declaration (one sentence, names the genre)

Always `<intensifier> + <genre> + <medium>`, optionally `inspired by <adjacent category>`.
> `Create an ultra-premium cinematic outdoor hero product campaign inspired by luxury adventure advertising.`
> `Create a luxury retro-editorial product photograph inspired by vintage 1970s–1980s design aesthetics.`
> `Create a premium high-performance sports lifestyle campaign image in a vertical editorial format.`

Genre vocabulary in use: commercial product portrait · editorial still-life · luxury beauty campaign ·
outdoor hero product campaign · expedition fashion campaign · lifestyle advertising photograph ·
conceptual still-life · flat-lay · macro product photograph · endurance-sports lifestyle campaign ·
café-meets-fashion campaign · surreal luxury still-life · consumer-electronics campaign.

---

## Block 5 — Composition & camera geometry

Every one of these that applies gets its own clause. **Use numbers.** The corpus is relentlessly specific.

- Frame position: `centered` / `slightly left of center` / `in the left foreground occupying approximately one-third of the frame height` / `lower half of the frame` / `positioned diagonally from the lower-left corner toward the upper-right corner`
- Rotation & tilt in degrees: `rotated approximately 15–20 degrees clockwise` · `tilted downward at approximately a 45-degree angle` · `at approximately a 35–45 degree angle` · `lid raised to approximately 100–110 degrees` · `at a 15–20° upward tilt`
- Camera height and angle: `straight-on at eye level` · `slightly below eye level looking upward` · `dramatic low-angle upward-looking shot captured from below shoulder level` · `top-down three-quarter camera angle` · `high-angle overhead perspective around 35–45 degrees` · `perfectly top-down flat lay`
- Crop bounds: `cropped from upper torso to feet` · `cropped from forehead to chin` · `tightly cropped from the upper chest to slightly above the head` · `only the lower torso and upper legs visible`
- Perspective register: `subtle three-dimensional perspective` · `slight three-quarter depth visibility` · `medium telephoto perspective` · `wide focal length creating powerful perspective distortion`
- Negative space, always stated: `generous negative space above the arrangement` · `abundant negative space` · `extensive negative space in the sky` · `clean negative space`
- Aspect ratio when it matters: `vertical 4:5 composition` · `vertical editorial format` · `portrait orientation`

### Product dominance — the frame has exactly one hero

An ad is not an editorial photograph: the product must be unambiguously the subject. **But dominance is not
the same as size**, and reaching for size first is what turns an environment frame into a bad packshot. Five
levers produce it, and a frame needs three:

1. **Size** — frame fraction. In an environment frame 30–40% of frame height reads as present; 50–60% reads
   as hero. State the number.
2. **Focus** — the product is the only critically sharp thing. Cheapest and strongest lever outdoors.
3. **Colour** — the product is the only saturated object in a desaturated field.
4. **Position** — nearest to camera, on the optical centre, or where the light actually lands.
5. **No competition** — *the one that gets forgotten.* Nothing else in frame may carry equal visual weight.

**The most common failure is lever 5, not lever 1.** A second detailed, warm-toned, similarly-sized object
beside the product splits the frame into two heroes and no amount of enlarging fixes it. Demote the rival
instead: crop it at the frame edge, throw it out of focus, push it further back, or desaturate it. Every
supporting prop should be legible but subordinate — state its role in the prompt (`partially cropped at the
right edge and falling to soft focus`), not just its presence.

**Do not resolve a weak environment frame by turning it into a close-up.** Context and craft are different
jobs: the environment frame says *where this product lives*, the macro says *what it is made of*. Collapsing
one into the other loses a slot and leaves the deck with a hole. Raise dominance with levers 2–5 and keep
the room.


---

## Block 6 — Environment and prop inventory

Object-by-object, each with **position + material + colour**. Never "some props". The corpus lists props
in reading order (left→right, foreground→background) and gives each a spatial anchor.

> `To the right of the product place a black ultralight mesh camping chair with thin folding aluminium frame, angled slightly toward camera. In front of the chair place a natural cut tree stump used as a small camp table. On the stump place a matte metal camping mug, a compact red outdoor accessory, and a small rugged camping item. A short piece of firewood rests beside the stump on the floor.`

Background is always named as a **seamless** surface with an explicit colour and gradient direction:
> `seamless cool silver-to-charcoal gradient background`
> `seamless warm beige studio backdrop with a soft monochromatic palette and no visible seams`
> `smooth gradient background transitioning from deep navy blue at the top into soft cobalt blue at the centre and fading into pure white toward the bottom`
> `matte charcoal-black upper backdrop fading into subtle darkness`
> `seamless matte black studio background with no distractions`

If the scene has a surface, name it too: `highly polished reflective acrylic surface creating a soft mirror
reflection beneath the subject` · `smooth matte cream-coloured tabletop` · `glossy reflective tabletop`.

---

## Block 7 — Lighting design

Never "good lighting". Always **instrument + position + quality + shadow behaviour**.

- Instrument: `large diffused softbox` · `large overhead softbox` · `two-light setup with key and fill` · `overhead spotlight creating a circular pool of light` · `strong rear key light` · `on-camera direct flash` · `cross-polarized professional studio lighting` · `natural window lighting with subtle bounce fill` · `golden-hour sunlight` · `bright overcast coastal sunlight`
- Position: `from camera-left` · `high front-left` · `from the upper left` · `front-left with soft fill from right` · `from behind and slightly below the product` · `a strong diagonal beam of warm sunlight entering from the upper right corner`
- Quality words: `soft diffused` · `highly controlled` · `bright crisp natural daylight` · `dramatic backlit` · `high-key` · `low-key`
- Named effects: `radiant halo effect around the silhouette` · `subtle rim light around the silhouette` · `controlled specular highlights` · `crisp catchlights in the eyes` · `luminous halo around the model` · `soft fog-like bloom`
- Shadow behaviour, always explicit: `realistic contact shadows beneath every object` · `gentle shadow falloff` · `deep but controlled shadows` · `smooth highlight roll-off without harsh specular clipping` · `subtle falloff toward frame edges`
- **The unlit side is a required clause, not an optional one.** State what happens where the light does not
  reach — open shadow with full detail, sculpted shadow with a bounce, near-silhouette with a rim, or a
  vignette running toward named corners — and say whether those darkest areas retain material detail. See
  the shadow-side table in `camera-lighting.md`. A rig without a shadow-side clause renders flat.

Key level maps to background: high-key ⇒ seamless white/ivory, minimal contrast. Low-key ⇒ matte black
backdrop, strong contrast, edge definition. Mid ⇒ grey or coloured gradient.

---

## Block 8 — Material physics & integration (the realism engine)

This is what separates these prompts from ordinary ones. Assert the physics of contact explicitly.

Always include, adapted to the scene:
- `realistic contact shadows where it touches the <surface>`
- `accurate ambient occlusion`
- `natural environmental colour bounce` / `environmental reflections of the surrounding <scene> on the product surface`
- `physically accurate reflections, refractions, and specular highlights`
- `materials respond naturally to light with physically accurate highlights, reflections and shadow transitions`

Add the interaction-specific physics:
- Worn: `realistic strap tension, natural fabric compression where it contacts clothing, authentic gravity pull, accurate interaction with the model's posture, weight distribution`
- Held: `realistic grip pressure, slight fabric tension, natural weight distribution, authentic gravity pull, subtle skin compression where contact occurs, realistic finger interaction`
- **Hands and skin lock** — paste verbatim whenever a hand, face or any skin appears. Hands are the highest-failure
  element in this format; a named block beats improvising the same sentence every time:
  > `Anatomically correct hands with five fingers, believable grip and natural joint positions. Realistic skin with
  > visible pores, tiny hairs and peach fuzz, fine lines, subtle wrinkles, natural nail texture, slight tonal variation,
  > small imperfections and realistic highlights. Keep the skin human and non-airbrushed. Avoid waxy, plastic, porcelain,
  > overly smooth or beauty-filtered texture.`
- **Name the contact points and count them.** "Held in the hand" is not a pose. State which part of which digit touches which part of the object, and say how many contacts there are (`exactly two points of contact and no others`). A grip supported at *both ends* of an object renders far more reliably than one cantilevered off a single end — the physics is self-evident, so the model has nothing to reinterpret.
- **Constrain scale with geometry the scene already contains, not with comparisons.** "As long as the palm is wide" is satisfiable by shrinking the palm; models invert it routinely. A structural constraint cannot be inverted: if the object must span from thumb tip to index fingertip, hand geometry fixes its size with no comparative instruction at all. When a pose keeps failing, look for a geometric constraint before adding more adjectives.
- Liquid: `realistic viscosity, gravity-driven flow, translucent highlights, pooled edges, drips, folds, layered reflections, accurate refraction, subtle magnification`
- Submerged / glass: `underwater-style magnification and optical distortion through the glass and liquid, realistic lensing effects, internal reflections`
- Cylindrical labels: `the label must wrap naturally around the cylindrical surface with physically accurate perspective, correct curvature, centred alignment, sharp typography, without stretching, floating, duplication, or warping`
- Repeating-pattern goods (monogram canvas, check, jacquard, print): `the pattern must follow the object's real surface curvature and panel geometry with correct repeat scale, spacing and alignment, continuing naturally across seams and folds, compressing accurately where the material bends, never stretched, re-tiled, re-drawn, invented, or duplicated at the wrong scale` — the single most common failure on patterned products, and it needs its own clause

Close the block with the anti-composite assertion (present in ~90% of the corpus):
> `The product should feel genuinely photographed on location rather than composited, never pasted, floating, distorted, stretched, warped, or AI-generated.`

---

## Block 9 — Colour grading & mood

Name the palette in explicit colour words, then the grading adjectives, then the emotional register.
> `Colour palette remains warm caramel, cream, amber, and white with luxurious premium food-photography aesthetics.`
> `Colour grading should be rich, warm and cinematic with deep contrast, glowing highlights, premium outdoor-brand aesthetics and high-end editorial polish.`
> `Preserve the cool winter colour palette, high contrast, crisp atmosphere and clean editorial outdoor aesthetic.`
> `Mood is refreshing, energetic, luxurious, premium, athletic, modern, and high-fashion.`

---

## Block 10 — Technical specification tail

A comma-run of camera body, lens, aperture, ISO, shutter, capture technique, colour depth, then quality
adjectives. See `camera-lighting.md` for the full selection tables.

> `Capture using a Phase One XF IQ4 150MP medium-format camera with a Schneider Kreuznach 120mm LS Macro Blue Ring lens, ISO 50, f/11, 1/160 sec, focus stacking, cross-polarized professional studio lighting, 16-bit colour depth, HDR capture, museum-grade colour accuracy, ultra-high micro-contrast, luxury commercial retouching, and native 8K ultra-high-resolution output suitable for premium global advertising.`

Lower-fidelity variant (when the look is a real-world camera rather than a studio digital back):
> `Shot on a full-frame professional camera with a 24–35mm lens, shallow-to-moderate depth of field, ultra-sharp product rendering, high dynamic range, photorealistic colour grading, natural imperfections.`

**These tails ride on an attached real photograph.** All 97 corpus prompts attach one, and that photograph sets
the tonal range. With no scene photograph (text-only, or rebuild), `HDR capture` combined with soft light
flattened a deck, which is measured. `retouching` and `8K` are untested text-only. Use a bare camera, lens,
aperture and ISO, plus the exposure clause from the realism gate (`principles.md` P1, P3).

---

## Block 11 — Negative list

Always a comma-run, always near the end, always prefixed `no`. Compose from:

`no text` · `no text overlays` · `no watermarks` · `no graphic overlays` · `no graphics` · `no logos added
beyond the original product branding` · `no additional branding` · `no duplicate branding` · `no packaging
redesign` · `no extra props` · `no additional objects` · `no extra accessories` · `no people` · `no
artificial glow` · `no artificial visual effects` · `no AI artifacts` · `no distorted anatomy` · `no extra fingers` · `no fused fingers` · `no impossible grips` · `no floating objects without believable contact` · `no excessive gloss` · `no perfect CGI surfaces` · `no over-sharpening` · `no
duplicated features` · `no duplicated textures` · `no floating elements` · `no unrealistic proportions` ·
`no perspective mismatches` · `no mismatched lighting` · `no compositing errors` · `no copy-paste
appearance` · `no creative reinterpretation` · `no cropping of the hero product`

The branding negative is worth its own sentence whenever the product carries a logo:
> `If the uploaded product contains branding, preserve only the branding already present on the uploaded product and do not generate any additional logos, labels, text, graphics, watermarks, or duplicate branding elsewhere in the scene.`

**`No text` in a brief means no text added to the scene — never the product's own printing.** A Codex deck read
a brief's *never generate an image containing text* as licence to blank the label (`render an intentionally
unlettered pack`), and every frame then read as a 3D mockup. The product's print is part of its identity and
belongs in the fidelity lock. Only a product that does not exist yet (Mode A-S) gets a text ban on the pack itself.

---

## Block 12 — Authenticity assertion (final sentence)

Always last. Pick one:
> `indistinguishable from a real professionally art-directed photoshoot.`
> `The final image should look like a real luxury lifestyle advertisement photographed by a professional commercial photographer, completely realistic, naturally styled, and indistinguishable from a genuine high-budget editorial campaign.`
> `The final result should resemble a museum-quality luxury advertising campaign photographed entirely in-camera with elegant minimalism and world-class commercial retouching.`

---

## Reusable locks — paste blocks rather than rewriting

Long campaigns benefit from a small set of verbatim blocks pasted into every prompt, rather than re-improvising the same
constraints each time. Repeating a lock **word for word** across a series is also what keeps a product consistent between
generations. Three worth keeping:

| Lock | Where | Why |
|---|---|---|
| Product fidelity | Block 2 | Stops redesign. Ends with `The environment may change; the product itself must remain visually consistent.` |
| Hands and skin | Block 8 | Hands are the highest-failure element in the format. |
| Negative list | Block 11 | Same bans every time; add scene-specific ones on top. |

Attribution: the paste-block pattern, the hands-and-skin lock and several negative phrasings (`extra fingers`,
`fused fingers`, `impossible grips`, `floating objects without believable contact`, `beautify`, `add gloss`) were adapted
from Digital Arnab's product-photography prompt pack (digitalarnabofficial.com, Aug 2026), not from the adgod corpus.
That pack also formats its prompts as labelled uppercase sections (`PRODUCT — CRITICAL:`, `COMPOSITION:`, `LIGHTING:`)
rather than one paragraph. Both formats work; there is no evidence here that either wins, so the corpus's single-paragraph
form stays the default. Consider the labelled form only for a prompt so constraint-dense that the paragraph stops being
readable to a human.

## Style rules that hold across all 62

1. One paragraph. No newlines, no lists, no headers, no emoji, no markdown.
2. Third person, present tense, declarative. Never "please", "I want", "try to", "you should".
3. Imperatives are reserved for `Preserve`, `Maintain`, `Recreate`, `Position`, `Place`, `Keep`, `Ensure`, `Match`, `Replace`, `Create`, `Capture using`.
4. Hedging is banned. `should` appears only in `should feel` / `should appear` / `should remain` constructions asserting a required outcome.
5. Numbers over adjectives wherever a number exists (degrees, percentages, counts, f-stops, focal lengths, `approximately eight thick golden-brown pancakes`, `exactly five ornamental goldfish`).
6. Repetition is deliberate. Product fidelity is restated 2–3 times per prompt in different words. Do not compress it.
7. Colours are always compound and specific: `burnt-orange`, `sage-green enamel`, `pearl-lilac`, `mocha-brown`, `charcoal-grey`, `ivory-beige`, `cobalt-blue`, `reddish-brown`.
8. Length: measured across all 62 corpus prompts — min 256, median 392, p90 505, max 569 words. Target the median for a normal scene; prop-dense still-life and multi-constraint recreations legitimately run 500+. Under ~250 fidelity starts dropping. Do not trim a prompt below the median to hit a round number.
