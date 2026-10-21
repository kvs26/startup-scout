# AI Companions — costs and possible income

Assessed 2026-10-18. Proposed offer: US$9 per month, paid in advance, for one adult text companion and up to 1,000 generated replies, with visible usage and renewal terms. One non-renewing trial of up to 100 replies. These are test terms, not accepted prices or live offers. [Business explanation](summary.md).

## Inputs and basis

| Input | Value | Basis and limit |
| --- | --- | --- |
| Subscription | US$9/account/month | Proposed; taxes, supported selling countries and checkout remain unresolved. |
| Generation | $0.30/million input; $2.50/million output tokens | Current Gemini 3.5 Flash-Lite Standard benchmark, [E005](research.md#e005); not a chosen or tested production model. |
| Ordinary use | 600 replies/month, 6,000 input and 250 total billable output tokens/reply | Assumption. Input includes character instructions, retrieved memories and recent chat. Output must include any reasoning charged by the supplier. |
| Proposed allowance case | 1,000 replies, same token sizes | Assumption; regenerations also consume allowance. |
| Long-context case | 1,000 replies, 20,000 input and 500 output tokens/reply | Stress scenario, not usage observed in customers. |
| Additional model work | 25% added to generation cost | Hypothetical reserve for retries, summaries, memory and automated checks; must be replaced with actual accounting. |
| Payment/refund allowance | 5% of sales | Hypothetical aggregate allowance, not a processor quote; fixed fees and cross-border charges can change it. |
| Other variable cash | $0.75/account/month | Assumed storage, email, monitoring and cash support reserve. Does not buy human support coverage. |
| Fixed technical cash | $10/month | $5 Workers base benchmark, [original source](../../scouting-runs/2026-10-18-consumer-apps.md#shared-e002), rechecked; another $5 assumed for domain allocation, logs/email/backups. Not a complete vendor quote. |
| Founder limits | ₹5,000/month; 10–19 hours/week | [User-supplied profile](../../FOUNDER-PROFILE.md); budget includes learning/building. |

## Per-customer calculation

`Generation = replies × ((input tokens × $0.30 + output tokens × $2.50) / 1,000,000) × 1.25`.

`Contribution = $9 × (1 − 0.05) − generation − $0.75`.

| Case | Generation/month | Contribution/month before acquisition, fixed spend, tax and founder labor |
| --- | ---: | ---: |
| Ordinary | $1.81875 ≈ $1.82 | $5.98125 ≈ $5.98 |
| Full proposed allowance | $3.03125 ≈ $3.03 | $4.76875 ≈ $4.77 |
| Long context | $9.06250 ≈ $9.06 | −$1.26250 ≈ −$1.26 |

The generation calculation is not the complete cost of serving a customer. If adequate quality needs twice the modeled generation spend, ordinary contribution becomes $4.1625; at three times, $2.34375. If 5% payment/refund allowance becomes 10%, each case loses a further $0.45. Taxes are not included in either allowance.

A message allowance alone does not bound the token bill. The proposed product needs managed context, input/output limits, a global supplier-spend limit, account abuse controls, and user-visible handling when the allowance ends. Check the complete experience at those limits; an affordable but frustrating companion is not viable. No unlimited plan is justified by this scenario.

## Acquisition and repeat use

A fully used 100-reply trial costs `100/1,000 × $3.03125 = $0.303125` in modeled generation. At hypothetical 10% trial-to-paid conversion, trial generation alone costs `$0.303125 / 0.10 = $3.03` per new payer; at 2%, `$15.16`. Trials also consume operations and founder effort. Neither conversion rate is measured.

At ordinary contribution, an assumed $12 cash acquisition cost needs `$12/$5.98125 = 2.01` paid months to recover, before fixed spend and labor. This is a payback scenario, not a retention or lifetime-value forecast. Views, followers and registrations cannot establish it.

100 hypothetical ordinary-use subscribers produce $900 monthly revenue and $598.13 contribution. Subtracting the assumed $10 fixed technical cash leaves $588.13 **before** acquisition, tax, production tools, reviews and all founder labor. This is arithmetic, not profit or a sales projection. At a hypothetical ten support minutes each, those accounts require 16.7 support hours/month before engineering, content and marketing.

## Founder cash and time

For budget stress only, assume **₹100 per US dollar**, deliberately a planning assumption rather than a current or historical exchange-rate quote. Actual conversion, tax and payment fees must replace it before spending. Also reserve a hypothetical ₹2,000/month for AI production tools; existing entitlements and actual required tools are unverified.

Five ordinary-use test accounts cost `($10 + 5 × ($1.81875 + $0.75)) × ₹100 + ₹2,000 ≈ ₹4,284/month` for this provisional technical/tooling/variable-cash bundle. Ten cost about ₹5,569; twenty about ₹8,138. These figures exclude acquisition, additional trial visitors, tax, paid reviewers and human work. Thus the ₹5,000 budget permits a tightly bounded technical exercise at best; it does not establish an affordable public launch. Participant compensation and age-assurance services are unpriced.

An initial founder effort envelope could be 30–60 hours directing and checking a sample, derived from an assumed 8–16 hours on character/experience, 12–24 on implementation direction and 10–20 on evaluation and repairs. At 10–19 hours/week that is roughly 2–6 weeks **for a sample**, not a commercial-readiness estimate. Extra production subscriptions, setup, specialist review and launch work may exceed both envelopes. These are planning allocations, not productivity measurements.

Charge monthly in advance only after a working deliverable and clear cancellation/refund terms exist. Supplier usage and tooling may be payable before customer payouts arrive; payment holds, refunds and failed renewals need a cash reserve. Do not fund an unbounded free tier on assumed future subscriptions. No checkout, API purchase or customer payment occurred.

## Decision-changing checks

Replace hypothetical usage with measured billable tokens and failures; verify character quality under the same budget; establish the payment route and actual fees; measure trial cost and renewal in [T002](tests/T002-payment-and-return.md). If quality requires longer context or extensive human intervention, revise the price/allowance before scaling. Preserve this scenario in the [dated round](rounds/2026-10-18-selected-investigation.md) when updating it.
