# The reference library — 630 catalogued adgod images

**Read `signature.md` before this page.** This library is **not a scene menu**, and a re-audit on 2026-09-03
cut it down hard.

**126 of the original 420 "reference photographs" were adgod's own campaign output, mis-filed.** The detector
was structural, not visual: his Instagram carousels ship with furniture — a "COMMENT PROMPT" promo card, a
six-up contact sheet, a "prompts" poster. **Any folder carrying that furniture is one of his posts, and the
6–7 frames inside it are the deck, not its sources.** 87 were reclassified at high confidence (folder has a
poster or contact sheet), 39 at medium (promo card only). The Rolex folder alone held the moka-pot frame, the
goldfish, the art-book frame and three more — all previously offered as things to transcribe.

Two independent confirmations that the reclassified frames are generated, not photographed: the Rolex dial in
the moka-pot frame reads "REPERPETUAL", and the art-book frame OCRs to 281 tokens of nonsense where a real
Rizzoli book would give real words.

**294 reference-photos remain.** They carry no carousel furniture, which makes them *probably* scraped
sources rather than his output — but they are still frames **he chose**, so the warning stands: use them for
craft, and treat a strong match as a signal that he has already been there.

Location: `~/Documents/adgod-prompts/refs/adgod-ig/`

## Searching it

```bash
cd ~/Documents/adgod-prompts/refs/adgod-ig
python3 find-refs.py --kind reference-photo "product sharp while person blurred"
python3 find-refs.py --format in-hand --genre documentary-street
```

Text-first: it ranks descriptions and keywords, prints `format · genre · uuid/file · desc`. **Then open the
two or three files it names with Read** — the description gets you to the right frame, the image is what you
transcribe. Never transcribe from the description alone; the description has no jigger in the lower right.

`--kind reference-photo` is almost always right. Omitting `--kind` returns adgod's own outputs mixed in with
the sources, and transcribing his AI output as if it were a photograph compounds his errors into yours.

Verified retrieval — these queries return correct top hits: *"product buried in its own ingredient"* →
Pringles in a heap of crisps, Laneige sunk in cream, Kerrygold on churned butter. *"luxury object among cheap
everyday things"* → both Rolex domestic-clutter frames. *"held in hand against blue sky low angle"* → Owala
on a running track, Apsara ice cream.

## The four kinds — filter before you look

| kind | n | what it is |
|---|---|---|
| `reference-photo` | 420 | Real brand campaign / editorial photography. **The sources. The valuable set.** |
| `promo-overlay` | 87 | "COMMENT PROMPT" carousel cards. Junk, tagged `skip`. |
| `adgod-output` | 68 | His own AI frames, the "prompts" posters, two brand-kit sheets. |
| `grid-contact-sheet` | 55 | Six-up carousel covers. Useless as one reference, useful for reading a deck's *shape*. |

**Two traps in the raw folders.** 45 images (`694e52cf`, `fd71a65a`) are Instagram Stories from *matcha bae*,
a Jakarta cafe — nothing to do with adgod, tagged `skip`. And 15 records carry a **Higgsfield** watermark:
third-party AI demos, not adgod's work and not photographs. Both are flagged in the catalogue; both are
invisible if you filter on `kind` and visible if you browse the directory by hand. Filter.

## What the sources actually look like (n = 420)

This is the part that corrects the skill's own bias. `archetypes.md` opens with four studio hero families and
the worked example in `SKILL.md` is a mirror-plinth packshot. **The photographs adgod actually selects are
overwhelmingly hand-held and in-the-world.**

**format** (n=294, post-audit) — environment **81** · in-hand **74** · prop-tableau 34 · macro-texture 18 ·
flatlay 13 · in-motion 11 · pour-splash 11 · hero-packshot 10 · and the specialist buckets below that

In-hand and environment are **half the library**. Clean studio hero and mirror-plinth together are **21 of
420 — five per cent.** If a deck is drifting to plinths and seamless sweeps, it has drifted away from the
source material. The studio look is the *output* register for a launch frame, not where the ideas come from.

**genre** — studio-gradient 92 · documentary-street **83** · still-life-classical 56 · luxury-beauty-editorial
52 · vintage-nostalgia 27 · outdoor-expedition 27 · scandi-minimal 27 · spa-bathroom 22 · french-pharmacy 14 ·
nightlife-flash 10 · industrial-brutalist 9 · swiss-technical 1

Documentary-street being second is the surprise, and it pairs with in-hand: a real hand, real daylight, a real
pavement, the product held at arm's length. That combination is the single most common frame in the library.

**lighting** — soft-diffused **166** · hard-sun 59 · hard-directional 59 · mixed 46 · raking-side 24 ·
overhead-softbox 22 · backlit-halo 15 · direct-flash 13 · beam-vignette 9 · overcast-daylight 7

Soft-diffused is 40%, but note what sits second: **hard sun, 59** — undiffused daylight with a real cast
shadow. Nothing exotic. Most of these frames were lit by a window or by the sky.

**palette** — cool-grey 133 · warm-neutral 99 · saturated-colour 65 · high-key-white 45 · earth-tone 37 ·
dark-moody 30 · metallic-silver 9 · monochrome 2

**human presence** — no human **200 (48%)** · a hand or hands somewhere 66 · a face visible **32 (7.6%)**

This sharpens `ideation.md` heuristic 4. "Never a face" is right as a bias — under 8% — but "no people" is
wrong: **52% of the sources contain a body.** The body is almost always a hand, a forearm, a torso with the
face cropped, or a figure from behind. **The buyer appears as a hand, not a face.**

## The most-repeated props

sunglasses 13 · foam 13 · bubbles 10 · sea 8 · headphones 7 · water 7 · strawberries 6 · steam 6 ·
wooden board 5 · moka pot 5 · water droplets 5 · towel 5 · books 5 · condensation 5 · tiles 5 ·
newspaper 4 · fork 4 · blue sky 4 · striped shirt 4 · milk bottle 4 · wooden racquet 4 · body brush 4

Two families and nothing else: **evidence of use** (foam, bubbles, steam, condensation, droplets, a towel)
and **the buyer's own objects** (sunglasses, books, a newspaper, headphones, a racquet). No decorative props.
Every recurring object either proves the product was just used or dates and places the person using it.

## Brand-kit sheets — the fidelity-lock template

Two images in the library are not campaign frames at all but **identity spec sheets**, and they are the most
directly reusable artifacts in it:

- `aff2bb62/db9831652334080a.jpg` — **FUTER DEATH** protein soda. Blackletter logo, "FEED YOUR FUTURE"
  endline, a six-swatch hex palette named in compound words (Void Black, Blood Oxide, Morbid Burgundy, Bone
  White, Bio Gold), typography ladder, mood strip, photography-language panel, DO / DON'T list.
- `a9bc4d15/3bb75a4a69e0ed12.jpg` — **OAKLEY META BRAND KIT**. Numbered blocks: brand essence, product
  identity lock with callouts to the shield lens, top sensor, front camera and nose pads, key views, hex
  system, typography.

The identity lock is decided **once, in a sheet, before any prompt is written** — then every prompt in the
deck inherits the same enumerated attribute list verbatim. That is exactly the fidelity-lock block in
`anatomy.md`, hoisted up a level so it cannot drift between frames. For a multi-frame deck, or for any
automated system generating many prompts for one product, build this sheet first and quote from it.

Also: **14 catalogue records are wholly invented brands** — Futer Death, Daily Good and others get a name, an
endline, a palette and a full seven-frame campaign. adgod does not wait for a client to demonstrate a look.

## Regenerating / extending the catalogue

OCR was the unlock. adgod stamps his own carousel furniture with fixed copy ("COMMENT PROMPT", "WANT ART
DIRECTION FOR YOUR BRAND?", "NO CAMERA. NO REAL SHOOT. ONLY PROMPTS."), so the templated kinds identify
themselves in **text**. macOS Vision OCR over all 630 images takes ~50 seconds with zero dependencies and
auto-resolved 193 images at zero false positives. Colour-histogram and file-size heuristics were tried first
and failed — the distributions overlap almost completely.

```bash
swiftc -O -o bin/ocr bin/ocr.swift          # macOS Vision, no deps
cat paths.txt | xargs -n 25 -P 4 ./bin/ocr > OCR.jsonl
python3 catalogue.py stats                  # 630 / 630
```

`SCHEMA.md` holds the record shape and the controlled vocabulary. Add an enum value only when three images
genuinely need it.
