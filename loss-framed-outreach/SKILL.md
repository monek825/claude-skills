---
name: loss-framed-outreach
description: Qualify Breq Studio outreach prospects and write plain Indonesian emails from dated website evidence, a plausible buyer consequence and a matching hero concept. Use for new lead emails, copy rewrites, selective Claude polish and warm sales replies. Keep observed facts separate from buying-intent and lost-sales hypotheses; do not invent metrics or authorize sending.
---

# Loss-framed outreach (Breq Studio)

Old emails said what a site **lacks** ("two paragraphs before Lihat Produk").
These emails say what it **costs** ("a buyer from Instagram sees text, not keripik, can't tell how to order, and the next keripik seller is one tap away").
Loss framing is a drafting hypothesis, not a proven response-rate advantage. Observations must be evidenced; visitor interpretations and departure are plausible risks, not established behaviour or lost sales. Never a made-up number.

Works alongside, does not replace: `outreach-2026-10/outreach-system/README.md` rules, `email-ops`, `conversion-copywriting`, `stop-slop`. Where they conflict, the README's truth/approval rules win.

## 0. Commercial qualification before a demo or email (8 Oct 2026)

For this workspace, read `outreach-2026-10/outreach-system/improvement-2026-10-08/QUALIFICATION-AND-SALES.md` before selecting leads or handling warm replies.

Record a published commercial purpose, a meaningful observed obstacle to that buying task, static scope fit, dated activity and a public business email. Deduplicate and check suppressions before outreach. Public email does not prove decision-maker authority or deliverability; budget/authority/timing stay unknown until confirmed. Assets are a separate design gate.

Use QUALIFY (all supported), RESEARCH (specific unresolved evidence), or PARK (no meaningful need/contact/scope fit or suppressed). Do not generate new outreach for RESEARCH/PARK simply to fill a quota. A directory listing, attractive pack or weak aesthetic alone is not a buying reason. A one-line contact repair alone is not a case for a paid rebuild. Preserve working checkout/marketplace/loyalty paths. This gate does not cancel existing schedules or change approval, daily volume or asset permissions.

## 1. Evidence first (per lead, dated)

Open the lead's page fresh. Do not reuse old notes as current state.

- Capture 375x812 (phone) first screen, and 1440 desktop. Save under `daily-review/<date>/research/<slug>/` as `cost-mobile-375.png`, `cost-desktop-1440.png`.
- Record in plain words: what is readable on the first phone screen without scrolling; is a product/service photo clearly visible; is the business's main thing named; is an order/contact action visible; how many scrolls/taps until product, price-or-catalog, WhatsApp/quote, reseller/grosir info.
- Note who the business sells to, from their own page: eceran (retail), reseller/grosir/agen, B2B/corporate shipper, distributor/export. Their own words ("open reseller", "terima grosir", "melayani perusahaan") decide this.
- Page type: **owned website** / **directory or marketplace listing** (KKI, Inaexport, Shopee, Tokopedia) / **no page found**.
- Access failed (403, cert error, timeout)? Record it. Make NO defect claim for that lead; keep its existing copy.

## 2. The cost chain (fill all five, in this order)

| # | Field | Rule |
|---|---|---|
| 1 | `first_screen` | Literal observation from the capture. Concrete nouns: "banner bertulisan kecil, lalu dua paragraf panjang". |
| 2 | `visitor_reads_it_as` | What a stranger can/can't answer in the first seconds: what is sold, why trust it, how to buy. Phrase as unanswered questions, never as an insult about the business. |
| 3 | `who_leaves` | Buyer tied to the published commercial purpose. Name reseller/grosir or corporate buyers only when supported. Departure and order value remain hypotheses; do not call them established high-value lost sales. |
| 4 | `where_they_go` | Only verifiable alternatives: back button to search/marketplace results, a directory page that shows other sellers' products next to theirs (verify it), competitors appearing in the same dated search (do NOT name competitors in the email). |
| 5 | `konsep_fix` | What the ATTACHED desktop/mobile PNG actually shows that removes 1-4. Open the PNGs and check. If the demo does not fix it, drop the claim or flag the demo `needs-revision`; never promise what the attachment doesn't show. |

### Cost patterns by page type

- **Owned site, product hidden below text** -> buyer can't tell what is sold/how to order -> leaves for marketplace/search results. Reseller can't find terms -> bulk order goes to a seller whose terms are visible.
- **Owned site, text baked into a banner image** -> on phones the text shrinks to unreadable -> service/product unknown -> shipper/buyer asks a competitor who states it plainly.
- **Contact friction** (number as plain text, wrong wa.me format, no visible action) -> extra steps between a ready buyer and a chat; some don't take them. State only what was tested: format observed, not "your number is dead".
- **Directory/marketplace only** -> the brand has no page of its own; buyers see it inside someone else's layout, often next to other sellers' products, with no space for the brand story or grosir terms. Never call the directory listing "your website is broken".
- **Logistics** -> a shipper needs in seconds: route/moda covered, cargo type, how to get a quote. Missing any one = the quote request goes to the next forwarder in the results.

## 3. Allowed vs banned claims

Allowed: dated observations; ordinary visitor behaviour stated softly-but-plainly ("orang yang buka dari HP biasanya langsung memutuskan lanjut atau kembali"); the business's own stated audience; verified side-by-side alternatives.

Banned: invented numbers (% lost, Rp lost, visitors), "bad SEO", "slow site" without a measured trace, "you are losing sales" as fact, unverified bestseller/premium claims, naming competitors, insults ("jelek", "kuno", "tidak profesional"), urgency tricks, prices, emojis, mentioning AI or tools, presenting the konsep as a finished site.
External research figures: do not use in emails (they read as sales pitch to UMKM owners and cannot be tied to this business).

## 4. Email shape (Indonesian, 90-140 words body)

```
Halo Kak, | Halo Bapak/Ibu,            (match existing salutation for the lead)

Saya Bray dari Breq Studio, saya membuat website untuk bisnis.

[first_screen - one or two sentences, with the absolute capture date, e.g. "pada 5 Oktober" + "di HP"; never "hari ini" - the email may send days later]

[visitor_reads_it_as + who_leaves + where_they_go - two or three sentences, the loss]

[konsep_fix - one or two sentences: "Konsep website terlampir ..." naming the concrete product/service shown]

Terlampir contoh tampilan untuk laptop dan HP.

[one easy question about a verified business purpose, not a design opinion; e.g. "Apakah pesanan kantor masih menjadi fokus <Brand>, Kak? Kalau ya, saya bisa jelaskan isi website dan biayanya secara singkat."]

Salam,
Bray | Breq Studio
Portofolio: https://breq-studio.vercel.app
WhatsApp: 08127201648
```

Invariants (checked by `check_emails.py`): contains "konsep website", the portfolio URL, the WhatsApp number, signature "Bray | Breq Studio"; no "%", "Rp", "AI", "SEO", emoji; body 90-140 words; client-focused vs agency-focused meaningful topics at least 2:1 (manual).
Subject: keep the existing subject for scheduled emails (changing it breaks nothing but keep it stable); new leads: `Konsep website <Brand>`.

Voice: plain spoken Indonesian, short sentences, one idea per sentence. Read it aloud as a WhatsApp voice note to an UMKM owner - if a phrase sounds like a brochure or a translated English deck, rewrite it. Avoid "solusi", "optimal", "meningkatkan konversi", "di era digital", "tingkatkan", "memaksimalkan".

## 5. Examples

**Morang Moreng (owned site) - before (lack only):**
> Di website Morang Moreng versi HP, dua paragraf panjang muncul sebelum tombol Lihat Produk. Calon pembeli harus melewati penjelasan itu dulu untuk melihat pilihan camilannya.

**After (cost chain):**
> Saya buka keripik-pedas.com di HP pada 5 Oktober. Layar pertama berisi banner dengan tulisan kecil, lalu dua paragraf panjang. Kemasan keripiknya belum terlihat jelas dan tombol Lihat Produk baru muncul setelah di-scroll.
>
> Orang yang datang dari Instagram atau Google biasanya langsung memutuskan mau lanjut atau kembali. Kalau yang terlihat hanya teks, mereka belum tahu keripik apa yang dijual dan cara pesannya. Calon reseller juga belum melihat cara daftar, padahal merekalah yang pesan dalam jumlah besar.
>
> Konsep website terlampir langsung menampilkan Keripik Cimol di layar pertama, dengan tombol pesan lewat WhatsApp yang terlihat tanpa scroll.

(The reseller sentence is allowed because the site itself says "open reseller". If the konsep has no reseller entry, either drop that sentence or flag the demo.)

**Directory listing (e.g. KKI) - cost angle:**
> Saat ini Sanrah Food tampil di halaman KKI. Di halaman itu, di bawah produk Sanrah juga muncul rekomendasi produk usaha lain. Pembeli yang sedang melihat Sanrah bisa langsung pindah ke produk lain sebelum menghubungi Kakak.

(Only if the listing really shows other businesses' products on the capture date.)

**Logistics (PT Aah) - cost angle:**
> Di HP, tulisan layanan ada di dalam gambar banner, jadi ikut mengecil dan sulit dibaca. Pengirim yang cuma ingin tahu "bisa kirim lewat laut atau udara?" tidak menemukan jawabannya sekilas, lalu kembali ke hasil pencarian dan bertanya ke forwarder lain.

## 6. Output record (per lead, extend the existing copy JSON)

Keep all existing fields (`slug, name, url, recipient, subject, body, attachments, proposed_send/scheduled_at, ...`). Also record `qualification` with tier, commercial-purpose source/date, buying-path gap/capture, scope fit, activity evidence/date, public contact source, unresolved checks, and budget/authority/timing (unknown unless confirmed). Qualification for prospecting is not confirmed willingness to buy. Add:

```json
"cost_chain": {
  "captured_at": "2026-10-05T14:00:00+07:00",
  "page_type": "owned|directory|none",
  "buyer_types": ["eceran","reseller"],
  "first_screen": "...",
  "visitor_reads_it_as": "...",
  "who_leaves": "...",
  "where_they_go": "...",
  "konsep_fix": "...",
  "demo_matches_claim": true,
  "evidence": ["research/<slug>/cost-mobile-375.png"]
},
"previous_body": "<the body this replaces>",
"draft_by": "codex",
"polished_by": "claude|skipped:<reason>"
```

## 7. Pipeline

1. Codex: evidence + cost chain + draft body (sections 1-4). Save `drafts.json`.
2. Selective Claude polish (7 Oct rule): only weak emails, at most five/day, in one `bash ~/.claude/skills/loss-framed-outreach/polish.sh weak.json weak-polished.json` call. Weak means failed checks, vague cost chain, unnatural brochure Indonesian or near-duplicate sentences. Merge returned bodies without new facts; mark actual Claude polish truthfully. On failure keep Codex copy, set `polished_by: "skipped:<exact reason>"`, do not retry. Otherwise mark `polished_by: "not-needed"`. A separately authorized strategic collaboration does not change this daily rule.
3. `python3 ~/.claude/skills/loss-framed-outreach/check_emails.py final.json` on the merged/final records - fix every FAIL.
4. Approval packet (old vs new side by side + capture + cost chain). Approval rules from the README still apply.

## 8. Follow-up (authorized by Bray, 6 Oct 2026)

Exactly ONE follow-up per lead, never a second.

- **Who:** leads whose first email was verified Sent 4+ days ago with no human reply, no bounce, no opt-out, and no out-of-office promising a later answer (wait until that date instead). Never follow up a bounced, replied or "tidak tertarik" lead.
- **How:** reply in the SAME Gmail thread (so the original konsep and images sit right below). No new attachments. Same subject (Gmail adds nothing; keep it).
- **Body:** 35-60 words, plain Indonesian, salutation matches the first email. One line reminding them of the konsep, one line restating the cost chain's buyer consequence in fresh words (no new claims), one easy question. Short signature `Bray | Breq Studio` + WhatsApp line. No price, no pressure, no "just following up", no guilt.
- **Example:**
  > Halo Kak, menyambung email saya tentang konsep website Morang Moreng. Pada pengecekan sebelumnya, kemasan dan cara pesan belum langsung terlihat di HP. Konsep terlampir menampilkan Keripik Cimol dan tombol WhatsApp lebih jelas. Apakah website untuk memperkenalkan produk sedang menjadi kebutuhan Morang Moreng, Kak?
  >
  > Bray | Breq Studio
  > WhatsApp: 08127201648
- **Volume:** follow-ups do not count toward the 10 new cold emails/day; separate cap 10 follow-ups/day; spread into the same 10/11/13/14/15 slots, at the same local time-of-day as the first email when possible.
- Follow-ups receive evidence/manual review and exact-text approval; only weak drafts enter the same capped selective polish call. Initial-email checker word limits do not apply; check manually 35-60 words.

## 9. Warm replies: one useful next step

Initial cold-email length, no-price restriction and cost-chain structure do not govern a requested warm quotation. Read the qualification/sales playbook's reply section.

- Answer the question asked. If they request price/an offer, give one recommended scope and an approved price with essential inclusions/exclusions; do not hide the answer behind a questionnaire.
- If purpose is unclear, ask one relevant question. Do not require a call for a simple written scope.
- Do not assume interest equals budget or authority; clarify timing/decision process naturally, not all in one message.
- No new discounts, deadlines, domain fees, care plans or payment terms without owner confirmation. Preserve quotes already made.
- A working marketplace is not an objection to overcome. Explore a separate verified need or accept the poor fit.
- Respect refusals; no second unsolicited follow-up. Warm replies still require exact human approval before sending. This skill authorizes no mailbox writes.
