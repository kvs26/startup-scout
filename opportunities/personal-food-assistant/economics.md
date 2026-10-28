# Personal food assistant — costs and possible income

Assessed 2026-10-27. India consumer software scenario. All customer counts, usage, prices for our offer, acquisition costs and effort estimates below are hypothetical. No customer has paid. USD supplier costs are retained in USD; no currency conversion or exchange-rate claim is made.

## Inputs and basis

| Input | Value | Basis and limits |
| --- | --- | --- |
| Founder resources | About ₹5,000/month; usually 10–19 hours/week | [User-supplied profile](../../FOUNDER-PROFILE.md); current affordability, not business revenue |
| Proposed monthly price P | ₹149/customer, up to 20 decision sessions | Working test offer, not an accepted price; a session includes search, refinement and feedback, not one message |
| Alternative occasional-use offer | ₹49 for five sessions | Hypothesis only; would be a separate experiment, not a validated recommendation |
| Monthly customers N | 100 paying, 100 trial users | Scenario, not audience size or forecast |
| Usage u / trial allowance t | 20 sessions/payer; three/trial user | Hypothetical; trial-user total is 300 sessions |
| All-in serving cost s | ₹0.50 / ₹2 / ₹5 per session | Sensitivities, not vendor quotes; must eventually include models, retries, tools and any platform usage fees |
| Payment fraction f | (2% + 0.99%) × 1.18 = 3.5282% | [E030](research.md#e030), recurring card-like web-payment example; quote/method eligibility unconfirmed |
| Fixed operating allowance F | ₹1,000/month | Hypothetical aggregate allowance, not a hosting quote; includes no guaranteed specialist budget |
| New/replacement customers k; acquisition cost a | 20/month; ₹200 each | Hypothetical ₹4,000 cash acquisition spend; founder sales time is additional |
| Founder support | 10 min/paying user/month | Hypothetical; excludes development, recruitment and reviews |
| Model supplier example | $0.25 input / $1.50 output per million tokens | [E029](research.md#e029), Gemini 3.1 Flash-Lite standard, retrieved 2026-10-27; not selected or benchmarked |
| Hosting reference | Workers paid minimum $5/month | [E031](research.md#e031); component only, not additive to F unless separately budgeted |

## A grounded model-cost illustration

Across all model calls in one complete session, assume 12,000 input and 2,000 output tokens:

`model USD/session = 12,000 / 1,000,000 × 0.25 + 2,000 / 1,000,000 × 1.50 = $0.006`.

A longer 60,000-input / 6,000-output session costs `$0.024`. These token counts are assumptions, including any repeated context and thinking in the totals. At 2,000 sessions these examples are $12 or $48 for model text processing alone. They are not measured traces and cannot establish latency or acceptable quality.

For scale sensitivity, 2,000 sessions × four search-grounding queries = 8,000 queries; if the full shared 5,000 allowance were available, 3,000 billable queries at $14/1,000 add $42. Actual queries per prompt and shared allowance consumption vary. Web/maps grounding does not supply authorized current delivery inventory. Neither USD example is converted into the INR serving-cost scenarios below. Platform fees, external data, voice, image processing, taxes, foreign-exchange charges and failures could add costs.

## Monthly cash sensitivities

`Gross collections = N × P`.

`Contribution per payer = P × (1 − f) − u × s`.

`Operating cash balance = N × contribution − F − trial_users × t × s − k × a`.

At N=100, P=₹149, gross collections are ₹14,900. Payment fees are ₹525.70. Trial usage is additional to the 2,000 paid-user sessions.

| Serving cost/session | Contribution/payer before fixed costs and acquisition | Paid + trial serving cost | Balance after fixed allowance and acquisition |
| --- | ---: | ---: | ---: |
| ₹0.50 | ₹133.74 | ₹1,150 | ₹8,224.30 |
| ₹2 | ₹103.74 | ₹4,600 | ₹4,774.30 |
| ₹5 | ₹43.74 | ₹11,500 | −₹2,125.70 |

These balances exclude founder pay, tax on our sales, refunds/chargebacks, implementation tools, legal/nutrition/security review and unpriced contract obligations. They are not profit forecasts. If P includes a sales tax that must be remitted, that amount must first be removed from revenue; applicability has not been determined.

At the middle case, ₹200 acquisition takes `200 / 103.743 ≈ 1.93 paid months` to recover before fixed costs and trials. At ₹5/session it takes about 4.57 months. This is contribution payback, not a lifetime-value forecast; churn is unknown. At ₹2/session, `149 × (1 − .035282) / 2 ≈ 71.87 sessions` exhausts a payer's entire contribution before other expenses, which argues against an unlimited plan without usage measurements.

Five sessions for ₹49 with a standard one-off fee of 2.36% and ₹2/session leave `49 × .9764 − 10 = ₹37.84` before acquisition/fixed costs. Lower purchase commitment also leaves less room to find/support each buyer.

## Initial spending, recurring work and cash timing

Before revenue: baseline product access, recruitment, data/permission investigation and later sample evaluation. A proposed research allocation is ₹0–₹1,000 for available trial tools, with remaining monthly budget retained pending demonstrated need. This is a spending ceiling suggestion, not authorization or proof trials are free. Device purchases and paid campaigns are unnecessary for the first comparison.

Before a production launch: approved data access, identity/profile handling, preference deletion/correction, payment setup, recommendation evaluation and security review. Cash quotes and founder build effort are unknown. Existing AI coding subscriptions may be incremental or already paid; do not silently count them as free. Specialist review and integration contracts could exceed the monthly budget.

During operation: model/tool invoices accrue as people use the service, including nonpayers and failed sessions. Proposed monthly payment is collected upfront; settlement can lag collection, and refunds can arrive later. The cited gateway describes typical T+2 business-day domestic settlement, not a guaranteed launch cash schedule. Prepaid packs create an obligation to serve future usage. Commission revenue is zero in all scenarios because no agreement exists.

At ten support minutes for 100 payers, support alone is 16.7 hours/month. If a human spends five minutes on every one of 2,000 paid-user sessions, that is 166.7 hours/month, beyond the founder's usual weekly capacity before other work. A manually assisted experiment can teach us something; it is not evidence of affordable automated delivery.

## Decision implication

Text generation may be inexpensive; customer acquisition, repeated use, data permissions and human attention are the larger unresolved variables. The present budget can plausibly support a bounded comparison using existing tools, but affordability of a compliant live product is not established. Capture real tool/token traces, founder minutes, trial costs and renewals in [T002](tests/T002-payment-and-repeat-use.md) before replacing these assumptions.
