# Decide business labels and opportunity priorities

Parent: [Research and deliver startup idea scout version 2](../map.md)
Labels: wayfinder:grilling
Type: grilling
Mode: HITL
Status: resolved
Assignee: Codex
Blocked by: none

## Question

How should scout v2 describe an opportunity's starting business model and possible scale, and how should that affect eligibility, comparison and recommendations?

Resolve whether gig/service/product and small/durable/scalable are separate dimensions or one label. Stress-test a solo SaaS that stays small, a freelancer who productizes a service, an agency that grows through hiring, and a marketplace needing substantial capital. Decide what evidence supports a scale hypothesis and how uncertainty is shown without unsupported earning promises.

Preserve the current software/AI/similar-technology scope unless the user explicitly broadens it. Decide whether nontechnical creator ideas are excluded, used for inspiration, or admitted. Consult grilling and domain-modeling; record agreed vocabulary in the root CONTEXT only when settled.

## Comments

2026-10-28 — Initial questions sent to user (answers pending):

1. Separate starting business model from possible scale, or use one gig/small-business/startup label? Recommendation: separate dimensions; scale is a hypothesis.
2. Which sizes should be prioritized? Recommendation: include all eligible sizes, favor durable businesses and show gigs separately. Alternatives: equal priority, or scalable-startup focus.

2026-10-28 — User answers received:

- Confirmed separate starting-business-model and potential-scale tags, with scale treated as a hypothesis.
- Confirmed inclusion of all eligible sizes, favoring durable businesses and showing gigs separately.
- The two agreed concepts are recorded in the root CONTEXT glossary. Exact label values and illustrative edge cases still need to be made concrete; this ticket remains claimed rather than claiming the entire classification design is resolved.
- Follow-up pending: retain software/AI/technology eligibility or include ordinary offline gigs/businesses too? The prior scope remains in force until answered.

2026-10-28 — Follow-up answer: retain the existing software/AI/technology scope; ordinary offline gigs are not newly admitted.

## Answer

Resolved 2026-10-28 through the user's two answer rounds; corrected by the user's explicit clarification on 2026-10-29. The earlier gig/freelancing interpretation is superseded below; historical comments remain as history.

- Record starting business model and potential scale separately. Starting model describes how value is delivered/paid for (for example service or product); scale is an evidence-backed hypothesis with its assumptions and constraints, never a promise based on the source platform or the word startup.
- Include opportunities of all sizes within software/AI/similar technology. **Small products aimed at earning quickly** means products the founder builds and owns, including playful/gimmicky apps and timely trend-based products. It does not mean freelance client assignments; do not use “gig” as this track's name.
- **2026-10-29 follow-up:** the user explicitly welcomes **Freelancing / paid client work** as a separate selectable category so those opportunities are not missed. Include it when selected individually or through an all-categories choice, alongside repeatable services/agencies, small owned products and longer-term startups. Assess the paid deliverable, first-client route, sales/delivery effort, net earnings and payment terms; preserve the small-product priority above without conflating the two models. This supersedes any implied general exclusion of freelance opportunities.
- When the user selects that small-product track, earning money as quickly as credibly possible is the top comparison priority. A nearer plausible path to first revenue can outrank a slower durable or larger business. Research build/setup time, first audience, promotion, payment conversion, payout timing and cost recovery; fast building or many views alone does not establish earnings. Virality is an uncertain acquisition hypothesis. Short-lived usefulness, copying or weak retention are explicit trade-offs, not automatic exclusions. No fixed earning deadline was supplied.
- Longer-term startup searches can accept slower initial earnings and favor durability/growth. This correction supersedes a universal durable-business preference; mixed searches must preserve the distinction between the two priorities.
- Keep nontechnical offline businesses outside opportunity eligibility. Creator material about such businesses can supply context or reveal a technology workflow; that does not make the offline business itself an eligible recommendation.
- Consequences of separating the dimensions: solo software can remain small; a service may have a proposed productization path; hiring can grow an agency but carries labor/management costs; a marketplace's growth hypothesis must expose capital and coordination requirements. A small novelty app can be product-based and short-lived without being freelance work. These are explanatory applications of the agreed distinction, not findings about actual businesses.
- The two agreed terms are in root CONTEXT. Exact display wording and how the distinction reads in a comparison will be reviewed in [Agree a concrete scout report with business labels and source coverage](06-agree-report-example.md), rather than prematurely freezing an exhaustive taxonomy here.

2026-10-29 — The user explicitly requested this rule in the skill now. Implemented the narrow correction in scout SKILL.md, the commercial-assessment guide and assessment template, with matching glossary/profile/workflow-map changes. Remaining version-2 work stays in its existing tickets. The commercial guide is the runtime owner of the detailed speed-to-revenue method.

Validation: skill-creator quick_validate.py passed; git diff --check passed; local links and the new commercial-guide anchor resolved. Reviewed the conditional rule against the longer-term comparison and retained research/handoff contracts. These are structural and instruction-consistency checks, not a completed scouting campaign or a runtime earning forecast. Full behavioral examples remain in the report/verification tickets.
