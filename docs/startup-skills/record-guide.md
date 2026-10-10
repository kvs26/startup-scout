# Shared opportunity records

Read this guide when creating, resuming, or updating an opportunity or scouting report. These records carry work between scouting, investigation, and customer-connection preparation. Use the meanings in the root [glossary](../../CONTEXT.md). Templates below are writing aids, not forms the user must complete.

## Find the same opportunity again

Keep each opportunity in `opportunities/<stable-name>/`, with its name and folder identity in `summary.md`. Search existing summaries before creating a folder. A price or feature revision stays in the same record. A different customer group or problem gets a linked sibling folder when it needs its own investigation; explain the relationship and retain each observation's original context.

Use readable Markdown and add files only when they contain useful work:

| Record | Location inside the opportunity | Template |
| --- | --- | --- |
| Short current view | `summary.md` | [Opportunity summary](templates/opportunity-summary.md) |
| Claims and original research | `research.md` | [Research](templates/research.md) |
| Inputs and calculations | `economics.md` | [Economics](templates/economics.md) |
| Proposed customer test | `tests/<test-id>.md` | [Customer test](templates/customer-test.md) |
| Supplied observations and artifacts | `results/<result-id>.md`, supporting files as needed | [Supplied result](templates/supplied-result.md) |
| Earlier outputs and explanation of changes | `rounds/<dated-round-id>.md` and `history.md` | [Round and history](templates/round-history.md) |
| Contacts and conversation preparation | `connections/<preparation-id>.md` | [Contact preparation](templates/contact-preparation.md) |

Keep cross-opportunity reports in `scouting-runs/<dated-run-id>.md`, using the [scouting report](templates/scouting-report.md). Keep the short current overview at `opportunities/comparison.md`, using the [comparison](templates/comparison.md). Planning tickets remain outside runtime records.

## Evidence has one home

Give claims, observations, tests, and results stable IDs within their opportunity, for example `C001`, `E001`, `T001`, and `R001`. Use an exact ID heading or an explicit stable anchor and link to that entry, including the file path. Retain IDs when wording changes; do not renumber old entries. Cross-opportunity references include the owning folder. At save time, check existing IDs before allocating a new one.

Store an observation once. A web account normally lives in `research.md`; a supplied customer result normally lives in its result file. Claim assessments, summaries, calculations, reports, and other opportunities refer to that original entry. A quotation, repost, follow-up article, or second summary is not another independent observation. Preserve original supplied files where permitted and link to them; a short finding derived from an artifact is not a second copy of the artifact.

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

Before changing a current view, preserve its earlier output in a dated round unless an existing saved round already contains it. A saved round records the proposition, findings, recommendation, user choice, and limitations at that time, with stable evidence links. When changing calculations or test plans, retain the earlier inputs/results or test procedure and interpretation criteria in that round or a linked versioned artifact. Links to mutable current files alone do not preserve earlier conclusions or designs. Append a short `history.md` entry explaining what changed, why, and the responsible evidence/round links. Keep completed reports and earlier accounts; append a linked correction rather than silently replacing their history.

Immediately before writing, reread each destination and any current findings used to derive it. Merge changes made since the initial read, preserve unrelated additions, and check IDs/filenames again. If an overlapping change cannot be reconciled, save the new detail separately and ask about the specific conflict rather than overwrite it. A stale full-file rewrite can erase another session's work.

For continuation, use the saved scouting report for its brief, searches, coverage, and unfinished work; use the opportunity's current record for its latest findings and user decision. An old run never restores a superseded proposition or selection. Recompute affected summaries from the merged current findings before saving.

## Current comparison and handoffs

Date `opportunities/comparison.md` and make it understandable on its own: explain each product and an illustrative use, compare the same business questions, then directly explain the relative recommendation and what could change it. Show important doubts, contrary evidence, access failures, and unfinished work on the page. Keep detailed source entries and calculations in linked records. There is no automatic selection, overall startup score, fixed number of candidates, or unsupported profit/cost ranking.

When one opportunity changes, update its affected overview content and explain whether the others were reassessed. Retain the last comparison date where useful; mark older/unreviewed findings. A partial update is not a new full comparison. Keep earlier scouting reports available as historical views.

A scout handoff links the current opportunity summary and relevant run, identifies the current proposition, evidence and contrary findings, business requirements, and unfinished investigation. Keep the user's explicit selection separate from the scout's recommendation. An investigator handoff adds the current offer and selected test plan; customer-connect adds sourced contact routes and preparation. No handoff implies permission to send messages, purchase anything, or run a live test.

## Use the templates

Read only the templates needed for the task. Adapt their sections to useful work and leave important unknowns visible. `{{...}}` denotes text or a link destination to replace when creating a record; it is not a working link in the template package. Resolve generated links relative to the saved record's destination and check that each target exists. Keep links between saved records inside the output workspace so copying it preserves the handoff; when paths use symlinks, normalize both link source and target consistently before computing relative paths. Remove template instructions and unused optional sections from the output. Do not create empty opportunity records merely to fill the directory layout.
