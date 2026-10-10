---
name: startup-customer-connect
description: Find relevant people and contact routes for a chosen technology opportunity, prepare learning conversations, sales meetings or negotiation, and save returned replies for investigation. Use startup-opportunity-investigator for business research and customer-test design, and startup-idea-scout for open discovery.
---

# Startup customer connect

Prepare the user's next customer conversation from the opportunity's current work. Produce sourced routes and usable material for the immediate goal, with a durable return path for what actually happens.

Examples: “Find people to learn from about this opportunity,” “Prepare this sales meeting,” “Help negotiate this pilot,” or “Save these replies and return them to the investigation.” Preparation ends before sending, spending, committing terms or running a live test; those actions require their own explicit authorization.

## Load the opportunity and conversation goal

Resolve the repository root from this skill's location (`../../..`). Read the shared [record guide](../../../docs/startup-skills/record-guide.md) and [tool routing](../../../docs/startup-skills/tools.md). The root [glossary](../../../CONTEXT.md) owns domain terms. Runtime work does not require the planning tracker or old project. An explicitly supplied output workspace changes the record destination, not the shared-resource location.

Resolve the supplied opportunity name/path against existing summaries. Load its current summary, investigation, offer/terms, unresolved customer questions, selected tests, relevant results, prior preparations and history. Use saved current findings over an older scouting report. Selection records the user's choice; it does not establish demand.

Infer **learning**, **sales preparation**, **negotiation**, or **returned results** from the request and records. Clarify only ambiguity that materially changes the work. Preserve the chosen market, customer group and business format; there is no default country, industry or subscription model. Ask for relationship context or the user's acceptable terms only when they affect the conversation. Work that does not depend on the answer can continue.

If the opportunity cannot be identified, or a missing customer/offer/test decision changes what should be prepared, name that gap and hand the question to `startup-opportunity-investigator`. Save useful partial preparation with assumptions explicit; do not silently invent a price, customer-test criterion, buyer or customer commitment. A selected opportunity need not repeat scouting before receiving help.

## Find suitable people and evidenced routes

When discovery is needed, consult the [contact-source section](../../../docs/startup-skills/source-catalog.md#customer-contact-sources) of the single source catalog and the [research guide](../../../docs/startup-skills/research-guide.md). Choose sources for the idea and market; the catalog is a starting point. Existing contacts may need only a focused role or route check.

Separate three questions: which organizations or communities fit, which people/roles matter, and which route is actually available. Distinguish users, influencers, payers and approvers; a title, directory listing or exhibitor entry alone establishes neither buyer fit nor purchasing authority. For consumer opportunities, community organizers and voluntary recruitment may fit better than business-contact databases; retain participation rules and moderator permission requirements.

Inspect accessible original company/team/contact pages, relevant associations/events, and appropriate local sources. Follow material uncertainty about role, employer or fit. For each useful lead save why it fits, the source and check date, relevant market, role/authority uncertainty, contact route, provenance and verification limits using the shared template. Source observations live once in the shared research record; preparations link to them. Retain source-specific storage restrictions, saving a permitted pointer instead of restricted details where necessary.

Treat public, vendor-supplied, inferred and unknown details distinctly, including field-level differences within one contact. A published company inbox/form/business phone or supported introduction can be a useful fallback when a named route is missing. Keep guessed email patterns as unverified hypotheses, not usable named addresses. Vendor deliverability labels do not establish identity, current role, buyer fit or willingness to speak. Nobody is recorded as contacted or willing without an actual sourced result.

Use only the capabilities available and checked in this session under [tool routing](../../../docs/startup-skills/tools.md); consult root [SETUP.md](../../../SETUP.md) for dated configuration status. A configured VS Code integration is not automatically a tool in another client. Hunter/Apollo are conditional aids: authentication, search, reveal/enrichment and verification are separate checks. Verify relevant free access and allowance before a call; otherwise use public or human-assisted routes and record the gap. LinkedIn access can be a precise task for the user's authorized account without assuming an API or scraping access. Additional setup follows existing setup instructions, rather than becoming an implicit part of preparation.

If contact information remains unavailable, save the sources attempted, failure/no-result/unattempted state, useful fallback and remaining check. Offline supplied snapshots can support explicitly dated, limited preparation; they are not fresh live verification. Missing contacts or sparse coverage do not establish absent demand.

## Prepare only what this conversation needs

Use the common [contact-preparation template](../../../docs/startup-skills/templates/contact-preparation.md), adapting its optional sections to the request. Keep factual personalization traceable; unknown relationship or product claims remain unknown.

| Goal | Useful material |
| --- | --- |
| Learning | A truthful introduction and appropriate follow-up, questions tied to the selected customer test, and a simple way to record actual observations. Ask about concrete past work, alternatives and consequences. Keep the learning request distinct from a sales pitch or a promise that the product exists. |
| Sales preparation | A tailored message, plain explanation of the current offer and its limits, supporting one-page material when useful, meeting outline and objections to explore. Preserve the difference between demonstrated capability and a proposed pilot. |
| Negotiation | Current proposed/accepted terms, the other party's actual requests, unresolved authority and the user's limits; possible responses, trade-offs and explicitly simulated practice. Suggested concessions remain proposals for the user, with material missing limits identified before any commitment. |

Draft follow-ups appropriate to the relationship and stated channel rules; a prepared sequence is not a campaign or an action log. Label example answers, objections and role-play as simulations. Link actual correspondence separately and preserve its wording and status. A suggested price, an interested reply, a conditional offer and an accepted purchase support different claims.

## Save preparation and return real results

Save task-specific work in the same opportunity's `connections/<preparation-id>.md`, linking the current offer, selected test and canonical evidence. Include the preparation date, usable material, uncertainties, action state and next human step. Follow the record guide's reread-before-write, ID, version/history and link checks. Keep earlier preparations available when revising terms or messages. Add a brief history entry and a current summary pointer where useful; preparation alone does not raise demand confidence or require a new business comparison.

For actual replies or meeting notes, use the record guide's **Resume and accept results** intake and the [supplied-result template](../../../docs/startup-skills/templates/supplied-result.md). Preserve pasted wording and original files, check event identity before creating a result, and retain repeats, corrections and conflicts with links. Keep drafts, plans and role-play in preparation files. Connect actual results to the relevant preparation/test/claim and distinguish user reports from supporting artifacts.

The investigator owns reassessment of business claims, calculations, tests and recommendations. If the user requests that reassessment, invoke [startup-opportunity-investigator](../startup-opportunity-investigator/SKILL.md) with the saved opportunity and result references; its intake should reuse those results. Otherwise save an explicit pending handoff with those references and material gaps. Receipt of results is not a completed investigation. If the investigator cannot run, say so and retain a usable handoff.

Stop when the requested preparation is usable, or a named missing input/access/real result blocks the remaining work. Finish in everyday language with the recommended people/routes or prepared material, why they fit, important unknowns, links to saved work and the next action for the user. The user chooses whom to contact and what terms to accept.
