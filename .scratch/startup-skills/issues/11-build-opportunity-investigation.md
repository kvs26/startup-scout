# Build and verify the opportunity investigation skill

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:task
Type: task
Mode: AFK
Status: resolved
Assignee: Codex
Blocked by: 08, 10

## Question

Does an implemented skill for deeper investigation of a chosen opportunity faithfully perform the agreed research and handoff, with meaningful behavioral checks showing that it works with the scout's output?

The user requested this skill during [Decide what scouting establishes and what remains untested](04-decide-scout-boundary.md), which also establishes its responsibility to design concrete customer tests for consequential unknowns. The map's execution override includes implementing it. Its agreed name is `startup-opportunity-investigator`; its detailed responsibilities and handoff to customer validation must follow the resolved boundary, commercial-coverage, shared-records, and suite-blueprint decisions; this ticket does not settle those remaining questions.

Use skill-creator and writing-for-agents, the agreed repository destination, and only the resources justified by the resolved decisions. The [resolved suite blueprint](08-decide-suite-blueprint.md#answer) now supplies the full contract, including focused customer-test depth, round stopping behavior, shared `docs/startup-skills/` guidance/templates, and selected/conditional tools. Read and extend the shared resources created by the scout build without duplicating the catalog or record guide.

Use the tools prepared in [Guide and verify the selected tool setup](13-guide-tool-setup.md). If implementation changes that setup, follow its manual-first and per-step delegation rules and update root-level `SETUP.md` with the actual changes and reasons.

Completion requires:

- A discoverable runnable skill with the agreed inputs, outputs, evidence requirements, stopping point, and human contribution.
- Direct entry from a user-supplied idea, creating or resuming the same opportunity records and investigating missing initial evidence without requiring a scouting run first.
- A working handoff from the scout that preserves sources, uncertainty, contrary evidence, and the user's selection without overstating prior findings.
- Explicit instructions and durable records for the [agreed investigation loop](05-decide-commercial-coverage.md#investigation-is-a-repeatable-loop-with-saved-work), using the shared-records contract: save each round's work and resume it with customer results brought back by the user or the separate customer-connection skill.
- A behavioral check across separate sessions: investigate and save an opportunity, resume from those records with new customer results including contrary evidence, and verify that prior work is retained, affected findings and next tests change appropriately, and the reasons for changes remain visible. Reintroduce the same result to check it is not counted as additional evidence. This check must work from saved records without relying on the previous chat context.
- Concrete customer-test plans that identify the claim, relevant customer population, how evidence would be obtained, and what result would change the decision, at the depth agreed in the design tickets.
- Check both result-submission routes (a supplied file and pasted findings with a project reference), and update the affected `opportunities/comparison.md` entry with its date or remaining comparison limits while retaining earlier scouting reports.
- Structural checks and independent behavioral evaluation in an isolated scratch location using contrasting software, AI, or similar technology opportunities across industries, including sparse evidence and an attractive-looking candidate with material contrary evidence. Check that proposed customer tests address the important unresolved claims and are not presented as executed tests or observed results.
- Checks that research conclusions, economic assumptions, and any supplied customer evidence retain their distinct meanings; desk research alone cannot establish customer purchase or repeat value for the proposed startup.
- Corrections for observed failures, implementation links, a concise record of results and remaining limits, and a concrete invocation example.

Record results under the answer when complete. Designing or implementing this skill does not authorize outreach, purchases, or real startup experiments.

## Comments

### 2026-10-06 — Claimed for implementation

Claimed before work for the user's request to solve this build. The blueprint and scout build are resolved. Following the user's existing instruction to leave Tavily for later, retained in root [TODO.md](../../../TODO.md), this build proceeds with existing web/file tools. The setup dependency remains visible pending that separate work; this does not connect Tavily, verify Hunter/Apollo, or resolve the setup ticket. Applying skill-creator and writing-for-agents, reusing shared resources, and checking behavior in isolated workspaces with independent agents.

## Answer

Resolved 2026-10-06. Delivered the discoverable [startup-opportunity-investigator skill](../../../.agents/skills/startup-opportunity-investigator/SKILL.md) and its [invocation metadata](../../../.agents/skills/startup-opportunity-investigator/agents/openai.yaml). It starts from a selected scout candidate or supplied idea, investigates the agreed business questions, prepares focused customer tests, and saves rounds that resume from files or pasted customer notes.

The skill reuses the shared records, research guide, tools, templates, source catalog and glossary. The [record guide](../../../docs/startup-skills/record-guide.md#preserve-history-and-concurrent-work) and [round template](../../../docs/startup-skills/templates/round-history.md) now explicitly retain prior calculation inputs/results and test designs when current files change. No duplicate guide, new runtime script or service installation was needed.

Structural validation and four independent behavioral executions passed: sparse-evidence scout handoff, direct live research with material contrary findings, fresh-session file intake with conflicting results, and another fresh-session intake of the same events as pasted notes. Actual outputs retain claim-specific uncertainty, separate reported evidence from assumptions, revise affected findings/costs/tests with reasons, preserve user decisions and old outputs, and update only the affected comparison. Repeated events add receipt history without new evidence IDs. Link and checksum checks passed; [the evaluation record](../checks/startup-opportunity-investigator.md) contains observations, artifacts and limits. No material behavioral failure required an implementation correction.

The user's earlier instruction to leave Tavily for the startup skills later, recorded in [TODO.md](../../../TODO.md), remains in force for this requested build. Existing web and file tools passed; Tavily was neither connected nor verified. Removed the setup blocking edge for this build while leaving [Guide and verify the selected tool setup](13-guide-tool-setup.md) open. [SETUP.md](../../../SETUP.md) reflects actual reused capabilities. Customer-connect remains a separate implementation; the investigator saves its handoff and reports its absence when unavailable.

Use: `$startup-opportunity-investigator Investigate an AI tool for small UK digital agencies that turns meeting recordings into client-approved scope changes and tracks extra charges. Save the findings and next customer tests.` Return with an opportunity path and a file or pasted notes. This is an invocation example, not a default market or product type.

No new decision ticket is needed. Test customer accounts were fictional; live research did not involve outreach, purchases or real customer experiments. This resolves only the investigator build, leaving the map's other work open.
