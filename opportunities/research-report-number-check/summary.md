# Research-report number checking

A market-research agency finishes a client presentation, but its reviewer still has to compare slide numbers with the approved results workbook. We would sell a bounded check that highlights mismatches and shows exactly which slide object and source cell were compared. Analysts use it; the proposed buyer is the research director or agency owner. This is a global B2B opportunity, initially for smaller commercial agencies delivering editable PowerPoint reports.

An imagined use: the approved table changes from 42% to 47%, but a slide still contains 42%. The analyst supplies the workbook and PPTX, confirms the relevant source mappings, and receives an exception report. The reviewer decides whether the slide, source selection or mapping needs correction. A numerical match is not proof that the underlying research is valid.

**Scout recommendation: investigate further, conditionally.** This led a completed fifty-idea comparison because the work is observable and the result can be tested against a source. It is not a validated business or a user-selected build.

## The customer and what they want

The starting segment is a small market-research or specialist consulting firm producing client slide reports from approved results tables. An analyst prepares the deck, a senior researcher checks it, and the client may ask for editable slides. Two original commercial-context accounts describe numerical copying errors and continued Excel/PowerPoint use. They establish examples of this workflow, not its prevalence, cost or willingness to pay. Current agency service pages also show that slide-report delivery is a real offering. See [workflow evidence](../../scouting-runs/2026-10-18-scope-selection.md#i017-e001), [client format requirements](../../scouting-runs/2026-10-18-scope-selection.md#i017-e002) and [agency discovery route](../../scouting-runs/2026-10-18-scope-selection.md#i017-e010).

The desired outcome is a more dependable final review with less repetitive comparison. Report frequency, reviewer effort and procurement authority remain to be measured in the chosen segment.

## What the first version would do

The proposed initial scope is one approved workbook and one finished PPTX, with a pilot cap such as fifty slides and one hundred explicitly mapped numeric items. Those caps are assumptions to test, not demonstrated capacity.

Support native tables/charts first. Identify source versions; let the analyst confirm source-cell/object mappings; compare literal values using agreed labels and rounding; produce source-linked exceptions and a coverage list. A reviewer resolves ambiguous mappings and approves any correction. Screenshots, unsupported chart types, prose claims and unmapped values must appear as unchecked rather than silently passing. The first offer checks consistency; it does not judge sampling, statistical significance or whether a conclusion is justified.

The founder initially helps with mapping and exception review. Customer-run/local processing is a possible way to reduce file-transfer friction, but installation and permissions can introduce support costs. No production design, code or prototype exists.

## Why someone might buy and return

Test **$99 per capped report** as a proposed price, with repeat purchases as new reports are delivered. If mapping becomes reusable and delivery dependable, consider **$199/team/month for up to ten reports**. The subscription is a different, more automated operating assumption; it is not sensible to include ten bespoke manual reviews at that price without measuring labor.

The paying director would need to see useful errors caught or review effort saved after setup. Neither price has been offered or accepted, and neither renewals nor loss reduction have been measured.

## Evidence and existing alternatives

The strongest support is the pair of original commercial workflow accounts. The strongest contrary evidence is that current tools already prevent or detect related errors: native Excel links, thinkcell source updates, Displayr reporting, FlexTabs source-cited deck generation, senior review, and Anthropic's publicly available deck-checking workflow. The last already checks numerical consistency and data/narrative alignment; AI runtime can still cost money. See [current alternatives and prices](../../scouting-runs/2026-10-18-scope-selection.md#i017-e003), [public checking workflow](../../scouting-runs/2026-10-18-scope-selection.md#i017-e008) and [FlexTabs](../../scouting-runs/2026-10-18-scope-selection.md#i017-e009).

The narrow proposed advantage is checking an existing finished report against an approved external workbook without rebuilding the report-generation process. Explicit coverage and repeatable comparisons could matter. This is an untested reason to choose us, not a unique feature or demonstrated advantage. Mapping may take longer than manual checking, and source-linked generation may eliminate the need.

## How to find initial customers

Start with public agency service pages that explicitly offer quantitative research and slide reports. DJS Research is an inspected example of that work, not a qualified small-firm prospect or evidence it needs our product. Identify research directors, reporting leads and owners, then qualify company size, report volume, current tools and access to a redacted past report.

A source-linked demonstration could open a learning conversation, followed by a comparison on permitted past files and a buying discussion. ResearchOps content provides another discovery route, subject to its community rules. No warm introductions, outreach, permission to use client data or conversion rates are established.

## Building and operating requirements

Initial work includes dependable Excel/PPTX parsing, stable object/source identification, rounding rules, transparent unsupported cases, version handling and an exception report. Quality work needs reviewed example files and checks for both missed discrepancies and false alarms. Ongoing work includes mapping new templates, resolving ambiguous bases, supporting file variants and handling customer data according to agreed permissions.

The founder can direct exploration and AI-assisted development, but file-format competence and research-method judgment are unassessed. An experienced research reviewer and appropriate technical review are dependencies, with cost/access still unknown.

| Illustrative scenario | Assumptions and result |
| --- | --- |
| One $99 report | $99 × 0.95 − $5 assumed variable delivery = **$89.05**, before labor, fixed costs, acquisition and taxes. |
| $199/month, ten reports | $199 × 0.95 − $20 assumed total variable delivery = **$169.05**, with the same exclusions. |
| Labor sensitivity | Two hours per report means twenty hours for that subscription, or about $8.45/hour before excluded costs. Twenty minutes per report means about 3.3 hours, or $50.72/hour before excluded costs. Neither workload has been achieved. |
| Basic hosting input | Workers paid base is $5/month; the shared 100GB R2 illustration adds $1.35 storage. This omits other services, security, AI, monitoring and support; local processing would change the architecture. |

The 5% allowance is a hypothetical payment/refund assumption, not a processor quote. Variable delivery figures are estimates to test. [Shared supplier inputs and limitations](../../scouting-runs/2026-10-18-scope-selection.md#shared-e006).

The approximately ₹5,000/month budget can constrain an initial investigation, but reliable production, specialist review and customer acquisition have not been shown to fit it. No currency conversion or payment-provider eligibility is assumed.

## Founder fit and domain knowledge needed

The research-team preference and willingness to learn support interest, not competence or demand. With ten to nineteen hours/week, one narrow file workflow is more plausible than a complete research platform. Manual review, sales and support must all fit those hours. No warm buyer access exists.

Learn what an approved results table represents, the denominator or “base” behind a percentage, weighted versus raw results, rounding, multiple-response questions, source versions and editable versus image-based slide objects. A total above 100% can be legitimate for multiple-response questions; a checker needs context rather than an automatic error label.

Suggested learning order: inspect a public/synthetic survey table; trace its cells into a small deck; introduce deliberate stale values and ambiguous labels; explain every flagged and unflagged item to an experienced researcher. Use the official Microsoft/thinkcell linking documentation in the source record to understand the current baseline. Basic orientation can precede a small prototype, but readiness for dependable paid delivery and time to acquire specialist competence remain unknown.

## What happens next

**Recommendation:** investigate I017 before building. The clearest reason for it is an observable final-review task; the clearest reason against it is that existing tools or simple review may solve it at lower total effort.

**User selection:** none recorded. No investigator stage or customer test has run.

**Next decisive question:** do agencies have enough costly residual mistakes, after their existing process, to pay for an additional source-workbook check that saves time?

Next owner: **startup-opportunity-investigator**. Carry this folder, compare the proposed offer with current linking and AI workflows, investigate file access and reviewer costs, refine pricing/labor assumptions, and design a bounded customer test. A useful future comparison would use ten permitted past report/workbook pairs and record missed discrepancies, false alarms and total setup/review time. Stop or change the offer if mappings take longer than the saved review or customers will not permit access.

Ready-to-use prompt:

> Use $startup-opportunity-investigator on opportunities/research-report-number-check/. Investigate whether small research agencies would pay for Excel-to-PowerPoint numerical checking despite current linking and AI tools. Resolve file access, accuracy, mapping/review time, specialist costs and a credible first-customer route; then design the smallest useful customer test within my time and budget.

## Research limits and saved work

Assessed 2026-10-18. Stage: **initially researched candidate**. Folder identity: `research-report-number-check`.

The campaign completed fifty distinct deep assessments and compared the full pool. Public evidence is English-language, selected and partly historical. Current capabilities are vendor descriptions, not runtime tests. No customer contact, accepted price, measured accuracy, pilot, retention, production budget or payment setup is established. Desk scouting stops because file-based comparisons and customer evidence now decide the case.

[Current claim assessment](research.md) · [Full campaign, fifty assessments and five alternatives](../../scouting-runs/2026-10-18-scope-selection.md#i017).

