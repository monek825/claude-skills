# Effects catalogue — optical and material effects, with paste-ready blocks

Built 2026-09-19 from the local corpus: **104 adgod prompts / 15 decks** (`corpus.md`) and
**630 catalogued adgod images** (`~/Documents/adgod-prompts/refs/adgod-ig/CATALOGUE.jsonl`,
294 reference-photo · 194 adgod-output · 87 promo · 55 contact-sheet), plus the fashionnn decks.

Every clause marked **PASTE** is written to be dropped into a prompt as-is, with `[PRODUCT]` swapped.
Counts in brackets are occurrences in the 104-prompt corpus.

---

## 0. The grammar — how adgod actually writes an effect

Any effect he renders well is written in the **same five parts**. Effects fail when a part is missing.
This is the single highest-value finding in the file.

| # | Part | What it does | Corpus count |
|---|---|---|---|
| 1 | **Preserve clause** | lists `transparency` / `liquid color` / `glass thickness` among the locked product attributes | `transparency` ×31 |
| 2 | **Cause clause** | names the physical apparatus doing the optics, and says it is the cause | e.g. *"caused by the water-filled glass environment"* |
| 3 | **Physics stack** | `physically accurate` + 4–6 optical nouns in one comma run | `physically accurate` ×**76** |
| 4 | **Anti-composite clause** | *"…so it appears photographed naturally in-camera rather than composited"* | ×**25** |
| 5 | **Camera tail** | Phase One XF IQ4 150MP + Schneider Kreuznach lens | ×53 / ×48 |

`physically accurate` appears in **76 of 104 prompts**. It is the load-bearing phrase of the whole corpus.
It is never used alone — it always governs a list.

**The optical noun bank** (use 4–6, never all):
`reflections · refractions · internal reflections · edge highlights · edge glow · optical clarity ·
light transmission · subtle caustics · magnification · optical distortion · lensing effects ·
liquid depth · glass thickness · specular highlights · contact shadows · ambient occlusion ·
surface tension · adhesion · gravity behaviour`

### The cause clause is what people leave out

Wrong: *"with realistic refraction and distortion."*
Right (Liquid Death 01): *"…realistic underwater-style magnification and optical distortion through the
glass and liquid… Ensure the product inherits physically accurate reflections, refractions, magnification,
and distortion **caused by the water-filled glass environment**."*

A named cause gives the model a mechanism. A bare adjective gives it a mood.

---

## Quick index

| # | Effect | Family | Risk |
|---|---|---|---|
| 1 | See-through hero | refraction | high |
| 2 | Waterline step | refraction | low |
| 3 | Partial submersion | refraction | low |
| 4 | Liquid-glass layer | refraction | med |
| 5 | Filled-vessel lensing | refraction | med |
| 6 | Droplet micro-lens | refraction | low |
| 7 | Fogged screen | barrier | low |
| 8 | Frosted-glass silhouette | barrier | low |
| 9 | Blurred foreground body | barrier | low |
| 10 | Appliance door | barrier | low |
| 11 | Self-cast caustic | caustics | med |
| 12 | Water-film caustics | caustics | med |
| 13 | Coloured shadow | caustics | low |
| 14 | Prism / rainbow flare | flare | **high** |
| 15 | Flare through the product | flare | med |
| 16 | Glass bar / prism over lens | flare | **highest** |
| 17 | Condensation field | water | low |
| 18 | Carbonation cling | water | low |
| 19 | Splash at max impact | water | med |
| 20 | Pour stream | water | med |
| 21 | Viscous liquid forms | water | med |
| 22 | Foam drift | water | low |
| 23 | Ripple rings | water | low |
| 24 | Bubble raft | water | med |
| 25 | Ice | water | low |
| 26 | Mirror plinth | reflection | low |
| 27 | Found mirror | reflection | med |
| 28 | Magnifier prop | found optics | med |
| 29 | Found aperture | found optics | med |
| 30 | Product as filter | found optics | med |
| 31 | Gobo shadow | light | low |
| 32 | Wedge / beam | light | low |
| 33 | Long-lens compression | lens | low |

"Risk" = how often it renders wrong or AI-looking when under-specified.

---

# Part 1 — Transparency and refraction

## 1. See-through hero — *the object behind the product is visible through it*

The one we kept failing. Full physics in `optics.md`. Three non-negotiables:

- **Name the object behind.** "Objects behind are visible" renders as nothing.
- **State magnification and displacement.** A filled clear bottle is a thick positive lens.
- **Give it contrast.** Dark object + amber oil + dark ground = genuinely invisible. That is correct physics,
  not a model failure. Put something **pale, bright-metal or hard-specular** behind it.

**PASTE**
```
The [OBJECT] passing behind [PRODUCT] is visible straight through its body, magnified about half again
and shifted sideways from where it enters, its edges softened and its colour pushed deeper amber by the
liquid inside; it breaks at the printed label, which sits on the outer wall and stays sharp and flat, and
it disappears into the bright band along the left and right edges where the curve turns to total internal
reflection. The fill line reads as a hard horizontal break across the body.
```

**Fails when:** the object stops dead at the outline · the scene continues through unchanged (no
magnification) · the label distorts with the contents · no bright edge band · the fill line is invisible.

---

## 2. Waterline step — *half in water, the submerged half jumps sideways*

Cheapest convincing refraction in existence and adgod uses it straight.
Catalogue: *"Oral-B iO brush stood inside a tall glass of water… the handle refracting and stepping sideways
at the waterline, bubbles clinging to the glass. **Refraction is the entire trick and the split line sits
dead centre.**"*

**PASTE**
```
Stand [PRODUCT] upright inside a tall plain drinking glass filled with clear water to just past its
midpoint, shot dead level so the waterline runs horizontally across the centre of the frame. The submerged
half is visibly wider than the half above and steps sideways at the surface line, with a bright meniscus
ellipse where the water meets the glass; small clear bubbles cling to the inner wall and to the product.
Physically accurate refraction, internal reflections, edge highlights and optical clarity through both the
glass and the water, so it appears photographed in-camera rather than composited.
```

**Fails when:** the offset is missing (renders as a product standing in a glass) · the camera is above level
so the waterline becomes an ellipse and the step disappears.

---

## 3. Partial submersion — *a hand or prop under a sheet of water, flattened*

Catalogue: *"gripped by a hand that is submerged just under a sheet of water, so the fingers refract and
flatten while the pale-blue handle stays crisp above the surface. **Water used as an optical device, not as
splash decoration.**"*

**PASTE**
```
A hand holding [PRODUCT] is submerged just beneath the surface of a shallow sheet of still clear water, so
the fingers read broadened, flattened and slightly displaced by refraction while the upper part of
[PRODUCT] stays tack sharp in the air above the surface. The surface itself is nearly mirror-flat with a
few loose droplets suspended on it. Physically accurate refraction, surface tension and internal
reflections at the waterline.
```

---

## 4. Liquid-glass layer — *the whole product behind a thick clear layer*

adgod's Olaplex S05, the most extreme optical frame in the corpus. The typography warps with it.

**PASTE**
```
Transform [PRODUCT] into an artistic liquid-distortion composition where the entire product appears
submerged behind a perfectly clear layer of thick transparent oil or liquid glass, creating realistic
organic ripples, wave-like edge distortions, refracted typography, warped contours, magnified details and
fluid optical refraction across the entire product surface. Compose as an extreme close-up macro crop so
the product extends beyond the frame edges. Clean seamless pure white studio background, no props. The
liquid layer should create highly realistic lensing effects, internal reflections, translucent wave
formations, glass-like distortions and subtle bubbles trapped beneath it, varying in thickness so every
bend and warp behaves according to real fluid optics rather than digital effects. [PRODUCT] must appear
physically photographed through a layer of liquid rather than edited afterward, with natural optical
imperfections and realistic fluid interaction.
```

**Note:** this is the one place adgod lets the label distort — because the distorting layer is *in front of*
the label, not behind it. Rule 1's "label stays flat" applies to see-through, not to this.

---

## 5. Filled-vessel lensing — *product seen through a water-filled glass*

Liquid Death 01. The strongest single optical paragraph in the corpus.

**PASTE**
```
Place a large crystal-clear transparent glass vessel filled with highly carbonated sparkling liquid between
the camera and [PRODUCT], with thousands of ultra-fine bubbles attached to the glass walls and surrounding
the product, producing realistic underwater-style magnification and optical distortion through the glass
and liquid. Preserve the thick glass rim, glass thickness, internal reflections, refractions, highlights,
edge glow and realistic lensing effects. Ensure [PRODUCT] inherits physically accurate reflections,
refractions, magnification and distortion caused by the water-filled glass environment.
```

---

## 6. Droplet micro-lens — *each bead magnifies what is under it*

The detail that separates real macro from sprayed-on CGI water.

**PASTE**
```
Each droplet must exhibit physically accurate surface tension, adhesion, gravity, optical refraction,
internal reflections, realistic magnification of the underlying texture, and natural clustering along
edges, grooves and curved surfaces, with larger beads sagging and leaving thin runs behind them.
```

---

# Part 2 — Shooting through a barrier

The catalogue's own verdict on this family: *"**The barrier between camera and product is the entire
technique.**"* Four variants, all in adgod's references, all low-risk and high-payoff.

## 7. Fogged screen — *everything blurred except where the glass has cleared*

**PASTE**
```
Photograph [PRODUCT] through a fogged glass shower screen: heavy condensation and vertical runnels blur
the whole frame except one cleared band directly over the label, which stays legible and sharp. Water
beads cling to the near side of the glass and catch the key light as small bright points. Everything in
the scene sits in one colour family.
```

## 8. Frosted-glass silhouette — *hands behind the glass become soft shapes*

**PASTE**
```
[PRODUCT] is held against the near side of a sheet of frosted glass by two hands pressing from the far
side, so the hands read as soft diffused silhouettes with no visible detail while [PRODUCT] stays sharp and
its liquid glows. Contact points where the palms touch the glass are darker and more defined than the rest
of the hand.
```

## 9. Blurred foreground body — *the camera is another guest at the table*

**PASTE**
```
Shoot [PRODUCT] past a heavily out-of-focus foreground body occupying the right third of the frame, as if
the camera were another person sitting across the table. Focus falls only on [PRODUCT]; the foreground is a
soft dark mass with no readable detail. Long lens, shallow plane, unposed documentary framing.
```

## 10. Appliance door — *shot through the fridge / washer glass*

**PASTE**
```
Shoot [PRODUCT] through the closed glass door of a [FRIDGE / FRONT-LOADING WASHING MACHINE], with warm
interior light spilling out, reflections and fingerprints on the outer surface of the glass, and the door's
chrome trim catching a hard highlight along one edge.
```

---

# Part 3 — Caustics and cast light

Caustics are what a transparent product does to its **surroundings**. Most people prompt what the product
looks like and forget the product is also a lens pointed at the table.

## 11. Self-cast caustic — *the product throws a bright coloured shape*

Catalogue: *"Amber glass dropper bottle lying at an angle on a white surface, **throwing a long golden
caustic shadow**."*

**PASTE**
```
A single hard light source rakes across [PRODUCT] from the upper left, so the liquid inside focuses the
beam and throws a long bright caustic onto the surface beside it — a sharp-edged elongated pool of
concentrated colour inside the softer shadow, brightest where the body is thickest, with a fine bright rim
running along the shadow's edge. The caustic is the brightest thing in the lower half of the frame.
```

**Fails when:** rendered as a plain drop shadow. The tell is that a caustic is **brighter than the
surrounding surface**, not darker. Say that explicitly.

## 12. Water-film caustics — *ripple net across the ground*

**PASTE**
```
[PRODUCT] sits in a shallow film of clear water on a [SURFACE], overhead hard light casting a net of
rippling caustic lines across the surface around it, the pattern tightening where the water is shallower
and dissolving at the edges of the pool.
```

## 13. Coloured shadow — *transmitted colour, not a grey shadow*

**PASTE**
```
Hard low sun passes through [PRODUCT] and lands on the surface behind it as a saturated coloured shadow
carrying the liquid's own hue, with a clean bright core where the light passes through the thinnest part of
the body.
```

---

# Part 4 — Flare, prism, and the glass bar

**This is the risky family.** The user's instinct is right: done right they read as expensive, done wrong
they read as a filter. The rule that separates the two: **a flare must have a source you can point at in the
frame.**

## 14. Prism / rainbow flare

Reference (Moxie): *"a hard sun-star and rainbow prism flare breaking across the right of frame and through
her hair. **The flare is the styling.**"*

**PASTE**
```
A hard point sun sits just outside the upper-right frame edge and clips the corner of [PRODUCT], producing
one clean sun-star with defined rays and a single line of spectral flare ghosts running diagonally down
toward the opposite corner, the colours splitting from warm gold at the source to magenta and cyan in the
furthest ghost. The flare is an in-camera artefact of that one source — no overlay, no bloom across the
whole frame, and the product's own contrast stays intact where the flare does not cross it.
```

**Fails when:** rainbow is laid over the whole image (reads as a preset) · there is no visible source ·
the flare crosses the label and eats the type.

## 15. Flare through the product — *the product makes the flare*

fashionnn S05: *"A point light source positioned precisely behind or to the side of the white sunglasses
creates a real lens flare — golden horizontal light streaks radiating outward from both lenses like twin
star bursts. The lens flare is a practical effect from the light hitting the glasses directly."*

**PASTE**
```
A warm amber point source sits directly behind [PRODUCT] and slightly to one side, so the light passes
through its transparent body and throws horizontal golden streaks outward across the frame from the widest
part of the glass. The streaks are a practical effect of the light hitting the product itself, not a
post-processed overlay; [PRODUCT]'s own edges stay defined against a deep brown-black ground.
```

## 16. Glass bar / prism held over the lens — **outside adgod's corpus**

Honest finding: **adgod never does this.** Searched all 104 prompts and 630 catalogued images —
zero `glass bar`, `glass block`, `glass rod`, `prism`. His refraction always happens at an object *in the
scene*, never at a filter over the lens. Given how often the effect looks cheap, that restraint is probably
deliberate.

If you still want it, the technique is real: a polished optical-glass bar or prism held partly across the
front element, refracting the scene into a streaked or doubled band along one edge while the centre stays
clear. Quality of glass is the whole difference — cheap acrylic smears instead of refracting.

**PASTE (use sparingly)**
```
A bar of polished optical glass is held across the lower-left quarter of the lens, refracting that corner
of the scene into a soft smeared double image with a faint spectral fringe along its boundary, while the
centre of the frame containing [PRODUCT] stays completely clear and sharp. The transition between refracted
and clear areas is a hard diagonal edge, not a gradient, and the refracted region carries a real duplicate
of the scene rather than a blur.
```

**Fails when:** applied as a blur instead of a duplicate · the boundary is a soft gradient (reads as
vignette) · it covers the product.

---

# Part 5 — Water, liquid and foam

## 17. Condensation field
**PASTE**
```
Cover [PRODUCT] in dense realistic condensation: micro-droplets, medium beads and larger water drops of
varying size, each with accurate refraction, a single bright specular highlight and correct gravity
behaviour, the larger beads sagging downward and leaving thin clear tracks through the fine mist behind
them. Denser on the upper third, sparser where a hand or surface has touched it.
```

## 18. Carbonation cling
**PASTE**
```
Thousands of ultra-fine bubbles attached to the inner glass walls in vertical columns, rising in slow
strings from a few nucleation points, with a fine foam collar at the surface.
```

## 19. Splash at max impact
Oakley 01: *"photographed at the exact moment of maximum impact, with crystal-clear water sheets, stretched
liquid arcs, suspended droplets, sparkling highlights, and razor-sharp refractions."*
**PASTE**
```
Frozen at the exact moment of maximum impact: crystal-clear water sheets, stretched liquid arcs, suspended
droplets held in mid-air, sparkling highlights and razor-sharp refractions, every droplet individually
resolved with no motion blur and no foam spray haze.
```

## 20. Pour stream
**PASTE**
```
The liquid stream displays realistic fluid dynamics, subtle twisting motion, natural variation in
thickness, accurate gravity-driven acceleration narrowing the stream as it falls, transparent highlights,
internal reflections and premium high-speed photography detail.
```

## 21. Viscous liquid forms
Dior gloss: *"smooth curved surfaces, glass-like transparency, realistic refraction, subtle magnification
effects, soft highlights."*
**PASTE**
```
Thick viscous liquid forms with smooth curved surfaces, glass-like transparency, realistic refraction,
subtle magnification of whatever lies beneath them, soft broad highlights and slow sagging edges that
have not yet run.
```

## 22. Foam drift
**PASTE**
```
A thick collapsing drift of foam poured over [PRODUCT] and spilling off the shelf edge in falling strings
of water, shot from just below shelf level so the suds hang over the edge and drip toward camera, bubble
structure visibly coarse at the top and dissolving to liquid at the bottom.
```

## 23. Ripple rings
**PASTE**
```
[PRODUCT] stands in a shallow tray of water on a [COLOUR] ground with concentric ripple rings spreading
outward across the entire surface behind it, the rings tightest near the base and widening toward the
frame edges, clear bubbles clinging to the lower body. The water pattern is the only graphic in the frame.
```

## 24. Bubble raft
**PASTE**
```
A raft of large iridescent soap bubbles clustered around and behind [PRODUCT], backlit against a
white-to-grey gradient so every film catches a full rainbow sheen, built to a real sculptural mass with
bubbles of genuinely different sizes packing into each other rather than sprinkled evenly.
```

## 25. Ice
**PASTE**
```
Ice cubes with realistic transparency, internal fractures, trapped air bubbles in clouded cores, wet
melting surfaces, bright edge highlights and natural reflections.
```

---

# Part 6 — Reflection

## 26. Mirror plinth
**PASTE**
```
[PRODUCT] stands on a mirror-polished round tray, its full underside and label reflected cleanly beneath
it, the reflection darker and slightly compressed, with a hard contact line where the base meets the
surface and no gap or float.
```

## 27. Found mirror — *a real-world reflective surface, not a studio prop*
**PASTE**
```
[PRODUCT] is set on the polished [OLIVE-GREEN CAR WING / CHROME COUNTER] in low sun, the paintwork acting
as plinth and mirror at once, with a warm stretched reflection running away from the base and the
environment behind visible as soft curved bands in the surface.
```

---

# Part 7 — Found optics

adgod's most-copied move: an **ordinary object used as a lens**. No post, no filter, and it reads as
art direction rather than an effect.

## 28. Magnifier prop
*"glasses examined through a large magnifying lens clamped in a chrome laboratory stand: the glass enlarges
the camera module and the script while the arms outside the lens stay soft. **The prop does the argument —
it says 'look closer' without a line of copy.**"*

**PASTE**
```
[PRODUCT] is examined through a large round magnifying lens clamped in a chrome laboratory stand, the glass
enlarging [DETAIL] and the brand mark to roughly twice size and displacing them slightly from where they
continue outside the lens, while the parts of [PRODUCT] outside the glass stay soft and unmagnified. A thin
bright ring runs around the inside of the lens rim.
```

## 29. Found aperture — *a prop makes the crop*
**PASTE**
```
[PRODUCT] is held up through the centre of [A CLEAR INFLATABLE RING / THE EMPTY RIMS OF A PAIR OF GLASSES /
A TORN PAPER HOLE], shot from below so the opening frames a clean circle of [SKY] around it and everything
outside the opening blows out to a featureless bright highlight. The prop provides the vignette; no
post-processed darkening at the edges.
```

## 30. Product as filter over a person
*"Gisou hair oil pinched between finger and thumb and held directly in front of the model's eye, so the
amber glass throws a coloured shadow across her cheek and the bottle hides half her face."*

**PASTE**
```
[PRODUCT] is pinched between finger and thumb and held directly in front of the model's eye so it covers
half her face, the hard sun passing through its body and throwing a saturated coloured shadow across her
cheekbone; the skin visible through the transparent part of the product is shifted in hue and slightly
displaced from the skin around it.
```

---

# Part 8 — Light shaping and lens

## 31. Gobo shadow — 19 `hard-shadow` + `window shadow` / `leaf shadow` / `dappled` in the catalogue
**PASTE**
```
One hard source throws the shadow of [A WINDOW FRAME / PALM FRONDS / SLATTED BLIND] across the scene at a
steep diagonal, the shadow edges crisp near [PRODUCT] and softening with distance, with the product sitting
in a deliberate clear wedge of light between two shadow bars.
```

## 32. Wedge / beam
**PASTE**
```
A single narrow diagonal spotlight beam crosses the frame and lands on [PRODUCT], the surrounding field
falling to near-black within the beam's own falloff, visible only as a gradient on the ground and never as
a rendered volumetric shaft in the air.
```

## 33. Long-lens compression
*"Long-lens compression flattens the stack into stripes."* / *"turn a domestic interior into pure colour
field."*
**PASTE**
```
Shot on a long telephoto so perspective is flattened: background elements compress into flat parallel
bands of colour directly behind [PRODUCT] with no converging lines, and the out-of-focus surroundings
resolve into soft blocks of colour rather than recognisable objects.
```

---

# Part 9 — The universal tails

Append one from each group. These are adgod's, verbatim frequency noted.

**Anti-composite** (×25 — use one):
```
…so it appears photographed naturally in-camera rather than composited.
…so [PRODUCT] appears physically photographed within the scene rather than composited, with flawless
perspective matching and realistic environmental reflections.
…must appear physically photographed through a layer of liquid rather than edited afterward, with natural
optical imperfections and realistic fluid interaction.
```

**Camera** (Phase One ×53 / Schneider ×48):
```
Shot on a Phase One XF IQ4 150MP medium-format camera with a Schneider Kreuznach 120mm macro lens,
ultra-detailed commercial product photography, hyper-realistic textures, pristine colour accuracy,
flawless retouching, 8K resolution, magazine-cover quality.
```

**Negative tail** (`no artificial CGI appearance` ×4):
```
no artificial CGI appearance, no copy-paste look, no pasted-on labels, no mismatched lighting,
no distorted product geometry, no warped label, no floating product, no text overlays, no watermark.
```

---

# Universal reject list for any effect

- The effect is an **adjective** with no named cause.
- Refraction with **no displacement** — things line up either side of the glass.
- A caustic rendered **darker** than the surface around it.
- Flare with **no source** you can point at.
- Droplets that **do not magnify** what is under them.
- Foam, bubbles or ice at **one uniform size**.
- The effect **covers the label**.
- More than **two** effects in one frame. Every strong frame in the corpus runs one, occasionally two.

---

# What adgod does NOT use

Worth as much as the list above. Searched 104 prompts + 630 images:

| Absent | Count |
|---|---|
| glass bar / block / rod over the lens | 0 |
| prism filter | 0 |
| kaleidoscope / fractal filter | 0 |
| volumetric god-rays in air | 0 |
| explicit "bokeh balls" as subject | 0 |
| lens-flare overlays not traceable to a source | 0 |

His optical repertoire is: **things in the scene that happen to be lenses.** Water, glass vessels,
the product itself, a magnifier, a shower screen. Nothing between the lens and the set.

## Sources
Corpus and image catalogue are local. Technique confirmation for the glass-bar/prism family:
[Shotkit, glass prism photography](https://shotkit.com/prism-photography/) ·
[DIYP, prism lens photography](https://www.diyphotography.net/prism-lens-photography-light-effects/) ·
[Wikipedia, caustic (optics)](https://en.wikipedia.org/wiki/Caustic_(optics)) ·
[Distil Ennui, the structure of light: on caustics](https://www.distilennui.com/blogs/studio-journal/the-structure-of-light-on-caustics)

---

# Part 10 — Four rules added 2026-09-19 after three renders were rejected

v3 frames 01, 03 and 05 were rendered and rejected on three separate grounds. Each has a cause in the
prompt, and each generalises.

## A. A liquid reads as liquid OUTSIDE the container, never inside it

Rejection: *"the liquid oil looks frozen like amber."*

Correct diagnosis, and the physics agrees. A sealed clear bottle of **still** oil is optically a solid
block — matched refractive indices, no surface in motion, no event. There is nothing you can write that
makes still liquid behind glass look wet. It will always read as resin.

**adgod never tries.** Count his Olaplex deck: S01 stages two oil droplets outside the bottle, S02 coats an
entire hand in the product and hangs a stretching droplet from the base, S05 submerges the bottle in a layer
of the stuff. He establishes the material's liquidity **outside** the container, and the identical contents
inside then read as liquid by inference.

**Give the liquid somewhere to behave:**
- coating a hand or a surface in a glossy uneven film
- one larger droplet stretching downward from a low point, about to detach
- a thin thread falling and pooling
- a run that has already travelled and left a trail

**And light it so the body has internal dynamic range.** A bottle lit from the front is a flat coloured
slab. A bottle lit from **behind or hard from the side** becomes a lantern: a bright glowing core where the
path is short, edges going to near-black where the curve turns to total internal reflection, and the air
gap above the fill line reading paler and less saturated with a visible curved meniscus.

**PASTE**
```
The hand is generously coated in a glossy uneven film of the product's own liquid, catching the light in
long wet highlights across the knuckles, and one larger droplet hangs stretching downward from the base of
[PRODUCT] with physically accurate surface tension, transparency, refraction and viscosity, the liquid
colour matching the product contents exactly. [PRODUCT] is lit from behind so the liquid inside glows as a
bright core, the curved edges of the body fall to near-black bands of total internal reflection, and the
air above the fill line reads paler and less saturated with a visibly curved meniscus where it meets the
wall.
```

**Reject:** a flat, evenly saturated body with no bright core and no dark edge band · no visible fill line ·
a droplet that is a perfect static teardrop (reads as glass) · no liquid anywhere outside the bottle.

## B. One shiny thing per frame

Rejection: *"too flashy, too much light reflections."*

Cause: the prompt put wet hair, water beads, polished steel, a glossy clip and a chrome tap in one frame,
then asked for `specular highlights` in the physics stack on top. Every one of those throws its own hot
point. The render sparkles everywhere and reads as CGI.

**Before writing a frame, count the materials that can throw a specular** — wet hair, water, polished metal,
chrome, glass, gloss plastic, oiled skin. **The product is one of them.** Allow at most one other, and put
every remaining surface in matte or in shadow.

**The brightest point in the frame belongs to the product.** Say so.

## C. State the light once, in plain words

adgod: *"a large diffused softbox positioned slightly above and camera left"* · *"strong directional
sunlight from the upper left."* That is the whole lighting instruction. He never gives an angle in degrees,
never stacks a key plus a rim plus a fill plus a named specular.

Ours had been: *"one hard source from camera-left at thirty degrees"* **plus** *"a single hard specular
skimming the tumbler rim"* **plus** `specular highlights` in the physics stack. Three lighting instructions
competing, which is how a frame goes flashy.

**One sentence. One source. A direction in words, not degrees.** Then say what it does to the product and
stop.

## D. For a transparent liquid product, strip the set

Counted across adgod's own seven-frame Olaplex deck:

| | |
|---|---|
| Frames with **zero** props | **5 of 7** (S01, S02, S04, S05, S07) |
| Frames with one surface | 1 (S03, a chrome tray) |
| Prop-dense still life | 1 (S06, glass shelves) |

This **inverts** `composition.md`'s corpus-wide finding (95% carry a named prop, median 3). That number was
measured across all 194 outputs — tins, cans, backpacks, watches, opaque things that need a set to be
interesting.

**A transparent bottle of coloured liquid does not.** It is already the most optically active object
available, and every prop beside it competes for the same speculars and the same attention. adgod's answer
for this product class is a person, the product, its own liquid, and **named negative space**:

> *"suspended in mid-air against a clean soft off-white studio background… generous negative space
> surrounding the subject"* — S02
> *"a dark luxurious background created by shadowed hair and negative space… extremely shallow
> environmental distractions"* — S04

**Rule:** for a transparent liquid product, at most **two** frames in a seven-frame deck carry props.
The rest are the product, at most one person, its own liquid, and empty ground you have named as empty.
