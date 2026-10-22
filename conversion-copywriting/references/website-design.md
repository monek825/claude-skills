# Website decisions that support conversion

Read for page planning, design, and audits. Design quality, task success, credibility judgments, and commercial conversion are different outcomes. This guidance combines standards, observed usability patterns and practical defaults; it does not establish a universal winning layout.

## Diagnose the journey

Identify traffic intent → relevant page → offer understanding → evidence/fit → primary action → completed outcome → downstream quality. Locate the weak step using the available evidence. A button-click event measures interest in a step, not a qualified lead. Confirm that links, forms, confirmations and delivery work before polishing visual details.

Use visitor questions to choose sections and order. Avoid adding sections simply to fill a template. One primary action can have repeated placements; secondary exploration is useful when visitors need it. Keep navigation for multi-purpose homepages and research-heavy buying journeys. A dedicated campaign page can reduce distractions without removing essential trust, costs or policies.

| Page job | Information that usually matters |
|---|---|
| Service enquiry | Clear service/fit, actual work, scope, process, price or pricing factors, contact and next-step expectations. |
| SaaS evaluation | Workflow demonstration, capability/plan limits, integrations, implementation, support, and security evidence when relevant. |
| Ecommerce purchase | Product/variant facts, availability, total cost, delivery, returns, reviews, and an understandable checkout. |
| Editorial/information | Direct answer, author/date/source, descriptive headings, context and useful onward links. |

These are decision needs, not mandatory sections. Preserve the project scope; an ecommerce example does not authorize adding checkout to a showcase site.

## Paragraphs, bullets, tables and headings

- Use focused paragraphs for connected explanation, reasoning, narrative and nuance.
- Use bullets for parallel inclusions, requirements, benefits or facts that can be scanned independently.
- Use numbered steps for a sequence and tables for meaningful comparisons.
- Make headings descriptive enough to predict the content. Put important words early.
- Keep prose readable on narrow screens. Do not force a universal sentence count or bullet ratio.

Eye-tracking patterns describe behavior influenced by task and formatting. An F-pattern is not a template to reproduce; useful headings can support more selective scanning. [NN/g scanning research](https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/).

## Why a person might click

The label, nearby context and visible destination should make the next step useful and predictable. Explain what the action offers, what it requires and what happens afterward. Match the ad's promise with the destination. Avoid clever labels that hide the task. [NN/g information scent](https://www.nngroup.com/articles/information-scent/).

Place relevant proof near the claim or decision it supports: actual work, sourced results with limits, attributable reviews, understandable conditions and real contact details. Do not replace evidence with decorative badges. An opening view should establish relevance and orient the reader; visitors can scroll when there is a useful reason. [NN/g trust](https://www.nngroup.com/articles/trustworthy-design/); [scrolling research](https://www.nngroup.com/articles/scrolling-and-attention/).

## Visual quality and typography

Follow the user's chosen references and brand. Use consistent alignment, meaningful grouping, a deliberate hierarchy and spacing that keeps related information together. A grid can support editorial or asymmetrical composition; it need not produce repeated card rows. Premium appearance is a design judgment, not a measured conversion score.

No font family is a universal winner. Choose legible forms, language coverage, license, appropriate tone and good rendering; assess actual copy on target devices. Practical starting defaults for marketing prose: roughly 16–18px effective body text, unitless line-height around 1.5, and a bounded reading measure around 60–70 characters on wider screens. Adapt for typeface, audience and content. These are defaults, not WCAG mandates or conversion evidence. USWDS recommends at least 16px effective size for most body text and a 66-character long-text target within a wider range. [USWDS typography](https://designsystem.digital.gov/components/typography/).

Use a small set of consistent type roles; avoid centered long prose in left-to-right languages, overly faint text and excessive all caps. Limit font files/weights, use a reliable fallback and deliberate font-display behavior. Do not add a font service or component library when existing assets suffice.

Choose images that explain the product, demonstrate the process, show real work, or support a coherent visual direction. Preserve their relationship with the copy. Serve responsive files, reserve dimensions, and avoid lazy-loading the primary LCP image. Decorative images need empty alternative text; meaningful images need alternatives appropriate to their purpose. [web.dev image performance](https://web.dev/learn/performance/image-performance/).

Use motion only when it earns attention for a meaningful purpose and fits project rules. Retain usable static/reduced-motion behavior. Reading, actions and focus should not depend on elaborate animation.

## Forms and interaction

Ask for information needed to complete the next useful action. Keep fields that genuinely improve qualification or are operationally required; defer the rest when possible. Explain unusual requests. Use persistent associated labels, suitable input types/autofill, useful errors, preserved input, and a clear confirmation. Placeholders alone are not labels. [W3C form labels](https://www.w3.org/WAI/tutorials/forms/labels/).

For ecommerce, show fulfillment costs and conditions before commitment and support appropriate checkout paths. Baymard's qualitative/benchmark research identifies friction; its modeled improvement estimates are not randomized lifts to promise. [Baymard checkout research](https://baymard.com/research/checkout-usability).

## Access and performance checks

WCAG 2.2 AA examples, not a complete conformance checklist:

- Normal text contrast at least 4.5:1; qualifying large text 3:1, with criterion exceptions.
- Keyboard-operable controls with visible focus; meaningful labels and errors.
- Text resizes to 200% without loss; ordinary content reflows at 320 CSS pixels, subject to inherently two-dimensional content exceptions.
- Pointer targets at least 24×24 CSS pixels or sufficient spacing/other permitted exceptions. A comfortable 44px target is a practical touch default, not the AA minimum or Apple points converted into web pixels.
- Support user text-spacing overrides without loss. Respect reduced-motion preferences; the specific interaction-animation criterion is AAA.

Use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and relevant Understanding documents for exact conditions. Do not claim a full accessibility audit from checking these few items.

Current good Core Web Vitals targets: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1, at the 75th percentile of real-user observations, checking mobile and desktop. Lab tests help diagnose; they do not prove field results or conversion. [web.dev Vitals](https://web.dev/articles/vitals).

Fresh visual checks should include narrow and wide layouts, longer content, zoom, relevant menu/form states and the complete primary journey. Use actual target-device data where available. Fix broken actions and inaccessible content before testing minor aesthetic differences.

## Theory sources and limits

- [Krug's author page](https://sensible.com/dont-make-me-think/): clarity and task-oriented usability; only publicly available sample material reviewed for the research.
- [Norman's publisher](https://mitpress.mit.edu/9780262525671/the-design-of-everyday-things/): signifiers, feedback and error recovery; publisher coverage, not full-book reading.
- [Lupton's author page](https://ellenlupton.com/Thinking-with-Type): typography scope; book not read in full.
- [Johnson's authorized sample](https://www.uxmatters.com/mt/archives/2010/04/designing-with-the-mind-in-mind.php): visual structure/cognition; partial book coverage.
- [Stanford credibility guidance](https://credibility.stanford.edu/guidelines/): perceived credibility is not measured purchase lift.

These sources inform design decisions. They do not justify promising that a beautiful site will generate a specified commercial result.
