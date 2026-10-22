# Web sourcing — finding references outside the library

**Status: experimental.** The library (`library.md`) is 420 hand-checked photographs and stays the first
stop. This page covers the case it cannot serve: a product category, genre or gesture the library has no
frame for. The known failure of this lane is that an agent left to "find a reference" returns something
plausible-looking and wrong — an AI-generated Pinterest image, a flat phone snapshot, a moodboard collage,
or a beautiful frame whose affordance is impossible for the product. Everything below exists to make that
failure loud instead of silent.

## Order of sourcing

1. **Library** — `find-refs.py --kind reference-photo`. Curated, kind-filtered, known-good.
2. **Web** — this page. Use when the library returns nothing above a score of ~4, or returns frames whose
   affordance cannot be restaged for the product.
3. **Memory** — describing a published campaign you recall. Last resort, and say so in the report.

Never skip to 3 because 2 is slower. Never skip to 2 because 1 felt like effort.

## Where to look, in trust order

| Rank | Source | Why |
|---|---|---|
| 1 | Brand newsroom / press kit / campaign microsite | The actual art-directed assets at full resolution, with credits. Highest signal, lowest noise. |
| 2 | The photographer's or studio's own portfolio site | Curated by the person who lit it. Usually names the client and the year. |
| 3 | Awards archives — D&AD, Cannes Lions, The One Show, LBB, Communication Arts | Judged work. Filterable by category and craft. |
| 4 | Editorial coverage — It's Nice That, Ad Age, Adweek, Creative Review, Design Week | Reliable captions and credits; images often downsized. |
| 5 | Behance, Dribbble | Real work mixed with spec and student pieces. Check the credits before trusting. |
| 6 | Pinterest, Tumblr, aggregator boards | Highest recall, highest slop. Untitled, uncredited, and increasingly AI-generated. Use only to *find* a frame, then trace it back to a source at rank 1–4 before transcribing. |

## Query construction

Search in the language of photography, not the language of the product. "Pocket watch advertisement" returns
catalogue packshots; **"object dangling from fingertips hard midday sun editorial"** returns the frame worth
transcribing. Compose queries from four axes and vary one at a time:

- **gesture** — dangling, lowered into, balanced on, half-buried in, held at chest, carried at knee height
- **light** — hard midday sun, raking window light, direct on-camera flash, overcast, single hard studio head
- **genre** — documentary street, French pharmacy, still-life classical, nightlife flash, scandi minimal
- **register** — editorial, campaign, product photography, art direction, 1970s advertising

Add `-ai -midjourney -aiart` where the engine supports it, and prefer searching a named source directly
("site:itsnicethat.com hard sun still life") over an open web search.

## The selection rubric — run it on every candidate before transcribing

**Hard rejects. Any one of these and the candidate is out; do not negotiate with it.**

- **AI tells** — warped or six-fingered hands, melted typography on packaging, text that is nearly-words,
  reflections that do not correspond to anything in frame, duplicated background objects, plastic skin with
  no pores, a shadow direction that contradicts the highlight, jewellery or straps that merge into skin.
- **Not a photograph** — a 3D render, a mockup template, an illustration, a CGI product visual.
- **Furniture, not a frame** — a moodboard, collage, contact sheet, carousel cover, or anything with more
  than one photograph in it.
- **Watermarked stock comp** — Getty/Shutterstock/Alamy overlays, or a visible agency grid.
- **Too small to read** — under roughly 800px on the short edge. You cannot transcribe a quadrant you cannot
  see. Open the full-resolution version or drop the candidate.
- **No lighting logic** — a flat on-phone snapshot with no nameable source, no falloff and no cast shadow.

**Positive tests. The candidate must pass at least four.**

1. One legible key light whose direction you can state in words.
2. A real cast shadow or contact shadow that proves the object sits in the scene.
3. Props that carry meaning — the product's own material, the benefit made physical, or the buyer as objects
   (the `ideation.md` heuristics). Decorative props are a fail, not a neutral.
4. A palette reducible to three or four compound colour words.
5. A place where the product plausibly goes, **with an affordance the product actually has**.
6. Negative space that could carry display type.

**If three consecutive candidates fail, the query is wrong, not the web.** Rewrite it along a different axis
— change the gesture or the light, not the product noun — and search again. Do not lower the bar to fill the
slot; a weak reference produces a weak frame that then has to be regenerated anyway.

## Affordance check comes before aesthetics

The most seductive failure is a genuinely beautiful photograph whose interaction the product cannot perform.
A backpack worn on the back is not a reference for a tote; a wristwatch on a wrist is not a reference for a
pocket watch. Ask before falling in love with a frame: *can this product be in that position without lying?*
If the answer is no, the frame can still supply the **light, palette, background and crop** — but the pose,
grip and contact physics get rewritten from the product's own affordance per `adaptation.md` §2, and the old
interaction gets negated explicitly in the negative list.

## Transcribe the same way as a library frame

Open the full-resolution image and describe it object by object, quadrant by quadrant, material by material,
with the lighting instrument and the palette named. Nothing abstract, no mood words. The transcription is the
deliverable of this step; the URL is not. An agent that pastes a link and writes "in the style of this" has
done none of the work.

## Record provenance

Every web-sourced frame carries three things into the deck, beside its prompt label:

```
02 — Into the pocket · in-hand · hard sun
    source: https://…  (photographer / client / year if known)
    rubric: passed 5/6 — no negative space for type, headline goes in the sky at top left
```

Say in the report which frames came from the library and which from the web. A campaign whose references
cannot be traced cannot be defended in a review.

## What this lane is bad at, stated plainly

- Judging aesthetic quality. The rubric catches broken and off-brief; it does not catch *boring*. A frame can
  pass all six tests and still be a stock photograph. Read it against the `ideation.md` heuristics before
  committing — especially heuristic 3, whether the genre carries the brand's positioning.
- Distinguishing recent AI work from photography. Detection is getting harder, not easier. Tracing an image
  back to a rank 1–3 source with a credited photographer is the only reliable defence.
- Dated material. An image from a decade ago may carry a colour grade or a styling register that now reads as
  old. Check the year where the source gives one.

## Copyright

Transcribing a photograph's composition in words and restaging it with a different product is what the corpus
does throughout, and composition is not itself protected. Do not reproduce a specific photograph closely
enough that the result is recognisably that image — a distinctive one-off frame is a bad reference for that
reason alone. Never present the source photograph as the client's own work, and never repost it.

## Tooling by host

- **Codex** — web search plus its browser. Search, open the page, view the image at full resolution, then
  transcribe.
- **Claude Code** — `WebSearch` and `WebFetch`, or the Browser pane (`preview_start` with a URL, then
  `navigate` / `get_page_text`). To transcribe, the image must be *seen*: download it and open it with Read,
  or view it in the browser pane. Transcribing from alt text or a caption is not transcription.
