# Camera, lens, aperture, lighting and palette tables

Every value below is attested in the 62-prompt corpus. Do not invent gear outside these tables — the
specific bodies are doing real work as style tokens, and unfamiliar ones dilute the look.

---

## Camera bodies (pick one, never mix two in a prompt)

| Body | Used for | Full string as written |
|---|---|---|
| Phase One XF IQ4 150MP | Studio still-life, hard goods, watches, tins, cans, submerged/liquid work, electronics macro. The default and by far the most common. | `Phase One XF IQ4 150MP medium-format camera` |
| Hasselblad X2D 100C | Beauty, cosmetics, flat-lays, fashion close-ups. | `Hasselblad X2D 100C medium format camera` |
| Full-frame professional | Direct-flash street editorial, nature/bokeh work — anywhere the look should read as a real 35mm camera, not a digital back. | `full-frame professional camera` |
| Unnamed medium format | When gear specificity isn't needed; still say medium format. | `medium-format camera look` / `medium-format camera quality` |

## Lenses (must pair with the body)

| Lens | Pairs with | Use |
|---|---|---|
| `Schneider Kreuznach 120mm LS Macro Blue Ring lens` | Phase One | Default hero product macro. Highest-fidelity option in the corpus. |
| `Schneider Kreuznach 120mm lens` | Phase One | Tight portrait / product portrait without macro framing. |
| `Schneider Kreuznach 80mm lens` | Phase One | Product-in-scene, wider still-life, mid-body crops. |
| `Schneider Kreuznach macro lens` / `macro optics` | Phase One | Generic macro when focal length doesn't matter. |
| `Schneider Kreuznach wide-angle lens` | Phase One | Low-angle athletic/lifestyle with perspective distortion. |
| `Schneider Kreuznach portrait lens` | Phase One | Beauty/lifestyle portraits. |
| `XCD 90V lens` | Hasselblad | Beauty portrait + product still-life. |
| `100mm macro lens` | Hasselblad | Flat-lay, cosmetic macro. |
| `120mm macro lens` | Hasselblad | Suspended-product / liquid-architecture beauty. |
| `90mm lens` / `90mm portrait lens` | Hasselblad | Symmetrical still-life; beauty portrait. |
| `80mm lens` | Hasselblad | Extreme close-up fashion (f/2.8 territory). |
| `85mm lens` / `85mm product photography look` | full-frame or generic MF | Lifestyle, held-product, telephoto compression. |
| `24–35mm lens` | full-frame | Direct-flash wide editorial, crouching/hand-forward compositions. |
| `100mm macro commercial lens` | generic MF | CPG hero with ingredient build. |
| `80mm lens perspective` | generic MF | Outdoor hero object on location. |

## Aperture selection (this is a decision, not decoration)

| f-stop | Meaning in the corpus | Use when |
|---|---|---|
| `f/11` | Everything critically sharp front to back, focus-stacked. The default for studio still-life and macro. | Hero product on a surface; prop clusters that must all read; macro texture; suspended/liquid architecture. |
| `f/8` | Sharp hero + slight background falloff. | Multi-object lifestyle scenes, flat-lays, portraits where face and product must both be sharp, worn products in daylight. |
| `f/5.6` | Moderate separation. | Portrait with a product in hand; scene has depth you want softened. |
| `f/4` | Hand + product sharp, secondary props soft. | Dark editorial desk scenes, single-hand hero. |
| `f/2.8` | Environment falls away entirely. | Extreme close-up fashion; product dominant against a blurred world. |
| `f/1.8` | Creamy circular bokeh. | Nature / forest placements; foreground framing elements out of focus. |

Companions: `ISO 50` with Phase One and Hasselblad; `ISO 100` with generic/full-frame; `1/160 sec` when a
shutter is stated; `focus stacking` / `focus stacked` whenever f/11 is used.

## Capture-technique tokens (append after the aperture)

`focus stacking` · `focus-stacked capture` · `cross-polarized professional studio lighting` ·
`cross-polarized optics for controlled reflections` · `16-bit colour depth` · `HDR imaging` /
`HDR capture` · `ultra-high dynamic range` · `maximum dynamic range` · `high-speed liquid capture` ·
`museum-grade colour accuracy` · `ultra-high micro-contrast` · `exceptional micro-detail` ·
`razor-sharp texture reproduction` · `flawless commercial retouching` / `museum-quality commercial
retouching` / `luxury commercial retouching` · `native 8K ultra-high-resolution output` /
`8K ultra high resolution` / `8K commercial masterpiece`

---

## Lighting rigs (name the rig, not just the mood)

| Rig | Full phrasing | Look |
|---|---|---|
| Large diffused key, camera-left | `soft diffused daylight-style studio lighting from camera-left with gentle shadow falloff, realistic contact shadows beneath every object` | Editorial still-life default. |
| High front-left softbox + rim + bounce | `one large diffused softbox positioned high front-left creating soft illumination, a subtle warm rim light from camera-right to define metallic edges, gentle bounce fill from below to retain shadow detail, controlled specular highlights across polished surfaces` | Luxury hard-goods hero. |
| Large overhead softbox + front fill | `a large diffused overhead softbox combined with subtle front fill lighting and gentle rim lights` | Symmetrical packshot, floating/levitation setups. |
| Beauty softboxes, front and slightly above | `large diffused softboxes from the front and slightly above, producing smooth skin tones, gentle shadows, catchlights in the eyes, subtle facial contouring` | Beauty portrait. |
| High-key even | `soft high-key commercial studio lighting with even illumination, natural skin tones, subtle facial shadows, clean catchlights, gentle contrast` | White-seamless lifestyle portrait. |
| Overhead spotlight pool | `one strong overhead spotlight creating a circular pool of light beneath the objects, soft directional fill, deep but controlled shadows, subtle falloff toward frame edges` | Product-in-set, gear campaigns. |
| Strong rear key (backlit) | `strong rear key light creating a luminous halo around the model, subtle rim lighting outlining the silhouette, low-key shadows, diffused atmospheric haze, soft fog-like bloom` | Sportswear editorial. |
| Golden-hour backlight | `strong golden-hour backlighting originating from behind and slightly below the product, producing a radiant halo effect around the silhouette; warm sunlight wraps naturally around edges while the front remains visible through reflected fill bouncing from the terrain` | Outdoor hero object. |
| Hard directional sun | `strong natural golden-hour sunlight from camera-right, producing sculpted highlights, crisp shadows, dimensional contrast` | Athletic lifestyle. |
| Bright overcast | `soft daylight conditions with bright overcast coastal sunlight, subtle atmospheric haze, low-contrast shadows, gentle highlight rolloff` | Outdoor lifestyle, muted. |
| Direct on-camera flash | `direct-flash editorial aesthetic with strong on-camera flash illumination, crisp highlights, deep shadows, slight falloff into the background, high contrast, subtle film-like grain` | Street/candid fashion. |
| Natural window + bounce | `professional natural window lighting with subtle bounce fill, warm highlights across the tabletop, subtle ambient bounce, smooth highlight roll-off` | Café / interior lifestyle. |
| Single beam + vignette | `one strong collimated beam entering from the upper left, carving a bright pool across the subject while the field falls away into a soft natural vignette toward the corners, soft ambient fill lifting the shadow interiors, deep but controlled shadows, subtle falloff toward frame edges` | Theatrical single-source. Works on a light field (vignette to warm grey) or a dark one (vignette to near-black). |
| Overhead spot pool | `one strong overhead spotlight creating a circular pool of light beneath the subject, soft directional fill, deep but controlled shadows, realistic contact shadows under every object, subtle falloff toward frame edges` | Product-in-set, gear campaigns. Attested North Face 07. |
| Raking side light | `a hard low side light raking across the surface almost parallel to it, revealing every ridge, pit and relief in cross-lit detail, with the unlit flanks dropping into open shadow and a soft bounce returning just enough detail` | Texture and wear stories — tread, grain, machining, stitching. |
| Beam-through-frame | `soft diffused key from the front-left, gentle fill, and a strong diagonal beam of warm sunlight entering from the upper right corner, crossing through the subject` | Cinematic beauty. |
| Backlit water | `strong backlighting shining through the water, brilliant specular highlights, sparkling reflections, translucent liquid detail, subtle rim lighting around the product` | Splash/frozen-liquid hero. |

---

## Background + palette pairs

| Key | Background phrasing | Palette words |
|---|---|---|
| High-key white | `seamless pure white background with a subtle warm grey gradient falloff` | white, cream, warm grey |
| High-key ivory | `seamless warm ivory-beige studio backdrop with matching surface creating a soft monochromatic environment` | ivory, beige, cream, silver, soft brown |
| Warm off-white | `clean warm off-white seamless studio backdrop` | off-white, warm neutral |
| Cool grey gradient | `seamless cool grey-to-light-grey gradient background with subtle studio falloff` | cool grey, silver, white |
| Silver→charcoal | `seamless cool silver-to-charcoal gradient background` | silver, charcoal, cool neutral |
| Mocha monochrome | `seamless monochromatic warm mocha-brown studio environment with matching tabletop and backdrop` | mocha, cocoa, cream |
| Chocolate brown | `warm chocolate-brown seamless studio backdrop with subtle texture and soft tonal gradients` | warm brown, cream, beige, charcoal, muted grey |
| Charcoal-grey set | `seamless charcoal-grey backdrop fading subtly darker toward the top, smooth light-grey floor surface` | muted, premium, cool-neutral |
| Matte black | `clean matte black seamless studio background with no distractions` | black, chrome, silver, white + one accent |
| Dramatic black | `dramatic black studio background with subtle falloff` | black, glass, high contrast |
| Blue descent | `smooth gradient transitioning from deep navy blue at the top into soft cobalt blue at the centre and fading into pure white toward the bottom` | navy, cobalt, white |
| Icy backlit | `cool icy blue-white gradient background, diffused atmospheric haze` | icy blue, white |
| Lavender→pearl | `luxury beauty gradient transitioning from cool lavender-blue on the left to soft pearl-lilac and pale silver on the right` | lavender, lilac, pearl, silver |
| Poolside aqua | `luminous aqua-blue to pale-cyan gradient reminiscent of a luxury poolside environment` | aqua, cyan, white |
| Golden sky | `vast glowing sunset sky transitioning from bright luminous golden light near the horizon into deeper amber and burnt-orange tones higher in the frame` | gold, amber, burnt orange |
| Alpine blue | `expansive deep blue sky transitioning into a lighter blue gradient near the horizon` | deep blue, white, cool |
| Storm evening | `dark moody evening sky with textured storm clouds` | slate, deep grey, high-contrast flash |
| Forest bokeh | `softly blurred forest with warm sunlight filtering through tall trees, producing creamy circular bokeh and subtle atmospheric haze` | green, earthy brown, muted highlight |
| Blue cinematic | `smooth blue gradient background fading into darker tones around the edges` | cool blue, black, specular white |

---

## Shadow side — writing the part the light does not reach

A rig only describes where light comes from. The corpus always also states what happens where it does
*not*, and skipping this is what makes an image read flat. Pick the clause that matches the intent:

**Not attested — use with care.** Unlike the tables above, these clauses are the skill's own: `open shadow` and
`crushed blacks` appear in 0 of the 97 corpus prompts. The first row, paired with soft light, `HDR capture` and
`protected highlights`, flattened a whole Codex deck to a mid-grey shadow floor (2nd-percentile luminance 81
against adgod's 17, 2026-09-13). Default to matching the reference plate's black point and let the deepest
shadows go near-black; reserve the open-shadow row for flat-lay and high-key frames whose plate actually shows it.

| Intent | Clause |
|---|---|
| Open shadow, full detail | `the unlit surfaces fall into open shadow that retains full material detail, with no crushed blacks anywhere in the frame` |
| Sculpted, dramatic | `deep sculpted shadows across the unlit faces, controlled and rich rather than empty, with a soft bounce returning just enough detail to read the material` |
| Near-silhouette | `the near surfaces fall away into deep shadow approaching silhouette while a thin rim keeps the contour legible` |
| Falloff across the frame | `illumination falls off smoothly toward the frame edges into a soft natural vignette, darkening the corners without hardening into a visible ring` |
| Occlusion in recesses | `recesses, grooves and undercuts fill with accurate ambient occlusion, darkest where surfaces meet and opening gradually toward the light` |
| Cast-shadow character | `casting one long hard-edged shadow that softens very slightly with distance from the subject exactly as a real cast shadow would` |

Two rules the corpus never breaks: name the **direction** the falloff runs, and say whether the darkest
areas **retain detail or not**. "Dramatic shadows" alone produces mud.

## Aspect-ratio phrasing

`vertical 4:5 composition` · `vertical editorial format` · `portrait orientation` ·
`magazine-cover composition` · `perfectly centered front-facing vertical portrait`

State one whenever the deliverable has a placement (feed post, story, print). Otherwise omit.
