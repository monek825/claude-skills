# Principles — why the rules work

The skill was built in four stages. **Copy** is done: `corpus.md` holds the literal prompts. This file is
**decode**: the mechanism underneath each visible rule, and how strong the evidence is. **Rebuild** uses these
principles to make new work with no adgod reference image and no adgod prompt. **Deviate** breaks them one
at a time to find out which ones actually carry weight. Imitation exists to build judgement, so that copying
stops being necessary.

Precedence: when a rule and a principle conflict, the principle wins. A rule with no principle beneath it is
copy residue (the table near the end). Test it before trusting it.

Evidence grades used below:

| Grade | Meaning |
|---|---|
| **MEASURED** | Renders we generated and judged, usually with pixel metrics. n is small and stated. |
| **CORPUS** | Frequency across adgod's 97 prompts. Says what he does, not why it works. |
| **THEORY** | Published research, cited in `invention.md`. |
| **OBSERVED** | Seen repeatedly in practice, never logged as an A/B test. |

## The finding that reframes the skill

**All 97 adgod prompts attach a real image.** 69 attach a scene plate and 28 attach the product photo only.
None is text-only. Measured 2026-09-14 on the prompt paragraphs in `corpus.md`:

| | Scene plate (69) | Product photo only (28) |
|---|---|---|
| Seamless backdrop | 50 | 18 |
| Soft or diffused light | 51 | 20 |
| Hard light source | 7 | 2 |
| Seamless + soft, no hard source | 38 | 15 |

His prompts overwhelmingly specify soft light on seamless sets, which is the exact condition that rendered as
CGI when we generated text-only. His outputs still read as photographs because the attached photograph
supplies what the words never state: real reflections, a real black point, real surface wear. **The prompt
steers; the photograph carries the realism.** Rebuild removes the scene photograph, so the prompt has to write
out in words what the photograph used to supply silently. That is the job of Layer 1.

## Layer 1 — why an image reads as a photograph

### P1 · Realism is inherited from whatever real thing is attached

The model copies the finish of its most informative input. In descending strength: a real scene photograph, a
real product photograph, physics written out in words, then abstraction. A render or AI-generated source passes
its finish on.

- **Explains:** Mode B/C over Mode A; "attach Image 1 whenever you have it"; "plates are often renders,
  rebuild reflections from the scene"; `model-editing.md`'s "a recast changes the person, not the prompt's
  finish"; the A-S limit.
- **Evidence:** MEASURED. The VT v1 deck used HEY GLOW render plates and every frame read as AI. The
  FASHIONNN recast S03 kept its AI source's gloss. G2 (plate attached) and G3 (text only) both read as photos
  once the prompt was fixed, but with the plate the grade came out closer (n=1 each). CORPUS: 97/97 attach.
- **Break test:** one prompt, three inputs: a real product photo, a render plate, no image.

### P2 · A photograph records a world beyond its edges

Light arrives from somewhere and bounces off things that exist outside the frame. A render is a closed
system: light from nowhere, reflections of nothing.

- **Explains:** one named source with a shadow direction; reflections built from the scene; the unlit-side
  clause; environment frames outnumbering packshots; objects cropped at the frame edge; the mirror-finish rule.
- **Evidence:** MEASURED, VT blind test 2026-09-14. Frames with environment, hard light and props (02, 03,
  04) read as photos. Seamless, soft-light chrome frames (05, 07) read as renders. The v2 rewrite flipped both,
  and 07's blown pixels fell from 13.1% to 0.5%. **Confound:** v2 changed the source, the environment and
  the material imperfection all at once.
- **Break test:** ablate 07 one variable at a time: hard light only, reflected environment only, wear only.

### P3 · Exposure is a physical limit, not a style

A real sensor clips only at the light source and reaches black where surfaces meet. Tone-mapped HDR and
renders keep everything in range, which reads as synthetic.

- **Explains:** pure white only in specular pinpoints; a true deep tone in contact shadows; no HDR tone
  mapping; matching the plate's black point.
- **Evidence:** MEASURED, but correlational. The v1 deck's shadow floor was 81 against adgod's 17, and its
  blown white 4.85% against 0.03%, alongside other faults. CORPUS: `HDR` 10/97, `retouch` 70/97, `8K`
  67/97. Those tokens are harmless on a real photo; text-only they are untested, apart from HDR combined
  with soft light, which flattened v1.
- **Break test:** text-only, a bare camera tail vs the full `16-bit, HDR, retouching, 8K` tail.

### P4 · Used objects were photographed; pristine ones were modelled

Fingerprints, scuffs, dust, a crushed tube, a tangled cable. Wear is evidence of time and of an owner.

- **Explains:** "damage the product on purpose" (`ideation.md`); honest-use clauses; the fingerprints in v2.
- **Evidence:** CORPUS: explicit wear appears in only 9/97, so adgod rarely writes it; the real plate supplies
  it. MEASURED, but confounded inside the v2 rewrite.
- **Break test:** the same text-only prompt, pristine vs worn.

### P5 · Real sets carry reasons; decoration carries counts

Numbers belong to geometry the camera enforces (angle, frame fraction, f-stop) and to counts the scene has a
reason for (two units, three contact points). Counted decoration, symmetrical reserved space and evenly
repeated highlights read as manufactured.

- **Resolves:** `anatomy.md` style rule 5 ("numbers over adjectives") against the realism gate's
  counted-droplets hard fail. Both hold, for different kinds of number.
- **Evidence:** CORPUS: `exactly N` appears in 1/97 and counted droplets in 0/97. CORRELATION: every v1
  prompt had counted droplets or reserved copy space.
- **Break test:** counted beads vs a single spill, same frame.

### P6 · Printing on a curved surface proves shape and identity

Text wrapping a cylinder is a perspective cue and an identity cue at once. A blank pack reads as a mockup.

- **Explains:** keep the product's own print; `no text` means no text *added*; the cylindrical-label clause.
- **Evidence:** MEASURED-correlated. Every v1 frame had its label stripped and read as AI; in the blind test
  all 7 had correct print.
- **Break test:** the same frame with print vs a blank pack.

## Layer 2 — why the model obeys

### P7 · Use constraints the model cannot invert

Geometry beats comparison ("spans thumb tip to index fingertip" instead of "as long as the palm"). Name and
count the contact points, and support the object at both ends.

- **Evidence:** OBSERVED (`anatomy.md` Block 8). No logged A/B.

### P8 · State what exists; negate only what could plausibly appear

A named negative still primes the thing it names. Negatives spent on things that would never appear cost
attention. A ghost of an inherited action needs exactly one explicit negation.

- **Evidence:** CORPUS: median 4 negatives per prompt, max 16. CORRELATION: the AI-looking deck ran 22–25.
  OBSERVED: ghost objects survive without the negation (`adaptation.md` §4).
- **Break test:** 25 negatives vs 5, same prompt.

### P9 · Words repeated verbatim become identity, but only for a product the model can see or already knows

- **Evidence:** MEASURED. An identical product block gave correct print in 7/7 blind frames, but VT PDRN
  100 is a bestseller the model may already know. A text lock for a real product it does not know: TP-7,
  0 of 7 accurate.
- **Consequence for rebuild:** a real product photo is still required. It is not an adgod reference.

### P15 · Size is re-estimated in every frame unless it is locked

The model redraws every dimension the prompt leaves unstated, separately for each scene.

- **Evidence:** MEASURED, 2026-09-14 rebuild deck. Four upright frames, measured against the front render:
  overall height ran 3.01–3.26 body widths against a real 2.72 (11–20% tall), and cap height 0.72–0.91 against 0.47.
  Every cap came out 53–94% too tall. Rerun with the lock (frames 03 and 07, n=1 per arm): overall height
  landed within ±3% text-only, and cap error fell to +13–23%. Attaching the render copied the label exactly
  but did not tighten proportions. In v3 (8 frames: a tighter cap relation that compares the cap's own width and
  height, plus the render), the median cap error was about +8%, and 4 of 7 upright frames were within 10%.
  Size against a person is still wrong: bottles held to the cheek came out 40–50% too large against the face,
  because the prompt anchored with a face comparison. In v4, facial-landmark spans decoded from adgod's
  contact-point language measured 1.43, 1.02 and about 1.0 against a target of about 0.86 (bottle height ÷
  pupil-to-chin). adgod never sizes a held product in words; it inherits scale from a real style plate. Held
  product size looks like a P1 problem: it needs a carrier, not better adjectives. The prompt had called it an `oversized` overcap and gave centimetres with no ratios.
  The user spotted the drift before any measurement was taken.
- **Fix:** `size-lock.md`. Ratios in body widths, self-evident relations (`clearly wider than it is tall`),
  no size adjectives, one scale anchor per scene, and an attached product image when one exists.
- **2026-09-18, held products:** a three-arm test (no size language / hand geometry / hand geometry plus
  frame fractions) was run and then measured. **Proportions came out within 4% in all three arms**, the best
  result so far. **Scale against the hand remains unestablished:** the arms were framed differently, so the
  first eye-based ranking was a crop artifact, and every cross-image normaliser tried was too noisy to use.
  The lesson generalises — **an A/B on size must lock the crop and put a known-size object in frame**, or the
  measurement cannot be made. MEASURED for proportion; scale untested.
- **Break test:** the same frame with and without the proportion lock, and with and without the attached
  image.

## Layer 3 — why a frame is remembered

### P10 · Same predicate, opposite register

A true thing about the product, said by an object from the wrong world. The viewer recovers the truth and
enjoys the distance.

- **Evidence:** THEORY (Giora's optimal innovation; Phillips & McQuarrie) plus one worked CORPUS decode
  (Rolex among goldfish). Never tested on viewers.
- **Break test:** for one predicate, a same-register frame vs an opposite-register frame; ask the user which
  they still remember the next day.
- **Viewer data (2026-09-14):** the user did not recover the rice-cake conceit ("idk what number 2 is supposed
  to be"), which I had self-scored 2/2 on recoverability. The ginseng jar went unremarked. Self-scored
  recoverability is not evidence: a conceit counts as landed only once a viewer states its truth.

### P11 · Strangeness needs a baseline

A conceit is memorable only against ordinary frames, which is why a deck carries one or two conceits per seven.

- **Evidence:** THEORY (von Restorff; the mixed-list bizarreness effect). CORPUS: 13 decks / 87 frames.

### P12 · The set is extruded from the product

Build the set from the product's material, make its invisible benefit physical, cite the photographic genre
that carries its positioning, and draw the buyer as objects. The product reads as native to the frame, and no
other product yields the same set, which is what makes the frame original **without any reference**. This is
the engine rebuild runs on.

- **Evidence:** CORPUS (the L'Occitane and Liquid Death decks). Untested as an A/B.
- **Break test:** the same product on a set with no material relation to it.

### P13 · Objects carry mood; adjectives decorate

- **Correction:** `ideation.md` said the corpus has no emotion words. It has a few: `aspirational` 4,
  `confident` 2, `joyful` 1, and a `Mood is…` clause in 5 of 97. They are rare and never carry a frame alone.
- **Evidence:** CORPUS. Mechanism untested: the model renders nouns, and mood adjectives pull toward stock.
- **Break test:** the same frame with and without its mood adjectives.

### P14 · A face competes with the product

- **Evidence:** CORPUS. In the library, 7.6% of frames show a face while 52% show a body. This is the fifth
  dominance lever, no rival of equal weight (`anatomy.md`). Untested.

## Copy residue — surface features with no known mechanism

These are the first candidates for deviate. Frequencies are from the 97 prompts unless marked.

| Rule | adgod frequency | What is actually known |
|---|---|---|
| 12 blocks, one paragraph | 97/97 | Labelled sections also work (FASHIONNN, Digital Arnab). No A/B. |
| 250–570 words | median 390 | "Fidelity collapses below ~250" was never logged. |
| Named camera body | 63/97 | A style-token hypothesis. Untested. |
| `retouching`, `8K` | 70/97, 67/97 | May pull text-only prompts toward render polish. Untested. |
| Seamless backdrop | 68/97 | Fine with a real photo; text-only mirror products render (P2). |
| Soft or diffused light | 71/97 | Same as above. |
| Authenticity sentence mandatory | not re-measured | The skill makes it mandatory; its effect is untested. |
| Restate fidelity 2–3 times | claimed in `anatomy.md` | Untested. |

## How rebuild uses this

- No adgod plate, no corpus prompt, no library search. The library is adgod's own selection.
- A real product photo is still required (P9). Without one, the output is a concept for a lookalike (A-S).
- With no scene photograph to carry realism, write P2–P6 into every prompt: a named source and its shadow
  direction, a world the product reflects, exposure limits, wear, contingent numbers, and the product's print.
- Ideas come from P10–P12 through `invention.md`. The originality gate still applies.
- If a non-adgod photograph is used for a frame, it becomes that frame's carrier (P1). Record which frames
  had one, so results separate.

## How deviate uses this

Take one principle and break one variable, holding everything else fixed. Run at least 2 renders per arm
(there is no seed control), shuffle the labels before judging, and log the result in
`~/Documents/adgod-prompts/tests/`. A principle that survives its break test gets upgraded to MEASURED. One
that fails gets rewritten here, not quietly dropped.
