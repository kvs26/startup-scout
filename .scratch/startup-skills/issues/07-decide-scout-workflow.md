# Decide how the scout discovers and compares open opportunities

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:grilling
Type: grilling
Mode: HITL
Status: resolved
Assignee: Codex
Blocked by: 02, 03, 04, 12

## Question

How should a scout run choose research directions, generate and investigate opportunities, compare the resulting candidates, and stop while keeping geographies and business models open within the agreed scope of software, AI, and similar technology across any industry?

Decide the behavior for an open-ended request, a user-supplied problem or idea, a named market, and continuation of earlier research. Address source diversity and bias, unexplored markets, evidence and counterevidence, existing alternatives, customer access, initial delivery requirements, and what to do when browsing or a source is unavailable.

Choose an initial source set suited to software, AI, and similar technology across industries, extending beyond the old passive-site resources. The user specifically requested considering Y Combinator and other relevant places. Evaluate candidates for their actual role: startup-method guidance, opportunity discovery, customer/problem evidence, competing offers, or technical and economic inputs. Guidance and lists of successful startups must not become evidence of demand for a proposed opportunity. The completed discovery-source research is a representative coverage study, not a finalized resource catalog or a review of YC. Any additional external research needed for selection must be performed before adopting a source; do not assume current access or suitability.

Agree useful breadth and research depth, adjustable effort, comparison criteria, and presentation of uncertainty. Do not introduce arbitrary candidate quotas, universal scores, default geography, or spending limits as settled rules. Decide what can be done with available tools before commissioning scripts. The user chooses among opportunities; autonomous research does not authorize external outreach or spending. Consult grilling and domain-modeling.

Use [Research reusable startup tools, MCP servers, and discovery resources](12-research-reusable-startup-toolkit.md) when considering existing discovery tools and maintained idea/problem lists. Its findings inform selection; they do not automatically adopt a resource or establish customer demand.

## Confirmed discovery requirement

The user clarified on 2026-10-03 that maintained idea lists are supplementary inputs, not the scope of discovery. The scout must independently search and crawl/read the wider web and public forums to find problems people describe, including opportunities not present in any curated list. Following only links from a list or checking only its suggested ideas does not satisfy this requirement.

Look for concrete accounts of frustrating work, repeated manual steps, unmet needs, limitations of existing products, and workarounds in relevant communities, discussions, reviews, and other public sources. Preserve the original source and context, investigate contrary accounts, and distinguish a reported problem from evidence that someone would buy the proposed solution. These examples guide investigation without fixing an exhaustive source list or requiring every run to visit every source family.

Choose search directions that can surface new problems beyond the idea-list suggestions. Save enough of the search scope and access gaps to explain where the findings came from. If browsing or a source is unavailable, disclose the limitation; do not substitute list summaries and claim that direct discovery occurred. Exact source choices, research effort, and stopping rules remain for this ticket's live decision. This clarification does not require a particular crawler or MCP server.

## Comments

### 2026-10-03 — Workflow discussion started

Claimed after confirming the research and scout-boundary prerequisites are resolved. A supporting subagent is checking practical source options and access; its findings do not adopt sources or settle workflow choices.

The first live round asks whether an open request should start autonomous exploration across varied customer/work problems or first ask the user to choose directions; whether a supplied idea should include nearby possibilities; and whether the default effort should be a balanced pass, a quick pass, or a question each run. Recommendations are proposals awaiting the user's answers, not agreed defaults. Later discussion must still settle comparison, source selection and coverage, stopping behavior, named-market requests, continuation, and access failures.

### 2026-10-03 — Supporting source and access check

The supporting research subagent independently searched for workflow problems and opened original discussions with the available web tools. This demonstrates a selective search-and-read pass, not exhaustive crawling or guaranteed access to every forum. No installations or source adoption occurred.

| Possible role | Checked source and limits |
| --- | --- |
| Independent public problem reports | [Small-business inventory/invoicing discussion](https://www.reddit.com/r/smallbusiness/comments/1mecoxb/small_business_needs_inventoryinvoicing/): original post and replies readable; manual-work complaints alongside spreadsheet workarounds, products and sales pitches. Identity, geography and willingness to buy remain unverified. |
| Regional and product-specific discussions | [Frappe India expense-allocation discussion](https://discuss.frappe.io/t/input-service-distributor-anyone-implemented-working-on-it/161555): March 2026 discussion readable; replies suggest existing functionality and development work. Linked GitHub issue failed to open, leaving current implementation status unverified. |
| Supplementary prompts and idea lists | [YC Requests for Startups](https://www.ycombinator.com/rfs) and [startup-ideas](https://github.com/fayerman-source/startup-ideas) readable. Expert/editorial prompts and links can seed leads; they do not establish customer demand or define the search scope. |
| Competing offers and costs | [Zoho Books India pricing](https://www.zoho.com/in/books/pricing/) readable with prices, features, billing units and limits. Advertised supply does not establish purchase behavior or suitability for a particular reported problem. |
| Coverage beyond online forums | [World Bank Enterprise Surveys methodology](https://www.enterprisesurveys.org/en/methodology) readable; dataset access untested. [India eProcurement](https://eprocure.gov.in/eprocure/app) landing-page notices readable; detailed search and attachments untested. Population, country, period and buyer type limit inferences. |

The [Census CBP About page](https://www.census.gov/programs-surveys/cbp/about.html) now warns that its information is no longer current while disclosure methods are reconsidered. This qualifies the earlier coverage research: check release-specific guidance before relying on its methods or figures.

This small English-language sample overrepresents digitally active people and existing product users. Proposed workflow implications remain subject to discussion: choose searches from customer roles and tasks independently of lists; read replies and alternatives; record search scope and access gaps; use existing tools for selective reading initially and evaluate extra retrieval tools only against a demonstrated need. Tool adoption and setup remain with the suite-blueprint and setup tickets.

### 2026-10-03 — Search direction and nearby possibilities agreed

The user accepted autonomous exploration across varied customers and problems when no direction is supplied, explicitly clarifying that an existing idea or supplied direction must guide the scout when present. The user also accepted checking closely related possibilities while keeping the original idea visible. This does not authorize ignoring a supplied scope or replacing it with unrelated exploration.

The user requested clarification of “chosen each run” in the research-effort question. It means asking how much research the user wants each time the scout starts. No effort default has been accepted yet; the balanced-pass recommendation remains pending.

### 2026-10-03 — Balanced effort with substantial research depth agreed

The user accepted balanced effort as the default, explicitly requiring deep research instructions rather than checking only one or two links. This supersedes the pending effort choice above. The scout must investigate findings beyond superficial link collection; “balanced” must not be implemented as a shallow scan. The user can still request a quicker or more thorough pass.

Proposed operational detail for the next live round: explore broadly, then follow promising leads into original problem accounts and replies, independent corroboration where available, existing solutions and workarounds, contrary evidence, customer access, and material delivery/cost dependencies. Follow important gaps with targeted searches, distinguish copied reports from independent observations, and explain unsupported claims. These details, the stopping rule, source menu, comparison approach and continuation behavior are still proposals for discussion; no fixed link count or candidate quota has been agreed. Scouting retains its agreed purpose of choosing further investigation; depth does not turn desk research into demonstrated customer demand.

### 2026-10-03 — Sources, comparison, collaboration and continuation agreed

The user accepted the proposed source strategy and explicitly requested a proper shared starting-resource list for agents using the skill. The list must be concrete and maintained as a common reference, while leaving agents free to use other relevant sources. A research subagent is preparing the checked planning asset under this map's directory; runtime packaging belongs to the blueprint and build tickets.

The user accepted comparison by customer/problem evidence, existing solutions and reasons to switch, payer and business model, customer access, delivery effort/costs/dependencies, and remaining doubts or next investigations. Recommendations explain their reasons and leave selection to the user.

The user accepted stopping when a useful evidence-backed comparison is possible and further searches mainly repeat findings, continuing when an unresolved question could change the recommendation. Access or available-time limits must produce an explicit incomplete result and next steps, not a false claim that research is complete. The user additionally required collaborative research: provide updates during the work and ask questions when needed.

The user accepted resuming saved work, following unfinished leads and coverage gaps, rechecking important changing facts, preserving history, and following new directions. They asked whether resumption reads the run or the idea folder. The clarification follows the already agreed shared-record contract: read the relevant saved run for search history and unfinished work, then linked opportunity folders for current findings and underlying evidence. For a request about one idea, start with its folder and follow relevant run links as needed. A historical run comparison must not overwrite newer opportunity findings; ask which run or idea only when genuinely ambiguous.

## Answer

Resolved 2026-10-03 through the live discussion. The user agreed the workflow below and requested the concrete [Shared starting resources for startup scouting](../../../docs/startup-skills/source-catalog.md), which has been created and checked. This resolution specifies the scout; its implementation remains with the build ticket.

### Start from the user's direction

- **Open request:** choose varied customer groups and work problems, explain the search directions, and start researching. Include different relevant industries and markets without assuming a default country or limiting the search to founder/technology communities. Record areas not explored; a run is not a worldwide market census.
- **Supplied idea or problem:** follow the user's direction, investigate the original proposition, and consider closely related problems or customer groups. Keep the original idea visible and respect explicit boundaries. Nearby exploration must not quietly replace the brief.
- **Named market:** focus discovery on that market, using relevant customer roles, local terms, languages, communities, and existing alternatives. Clarify the meaning of the market only when ambiguity would materially change the work. Wider examples can supply context without becoming evidence about that market.
- **Continuation:** use saved run history and current opportunity records as described below, incorporating any new direction.

The opportunity scope and evidence boundaries remain those in the [map](../map.md#notes) and [scout-boundary decision](04-decide-scout-boundary.md#answer). Founder time, budget and income goals are not prerequisites for broad discovery; use supplied constraints without inventing others.

### Research broadly, then follow the important questions deeply

Balanced effort is the default, with substantial research depth. The user may request a quicker or more thorough pass. A quick request changes the amount of work and the reported completeness, not the standard for making factual claims.

1. Search independently for actual customer problems: frustrating tasks, repeated manual steps, workarounds, unmet needs and limitations of existing products. Choose directions from customers and work, not only from curated idea lists. Preserve useful search terms, source families, markets and access gaps in the run record.
2. Read original problem accounts and relevant replies. Follow linked explanations, corrections and resolutions. Distinguish the observed problem from an author's proposed solution, and distinguish several independent observations from copies of the same incident.
3. Follow promising leads with targeted searches. Look for corroboration where available, existing products and manual alternatives, reasons customers might switch or stay, and accounts that challenge the proposition. Investigate whether an apparent missing feature is already available, a configuration issue or a solved problem.
4. Investigate the material business questions enough to support comparison: customer and possible payer, possible revenue mechanism, customer-access routes, initial delivery work, operating effort, costs and dependencies. Use current first-party offers and supplier documentation when relevant; label assumptions and estimates. Scouting does not require exhaustive financial modeling of every lead.
5. Pursue important uncertainties and contradictions that could change the recommendation. After follow-up, state what the evidence supports, what it challenges, and what remains unanswered. A specific obstacle or missing customer observation is more useful than an unsupported confident conclusion.

Opening one or two links is not a completion rule. Depth is demonstrated by following material questions, checking alternatives and opposing evidence, and explaining remaining gaps. Neither a link quota nor a fixed candidate count establishes quality. Sparse evidence can remain a clearly qualified candidate; unsupported speculation remains an unresearched lead. A run may find no convincing candidates.

### Shared starting resources and tools

Use the [shared resource catalog](../../../docs/startup-skills/source-catalog.md) when choosing where to research. It records concrete sources, their purposes, evidence limits, access checks and dates. It covers independent discussions and reviews, supplementary idea prompts, startup-method guidance, official market and buyer context, and first-party product and supplier information.

The catalog is a common starting point, not a closed list or a requirement to visit every source. Search beyond it when the customer, language, industry or question warrants that. Keep useful reusable additions in the catalog; keep opportunity-specific source evidence in the relevant opportunity record. YC and maintained idea lists supply directions, while customer and problem claims require their own evidence.

The source checks support using available search and page-reading tools for an initial selective discovery workflow. They do not establish comprehensive crawling, universal site access or tested APIs. Additional tools, scripts and integrations must address a demonstrated need; adoption and setup remain with the [suite blueprint](08-decide-suite-blueprint.md) and [selected-tool setup](13-guide-tool-setup.md).

When a source fails, try relevant alternatives and record the limitation. If browsing is unavailable, use saved or user-supplied material with its dates and limits, and identify work requiring live research. Never present a list summary as completed independent discovery. Distinguish a failed source, an unperformed search, and a completed search with no relevant results. None alone establishes absent demand.

### Compare opportunities with reasons

The concise comparison covers:

| Question | What the scout presents |
| --- | --- |
| Who has the problem? | Customer/problem and market context, supporting and contrary evidence, and limits on what can be concluded. |
| Why change the current approach? | Existing products, services, manual workarounds or doing nothing; plausible reasons to switch and reasons to stay. |
| Who might pay? | Possible payer and revenue mechanism, with willingness to pay and economic assumptions kept explicit. |
| How could customers be reached? | Plausible access routes and uncertainties, without claiming access has been obtained. |
| What would delivery involve? | Initial build and operating effort, material costs, capital needs and specialist or external dependencies. |
| What should be learned next? | Important doubts, the next investigation, and the reason for recommending investigation, revision or setting aside the current proposition. |

Use plain-language comparisons and explained recommendations. Confidence attaches to particular claims, not a universal startup score. Existing competitors, unknown customer access and demanding solo delivery are findings to evaluate, not hidden exclusion rules. The user chooses which opportunity to pursue; selection adds no evidence of demand.

The [output prototype](09-prototype-scout-output.md) will settle readable presentation and detail placement. The [shared-record decision](06-decide-shared-records.md#answer) governs underlying evidence and history; summaries link to that evidence rather than duplicating it.

### Collaborate during the run and stop for an explicit reason

Tell the user where the scout is looking, share meaningful findings or changes in direction during research, and explain what is being checked next. Ask when the user's answer would materially change scope, resolve competing interpretations, or guide a meaningful trade-off. Continue independent useful work while waiting when possible. Routine factual questions belong to research, not to the user.

A normal round ends when it can support a useful comparison and targeted follow-up is mostly repeating findings. Keep investigating an unresolved question when accessible further research could change the recommendation. Repetition within one narrow source family is not evidence that wider relevant coverage is complete; explain material coverage gaps.

If source access or available time prevents completing those checks, save an explicitly incomplete result with the blocking gap and next useful step. If the missing evidence requires customer observation or a real test, identify it as the next investigation need. Do not keep searching indefinitely for a purchase fact that desk research cannot establish. Fixed link counts and candidate quotas are not stopping rules. The user can redirect or stop the work.

End with findings, reasons for recommendations, remaining uncertainties, searched and unexplored directions, why this round stopped, and the next useful choice or investigation. No external outreach, spending or live experiments are authorized by a scout run.

### Continue from both the run and the opportunity folders

The two records answer different questions: a run says **what we searched and compared then**; an opportunity folder says **what we currently know about this idea and why**.

- For “continue that search,” load the relevant saved report under `scouting-runs/` for the original brief, search directions, unfinished leads, access gaps and stopping point. Then read the linked opportunity summaries and relevant evidence before revising claims or comparing them again.
- For “continue this idea,” start with that idea's folder under `opportunities/`. Follow links to earlier runs when their discovery context or unfinished searches matter. Deeper investigation of a selected idea remains a separate skill invocation according to the agreed boundary.
- If the run or idea is genuinely ambiguous, ask which one. Use file references and saved state rather than relying on chat memory. Read relevant linked material progressively; every run need not load every opportunity folder.
- Recheck important facts whose age or changed circumstances matter. Preserve old reports as historical comparisons. If an opportunity changed after a run, use its newer findings and explain the change instead of restoring an obsolete conclusion. Preserve conflicts and trace conclusions to the underlying evidence.
- Save a new dated run report, update affected opportunity records and the derived `opportunities/comparison.md`, and show what changed or remains unreviewed, following the shared-record contract.

### Handoff and remaining work

The resource catalog is the source-selection asset; it is linked here rather than copied into the resolution. The suite blueprint will place that single maintained catalog where the implemented skills can reach it. Prototype and build tickets now point to the agreed depth, collaboration, stopping and continuation behavior. No new decision ticket is needed: existing blueprint, prototype, setup and build tickets cover the remaining work. This resolution does not implement either runtime skill or resolve those tickets.
