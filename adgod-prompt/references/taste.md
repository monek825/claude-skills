# Image taste system

Adapted from the user's Designare “AI Reference & Taste Guide.” This is a decision layer for image prompts, not a style recipe. Use it to turn visual judgement into specific, testable direction before writing the 12-block prompt.

## The principle

Generic language retrieves the category average. Specific images come from a studied reference, one named mechanism, hard constraints, a kill list, and a verdict written before generation. “Cinematic,” “premium,” “editorial,” and “realistic” are labels, not decisions. Translate them into camera, light, composition, material, colour, human action, and omission.

Do not import the Designare guide's graphic-design rules literally into photography. Type count, grid, and accent-percentage are useful only when the image contains those elements. Preserve the underlying habit: observe, name the mechanism, constrain, compare, reject, and decide.

## The image reference brief

Fill this before the prompt prose. Defaults may be inferred from the product image and user brief, but the decisions must still be explicit in the working notes.

1. **Job** — one sentence and one verb: what should the image make the viewer notice, feel, understand, or do?
2. **Viewer and surface** — who sees it, where, at what crop/size, and for how long?
3. **Reference and one move** — identify one compositional, lighting, camera, material, or human-action mechanism to borrow. Never use only “in the style of.”
4. **Visual constraints** — aspect ratio; subject scale and placement; palette family; camera/lens/aperture; light direction and shadow behaviour; allowed props; required product details.
5. **Kill list** — name the defaults that must not enter: generic studio gradient, floating object, stock pose, empty environment, invented logo, plastic skin, decorative clutter, or any scene-specific cliché.
6. **Tone in three words** — use words with slight tension, such as “observed, electric, unpolished,” not three synonyms like “clean, modern, premium.”
7. **Done looks like** — a visible pass/fail condition: e.g. “the product reads at thumbnail size, the hand action is physically believable, and the setting could not be swapped for a stock studio.”

## Six-pass image reference read

Read the actual reference, not a remembered category. Write observations before borrowing anything.

1. **Structure** — squint. Mark the dominant mass, secondary mass, horizon/vanishing logic, crop pressure, negative space, and reading order.
2. **Camera** — estimate viewpoint, distance, focal-length feel, camera height, tilt, depth of field, and what is deliberately sharp or soft.
3. **Light and colour** — name source direction, hardness, falloff, shadow density, practical sources, colour temperature, and the role of each major colour. Separate the field colour from the light colour.
4. **Tension** — find the controlled irregularity: an off-axis gesture, awkward crop, mixed light, rough surface, visual interruption, or scale mismatch that makes the frame specific. Do not copy the subject if the mechanism is enough.
5. **Detail and physics** — inspect skin, hair, fabric, glass, chrome, paper, contact shadows, reflections, occlusion, wrinkles, fingerprints, dust, and edge wear. Decide which details prove a real capture and which are merely decoration.
6. **Intent and transfer** — state who the frame is for and what it is doing. Then name what survives when the product, person, or setting changes and what must be rebuilt through `adaptation.md`.

One reference read six ways is more useful than a large moodboard skimmed once. For a set, annotate each selected reference with:

`[shelf] — [one mechanism being borrowed] — [where it will work] — [what will be different]`

Useful image shelves are `composition`, `camera & light`, `colour & material`, `human contact`, and `outside photography`. Keep a small active library and remove weak or redundant references rather than treating saves as study.

## Specificity ladder

Before generating, identify the rung:

- **1 — Category:** “a realistic lifestyle product photo.”
- **2 — Adjectives:** “cinematic, premium, editorial, authentic.”
- **3 — Attributes:** concrete subject, setting, camera position, lens feel, light direction, palette, crop, and physical action.
- **4 — Attributes + mechanism:** those decisions plus one transcribed move from a real reference.
- **5 — Mechanism + kill list + verdict:** add exclusions and the exact condition that makes the frame successful.

Prompts for this skill should reach rung 4 or 5. Add decisions, not more adjectives. A reference mechanism is “a cropped shoulder blocks the near edge while a window reflection carries the face,” not “in the style of street photography.”

## Critique loop

When iterating, diagnose in this order:

1. **Brief:** Is the frame answering the intended job? If not, rewrite the brief; do not polish the wrong answer.
2. **Structure:** Does the squint reading order match the priority? Correct dominance, spacing, crop, contrast, or alignment before colour grading.
3. **Craft and truth:** Check optical alignment, contact physics, skin and material detail, reflections, edges, anatomy, and the smallest visible text. Fix manually where possible.

Change one variable per round so the result teaches you something. Keep a high kill rate; exploration is not keeping every near-duplicate. After roughly twenty variations, stop and judge later—discrimination degrades faster than generation does.

## Taste gate before delivery

Pass only when:

- the job is stated and visibly answered;
- the reference is named by mechanism, with a clear difference from the source;
- the subject remains physically and culturally credible in its setting;
- the frame has a dominant read and intentional negative space or crowding;
- the light, palette, camera, material, and human action are decisions rather than mood words;
- the kill list did not creep back in;
- the image still works at its real viewing size;
- every important element has an explanation other than “the model made it.”

The guiding question is: **could another competent prompt writer have arrived at this frame from the same category, or does it reflect a reference you actually studied and a choice you can defend?**
