# Content for search + AI citation

Use after `conversion-copywriting` has set the argument. This file adds the findability and quotability layer; it never overrides the no-fabrication rule.

## 1. Query map (do in the brief)

Per page: one primary intent + the sub-questions an AI would fan out to.

| Page | Primary query (how buyers phrase it) | Sub-questions to answer on-page |
|---|---|---|
| Home | "[service] [city]" / brand name | what is it, who for, where, price range, how to order |
| Service page | "[specific service] [city]" | cost, duration, process, what's included, vs alternatives |
| About | "[brand] siapa / review" | who runs it, since when, credentials, location |

Sources for phrasing: GSC queries (after launch), Google autocomplete + "People also ask", the client's WhatsApp/customer questions, competitor pages. Write in the language people search in (Indonesian for local buyers; check whether they mix English terms like "jasa", "custom", "freight").

One page per intent. Two pages chasing the same query = cannibalisation; merge them.

## 2. Title, meta, H1 formulas

- Title: `[Primary topic] [qualifier/city] — [differentiator] | [Brand]`, ≈50–60 chars. Front-load the topic.
- Meta description: answer + proof + next step, ≈140–160 chars. Google rewrites weak ones; AI engines read the page, not this, so it's for CTR.
- H1: the page's promise in plain words; may differ from title, same topic.
- H2/H3: phrase as the questions or tasks from the query map ("Berapa biaya …?", "How the process works").

## 3. Citable passages (the GEO layer)

AI engines retrieve **passages**, not pages. Make each section survive being lifted out alone:

- **Answer first.** First 1–2 sentences under a heading directly answer it (≈40–60 words), then detail. No "In today's fast-paced world".
- **Self-contained.** Name the subject instead of "we/it/this" at the start of a section ("Greenpact Society menanam …" not "Kami menanam …" when it opens a section).
- **Specific facts with a source or basis**: numbers, dates, prices, quantities, locations, named people with roles. GEO paper: statistics, quotations and citing sources were the top-performing edits. Only real facts from the client — missing → CONTENT-GAPS.md.
- **Quotes from real named people** (founder, chef, engineer) with their role — counts as both E-E-A-T and a GEO lift. Never invent.
- **Structure that parses**: comparison tables, numbered steps, short definition lists. Real `<table>`, `<ol>`, `<dl>` — not divs styled as tables.
- **Visible FAQ** answering real objections; 3–8 Qs, each answer standalone.
- **Definitions** for niche terms the first time they appear.
- No keyword stuffing (hurt in the GEO paper and is spam policy).

## 4. E-E-A-T on small business sites

Google's quality rater guidelines: Experience, Expertise, Authoritativeness, Trust — Trust most important. On-page evidence:
- Real About page: people, faces, history, location, registration/licence numbers if they exist.
- Contact: full address, phone/WhatsApp, hours, map embed — identical to Google Business Profile (NAP consistency).
- Real photos of work/products/premises, case examples with permission.
- Author/owner byline + date on articles.
- Clear policies where relevant (pricing terms, returns, privacy).

## 5. Pages worth having (by site type)

- Local service / F&B: home, one page per main service or menu category, location page per REAL branch (no fake city pages), about, contact, FAQ.
- B2B (logistics, SaaS like Iluvatrack): per-use-case/industry pages, pricing or "how pricing works", comparison vs alternatives (honest), case studies, docs/help.
- Nonprofit (Greenpact, yayasan): mission, programs (one page each), impact with sourced numbers, how to donate/volunteer, reports.
- A blog only if someone will actually write useful posts; an abandoned blog is worse than none.

## 6. Internal linking

- Every important page ≤3 clicks from home, linked in body copy with descriptive anchors ("biaya pengiriman ke Jakarta", not "klik di sini").
- Service pages link to related services + contact; articles link to the service they support.
- Breadcrumbs on anything deeper than one level (+ BreadcrumbList schema).

## 7. Refresh loop

Update the core pages when facts change (prices, hours, team), bump `dateModified` only on real edits, ping IndexNow. Re-check GSC queries monthly: add the sub-questions people actually search to the relevant page.
