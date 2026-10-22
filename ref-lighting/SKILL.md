---
name: ref-lighting
description: Replicate a reference photo's exact look (lighting, exposure, colour, softness, grain, water/texture, framing) and swap only the subject. Use when the user attaches a reference and wants it reproduced "exactly the same, just change the product", when a generated image "looks AI", "too bright", "too sharp", "lighting is different from the ref", or before writing any GPT Image / Nano Banana prompt that pairs a reference photo with a product photo. Includes a measuring script that turns a reference into look words and diffs a generation against it.
---

# ref-lighting: replicate the reference, swap the subject

## Why renders drift from the reference (VOID SCENT, 2026-10-15)

Two v1 prompts paired a Pinterest reference with a product photo and came back wrong:

| Frame | What came back | Measured |
|---|---|---|
| Bara held to the sky (ref2) | crisp, bright, saturated, hard sun star | 2.55x sharper, 1.31x more saturated, black point +19 |
| Bara + Mizu in shoreline foam (ref1) | bottles twice the size, big glossy bubbles, warm gold caustics | warmth +24, black point +27, darker; 2 bottles at ~40% frame instead of 3 at ~15% |

Cause: the prompt **re-described the scene in my own words** (550-680 words: "hard direct sun", "caustic lines", "30% of frame", "high-end retouching, 8K") and treated the ref as a loose style guide. GPT Image follows text over image. Every sentence about the scene gives it room to swap the photo's actual look for its default commercial look. The product plate makes it worse: the plate is a crisp studio photo, so the bottle comes out crisp and the scene follows it.

## Round 2 failures (v2 edit prompts, same day)

The edit framing fixed composition and colour. Two failures were left:

1. **Silhouette inheritance.** The model fitted the new bottle into the **old object's outline**, and kept everything the old object had shaped:
   - 04: bottles bent to follow the straight tubes.
   - 06: the water cavity kept the old square bottle's straight edges and corners, leaving an empty air gap beside the curvy bottle.
   - 09: the bubble funnel kept the old outline and the whole bottle warped.
   - 08: bottles flared wider at the bottom like the old cylinders; reflections and shadows were the old shapes.
   - 01: the waisted bottles came out rectangular, like the Polo bottles.
   Cause: "same place, angle and size as the original" also carries over the original's shape.
2. **Over-sharpening is systematic.** All 5 renders measured 1.65–2.56x sharper than their ref, with harder edges (edge_p99 up to 1.6x) and bluer light. The user called it "too intense, details too sharp". Global brightness and saturation were almost identical, so **what people read as "intense" is micro-contrast and hard glints, not exposure.**

## Round 3 (v3 prompts): what was fixed and what is still open

09 (underwater) passed. Four problems were still open:

1. **The shape lock overshot.** "S-curves that pinch in and swell back out" made the bottles **too wide and curvy**. The real waist is about 0.9 of the shoulder width, and the body is about 2.0x as tall as it is wide. Write proportions in numbers and add a strength word ("a soft pinch, not a dramatic hourglass", "never wider, shorter or curvier than the product image"). A vivid shape word gets exaggerated.
2. **Caps get "normalised".** The product's cap is a cube mounted on its corner: turned 45° around the axis and tipped 45° forward, with a V-notch above each shoulder. The model kept rendering it as a flat-sitting cube. Any non-default orientation needs its own **orientation lock**: the rotation in degrees on each axis, what points at the viewer, and "fixed to the bottle, keeps this orientation when the bottle lies, tilts or sinks".
3. **Air sleeve.** Even after the splash was rebuilt, the water left a hollow channel along the bottle's sides (the old bottle's volume). Name it: `no air sleeve, hollow channel or gap along either side or under the base: the water touches the glass directly`.
4. **Inherited shadows.** Ref7's floor shadows kept the old bottles' shapes and positions. Shadows are never fixed by a shape lock, so delete and recast them explicitly: `remove the original shadows completely; each new object casts exactly one shadow, offset in the same direction and distance as in Image 1, shaped like its own outline; no other dark shapes`. When masking, brush over the shadows too.

## Round 4 (v4 prompts)

1. **The orientation lock overshot too.** "Lowest corner points down into the collar, a V-notch on each side" rendered as a cap **crushed and dented into the bottle**. Words like *into*, *notch*, *pinch*, *softened* or *pressed* read as deformation. Describe the part as a **solid, undented block that sits ON its mount**, call the gaps **air, not dents**, and add a no-deformation list (`no face crushed, caved in, pinched, crumpled or pressed into the bottle; every face convex with smooth unbroken reflections`). Lead with `copy the cap exactly from the product image` and keep the geometry to one sentence. Each extra geometric clause is something else the model can over-apply.
2. **Floating vs standing.** v1-v3 put the ref8 bottles "standing on a submerged step", so they rendered upright, sitting on the water like figurines. The user wanted them floating like the originals. When the ref object floats, write its **state**: `floating, not standing; bobs low, waterline crosses just below [mark]; most of the body under the surface, seen blurred and shifted through the water; tilts N° and M° in different directions; meniscus ring where it pierces the surface; nothing suggests a floor`. Don't overrule what the ref shows with your own physics ("glass sinks"). In replicate mode the ref decides.

## Round 5: refraction is what puts an object in water

Floating (v5) didn't match ref8 either: the bottles still hovered. The user found the cause: **water distortion.** In the ref, everything below the waterline is refracted (wavy edges, broken horizontal bands, smeared print, a sideways shift, melting into the reflection), while the part above the water is crisp. The renders drew the whole bottle sharp and unbroken down to the base, so it read as hovering or standing on the water, whatever the prompt said about floating, depth or tilt.

Rule for any partly submerged subject: state the waterline height on the product (`crosses just below the logo`), then write a refraction sentence: `everything below the waterline is seen through rippling water: wobbly, wavy-edged, broken into shifting bands, displaced sideways, print bent and smeared, melting into its reflection; only the part above the water is clean and rigid; the glass is rigid, only the view through water distorts it`, and end with `its lower half is never shown sharp and undistorted`. The last clause matters because the rigid/no-warp shape lock otherwise suppresses refraction. Use a hidden submerged platform to keep a standing object upright, and don't tilt it unless the ref is tilted.

Colour, same round: v5 measured warmth -30 against the ref's -9. GPT pool water drifts toward electric cyan, which the user reads as "not dull enough". Write `muted, slightly greyed teal, warmer white balance, about 20% less saturated` for any water ref.

## Round 6: say what must NOT be visible

v6 had a refraction sentence and still rendered the **whole bottle sharp down to its base**, with a ring drawn round its middle and a reflection underneath. It read as standing on top of the water and leaning. Lessons:

- **Positive descriptions of hidden parts get ignored; negative visibility works better.** Write `the bottom of the bottle is not visible at all: no base, no bottom edge, no bottom corners; its crisp outline ends at the waterline`.
- **Anchor the waterline to the product's own marks**, not to a height fraction: `between the logo and the name: cap, shoulder and logo above; name, volume and base below`.
- **Fight perceived lean with frame geometry:** `vertical axis exactly parallel to the left and right edges of the frame and to the other bottle`. "Upright" alone isn't enough at a three-quarter top-down angle.
- **A near-miss render is fixed faster by a follow-up edit than by regenerating.** Brush only the wrong region (here the lower halves plus their reflections) and send a short prompt that changes only that region. Ship a follow-up block like this (`08b`) next to any prompt that has failed twice.

## Round 7: perspective mismatch reads as tilt

The 08 bottles still "leaned" after the axis was locked parallel to the frame. The cause: the bottles were drawn **from eye level (side view, the product plate's angle)** while the water was seen **from 45° above**. Mismatched perspective reads as a lean or hover. The product plate's camera angle leaks into the render. Always state the camera elevation for the subject: `seen from the same high camera angle as the scene, looking down ~N°: the top of the product clearly visible from above (top plane foreshortened, cap top face seen from above), body foreshortened`.

## Round 8: parts shrink unless the prompt insists on their size

The caps came out about 0.6x body width; the real cap is the full body width or wider. "As wide as the body" wasn't strong enough, because the model shrinks a heavy decorative part toward a generic small cap. Size the part against its neighbour with a floor and a limiter: `at least as wide as the widest part of the body, slightly overhanging; never a small knob on top`.

## The rule

**Replicate mode is an edit, not a generation.** Image 1 (the reference) is the authority on everything. The text names only what changes: the subject. Everything else gets one blanket "keep exactly", plus the measured look words, because those are the "flaws" the model would otherwise fix.

- Keep it short: 120-220 words. Long prompts make the model regenerate the scene.
- Open with `Edit Image 1.` and do not write "create", "generate" or "ultra-premium".
- The subject's size, position and angle are **copied from the object it replaces**. Measure it in the ref (percentage of frame height); never choose it.
- The new subject must have the **same softness, grain, exposure and white balance** as the ref. Say it outright: "not sharper, brighter or more saturated than the rest of the photo".
- **Shape lock, every prompt.** Describe the product's 2D outline in plain geometry (which sides curve and where, whether the top and bottom are the same width, where it flares or tapers, how big the cap is relative to the body). Add `rigid: never bends, stretches or warps`. Then: `Do not fit it into the outline of the object it replaces; rebuild everything that touched the old object (water, splash, air pockets, bubbles, liquid, shadows, reflections) around this bottle's own outline.` Copy only the old object's **position, angle and footprint**, never its shape.
- **Orientation lock** for any part that isn't axis-aligned (a cap on its corner, a tilted label, a twisted handle): give the rotation in degrees on each axis and what faces the viewer, and say it is fixed to the product.
- **Proportions as numbers plus a limiter**, never vivid shape words alone ("waist about 0.9 of shoulder width, a soft pinch, not a dramatic hourglass").
- **Contact and shadow cleanup, by name:** `no air sleeve / gap where the old object was` for water, and `remove the original shadows; recast one per new object` for every shadow in the ref.
- **Softness line, every prompt, even when the ref is sharp.** GPT Image renders about 2x sharper than any ref. Write: `Match the camera softness exactly: crisp edges, star-shaped glints and high micro-contrast are wrong here; keep the subject and everything around it as soft and grainy as Image 1.` If the ref is backlit or sparkly, also write `light gentle rather than intense, sparkles small, soft-edged and sparse, about 15% less saturated than a typical render; when in doubt, softer and duller`.
- **Masking (ChatGPT select/brush):** paint the object **plus everything it shaped**: splash cavity, bubble trail, wet ring, shadow, reflection, liquid coating, fabric bulge. Anything left unpainted keeps the old outline.
- Ban anything not in the ref: sparkles, sun stars, flare, caustics, droplets, props, text.
- Count mismatch (ref has 3 objects, you have 2 products): say what fills the empty slot, and tell the user it changes the composition.

**Banned words in replicate mode:** ultra-premium, commercial, editorial, high-end, retouching, 8K, HDR, ultra-detailed, crisp, tack-sharp, focus stacked, studio (unless the ref is a studio shot), vibrant, cinematic, glow, sparkle, and any light direction or effect you invented rather than saw.

## Step 0: product plate (do this before any frame)

The biggest recurring failure was **size and proportion drift**. Caps came out too small, bodies too wide or long, and caps sunk into the neck, and fixing them one at a time made other parts worse. The cause: the only product image was a lifestyle shot (fingers hiding the edges, cap seen from below, bottle tilted), so the model guessed the geometry differently in every frame.

Fix: **generate one clean product plate first** (ChatGPT or Codex `image_gen`) and use it as the product image in every later prompt.
- Inputs: every real product photo.
- Layout: plain light grey seamless, even light, no hands or props. One row: each product front-on at eye level, the same scale, side by side. (A 45° row was tried on 2026-10-15 and came out nearly identical to the front row, with the cap unchanged. Drop it.)
- Write the proportions as numbers, with the cap/body relation stated (`cap exactly as wide as the body, almost as tall as wide, sitting on top of the collar`).
- **Check it before use:** proportions against the real photo, cap seated not sunk, print correct. Fix any single error in the same thread. Save it as `plate.png` in the campaign folder.
- In every replicate prompt: `Image 2 is the authority on proportions`. Point at the right view (`the Mizu on the right`).
- **The plate carries its own studio background into the product.** The liquid comes out as a flat block of colour lit for grey seamless. Every prompt that uses the plate needs a transparency line: `liquid and glass transparent; the scene behind shows through, tinted and bent; shade changes with the background; the plate's flat studio colour must not carry over`.
- **Size anchor when the replaced object has a different shape:** match only the **height** (the top of the new cap = the top of the old object), and take the width from the plate. Never inherit the old object's width.
- Abandon a frame when the ref object differs too much from the product in shape (tubes or wide flasks versus a slim bottle) **and** it has failed 3+ fix rounds. Swap in a ref whose object is close in silhouette instead.

## Workflow

1. **Measure the ref.**
   ```bash
   python3.13 ~/.claude/skills/ref-lighting/scripts/measure.py REF.jpg
   ```
   This prints a numeric card plus look words (exposure, contrast, black point, clipping, saturation, colour cast, sharpness, grain). Paste the look words into the prompt's LOOK sentence. Caveat: on frames with no flat area (foam, sand, fabric everywhere), the grain and sharpness numbers read the texture, not noise, so check those two by eye.
2. **Read what the script can't see,** by eye: object count, subject footprint (percentage of frame height), position, angle, texture scale (bubble size, ripple size), light direction, focus plane.
3. **Write the prompt** from the template below.
4. **After a generation, diff it:**
   ```bash
   python3.13 ~/.claude/skills/ref-lighting/scripts/measure.py REF.jpg GEN.png
   ```
   It lists every measure outside tolerance with the phrase to add. Then compare composition by eye (count, size, texture scale).
5. **Fix one thing per round,** the biggest delta first. In ChatGPT, reply in the same thread ("keep everything, make it softer and less saturated to match Image 1") rather than starting over.

**Strongest option for "exactly the same":** in ChatGPT, open the reference itself, use the image **select/brush edit tool** to paint over only the old product, and attach the product photo with the prompt. Unselected pixels stay as they are, so the light, water and grain are the real photo's. Use the full-prompt route only when the subject's shape is very different from what it replaces.

## Template

```
Edit Image 1. Replace only [the bottle / the N bottles] with [product] from Image 2[ and Image 3]. Keep everything else in Image 1 exactly as it is: the framing and crop, the camera angle and distance, [2-4 concrete elements of the ref: sky, foam, sand, hand, fabric], the direction and quality of the light, the exposure, contrast, colour cast, softness, grain and every texture at the same scale. The new [product] sits in the exact place, angle and size of the original [object] — about [N]% of the frame height, [pose in ref terms]. It must look photographed in that same moment with the same camera: same focus softness, same grain, same haze, same white balance and the same light falling on it, not sharper, brighter or more saturated than the rest of the photo. [Compact product lock: material, cap, liquid colour, exact print text and layout from Image 2.] [Shape lock: the 2D outline in geometry + body-width proportions + rigid + "do not fit it into the old outline; rebuild water/splash/bubbles/shadows/reflections around its own outline".] [Interaction rebuild for this scene, e.g. "the water wraps tightly against its curved sides, no straight edges or air gap left from the original".] [Count/spacing note if needed.] [Softness line.] Look to match, measured from Image 1: [look words]. Remove the original [object]'s cap, label, logo and text completely. Add nothing that is not in Image 1: no sparkles, sun stars, lens flare, light streaks, caustics, extra droplets, props or text.
```

## Relationship to adgod-prompt

`adgod-prompt` writes 12-block **generation** prompts: new scenes, a new look, polished commercial finish. This skill is the other mode. When the user says "same as the ref", it wins, and the adgod finish tail (HDR / retouching / 8K) must not be added.
