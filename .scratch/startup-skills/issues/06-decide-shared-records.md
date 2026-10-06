# Decide shared opportunity records and skill handoffs

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:grilling
Type: grilling
Mode: HITL
Status: resolved
Assignee: Codex
Blocked by: 04, 05

## Question

What is the smallest durable record of an opportunity, its customer and market hypotheses, sources, observations, assumptions, contrary evidence, decisions, and next tests that scouting can hand to the rest of the suite without duplicating or overstating evidence?

Decide canonical records versus derived summaries, market and currency context, observation versus retrieval dates, claim-specific freshness, how inaccessible sources differ from no results, revisiting an idea, and how user rejection differs from evidence against a hypothesis. Scope the first contract to the scout and its handoff to the required deeper investigation skill, while leaving explicit extension points for other skills.

Include the saved-work and return-results requirements agreed in [Decide the business and customer questions the suite must cover](05-decide-commercial-coverage.md#investigation-is-a-repeatable-loop-with-saved-work). Specify how an investigation resumes in another session, where all prior research and outputs are retained, how customer results return from the separate customer-connection skill or the user, and how the current findings remain connected to their history. Decide how to identify repeated results, preserve conflicting evidence, and record changed conclusions without erasing earlier work. This loop is part of the first investigation contract, not a future extension.

Choose the repository location for the runnable skills and eventual run outputs, keeping this map's planning files in `.scratch/`. Agree which shared resources are actually needed. Consult grilling and domain-modeling; keep implementation detail out of the domain glossary.

Include the user's 2026-10-02 request for a Markdown glossary: each term gets just one short explanation in easy language. Decide whether to simplify the existing root `CONTEXT.md` or provide a separate reader-friendly file, where it belongs, and how to keep its meanings consistent as terms are added or changed.

## Comments

### 2026-10-03 — Opportunity folders and glossary agreed

- The user agreed to one folder per opportunity, shared by scouting and deeper investigation, containing its current summary, research, customer-test plans, results, and earlier work.
- The user agreed that price and feature changes remain versions of the same idea, while a different customer group or problem gets a separate linked record when it needs its own investigation. They asked whether a new record means a subfolder or a separate folder. The clarification offered is a sibling opportunity folder, with links between related opportunities; the physical layout is still being discussed.
- The user accepted simplifying the existing root `CONTEXT.md` and requested a heading named `Glossary`. That heading and the one-line, everyday-language definitions have been applied. There is no second glossary.
- Repository inspection found existing runnable skills under `.agents/skills/` and no established run-output directory. Proposed paths for saved outputs and shared resources remain choices for the live discussion.
- The scout-workflow dependency remains open. Common saved-record decisions can proceed, while workflow-specific run inputs, comparison fields, and stopping details remain unsettled. No dependency has been removed and this ticket is not resolved.

### 2026-10-03 — Locations, linked summaries, return results, and freshness agreed

- The user accepted `opportunities/` for durable opportunity work, with sibling folders for distinct opportunities, and `.agents/skills/` for runnable skills. Use readable Markdown files; map planning stays in `.scratch/`.
- The user accepted a short current summary linked to detailed research, calculations, tests, and earlier conclusions. Save each piece of evidence once and refer to it from summaries. Retain older findings and explain changes in conclusions.
- The user accepted flexible result submission and explicitly clarified both routes: create a file for the project, or invoke the investigator again with the project and newly found data. The investigator must identify the opportunity, load its saved work, incorporate the supplied data, and continue from there. Ask which opportunity only when the supplied project reference is ambiguous; do not require a form or rely on earlier chat memory.
- Preserve the submitted notes and supplied artifacts, distinguish user reports from supporting material, identify the relevant customer/test/claim where possible, check for duplicate results, and keep conflicting accounts. Ask only about gaps that materially affect interpretation. Repeated submission does not create independent evidence.
- The user accepted decision-specific freshness checks rather than one fixed expiry for all evidence. Preserve observation/event dates separately from retrieval dates, and relevant country, currency, and units. Unknown dates remain unknown. Record inaccessible sources separately from searches yielding no results.
- Shared record guidance/templates and storage for comparisons spanning multiple opportunities remain to be discussed. Exact research controls, comparison content, and stopping rules still belong to the scout-workflow and output-prototype tickets.

### 2026-10-03 — Shared guide, separate tools, and comparison file agreed

- The user accepted one shared record guide and simple templates, noting that different tasks may require different tools. The shared guide governs saved information and handoffs, not tool selection.
- The user requested research into reusable projects, MCP servers, and open-source resources, including maintained idea lists. This is now [Research reusable startup tools, MCP servers, and discovery resources](12-research-reusable-startup-toolkit.md), assigned to a research subagent. Its findings feed the scout-workflow and suite-blueprint decisions.
- The user accepted `scouting-runs/` and additionally requested one file directly inside `opportunities/` with short comparison results. Use `opportunities/comparison.md` for that current overview, linked to detailed opportunity records and the saved run reports.
- Clarified that an opportunity record means the saved information for an idea, not a second folder layer: each distinct opportunity has a sibling folder under `opportunities/`. Revisions to its price or features stay in its existing folder. Internal folders may organize supporting files or history; they do not represent new opportunities.
- Removed the scout-workflow blocking edge because this resolution establishes common storage and handoff rules independently of research breadth, stopping rules, and comparison criteria. Those choices remain explicitly owned by the existing workflow and output-prototype tickets. No workflow decision is being resolved here.

## Answer

Resolved 2026-10-03 through the live discussion. This answer records the shared storage and handoff contract. It does not implement the runtime skills or choose their research tools.

### One folder per opportunity

An opportunity record is the saved information about one idea. Each opportunity has its own folder directly inside `opportunities/`; the record is not an additional folder nested inside it. Use a stable, readable folder name and an explicit opportunity name in its summary so skills can find the same work again.

```text
opportunities/
  comparison.md
  appointment-tool-for-clinics/
  appointment-tool-for-salons/
scouting-runs/
.agents/skills/
```

The names of the example opportunities above are illustrative, not researched candidates. Price and feature changes remain versions of the same opportunity. A changed customer group or problem gets a new sibling folder when it needs a separate investigation, with links explaining the relationship. Evidence retains its original customer and market context; a linked idea does not automatically inherit support for its own claims. Subfolders within an idea may organize files or history, but do not signify another opportunity.

Runnable skills live under `.agents/skills/<skill-name>/`. Durable opportunity work lives under `opportunities/`, and reports spanning several opportunities live under `scouting-runs/`. This map's tickets, research answers, and planning prototypes stay under `.scratch/startup-skills/`. Create runtime files as they become useful rather than generating empty opportunity folders during planning.

### Current view, original detail, and history

Use readable Markdown. Each opportunity needs a short current summary linked to its detailed records. The summary identifies the customer/problem and market, current offer or version, important findings and uncertainties, the user's latest selection, and the next useful investigation or test. It is a view of saved detail, not an independent source of evidence.

The detailed records preserve:

- Claims and findings, with their context, supporting and contrary evidence, limits, and reasons for confidence. Assumptions remain distinguishable from observations.
- Sources and research notes, including useful unsuccessful searches and access failures.
- Calculations and their inputs, distinguishing sourced, user-supplied, and hypothetical numbers as agreed in the commercial-coverage decision.
- Customer-test plans, their target claims and customers, and what results would change the decision.
- Supplied results and original supporting material, linked to the relevant test and claim where known.
- Recommendations, user decisions, previous outputs, and a dated explanation of changes to the idea or its conclusions.

Store each observation/result once as the authoritative entry and link to it from findings, summaries, and other skills. Give entries stable references, such as file links and labeled entries, so a later session can connect evidence to claims without relying on chat memory. Multiple claims or ideas may refer to the same evidence without presenting it as independent observations.

Updating the current summary must retain the prior research and outputs. Keep dated earlier versions or snapshots and a change history stating what changed, why, and which new information caused it. Preserve disagreements and corrections rather than silently overwriting the earlier account. Exact template filenames and visual layout can be settled during the blueprint and output prototype without changing these requirements.

### Sources, context, and freshness

For a source or result, retain its origin or supplied artifact, what it actually reports, the claim it bears on, and relevant customer/market context. Separate the observation or event date from the date retrieved or received. Preserve publication dates where useful; unknown dates remain unknown. Preserve relevant country, currency, billing period, and units. Any currency conversion or calculation must retain its basis instead of silently replacing the original amount.

Recheck claims when their age or changed circumstances matter to the next decision, not after a universal expiry period. For example, current supplier prices matter to a new cost calculation. If a needed recheck cannot be done, mark the current finding's limitation rather than treating old information as freshly verified.

An inaccessible source, an unperformed search, and a completed search that found no relevant results are different states. None alone establishes absent demand. User rejection is a selection decision, with its stated reason; it is not contrary customer evidence. These distinctions preserve the already agreed scouting boundary.

### Resume with new findings

The user can create a file for an opportunity or invoke the investigator again with the project and pasted findings. No strict intake form is required. The investigator must:

1. Locate the opportunity from the supplied name or path, asking only if the reference is ambiguous. Load its current summary, history, relevant detailed work, and outstanding tests.
2. Read and preserve the new notes or files. Distinguish the user's report from any supporting artifact; record relevant dates and customer/test/claim links when known. Ask only about gaps that affect interpretation.
3. Check whether the same result is already recorded. Use the original event, source/artifact, customer or test reference, date, and content where available. Rephrasing or resubmitting the same event is not independent evidence. If identity is uncertain, flag possible duplication rather than assume another result. A correction is linked to the earlier entry; a genuinely new event can add evidence even if it comes from the same customer.
4. Reassess affected claims, retaining supporting and conflicting evidence. Explain which conclusions changed, stayed the same, or remain uncertain. A planned test is not a completed test, and a new report does not automatically establish purchase or repeat value.
5. Save the updated current view, detailed results, changed calculations or tests, and a dated account of the changes. Propose the next useful step while preserving the user's decision authority.

The future customer-connection skill can hand back results through these same records. Other skills may add task-specific detail and artifacts linked to the opportunity; they must preserve the common evidence, history, and handoff rules rather than creating competing copies of the truth.

### Comparisons across opportunities

Save each scouting round's report under `scouting-runs/`, preserving the comparison made at that time and linking to the opportunity records. Maintain `opportunities/comparison.md` as the short current overview requested by the user, with links to each relevant opportunity and its detailed comparison report. It is a derived summary, not another evidence store.

Date the overview and show what has changed or has not yet been reassessed when an investigation updates an opportunity. Update affected summaries from saved findings without inventing a fresh full comparison. Earlier run reports remain available. Exact comparison fields, research breadth, and stopping rules belong to [Decide how the scout discovers and compares open opportunities](07-decide-scout-workflow.md) and [Try the scout output before implementing the skill](09-prototype-scout-output.md).

### Shared resources and glossary

Use one shared guide and simple templates for the records and handoff above, referenced by each skill that reads or updates them. The guide covers the shared core; task-specific tools and additional templates can differ. Its runtime packaging belongs to the suite blueprint and implementation, avoiding duplicate guides that can drift apart.

Keep the sole domain glossary in root `CONTEXT.md` under `## Glossary`, with one short, everyday-language explanation per term. That simplification has been applied. Update this same glossary when a term's meaning is agreed or changed, and check that the skills and templates use it consistently. Keep file formats and implementation instructions out of the glossary.

### Remaining decisions

[Research reusable startup tools, MCP servers, and discovery resources](12-research-reusable-startup-toolkit.md) investigates the user's request for existing resources. Findings inform later selection rather than automatically adding dependencies. [Agree the startup skill suite blueprint](08-decide-suite-blueprint.md) owns tool adoption, shared-resource packaging, skill names and detailed contracts. The existing implementation tickets must implement and check this contract, including cross-session resumption, repeated results, conflicting evidence, history retention, and the shared comparison overview.
