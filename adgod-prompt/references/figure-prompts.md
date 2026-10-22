# Figure and fashion frames — the descriptive register

The 12-block anatomy in `anatomy.md` is **directive**: it instructs a model to build a scene. There is a
second register, used for frames whose subject is a *person* rather than an object, which is **descriptive**:
it reads as an analyst's exhaustive account of a photograph that already exists, and it ships with the
palette measured out in hex.

Both are transcription. The directive register transcribes a scene the model must construct; the descriptive
register transcribes a photograph so completely that reconstruction is the only thing left to do.

## Supplemental fashion/model routing

For fashion, portrait, model-led lifestyle, streetwear, travel-fashion, or everyday figure prompts, also load
`fashionnn-corpus.md`. It contains 14 page-mapped prompt/reference pairs that are useful for scene realism,
wardrobe description, pose, gaze, phone-camera language, and body/garment/prop contact. They are identified as
AI-generated FASHIONNN.AI / LUXRY.AI references and are **supplemental**, not Adgod ground truth.

When the user changes a model's physical traits or asks to preserve a person across frames, also load
`model-editing.md` before rewriting. Keep scene, camera, lighting geometry, mood, wardrobe concept, pose, gaze,
action, product orientation, and contact physics locked by default; recast identity through the full dependency
cascade rather than replacing a single adjective.

## When to use which

| Use directive (`anatomy.md`) | Use descriptive (this page) |
|---|---|
| The product is the subject | A person is the subject |
| Studio, still-life, prop tableau | Fashion editorial, campaign portrait, lifestyle figure |
| Fidelity lock on a manufactured object | Fidelity is about styling, light quality and mood |
| Negative list carries the weight | The exhaustive description carries the weight |

For a deck that mixes both — a campaign with three still-lifes and two figure frames — write each frame in
its own register and keep the *campaign constants* identical across them.

## What the descriptive register does differently

- **Third-person analytical voice, not imperative.** "A straight-on, medium-long shot features a young woman
  reclining sideways on a padded armchair" — the frame is reported, not commanded.
- **The shot is named first**, in the language of a shot list: eye-level close-up portrait · straight-on
  medium-long shot · tightly cropped, subject off-centre.
- **Wardrobe and material are enumerated garment by garment**, including finish and how it is worn — the same
  exhaustiveness the corpus applies to props.
- **Expression and gaze are stated explicitly.** Pensive, direct, serious, slightly pursed. Never an emotion
  word about the *viewer* ("aspirational") — only what the face is doing.
- **The lighting is characterised, not rigged.** "Soft and diffuse with minimal shadow, evoking a studio
  setup" rather than an instrument-and-position spec. The exception: state the hour when it is daylight —
  "late afternoon or golden hour" is doing real work.
- **The technical read is descriptive too**: shallow depth of field, no notable lens distortions, subtle
  digital grain, natural skin texture, high-resolution digital photograph.
- **It closes on the mood**, in two or three adjectives, after everything physical has been settled.

## The hex palette lock

Append the measured palette as an explicit array after the prose:

```
HEX VALUES: ["#f3efe5", "#b5957c", "#bfa695", "#a18265", "#e9d7c4", "#85694e", ...]
```

Fifteen swatches, ordered roughly by area, covering ground, skin, wardrobe, accent and shadow. This is the
strongest colour control available in either register — compound colour words ("warm caramel, cream, amber")
set a direction, hex sets the actual grade, and it survives across frames far better than adjectives do.

**Carry one palette array across a whole deck** and the set reads as one shoot even when the scenes differ.
Vary it per frame and you get five unrelated images. This is the descriptive register's equivalent of locking
the register in `SKILL.md` step 2.

## Exemplar 1 — staged interior, luxury fashion

> A straight-on, medium-long shot features a young white woman with short brown hair and striking, model-like
> facial features reclining sideways on a padded armchair with her face turned toward the camera. Her
> expression is pensive and her gaze is direct. She wears a black long-sleeve dress or top adorned with
> baroque floral embellishments in gold and orange, creating a textured, decorative effect. Her legs are
> exposed, revealing light gray mid-calf socks and brown leather penny loafers, both bearing the brand logo in
> gold embossing. Clutched in her left hand across her lap is a large brown leather handbag with prominent
> branding and attached decorative floral charm accents. The setting is an elegant, staged indoor scene, with
> the chair upholstered in pinkish floral brocade fabric against a pastel wall and opulent gold and brown
> draped curtain. The light is soft and diffuse with minimal shadow, evoking the style of a studio setup.
> Dominant colors in the image include pastel peach, taupe, brown, black, and gold, with accent colors from
> the embellishments and accessories. The image has a shallow depth of field focused on the subject, with the
> backdrop subtly out of focus, and no notable lens distortions are present. The composition is highly
> stylized, with a vintage, editorial aesthetic, likely digitally retouched for a smooth, painterly effect.
> The mood is sophisticated yet dreamy, with a sense of nostalgia and high-fashion detachment.
>
> HEX VALUES: ["#f3efe5", "#b5957c", "#bfa695", "#a18265", "#e9d7c4", "#85694e", "#b9babc", "#ddbd9c",
> "#33200c", "#cfd3d9", "#63503d", "#1b1207", "#8a909a", "#513518", "#3e342a"]

## Exemplar 2 — natural light, wet-hair beauty portrait

> An eye-level close-up portrait captures a young adult Caucasian woman, likely in her early 20s, with
> striking, model-like facial features including symmetrical lips, high cheekbones, and a prominent brow. Her
> wet, light brown hair, tangled and stringy, falls across her slightly glistening face, suggesting she has
> recently been swimming or exposed to a humid environment. She wears a soft-textured, thick terrycloth towel
> with large, high-contrast green and white checkered pattern wrapped around her shoulders, with the edge of a
> second towel, purple-striped, just visible at the lower left. Her piercing direct gaze, serious expression,
> and slightly pursed lips create an intensely pensive and moody presence. The natural lighting is late
> afternoon or golden hour sunlight, casting strong warm highlights and deep, dramatic shadows. The color
> palette is dominated by warm skin tones, green accents, and subtle gray-blues in the blurry background,
> where hints of water and negative space are discernible. The composition is tightly cropped, putting strong
> emphasis on her face, which sits just off-center, and uses a wide aperture to achieve a shallow depth of
> field that isolates the subject from her surroundings. This high-resolution digital photograph is sharp with
> subtle digital grain and natural skin texture present, contributing to an organic, fashion-editorial
> aesthetic that is simultaneously intimate and enigmatic.
>
> HEX VALUES: ["#101619", "#55382a", "#844f32", "#2f2321", "#1b392a", "#2e434e", "#ad7048", "#b4c04c",
> "#405965", "#d29c6d", "#e3d4c2", "#cbb99c", "#979288", "#7d912c", "#617277"]

## Notes on the exemplars

Both name a real brand in their original form. Producing branded fashion frames for a brand you do not work
for is spec work — label it as spec, do not monetise it, and never present it as the brand's own. See the
originality gate in `signature.md`; a *format* is copyable, a brand's authorship is not.

Exemplar 2 is the stronger of the two as a model. It earns its mood from physical facts — wet stringy hair,
a glistening face, a terrycloth weave, a second towel just in frame — and only then names the mood. Exemplar
1 leans harder on style words ("painterly", "dreamy") that describe an effect rather than a cause; when
adapting it, replace those with the physical thing producing them.

Neither carries a negative list. Add one from `anatomy.md` Block 11 when generating, especially the hands and
skin lock — these are figure frames and hands remain the highest-failure element in the format.
