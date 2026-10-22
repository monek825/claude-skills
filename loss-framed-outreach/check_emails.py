#!/usr/bin/env python3
"""Mechanical invariants for Breq outreach emails. Usage: check_emails.py emails.json"""
import json, re, sys

REQUIRED = ["konsep website", "https://breq-studio.vercel.app", "08127201648", "Bray | Breq Studio",
            "Saya Bray dari Breq Studio"]
BANNED = [r"%", r"\bRp\b", r"\bAI\b", r"\bSEO\b", r"\bsolusi\b", r"\boptimal\b", r"di era digital",
          r"meningkatkan konversi", r"\bjelek\b", r"\bkuno\b", r"tidak profesional"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
CHAIN = ["first_screen", "visitor_reads_it_as", "who_leaves", "where_they_go", "konsep_fix"]


def check(rec):
    body, errs = rec.get("body", ""), []
    errs += [f"missing '{r}'" for r in REQUIRED if r.lower() not in body.lower()]
    errs += [f"banned '{b}'" for b in BANNED if re.search(b, body, re.I)]
    if EMOJI.search(body):
        errs.append("emoji")
    main = body.split("Salam,")[0]
    words = len(main.split())
    if not 90 <= words <= 140:
        errs.append(f"{words} words before signature (want 90-140)")
    chain = rec.get("cost_chain") or {}
    if not chain.get("access_failed"):
        errs += [f"cost_chain.{k} empty" for k in CHAIN if not str(chain.get(k, "")).strip()]
    if chain.get("demo_matches_claim") is False:
        errs.append("demo_matches_claim=false: fix demo or drop the claim")
    return errs


def demo():
    good = {"body": "Halo Kak,\n\nSaya Bray dari Breq Studio, saya membuat website untuk bisnis.\n\n" + "kata " * 95
            + "konsep website\n\nSalam,\nBray | Breq Studio\nPortofolio: https://breq-studio.vercel.app\nWhatsApp: 08127201648",
            "cost_chain": {k: "x" for k in CHAIN}}
    assert check(good) == [], check(good)
    assert any("banned" in e for e in check({**good, "body": good["body"] + " 30% Rp"}))


if __name__ == "__main__":
    demo()
    recs = json.load(open(sys.argv[1]))
    bad = 0
    for r in recs:
        errs = check(r)
        bad += bool(errs)
        print(("FAIL " if errs else "PASS ") + str(r.get("slug")) + ("" if not errs else ": " + "; ".join(errs)))
    print(f"{len(recs) - bad}/{len(recs)} pass")
    sys.exit(1 if bad else 0)
