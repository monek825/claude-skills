# Where the ideas come from

This page exists because the skill could execute an adgod prompt long before it could think of one. That
gap had a specific cause, and the cause is documented below.

## The finding

**These prompts are not descriptions of invented scenes. They are descriptions of photographs that already
exist.** Measured across the corpus: **39 of 62 prompts** contain explicit transcription language — "recreate
the exact composition", "as shown in the reference", "replace the original featured item", "maintain the
exact refined clutter level, spacing, layering, and object relationships of the reference image". The
L'Occitane hand-cream deck is **7 of 7**.

Per deck: Rolex 7/7 · Liquid Death 7/7 · Nothing 6/7 · Rhode 5/7 · Matchaeologist 3/7 · Chamberlain 3/7 ·
North Face 2/7 · Dior 2/7.

The giveaway is the specificity. From the hand-cream deck, prompt 04:

> a long metal scoop extending diagonally from the upper left area, a cylindrical metal measuring cup
> resting in the upper right quadrant partially surrounded by foam, and a polished double-sided metal
> jigger placed diagonally in the lower right section of the tray

Nobody invents a double-sided jigger in the lower right. That is a person **looking at a photograph and
transcribing it quadrant by quadrant.** Same in prompt 02's prop list, same in North Face 01 ("preserve the
exact body orientation, shoulder position, head angle and overall silhouette of the reference image").

So the creative act is **selection and transcription**, not imagination. The scene was art-directed by a
professional photographer, shot, published, and proven. The work is finding it and describing it exactly.

## So can this skill invent anything?

Yes — but not where people expect. **The invention is the concept; the photograph is the evidence that the
concept can be lit.** Those are two separate acts and the skill does both.

The four heuristics below are generative, not descriptive. "Build the set out of the product's own material"
applied to an aluminium tube produces a silver tray, a stainless scoop and a chrome jigger — a scene nobody
had photographed for that client. "When the benefit is invisible, find an object that physically has it"
produces the mohair glove. Neither came from copying a frame; both came from reasoning about the product and
then finding a photograph that already solves the lighting, the palette and the spatial logic.

What the skill refuses to do is generate a scene **from an abstraction** — "editorial prop tableau", "premium
lifestyle" — and write it straight into a prompt. That path has no jigger in the lower right, and it is what
makes output look like stock. The reference is not a substitute for the idea. It is the proof that the idea
survives contact with real light.

So: concept invented, execution transcribed. If a concept genuinely has no photographic precedent anywhere —
library or web — that is worth noticing rather than pushing through. Usually it means the concept is not yet
concrete enough to photograph, and the fix is to make it more physical, not to write it more vividly.

## Why the archetype menu underperforms

`archetypes.md` lists 18 reusable scenes. That is a **menu**, and a menu produces menu-grade output: the
scene is generated from an abstraction ("editorial prop tableau") rather than from a specific photograph
that already works. Abstractions have no jigger in the lower right. They have no reason for any particular
object to be present, so the objects come out generic and the frame looks like stock.

Use `archetypes.md` to name the *kind* of frame a deck still needs. Do not use it as the source of the
scene. **Source the scene from a real photograph.**

## The pipeline

**Source from non-adgod photography first** (`web-sourcing.md`, whose rubric keeps AI-generated images,
moodboards and flat snapshots out), **and memory last.** The local library (`library.md`) is adgod's own
selection. Use it for craft calibration and as a negative index (`signature.md`), not as a scene source. In
the rebuild stage it is off limits entirely. Describing a photograph from memory is step 1's fallback, not
its first move. With no photograph at all, the prompt must carry the realism itself (`principles.md` P1–P6).

1. **Source.** Find a real photograph — a published campaign, an editorial spread, a photographer's
   portfolio, a Pinterest board. It should already contain a product roughly the shape of the client's, or
   a clear place where one would sit.
2. **Transcribe.** Describe it object by object, quadrant by quadrant, material by material, with the
   lighting instrument and the palette named. Nothing abstract.
3. **Swap.** Add the replacement instruction: *"the product must replace the original featured item while
   preserving the exact composition, object placement logic, camera angle, styling philosophy and visual
   balance of the reference image."*
4. **Adapt.** Add the affordance-adaptation clause: *"automatically adjust scale, orientation and grip
   placement according to the product's dimensions while preserving the overall composition."* See
   `adaptation.md`.
5. **Lock.** Fidelity lock, contact physics, negatives, authenticity assertion. See `anatomy.md`.

When the user supplies the reference image, this becomes Mode B and the model does the transcription for
you. When they do not, **you transcribe it in words** — which is what these decks are.

## How he chooses which photograph

Selection is where the judgement lives. Four heuristics account for nearly every frame in the hand-cream
deck.

### 1. Build the set out of the product's own material

The L'Occitane tube is **aluminium, silver, with a blue label**. Look at what he put around it: a polished
silver tray, a stainless scoop, a metal measuring cup, a chrome jigger, white foam, and a stated palette of
"cool, clean, silver, white, and slightly blue-toned". The set is made of the same substance as the product.

Same logic in the Liquid Death deck: the can is white with black type, so every frame is white, black and
transparent — a glass stein, a clear pour, a crushed white can.

The product is not placed *on* a set. The set is **extruded from the product**, so the product reads as
native to the frame rather than dropped into it. This is the single most transferable rule on this page.

### 2. When the benefit is invisible, find an object that physically has it

You cannot photograph "soft hands". So prompt 03 puts the tube in an **oversized fuzzy mohair knit glove**.
The glove is soft — the benefit made touchable. It is also winter, which is when hand cream is used, and it
is a hand, which is the body part. One prop, three locks.

Prompt 06 does the same thing differently: it stands the tube in a **field of the cream itself**, sculpted
into glossy peaks. You cannot show "moisturising", so you show the formula as landscape. Product as its own
set.

Generalise: name the benefit, then find a physical object whose material properties *are* that benefit.

### 3. Cite a photographic genre that already carries the brand's positioning

The Liquid Death frame the user asked about — woman, sunglasses, direct flash, sky — works because **direct
on-camera flash is the visual language of nightlife and party photography**. Liquid Death is punk,
anti-wellness, bar-coded. The flash is not a lighting decision; it is the brand's positioning expressed as a
photographic genre. Shoot that same can on soft beauty light and it becomes a wellness drink.

Compare hand-cream prompt 01: soft diffused light from upper left, cool grey seamless, a hand emerging from
an **oversized structured black tailoring sleeve**. That is French-pharmacy luxury-beauty editorial, and it
is doing exactly the same job in the opposite direction.

Pick the genre first, from the brand's positioning. The lighting, camera and styling follow from the genre.

### 4. Draw the buyer as a pile of objects, or as a hand — almost never as a face

Hand-cream prompt 02 lists: a compact silver digital camera, a vintage silver flip phone, folded cash,
scattered coins, a grey notebook, a black leather wallet, a partially visible VHS cassette. That is not a
generic "luxury essentials" list — a digicam, a flip phone and a VHS tape in 2026 are a precise cultural
position. The props date the buyer, place her, and price her without a single person in frame.

Prompt 05 does the same with a matte white insulated tumbler, white wired earphones, a scrunchie and a
black wide-tooth comb. Different person, same technique.

Measured across the 420 sourced photographs in `library.md`: **7.6% show a face — but 52% contain a body.**
The bias against faces is real; a bias against people is not. The body arrives as a hand holding the product
(the single most common format in the library, 109 frames), a forearm in a sleeve, a torso with the head
cropped, or a figure from behind. The face is what gets excluded, not the person.

## Three smaller techniques worth stealing

**Damage the product on purpose.** Prompt 05: *"Both product tubes must appear realistically used with
natural crushed aluminum tube deformation, authentic pressure folds, creases, dents, compression marks,
subtle asymmetry."* The Liquid Death grid has a crushed can. A pristine product reads as a render; a used
one reads as photographed *and* as owned by somebody. Usage evidence buys realism and social proof at once.

**Two units in one frame.** Prompts 05 and 07 both place two of the product — one standing, one lying. It
shows two faces of the packaging in one image, and fills the composition without importing a foreign prop.

**Let objects carry the mood, not adjectives.** Emotion words are rare in the corpus but not absent: across
the 97 prompts, `aspirational` appears 4 times, `confident` twice, `joyful` once, and a `Mood is…` clause
appears in 5 (recounted 2026-09-14). None of them carries a frame on its own. The mood comes from objects,
materials, light and palette. If a concept cannot be stated as a thing in the frame, it does not go in the
prompt (`principles.md` P13).

## The job, start to finish

1. Read the product: material, colour, form, benefit, use occasion, buyer.
2. Choose the genre from the brand's positioning.
3. Find real photographs in that genre — one per frame the deck needs.
4. Check each against the four heuristics. Prefer references whose props already encode the material, the
   benefit, or the buyer.
5. Transcribe each exhaustively.
6. Swap, adapt, lock.

Steps 1–4 are the creative work and none of it happens in the prompt. By the time you are writing prose,
the decisions are already made.
