# Swap adaptation — affordances and cascade rules

The corpus prompts describe **one specific product in one specific scene**. Reusing a prompt for a
different product, subject, or environment without re-deriving the dependent clauses is the single most
common failure mode: a tote worn as a backpack, a watch "gripped by the handle", a studio palette left
warm after the background moved outdoors.

Rule of the file: **the style plate owns the look; the product owns the interaction.** Never inherit a
carrying, wearing, holding, or placement verb from a reference image. Derive it fresh from the new product.

---

## 1. Affordance table

How each product category is naturally displayed. Pick the row for the *new* product, not the reference's.

| Product | Worn / carried | Held | Placed |
|---|---|---|---|
| Backpack, rucksack | both shoulder straps, high on the upper back, slight forward lean | one strap in hand, hanging at side | upright on ground/rock, front facing camera |
| Tote, shopper | over one shoulder, top handles bunched; or crook of the elbow | top handles in one hand, bag hanging at thigh level | standing upright, handles settled, structure held |
| Crossbody, messenger, camera bag | strap diagonally across the torso, body at hip | by the strap at the top | resting on its base, flap facing camera |
| Clutch, pouch | under the arm | flat in one hand, or pinched at the top edge | flat or leaning against a support |
| Duffle, weekender | long strap over the shoulder | twin handles gripped together, arm straight | on its side, handles composed |
| Belt bag | around the waist or across the chest | by the buckle | coiled, buckle facing camera |
| Handbag with top handle | crook of the elbow, forearm horizontal | top handle in the fingers, bag hanging | upright, handle standing |
| Suitcase, trolley | — | telescopic or leather handle in hand, walking | upright, diagonal to camera |
| Watch (wrist) | on the wrist, dial to camera, bracelet articulated over the wrist bone | between thumb and fingers, dial to camera | flat, or draped over an object, bracelet open |
| Pocket watch on a lanyard / chain | lanyard over the head, case resting at the sternum, dial outward; flipped up to read | dangled from the lanyard hooked over two fingertips, case swinging free; or case pinched at the caseband with the lanyard slack | laid dial-up with the lanyard pooled in a loose S beside it; or lowered case-first into a pocket, lanyard tail over the seam |
| Eyewear | on the face, temple arms over the ears | by one temple arm, lenses to camera | folded on a surface, or open and standing on the temples |
| Earbuds | in the ear, stem angled to the jaw | pinched between thumb and index | in or above the open charging case |
| Headphones | over the ears, headband centred | by the headband | folded flat, or on a stand |
| Sneakers, shoes | on the feet | by the heel collar or laces | paired on a surface, three-quarter angle |
| Jacket, outerwear | worn, arms in sleeves | over the forearm, or held up by the shoulders | on a hanger, or laid flat |
| Fragrance bottle | — | between fingers at neck/collarbone level, or sprayed | upright, cap on or beside |
| Lipstick, gloss, mascara | — | between fingers near the mouth or cheekbone, applicator visible if in use | upright, or lying with cap beside |
| Compact, blush, palette | — | open in the palm, or pinched at the edge | open on a surface, pan facing camera |
| Skincare jar / tube / dropper | — | in the palm; dropper held above the skin | upright, lid beside |
| Can, bottle, beverage | — | wrapped in the hand at chest level; or at the lips, head tilted back | upright, label to camera, condensation |
| Tin, canister | — | one hand under the base, lid removed by the other | upright, lid off and placed beside |
| Phone, tablet | — | in one hand, screen or back to camera | propped, or flat on a surface |
| Laptop | — | closed, under the arm | open on a desk at a working angle |
| Jewellery — ring / necklace / earring | on the finger, neck, or ear | pinched between fingertips | on a plinth, fabric, or reflective surface |
| Food, produce | — | in the palm or fingertips | on a plate, board, or in a build |

If the product isn't listed, ask: *how does a person get this from the shelf to use?* That verb is the
affordance. State it in the prompt in the same physical detail the corpus uses for straps and grips.

**The near-miss row is more dangerous than a missing row.** A product absent from the table makes you think;
a product whose *name* matches a row makes you stop thinking. The AP × Swatch Royal Pop is a watch, so the
Watch row says wrist — and the wrist is the one place this product never goes. Read the row you land on
against the actual object before using it: if the physical interaction differs, the row is wrong for you and
you derive fresh. Write the new row back into this table when you do, as the pocket-watch row above was.

A derived affordance is worth four gestures, not one. Name them all before choosing: worn, held, dangled,
placed, stowed. The gesture no competitor product can perform is usually the strongest frame in the deck —
for the pocket watch it is the hand lowering the case into a pocket with the lanyard over the seam, which no
wristwatch can stage.

---

## 2. Affordance override sentence

When a style plate shows a different affordance from the new product, the prompt must say so explicitly.
Insert this immediately after the adaptive-scale clause (block 3), before the scene declaration:

> `Do not inherit the carrying method, grip, or placement from the style reference. The product is a
> <product type>, which is naturally <affordance from the table>; restage the subject's pose, hand
> position, and body contact accordingly while preserving the reference's camera angle, framing, crop,
> lighting design, background, palette, and colour grading exactly.`

Then rewrite the pose and physics clauses from the new affordance. Worked example — North Face 02
(backpack worn on the back) retargeted to a structured leather tote:

> ~~`worn high on the back, slightly angled toward camera... realistic strap tension, natural fabric
> compression where it contacts clothing, authentic gravity pull`~~
>
> `carried over the right shoulder with the twin top handles bunched naturally in the hand, the body of
> the bag resting against the outer hip, with realistic handle tension where the leather bends under
> load, authentic weight pulling the shoulder line down slightly, natural creasing at the handle
> attachment points, structured leather holding its shape rather than collapsing, and accurate contact
> shadow where the bag meets the jacket.`

Camera angle, snowfield, sky gradient, daylight, palette and tech tail all carry over unchanged.

---

## 3. What is inheritable vs. what must be recomputed

| Change the user asks for | Inherit unchanged | Must rewrite |
|---|---|---|
| **Product swap, same affordance** (backpack → backpack) | everything except block 2 | fidelity lock (new category enumeration) |
| **Product swap, different affordance** (backpack → tote) | camera body/lens/aperture, lighting rig, background, palette, grade, negative list, tail | fidelity lock · affordance override · pose and body contact · contact physics · frame position and scale · any prop that existed to serve the old affordance |
| **Product swap, different scale** (can → suitcase) | lighting rig, palette, grade, background family | frame fraction, camera height, aperture (bigger object at the same distance needs more depth — step toward f/8–f/11), prop scale relationships |
| **Subject swap** (different model, or none) | camera, background, palette, grade, product fidelity lock | wardrobe · hair · skin rendering clause · pose · crop bounds · hand/body interaction physics · catchlight and facial-shadow clauses |
| **Model added to a still-life** | background, palette, grade | crop bounds, wardrobe, skin rendering, affordance and grip physics, aperture (usually opens to f/5.6–f/8), lighting gains a fill and catchlight clause |
| **Model removed** | lighting rig, background, palette | frame position (product must re-centre), a placement affordance replaces the held one, prop inventory to fill the space, aperture usually closes to f/11 |
| **Background swap, studio → studio** | camera, lighting rig, physics | background phrase, palette, environmental colour bounce onto the product, grade |
| **Background swap, studio → location** | camera body, fidelity lock | lighting rig becomes natural (sun direction, quality, time of day) · background · palette · grade · atmospheric haze · environmental reflections and colour bounce · contact shadows to the new ground material · often aperture opens |
| **Background swap, location → studio** | fidelity lock | lighting rig becomes named instruments · seamless backdrop · surface material · palette · grade · aperture usually closes to f/11 |
| **Lighting change** | camera, background geometry, product | instrument, position, quality, shadow behaviour, key level, background luminance, palette temperature, grade |
| **Palette change** | camera, lighting rig, composition | background colour, prop colours, colour bounce onto the product, grade adjectives |
| **Aspect ratio change** | everything | frame position, crop bounds, negative-space clause, prop inventory (a 4:5 tableau loses props at 1:1) |

Cascade rule: **anything the changed element physically touches, reflects into, or casts onto must be
rewritten.** A new background changes the light bouncing onto the product; a new product changes what the
hand does; a new model changes the wardrobe colours in the palette.

---

## 4. Conflicts the table can't resolve

When the style plate's narrative beat is impossible for the new product — reference shows a model drinking
from a can, the new product is a watch — keep the **beat**, restage the **action**:

- Keep: crop, camera height, energy, light direction, palette, grade, negative space
- Replace: the action with the nearest affordance from the same emotional register

Drinking (consumption, head back, arm raised) → for a watch: checking the time, wrist raised to the same
height, same head angle, same arm geometry. For eyewear: settling the frames on the nose, same raised arm.
For a fragrance: spraying at the neck, same lifted forearm.

State the substitution in the prompt so the model doesn't try to reconcile both:

> `The subject's raised-arm gesture and head angle from the style reference are preserved, but the action is
> restaged as <new action> appropriate to the product; no drinking, no beverage container, and no
> consumption gesture appears in the final image.`

That trailing negative matters — without it the model often keeps a ghost of the original object.

---

## 5. Quick check before writing a swapped prompt

- [ ] Named the new product's affordance out loud, from the table
- [ ] Affordance differs from the style plate? → override sentence present, pose and physics rewritten
- [ ] Every prop that only existed to serve the old product has been removed or re-justified
- [ ] Frame fraction and camera height re-derived if the size class changed
- [ ] Aperture re-checked against the new depth requirement
- [ ] Background swap? → colour bounce, reflections, contact-shadow surface and grade all updated
- [ ] Subject swap? → wardrobe, hair, skin clause, crop and grip physics all updated
- [ ] Any impossible inherited action explicitly negated in the negative list
