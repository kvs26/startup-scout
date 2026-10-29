# Enforce required source coverage and disclose unread inputs before research

Parent: [Research and deliver startup idea scout version 2](../map.md)
Labels: wayfinder:task
Type: task
Mode: AFK
Status: resolved
Assignee: Codex coordinator
Blocked by: none

## Question

Can the scout's instructions and output contract enforce the user's chosen category's relevant sources, check supplied links before candidate research, and pause for missing material or consequential ambiguity instead of silently substituting sources or claiming completion?

## Comments

- 2026-10-30: The user reports a run based mainly on Reddit, Etsy, app stores and product pages; creator coverage consisted of two publisher transcripts, inaccessible Instagram links and an unread new reel. The user requests explicit source obligations, immediate disclosure, an opportunity to provide screenshots/material, and research into reliable YouTube/Instagram access. Implementation is expressly authorized. The related access investigation has its own research ticket.

## Answer

Resolved 2026-10-30. The [scout entrypoint](../../../.agents/skills/startup-idea-scout/SKILL.md) now requires the [source-readiness check](../../../.agents/skills/startup-idea-scout/references/source-readiness.md) before candidate research in every mode. It maps the selected category/audience/angle to actual sources, checks supplied references, immediately discloses unread or partial material, and pauses dependent work until the material is available or the user explicitly changes scope. Current creator/trend work requires relevant dated originals and the appropriate speech/visual evidence; historical interviews and unrelated accessible sites do not fulfill that obligation.

The discovery/delegation guides, report template, shared research/tool guides, maintained source catalog and SKILL-MAP now carry that contract through assignments, acceptance and reporting. Workers must promptly report failures. The coordinator reconciles every required source family and supplied reference against actual inspected evidence or an explicit user scope change before final comparison; fifty assessments alone cannot establish campaign completion. Material limitations appear before recommendations in chat. Optional sources can still be skipped without an unnecessary approval round.

Validation: [five independent forward-test scenarios](../checks/source-coverage-2026-10-30.md) cover unread supplied inspiration, fifty assessments with missing platform coverage, an unrelated optional Instagram failure, an explicit narrowed scope with screenshots, and a worker's overstated audiovisual coverage. The coordinator reviewed the actual outputs: all five followed the intended next-action boundaries and retained truthful counts/provenance. Skill validation, local-link/anchor and whitespace checks passed. These checks do not guarantee compliance on every future model run.

The [access investigation](14-research-youtube-instagram-access.md#answer) supplies concrete provider candidates and real runtime limitations. SETUP and the source catalog now say no end-to-end YouTube/Instagram content route was verified here. No prior campaign was relabeled, no new discovery campaign was launched, and no provider account, paid plan or outreach was created.

Next owner: a connection task can test the documented free Apify/Supadata routes after an available account connection is supplied, using the original carousel/reel and a relevant YouTube sample. Until access or supplied material satisfies the brief, source-dependent scouting remains paused. Ready prompt: “Use the creator-access pilot in `.scratch/scout-skill-v2/youtube-instagram-access-research.md` to verify my supplied YouTube/Instagram material with included free allowances. Report actual text, visual and discovery coverage before starting any idea research.”
