# Optics — research the material before you write the scene

Added 2026-09-19 after a v3 render failed in a way no lint or rubric could catch. The frame put the OLAPLEX
bottle on the tines of a horn comb. The bottle came out **opaque**: the tines ran up to its edge and vanished.
A bottle of clear acrylic full of transparent oil has to show the comb continuing *through* it.

The prompt did ask for it — `and the comb's own edge visible through the body` — one clause at the end of a
long physics comma-run. All seven v3 frames had exactly one such clause and every one was ignored.

**A see-through product is a compositional fact, not a physics footnote.** It belongs in the scene
description, with the thing behind it named and its distortion described. Physics lists at the end of a
prompt are where instructions go to die.

## Step 0 of any brief: what does this product do to light?

Before the scene, answer three questions about the product itself.

1. **Is it transparent, mirrored, translucent or matte?**
2. **What does it do to whatever is behind it?** (transparent: shows it, changed · mirrored: replaces it with
   a reflection of the room · matte: hides it)
3. **What does it do to whatever is around it?** (casts colour, throws caustics, bounces light)

Write the answers into the scene. If the answer to 2 is "shows it", **name what is behind and say what
happens to it.**

## Transparent products: the numbers

For OLAPLEX Nº.7 — clear acrylic body, clear acrylic cap, transparent golden oil:

| Material | Refractive index |
|---|---|
| Air | 1.00 |
| Clear acrylic (PMMA) | **1.49** |
| Dimethicone / silicone oil | **1.40** (dimethyl silicones run 1.35–1.45) |

Sources: PMMA 1.49 and dimethyl silicone 1.399 are standard published values (see below).

What follows from those three numbers:

- **The air-to-acrylic jump does nearly all the bending.** Acrylic to oil is 1.49 → 1.40, almost matched, so
  the inner wall is faint and **the filled bottle behaves as one solid block of glass**, not as a wall plus a
  liquid.
- **What that block does depends on the bottle's cross-section, and this is where I got it wrong.**

  | Bottle | Optically | What happens to what's behind |
  |---|---|---|
  | **Round / cylindrical** | a thick positive lens | **magnified**, displaced sideways, and **flipped left to right** if far enough back |
  | **Flat-faced prism** (square, rectangular, rounded-square — **including OLAPLEX Nº.7**) | a **plane-parallel slab** | lateral magnification is **exactly 1.0**. Same width. A small sideways shift and a colour cast, nothing more. |

  A plane-parallel slab has flat, parallel entry and exit faces, so every ray leaves parallel to how it
  entered. It displaces the image; it cannot enlarge it. **The lensing on a flat-faced bottle happens only
  at the rounded vertical corners**, where the stripes or edges behind compress hard, bunch together and
  vanish into the total-internal-reflection band.

  Corrected 2026-09-19 after two failed stripe-card tests. The prompt had asked for the image behind to be
  "broadened to roughly half again its width" on a flat-faced bottle. **Asking for physics the glass cannot
  perform is a reliable way to get no physics at all** — the model has nothing consistent to render, so it
  falls back on its prior, which is a uniform amber body. Check the cross-section before writing the clause.
- **The outer edges do not show what is behind them.** Past the critical angle — about 44° for n≈1.45 — rays
  totally internally reflect, so the outer tenth of the body reads as a bright or dark band carrying a
  compressed smear of the room, not the object behind.
- **Path length tints and darkens.** Through the thick middle the scene behind goes deeper amber than through
  the thin edges.
- **The printing is on the OUTSIDE wall**, so it stays sharp and undistorted and blocks whatever is behind
  it. Only the unprinted areas of the body show the scene.
- **The oil's top surface is a hard optical break.** Above the fill line there is air inside the bottle, so
  that band bends things differently and the meniscus reads as a visible line.

## Wording that carries it

Put this in the scene sentence, not the physics tail. Name the object, say where it reappears, say how it
changed:

For a **flat-faced** bottle (OLAPLEX Nº.7):

> `The two tines that pass behind the bottle are visible straight through it at very nearly their true
> width, neither enlarged nor shrunk, shifted only slightly sideways, their edges softened and their colour
> pushed deeper amber by the oil; they break at the printed type, which sits on the outer wall and stays
> sharp and flat; and toward each side they compress hard as the flat face turns into the rounded corner
> before vanishing into the bright band of total internal reflection along the outer edge.`

For a **round** bottle, and only then:

> `…magnified about half again and shifted sideways from where they enter…`

Rules of thumb:

- **Name the specific object** behind it. "Objects behind are visible" renders as nothing.
- **Say the magnification, correctly for the cross-section** — "half again as wide" for a round bottle,
  "at very nearly their true width" for a flat-faced one — **and the displacement**.
- **Say where it stops** — at the label, at the edge band, at the meniscus.
- **Repeat it once** in the physics tail, but only after it exists in the scene.

## Choose an object that can actually be seen through it

**2026-09-19, honest correction.** After the see-through wording was moved into the scene sentence, the comb
frame *still* rendered with the tines invisible behind the bottle. Before blaming the model, do the physics:
the comb is **dark brown horn** and the medium is **saturated amber oil**. A dark object seen through a deep
amber filter, against a dark red ground, is genuinely almost invisible. The render was closer to correct than
the prompt was.

**The fix is contrast, not more words.** If you want the see-through to read, put something behind it with
tonal or colour separation from the oil:

- Good behind amber oil: a pale or white object, a bright metal edge, a hard specular line, a strong
  geometric pattern in a light tone, skin.
- Bad behind amber oil: dark brown, black, deep red, anything in the oil's own hue.

State the see-through only where it can be seen. Asking for it against a dark prop writes a promise the
optics cannot keep.

## Mirrored and matte, for completeness

- **Mirrored** (chrome, polished metal, gloss lacquer): it does not show what is behind, it shows the room in
  front. Give it a world to reflect and one hard source — the existing rule in `SKILL.md`'s realism gate.
- **Translucent** (frosted glass, HDPE, paper): what is behind becomes a soft coloured shadow, not an image.
  Say "a diffused silhouette", never "visible through".
- **Matte**: it occludes. Nothing to state.

## Reject list for a transparent product

- Objects that stop dead at the product's outline.
- The scene behind continuing **unchanged** through the body — no displacement, no colour cast, no
  compression at the corners. (On a flat-faced bottle, unchanged **width** is correct; unchanged everything
  else is not.)
- The printed label distorting along with the contents. It is on the outside; it stays flat.
- Uniform brightness across the body with no dark or bright edge band.
- The fill line invisible.

## Sources

PMMA refractive index ~1.49 and dimethyl silicone ~1.399, with dimethyl silicones spanning 1.35–1.45:
[Personal Care Magazine, refractive index modification of silicone polymers](https://www.personalcaremagazine.com/story/10596/refractive-index-modification-of-silicone-polymers)
· [Cargille index matching liquids](https://www.cargille.com/matching-liquids/)

---

# The keyword set for a transparent bottle of liquid

Built 2026-09-19 by counting the **30 of 104 corpus prompts** whose product is a transparent vessel with
liquid in it, then checking those keywords against two pixel-measured official pack shots. Frequency alone
is not evidence — adgod's own transparent-product renders carry the same flat, emissive oil the client
rejected in ours. So the tiers below separate *what he says* from *what the measurement says*.

## Tier 0 — the anti-keywords. Delete these first.

**The single highest-value edit.** Asking for a glow is how you get a glow.

| Word | In corpus | Verdict |
|---|---|---|
| `luminous` applied to the product, its liquid, or light it casts | 6 of 30 | **delete** |
| `glow` / `glowing` applied to the product | 4 of 30 | **delete** |
| `radiant halo`, `soft luminous glow cast beneath it`, `luminous transparency` | 3 | **delete** |

Keep them for **skin and hair** — `luminous skin highlights`, `skin luminosity` — where they are correct
and desirable. The distinction is what the word is attached to.

This was found the hard way: a deck whose lock block said **LIGHT, NOT GLOW** still rendered glowing
bottles, because adgod's scene text 200 words below asked for *"a soft luminous glow cast beneath it"*.
**Audit the whole prompt for contradictions before blaming the model.**

## Tier 1 — physics. None of these are in adgod's prompts. All four are measured.

These are what actually separate a photographed bottle from a rendered one.

1. **Specular hierarchy.** On the real pack shot the brightest 0.1% of the product sits at **saturation
   0.03** — colourless white — while the oil peaks at **95% brightness at saturation 1.00**. A real photo's
   brightest pixel is a white specular on the cap and glass edges. An emissive render's brightest pixel is
   the liquid itself.
   > `The brightest pixels are colourless white speculars on the clear cap and the glass edges; the oil is never the brightest thing in the frame and never reaches full brightness at full saturation.`

2. **Internal tonal map.** Measured across the body: silhouette edges **149–163**, centre **210–220**, the
   band under the cap rim **140** (darkest), thick glass floor **198**. A 2.2× range with a specific layout,
   caused by path length through the liquid.
   > `Near-white acid yellow through the centre where the light path through the liquid is shortest, deepening to dark bronze-brown along the left and right silhouette edges, darkest of all in the band under the cap rim, deeper again through the thick glass floor.`

3. **Lit side and shadow side.** Separate from (2) — that one is glass geometry, this one is the key light.
   > `One key gives the bottle a lit side and a shadow side, and the side away from the key both darkens and loses saturation, going brown rather than staying yellow. Any reflection of the bottle is darker and less saturated than the bottle itself.`

4. **A named object behind, with its transformation stated.** See the rules earlier in this file. "Objects
   behind are visible" renders as nothing, and the object must be pale enough to survive the amber.

## Tier 2 — adgod's house vocabulary. Use it; it sets the style.

Ranked by how many of the 30 transparent-vessel prompts carry it:

| | | |
|---|---|---|
| `refraction` | 21/30 | `physically accurate` | 20/30 |
| `transparency` | 18/30 | `contact shadows` | 16/30 |
| `specular highlights` | 12/30 | `liquid color` (matching the contents) | 9/30 |
| `crystal-clear` | 9/30 | `internal reflections` | 8/30 |
| `rather than composited` | 7/30 | `edge highlights` | 6/30 |

His canonical stack, verbatim:
> `physically accurate reflections, refractions, internal reflections, edge highlights, optical clarity`

## Tier 3 — situational, one or two at most

`subtle caustics` · `light transmission` · `magnification` · `optical distortion` · `lensing effects` ·
`liquid depth` · `glass thickness` · `refractive depth` · `surface tension` · `viscosity`

## Tier 4 — the liquid must behave somewhere

A sealed bottle of still oil is optically a solid block and will always read as resin. Establish the
material outside the container — coating a hand, a stretching pendant drop, a run that has already
travelled — and the contents read as liquid by inference. Full rule in `effects.md` Part 10A.

---

# A lock rule that describes the product will overwrite the scene

**2026-09-19, the finding that finally made see-through render, after four test runs.**

The lock block carried this, in capitals, at the top of every prompt:

> `LIQUID COLOUR. The oil is never one flat colour. Near-white acid yellow through the centre of the body …
> deepening steadily to dark bronze-brown along the left and right silhouette edges …`

That is a complete description of the body's appearance — **a smooth horizontal gradient with no vertical
structure.** A striped card seen through the bottle requires vertical structure. The two are mutually
exclusive, the lock was front-loaded and in capitals, and the scene's see-through clause was 300 words
below it. Three runs drew a smooth gradient, exactly as instructed.

Every optics clause written in those three runs was correct and irrelevant.

## The rule

**A lock rule may constrain how the product looks *when nothing is behind it*. It must never state what the
product looks like unconditionally, because the scene's whole job is to put things behind it.** Write locks
so they yield:

> `The glass is fully transparent and the oil inside is a clear transparent amber, not an opaque or painted
> fill. Whatever stands behind the bottle is seen through it, recoloured by the oil, and is never painted
> over by a smooth gradient. **Where nothing stands behind it**, the oil is still never one flat colour: …`

Same shape as the `luminous glow` contradiction earlier in this file, and the same drill: **after assembling
any prompt, read the lock block and the scene against each other and find the clause that makes the other
impossible.** That check has now caught the two defects that cost the most runs.

## And: describe the picture, not the derivation

The other half of the fix. Three runs derived optics — plane-parallel slab, magnification 1.0, lateral
displacement, critical angle. The run that worked described the finished frame:

> `…straight down the front of the bottle, seen through the transparent golden oil, those same stripes
> continue without interruption: six clear vertical bars of dark bronze-brown separated by bands of glowing
> transparent gold, standing directly in line with the black-and-white stripes above the cap and below the
> base … the bottle reads as a pane of gold-tinted glass standing in front of the card, not as a solid gold
> object placed over it.`

Do the physics to work out **what the picture looks like**, then write the picture. The derivation is for
you, not for the model.

---

# Transparent vs metallic: the read is absorption, not colour

**2026-09-19.** A render was rejected with *"it looks like the liquid inside is liquid gold, not oil. it
doesn't look transparent."* The amber was the right hue and the right saturation — measured off the real
pack shot — and it still read as molten metal.

**Colour is not what separates them. The mechanism is.**

| | Gets its colour by | Therefore |
|---|---|---|
| **Metal** | **reflecting** the environment off its surface | can be **brighter** than its surroundings · carries mirrored shapes and warm curved sheen bands **inside the volume** · shows nothing behind it |
| **Transparent liquid** | **absorbing** part of the light passing through it | is **always darker** than what is behind it · the only reflections are colourless speculars on the **outer glass surface** · what is behind it shows through, dimmed and tinted |

## The one test that settles it

> **Is the liquid brighter than the background, or darker?**

A filter cannot add light. Where a bright white background shows through the bottle it must read as a
**dimmed, softened, gold-tinted white — distinctly darker than the same background beside the bottle.** If
the body is brighter or more brilliant than what surrounds it, the render has made it a light source or a
metal, whatever hue it is.

This is the single most diagnosable transparency fault and it is visible at a glance, without measuring.

## Wording

> `The oil is a clear transparent amber that light passes through and is dimmed and tinted by. It is not a
> paint, not an opaque fill and not a molten metal. Because it is a filter it is never brighter than what is
> behind it: wherever the background or a prop shows through the bottle it reads as a dimmed, softened,
> gold-tinted version of that same thing, distinctly darker than that thing seen beside the bottle. There
> are no mirrored reflections inside the liquid volume and no warm metallic sheen within the body — the only
> reflections are crisp colourless speculars on the outer surface of the glass. No molten gold, no liquid
> metal, no chrome-like curved highlight bands inside the oil, no thick opaque honey.`

Note this sits **alongside** the absorption gradient, not instead of it: path length still governs where the
oil is pale and where it is deep. The filter clause governs whether it is a liquid at all.

---

# The headspace is the proof that it is a liquid

**2026-09-20, found by the client after every other transparency fix had landed.**

> *"liquids should have an air bubble on the top. you know when u tilt a bottle, an air bubble appears?
> that's literally it."*

Correct, and it is the cheapest and most reliable liquid tell there is.

**A liquid surface is always level with the horizon, never with its container.** Tilt the pack and the
liquid stays horizontal while the air above it becomes a **wedge at the raised shoulder**, so the fill line
cuts **diagonally** across the body and across the printed label. A solid coloured fill physically cannot do
this — which is exactly why its presence reads instantly as real liquid and its absence reads as a painted
object.

An earlier lock rule said *"the oil fills the body to a visible line just below the shoulder"* and that was
only half of it: it never said the line stays **level**, so on every tilted or lying-down frame the model
drew the fill line parallel to the bottle and the liquid went back to reading as a solid.

**PASTE — for any transparent or translucent container of liquid**
```
[PRODUCT] is not full. Its liquid surface is always level with the horizon, never with the container:
whenever [PRODUCT] is tilted or lying down the liquid stays horizontal and the air above it becomes a
clear wedge at the raised shoulder, so the fill line cuts diagonally across the body and across the
printed label. One fine air bubble sits under the surface.
```

**Reject:** a fill line parallel to the container on a tilted pack · no air gap at all · a bubble that
moves with the bottle rather than staying at the highest point.
