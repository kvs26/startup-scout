# Build and verify startup idea scout

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:task
Type: task
Mode: AFK
Status: resolved
Assignee: Codex
Blocked by: 08, 09

## Question

Does an implemented `startup-idea-scout` faithfully perform the agreed workflow and produce the agreed records and comparison, with meaningful behavioral checks demonstrating that it is ready to use?

This execution task is authorized by the map's explicit override. Use skill-creator and writing-for-agents to build the skill and only the resources justified by the resolved decisions. Use the agreed repository destination. The suite's other skills do not need to be implemented for this task to finish.

Use the tools prepared in [Guide and verify the selected tool setup](13-guide-tool-setup.md). If implementation changes that setup, follow its manual-first and per-step delegation rules and update root-level `SETUP.md` with the actual changes and reasons. On 2026-10-06, the user deferred Tavily and authorized completion with the verified existing web tools; the setup dependency is removed for this build, with the follow-up recorded in [TODO.md](../../../TODO.md).

Completion requires:

- Implement the [resolved blueprint](08-decide-suite-blueprint.md#answer), including shared runtime guidance/templates in `docs/startup-skills/`. Move the single starting-source catalog there as `source-catalog.md`, repairing its internal relative links and all planning/runtime pointers instead of keeping divergent copies. All three skills must be able to reference the same maintained resources.
- A discoverable skill with clear invocation boundaries, inputs, outputs, and linked resources, usable without the copied passive-site project.
- Structural validation and working local references; added scripts must be exercised if the decisions actually require them.
- Check the agreed saved-record layout: opportunity folders, a concise linked `opportunities/comparison.md`, and preserved reports under `scouting-runs/`, using the shared-record guide without copying evidence into competing authoritative records.
- Implement and behaviorally check the [accepted output presentation](09-prototype-scout-output.md#answer): explain each product and a concrete example before evidence, compare common questions in a table, and add one explicit cross-idea comparison with reasons, trade-offs and what could change the recommendation. The overview must stand alone for the reader; supporting research is optional detail. Check understanding and justified comparisons, not exact wording or invented cost/profit rankings.
- Independent behavioral evaluation in an isolated scratch location using contrasting realistic requests: open discovery, a supplied idea, different markets, customer industries and technology business models, contradictory or missing evidence, an existing incumbent, and a high-effort solo opportunity. Select a compact set that covers those behaviors; check actual outputs instead of matching prescribed wording.
- Explicit checks that software, AI, and similar technology opportunities across any industry remain eligible without narrowing to SaaS or adding hidden preference or solo-founder vetoes; estimates remain labeled, source failures remain gaps, and research findings do not masquerade as customer validation.
- Verify independent discovery from the wider web and public forums: a run must pursue relevant problem searches beyond curated idea lists and preserve original sources. Include a case where a list is unavailable or misses a relevant problem; verify actual discovery behavior and honest access limits rather than requiring a predetermined number of ideas or fabricated findings.
- Apply the [agreed research workflow](07-decide-scout-workflow.md#answer), including the linked starting-resource catalog, substantial follow-up research, opposing evidence, progress updates and useful questions. Check a case where an initial link or two leaves a material uncertainty: the scout must pursue it or explain a concrete blocker. Link counts alone do not demonstrate depth or completion.
- Check continuation from both a saved run and a named opportunity. Use run history for prior search scope and unfinished work, and opportunity folders for current findings; include a case where an opportunity was updated after the run so older comparisons cannot silently replace newer findings.
- Corrections for observed failures, a concise record of what was checked and remaining limits, and a concrete invocation example the user can run.

Record implementation links and results in the answer. Resolve only when the scout works; a draft prompt or future implementation plan does not satisfy the map's destination.

## Comments

### 2026-10-06 — Implementation and independent checks started

Claimed for the user's explicit request to work on this build. The blueprint and output-presentation decisions are resolved. The setup dependency remains open: no Tavily tool is available in this session, inspected Codex MCP configuration lists no Tavily server, and the process has no `TAVILY_API_KEY`. These checks inspect configuration names/presence only, not secret values. The user has been asked whether to defer Tavily for this build, supply an existing setup location, or retain it as a closing prerequisite; no answer has been assumed.

Proceeding with authorized implementation, structural validation and isolated behavioral checks using existing web/file tools. No account setup or configuration change is being performed. The scout entrypoint and shared runtime resources are being built from the resolved contracts; a subagent implemented the shared records/templates, and independent agents are executing realistic requests. The task remains unresolved until results and any remaining setup requirement are addressed.

### 2026-10-06 — Implementation and available-tool checks complete; setup prerequisite pending

Implemented [startup-idea-scout](../../../.agents/skills/startup-idea-scout/SKILL.md) with discovery metadata, clear entry paths, substantial independent research, the accepted comparison presentation and durable continuation. Added the shared [record guide and nine templates](../../../docs/startup-skills/record-guide.md), [research guide](../../../docs/startup-skills/research-guide.md), and [tool routing](../../../docs/startup-skills/tools.md). Moved the sole [source catalog](../../../docs/startup-skills/source-catalog.md) to its runtime location, repaired planning links and added the contact-source section. No copied-project code or new runtime scripts are required. [SETUP.md](../../../SETUP.md) records actual capabilities and gaps.

[Evaluation results and artifact links](../checks/startup-idea-scout.md) document structural validation, local-link checks and four independent behavioral executions: live open discovery with the usual idea list unavailable, a supplied non-SaaS Indian industrial opportunity with contrary/sparse evidence and high solo effort, continuation from an old run, and continuation from a named opportunity. Actual outputs preserve evidence limits, labeled estimates, opposing findings, original sources, substantive follow-up, readable comparisons and the user's selection authority. Both continuation checks retain newer findings, deduplicate a repeated customer note, preserve historical outputs and mark unrelated older evidence as unreassessed; checksums verify unchanged history/input/unrelated records. All generated evaluation work remains under `/tmp/`.

Concrete invocation: `$startup-idea-scout Find software and similar technology opportunities across markets. Explain the products, compare the evidence and delivery work, and save the findings.`

**Remaining blocker:** the selected Tavily setup in [Guide and verify the selected tool setup](13-guide-tool-setup.md) is still unverified. Existing web research passed, but it is not a Tavily check. The user has not yet answered the setup-status/deferral question. Keep this ticket claimed and unresolved, retain its setup dependency, and do not add it to the map's resolved-decision index until Tavily is verified or the user explicitly defers that prerequisite for this build. No additional design ticket or source adapter is justified by the observed results.

## Answer

Resolved 2026-10-06 after the user explicitly deferred Tavily, requested a one-line root follow-up, and instructed completion of this ticket. [TODO.md](../../../TODO.md) records the remaining Tavily connection/check. The scout uses verified existing web tools; Tavily has not been connected or tested.

Delivered [startup-idea-scout](../../../.agents/skills/startup-idea-scout/SKILL.md), the shared [record guide and nine templates](../../../docs/startup-skills/record-guide.md), [research guidance](../../../docs/startup-skills/research-guide.md), [tool routing](../../../docs/startup-skills/tools.md), and the single maintained [source catalog](../../../docs/startup-skills/source-catalog.md). Planning links point to the moved catalog. The skill supports open discovery, supplied ideas, readable comparisons, durable evidence/history, and continuation from either a run or an opportunity. It does not require the old scripts.

Structural validation and four independent behavioral scenarios passed: live discovery beyond idea lists, a demanding non-SaaS supplied idea with sparse/contrary evidence, saved-run continuation, and named-opportunity continuation. Actual outputs preserve original sources, labeled estimates, newer findings, duplicate-result identity and user-owned selection. Local links, output anchors and historical-record checks passed. See [the evaluation record](../checks/startup-idea-scout.md) for evidence and limits; all test outputs remain isolated under `/tmp/`.

Use: `$startup-idea-scout Find software and similar technology opportunities across markets. Explain the products, compare the evidence and delivery work, and save the findings.`

No additional design ticket is needed. The remaining setup work and the investigator/customer-connect implementations stay with their existing tickets; this resolution completes the scout build only.
