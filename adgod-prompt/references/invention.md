# Invention — how to produce an idea that has taste

`ideation.md` says where scenes come from. This page is the machine that generates them, and the rubric that
scores them. It exists because "be creative" produces slop and "transcribe a reference" produces someone
else's work.

## The finding, in one line

**Memorable = a true thing about the product, said by an object from the wrong world.**

Both halves are load-bearing. Drop the truth and you get arbitrary weirdness that the viewer cannot decode.
Drop the wrong world and you get a competent, forgettable literal shot.

## Worked decode: the Rolex among goldfish

| Layer | Content |
|---|---|
| Product truth | A Submariner is water-resistant to 300 metres. Verifiable, printed on the dial. |
| Predicate | *It survives being underwater.* |
| Literal execution | A diver, an ocean, a wave. What Rolex's own advertising does. Nobody remembers it. |
| The move | Find another thing that shares the predicate — but from the **cheapest, most domestic water in the world.** A goldfish bowl. |
| Why it lands | The watch is over-engineered for this water by a factor of thousands. The spec is stated *and* mocked in the same frame. The viewer does the arithmetic themselves, which is the pleasure. |

The generative rule this yields:

> **Same predicate, opposite register.**

Register distance is the dial. Submarine and diving bell share the predicate but sit in the *same* register
as the watch — heroic, technical, expensive — so they read as illustration. Goldfish, a dishwasher, a glass
of denture tablets share the predicate from the opposite register — domestic, cheap, faintly comic — so they
read as wit. **Turn the register dial up until the predicate is about to become unrecoverable, then stop.**

## The engine — six steps, run in order

**1. Extract product truths, not benefits.** A benefit is a claim ("keeps you dry"). A truth is a physical
predicate you could verify with your hands. Aim for six to ten. Include the boring ones — manufacturing,
material, history, what it replaces, what it does when nobody is looking.

> Rolex Submariner: water-resistant to 300m · mechanical, no battery · gold is soft and heavy · the bracelet
> articulates over the wrist bone · it keeps running unattended · it outlives its owner · it was designed for
> divers who now never dive.

**2. Reduce each truth to a bare predicate sentence.** Five words if possible. *It survives underwater. It
never needs charging. It outlives the person wearing it. It makes hard things soft.* The sentence must be
literally true and contain no brand language.

**3. Burst.** For one predicate, list every *other* thing in the world that shares it. Twenty items, fast, no
filtering, no taste — taste comes later and applying it here kills the range. This is the "random burst of
thought," and the reason it produces ideas rather than noise is that **the predicate is the leash.** Free
association without a predicate is what generates AI slop.

> *It survives underwater:* submarine · diving bell · goldfish · ice cube · bar of soap · pearl · message in
> a bottle · water lily · dishwasher · denture tablet in a glass · tea bag steeping · swimming-pool tiles ·
> a boat · wet hair · a sponge · rain on glass · a koi pond · a snorkel · a rubber duck · a drowned phone

**4. Sort the burst by register distance.** For each item ask: how far is this object's cultural world from
the product's? Cheap/expensive, domestic/heroic, comic/serious, disposable/permanent, feminine/masculine,
child/adult, dirty/clean.

| Register | Items | Verdict |
|---|---|---|
| Same as product | submarine, diving bell, snorkel, boat | Illustration. Discard. |
| Adjacent | pearl, water lily, koi pond | Decorative. Mild. |
| **Opposite** | **goldfish, rubber duck, denture tablet, dishwasher, tea bag, drowned phone** | **The candidates.** |

**5. Choose the visual structure.** Phillips & McQuarrie's typology is the operator table. Three structures ×
three meaning operations, and both dimensions increase the elaboration the viewer must perform:

|  | **Connection** (associated with) | **Similarity** (is like) | **Opposition** (is not like) |
|---|---|---|---|
| **Juxtaposition** — side by side | easiest to read | | *watch beside goldfish* |
| **Fusion** — merged into one object | | | *bezel is the bowl rim* |
| **Replacement** — product absent, implied | | | *empty bowl, watch-shaped ripple* |

Read downward for more work demanded of the viewer; read rightward for richer meaning. Opposition +
replacement is the most demanding cell and the most likely to fail. Most strong frames live in
juxtaposition/opposition and fusion/opposition.

**6. Score it.** See the rubric below. If it fails, go back to step 4 and take the next item, not back to
step 1 — the predicate is usually fine and only the object was wrong.

## The taste rubric — how to rate this without eyes

Every criterion is answerable in words, which is what makes it usable by an agent. Score each 0–2. **A frame
needs 10+ of 14, and any zero on 1, 2 or 3 is an automatic fail regardless of total.**

**1. Recoverability (Giora, optimal innovation).** Can a viewer state the product truth within about three
seconds of looking? Novelty is pleasurable *only when the familiar remains recoverable underneath it.*
Unrecoverable novelty is not edgy, it is noise. → *Watch among goldfish → "waterproof." Recovered.*

**2. Predicate truth.** Is the shared property literally true of both objects? A forced or invented shared
property is the single most common way an AI-generated "surreal" idea is hollow. → *Goldfish live in water;
the watch survives water. True of both.*

**3. Non-substitutability.** Swap in a competitor's product. Does the frame still work? If yes, the idea
belongs to the category, not to this product — that is the definition of generic. → *A quartz fashion watch
among goldfish says nothing, because it has no 300m claim to over-satisfy.*

**4. Register distance.** How far apart are the two worlds? Score 0 for same-register illustration, 2 for
maximum distance with the predicate still intact.

**5. One-sentence test.** Can you state the idea in one sentence with no "and"? Two ideas in a frame is zero
ideas. → *"A dive watch in the shallowest water there is."*

**6. Prior art.** Search the library and the web. Existing → 0. This is where `signature.md` bites.

**7. Craft affordance.** Can it actually be lit and staged? A concept that cannot be photographed is not yet
concrete — make it more physical, not more vivid.

## Deck-level rule: do not make a deck of these

**The bizarreness memory advantage appears in mixed lists and disappears in pure lists.** Bizarre material is
remembered better than ordinary material *only when the two are studied together*; a set made entirely of
bizarre items loses the advantage, because distinctiveness is a contrast effect, not a property. The same
logic is von Restorff's isolation effect.

So a seven-frame deck carries **one or two** high-register-distance frames. The rest are ordinary, beautifully
executed, in-hand and environment work. **The goldfish frame is only memorable because the other six frames
are not goldfish.** A deck of seven surreal conceits is a pure list and reads as noise — which is exactly
what an unconstrained image model produces by default.

MAYA points the same way: typicality and novelty jointly predict preference and suppress each other. Advanced,
*yet acceptable*.

## Varying a frame that works

Change **one axis at a time**, and re-score. This is how one good idea becomes seven.

| Axis | Operation | Rolex example |
|---|---|---|
| **Source object** | swap within the same predicate *and* register | goldfish → a rubber duck → a denture tablet fizzing |
| **Register** | move the dial and watch the meaning change | goldfish → koi (adjacent, luxurious — weaker) → dishwasher rack (further, funnier) |
| **Visual structure** | juxtaposition → fusion → replacement | watch beside the bowl → the bezel *is* the bowl rim → an empty bowl with a watch-shaped ripple and one fish nosing it |
| **Predicate** | keep the product, change which truth you are saying | waterproof → *never needs charging*: the watch alone among dead phones, all screens black |
| **Figure/ground** | invert what is sharp, lit, or in focus | the fish are tack sharp and the watch is the blur they swim around |
| **Absence** | remove the product; leave its evidence | the tan line, the empty winder, the bracelet-shaped mark |

Applied to your own question — the fish become **lily pads and flowers** only if the predicate survives, and
it weakens: lily pads are decorative and adjacent-register, so the frame becomes pretty rather than witty.
**Shadows** change the predicate entirely (not "waterproof" but "keeps time"), which is a different, valid
idea: a sundial's shadow falling across a mechanical watch — two timekeepers, one obsolete.

## Connecting visuals to the product's own story

The strongest predicates come from four places. Mine all four before bursting:

- **Spec** — the number on the box. 300m. 20% shea butter. Bioceramic. IP68.
- **Material** — what it is made of and how that behaves. Aluminium is cold and crushable. Gold is soft.
- **Origin** — why it was built and for whom, especially when that is now obsolete. *The Submariner was made
  for divers who no longer dive.* Obsolete purpose is the richest seam in the whole method.
- **Ritual** — when in a life it gets used. Hand cream is a winter object, used indoors, after cold.

L'Occitane worked because *softness* is a predicate you can find in another object — a mohair glove is
literally soft, and it is also winter, and it is also a hand. **One prop, three predicates locked.** That
density is the mark of a strong choice: a weak object satisfies one predicate, a strong one satisfies three.

## Delivery format

When a brief arrives, show the reasoning before the prompts, as a short block:

```
TRUTHS      300m water resistance · mechanical, no battery · built for divers who no longer dive
PREDICATE   It survives underwater.
BURST       submarine · goldfish · ice cube · soap · denture tablet · dishwasher · rubber duck · tea bag
SELECT      goldfish — opposite register (domestic, cheap, comic), predicate intact
STRUCTURE   juxtaposition / opposition
SCORE       recoverable 2 · true 2 · non-substitutable 2 · distance 2 · one-sentence 2 · prior-art 0 (EXISTS — adgod)
VERDICT     rejected on prior art; take denture tablet, re-score
```

Then source photography for the chosen frame, then write the prompt. The reasoning block is not decoration —
it is the auditable part, and it is where a bad idea gets caught before it becomes a 500-word prompt and an
image generation.

## Sources

Phillips & McQuarrie, *Beyond Visual Metaphor: A New Typology of Visual Rhetoric in Advertising* (Marketing
Theory, 2004) · Giora et al., *Optimal Innovation and Pleasure* · Hekkert, Snelders & van Wieringen, *Most
Advanced Yet Acceptable* (2003) · Berlyne, collative variables and the inverted-U · von Restorff isolation
effect and the mixed-list bizarreness finding · Graf & Landwehr, Pleasure-Interest Model of Aesthetic Liking ·
Loewenstein, information-gap theory of curiosity.
