#!/usr/bin/env python3.13
"""Measure the photographic look of a reference image (and optionally a generated one).

Usage:
  python3.13 measure.py REF.jpg                 # look card + prompt phrases for the reference
  python3.13 measure.py REF.jpg GEN.png         # side-by-side + what to change in the prompt

Every number is measured on a copy resized to 1024px on the long side, so sharpness
and grain compare across files of different resolution.
"""
import sys
import numpy as np
from PIL import Image

LONG_SIDE = 1024


def load(path):
    im = Image.open(path).convert("RGB")
    s = LONG_SIDE / max(im.size)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    return np.asarray(im).astype(np.float32)


def laplacian(g):
    return (-4 * g[1:-1, 1:-1] + g[:-2, 1:-1] + g[2:, 1:-1] + g[1:-1, :-2] + g[1:-1, 2:])


def box3(g):
    p = np.pad(g, 1, mode="edge")
    return sum(p[y:y + g.shape[0], x:x + g.shape[1]] for y in range(3) for x in range(3)) / 9


def measure(path):
    rgb = load(path)
    r, gch, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    lum = 0.2126 * r + 0.7152 * gch + 0.0722 * b
    mx, mn = rgb.max(-1), rgb.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0)
    lap = laplacian(lum)
    # grain: high-frequency residual measured only in flat areas (sky, backdrop),
    # so edges and texture don't count as noise
    resid = lum - box3(lum)
    local_var = box3(lum ** 2) - box3(lum) ** 2
    flat = local_var < np.percentile(local_var, 30)
    return {
        "mean_lum": lum.mean(),
        "contrast": lum.std(),
        "black_pt": np.percentile(lum, 1),
        "white_pt": np.percentile(lum, 99),
        "blown_pct": (lum > 250).mean() * 100,
        "crushed_pct": (lum < 8).mean() * 100,
        "saturation": sat.mean() * 100,
        "warmth": (r - b).mean(),          # + warm / - cool
        "tint": (gch - (r + b) / 2).mean(),  # + green / - magenta
        "sharpness": lap.var(),
        "edge_p99": np.percentile(np.abs(lap), 99),
        "grain": resid[flat].std(),
    }


def words(m):
    out = []
    L = m["mean_lum"]
    out.append("bright, airy exposure" if L > 165 else "slightly dim, underexposed feel" if L < 110 else "normal mid exposure")
    c = m["contrast"]
    out.append("very flat, low-contrast tonality" if c < 38 else "punchy high contrast" if c > 65 else "moderate contrast")
    out.append("lifted, milky blacks (nothing truly black)" if m["black_pt"] > 40 else
               "deep true blacks" if m["black_pt"] < 12 else "slightly lifted shadows")
    out.append("highlights soft and unclipped" if m["blown_pct"] < 0.3 else
               f"some clipped highlights ({m['blown_pct']:.1f}% blown)")
    s = m["saturation"]
    out.append("muted, washed-out colour" if s < 28 else "saturated colour" if s > 50 else "natural colour saturation")
    w = m["warmth"]
    out.append("warm golden cast" if w > 15 else "cool blue cast" if w < -15 else "neutral white balance")
    sh = m["sharpness"]
    out.append("soft, slightly out-of-focus, not crisp" if sh < 60 else "very crisp, sharp detail" if sh > 300 else "moderately sharp")
    gr = m["grain"]
    out.append("heavy visible grain/noise" if gr > 2.2 else "fine visible grain" if gr > 1.2 else "clean, almost no grain")
    return out


def fmt(m):
    return "  ".join(f"{k}={v:.1f}" for k, v in m.items())


DELTA_RULES = [
    # key, ratio/diff threshold, if gen too high, if gen too low, mode
    ("sharpness", 1.25, "image too crisp: add 'soft focus, slightly blurry, low micro-contrast, no crisp detail'; delete 8K/HDR/retouching/ultra-detailed", "image too soft: add 'in focus, clear detail'", "ratio"),
    ("contrast", 1.25, "too contrasty: add 'flat low-contrast tonality, lifted shadows'", "too flat: add 'more contrast, deeper shadows'", "ratio"),
    ("saturation", 1.25, "too saturated: add 'muted washed-out colour, desaturated'", "too muted: add 'richer colour'", "ratio"),
    ("grain", 1.5, "too much grain: add 'cleaner image'", "missing grain: add 'visible film grain / phone sensor noise across the whole frame'", "ratio"),
    ("mean_lum", 15, "too bright: add 'darker, slightly underexposed'", "too dark: add 'brighter exposure'", "diff"),
    ("black_pt", 15, "blacks too lifted: add 'deeper shadows'", "blacks too deep: add 'milky lifted blacks, faded shadows'", "diff"),
    ("warmth", 10, "too warm: add 'cooler, neutral white balance'", "too cool: add 'warmer white balance'", "diff"),
    ("edge_p99", 1.2, "edges too hard (reads as 'too intense'): add 'low micro-contrast, soft edges, gentle light'", "", "ratio"),
    ("blown_pct", 1.0, "too many blown highlights: add 'no hard specular stars, soft highlights'", "", "diff"),
]


def compare(ref, gen):
    print("\nGEN vs REF (what to change in the prompt):")
    hit = False
    for key, th, hi, lo, mode in DELTA_RULES:
        a, b = ref[key], gen[key]
        if key == "grain" and max(a, b) < 0.8:
            continue  # both effectively grain-free; ratio of two near-zeros is noise
        if mode == "ratio":
            r = (b + 1e-6) / (a + 1e-6)
            bad_hi, bad_lo, shown = r > th, r < 1 / th, f"x{r:.2f}"
        else:
            d = b - a
            bad_hi, bad_lo, shown = d > th, d < -th, f"{d:+.1f}"
        if bad_hi or (bad_lo and lo):
            hit = True
            print(f"  {key:11s} ref {a:7.1f}  gen {b:7.1f}  ({shown})  -> {hi if bad_hi else lo}")
    if not hit:
        print("  within tolerance on every measure")


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    ref = measure(sys.argv[1])
    print(f"REF {sys.argv[1]}\n  {fmt(ref)}\n  look: " + "; ".join(words(ref)))
    if len(sys.argv) == 3:
        gen = measure(sys.argv[2])
        print(f"GEN {sys.argv[2]}\n  {fmt(gen)}\n  look: " + "; ".join(words(gen)))
        compare(ref, gen)


if __name__ == "__main__":
    main()
