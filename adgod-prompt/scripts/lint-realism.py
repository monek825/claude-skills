#!/usr/bin/env python3
"""Realism lint for adgod-style image prompts.

Flags prompt patterns measured to produce AI-looking renders. The taste rubric scores the idea and the
self-check scores compliance; neither sees realism, so an agent can grade an AI-looking deck 14/14.
This lint is objective and cannot be self-graded leniently.

Calibrated 2026-09-14:
  Codex VT PDRN deck, renders read as AI, rubric 12-14/14 ... every prompt hard-fails
  test prompts G1-G3, renders read as photographs .......... 0 hard fails
  references/corpus.md, adgod's 97 prompts ................... 0 hard fails, 11 warnings
  references/fashionnn-corpus.md, 14 prompts ................. 0 hard fails, 3 warnings

Usage:  python3 lint-realism.py DECK.md [MORE ...]   lints each ``` block, else the whole file
        python3 lint-realism.py --selftest
Exit status 1 when any hard fail is found.
"""
import re
import sys

HARD = {
    "strips the product's own printing ('no text' means no ADDED text)":
        r"remove all printed|unlettered|remove it completely|label copy",
    "locks the plate's reflections (plates are often renders; rebuild reflections from the scene)":
        r"reflection behavio",
    "reserves empty space for later copy":
        r"later typography|space for (copy|typography)",
}
WARN = {
    "counted decorative droplets — fine as a designed studio object (adgod Olaplex 01 stages two), a fail only when posing as incidental realism on a dry surface":
        r"\b(exactly \w+|three|five|six|seven|eight|nine|\d+) (small |round |clear |tiny )*(water )*(beads|droplets)\b",
    "HDR / open-shadow language (with soft light it flattens the shadow floor)":
        r"no crushed blacks|open shadow|HDR (capture|imaging)|protected highlights",
    "airbrushed skin (rewrite to visible pores and texture)":
        r"poreless|flawless skin|no visible texture",
}
MAX_NEGATIVES = 20  # no adgod corpus prompt exceeds this; the AI-looking deck ran 22-25


def lint(text):
    hard = [k for k, rx in HARD.items() if re.search(rx, text, re.I)]
    warn = [k for k, rx in WARN.items() if re.search(rx, text, re.I)]
    negatives = len(re.findall(r"\bno [a-z]", text, re.I))
    if negatives > MAX_NEGATIVES:
        # ponytail: warning, not hard fail — correlated with the AI-looking deck, no visual evidence it causes it
        warn.append(f"{negatives} 'no ...' negatives (no adgod prompt exceeds {MAX_NEGATIVES}); keep only what could plausibly appear")
    return hard, warn


def selftest():
    bad = ("Remove all printed words and preserve reflection behavior. HDR capture. Add exactly nine round "
           "water beads. Leave the upper-left 30% for later typography.")
    good = ("Preserve every printed letter. Rebuild every reflection from this scene. No HDR tone mapping, "
            "no marble-like water beads.")
    hard, warn = lint(bad)
    assert len(hard) == 3 and warn, (hard, warn)  # droplets moved to WARN 2026-09-18
    hard, warn = lint(good)
    assert not hard and not warn, (hard, warn)
    print("selftest ok")


def main(paths):
    failed = 0
    for path in paths:
        text = open(path, encoding="utf-8").read()
        blocks = re.findall(r"```[^\n]*\n(.*?)\n```", text, re.S) or [text]
        for i, block in enumerate(blocks, 1):
            hard, warn = lint(block)
            failed += bool(hard)
            status = "FAIL" if hard else "pass"
            print(f"{status}  {path} block {i}")
            for reason in hard:
                print(f"      hard: {reason}")
            for reason in warn:
                print(f"      warn: {reason}")
    print(f"\n{failed} block(s) with hard fails")
    return 1 if failed else 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    elif len(sys.argv) > 1:
        sys.exit(main(sys.argv[1:]))
    else:
        print(__doc__)
