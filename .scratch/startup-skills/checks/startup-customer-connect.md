# Startup customer connect checks

Checked: 2026-10-10

Implementation: [skill](../../../.agents/skills/startup-customer-connect/SKILL.md), [UI metadata](../../../.agents/skills/startup-customer-connect/agents/openai.yaml), and [shared preparation template](../../../docs/startup-skills/templates/contact-preparation.md).

## Method and limits

A separate agent prepared fictional raw fixtures. Each execution agent then received the skill path, a realistic request, and one isolated output workspace without the implementation discussion, expected answer or sibling scenarios. The parent reviewed generated records and checked links, original-file hashes, evidence identity and action state. No fixture involved real people, external services, credentials, sending, purchases or live experiments.

The [temporary fixture manifest](/tmp/startup-customer-connect-checks-mv77vm3r/manifest.json) records initial hashes for 24 input files, including seven raw source artifacts. Temporary execution artifacts linked below may be removed by system cleanup; this report retains the requests, observed outcomes and limitations. These executions assess instruction behavior on supplied evidence. They do not establish live contact accuracy, provider coverage or future model reliability.

## Structural and contract checks

- Skill-creator's `quick_validate.py` reports **Skill is valid!**. System Python lacked PyYAML; validation reused existing cached PyYAML through command-local `PYTHONPATH`, with no installation or added runtime dependency.
- UI metadata matches skill-creator's generated output byte-for-byte, parses, uses the required short-description length, invokes the skill in its default prompt, and leaves automatic invocation enabled. The generator ran in a writable temporary directory because direct script writes to `.agents/` are sandbox-restricted; the installed file was written with the patch tool.
- A separate read-only acceptance review found no actionable gap against the agreed customer-connect contract or skill-authoring guidance.
- All 38 local link targets, including the contact-source anchor, resolve across the new skill and shared resources.
- The implementation extends the existing contact-preparation template. It adds no separate record guide, source catalog, glossary, provider adapter or credential configuration.

## Learning conversation and missing named address — passed

Request: prepare Canadian museum learning conversations from current investigation/test and supplied website/directory snapshots, including relevant people/routes, introduction, follow-up and interview questions.

The [preparation](/tmp/startup-customer-connect-checks-mv77vm3r/learning/opportunities/museum-offline-captions/connections/2026-10-10-learning.md) identifies two published staff roles through one museum's institutional form. Named emails stay unknown, routing and purchasing authority stay unverified, and a similarly named exhibitor is correctly excluded as a separate supplier. Both staff members remain one organization. The agent read the original snapshots and expanded existing evidence entries without duplicating them.

The questions apply the selected test to recent caption updates and visitor experiences, retaining printed guides/PDFs as potentially sufficient alternatives. A conditional follow-up and blank observation aid remain preparation. The [response](/tmp/startup-customer-connect-checks-mv77vm3r/learning/evaluation-response.md) links usable work and states offline limits. Prior findings were preserved in a dated round; no customer result was created and demand confidence stayed unchanged. Parent verification: 45 local links, including 20 anchors, passed.

## Sales and negotiation with inferred vendor data — passed

Request: prepare a UK agency sales conversation and response to a 300 GBP/unlimited-support request against the founder's proposed 600 GBP, two-week, one-project pilot. Minimum price and support ceiling are unknown. A saved original reply and vendor export accompany the request.

The [preparation](/tmp/startup-customer-connect-checks-mv77vm3r/sales/opportunities/agency-scope-approval/connections/2026-10-10-alder-lane-sales.md) uses the supplied reply thread, retaining its source limits. It distinguishes the vendor's inferred named email and deliverability label from identity, current role, fit and willingness. It preserves the managing director's approval role without inventing a named buyer or direct route.

The reply draft, offer explanation, meeting outline, objections and explicitly simulated negotiation preserve the current proposed scope and price. Missing founder limits and VAT treatment remain open; no discount, unlimited support or profit figure is invented. The [response](/tmp/startup-customer-connect-checks-mv77vm3r/sales/evaluation-response.md) requests only the material missing terms while delivering usable preparation. R001, research, economics and the test remain byte-for-byte unchanged, with no extra result created. Earlier summary and history are preserved. Parent verification: 52 local links, including 10 anchors, passed.

## Consumer recruitment and missing commercial details — passed

Request: prepare learning conversations for a Brazilian amateur-ensemble scheduling idea using saved community pages, without named contacts or a price, and write the introduction/follow-up in Brazilian Portuguese.

The [preparation](/tmp/startup-customer-connect-checks-mv77vm3r/consumer/opportunities/ensemble-rehearsal-scheduling/connections/2026-10-10-learning.md) uses the moderator form and a proposed public opt-in invitation. It retains the rules against unsolicited member messages and contact-list collection. The moderator is not treated as a buyer, approval is not claimed, and no member list or invented named contact appears. Missing price does not block the learning request or become an invented offer.

Portuguese questions examine a recent scheduling cycle, effort, consequences and cases where existing tools work. The [response](/tmp/startup-customer-connect-checks-mv77vm3r/consumer/evaluation-response.md) identifies the next human step and preserves the distinction between drafts and actual recruitment. No result record was created. Parent verification: 40 local links, including 16 anchors, passed.

Across these three executions, all seven raw artifacts and all three selected test plans remained byte-for-byte intact. Learning and consumer preparation created no result records; sales retained only its original R001. Changes to current summaries were accompanied by saved earlier views and history entries.

## Fresh-session returned-result intake — passed

Request: save a reattached morning email and paraphrased notes, plus a later email withdrawing the pilot discussion, and prepare an investigation handoff for the next session. The user explicitly says the prepared sales message was never sent and there is no agreement or payment.

The fresh customer-connect execution matched the morning attachment byte-for-byte to [R001](/tmp/startup-customer-connect-checks-mv77vm3r/return-intake/opportunities/agency-scope-approval/results/R001.md), adding receipt history and the user's account without creating another observation. The later message became [R002](/tmp/startup-customer-connect-checks-mv77vm3r/return-intake/opportunities/agency-scope-approval/results/R002.md): a new event from the same customer, not a second independent customer. The customer's clarification, the founder's changed impression and the earlier interpretation remain distinguishable. The exact user submission and both original message artifacts were preserved.

The [handoff](/tmp/startup-customer-connect-checks-mv77vm3r/return-intake/opportunities/agency-scope-approval/connections/2026-10-10-return-intake-handoff.md) links the opportunity, results, claim, test and economics, names the unanswered questions, and marks investigator reassessment pending. The former draft is flagged for review against the customer's hold request, with its prior version retained. The [response](/tmp/startup-customer-connect-checks-mv77vm3r/return-intake/evaluation-response.md) accurately reports intake rather than a completed investigation. No draft was treated as sent or as the cause of the supplied replies.

Parent verification: exactly R001 and R002; unchanged original artifacts and earlier rounds; unchanged research, economics and test while reassessment is pending; exact preserved submission/later reply; 130 local links including 21 anchors passed.

## Fresh-session investigator continuation — passed after link correction

Request: continue the opportunity from the saved customer-connect handoff, assess what the returned replies change, and propose the next useful test using only saved files. A separate agent received a copy of the intake workspace without previous chat or evaluation conclusions.

The [response](/tmp/startup-customer-connect-checks-mv77vm3r/investigator-resume/evaluation-response.md) distinguishes the weaker sale to this customer from a market-wide rejection. The [research](/tmp/startup-customer-connect-checks-mv77vm3r/investigator-resume/opportunities/agency-scope-approval/research.md) retains C001, adds a workflow-fit question, and reuses R001/R002 without new result IDs. The original 600 GBP proposal remains unchanged; economics marks the 300 GBP amount as historical discussion, leaving costs and founder limits unknown. No purchase or use is inferred.

The sales test is deferred and [T002](/tmp/startup-customer-connect-checks-mv77vm3r/investigator-resume/opportunities/agency-scope-approval/tests/T002.md) proposes comparing an actual disputed request with a smooth one to distinguish agreeing scope from recording approval. It respects the proposal hold and supplies participant roles, procedure, materials, observation capture and supporting/contrary/ambiguous interpretations. The [saved round](/tmp/startup-customer-connect-checks-mv77vm3r/investigator-resume/opportunities/agency-scope-approval/rounds/2026-10-10-returned-replies-reassessment.md) preserves conclusions, calculation inputs and test design. The current comparison covers only this opportunity and its spreadsheet alternative, with offline limits explicit.

One observed implementation issue was corrected before completion: a history snapshot initially mixed resolved `/private/tmp` targets with an unresolved `/tmp` source path. Its links resolved on this machine but escaped the saved workspace and would fail after relocation. The agent corrected all 20 affected links; the common [record guide](../../../docs/startup-skills/record-guide.md#use-the-templates) now explicitly requires workspace-local record links and consistent path normalization through symlinks. This is a narrow shared-guidance correction; no business-workflow change was needed.

Parent verification confirmed 13 protected original/result/prior-round/preparation files unchanged, exactly R001/R002, and the complete previous summary, research, economic inputs and T001 procedure preserved in the history snapshot (allowing relocated link destinations). The corrected workspace was copied to a different temporary directory: all **204 local links and 28 anchors** resolved inside that copy. This exercises portability rather than merely checking targets at the original location.

## Outcome

All five isolated executions passed after the link correction. Drafts, plans and role-play stayed separate from observed customer results; repeated events preserved identity; conflicting replies and earlier outputs remained available across sessions. Existing provider limitations still apply through [tool routing](../../../docs/startup-skills/tools.md) and [SETUP.md](../../../SETUP.md). No new provider connection, live contact search, paid capability, outreach or customer experiment was tested or claimed.
