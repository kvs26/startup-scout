# Survey correction follow-up — costs and possible income

Assessed: 2026-10-17, Asia/Kolkata  
Offer/market: proposed cross-platform follow-up workspace for smaller Indian social, education and development survey teams. Proposed unit is one active study-month, with separately scoped setup; no price or payment terms are agreed.

## Inputs and their basis

| Input | Value, unit and currency | Basis and date | Limit |
| --- | --- | --- | --- |
| Founder cash budget | About ₹5,000/month | User-supplied [profile](../../FOUNDER-PROFILE.md), recorded 2026-10-11 | Available for software/hosting and perhaps occasional expert help, not a promise to fund a business loss indefinitely. |
| Founder time | Usually 10–19 hours/week for learning and building combined | User-supplied [profile](../../FOUNDER-PROFILE.md), recorded 2026-10-11 | Total work capacity including selling/support was not separately stated. |
| Linux server A | US$7/month, 1 GB RAM, 40 GB disk | Sourced [E017](research.md#e017), rechecked 2026-10-17 | Prototype-sized; production suitability untested. |
| Linux server B | US$12/month, 2 GB RAM, 60 GB disk | Sourced [E017](research.md#e017), rechecked 2026-10-17 | Illustrates one larger option, not a recommended production design. |
| Retained snapshots | US$0.05/GB-month; 40 GB assumed | Sourced unit price [E017](research.md#e017), hypothetical retained volume, 2026-10-17 | No restoration, retention or customer requirement tested. |
| Planning conversion | ₹100 per US$1 | Hypothetical, carried from the 2026-10-11 scouting scenario | **Not a current exchange rate or bill.** Used only to compare a USD example with the founder's INR budget. |
| Test price A/B | ₹3,000 or ₹6,000 per active study-month | Hypothetical, 2026-10-17 | Neither is an accepted price or forecast. The lower price is a possible buying-test offer only after a safe product exists. |
| Support exposure | 2 or 4 hours per active study-week | Hypothetical, 2026-10-17 | Excludes onboarding, outages, acquisition and engineering. |
| Customer count | 1 or 2 simultaneously active studies | Hypothetical, 2026-10-17 | A scenario, not a lead or forecast. |
| Payment lag | 0 or 30 days after month end | Hypothetical, 2026-10-17 | Actual procurement, invoicing, taxes and collection terms unknown. |

Competitor prices are separate evidence: [DataQuad](research.md#e018) advertises US$15/month for two checking projects; [SurveyCTO](research.md#e011) advertises US$250/month on monthly Basic billing for its collection platform; [Survey Solutions](research.md#e024) offers free software but requires hosting/devices. None establishes what a team would pay for this proposed workflow.

## What delivery requires

**Before the first paid study:** Learn and verify one team's record IDs, study waves, missing-value codes and approval path; build/import/export with synthetic data; obtain a practitioner review of the workflow and an independent technical review before confidential data. Review fees, domain, monitoring, legal/procurement documents, sales travel and build hours are unpriced. The founder's own time is unpaid in the cases below.

**For each study:** Map the issue-file columns, set permissions, train coordinator/supervisors, help with changed files and disputed matches, respond during fieldwork, export a usable decision log, support deletion/retention and check backups. The proposed product does not itself repair survey data or decide scientific validity. Support and onboarding are not yet measured; a customer may require hosting location, uptime, access controls or data-processing terms that change the cost.

**Cash timing:** Server and other suppliers can bill before any customer money arrives. A study-month fee would be invoiced during or after work under terms still to be negotiated. There is no evidence that a buyer would prepay; if a buyer pays 30 days after month end, the founder would finance at least the first month of hosting and other setup costs. Tax treatment and payment collection costs are unknown.

## Possible cases, not forecasts

1. **Prototype infrastructure:** Server A + assumed 40 GB snapshots = US$7/month + (40 GB × US$0.05/GB-month) = **US$9/month**. At the hypothetical ₹100/US$1 planning conversion, **₹900/month**, leaving ₹4,100 of the stated monthly cash budget before all other costs. Server B with the same snapshots = **US$14/month**, or **₹1,400/month** under that same assumption, leaving ₹3,600. These are supplier subsets, not all-in hosting quotes.
2. **Invoice illustration:** One active study at the hypothetical ₹3,000 fee yields **₹3,000 invoiced for that month**. Two yield **₹6,000**. At the hypothetical ₹6,000 fee, one or two yield ₹6,000 or ₹12,000. Subtracting the ₹900 server-A example gives arithmetic balances of ₹2,100, ₹5,100, ₹5,100 and ₹11,100 respectively **before** every other cash expense and unpaid work. This is not profit. A 30-day payment delay could leave **₹0 cash collected in the first month** against at least ₹900 of modeled supplier spend.
3. **Time exposure:** Two active studies × 2 support hours/study-week = **4 support hours/week**, equivalent to 21–40% of the founder's usual 10–19-hour *learning/building allocation* if support must come from it. At 4 hours/study-week, that is **8 hours/week**, equivalent to 42–80% and leaving 2–11 hours of that allocation for its original purpose. The founder's total hours available for sales/support are unrecorded. A hypothetical 6 hours of setup per study would add 12 hours when those two studies start; actual work may be very different.

## What could change the decision

The decision is more sensitive to a genuine paid gap, customer support hours and specialist review than to the difference between these small server examples. [T001](tests/T001-workflow-and-alternatives.md) seeks actual case volume, handoff friction, existing-tool satisfaction and setup effort. [T002](tests/T002-buying-decision.md) seeks a real purchasing path and buying decision on a defined offer. If a delivery trial becomes appropriate, log founder hours and supplier charges, obtain quotes for independent review and use the customer's actual terms before treating any margin as meaningful. No live customer test, purchase or paid deployment has occurred.

Earlier 2026-10-11 inputs and results, including the US$9/₹900 and support examples, are preserved in [the scouting report](../../scouting-runs/2026-10-11-researcher-workflows.md) and [the pre-investigation snapshot](rounds/2026-10-15-pre-investigation.md). The current [assessment](summary.md) explains why these scenarios do not justify building yet.
