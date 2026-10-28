# Decide the opening questions for a new scouting search

Parent: [Research and deliver startup idea scout version 2](../map.md)
Labels: wayfinder:grilling
Type: grilling
Mode: HITL
Status: resolved
Assignee: Codex
Blocked by: 01, 04

## Question

Which short opening questions should the scout ask on its first invocation in a new session, and how should the answers guide a diverse search while preserving supplied scope, saved profile context and continued campaigns?

The user requests this change on 2026-10-29: ask what kind of ideas to find, beyond the current industry selection, then research based on the answers. They want to explore different kinds of opportunities rather than repeatedly receive one type. Decide exact question wording/options, mixed or delegated choices, priority versus exclusion, reuse of known answers, and new-search versus continuation behavior. This is a human decision using grilling/domain-modeling; the following proposal is not adopted yet.

## Comments

2026-10-29 — Existing behavior checked in scout references/discovery.md: a new broad search offers about six randomly sampled eligible industries plus saved leads, then waits for the user's directions. Already-supplied scope skips that menu; a continuation retains saved scope. Diverse audiences, motives and models are required within chosen areas, but there is no explicit opening questionnaire for their mix.

Proposed opening brief, presented directly in chat, allowing multiple selections and free text:

1. **What would you like to sell?** Paid gigs/freelance work; repeatable services/agency work; digital products/apps/software; a mix; or suggest a mix. These describe starting models, not guaranteed scale. Examples stay within existing software/AI/similar-technology eligibility unless the user explicitly changes it.
2. **What matters most this time?** Start earning sooner; build a durable ongoing business; pursue larger growth potential; or balance these. Optional income target/time horizon when the user has one; do not demand a financial forecast. Treat priority as a preference unless the user states a hard limit.
3. **Which discovery angles interest you?** Existing businesses we could improve/adapt; emerging trends and opportunities with potential to spread; overlooked customer needs/wants; or a mix. These overlap and are not exclusive source categories. Overseas adaptation follows chosen geography and brief.
4. **Who and where should we serve?** Businesses, consumers, or both; India, international markets, or both. The scout owns detailed buyer discovery. Do not silently carry an old campaign's audience/market restrictions into a new one.
5. **Which areas should we explore?** Choose from sampled industries/saved leads, name a theme, or delegate a broad cross-industry mix. Preserve the existing menu for users choosing it. A delegated broad mix is bounded by an explicit stated scope and diversity plan, not a promise to cover every possible idea/industry.
6. **Any practical limits or changes for this search?** Reuse the founder profile's business budget, available time, learning preferences and customer-work preferences; invite corrections plus exclusions or promotion preferences. Keep business startup/running budget distinct from the paid-research API cap. Ask follow-ups only when they materially change the search.

Proposed lifecycle: ask this brief once at the start of a fresh search, filling already-supplied answers and showing known constraints briefly. Explicit “mixed search” or “you choose” can delegate unanswered choices; silence cannot. Summarize the chosen brief and research after actual answers/delegation, without an extra approval round for a faithful summary. For a new chat resuming a saved campaign, display its brief and continue under the user's continuation instruction, asking only about ambiguity or requested changes. Assessing a supplied idea does not trigger an unrelated broad-search questionnaire. Save campaign answers in its existing canonical run record; keep temporary choices separate from lasting founder preferences. Fifty deep assessments remain campaign-wide, not per combination.

2026-10-29 — User accepted the question topics with a correction: give explicit options and let the user choose one. They accepted fresh-search versus resumed-search behavior. This supersedes the proposal's multiple-selection format and its suggested agent-chosen balance. Exact option presentation will be shown in the report prototype; do not treat the earlier option wording as independently approved.

## Answer

Resolved 2026-10-29 through the user's acceptance and format correction.

- Cover the six opening topics: starting business model, commercial priority, discovery angle, customer/geography, search areas, and practical constraints. Present clear, labeled options directly in chat and ask the user to select **one option per question**. Compound topics such as customer type and geography use separate single-choice prompts so one choice has a clear meaning; six topics need not be six overloaded questions.
- **2026-10-29 terminology correction:** the user's small-opportunity choice means “Small products aimed at earning quickly,” including playful/gimmicky or potentially viral apps, not gig/freelance assignments. Use the corrected [business-label decision](01-decide-business-labels.md#answer). Present search track/priority distinctly from the service/product starting model. Selecting the quick-earning small-product track sets speed to revenue as its top priority; do not ask a later generic priority question that silently undoes that selection. A longer-term startup track accepts a slower start, and an explicit mixed choice preserves both. Exact menu presentation remains with the report prototype.
- Offer an explicit broad option where appropriate, such as “all these types,” “both customer groups,” or “balanced priorities.” Selecting it is one user choice; do not infer it from silence or choose the user's balance automatically. Include a custom-answer route where the fixed options do not fit. A user may still explicitly delegate in their own request, but the standard opening should solicit their selection.
- **2026-10-29 follow-up:** retain **Freelancing / paid client work** as its own explicit option; the user has now requested it alongside the small-product track. The category menu covers freelance/client work, repeatable services/agencies, small products aimed at earning quickly, longer-term startups, and an explicit all-categories option. Selecting all includes freelancing; selecting only owned products does not introduce client assignments. Exact presentation remains part of the report prototype, with starting model and scale still recorded separately.
- The industry/lead menu follows the same single-choice format. It can offer individual areas and clearly described multi-area bundles so selecting one option need not force a one-industry campaign. Show actual options, including saved leads and sampled industries as relevant, rather than merely asking the user to invent a scope. Preserve provenance for actual random sampling. Preview exact option wording in [Agree a concrete scout report with business labels and source coverage](06-agree-report-example.md).
- Ask the opening brief for a fresh search, reuse answers already supplied, and show the existing founder constraints for keeping or changing. Wait for missing scope choices. For a new chat resuming a saved campaign, show its saved brief and continue without repeating the full questionnaire. Ask only when necessary to resolve ambiguity or a requested change. A supplied specific idea receives only relevant clarification.
- After the actual selections, summarize the brief and research without another approval round for that faithful summary. Save answers in the canonical run record; campaign preferences do not silently become permanent profile restrictions. Distinguish preferences from hard exclusions, starting model from potential scale, and business budget from research API budget. Keep the campaign-wide fifty-deep-assessment requirement.

Next owner: wayfinder with the user for [Decide category subagents and synthesis ownership](05-decide-subagent-workflow.md), using this opening brief as the researchers' shared scope. The report prototype will make the single-choice menus concrete; implementation and behavioral checks follow in their existing ticket.
