# Decide what scouting establishes and what remains untested

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:grilling
Type: grilling
Mode: HITL
Status: resolved
Assignee: codex-scout-boundary
Blocked by: 01, 02

## Question

What must a scouting run establish, what may it present as a hypothesis, and which decisions belong to validation or to the user's later selection?

Use concrete contrasting examples to agree what candidate, evidence, assumption, confidence, validation, and selection mean. Decide how weak or contradictory evidence, an existing competitor, unknown customer access, and a demanding solo launch are represented without becoming hidden preference filters or unsupported endorsements. Distinguish a disproven claim from rejection based on the user's taste.

Resolve the smallest useful scout endpoint and its handoff: what the user can decide from its output and what requires further work. Consult the research answers, the map's confirmed preferences, grilling, and domain-modeling. This is a live human decision; research agents cannot resolve it on the user's behalf.

## Comments

### 2026-10-01 — Scope clarification during the live discussion

The user likes the proposed scout boundaries but wants the handoff clarified before settling the decision. They narrowed their interest to technology startups, principally SaaS, software products, and AI, excluding businesses such as manufacturing cars. They also requested a skill to perform the deeper investigation after scouting. The map now includes implementing that skill as well as the scout; its detailed responsibilities and name remain open.

The four proposed boundaries remain under discussion: scouting supports choosing the next investigation; sparse evidence and speculative leads stay distinguishable; recommendations carry reasons without hidden filters; and confidence describes individual claims. This comment records the clarification, not a resolution or blanket acceptance of every proposed detail.

### 2026-10-01 — Handoff and scope agreed

The user clarified that software, AI, and similar technology opportunities can exist in any industry, and accepted the recommendation that deeper investigation should produce concrete customer-test plans. This completes the clarification requested after their earlier acceptance of the proposed scout boundaries. The resolution below supersedes the pending-discussion state in the preceding comment.

## Answer

Resolved 2026-10-01 through the live discussion with the user. This settles the scout's boundary and the purpose of its handoff; detailed workflow, records, commercial depth, and skill naming remain with their existing decision tickets.

### What scouting establishes

Scouting provides enough initial research and comparison for the user to choose what deserves deeper investigation. A candidate describes a customer and problem, market, existing alternatives, a possible way to earn money, major delivery dependencies, supporting and contrary evidence, and the next important uncertainty. Unknowns and inferred parts must be explicit; completing those fields is not proof that their hypotheses are true.

The scout must distinguish what a source actually reports from what the proposed opportunity assumes. It can establish that a particular complaint, competing offer, published price, or other attributable observation exists in its recorded context. It cannot transfer that observation into proof that this proposed startup will attract customers, deliver value, earn a margin, or retain users. Desk research alone does not justify an unqualified "validated business" label.

The agreed opportunity scope is maintained in the [map's Notes](../map.md#notes): all kinds of software, AI, and similar technology in any industry. SaaS and AI are examples rather than mandatory product forms. Customer sectors remain open, including sectors whose own businesses make physical products.

### Candidates, weak evidence, and assumptions

Use the canonical definitions in [the domain glossary](../../../CONTEXT.md). A candidate has received initial investigation and may merit further investigation; the term is not an endorsement. A purely speculative idea remains identifiable as an unresearched lead until it has been investigated. Investigation may return thin or no accessible support without establishing that the idea is false.

Retain plausible opportunities with sparse evidence when they have a specific customer/problem and possible business mechanism. Show whether support is direct, indirect, missing, or contrary, rather than presenting all candidates as equally supported. Missing results and inaccessible sources leave uncertainty. Relevant contradictory observations challenge the particular claim they bear on. The scout can finish without convincing candidates and must not invent evidence or enthusiasm to fill a quota.

Assumptions, estimates, and projections remain explicit. Confidence describes the strength of support for a particular claim or finding, with a brief reason; it is not one overall startup confidence score. Strong evidence can support a negative finding. Neither weak confidence nor strong confidence is a synonym for an unattractive or attractive business.

### Recommendations and selection

The scout may recommend investigating, revising, or setting aside the current proposition, with its reasons and uncertainties visible. It does not silently exclude eligible opportunities because of personal taste, a visible competitor, unknown customer access, or the founder starting solo. An evidence-based recommendation is distinct from the user's decision about what to pursue.

Concrete adverse evidence can undermine a specific claim or proposed entry path. Keep the conclusion within that evidence's scope: finding that an incumbent supplies a proposed feature disproves an "unavailable feature" claim, not every possible opportunity in that market. The user's dislike of an idea records a preference-based selection decision, not evidence that customer demand is absent.

The agreed treatment of contrasting hypothetical cases is:

| Case | Scout treatment |
| --- | --- |
| Software for an offline industry has few accessible customer records | Keep the opportunity's evidence gaps visible and identify what must be investigated; poor online coverage is not proof of absent demand. |
| Many attributable complaints describe a recurring problem, but purchase behavior is unknown | Support the problem claim only to the extent the observations warrant; willingness to pay for this solution remains untested. |
| A competing product already addresses the proposed problem | Examine alternatives and a credible reason to switch; neither automatic rejection nor an assumption that competitor customers will buy from a new entrant is justified. |
| Customer access or the identity of the buyer is unknown | Record the uncertainty and its importance to further investigation; do not assume easy access or impossible acquisition. |
| Launch appears to require several people, substantial capital, or specialist dependencies | Expose the requirements and assumptions; do not silently exclude the opportunity or describe it as immediately launchable alone. |

### The deeper investigation handoff

The user chooses an opportunity for a separate deeper investigation skill. The handoff carries the candidate's sources, supported claims, assumptions, contrary evidence, commercial possibilities, dependencies, and unresolved questions, along with the user's selection. It must preserve uncertainty rather than treating selection as new evidence.

The investigator examines the selected opportunity more closely: customer and buyer, competing offerings, differentiation and reasons to switch, pricing, costs, technical feasibility, customer access, and contrary evidence. It can recommend continuing, changing the proposition, or setting it aside, stating the evidence and limits of that judgment.

The investigator also produces concrete customer-test plans for the most important unresolved claims. Each plan identifies what claim to test, with whom, how to obtain relevant evidence, and what result would change the decision. Planning these tests is part of the skill. Running them is a later, separately authorized activity; this map does not authorize outreach, spending, or live startup experiments. Relevant customer evidence must exist before making customer-tested conclusions about purchase or repeat value; doing more desk research does not substitute for it.

Both the scout and this investigation skill must be implemented and behaviorally checked before the map closes. The investigator's final name and detailed contract remain to be settled; no third standalone validation skill is mandated by this boundary decision.

### Remaining work and context pointers

- [Decide the business and customer questions the suite must cover](05-decide-commercial-coverage.md) sets commercial depth and the detail of experiment plans within this boundary.
- [Decide how the scout discovers and compares open opportunities](07-decide-scout-workflow.md) sets research breadth, comparison, and stopping behavior.
- [Decide shared opportunity records and skill handoffs](06-decide-shared-records.md) sets the durable record and repository locations.
- [Agree the startup skill suite blueprint](08-decide-suite-blueprint.md) sets skill contracts and responsibilities within the agreed scouting/investigation boundary.
- [Build and verify the opportunity investigation skill](11-build-opportunity-investigation.md) captures the additional authorized implementation. It remains blocked until its design and scout handoff are ready.

No further research ticket is required to settle this boundary. The existing design tickets cover the remaining sharp questions; broader investigations remain in the map's fog until a concrete need appears.
