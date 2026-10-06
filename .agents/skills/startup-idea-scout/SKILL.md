---
name: startup-idea-scout
description: Find, research, compare, or resume software, AI, and similar technology business ideas across industries and markets. Use for open discovery or initial research of a supplied idea; hand deeper investigation of a selected opportunity to startup-opportunity-investigator.
---

# Startup idea scout

Help the user choose what deserves deeper investigation. Deliver a readable comparison supported by substantial initial research, with durable records another session can continue.

## Orient

Resolve the repository root from this skill's location (`../../..`). Shared instructions live under that root's `docs/startup-skills/`; opportunity output normally lives at the repository root. An explicitly supplied output workspace overrides the output root, not the shared-resource location. Resolve existing run/opportunity references before writing.

Read the [record guide](../../../docs/startup-skills/record-guide.md), [research guide](../../../docs/startup-skills/research-guide.md), and [tool routing](../../../docs/startup-skills/tools.md). Consult the [source catalog](../../../docs/startup-skills/source-catalog.md) when choosing sources; follow sources beyond it as the customer and question require. Use [CONTEXT.md](../../../CONTEXT.md) for domain terms. Runtime work does not require reading the planning tracker or the old project.

The eligible scope is software, AI, and similar technology serving **any industry and market**. SaaS and AI are examples, not requirements. Software serving factories is eligible; manufacturing cars itself is outside scope. There is no default country or closed list of product types. The founder starts solo: expose delivery effort, capital and specialist needs, without silently excluding demanding ideas. Use supplied constraints; weekly time, budget, funding preference and income targets can remain unknown for broad discovery.

Choose the entry path from the request:

- **Open discovery:** begin varied searches around customers and their work. Explain the starting directions as exploratory coverage, not the user's preferences. Broaden beyond the first familiar technology community.
- **Supplied idea/problem:** retain and research the original proposition. Nearby alternatives may help compare, but must not replace the brief. Follow explicit market constraints and relevant local terms/languages.
- **Continue a search:** read its saved `scouting-runs/` report for the brief, searched directions, unfinished leads and access gaps; then read the linked opportunities' current summaries and relevant evidence/history.
- **Continue an idea:** read its current opportunity folder first, following earlier runs where search context matters. If the request is deeper investigation of an already selected idea, hand off with the current record instead of running open discovery again. If the investigator is unavailable, give a usable handoff and say so; do not claim it ran.

Ask a short question only when the answer materially changes scope or resolves an ambiguous saved reference. Continue independent useful work while waiting. Tell the user where research is starting and give progress updates on findings, uncertainties and the next checks.

## Discover and pursue the questions that matter

Use independent web searches and relevant public forums to discover customer problems through tasks, frustrations, workarounds and local terminology. Follow relevant pages and links selectively. Idea lists and investor prompts are supplementary inputs; a list failure does not end discovery. Save original sources and meaningful search/access history.

Read original accounts and relevant replies, linked corrections and resolutions. Separate the reported problem from the author's proposed solution. Investigate promising leads with corroboration where available, existing products, manual processes, services and doing nothing. Search for satisfied customers and reasons the proposed product might be unnecessary. Check whether an alleged missing feature already exists or the complaint was resolved.

Follow consequential gaps beyond the first result: identify the customer and possible payer, plausible revenue mechanism, reasons to switch or stay, ways to reach customers, initial build/support work, material costs and dependencies. Use current first-party information for changing product, price or supplier claims. The research guide explains evidence limits and estimates; a candidate needs useful initial findings, not a complete business plan.

Keep uncertain but specific opportunities visible. An investigated idea may remain weakly supported; a purely speculative idea is an unresearched lead. A competitor, limited public evidence, unknown customer access or high solo effort is a finding to evaluate, not an automatic veto. Tie confidence to individual claims, including negative findings. Research and user selection do not establish purchase or repeat-use evidence.

Before ending research, check whether accessible follow-up could change the recommendation. Pursue such questions or name the concrete blocker. A normal round can stop when the comparison is useful and targeted follow-up mainly repeats findings; repetition in one narrow source family does not establish wider coverage. Missing customer observations can warrant an investigation handoff. Save an explicitly incomplete round when access or the requested time/depth prevents the material checks. Neither a candidate quota nor a link count establishes completion; zero convincing candidates is a valid outcome.

## Save and explain the comparison

Use the record guide's templates as aids, filling only useful records. Save authoritative evidence in `opportunities/<stable-name>/`, a new dated report in `scouting-runs/`, and the derived current overview in `opportunities/comparison.md`. Preserve earlier outputs and record what changed. Re-read affected files immediately before updating them so concurrent/newer findings survive.

The overview must stand alone in this order:

1. **Explain each idea:** who uses it, what the product does, and a concrete example of its use. Label an imagined example as an illustration. Explain the customer's work before the evidence, then briefly state the support and the strongest reason this product might be unnecessary.
2. **Compare shared questions in a table:** problem evidence, reasons to change from alternatives, possible payer/income, customer access, build and support work, costs or unpriced requirements, and the biggest doubt. Link findings to their saved detail.
3. **Make an explicit comparison:** explain which idea deserves investigation before another, why the evidence or delivery requirements differ, the trade-offs, and what could change the recommendation. Equal uncertainty or a conditional recommendation is acceptable. With only one candidate, compare the proposed approach with the current workaround or a relevant variation; do not invent another candidate. With none, explain the findings and next search direction.
4. **Show unfinished work:** material unknowns, access limits, older/unreviewed findings, omitted directions and why this round stopped. Important limitations belong here even when details are linked elsewhere.
5. **Link optional detail:** current opportunity summaries and the dated run. The reader need not open them to understand the products and trade-offs.

Use everyday words. Avoid unsupported cheapest/most-profitable/highest-demand rankings and overall startup scores. Keep recommendations separate from the user's selection.

On continuation, current opportunity evidence governs the new comparison. Old runs preserve what was searched and concluded then; they must not overwrite later findings. Refresh or qualify affected overview entries and identify entries not reassessed, without claiming a new full comparison. Leave earlier reports intact.

Finish with the main findings and recommendation, meaningful limits, why research stopped, links to the saved comparison/report, and the next useful choice. The user selects which idea to advance. A handoff to `startup-opportunity-investigator` carries the current opportunity path, proposition, sources, contrary evidence, assumptions, dependencies and unfinished questions. Scouting authorizes no outreach, purchases or live customer tests.
