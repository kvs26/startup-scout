# Build and verify startup customer connect

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:task
Type: task
Mode: AFK
Status: open
Assignee: unassigned
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
