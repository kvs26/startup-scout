# Shared opportunity records

Read this guide when creating, resuming, or updating an opportunity or scouting report. These records carry work between scouting, investigation, and customer-connection preparation. Use the meanings in the root [glossary](../../CONTEXT.md). Templates below are writing aids, not forms the user must complete.

The root [skill map](../../SKILL-MAP.md) owns the current skill relationships, routing, next-step handoffs and maintenance rules when skills change. Keep the next plan in the existing run or opportunity record under that convention.

## Skill boundaries

The three startup skills produce business research, assessments, test plans, contact research, conversation preparation and their saved records. They do not create code, artwork, product prototypes, websites, apps or production automations. The user plans to create separate skills or automations for that work and personally handle conversations with people.

Treat the founder's AI production plan as context for evaluating ideas, feasibility, costs and learning needs. Recording that plan does not authorize implementation or establish that the production tools already exist. When a proposed test needs a sample or prototype, describe the required material and what the test should establish for the separate production workflow. Assess returned artifacts or results within the relevant startup skill's remit; keep proposed checks distinct from completed work.

## Founder profile

The root [FOUNDER-PROFILE.md](../../FOUNDER-PROFILE.md) is the shared source for the founder's background, skills, learning gaps, interests, time, budget, customer access and preferences. Read it at the start of scouting, investigation and customer-connection work. If absent, proceed with supplied information and explicit unknowns. An output-workspace override changes opportunity destinations, not this profile's location; use another profile only when the user supplies one.

Use the profile to tailor discovery, domain-learning explanations, cost assumptions, customer tests and conversation preparation. Keep business evidence in the opportunity records. A founder preference or capability changes fit, not evidence that customers will buy. The current explicit request governs the task; treat an alternative market or model for one task as task-specific unless the user makes it a lasting preference.

Automatically maintain the profile during interactions through these skills:

- Update it in the same turn when the user supplies a relevant new fact, correction, lasting preference, completed learning or experience, or when a concrete artifact demonstrates a relevant capability. Routine updates within this authorization need no repeated confirmation.
- Preserve the distinction between self-report, observed work, interest, plans and unassessed knowledge. Describe what a completed activity supports: studying a topic is not proof of reliable professional delivery, and publishing a site does not establish traffic or revenue. An AI-generated conclusion about the founder is not new evidence.
- Reuse recorded answers and ask only about material gaps. Keep ambiguous or conflicting information qualified; clarify consequential conflicts while continuing unaffected work. The latest clear correction updates the current field and leaves a short explanation of what changed.
- Immediately reread the profile before writing, merge newer additions, update its date and append a concise source/change note for material changes. Preserve dates, currencies, billing periods and the context of capability claims. Repeated answers or unchanged information require no new entry.
- Maintain one profile rather than copies inside opportunity folders or skill files. Save only background relevant to this startup work. Profile updates alone do not trigger rewriting existing opportunities, historical reports or unrelated files, and do not authorize external actions.

When profile information affects a recommendation, name the relevant requirement and fit or learning gap in everyday language. Carry the profile reference in handoffs instead of creating another current copy.

Profile changes use its short source/change notes. Dated opportunity rounds and history files below apply to changes in opportunity records.

## Find the same opportunity again

Keep each opportunity in `opportunities/<stable-name>/`, with its name and folder identity in `summary.md`. Search existing summaries before creating a folder. A price or feature revision stays in the same record. A different customer group or problem gets a linked sibling folder when it needs its own investigation; explain the relationship and retain each observation's original context.

When writing a summary or comparison's product explanation, follow [explaining ideas](explaining-ideas.md) and complete its comprehension check. Explain the business before the research findings; keep detailed evidence in its owning record.

Use readable Markdown and add files only when they contain useful work:

| Record | Location inside the opportunity | Template |
| --- | --- | --- |
| Self-contained current business explanation and assessment | `summary.md` | [Opportunity summary](templates/opportunity-summary.md) |
| Claims and original research | `research.md` | [Research](templates/research.md) |
| Inputs and calculations | `economics.md` | [Economics](templates/economics.md) |
| Proposed customer test | `tests/<test-id>.md` | [Customer test](templates/customer-test.md) |
| Supplied observations and artifacts | `results/<result-id>.md`, supporting files as needed | [Supplied result](templates/supplied-result.md) |
| Earlier outputs and explanation of changes | `rounds/<dated-round-id>.md` and `history.md` | [Round and history](templates/round-history.md) |
| Contacts and conversation preparation | `connections/<preparation-id>.md` | [Contact preparation](templates/contact-preparation.md) |

Keep one Markdown file per scout session/run, `scouting-runs/<run-id>.md`, using the [scouting report](../../.agents/skills/startup-idea-scout/assets/scouting-report.md). Include the index, full comparison, dated result, all assessments, source evidence, shared costs and resume notes in that file. The [idea assessment](../../.agents/skills/startup-idea-scout/assets/idea-assessment.md) is a repeatable section template, not a separate output file. Use temporary working storage if necessary and consolidate it into the run; persistent per-idea files, batch dossiers and sidecar research folders are outside this layout. A continuation updates the same run, preserving dated conclusions and appending material corrections. Older multi-file runs remain readable; consolidate them when requested, retaining evidence and repairing inbound links before removing superseded files.

The scout's [discovery guide](../../.agents/skills/startup-idea-scout/references/discovery.md) owns the minimum of 50 distinct deep assessments, completion audit and resumable counts; the one-file layout does not reduce that depth. Its [commercial guide](../../.agents/skills/startup-idea-scout/references/commercial-assessment.md#compare-the-researched-pool) owns comparison, the strongest recommendation with brief runners-up, and discussion options when none is recommended. An in-progress run is explicitly marked incomplete. The winning opportunity's separate handoff below remains required.

For a completed scout campaign, automatically promote only the strongest recommended idea into an opportunity folder with a self-contained `summary.md` and `research.md` linking its existing evidence. Reuse an existing folder for the same opportunity. Runners-up and fallback discussion options stay in scouting records unless the user selects one; if none is recommended or selected, create no opportunity folder. The opportunity summary explains the customer motive, offer, evidence, alternatives, delivery, costs, domain learning and founder fit on the page. A supplied idea can have its own record even with a negative verdict. A user can choose a discussion option without changing its evidence verdict or repeating the broad search.

Use `opportunities/comparison.md` and the [comparison template](templates/comparison.md) for an explicitly requested comparison of saved opportunity folders. The scout’s required campaign comparison stays in its run report and does not create or overwrite this separate current view. When later work changes an opportunity included in an existing comparison, update or qualify the affected entry. Planning tickets remain outside runtime records.

## Evidence has one home

Give claims, observations, tests, and results stable IDs within their opportunity, for example `C001`, `E001`, `T001`, and `R001`. Use an exact ID heading or an explicit stable anchor and link to that entry, including the file path. Retain IDs when wording changes; do not renumber old entries. Cross-opportunity references include the owning folder. At save time, check existing IDs before allocating a new one.

Store an observation once. A web account normally lives in `research.md` or, before promotion, inside its scouting run; a supplied customer result normally lives in its result file. Within a run, namespace explicit anchors by idea: `i001` for the assessment, `i001-e001` for its evidence and `i001-c001` for its claim. Use `shared-e001` for a genuinely shared observation. Link within the run with fragments such as `#i001-e001`; external records use `scouting-runs/<run-id>.md#i001-e001` relative to their destination. Repeated bare `#e001` anchors cannot identify fifty different observations. Preserve existing IDs when consolidating older runs and add the idea namespace to resolve collisions. On promotion or reuse, link to the original entry instead of copying it. Claim assessments, summaries, calculations, reports, and other opportunities refer to that original entry. A quotation, repost, follow-up article, or second summary is not another independent observation. Preserve original supplied files where permitted and link to them; a short finding derived from an artifact is not a second copy of the artifact.

For each observation retain:

- Origin: source URL or supplied artifact, author or participant where known, and what was actually observed or reported. Separate user reports, supporting material, advertised capabilities, and direct observations.
- Relevant customer, role, country/market, and circumstances. A person's job title alone does not establish purchasing authority.
- Observation/event date, publication date when useful, and retrieval/receipt date separately. Use `unknown` when a date is unknown; today's retrieval does not date the original event.
- Related claim/test, support and contrary implications, limitations, and any dependence on another account or event.
- Original currency, unit, billing period, and geography for numbers. Retain the original amount and the dated rate/source for any conversion.

Assess confidence for a particular claim, explaining its basis and limits. Keep assumptions explicit. Problem reports, interest, purchase, use, and continued value support different claims; a planned test or draft supports none of them as a completed customer result. User selection or rejection records a choice and its stated reason, not demand evidence.

Recheck an old claim when its age or changed circumstances matter to the next decision. Record a failed recheck as a current limitation while retaining the old evidence and its dates. There is no universal expiry period. Keep these research states distinct: **not performed**, **access failed**, **completed with no relevant results**, and **completed with findings**. None of the first three alone proves absent demand. Search history belongs in its run/round; link to it from research rather than copying it.

## Resume and accept results

The user may supply a file or paste findings with an opportunity name/path. Resolve that reference and load the current summary, relevant detail, history, and outstanding tests. Ask which opportunity only when identity is ambiguous. Saved records, rather than earlier chat, provide the context.

Preserve the submitted notes and any supplied artifacts. Record who supplied them and when; distinguish their account from what an attached artifact independently shows. Connect the result to the customer, event, test, and claim where possible. Ask only about gaps that materially affect interpretation; an incomplete submission can still be saved.

Check for a prior result using the original event, source/artifact, customer/test, date, and content. A repeated submission links to the existing result and adds only new provenance or receipt history. If identity is uncertain, mark possible duplication and avoid counting it as independent evidence. A correction links both accounts and explains what changed. A genuinely new event from the same customer can add evidence without becoming another independent customer.

Reassess affected claims against both supporting and conflicting entries. Explain which conclusions changed, stayed the same, or remain uncertain. Save changed calculations/tests and the next useful step. Customer-connect returns actual replies or meeting notes through this same path; the investigator reassesses the business claims.

## Preserve history and concurrent work

Use ISO dates (`YYYY-MM-DD`) and include the time and time zone when ordering matters. A dated run/round filename may use `YYYY-MM-DD-short-topic`, with an unused suffix for another round that day. Distinguish when a finding was assessed from when the record was edited.

Before changing a current view, preserve its earlier output in a dated round unless an existing saved round already contains it. A saved round records the proposition, findings, recommendation, user choice, and limitations at that time, with stable evidence links. When changing calculations or test plans, retain the earlier inputs/results or test procedure and interpretation criteria in that round or a linked versioned artifact. Links to mutable current files alone do not preserve earlier conclusions or designs. Append a short `history.md` entry explaining what changed, why, and the responsible evidence/round links. Keep completed reports and earlier accounts; append a linked correction rather than silently replacing their history. An explicit request to delete records overrides this preservation convention within the requested scope; remove obsolete references without recreating the deleted material as a new archive.

Immediately before writing, reread each destination and any current findings used to derive it. Merge changes made since the initial read, preserve unrelated additions, and check IDs/filenames again. If an overlapping change cannot be reconciled, save the new detail separately and ask about the specific conflict rather than overwrite it. A stale full-file rewrite can erase another session's work.

For continuation, use the saved scouting report for its brief, searches, coverage, and unfinished work; use the opportunity's current record for its latest findings and user decision. An old run never restores a superseded proposition or selection. Recompute affected summaries from the merged current findings before saving.

## Current comparison and handoffs

When a comparison is requested, date `opportunities/comparison.md` and make it understandable on its own: explain each saved product and an illustrative use, compare the same business questions, then directly explain the relative recommendation and what could change it. Show important doubts, contrary evidence, access failures, and unfinished work on the page. Keep detailed source entries and calculations in linked records. There is no automatic selection, overall startup score, or unsupported profit/cost ranking. A request to compare named saved opportunities does not itself authorize a new discovery campaign; the scout’s open-discovery campaign separately includes its required research and comparison.

When one opportunity changes, update its affected overview content and explain whether the others were reassessed. Retain the last comparison date where useful; mark older/unreviewed findings. A partial update is not a new full comparison. Keep earlier scouting reports available as historical views.

A scout handoff links the current opportunity summary and relevant run, identifies the current proposition, evidence and contrary findings, business requirements, and unfinished investigation. Carry the chosen search priority, starting model and separate scale hypothesis so later investigation preserves the reason for the recommendation. Keep the user's explicit selection separate from the scout's recommendation. An investigator handoff adds the current offer and selected test plan; customer-connect adds sourced contact routes and preparation. No handoff implies permission to send messages, purchase anything, or run a live test.

## Use the templates

Read only the templates needed for the task. Adapt their sections to useful work and leave important unknowns visible. `{{...}}` denotes text or a link destination to replace when creating a record; it is not a working link in the template package. Resolve generated links relative to the saved record's destination and check that each target exists. Keep links between saved records inside the output workspace so copying it preserves the handoff; when paths use symlinks, normalize both link source and target consistently before computing relative paths. Remove template instructions and unused optional sections from the output. Do not create empty opportunity records merely to fill the directory layout.
