# Build and verify startup customer connect

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:task
Type: task
Mode: AFK
Status: resolved
Assignee: Codex
Blocked by: 08, 11, 13, 15

## Question

Does an implemented `startup-customer-connect` skill help the user prepare customer conversations and sales discussions for a chosen opportunity, while preserving the investigation's evidence, saved work, and return-results loop?

The user explicitly added implementation of this third skill to the current map on 2026-10-03 during [Agree the startup skill suite blueprint](08-decide-suite-blueprint.md). Follow that ticket's final contract for detailed outputs, invocation, stopping behavior, resources, and tools; this implementation task does not settle those remaining choices.

Use [Research customer contact sources and access across markets](15-research-customer-contact-sources.md#answer) for checked source/access limits; its provider shortlist does not itself adopt tools. Choose sources and representative checks according to the idea and target market, with no default country or industry.

Use skill-creator and writing-for-agents, the agreed shared record guide, and the tools verified through [Guide and verify the selected tool setup](13-guide-tool-setup.md). Follow its manual-first and individual-step delegation rules for any additional setup needed.

The [resolved suite blueprint](08-decide-suite-blueprint.md#answer) now supplies the detailed contract and shared runtime resources under `docs/startup-skills/`. Use Hunter/Apollo only to the extent their free capabilities were verified in setup; otherwise use the documented public-source and human-assisted routes, explaining gaps. Do not assume both providers are connected, contact details are available, or paid features are authorized. Add contact guidance/templates to the common resources without making a second record guide or source catalog.

Completion requires:

- A discoverable runnable skill at `.agents/skills/startup-customer-connect/`, with clear invocation examples and the agreed inputs, outputs, human contribution, and handoffs.
- Read the selected opportunity's current investigation, offer, unresolved customer questions, and relevant customer-test plans. Prepare the appropriate learning or sales materials without assuming selection establishes demand.
- Find relevant people, organizations, and available contact routes with sources and explicit uncertainty. Do not invent contact details or claim that a person has agreed to talk.
- Draft the agreed messages and supporting material, prepare conversations and negotiation, and preserve the distinction between proposed terms and actual customer commitments.
- Save task-specific preparation in the same opportunity record and link to shared evidence. Support returning user-supplied results to the investigator without losing original notes, conflicting evidence, history, or duplicate-result identity.
- Meaningful isolated behavioral checks of learning-conversation and sales-preparation requests, missing contact information, and the cross-session return to the investigator. Verify that drafts, plans, and role-play are not saved as completed outreach or observed customer evidence.
- Structural checks, corrections for observed failures, implementation links, check results, and remaining limits recorded in the answer.

Implementing and testing preparation does not authorize sending messages, spending, contacting real people, or running a real startup experiment. Use isolated fixtures for behavioral checks.

## Answer

Resolved 2026-10-10. Implemented [startup-customer-connect](../../../.agents/skills/startup-customer-connect/SKILL.md) with [discoverable UI metadata](../../../.agents/skills/startup-customer-connect/agents/openai.yaml), following skill-creator and writing-for-agents. It loads the current opportunity, offer, tests, evidence and history; finds appropriate people and supported routes; and prepares learning conversations, sales discussions or negotiation according to the immediate request. Missing addresses, uncertain buyer authority and undecided founder terms remain explicit. The user chooses contacts, actions and acceptable terms.

The skill saves preparation in the existing opportunity's `connections/` records and uses the common intake for actual replies or meeting notes. Originals, event identity, corrections, conflicting accounts and history survive the return to the investigator. Reassessment is either explicitly pending or performed by the investigator when requested; preparation never becomes proof of outreach, purchase or demand.

Extended the existing [contact-preparation template](../../../docs/startup-skills/templates/contact-preparation.md) with field-specific provenance, action state, purpose-specific material, observation capture and a clear return handoff. The single shared [record guide](../../../docs/startup-skills/record-guide.md#use-the-templates) gained a narrow rule for portable record links after a temporary-path symlink issue was observed and corrected. No duplicate guide, source catalog, glossary, provider adapter or setup dependency was introduced.

Validation is recorded in [Startup customer connect checks](../checks/startup-customer-connect.md). Skill-creator validation, generated UI metadata comparison, independent contract review and runtime-resource links passed. Five independent executions covered museum learning with missing named emails, agency sales/negotiation with inferred vendor details, consumer recruitment in Brazilian Portuguese, duplicate/contrary reply intake, and a fresh-session investigator continuation. Parent checks verified original artifacts, unchanged result identity, preserved prior findings/calculations/tests, and all 204 links in a relocated copy of the final workspace.

The checks used isolated fictional fixtures. They establish preparation and record-continuity behavior, not live market coverage or contact accuracy. Existing dated tool status and public/human-assisted fallbacks remain in [SETUP.md](../../../SETUP.md) and [tool routing](../../../docs/startup-skills/tools.md); this task did not retest or broaden Hunter/Apollo access or assume VS Code's Tavily configuration is exposed in every client. No messages, purchases, commitments or live experiments were made.

Example invocation: `$startup-customer-connect` — “Prepare learning conversations for `opportunities/<name>`” or “Prepare this sales meeting using the saved offer and replies.” No newly exposed design gap requires another ticket. This completes the required three-skill implementation floor of the map; optional extensions remain future work.
