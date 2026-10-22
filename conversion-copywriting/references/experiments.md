# Conversion evidence and experiments

Read when interpreting results or proposing tests. Prioritize completed qualified outcomes and downstream value; use clicks, scroll depth, and form starts as diagnostic measures.

## Evidence classification

| Evidence | What it supports | Important limit |
|---|---|---|
| Valid concurrent randomized test | Causal estimate for the tested population, exposure and period. | Instrumentation, power, uncertainty and later effects still matter. |
| Before/after or vendor case | An observed association or reported implementation result. | Traffic, seasonality, bundled changes and reporting bias may explain it. |
| Usability observation/eye tracking | Friction, comprehension and navigation patterns. | Does not estimate purchase uplift. |
| Survey | What respondents reported. | Recall, sampling and intention differ from observed behavior. |
| Standard/design system | Access requirements or reusable conventions. | Does not prove commercial performance. |

For every study record source/date, population, change/control, allocation, sample/denominator, duration, outcome, absolute and relative effect, uncertainty, and caveats. Write “not disclosed” when missing. Do not silently call a percentage a percentage-point change.

## Useful published findings

- GOV.UK's 2016 randomized CTA experiments ran for two weeks on three pages; sample counts and baseline rates were not disclosed. Wording changes moved clicks in different directions depending on the task. The report found no change in continuation after a click. This supports testing expectation-setting, not prescribing one universal CTA. [Original report](https://insidegovuk.blog.gov.uk/2016/08/23/absolutely-fabulous-testing/).
- GOV.UK reported that replacing “Start now” with “Find contact details” increased DVLA contact-page button clicks by 30% on mobile and 14% on desktop. Public counts, duration and intervals were absent. Those are click uplifts, not sales or completed-service uplifts. [Original report](https://insidegovuk.blog.gov.uk/2017/11/14/using-ab-testing-to-measurably-improve-common-user-journeys/).
- A Google Paisabazaar case describes parallel equal-budget search campaigns for two weeks, query-based traffic splitting, consistent design/functionality, and a faster AMP page. It reports 10% more completed lead forms but omits sample and uncertainty. Treat this as a contextual speed hypothesis, not a forecast or a recommendation to adopt AMP. [Case PDF](https://www.thinkwithgoogle.com/_qs/documents/6687/TWGAPAC_Google_Experiments_Paisabazaar.pdf).
- A Convert/iProspect pricing case reports an A/B/C experiment with 22,000 visitors over four weeks. A low starting-price variant yielded a reported 15% increase in enquiry submissions; higher prices performed differently by category. Baseline/arm counts and downstream lead value were absent. Price transparency is a hypothesis to investigate, not proof that showing the lowest price maximizes value. [Vendor case](https://www.convert.com/case-studies/iprospect/).

Do not copy published percentages into client promises or compare unrelated headline lifts as if they were a common benchmark. Interpret the measurement named in the source.

## Plan a trustworthy test

1. **Define the hypothesis and metric.** State the decision friction, change, primary completed outcome, denominator, and qualification definition. Add appropriate guardrails such as lead quality, revenue per visitor, cancellations, errors and performance.
2. **Assess feasibility.** Record baseline, minimum worthwhile effect, eligible traffic, allocation, desired power and error tolerance. Estimate sample needs for the actual outcome. At low traffic, use task tests/interviews and larger consequential decisions rather than many tiny underpowered variants.
3. **Validate setup.** Use persistent assignment appropriate to the unit of randomization. Check both versions and logging, deduplicate events, and investigate unexpected allocation imbalance (sample-ratio mismatch) before trusting results. Avoid exposing the same user to both variants when that breaks the design.
4. **Agree on duration and stopping.** A fixed-horizon plan needs a sample target and a sensible calendar window. Do not stop on the first favorable ordinary p-value. Use a valid sequential method if adaptive stopping is required. Monitor serious harm/technical issues separately from declaring a winner.
5. **Analyze with uncertainty.** Report control and treatment counts/rates, percentage-point change, relative change, confidence/credible intervals or the method's uncertainty, and guardrails. Inconclusive does not mean equivalent. Account for multiple comparisons. Avoid subgroup winner claims based only on one significant and one nonsignificant result.
6. **Check durability and quality.** Examine predefined device/source segments, novelty and timing effects. Do not condition analysis on behavior caused by treatment. Give delayed commercial outcomes their follow-up window. Confirm results after an appropriate rollout.

[Microsoft SRM guidance](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/); [Microsoft during-experiment guidance](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/); [metric interpretation paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2020/08/2017-08-KDDMetricInterpretationPitfalls.pdf).

## Arithmetic and low-traffic reality

An illustrative change from 3.0% to 3.6% is +0.6 percentage points and +20% relative. It is not +20 percentage points. A standard equal-allocation, two-proportion normal-approximation calculation with two-sided 5% significance and 80% power needs roughly 13,900 observations per arm for that effect. This is an independently calculated illustration, not a observed study result or a guaranteed sample size for every design.

At 500 eligible new visitors per month, approximately 27,800 total visitors would take about 56 months. Repeat visitors, clustering, delayed events, missing data and multiple comparisons can change requirements. Avoid planning an impractical multi-year test; fix known barriers, observe users and collect evidence about major changes. Use a method appropriate to the experiment when calculating a real sample target. [Sample-size tool and assumptions](https://www.evanmiller.org/ab-testing/sample-size.html).
