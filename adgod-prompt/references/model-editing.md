# Model identity editing — controlled physical-trait recasting

Use this reference whenever a fashion, portrait, beauty, or lifestyle prompt keeps the shot but changes the person. The objective is **identity replacement with shot continuity**: the new model must occupy the same composition, wear the same wardrobe concept, perform the same action, and receive the same light unless the user explicitly requests another change.

The FASHIONNN supplemental examples live in `fashionnn-corpus.md`; their image/prompt index is `/Users/brayden/Documents/adgod-prompts/refs/fashionnn/INDEX.md`.

## Accuracy boundary

Text can specify a plausible **type** of person: age band, ancestry/appearance, skin tone, facial geometry, hair, build, and visible marks. Text alone cannot reproduce a particular person's identity accurately. For accurate identity, require a clean portrait reference with:

- one unobstructed adult face, preferably neutral expression;
- even, neutral light without colour filters or beauty effects;
- sharp eyes, visible jawline, and natural skin texture;
- minimal occlusion from hair, hats, sunglasses, hands, or phones;
- a useful crop from the top of the head through the shoulders;
- permission to use the person's likeness.

With multiple references, designate one identity master and use the others only for views that the master does not show. Do not average unrelated faces. If no clean portrait exists, state that the result will be a plausible model matching the description, not an accurate likeness.

## The edit boundary

### Editable identity and physical traits

These form one coordinated `MODEL_IDENTITY` layer:

- adult apparent age band;
- gender presentation and consistent pronouns, only when requested or required by the source grammar;
- ancestry/ethnic appearance, when explicitly supplied;
- skin depth, undertone, surface texture, freckles, moles, scars, vitiligo, and other stable marks;
- face shape, forehead, cheekbones, jaw, chin, nose, lips, ears, and other distinctive facial geometry;
- eye colour and shape, eyelids, lashes, and brow colour/density/shape;
- hair colour, roots/highlights, texture, density, length, hairline, part, and style;
- body height, build, proportions, and visible limb characteristics when relevant to the crop;
- nails and other stable grooming details;
- makeup palette, coverage, placement, and finish when the user asks to change it.

### Locked shot invariants

Do not change these merely because physical traits changed:

- **SCENE:** location, architecture, terrain, weather, time, props, background people, spatial layout, and realism cues.
- **CAMERA:** body/device, lens, focal length, camera position, height, tilt, distance, crop, aspect ratio, depth of field, focus plane, exposure, grade, grain, and border treatment.
- **LIGHTING GEOMETRY:** source type, direction, height, distance, hardness, fill ratio, rim side, shadow direction, bounce source, practical lights, and time-of-day logic.
- **MOOD:** the narrative and editorial register.
- **WARDROBE CONCEPT:** garment category, design, colour, material, construction, layering, styling intent, and hero accessories.
- **POSE AND BODY ORIENTATION:** seated/standing state, weight shift, torso turn, head angle, shoulder height, limb placement, and camera-facing side.
- **GAZE AND EXPRESSION:** gaze target, eye state, mouth state, smile/pout/laugh, and candid versus posed character.
- **ACTION:** the event taking place and its timing.
- **PRODUCT:** identity, scale, material, logo/artwork, camera-facing side, orientation, visibility, and hero status.
- **CONTACT PHYSICS:** which hand touches or holds what; grip; finger placement; wrist rotation; shoulder strap path; garment-to-body contact; cloth tension and pooling; hair/hat contact; occlusion order; contact shadows; ambient occlusion; gravity; reflection; and environmental colour bounce.

If the user requests a locked attribute change too, treat it as a second explicit edit and run the separate adaptation cascade in `adaptation.md`.

## Canonical physical-trait schema

Create one normalized identity object before rewriting prose. Omit unspecified fields rather than inventing excessive detail.

```yaml
model_identity:
  reference_mode: "portrait-reference | text-only"
  reference_role: "exact identity master | plausible type"
  adult_apparent_age: ""
  gender_presentation: ""
  pronouns: ""
  ancestry_or_appearance: ""
  skin:
    depth: ""
    undertone: "warm | cool | neutral | olive"
    texture: ""
    stable_marks: ""
  face:
    shape: ""
    cheekbones: ""
    jaw_chin: ""
    nose: ""
    lips: ""
    distinctive_features: ""
  eyes:
    colour: ""
    shape: ""
    lids_lashes: ""
    brows: ""
  hair:
    colour: ""
    roots_highlights: ""
    texture: ""
    density: ""
    length: ""
    hairline: ""
    part: ""
    style: ""
  body:
    height: ""
    build: ""
    proportions: ""
    visible_details: ""
  grooming:
    nails: ""
    other: ""
  makeup:
    base: ""
    complexion: ""
    eyes: ""
    brows: ""
    lips: ""
    finish: ""
```

Write the identity anchor in this order: `adult age → appearance/ancestry → skin → face → eyes/brows → hair → build → stable marks`. Reuse the same anchor verbatim across a multi-image set. Slide-specific hair styling or makeup follows the anchor and must not silently mutate the person's stable identity.

## Dependency cascade

A trait edit is not confined to the `MODEL` sentence. Rewrite every dependent description, but preserve the physical setup.

| Changed trait | Required dependent updates | Must remain fixed |
|---|---|---|
| Skin depth/undertone | `MODEL`, `SKIN`, foundation/base, blush/bronzer/contour/lip harmony, visible highlight and shadow response, colour-bounce wording, old skin/wardrobe contrast claims | light source, direction, hardness, exposure intent, garment colours |
| Skin texture/stable marks | `MODEL`, `SKIN`, retouch/texture language, visible placement at the current crop | crop, focus plane, lighting geometry |
| Face geometry | identity anchor, likeness/reference sentence, compatible makeup placement | gaze, head angle, expression, camera position |
| Eye/brow traits | `MODEL`, eye/brow makeup colours and density; eye visibility if glasses already exist | glasses, gaze target, eye-open/closed state |
| Hair colour | `MODEL`, hair highlight/rim-light response, wardrobe/background contrast wording | light colour and direction, hairstyle geometry unless requested |
| Hair texture/length/style | `MODEL`, hat/headband fit, collar/shoulder occlusion, wind/gravity behaviour, silhouette, shadow/contact clauses | hat/headband identity, pose, wind direction, crop |
| Height/build/proportions | `MODEL`, garment fit and tension, hem position on the body, sleeve/trouser break, occupied frame fraction if necessary | wardrobe design, camera/lens, stance, action |
| Makeup | `MAKEUP`, compatible `SKIN` finish, any facial-feature emphasis | identity geometry, light rig, mood unless expression also changes |
| Nails/grooming | `MODEL` or `MAKEUP`, hand close-up details and prop-contact visibility | hand assignment, grip, prop orientation |
| Pronouns/gender presentation | every pronoun, relational noun, and gendered descriptor throughout the complete prompt | scene and action unless explicitly requested |

### SKIN rewrite rule

Separate three concepts:

1. **Intrinsic skin:** depth, undertone, texture, stable marks.
2. **Cosmetic finish:** bare, natural, dewy, satin, matte, powdered, glossy.
3. **Light response:** warm rim, cool fill, specular highlight, soft shadow, neon bounce.

Do not turn a lighting effect into an intrinsic trait. “Warm orange neon reflects onto deep neutral-brown skin” preserves both the skin and the scene; “orange skin” does not. Do not equate darker skin with lower exposure, or lighter skin with overexposure. Keep intentional exposure and relight only in words describing how the fixed source renders the new skin.

### MAKEUP rewrite rule

Preserve makeup **intent and intensity** unless the user changes it. Translate the palette to the new traits: base depth and undertone, blush/bronzer visibility, lip hue, brow colour, and eye contrast. Avoid contradictory stacks such as “barely-there makeup” plus “heavy full-coverage base,” or “matte skin” plus “dewy glass-skin finish.”

### Wardrobe-fit rewrite rule

The garment is locked; its physical fit may respond to the new body. Update only what contact requires: fitted versus relaxed tension, shoulder seam position, waistband placement, hem height, sleeve break, exposed skin area, cloth folds, and pooling. Never redesign the garment, change its size category, recolour it, or substitute accessories unless asked.

### Crop rewrite rule

Keep the camera, lens, and composition. If height or proportions change, express the same intended crop and occupied frame fraction—for example, “three-quarter crop ending at mid-calf” or “face remains the same size in frame.” Do not solve a body change by moving the camera or changing focal length.

## Pose, product, and contact-physics lock

Before editing, extract a compact invariant ledger:

```yaml
shot_invariants:
  body_orientation: ""
  head_and_gaze: ""
  left_hand: ""
  right_hand: ""
  product_orientation: ""
  garment_contacts: ""
  hair_headwear_contacts: ""
  foreground_occlusion: ""
  gravity_and_motion: ""
  camera_geometry: ""
  lighting_geometry: ""
```

Keep left/right assignments explicit. Preserve hand-to-prop contact, the visible product face, strap routing, garment drape, and foreground scale. If a changed trait makes an invariant impossible—for example, “long hair falls forward” after changing to a shaved head—remove the impossible clause and replace it with a physically coherent description that preserves the silhouette and composition as closely as possible. Flag that dependency instead of leaving a contradiction.

## Recast plus a new held object (verified 2026-09-14)

The most common real brief — a different model holding a specific product — is two edits. Run them in this
order and keep them separate:

1. **Identity recast** through the schema and cascade above. Pick hair that keeps the source silhouette (same
   length and occlusion) unless the brief asks otherwise; the pose, crop and hair-halo invariants then survive.
2. **Held-object swap** as a second explicit edit. Take the grip from the affordance table in `adaptation.md`
   and write it into the hand clause: which hand, which fingertips, skin compression at contact. Rewrite the
   `PRODUCT` section with a fidelity lock that keeps the product's own printing and builds its reflections from
   the scene, not the plate. Negate the old object and its gesture (`no mug, no cup, no drinking gesture`).
   Keep the beat: object height, head angle, expression.

**Rewrite airbrushed skin during any recast.** Three FASHIONNN prompts ask for it — luxry S02 `flawless skin`,
S05 `Smooth, no visible texture`, S06 `poreless` — and `scripts/lint-realism.py` warns on all three. Replace
with visible pores and fine texture. None of the 14 references shows a deep-skin model, so there is no
in-corpus precedent; the verified example renders deep brown skin correctly with the SKIN and exposure rules.

Verified example with prompt, inputs and result:
`/Users/brayden/Documents/adgod-prompts/refs/fashionnn/recast-examples/S03-west-african-vt-bottle.md`. Identity,
hair, wardrobe, scene, pose and the chin-level hold all carried in one generation. The finish stayed as glossy
as the Higgsfield source: **a recast changes the person, not the prompt's finish.**

## Rewrite procedure

1. **Declare scope.** List only requested identity/physical changes. Everything else is locked.
2. **Choose reference mode.** A clean portrait reference means exact identity; text-only means plausible type.
3. **Normalize identity.** Fill the canonical schema and resolve alternatives to one value.
4. **Extract invariants.** Record scene, camera, light, mood, wardrobe concept, pose, gaze, action, product orientation, and contact physics.
5. **Replace, do not append.** Remove the entire old identity clause, then insert one consolidated new anchor. Never leave both old and new ethnicity, complexion, eye, hair, age, or build language.
6. **Run the cascade.** Rewrite `SKIN`, `MAKEUP`, wardrobe fit, crop occupancy, and light-response/contrast wording touched by the new traits.
7. **Restore invariants.** Confirm that all locked shot facts remain present and unchanged.
8. **Clean contradictions.** Search the full prompt for residual traits, alternatives, incompatible finishes, impossible hair/headwear relations, old body-fit language, and conflicting pronouns.
9. **Read for physics.** Verify hand assignment, grip, product face, straps, occlusion, cloth tension, hair gravity, shadows, bounce, and reflections.
10. **Read for identity continuity.** Across a deck, compare the identity anchor word-for-word; only explicitly variable styling may differ.

## Contradiction and pronoun cleanup

Perform a whole-prompt search, not a paragraph-only check:

- old ancestry or appearance terms;
- old skin depth/undertone words and incompatible colour metaphors;
- old eye colour, brow colour, hair colour/length/texture/style;
- old age/build/height and garment-fit consequences;
- incompatible pairs such as `warm cool undertone`, two hair lengths, two partings, or both matte and dewy finish;
- stale gendered nouns and every subject/object/possessive pronoun;
- pose verbs that conflict with the named camera side or hand assignment;
- gaze/expression language that conflicts with closed eyes, sunglasses, or head direction.

Pronouns must be consistent across `MODEL`, action, wardrobe, product, lighting, camera, and mood. When neutral grammar works, repeat “the model” instead of forcing gendered pronouns. Never change pronouns as an inferred consequence of ancestry, hairstyle, wardrobe, or body type.

## Delivery contract

When returning a recast prompt, state the reference mode once. If text-only, say “plausible model matching the description.” If using a clean portrait, place the identity-reference contract at the start and state that pose, expression, wardrobe, scene, product, camera, and lighting come from the shot prompt—not from the portrait. Then deliver the complete cleaned prompt, not a patch or a list of substitutions.

## Final validation

- [ ] Adult age band is clear when age matters.
- [ ] Identity reference is clean and designated, or the text-only limitation is stated.
- [ ] One ancestry/appearance description, one skin depth, and one undertone remain.
- [ ] One face, eye, hair, build, and makeup specification remains.
- [ ] `MODEL`, `SKIN`, and `MAKEUP` agree.
- [ ] Fixed lighting is described accurately on the new skin and hair.
- [ ] Wardrobe design is unchanged; fit/contact updates are physically coherent.
- [ ] Camera/lens/crop intent is unchanged; frame occupancy still matches.
- [ ] Scene, mood, pose, gaze, action, product identity/orientation, and contact physics are preserved.
- [ ] Left/right hands, straps, props, hair/headwear, occlusion, gravity, shadow, and bounce are coherent.
- [ ] All pronouns are consistent.
- [ ] No residual old trait or unresolved alternative remains.
