---
name: adgod-prompt
description: Write AI product-shoot prompts in the adgod.ai house style — the long single-paragraph, block-structured, camera-and-lighting-specified prompts used in the adgod Vol.01 decks (North Face, Chamberlain Coffee, Liquid Death, Dior, Rhode, Rolex, Oakley, Nothing, Matchaeologist, Stanley, Olipop, Chanel, Crown Affair). Use whenever the user asks for an image-generation prompt for a product shot, ad creative, campaign image, packshot, beauty shot, lifestyle product photo, or a whole ad campaign set; whenever they say "adgod", "adgod style", "product shoot prompt", "campaign prompt deck"; or when they hand over a product photo and want scenes built around it. Also use to reproduce or adapt any of the 97 original prompts verbatim, or to search the local reference library the decks are sourced from.
---

# adgod prompt writer

Produces prompts that read exactly like the adgod.ai Vol.01 decks. Target model is **GPT Image 2** (also
works on Nano Banana Pro / Seedream / Flux Kontext with reference images; the structure is the same).

**Ground truth is `references/corpus.md` — all 97 original prompts, verbatim.** Lift its **sentence patterns,
block order and phrasing** literally; that is the fastest route to the same output quality and there is no
reason to paraphrase what already works. **Never lift the scene, the props, or the conceit.** Those are
adgod's authorship, not his craft, and reproducing them makes the work recognisably his — read
`references/signature.md` before going near the corpus for anything but phrasing.

**Stage (2026-09-14): copy is done, decode is in progress, rebuild is next.** `references/principles.md`
records why each rule works and how strong its evidence is. Where a corpus frequency and a principle
disagree, the principle wins. **Rebuild uses no adgod reference image, no corpus prompt and no library
search.** Note that every corpus prompt attaches a real photograph, so a text-first prompt has to write out
the realism that photograph used to supply.

**Replicate mode → use `ref-lighting`, not this skill.** When the user wants a reference photo copied "exactly, just swap the product", write a short `Edit Image 1` prompt with `~/.claude/skills/ref-lighting` and measure the reference with its script. Do not use the 12-block anatomy or the HDR/retouching/8K finish tail: on 2026-10-15 both pushed the VOID SCENT renders 2.5x sharper and more saturated than their refs.

## Files

| File | Load when |
|---|---|
| `references/size-lock.md` | **Always, before writing a product block.** Build the product's size card once (published dimensions → measured from a straight-on photo → one recorded estimate), write the proportion lock in body widths, give each scene one scale anchor, attach the product image when one exists, and reject renders more than 10% off the card. |
| `references/taste.md` | **Always, before ideation and prompt writing.** The image-specific adaptation of the Designare taste guide: reference brief, six-pass image read, specificity ladder, one-variable critique loop, and delivery gate. |
| `references/principles.md` | **Always, first.** The mechanism under each rule, its evidence grade (measured / corpus / theory / observed), the copy-residue list, and a break test per principle for the deviate stage. |
| `references/library.md` | **Always at step 0.** 630 catalogued adgod images — 420 real source photographs, searchable locally. How to query them, what the sources actually look like by the numbers, and the brand-kit template. |
| `references/invention.md` | **Always, at step 0, before anything else.** The idea engine: product truth → bare predicate → association burst → register-distance sort → visual-structure grid → the 7-point taste rubric. Also the deck-level mixed-list rule. |
| `references/deck-composition.md` | **Always when building a set.** The twelve slot types measured across 13 complete decks / 87 frames, the 1–2 conceit : 5–6 grounded ratio, the four treatment devices, and a seven-frame build sheet. |
| `references/signature.md` | **Always, and again before delivering.** What is craft and copyable versus what is adgod's authorship and off limits. Carries the do-not-restage list and the originality gate. |
| `references/web-sourcing.md` | **Experimental.** When the library has no frame for the scene — searching the open web for a reference, the trust-ranked source list, the hard-reject rubric that keeps AI slop and moodboards out, and provenance recording. |
| `references/ideation.md` | **Always, before anything else, whenever the scene is not already given.** Where the ideas actually come from — the corpus transcribes real photographs rather than inventing scenes. |
| `references/anatomy.md` | Always, before writing the first prompt. The 12-block skeleton + phrasing library. |
| `references/camera-lighting.md` | Always. Camera bodies, lenses, aperture-selection logic, lighting rigs, background/palette pairs. |
| `references/adaptation.md` | **Always when a product, subject, background, or lighting differs from the source scene** — i.e. nearly every real job. Affordance table + what-to-rewrite cascade. |
| `references/industrial-cmf.md` | The industrial / CMF register — Braun-to-Teenage-Engineering hardware on soft grey with one saturated accent. Load when the product's own design is the story, or the brief references that look. Carries a render tail as well as the photographic one. |
| `references/optics.md` | **Always, at step 0, before writing any scene.** What the product does to light: transparent, mirrored, translucent or matte, and therefore what happens to whatever is behind it. Carries the refractive indices for a clear acrylic bottle of oil (air 1.00 / PMMA 1.49 / silicone 1.40), why the filled bottle behaves as one solid lens, and the wording that actually renders — the object behind named in the SCENE sentence with its magnification, displacement and where it stops. A see-through clause buried in the physics tail is ignored: all seven v3 frames had one and all seven came out opaque. |
| `references/composition.md` | **Always, before placing the product in any frame.** Measured across all 194 catalogued adgod outputs: **0 of 143 photographs show the product alone** — 95% carry a named prop, 43% a human, median 3 props. His placement vocabulary (perched, buried, draped, wrapped, balanced, threaded, sunk, pressed into, poured over, against a body part), the fact that upright is the exception, and the second output mode we never make — the 27% of his feed that is a designed poster, which is the only place a lone upright hero is allowed. |
| `references/effects.md` | **Whenever a frame carries an optical or material effect** — refraction, caustics, flare, water, reflection, a magnifier or a barrier. 33 catalogued effects with a paste-ready clause each, mined from the 104-prompt corpus and 630 catalogued images. Carries the five-part grammar every effect adgod renders well is written in (preserve clause / **named cause** / `physically accurate` + 4-6 optical nouns, which appears in 76 of 104 prompts / anti-composite tail, 25 / camera tail, 53) and the rule that separates a real effect from a filter: **a named cause and a visible source**. Also records what he never uses — zero glass bars, prisms, kaleidoscopes or volumetric rays: every lens in his work is an object in the scene, never something held over the camera. |
| `references/art-direction.md` | **Always for a campaign or a deck, and always before locking constants.** The counted head-to-head between adgod's Olaplex deck and ours for the same product: the grade (83% vs 0%), the finish tail (100% vs 0%), colour range (0.91 vs 0.17 background colours per frame), gravity, people, and the one-spectacle-in-an-empty-field structure that all his frames share. Carries the corrected constants rule and the do-not-restage additions for Olaplex. |
| `references/aliveness.md` | **Always when a person must look real rather than look good.** Why one model reads as a person and the next as a mannequin: ten levers counted across the @prompts.soul, LUXRY.AI and FASHIONNN Set 2 decks — phone not camera, named sensor defects, flat available light with no instrument, a stated non-smile, one specific hand action, body torsion, ungraceful posture, incidental background life, AI-tell negatives, muted-with-one-accent. Carries the eight @prompts.soul street prompts verbatim and a spinoff template. |
| `references/plate-pipeline.md` | **When no usable reference photograph exists, or a product must be held at a credible size.** The R0 Studio three-slot architecture (`@Image1` product truth / `@Image2` light and mood only / `@Image3` fit and proportions) with its stated order of authority, the build-the-plate-you-need method, the rule that a character sheet must not already wear the hero, and the proposed held-plate fix for the unsolved held-product scale problem. |
| `references/figure-prompts.md` | Frames whose subject is a person. The descriptive register — an analyst's exhaustive account of a photograph, closing on a 15-swatch hex palette — as against the directive 12-block anatomy. Load for fashion, portrait or lifestyle figure work. |
| `references/fashionnn-corpus.md` | **Supplemental figure corpus.** Fifty-six FASHIONNN.AI / LUXRY.AI prompt-and-reference pairs from eight decks (2026-09-17: eyewear selfies Vol. 10, outfit-led locations Vol. 08, a MOTIONMAN menswear motion-technique study covering long exposure, double exposure, motion blur and ghost frames, and a vintage-analog reverse prompt deck with negatives and hex palettes; 2026-09-18: LUXRY.AI “Soft Hours, Golden Light” with a nine-block schema carrying a PRODUCT block in 6 of 7, and a second Reversed Image Prompts set of seven) for fashion, model-led lifestyle, streetwear, travel, everyday environments, pose, wardrobe and contact mechanics. Decode notes: `~/Documents/adgod-prompts/refs/fashionnn/REVERSE-ENGINEERING-2026-09-17.md` and `REVERSE-ENGINEERING-ALIVENESS-2026-09-18.md`. Load with `figure-prompts.md` for fashion/model/lifestyle work. It is AI-generated reference material, not Adgod ground truth. |
| `references/model-editing.md` | **Always when changing model identity or physical traits, or preserving a model across frames.** Canonical trait schema, clean-portrait accuracy boundary, locked shot invariants, dependency cascade through SKIN/MAKEUP/wardrobe fit/crop/light response, contact physics, contradiction cleanup and pronoun consistency. |
| `references/display-copy.md` | Writing the headline/copy that goes *beside* an image — short, bold, built for tall condensed type. Load whenever a job asks for copy as well as prompts. |
| `references/archetypes.md` | Naming what *kind* of frame a deck still needs. Not a source of scenes — see `ideation.md` on why the menu underperforms. |
| `references/corpus.md` | The user names a source deck/prompt, wants verbatim reproduction, or the brief is close to an existing scene. Large — grep it (`grep -A2 "Deck: Rolex"`) rather than reading whole. |

**People routing:** for any fashion, portrait, model, or model-led lifestyle brief, load `figure-prompts.md`
and `fashionnn-corpus.md` together, and add `aliveness.md` whenever the person has to read as alive rather than merely correct. If the brief changes complexion, facial traits, hair, eyes, age, build,
grooming, makeup, pronouns, or likeness—or asks for the same model across a set—also load
`model-editing.md` and apply its full dependency cascade before writing. Keep the Adgod `corpus.md` authority
separate from the supplemental FASHIONNN material.

## Workflow

**Taste pass — make the decisions before making the prose.** Read `references/taste.md` and complete the image reference brief. If a reference image exists, perform the six-pass read and name the one mechanism being borrowed plus what will be different. The invention engine decides the concept; the taste pass decides how the concept becomes a specific, judgeable image. Do not let the 12-block anatomy, realism tail, or a long adjective list substitute for this work.

**0. Build the concept from the product, then find photography that proves it can be lit.** Two acts, in
this order. In the earlier 69-prompt baseline, 39 prompts carried explicit transcription language
— but what it transcribes was chosen *after* the idea existed. Skipping to a reference and working backwards
is what produces frames that look like somebody else's.

**Run the invention engine in `invention.md` first — it is the step that decides whether the work is
memorable or merely competent.** Extract the product's physical truths, reduce one to a bare predicate
sentence, burst twenty other things in the world sharing that predicate, sort them by register distance, and
take the item furthest from the product's own world **whose predicate a viewer can still recover in three
seconds.** Same predicate, opposite register — that is the whole formula. Then pick a cell from the
Phillips-McQuarrie structure grid and score the result on the 7-point rubric before writing a word.

**Deck-level, non-negotiable:** one or two high-register-distance frames per seven, and fill the other five
or six from the measured slot list in `deck-composition.md` — in-hand body contact, environment carrying the
positioning, buyer-as-objects tableau, formula-as-set, ingredient-as-terrain, output-as-hero, macro texture,
pour, flatlay, pair-set, worn. Lock the conceit first, then build the grounded slots around it. The bizarreness memory
advantage exists in mixed lists and vanishes in pure ones — a deck of seven surreal conceits is a pure list
and reads as noise. The strange frame works because the other six are ordinary.

**Supporting heuristics from `ideation.md`:** build the set out of the product's own material ·
make an invisible benefit physical · cite a photographic genre that carries the brand's positioning · draw
the buyer as objects or a hand, never a face. Add the affordance from `adaptation.md` — the gesture no
competing product can perform is usually the deck's strongest frame. A concept derived this way is
inherently original, because no other product yields the same set.

**Then find the photograph**, in this order: **non-adgod photography** via `web-sourcing.md` (brand
newsrooms, photographers' portfolios, awards archives) — or, when the concept is a plain lifestyle or
still-life situation rather than a distinctive conceit, the local library. Open the file and transcribe it
object by object, quadrant by quadrant, material by material. Transcribing from a one-line description is
not transcription.

**The library is craft reference and a negative index — not a scene menu.** It holds 420 photographs adgod
selected for his own campaigns plus 68 of his finished outputs, and the `kind` field is imperfect, so some
outputs sit in the `reference-photo` bucket. Search it to calibrate lighting, palette, crop and genre, and
search it again before committing to a scene: **a strong match is a warning, not a find.** It means you have
arrived at something he has already published.

```bash
cd ~/Documents/adgod-prompts/refs/adgod-ig
python3 find-refs.py --kind reference-photo "<the scene in plain words>"
```

**Then run the originality gate from `signature.md` before writing a word of prompt:** would a follower of
adgod recognise this frame as one of his? Strip the product — is what remains a scene he already made? A
watch belted round a moka pot is his composition whether the watch is a Rolex or an AP. If either answer is
yes, rebuild the frame from the product.

What the 420 sources look like, measured, because `archetypes.md` does not reflect it: **in-hand 109 and
environment 102 are half the library; clean hero-packshot and mirror-plinth together are 21, five per cent.**
Genre runs studio-gradient 92, documentary-street 83, still-life-classical 56. 48% contain no person at all
and only 7.6% show a face — but 52% contain a body, nearly always a hand or a cropped torso. Weight the deck
that way.

**1. Establish the brief.** You need five things. Ask only for what you genuinely cannot infer from the
product image or the user's message — a missing answer gets a stated default, not a blocking question:

| Need | Default if unstated |
|---|---|
| Product + category | read from the image |
| Reference mode (A product-only / A-S symbolic no-plate / B style+product / C master-DNA) | A if one image, B if two, A-S if none |

**A-S only holds for a product that does not exist.** For a *real* product with no plate attached, a text
lock — however detailed — will not reproduce it: the model builds a plausible object in the brand's design
language and keeps it consistent across the deck, which reads as a convincing campaign for a product that
was never made. Measured on a TP-7 set: seven frames, one coherent invented device, zero accurate ones.
**Get one real product photo and run Mode A.** If none exists, say so and treat the render as a concept
for a lookalike, not as that product. Generating the tightest macro frame first and re-attaching it as the
plate for the rest fixes internal consistency but cannot fix accuracy — the first frame is already wrong.
| Scene or archetype | pick from `archetypes.md` and say which |
| Deliverable count | 1 prompt; if they said "campaign", 7 |
| Aspect ratio | vertical 4:5 |

**2. Pick the archetype and lock the campaign constants — but lock the RIGHT ones.** Measured 2026-09-18
against adgod's own Olaplex deck (`art-direction.md`): **he does not lock the field, he locks the production
value.** His decks average **6.4 distinct background colours per seven frames** — eleven in the Nothing deck,
ten in Dior. What stays identical across his set is the camera body, the finish tail, the no-CGI assertion
and the product's fidelity; the world changes completely from frame to frame.

Lock: product fidelity · camera system · the finish tail · the grade's *register* (luxury, editorial, clinical)
· aspect ratio. Vary: background colour and value, lighting rig, surface, crop, and whether a person is present.

Applying the old wording literally across 24 frames produced bone-white plaster, warm side light and a white
block twenty times over. One palette across a whole deck is not consistency, it is monotony.

What "locked" means precisely: the **register** is locked — background family, key colour, palette, grade,
camera body, aspect ratio. The **instrument** may vary per image when the concept physically requires it,
and often must. A backlit halo destroys a reflection the concept depends on; a diffuse source cannot throw
a hard cast shadow; flat frontal light hides the texture a wear story is about. Choose the rig that makes
that image's idea legible, from the rig table in `camera-lighting.md`, and keep everything else identical.
A set can legitimately run backlit halo, hard collimated beam, and raking side light side by side and still
read as one campaign, provided the field, palette and grade never move.

Every prompt states its rig AND its shadow side. Light-field work is not exempt: a high-key background can
still carry a single beam, a vignette to warm grey at the corners, and genuinely dark unlit faces — "light
background" is a statement about the field, not a ban on shadow.

**2·0. Assemble from the corpus before writing a single sentence of your own.** `corpus.md` opens with the
instruction and it is not decoration: *"copy the sentence patterns literally and swap only the
product-specific nouns."* Search the corpus for the closest scene, take its pose sentence, its background
sentence, its lighting sentence, its grading sentence and its camera tail **verbatim**, and change only the
nouns. Original prose is for the product locks that adgod does not need — print, orientation, proportion —
and for nothing else. Measured 2026-09-19: four decks written in my own voice were rejected in a row; the
fifth, assembled at ~83% verbatim from his sentences, is the first one built the way the corpus says to
build it. If the PDF extraction garbled a sentence, repair it back to what it obviously was and say so —
do not rewrite it.

**2a. Answer the three optics questions (`optics.md`) before the scene exists.** Is the product transparent, mirrored, translucent or matte · what does it do to whatever is behind it · what does it do to whatever is around it. If it is see-through, name the object behind it inside the scene sentence and say how it is magnified, displaced and where it stops. This is research about the product, not decoration, and it is the step that was missing when a clear bottle rendered opaque on top of a comb.

**2b. Derive the affordance — do this before writing a single word.** Look up the product in the affordance
table in `references/adaptation.md` and name how it is actually worn, carried, held, or placed. **Never
inherit an interaction verb from a style plate or from a corpus prompt.** A backpack is worn on the back; a
tote is carried by its handles at the hip; a watch is on the wrist; a clutch is under the arm. If the
reference scene's affordance differs from the new product's, the prompt must carry the affordance override
sentence from `adaptation.md` §2 and rewrite the pose, grip and contact-physics clauses from scratch.

Then run the cascade table (`adaptation.md` §3) for everything else the user changed — product, subject,
background, lighting, palette, aspect ratio. Anything the changed element touches, reflects into, or casts
onto gets rewritten; everything else is inherited verbatim. If the reference's action is impossible for the
new product, keep the narrative beat, restage the action, and negate the old one explicitly (§4).

**3. Write each prompt through all 12 blocks in order** (`anatomy.md`). Non-negotiables:

- One unbroken paragraph. No line breaks, no bullets, no markdown, no headings inside the prompt.
- Word count in the corpus range: min 256, median 392, p90 505, max 569. Aim near 392 for a simple scene; prop-dense or heavily-constrained prompts legitimately run 500+. Count it. Below ~250 fidelity collapses.
  **Budget the mandatory tail before the scene.** Hands-and-skin lock, negative list, branding sentence and authenticity assertion cost roughly 230 words before a single word of scene description. Any frame containing a hand therefore lands at 500–570, not 392 — that is correct, not bloat. The 392 median belongs to frames with no person in them.
- Third person, present tense, declarative. Never "please", "I want", "try to", "you should".
- The fidelity lock enumerates **category-specific** attributes (see the table in `anatomy.md`) — a watch
  prompt names bezel/crown/crystal/links/clasp; a can prompt names cap/label artwork/embossing/fill level.
- Every spatial and angular value is a number: degrees of tilt, percentage of frame, object counts, f-stop.
- Lighting is instrument + position + quality + shadow behaviour + what the unlit side does. Never "good
  lighting", never "soft light" on its own, never a rig with no stated falloff.
- The contact-physics block is mandatory: contact shadows, ambient occlusion, environmental colour bounce,
  plus the interaction physics for worn / held / liquid / cylindrical-label cases.
- Aperture is a decision, from the table in `camera-lighting.md`. f/11 + focus stacking for studio
  still-life and macro; f/8 for multi-object and portraits that need face + product sharp; f/2.8–f/4 only
  when the environment should genuinely fall away.
- Camera body and lens must be a real pairing from `camera-lighting.md`. Never mix two bodies.
- End with the negative list, then the authenticity assertion. Both mandatory.

**4. Deliver.** Each prompt in its own fenced block so it copies cleanly, preceded by a one-line label
(`01 — Mirror-plinth hero (A2)`). Above the set, one short line naming the shared palette and lighting
logic. No commentary between prompts.

Before delivery, run the taste gate in `references/taste.md`. For a generated set, use its critique loop in
brief → structure → craft order, changing one variable per iteration and recording why frames were rejected.

## Generating the images

If the user wants images, not just prompts:

- **In Codex:** the built-in `image_gen` tool. Attach the product photo as the reference and pass the prompt
  verbatim. For Mode B/C prompts attach the style plate first and the product plate second, matching the
  "Image 1 / Image 2" wording in the prompt.
- **In Claude Code:** there is no local image model. Hand the user the prompts and point them at GPT Image 2
  (ChatGPT / OpenAI Images), or tell them to run the same skill in Codex, which can generate directly.

Do not silently reword a prompt at generation time. If a prompt needs a change, change it in the text you
give the user too.

## Realism gate — what the rubric cannot see

The taste rubric scores the idea; the self-check scores compliance. Neither looks at realism. Measured
2026-09-13: a Codex deck for VT PDRN Essence 100 self-scored 12–14/14, passed every self-check item, and every
render read as AI — blown-white pixels 4.85% against adgod's 0.03%, shadow floor 81 against 17. **Run the lint
before generating; hard fails must be zero:**

```bash
python3 ~/.claude/skills/adgod-prompt/scripts/lint-realism.py <deck.md>
```

Hard fails appear in none of adgod's 97 prompts and in every prompt checked from that deck:

- **Removing or blanking the product's own printing.** `No text` means no text *added*; the label is part of the product.
- **`preserve … reflection behavior` from a plate.** Product plates are often renders. Say so, and rebuild every
  reflection from the scene — chrome and glass have no look of their own.
- **Empty space reserved for later copy** in every frame.
- **Counted decorative droplets** (`exactly nine water beads`). Real water is a spill, a film or a ripple.

**Correction 2026-09-18 — restore the finish tail when a real product photo is attached.** The gate stripped
`HDR`, `retouching` and `8K` from our prompts on the evidence that HDR plus soft light flattened the VT deck.
adgod carries that tail in **7 of 7** Olaplex prompts and 67–70 of 97 corpus-wide, and his output is the
standard. What flattened VT was a sourceless soft rig on a render plate, not the token. Keep the tail off only
for text-only work until that is tested on its own.

**Correction 2026-09-18 — counted droplets are not automatically a fail.** adgod's Olaplex 01 says `Place two
translucent glossy serum/oil droplets around the product, one near the upper left side and one near the lower
right side`, and that frame reads as high-end. Counted droplets are legitimate when staged as designed objects
in a studio frame; they fail when they pretend to be incidental realism on a dry surface. The lint now warns
rather than fails. Judge by intent.

Warnings — judge in context. `HDR capture`, `open shadow` / `no crushed blacks`, `protected highlights` and
`poreless` / `no visible texture` also appear in 8–11% of adgod's own prompts; the failure is their combination
with a soft, sourceless rig, and one directional source plus the plate's own black point fixed it. More than 20
`no …` negatives: no adgod prompt has that many and the AI-looking deck had 22–25, but that is correlation only.

**Mirror-finish products — give the mirror a world and one hard light.** Chrome, metallised plastic, polished
metal and gloss lacquer have no look of their own. On a seamless set under soft, sourceless light they reflect
nothing but smooth gradient bands, which is the signature of a 3D render. Tested 2026-09-14 on the VT PDRN 100
blind test: frames 05 and 07 had 0 hard fails and still read as CGI, and 07 blew 13.1% of its pixels. A
rewrite with three changes turned both into photographs (n=1 each): blown white 0.27% → 0.04% and 13.1% → 0.5%.

1. **An environment the mirror can show, bent around the form.** Examples: a window and its mullions, the
   dark studio behind the camera with a small unreadable camera silhouette, the sleeve or hand holding it, a
   neighbouring prop. Write `the silver is a curved mirror, not a smooth gradient, so it shows the room bent
   around the cylinder: …`. The model did not draw the listed reflections literally. What mattered was
   giving it a scene to reflect, so do not spend words on an exact reflection map.
2. **An imperfect material.** Metallised plastic is not polished steel: its reflections wobble, the mirror is
   slightly soft and grey, faint fingerprints sit where it was handled, and it carries dust, lint or hairline
   scuffs on the cap.
3. **One hard source with a crisp cast shadow**, such as low window sun or a bare strobe in a small reflector.
   The backdrop is exposed to light grey, never paper-white. Pure white appears only in the source's own
   reflection.

Cost: frame 07 came out darker than its bright white reference (mid-grey backdrop, grey marble table). When the
reference is high-key, push the backdrop lighter; do not go back to soft light. A seamless white set is still
fine for matte, paper and frosted products.

Scope: the rule applies when no real photograph supplies the reflections, meaning text-only generation or a
render plate. adgod's Rolex prompts put polished metal under diffused light on seamless sets and still read as
photographs, because each attaches a real photograph as Image 1. There is no lint check for this rule. A
keyword version fired on 20 of adgod's 97 prompts, 19 of them with a real photo attached (chrome clocks, silver
spoons, those Rolex frames). Judge it by eye with the reject list.

**Attach the transcribed photograph as Image 1 whenever you have it.** 69 of 97 corpus prompts attach a
scene plate and the other 28 attach the product photo, so none is text-only (recounted 2026-09-14,
`principles.md`). In a live
A/B test (2026-09-14) the rewritten prompt read as a photograph both with the plate attached and as text alone;
the attached plate gave the closer editorial grade and composition. One sample each: direction, not proof.

**Reject a render when:** the product's print is missing or garbled · chrome or glass shows the same highlight
pattern in every frame, or only smooth gradient bands, instead of its own scene · a non-white set has pure white larger than a specular
pinpoint · water sits in perfect spheres on a dry surface · a hand has the wrong finger count or no skin
compression at contact · an environment frame has nothing cropped by its edges.

## Self-check before delivering

- [ ] `scripts/lint-realism.py` reports zero hard fails on the deck, and every render passed the reject list above
- [ ] Taste brief is complete; the reference is described by a mechanism, the prompt reaches specificity rung 4 or 5, and its kill list and verdict are explicit
- [ ] Any iteration was diagnosed in brief → structure → craft order, with one variable changed per round
- [ ] A size card exists for the product (`size-lock.md`), its proportion lock is pasted verbatim in every prompt with no size adjectives, and upright renders sit within 10% of the card
- [ ] Taste rubric scored 10+/14 with no zero on recoverability, predicate truth, or non-substitutability
- [ ] Deck carries at most two high-register-distance frames; the rest are ordinary and well executed
- [ ] **Originality gate passed** — would a follower of adgod recognise this frame as one of his? Strip the product: is what remains a scene he already made? If either answer is yes, rebuild the frame from the product
- [ ] Scene traceable to the product's own material, benefit, buyer or affordance — not to his archive
- [ ] Scene sourced from a real photograph — file opened and transcribed (not recalled)
- [ ] Web-sourced frames passed the `web-sourcing.md` rubric, and every source URL is recorded in the deck
- [ ] Single paragraph, 250–570 words (median 392; only exceed 500 if the scene genuinely needs it)
- [ ] Reference contract is the first sentence and names each uploaded image's role
- [ ] Fidelity lock enumerates attributes specific to this product category
- [ ] Adaptive-scale clause present (whenever a style plate is used)
- [ ] Affordance is the new product's own, taken from `adaptation.md` — not inherited from the reference
- [ ] Table row checked against the actual object; near-miss row (watch→wrist) rejected and derived fresh if it does not fit
- [ ] Affordance differs from the style plate? → override sentence present, pose and physics rewritten
- [ ] Cascade run for every changed element; props serving the old product removed; impossible inherited actions negated
- [ ] Product dominance: three of five levers present (size · sole focus · sole saturation · position · no rival object of equal weight), and every supporting prop given a stated subordinate role
- [ ] At least three numeric values (angle, frame fraction, count, f-stop)
- [ ] Background named as seamless + explicit colour + gradient direction — except a mirror-finish product: a room it can reflect plus one hard source (realism gate)
- [ ] Lighting names instrument, position, quality, shadow behaviour AND what happens on the unlit side
- [ ] Contact physics asserted; anti-composite sentence present
- [ ] Palette named in compound colour words
- [ ] Camera body + lens are a valid pairing; aperture matches intent; ISO and capture technique present
- [ ] Negative list present; branding-negative sentence included if the product carries a logo
- [ ] Final sentence is the authenticity assertion
- [ ] No hedging, no second person, no markdown inside the prompt

## Worked opening (Mode A, archetype A2, beverage can)

> Ultra-premium commercial product photography, vertical 4:5 composition, clean luxury studio setup on a
> seamless pure white background with a subtle warm grey gradient falloff, highly polished reflective acrylic
> surface creating a soft mirror reflection beneath the subject. Use the uploaded product image as the exact
> product identity reference and preserve every physical detail, proportions, materials, colours, finish,
> shape, cap details, label artwork, typography, embossing, printing details and construction exactly as
> supplied. Position the product upright slightly left of centre, perfectly front-facing with slight
> three-quarter depth visibility, occupying approximately half the frame height... *(continue through
> blocks 6–12)*
