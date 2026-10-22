# Plate pipeline — building your own references instead of hunting for one

Decoded 2026-09-18 from the AI BY CAMILA × R0 STUDIO garment study template (CR0-30), archived at
`~/Documents/adgod-prompts/refs/r0-studio/garment-study-template/`. It is a pipeline document, not a prompt
carousel: it publishes the whole node graph behind a commercial garment film.

Why it matters here: every adgod prompt inherits its realism from an attached photograph (P1), and rebuild
removed that photograph. This deck shows the third option — **generate the plate you need, then attach it.**

## The architecture

Three stills feed the final node. Each one has exactly one job and the prompt names which.

| Slot | Carries | Never carries |
|---|---|---|
| `@Image1` product / garment | colour, structure, hardware, artwork — **product truth** | light, mood, scene |
| `@Image2` style plate | the raking light, the focus band, the grain, the palette | **its content or composition** |
| `@Image3` worn plate | face, hair, proportions, and **the fit** | the product's own detail |

The deck states the order of authority in the prompt itself, and the wiring order into the reference port
*is* the slot number. That is the part worth copying: our Mode B/C says "style plate + product plate" but
never says which one wins on a given attribute. This does, attribute by attribute.

## The four rules that are not obvious

**1. Build the character sheet deliberately WITHOUT the hero.**
> *"Front and back on plain grey, in the jeans, the heels and a plain white tank — and deliberately without
> the garment. The garment is the hero the film introduces; a sheet that already wears it will put a second
> one in the frame."*

A reference that already contains the product teaches the model the product is furniture, and you get two of
them. The character sheet establishes the person; the worn plate introduces the object.

**2. One object, in one state, said explicitly.**
> *"THERE IS EXACTLY ONE SWEATER IN THIS FILM. @Image1 shows it off the body as product truth; @Image3 shows
> that same single garment worn. It is one physical object throughout and never appears twice in one frame."*

**3. The reference cannot be invented from.**
> *"Every feature the film will visit — a cuff button, a drawcord, a chest lockup — must be visible in this
> picture, because the film cannot invent what it cannot see."*

So the plate's own quality bar is set by the *shot list*, not by taste. Before writing, list the details the
work will visit, then check each one is legible in the reference.

**4. Approve each plate against the one above it before anything downstream runs.**
The deck carries a `Verify:` triplet under every prompt — face, garment, frame — each naming the failure, not
the success: *"A narrower, thinner-faced or lighter-eyed woman is a different person."* Writing the failure
into the plate prompt itself is a trick worth stealing; it appears inside the prompt text as
`… is a different person and a failed sheet.`

## Reference quality, as specified

| Reference | Requirement |
|---|---|
| Faces | two close-up sheets: front, three-quarter, profile, **same light** |
| Product photo | the retailer's flat shot at full size, front view, one object, nothing else in frame |
| Worn plate | full length, square to camera, plain grey, no floor line, no shadow, hands visible |

And a preparation rule we did not have: **"Crop every product picture to one object and pad it back to a
normal aspect ratio before you load it."**

## Third-party confirmation on rendered type

> *"Large simple type — a block wordmark, a big outlined word — renders correctly even at a quarter of a
> second. Small script and fine serif do not, at any angle or duration. Where your garment carries small type,
> treat it as texture and put the real lockup on an end card in your edit."*

This is an independent source arriving at the same split we predicted for the OLAPLEX label: the wordmark
survives, the small mixed-case line is the casualty. The workaround — treat small type as texture and place
the real lockup elsewhere — is worth having for stills too: shoot the macro on the wordmark, not on the
volume line.

## What this gives the held-product problem

`size-lock.md` records the unsolved case: a product held to a face renders 15–65% too large, and neither a
comparison (`about half as tall as her face`) nor a landmark span (`from cheekbone to jawline`) fixed it.
The decode there concluded it is a P1 problem — it needs a carrier, not better adjectives — and named the
next test as a real photograph of a hand holding a similar object.

This pipeline supplies the missing step: **you do not have to find that photograph, you can build it.**
By direct analogy to the worn plate:

1. **Character sheet** — the model, plain grey, full length, hands empty, **no product**.
2. **Held plate** — the same person holding a *familiar* object of known size at the same contact point the
   final frame needs (the FASHIONNN boundary condition in `size-lock.md`: familiar objects render at
   plausible scale without any stated size). Approve it against real hand geometry.
3. **Final frame** — attach the held plate as the fit-and-scale authority and the product photo as product
   truth, and state the order of authority: *hand position, grip and the object's size relative to the hand
   come from @Image3; the object's own colour, shape and printing come from @Image1.*

The bet is that scale transfers from the plate the way fit does. **Untested.** It is the cleanest candidate
we have and it is the next thing to run after the aliveness work.

Risk to watch: rule 1 above. If the held plate already contains the real product, expect two of them in the
final frame — so the held plate should hold the *stand-in*, and the swap happens in the final node.

## Not copied

The 23-shot burst, the quarter-second rhythm, the walk-and-turn ending and the Seedance node setup are video
craft and belong to that deck. The slot architecture, the four rules, the reference quality bar and the
type finding are general.
