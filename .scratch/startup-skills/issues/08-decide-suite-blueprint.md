# Agree the startup skill suite blueprint

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:grilling
Type: grilling
Mode: HITL
Status: resolved
Assignee: Codex
Blocked by: 05, 06, 07, 12, 15

## Question

Which distinct skills and shared resources form the smallest coherent suite for the agreed discovery, validation, customer, business-model, costing, marketing, and sales decisions, and how do they compose?

For each proposed skill, agree its invocation, inputs, decision or output, required evidence, human contribution, and handoff. Identify overlap and combine responsibilities when separate invocation would add no value. State what is fully specified, what research gaps remain, and what must be carried into the future infrastructure and first-customer maps.

Include the separate skill requested on 2026-10-02 for ideas the user chooses to advance after investigation: find relevant contacts, draft emails and other material for connecting with people, and help the user communicate and negotiate for that specific idea and offer. Agree its name, how it receives the investigation's findings and customer-test plans, what it prepares for learning conversations versus sales, and whether implementing it belongs to this map or a later effort. The request establishes a distinct capability; it does not authorize sending messages, purchases, or live experiments. Use the commercial-coverage ticket's final answer for the agreed handoff rather than duplicating it here.

Make the supporting resources explicit for the scout and investigator: selected source families and reference guidance, useful templates, reusable parts of the old scripts, and any justified new scripts or integrations. Follow the source-selection decision in [Decide how the scout discovers and compares open opportunities](07-decide-scout-workflow.md), including evaluation of YC and other candidate resources requested by the user. Record each resource's purpose, relevant limits, access requirements, and whether ordinary browsing is sufficient or repeatable work warrants automation. Do not assume the old source list is sufficient for this scope or require a new script for every source. Additional resource choices remain open until evaluated.

Package the [Scout starting resources](../../../docs/startup-skills/source-catalog.md) as one shared reference reachable from the implemented scout and useful to the investigator. The workflow ticket owns the initial source selection; this blueprint owns its runtime location and skill pointers. Preserve one maintained catalog when moving it into runtime resources, updating planning links instead of creating diverging copies. Agents consult it when choosing research sources and extend beyond it when the customer, problem or market calls for other sources. Using a listed public source does not select an API, MCP server or installation.

Evaluate the findings in [Research reusable startup tools, MCP servers, and discovery resources](12-research-reusable-startup-toolkit.md) before choosing tools to adopt. Different skills may use different tools; a shared record guide and templates standardize their saved work without imposing one common toolkit. Distinguish using a resource through ordinary browsing from installing or depending on its API/MCP server.

For each adopted tool, identify whether setup is required for the scout, investigator, or customer-connect skill or is optional. Hand those choices to [Guide and verify the selected tool setup](13-guide-tool-setup.md), which owns manual setup guidance, execution of individual steps delegated by the user, connection checks, and the short root-level `SETUP.md` summary before the skill build tasks.

Preserve the [confirmed independent-discovery requirement](07-decide-scout-workflow.md#confirmed-discovery-requirement): idea lists supplement direct web and public-forum investigation. Resource selection must support discovering customer problems beyond listed ideas, not turn the scout into a curated-list summarizer.

Make the [agreed investigation loop](05-decide-commercial-coverage.md#investigation-is-a-repeatable-loop-with-saved-work) explicit in the investigation skill's instructions: start or resume an opportunity, load saved work, accept returned customer results, update findings with a record of what changed, and propose the next useful step. Define when a round stops to await customer results and how the customer-connection skill hands those results back. Follow the shared-records decision for storage; chat memory alone is insufficient.

Record the blueprint in this ticket's answer as the canonical planning artifact. It must be actionable enough to implement the remaining skills later. All three skills, `startup-idea-scout`, `startup-opportunity-investigator`, and `startup-customer-connect`, are required implementations in this map following the user's 2026-10-03 scope expansion. Explicitly define the investigation skill's name, research depth, stopping point, detailed relationship to customer validation, and handoff from the scout, preserving the customer-test planning responsibility agreed in [Decide what scouting establishes and what remains untested](04-decide-scout-boundary.md). Consult grilling and domain-modeling; do not resolve material unknowns by inventing the user's preferences.

## Comments

### 2026-10-03 — Blueprint discussion started

Claimed after checking that all blocking decisions are resolved. Using grilling and domain-modeling for the live discussion; a supporting subagent is reviewing existing source/tool findings without adopting tools or modifying tickets.

First-round proposals, awaiting the user's answers:

- Organize the initial suite as `startup-idea-scout`, `startup-opportunity-investigator`, and `startup-customer-connect`. Keep customer validation, business model, costs, and marketing/sales planning inside the investigator, with contact research, communication materials, and negotiation preparation in customer connection. Separate skills for individual commercial topics are not yet proposed.
- Implement the already required scout and investigator in this map; specify customer connection fully here and implement it in the later first-customer effort, unless the user chooses to expand this map's implementation scope.
- Allow the investigator to start directly from a user-supplied idea as well as a scout candidate, creating the same opportunity record and identifying missing initial evidence without requiring a scouting run first.

These are proposals, not resolutions. After the user's answers, finish the detailed skill contracts, investigator depth and stopping behavior, customer-connection outputs and return path, shared resource/template packaging, and tool selection/setup handoff. Preserve prior agreed scope, evidence standards, saved-work rules, and user-owned decisions.

### 2026-10-03 — Three skills and implementation scope agreed

The user accepted the three-skill division and names: `startup-idea-scout`, `startup-opportunity-investigator`, and `startup-customer-connect`. The investigator owns customer validation, business model, costs, and marketing/sales planning; customer connection owns contact research, communication materials, conversation preparation, and negotiation preparation.

The user explicitly rejected deferring customer-connect implementation: all three skills must be built and behaviorally checked within this map. The destination and execution override now reflect that instruction, and [Build and verify startup customer connect](14-build-startup-customer-connect.md) tracks the additional implementation. Actual outreach and customer acquisition remain outside this map.

The user accepted direct investigator entry from their own idea, as well as from a scout candidate. It must create or resume the same durable opportunity record, identify missing initial evidence, and research it without requiring a prior scouting run.

The supporting local review found no established need for a new integration or direct reuse of legacy scripts. Existing source selections remain agreed; runtime packaging and tool adoption still await the blueprint discussion. The review did not install tools or freshly verify external capabilities.

### 2026-10-03 — Next blueprint choices proposed

Awaiting the user's answers:

- Give the investigator a full view across the agreed business questions, but prepare detailed customer tests for the few uncertainties most likely to change the next decision. Each actionable plan includes target participants, questions or procedure, material to show where relevant, what to record, and how to interpret results. Pause a round when the next material evidence needs customer participation; resume from saved results. Do not invent universal sample sizes or success thresholds.
- Let customer-connect prepare only what the current request needs: sourced contacts and access routes, tailored messages and follow-ups, learning-conversation questions, sales explanations or a short offer document, meeting preparation, and negotiation practice. Infer learning versus sales from the request and saved work; clarify ambiguity. Save preparation and supplied actual results separately, with actual results returned through the shared investigator intake.
- Use existing search/page reading and local file tools as the required baseline, with interactive browsing as needed. Add an extra retrieval/research integration only when a concrete task demonstrates a gap; do not require a new MCP server or legacy script initially. Tool-setup verification still belongs to its own task.

A fresh basic access check in this session returned web search results for practitioner reconciliation discussions and read [YC Requests for Startups](https://www.ycombinator.com/rfs). This is limited evidence that existing search/page retrieval is available, not proof of universal site access, comprehensive crawling, or completion of setup checks.

### 2026-10-03 — Focused tests agreed; contact sources and tools need investigation

The user accepted the proposed investigator depth and focused customer-test preparation: research all agreed business areas, prepare detailed tests around the uncertainties most likely to change the next decision, and pause/resume around needed customer evidence.

The user responded positively to customer-connect preparing materials for the immediate task, but asked how it will find real contacts, whether LinkedIn and other sources need APIs, and how sources change with the idea and market. [Research customer contact sources and access across markets](15-research-customer-contact-sources.md) now supplies that missing evidence before this part of the blueprint is settled.

Superseded interpretation: the agent initially treated the India comment as a starting-market preference. The user subsequently removed that preference explicitly. There is no fixed market preference; choose markets according to each opportunity and the user's direction, including India, the US, other developed markets, and other relevant markets.

The user did not accept the no-new-tools recommendation: they think additional tools may be needed and asked whether setup belongs to [Guide and verify the selected tool setup](13-guide-tool-setup.md). Clarified that the blueprint chooses tools and required/optional use; the setup task performs manual-first setup and verification. No provider, API, or paid plan has yet been selected.

### 2026-10-03 — Retrieval-tool documentation rechecked

Current official documentation confirms two candidates from the earlier toolkit research:

- [Tavily MCP](https://github.com/tavily-ai/tavily-mcp) exposes search, extraction, site mapping, and crawling through a remote connection using an API key or supported account sign-in. Its [credit documentation](https://docs.tavily.com/documentation/api-credits) currently lists 1,000 free monthly credits without a credit card, with different consumption for search/extraction/crawl and separate paid options. This makes a bounded setup trial possible; it does not establish sufficiency for recurring deep research or access to private contact data.
- [Firecrawl MCP](https://docs.firecrawl.dev/mcp-server/keyless) documents rate-limited keyless search, scraping, and parsing. Higher limits and the full tool surface depend on an API key/account access and plan/deployment. It overlaps Tavily in retrieval; documentation alone does not justify requiring both.

These checks read documentation only. No service was connected, credit used through its API, or paid plan selected. A retrieval connection and a contact-data service solve different tasks. The pending contact-source research will inform the latter choice. Proposed tooling must preserve ordinary browsing fallbacks and distinguish vendor-supplied or inferred contact information from first-party published details.

### 2026-10-03 — Contact research complete; proposed adoption awaiting user

[Research customer contact sources and access across markets](15-research-customer-contact-sources.md#answer) is resolved and is the canonical source for checked contact-resource facts and limits. It does not resolve this human decision.

Propose an opportunity-specific contact workflow with no default country: choose the customer segment/location and relevant role; find suitable organizations through company sites, local discovery or relevant industry/event directories; identify people through published roles, human LinkedIn use or an appropriate licensed service; find and assess an actual business contact route; retain sources, dates, uncertainty, and organizational fallbacks. For consumer ideas, use suitable community/recruitment routes instead of forcing a business-contact database.

Propose selecting Tavily for a search/extraction/crawl connection and Hunter for a first business-email lookup/verification trial in the setup task. Keep Apollo as a candidate when filtered person/role discovery is the demonstrated missing capability; do not install overlapping tools by default. LinkedIn/Sales Navigator is a human account route unless approved API access is established. Google Places API is a possible later local-discovery integration, not an assumed permanent prospect-data source. These proposals await the user's response; no provider or paid plan is adopted yet.

For any selected contact service, setup must check actual account eligibility and credit costs plus a small authorized sample relevant to the selected market and customer segment, retaining fallback routes if coverage is poor. A successful connection alone does not establish useful contact coverage or accuracy. Shared runtime guidance must carry these source-selection and saved-data rules alongside the existing common evidence/handoff guide.

### 2026-10-03 — Market correction and tool clarification

The user explicitly removed the inferred India-first preference. Market choice depends on the idea, with the US and other developed markets among the relevant possibilities for SaaS/technology. All eligible industries remain open; healthcare examples must not become a sector restriction. The contact-source research and map now reflect this correction.

The user asked whether customer-connect implementation should depend on the contact-source research. It already did transitively through this blueprint; a direct blocking edge has also been added to make the research prerequisite visible.

The user requested short explanations of Tavily and Hunter and questioned whether Apollo was healthcare-specific. Apollo here means `apollo.io`, the cross-industry business-contact service, not a healthcare-specific selection. It remains an evaluated candidate, not an adopted dependency. Tavily/Hunter adoption remains pending; requests for explanations do not constitute acceptance.

### 2026-10-03 — User requested completion and settled tool direction

After discussing Tavily and its free allowance, the user reported creating a Tavily account and asked to finish this ticket. They also requested adding Hunter and Apollo if their relevant capabilities are free, with those checks and setup handled in the setup task. This supersedes the earlier pending tool proposals: Tavily is selected; Hunter and Apollo are conditionally included under the free-only rule below. Account creation is user-reported, not an independently verified connection. No paid plan, automatic paid overage, installation, or outreach has been authorized by this resolution.

## Answer

Resolved 2026-10-03 through the live discussion and the user's explicit request to finish. This is the canonical suite blueprint. The earlier comments retain the discussion history; this answer states the final design and supersedes pending proposals. Packaging and template names below are routine implementation choices under the agreed shared-record contract.

### Suite, scope, and ownership

Build and behaviorally check all three skills in this map, under `.agents/skills/<skill-name>/`. They serve software, AI, and similar technology opportunities across any industry. There is **no fixed market preference**. Choose markets according to the idea, evidence, and user direction; India, the US, other developed markets, and other relevant markets remain eligible. Clinic and manufacturing examples are illustrations, not industry restrictions. SaaS is one possible business format.

| Skill and invocation example | Inputs | Output and decision supported | Human contribution and handoff |
| --- | --- | --- | --- |
| `startup-idea-scout` — “Find technology opportunities” / “Explore this problem” / “Continue this search” | Optional idea, problem, market, constraints, or prior run; otherwise an open brief | Substantial initial research, a sourced comparison, important doubts, and recommendations about what deserves investigation | User guides scope when needed and chooses an opportunity. Hand its saved record and relevant run context to the investigator. |
| `startup-opportunity-investigator` — “Investigate this opportunity” / “Continue this idea with these results” | A chosen scout candidate **or a user-supplied idea**, plus any new notes/files and constraints | Deeper business findings, grounded calculations, recommendation to keep exploring/change/leave, and focused customer-test plans | User supplies relevant context, chooses next steps, and later returns real results. Hand selected tests and the current offer to customer-connect. |
| `startup-customer-connect` — “Help me find people to learn from about this idea” / “Prepare this sales meeting” / “Help negotiate this pilot” | The opportunity reference, current findings/offer, relevant tests, and immediate conversation goal; optionally existing contacts or correspondence | Sourced contact routes and task-specific messages, questions, offer material, meeting preparation, or negotiation practice | User supplies relationship context and their own acceptable terms, chooses whether to act, and brings back replies/notes. Hand actual results back to the investigator through the shared record. |

The investigator owns customer validation, pricing/business model, costs, customer access, marketing routes, and sales-process planning. Customer-connect applies that work to particular people and conversations. No separate validation, finance, marketing, or sales skill is required for this version. Scouting finds and compares opportunities; selecting one does not establish demand. No skill treats research, drafts, role-play, or planned tests as observed customer results.

### Scout contract

Implement the full [scout workflow](07-decide-scout-workflow.md#answer), [scout boundary](04-decide-scout-boundary.md#answer), and [shared records](06-decide-shared-records.md#answer). Those tickets remain the owners of their detailed decisions.

The scout follows a supplied direction and explores nearby possibilities without replacing the brief; an open request starts varied independent problem searches. Balanced effort means substantial follow-up, not one or two links. Follow original accounts and replies, alternatives, workarounds, contrary evidence, possible payer, access routes, and material delivery/cost requirements. Curated lists and YC prompts supplement independent web/forum discovery. Confidence belongs to individual claims; neither a universal score nor a candidate/link quota is a completion rule.

Stop when a useful comparison is supported and relevant follow-up mainly repeats findings, or save an explicitly incomplete round when access, time, or missing customer evidence prevents completion. Give progress updates and ask useful scope questions. Continuation reads the saved run for search history and opportunity records for current findings; old reports never override newer research. Save the dated run and update the linked current comparison. Presentation is refined by [Try the scout output before implementing the skill](09-prototype-scout-output.md).

### Investigator contract and stopping point

Start from the supplied opportunity name/path and load its current summary, linked evidence, prior conclusions, calculations, and outstanding tests. A direct idea starts the same record without requiring the scout to run first; missing initial evidence becomes investigation work. Ask only when identity or scope is materially ambiguous.

Investigate all areas in the [commercial-coverage decision](05-decide-commercial-coverage.md#answer): customer problem; user, payer, and purchasing authority; existing alternatives and reasons to switch; offer/pricing/payment terms; startup and recurring costs, cash timing and founder effort; customer-access and marketing routes; buying process; onboarding and continuing value; and technical/data/operating dependencies. Research depth follows decision importance: use original sources, check material contradictions and changing facts, and explain which unanswered questions can change the next step. Do not fill headings with invented facts or turn this into an exhaustive business encyclopedia.

Competitor prices and supplier costs require relevant sources and market/date/currency/units. Calculations expose sourced, user-supplied, and hypothetical inputs, with useful ranges or alternative cases where justified. Competitor prices do not establish willingness to pay for this offer, and simulated revenue is not a forecast. Unknowns remain unknown.

Prepare detailed customer tests for the few uncertainties most likely to change the next decision. Each plan identifies the claim, relevant participants, questions or procedure, any material to show, what to record, interpretation of possible results, and known effort/cost. Match the test to the claim: a positive conversation cannot establish purchase or repeated use. Choose meaningful decision criteria for that test; do not invent universal sample sizes or pass thresholds.

A normal round ends with a usable current view, reasons for the recommendation, and the next focused test or investigation. Stop to await customer evidence when that evidence is necessary; keep researching a consequential desk-research question while accessible follow-up is still useful. Save incomplete work with its blocker instead of falsely claiming completion. The user decides whether to continue, revise, or leave the opportunity.

On return, accept either a supplied file or pasted results with the opportunity reference. Preserve original notes/artifacts; distinguish user reports from supporting material; identify repeated events so re-submission is not extra evidence; retain contradictions and corrections. Update affected claims, calculations, tests and recommendations, explain what changed, preserve earlier outputs, and refresh or qualify the affected comparison entry. Follow the existing [repeat-investigation agreement](05-decide-commercial-coverage.md#investigation-is-a-repeatable-loop-with-saved-work) and shared-record intake rules.

### Customer-connect contract

Read the opportunity's current work before finding people or drafting material. Infer whether the immediate task is learning, sales preparation, or negotiation from the request and records; clarify when that difference materially changes the work. It need not generate every possible artifact on each invocation. If key customer/offer/test decisions are missing, make the gap explicit and hand that question to the investigator rather than silently inventing the business.

Use the approach and access limits established by [contact-source research](15-research-customer-contact-sources.md#answer):

1. Identify a suitable market, customer segment, and role for this idea. Distinguish users, influencers, and buyers; a job title alone is not proof of purchasing authority.
2. Find relevant organizations using their own websites, market-specific directories, local discovery, associations, or events. Source choice follows the idea; checked Indian directory examples are not a worldwide catalog or a preferred-market rule.
3. Identify people through published roles, user-provided relationships, human LinkedIn use, or a supported contact service. For consumer ideas, appropriate communities, organizers, and voluntary research recruitment may be more useful than business databases.
4. Find an evidenced business contact route. Use a named professional email where supported; otherwise offer a company inbox, enquiry form, published business phone, or possible introduction. Do not fabricate addresses or claim access to private profiles.
5. Save why the organization/person fits, source and check date, role uncertainty, route, verification state, and whether details are public, vendor-supplied, inferred, or unknown. Preserve applicable storage limits. Deliverability is distinct from buyer fit or willingness to speak.

For learning, prepare an introduction, suitable follow-up, conversation questions based on the selected tests, and a way to record actual observations. For sales, prepare tailored messages, a plain explanation of the offer, supporting one-page material where useful, a meeting outline, objections to explore, and negotiation practice. Use the user's actual offer and terms; label proposed concessions and ask for material missing limits rather than making commitments. Role-play and suggested responses remain simulated material.

Stop when the requested preparation is usable or a named gap requires user input, access, or real results. Save work in the opportunity folder so another session can continue. Actual replies/meeting notes use the common result-intake path; the investigator reassesses the business claims. This map builds preparation capabilities; it does not send messages, run campaigns, purchase data, or execute live startup tests.

### Shared runtime resources and templates

Use one shared runtime directory, `docs/startup-skills/`, referenced explicitly from each skill. The scout build creates the common resources; later builds extend them without making separate copies. Runtime files are created in the build tasks, not by closing this planning ticket.

| Runtime resource | Contents and ownership |
| --- | --- |
| `record-guide.md` | The implementation of the shared-record/handoff contract: identity, evidence references, dates/context, intake/deduplication, uncertainty, history, summaries, and concurrent read-before-update discipline. |
| `source-catalog.md` | Move the single existing [scout catalog](../../../docs/startup-skills/source-catalog.md) here during the scout build, fix its relative links and every planning/runtime pointer, and retain only this maintained catalog. Include a distinct contact-source section drawn from the contact research; preserve purpose, limits, access requirements/check date, and browse-versus-API distinctions. |
| `research-guide.md` | Compact guidance grounded in the resolved evidence/commercial/workflow tickets: original-source checks, claim-specific support, opposing evidence, customer-test design, and calculations with explicit assumptions. Link selected method sources; do not duplicate the whole planning history. |
| `tools.md` | Tool selection/routing, setup reference, free-use limits, access failure handling, and public/vendor/inferred contact distinctions. Link root `SETUP.md` for actual configured status; do not store credentials or assume an account is a working connection. |
| `templates/` | Simple Markdown templates for an opportunity summary, research/evidence, economics, customer-test plan, supplied result, dated round/history, contact/preparation record, scouting report, and current comparison. Create only when useful; a template is not a strict form required from the user. |

Use root `CONTEXT.md` as the sole short glossary. The shared guide and templates must use its meanings.

The runtime layout implements [the existing storage decision](06-decide-shared-records.md#answer): `opportunities/<stable-name>/` contains `summary.md`, linked research/economics, test/result records, customer-connection preparation, and dated rounds/history. Use stable evidence/test/result references; save each observation once and link to it. A `history.md` entry states what changed and why, and dated rounds preserve previous outputs. Distinct customer/problem investigations get linked sibling folders; price/features can change within one opportunity. Files and subfolders are added as needed, without empty scaffolding for nonexistent ideas.

Save cross-opportunity runs under `scouting-runs/` and the derived current overview in `opportunities/comparison.md`. The output prototype may refine the scout presentation; it must preserve evidence identity and the common saved-record rules. Packaged runtime instructions must be usable without reading all planning tickets or relying on chat memory.

### Sources, tools, and setup handoff

**2026-10-06 update:** the user deferred Tavily and authorized completing the scout with verified existing web tools. [Build and verify startup idea scout](10-build-startup-idea-scout.md#answer) records the resolution; root [TODO.md](../../../TODO.md) retains the Tavily follow-up. This supersedes the Tavily setup prerequisite for that build without claiming a working connection.

The [source catalog](../../../docs/startup-skills/source-catalog.md) remains the canonical selected starting-source list until its build-time move. It covers practitioner discussions/reviews; supplementary YC and maintained idea prompts; startup-method guidance; official market/procurement context; and first-party product/supplier information. Read beyond the catalog whenever the market or question warrants it. Lists and advice are not demand evidence. Choosing a website does not install its API.

| Tool or capability | Decision for this version | Setup and limits |
| --- | --- | --- |
| Existing search, page reading, local files; interactive browsing when needed | Required basic capabilities for all three skills; retained alongside Tavily | Verify in the actual environment. Source/login failures remain explicit gaps; no claim of comprehensive crawling. |
| Tavily | Selected search/extraction/crawl integration, required setup for scout/investigator and reusable for customer-connect research | User reports account created. Connect and check supported operations through the official MCP route where available; verify with small public-page tasks. Start within the free allowance discussed; no paid upgrade/overage is authorized. Account and key/connection readiness are separate facts. |
| Hunter | Include if relevant lookup/verification features are available free; primarily customer-connect | Setup must check actual free account access, usable API/MCP route, quotas and credit costs. Connect the free capability if available; otherwise record the limit and defer the paid portion. Do not block the whole suite on a paid feature. |
| Apollo.io | Include if relevant company/person search or contact enrichment is available free; primarily customer-connect | Setup must distinguish free people search from email/phone enrichment, verify account/endpoint eligibility and included credits, and enable only usable free capabilities. Do not assume a free account unlocks all endpoints or contact details. |
| LinkedIn / Sales Navigator | Optional human-assisted research route; no required subscription or automation integration | Use the contact research's access limits. No general people-search API is assumed and no scraping dependency is selected. |
| Firecrawl, Crawl4AI, extra browser servers, GPT Researcher | Deferred alternatives, not required setup | The toolkit research found overlap or additional operational cost; revisit only for a demonstrated retrieval/research gap. No integrated third-party startup agent replaces the agreed saved-record workflow. |
| Google Places API, paid directories, CRM/outreach services | Not required for this version | Use relevant accessible sources; any later integration must address its actual need, access/cost and saved-data constraints. |

Documentation checked during this decision: [Tavily MCP](https://github.com/tavily-ai/tavily-mcp) and [credits](https://docs.tavily.com/documentation/api-credits) describe the chosen retrieval connection and free allowance; [Hunter pricing](https://hunter.io/pricing) currently advertises a free plan, but usable account/API capabilities still need checking; [Apollo developer FAQ](https://docs.apollo.io/docs/developer-faqs) and [People Search](https://docs.apollo.io/reference/people-api-search) describe plan-dependent access and the distinction between search and contact enrichment. Do not hard-code remembered quotas as enduring guarantees. None of these documentation checks establishes runtime quality or market coverage.

[Guide and verify the selected tool setup](13-guide-tool-setup.md) owns manual-first guidance, user-delegated individual steps, credential configuration, bounded free capability checks, remaining limits, and the short root `SETUP.md`. For a contact service, use a small suitable sample to check relevance and usable routes as well as connectivity, within allowed free usage; preserve source/storage distinctions. Tool setup does not send messages. If quota/access is unavailable, record the actual failure and use public-source fallbacks; paid-only Hunter/Apollo features can be explicitly deferred under this conditional decision. Tavily setup remains required unless the user later changes that selection.

No legacy script is adopted directly. Retain useful practices from the [legacy assessment](01-assess-legacy-references.md), such as traceable evidence and explicit cost assumptions, while avoiding its source, geography, caching/failure-state and business-model restrictions. No new crawler or script per source is required. Prefer official connections; if setup proves a small adapter necessary for a selected free capability, keep it narrowly scoped, preserve provenance/failure states, and exercise it during implementation.

### Implementation checks and remaining work

The existing build tickets own structural validation and independent behavioral checks. Across the suite, cover different industries and markets without a default-country filter; sparse and contrary evidence; unavailable sources/tools; actual original-source discovery; scout-to-investigator handoff; direct idea entry; and cross-session continuation with duplicate/conflicting results. Customer-connect additionally checks learning versus sales material, missing named contacts, vendor/inferred details, and return of actual results without treating drafts as evidence. Use isolated records and simulated fixtures for behavioral checks rather than real outreach.

Work is assigned as follows:

- [Guide and verify the selected tool setup](13-guide-tool-setup.md): selected/conditional connections and `SETUP.md`.
- [Try the scout output before implementing the skill](09-prototype-scout-output.md): readable output presentation.
- [Build and verify startup idea scout](10-build-startup-idea-scout.md): scout and initial shared runtime resources/catalog move.
- [Build and verify the opportunity investigation skill](11-build-opportunity-investigation.md): deeper research, direct entry, focused tests, and saved-result loop.
- [Build and verify startup customer connect](14-build-startup-customer-connect.md): contact discovery, task-specific preparation, and the return handoff. Its direct contact-research dependency is retained.

No unresolved design decision requires another ticket to close this blueprint. Account-specific free access, tool quality, and market-specific contact coverage remain verification work in setup or actual opportunity runs, not assumed findings. Additional adapters or specialist sources can be raised when a concrete gap appears. The map remains open until all three required skills are built and checked.

Future infrastructure work receives the selected customer outcome, delivery requirements/dependencies, sourced cost inputs, and unresolved feasibility questions. Future first-customer work receives the current offer, market/customer/buyer findings, contact routes, communication material, customer tests and actual results available at that time. Those later efforts own product construction and actual acquisition; this blueprint does not claim either has happened.
