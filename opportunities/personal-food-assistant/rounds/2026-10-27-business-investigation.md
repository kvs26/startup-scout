# Personal food assistant — first business investigation

Recorded and assessed 2026-10-27, Asia/Kolkata. Round state: **usable desk-research result; hands-on comparison and customer evidence outstanding**. Starting records: October 24 scout and October 25 correction, current opportunity files, founder profile and shared guides. The [pre-investigation views](2026-10-25-pre-investigation-snapshot.md) were preserved before updating them.

## Proposition and conclusion at this time

Software for adults who find repeated delivery decisions difficult: the person asks conversationally, the assistant searches authorized current menus and offers a shortlist, and optional after-meal feedback informs later choices. Checkout is optional; cooking and groceries remain later possibilities. India is the inherited initial delivery context, not a permanent restriction. Individual user/payer; proposed ₹149 per 30 days for up to 20 decision sessions, food separate. No accepted price or validated customer segment.

**Recommendation then:** continue with a fair comparison against existing assistants before building the full product. A narrower advantage could justify entry into a competitive market, but none has been demonstrated. The strongest support remains the founder's specific experience. The strongest objection is that existing assistants and dedicated apps already advertise conversation, memory and even learning from dining feedback. The presence of competitors does not rule out a business; it makes comparative value the central question.

User selection: on 2026-10-27 the user explicitly requested proper investigation of this opportunity and invited clarifying questions. No build, price, launch or customer-test execution was selected. Questions about previous trials and participant access were sent; no answers had arrived when saved. No new lasting founder fact warranted a profile rewrite.

## Findings and changes

1. **Overlap confirmed, benefit still untested.** Claude/Swiggy remains the main India-oriented baseline. Current Anthropic sources document memory and web connectors on free plans, subject to practical access/usage. ChewIQ's advertised outcome learning challenges a feedback-memory uniqueness claim. Its app-description mismatch and Choozin launch conflict remain unresolved. Alexa's checked India announcement still calls Swiggy delivery forthcoming. [E020–E025](../research.md#e020).
2. **Delivery access is conditional.** Swiggy offers an application route; staging/production documentation conflicts persist. Zomato explicitly restricts third-party apps. Contractual retention and model-processing conditions matter for the proposed persistent profile. Approval, quotas and tariffs remain unknown. [E016–E019](../research.md#e016).
3. **A concrete data gap emerged.** Checked Swiggy menu schemas do not guarantee nutrition, allergen or spice fields. This limits what can be promised even with access. Some descriptions may supply information; no live coverage audit occurred. [E018](../research.md#e018).
4. **Customer evidence is still weak.** One original public account reports successful conversational ordering but explicitly questions convenience; a food-quality complaint does not prove actual nutrient composition. Satisfied favorites and household fallbacks appeared in search extracts, but original-page access failed. Builder surveys/promotions were excluded from independent-demand evidence. [E026–E028](../research.md#e026).
5. **Economics are more explicit.** Added sourced model/payment/hosting inputs and separated trial costs and founder labor. Costs can be manageable without establishing profitable acquisition or retention. [E029–E031](../research.md#e029).

Stable C001–C005 were retained. Added C006 for data sufficiency and C007 for customer access/solo operation. No customer result IDs allocated. The old scout report was left unchanged. `opportunities/comparison.md` did not contain this opportunity, so no comparison entry was added or other opportunity reassessed.

## Calculation snapshot

The earlier scout used 100 × ₹149 collections, 20 sessions/payer, serving cost ₹2/₹5, a 3% payment assumption, ₹1,000 fixed allowance and 20 acquisitions × ₹200. Its residuals were ₹5,453 and −₹547 before exclusions. That historical scenario remains in the scout.

This round uses 100 payers × ₹149 = ₹14,900 gross; 20 sessions/payer plus 100 trial users × three sessions; illustrative recurring payment `(2% + .99%) × 1.18 = 3.5282%`; fixed ₹1,000; acquisitions 20 × ₹200. Formula: `N × [P × (1 − f) − u × s] − F − trials × t × s − acquisitions × CAC`.

| Hypothetical INR/session | Contribution/payer | Monthly residual before exclusions |
| --- | ---: | ---: |
| ₹0.50 | ₹133.74 | ₹8,224.30 |
| ₹2 | ₹103.74 | ₹4,774.30 |
| ₹5 | ₹43.74 | −₹2,125.70 |

All volumes, demand, INR serving costs and acquisition are assumptions. Excludes founder pay, sales taxes, refunds, review and unpriced obligations. At ₹200 acquisition, contribution payback is approximately 1.50/1.93/4.57 months; not predicted customer lifetime. Five prepaid sessions at ₹49, one-off payment fee 2.36% and ₹2/session leave ₹37.84 before fixed/acquisition costs. No commission assumed.

Sourced supplier illustration: Gemini 3.1 Flash-Lite standard input $0.25/million and output $1.50/million. Hypothetical session totals 12k/2k tokens cost $0.006; 60k/6k cost $0.024. At 2,000 sessions: $12/$48 model-only. Four grounding queries/session gives 8,000 queries; with an unused shared 5,000 allowance and $14/1,000 excess, adds $42. USD was not converted to INR. Workers paid minimum $5/month is a component, not an additional charge on top of the hypothetical fixed allowance. No model/tool trace measured.

Ten support minutes × 100 payers = 16.7 hours/month. Five manual minutes × 2,000 sessions = 166.7 hours/month. These hypothetical workloads show why assisted research cannot establish self-operated software economics. Provider and specialist quotes remain unknown; ₹5,000/month cannot be assumed to cover production obligations.

## Test-design snapshot

**T001 — existing alternatives:** propose a small scheduling batch of five to eight willing adults with recurring delivery occasions, distinguishing frequent and cook-absent users and including satisfied reorders. This is not a statistical sample-size rule. Reconstruct three prior choices; observe ordinary-method occasions; fairly configure Claude/Swiggy with the same profile and feedback; compare later new-chat recall, changed budgets, disliked fallbacks and variety over naturally occurring orders. Record active choosing/setup/feedback time, rejections, price evidence, choice, after-meal report, researcher help and voluntary return. Menu uploads are a partial ranking test, not delegated search. Existing solutions working well argues against the present build; shared data failures require data work; repeated consequential failures suggest a specific improvement. Planning estimate 20–30 minutes initial/person, a few occasions over about two weeks, final 5–10 minutes; founder 4–8 hours/week, unmeasured. No purchases induced. [Full T001](../tests/T001-existing-alternatives.md).

**T002 — purchase and repeat use:** conditional on T001 showing a useful improvement and on permitted delivery. Separate production workflow must supply a usable, accurately described sample. Offer ₹149 prepaid/30 days/up to 20 sessions, food separate; finalize scope/refunds/taxes before any actual offer. Record real payment/refusal/refund, full-month voluntary use, costs and assistance, then intentional renewal plus later use. Interest, deposits, automatic renewals without use, or heavily assisted use are weaker evidence. Compare to free alternatives. Occasional-use pricing would be a later version, not an untracked change. No universal conversion target; proceed only when reasons to buy, continued value and realistic cost coverage agree. [Full T002](../tests/T002-payment-and-repeat-use.md).

## Research coverage and access

Available tools were discovered: built-in web search/read and browser runtime. Tavily was not exposed as a callable tool; local configured credentials were not used and no allowance check or paid call was attempted. Built-in web served as fallback.

| Direction / representative query | Work and result |
| --- | --- |
| Existing remembered food assistants; ChewIQ/Choozin pricing; Claude Swiggy memory; Alexa delivery | Completed with first-party findings. Local installed performance untested. ChewIQ correct domain found in prior evidence after an unsuccessful guessed `.com` URL. |
| Swiggy access, data/compliance, rate limits, search/full-menu schema; Zomato manifest | Completed with findings and documented contradiction; no authenticated call or production permission. |
| `Swiggy Claude MCP food ordering experience` | Found and read an original mixed success account. StartupTalky repost not counted independently. MediaNama review direct open returned 403; indexed claims not used as confirmed current failures. |
| `what to order swiggy same`; `Swiggy EatRight good`; India fitness food complaints | Completed with selective findings. Several obvious founder/research/promotional posts excluded as independent customers. Protein-label complaint read with replies. |
| Satisfied favorites, food recommendations and household alternatives | Search extracts found positives/fallbacks; two relevant original Reddit threads failed with cache misses. Retained as limited leads, not verified observations. |
| Google model pricing, Razorpay payments, Cloudflare hosting | Completed with original-source inputs. Razorpay pricing root empty; official explanatory article supplied rates. |
| FSSAI menu-labelling context | Search found older guidance and current amendments index, but current legal applicability not fully reviewed; no legal rule inferred into the recommendation. |
| Public ChewIQ demo | Browser bootstrap failed with `Importing module "node:process" is not allowed in node_repl`, before navigation or interaction. Hands-on test not performed; failure says nothing about the product. |
| Choozin Indian App Store, Swiggy standalone FAQ | Opening failed. Official website/developer FAQ used where informative; launch and staging conflicts remain qualified. |

Scope is selected alternatives, not an exhaustive global inventory. Sources skew English/digital, and public forum identities/dates are uncertain. No relevant representative survey, prospective-buyer interview, signed terms, cost trace, current dish audit, payment or retention observation was obtained. These are unknowns, not proof of absent demand. No outreach, order, purchase or implementation performed.

## Next owner and stopping reason

Further similar desk research would repeat the core findings. The next material uncertainties need a hands-on comparison, actual customer behavior and provider confirmation. The failed demo leaves practical benchmarking explicitly unfinished; it does not invalidate the usable business assessment.

Next owner: **startup-customer-connect** to prepare T001 recruitment and conversations; skill available/read for handoff but not invoked. Then the **user** runs voluntary comparisons and returns observations to **startup-opportunity-investigator**. Build, pricing and continuation decisions remain the user's.

Ready-to-use handoff:

> Use `opportunities/personal-food-assistant/summary.md`, `research.md`, `tests/T001-existing-alternatives.md` and `FOUNDER-PROFILE.md`. Prepare recruitment and learning conversations with adults facing repeated delivery choices, including satisfied existing-tool users. Confirm contacts instead of assuming friends will participate. Preserve delegated search, conversation and remembered preferences; checkout optional. Prepare only, with no sending or live tests. Return actual observations to startup-opportunity-investigator under this opportunity path.
