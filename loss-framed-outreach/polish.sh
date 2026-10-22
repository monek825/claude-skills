#!/bin/bash
# Claude polish pass: reads Codex drafts JSON, writes polished JSON. Adds no facts.
# Usage: polish.sh drafts.json polished.json
set -euo pipefail
IN="$1"; OUT="$2"; DIR="$(cd "$(dirname "$0")" && pwd)"
[ -f "$IN" ] || { echo "missing $IN" >&2; exit 1; }

{ cat "$DIR/SKILL.md"; echo; echo "=== DRAFTS JSON ==="; cat "$IN"; } | claude -p "$(cat "$DIR/polish-prompt.md")" --model "${POLISH_MODEL:-sonnet}" --output-format text > "$OUT.raw" \
  || { echo "claude polish failed: $(head -c 300 "$OUT.raw")" >&2; rm -f "$OUT.raw"; exit 2; }

# strip accidental code fences, then require valid JSON with same length as input
python3 - "$IN" "$OUT.raw" "$OUT" <<'PY'
import json, sys, re
src, raw, out = sys.argv[1:4]
text = re.sub(r"^```(?:json)?\s*|\s*```\s*$", "", open(raw).read().strip())
data, orig = json.loads(text), json.load(open(src))
assert isinstance(data, list) and len(data) == len(orig), "polish returned wrong record count"
for a, b in zip(orig, data):
    for k in ("slug", "recipient", "subject"):
        assert a.get(k) == b.get(k), f"polish changed {k} for {a.get('slug')}"
json.dump(data, open(out, "w"), ensure_ascii=False, indent=1)
print(f"polished {len(data)} emails -> {out}")
PY
rm -f "$OUT.raw"
