# Research evidence for startup and commercial decisions

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:research
Type: research
Mode: AFK
Status: resolved
Assignee: startup-evidence-research
Blocked by: none

## Question

What primary-source methods can inform a startup skill suite's treatment of problem discovery, customer and buyer evidence, willingness to pay, competing alternatives, business models, pricing, costs, and marketing/sales hypotheses, without treating desk research as a validated business?

Bound the investigation to sources that change a design decision. Distinguish evidence about a problem, a proposed solution, a purchase, and repeat use; identify what desk research can establish and what needs customer behavior. Consider service, software, physical-product, and marketplace examples rather than assuming one universal metric or sequence.

Return a concise synthesis with primary-source links, source limitations, candidate design implications, and unresolved decisions. Keep financial formulas or example estimates labeled as models, never observed results or universal thresholds. Include what should pass to the future infrastructure and acquisition maps, without executing those efforts.

## Working instructions

Use the research skill. Claim this ticket before researching. Store findings directly under `## Answer` in this file, set `Status: resolved` only when the question is answered, and return a one-line map gist to the map owner. Do not edit the map or other tickets. This workspace has no Git repository; the map authorizes this local-ticket research workflow.

## Answer

Resolved 2026-09-30 by startup-evidence-research. Seven primary-source pages were read; all links below were accessible on that date. This is method research, not evidence for any particular startup. The design implications are proposals for later decisions, not settled skill requirements.

### Findings and source limits

| Primary source | Finding relevant to the suite | Limitation |
| --- | --- | --- |
| Strategyzer, [Start with the most critical hypotheses](https://www.strategyzer.com/library/how-to-test-your-idea-start-with-the-most-critical-hypotheses), 2017-05-02 | Explicit desirability, feasibility, and financial viability assumptions should determine experiments. Results reconnect to the hypothesis and may leave it unresolved. | Advice from the framework's creator, not a controlled comparison of methods or a universal sequence. Its scalability goal need not become this user's business filter. |
| Strategyzer, [Ways to test your value proposition and business model](https://www.strategyzer.com/library/ways-to-test-your-value-proposition-and-business-model), 2015-04-30 | Ask about actual experiences; distinguish statements from actions. Observed purchase behavior tests a different claim from an interview. Researcher presence can alter behavior. | Method guidance; stronger behavior still only supports the specific claim and context tested. |
| SBA, [Market research and competitive analysis](https://legacy.sba.gov/business-guide/plan-your-business/market-research-competitive-analysis), updated 2026-03-24 | Existing data can describe demographics, location, trends, alternatives, and prices. Direct research offers more specific customer information. Include indirect competition and entry barriers. | US institution and US data links; useful questions do not establish Indian or other markets. Published prices do not reveal negotiated prices or actual sales. |
| SBA, [Break-even point](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point), updated 2024-10-03 | Separate fixed, variable, and mixed costs; break-even is an estimate using price and costs. | Simplified product/service model, not proof of viability or cash sufficiency. Independently check arithmetic and period conversions; the page's quarterly-cost illustration is inconsistent. |
| SBA, [Marketing and sales](https://legacy.sba.gov/business-guide/manage-your-business/marketing-sales), updated 2025-05-29 | Connect audience, advantage, sales steps, channels, goals, budget, and review of results. Delivery and returns influence the customer experience. | General small-business guidance; neither its example channels nor its annual planning cadence is a startup default. Attribution can be difficult. |
| Kickstarter, [Why is funding all-or-nothing?](https://updates.kickstarter.com/why-is-funding-all-or-nothing/), 2024-03-14 | Pledges are charged only if the funding goal is reached. Backing is distinct from purchasing a finished item; delivery can change or be delayed. | Authoritative about its platform, promotional about its benefits. Applies to eligible creative projects; funding does not establish fulfillment, margins, or repeat demand. |
| Sharetribe, [Marketplace metrics](https://www.sharetribe.com/academy/measure-your-success-key-marketplace-metrics/), updated 2024-10-24 | Transaction matching, repeat activity, buyer/seller balance, and captured revenue convey different information. Aggregate visits or transaction value cannot describe all marketplace health. | Advice from a marketplace software vendor. Do not inherit its cited investor benchmarks or loose accounting terminology as universal definitions. |

### Separate the claims being tested

The following distinction is a proposed synthesis of the sources, not a standardized maturity ladder:

| Claim | Useful evidence | What it cannot establish by itself |
| --- | --- | --- |
| A problem exists for a defined segment | Specific past incidents, frequency, consequences, workarounds, existing spending; attributable public records can suggest leads | That the segment wants this solution or will switch |
| A proposed solution produces value | An observed task or delivered service with a stated outcome and conditions | Purchase intent, buyer authority, or repeat value |
| A buyer will commit at stated terms | A recorded commitment with actor, price, conditions, payment state, cancellation/refund terms, and date | A repeatable sales process, successful delivery, or retention |
| Value persists after initial adoption | Follow-up use, renewal, repeat orders, or another outcome appropriate to the buying cycle | Profitability or the same behavior in another segment/geography |

This distinction follows Strategyzer's separation of statements and actions, Kickstarter's conditional funding mechanics, and Sharetribe's repeat-use concerns. A signup, letter of intent, refundable deposit, settled payment, and fulfilled order should retain their actual meanings rather than being flattened into “validated.” A source describing another company's customers remains evidence about that company.

Desk research can establish what a source reports: published offers, competitor features, market counts, documented complaints, cost quotations, or a historical transaction. It can suggest a market entry opportunity and identify contradictory evidence. It cannot establish this startup's conversion, delivery ability, willingness to pay, or repeat demand without relevant behavior. Absence of searchable evidence is an uncertainty, not proof that no problem or competitor exists. These are research implications of the source limits, not a ban on scouting ideas with sparse evidence.

### Use experiments and economics appropriate to the business

These are illustrative experiment candidates, not instructions to execute or required stages:

| Business example | Candidate behavioral evidence | Economics or operational facts to expose |
| --- | --- | --- |
| Service | A paid, bounded engagement delivered to an agreed outcome; later rebooking where relevant | Delivery and selling hours, usable capacity, rework, collection timing |
| Software | A real workflow completed, then a paid pilot/subscription or another suitable purchase; use/renewal after enough time | Hosting or usage costs, onboarding/support effort, purchase authority, cancellation and renewal cycle |
| Physical product | A usable sample plus a clearly described order/deposit; fulfillment and returns tracked separately | Production, minimum quantities, inventory cash, shipping, defects and returns; crowdfunding pledges retain their conditional status |
| Marketplace | A match completed for buyer and supplier, followed by relevant repeat activity | Availability by location/time, match completion, acquisition on both sides, transaction value versus the business's fee revenue |

For durable or infrequent purchases, near-term repurchase may be inappropriate; define an observation window and outcome suited to that product. No source reviewed supports one universal interview count, conversion cutoff, margin, retention rate, or ordering of tests for all these businesses.

**Model, not observed result:** for one consistently defined product/service and period, estimated break-even units = fixed costs / (unit price − unit variable cost), only when the denominator is positive. [SBA's model](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point) provides the starting point. Proposed extensions are to disclose cash versus unpaid founder effort, startup outlay versus recurring expenses, capacity, payment timing, and low/base/high assumptions. Do not substitute modeled revenue or customer lifetime value for observations. Use currency, geography, date, tax treatment, and units consistently.

### Candidate implications for the blueprint

1. Let the scout produce research-supported opportunity hypotheses, contrary evidence, commercial possibilities, and the next uncertainty to investigate. Reserve customer-tested conclusions for recorded customer evidence. Avoid an unqualified “validated startup” label.
2. Carry user, beneficiary, buyer, budget owner, and approver as distinct roles where relevant. Label roles inferred from desk research; verify them during customer work. A user's enthusiasm may leave purchase authority unknown.
3. Keep alternatives broad: direct suppliers, adjacent services, manual work, internal tools, and doing nothing. Existing competition can reveal spending and switching difficulty; it is neither automatic rejection nor proof of demand for the proposed entrant.
4. Treat pricing as an offer hypothesis: who pays, for what unit/outcome, how often, under which terms. Compare alternatives and costs, then identify the customer behavior needed to test it. Geography is part of each claim; evidence from one market should not silently transfer to another.
5. Make marketing and sales hypotheses concrete: segment, buying trigger, reachable venue/channel, message, buying steps, expected effort/cost, and observable response. Record hypothetical acquisition costs separately from measured results. Their design belongs here; outreach and spending do not.
6. Prefer a small shared evidence record: claim, source/artifact, date and geography, observed versus reported versus assumed, sample/context, contrary evidence, limitation, and next test. Prioritize a test by decision impact, uncertainty, time/cost, and reversibility; do not invent universal scores.

### Handoffs and decisions still open

For the **future infrastructure map**, pass the selected opportunity, intended customer outcome, proposed delivery workflow, dependencies, cost assumptions, and unresolved feasibility questions. For the **future first-customer map**, pass the segment and buyer hypotheses, offer/terms, channel hypotheses, experiment design, and measurement definitions. Neither handoff implies authorization to build, purchase, contact people, or run campaigns now.

Still for human/design tickets: the skill boundaries; the smallest scout output; the precise shared-record vocabulary; when to seek live customer evidence; and how to compare ideas without hiding weak evidence inside a total score. This research does not decide the user's preferences or exclude businesses because the founder is solo.
