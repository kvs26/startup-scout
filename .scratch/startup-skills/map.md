# Design the startup skill suite and ship the first scout

Labels: wayfinder:map
Status: open

## Destination

A research-backed blueprint for a startup skill suite covering discovery, validation, customers, business model, costs, marketing, and sales, with working and behaviorally checked skills for both startup idea scouting and deeper investigation of a chosen opportunity delivered before this map closes.

## Notes

- **Execution override:** the user explicitly expanded this map beyond wayfinder's planning default. Its destination includes implementing and checking `startup-idea-scout` and, following the user's 2026-10-01 clarification, a skill for deeper investigation of a chosen opportunity. The investigation skill's name and detailed contract remain to be agreed. Other skills need a usable blueprint; implementing those is not required to close this map. Task tickets may deliver both authorized skills under this override.
- **Founder situation:** starting solo; considering a team only after acquiring a few customers. Surface delivery effort, capital needs, customer access, and dependencies as facts or explicit assumptions. Do not turn solo status into an automatic sector or business-model exclusion. Weekly time, budget, funding preference, and income goals are unspecified; do not inherit the old project's limits or block broad discovery to obtain them.
- **Opportunity scope, clarified 2026-10-01:** focus on technology startups whose core offering is SaaS, another software product, or an AI product. Exclude physical-product manufacturing businesses such as making cars. Software serving physical industries remains eligible. This explicit user preference replaces the earlier unrestricted business-type scope; do not add further hidden preference or founder-fit filters. Geographies remain open: India, the US, and other markets are eligible according to the opportunity. The user can reject individual ideas at selection. Evaluate and expose contrary evidence honestly; eligibility does not make every idea attractive or every hypothesis true.
- **Fresh design:** `my_old_resoures/` is reference material. Its complete review is retained in [Assess what the passive-site references contribute](issues/01-assess-legacy-references.md). Do not treat its restrictions, scripts, source list, or historical benchmarks as the specification.
- **Move quickly:** use the research to resolve concrete design choices, choose the smallest useful scout and investigation handoff, and defer integrations until a demonstrated need warrants them. Do not turn the blueprint into a general startup encyclopedia or require every future skill to exist before the scout works.
- **Skills to consult:** use `wayfinder` for map operations, `grilling` and `domain-modeling` for human decisions, and `research` for research tickets. Use `prototype` for the output discussion and `skill-creator` plus `writing-for-agents` when implementing either required skill. Established repository instructions still apply.
- **Tracker:** all map, ticket, research-answer, and planning-prototype material stays under `.scratch/startup-skills/`. Open work lives in child issues, not a duplicate checklist here. Scan `issues/` in number order for open, unclaimed tickets whose `Blocked by:` entries are resolved. Record claims before work, keep answers in their tickets, and append only a gist and link here after resolution.
- **Research workflow exception:** this workspace is not a Git repository. Keep research findings and citations directly in each assigned research ticket under `## Answer`; do not initialize Git or pretend throwaway branches exist. Separate ticket ownership isolates parallel research. Findings inform later human decisions; they do not settle them.
- **Implementation destination:** the map is stored in `.scratch/`; the runnable skills' repository location will be selected in the shared-records decision. The user's instruction about the map's location is not a request to bury runnable skills in planning notes.
- **Current boundaries:** design customer research, experiment planning, and commercial preparation here. Building infrastructure for a selected startup and actually acquiring its first customer belong to later maps. This map does not authorize outreach, purchases, or running a real startup experiment.

## Decisions so far

<!-- One line per resolved child; answers live only in the linked tickets. Confirmed user scope choices live in Notes and are not invented ticket resolutions. -->

- [Assess what the passive-site references contribute](issues/01-assess-legacy-references.md): prior review retained as evidence; useful research habits identified alongside passive-site assumptions and script limitations that require fresh design decisions.
- [Research evidence for startup and commercial decisions](issues/02-research-startup-evidence.md): primary-source guidance distinguishes problem, use, purchase, and repeat-value evidence, with business-specific experiments and explicit economic assumptions; adoption remains a design decision.
- [Research discovery sources across markets and business types](issues/03-research-discovery-coverage.md): representative primary sources expose complementary market coverage and access limits; sparse online evidence leaves uncertainty rather than establishing absent demand.

## Not yet specified

- Follow-up investigations prompted by gaps or disagreement in the initial research; only create them when a concrete decision needs an answer.
- Model-specific exceptions and specialist resources whose necessity becomes visible after the suite's responsibilities and example outputs are discussed.
- Additional source adapters or automation justified by the scout prototype or behavioral checks, rather than by the existence of old scripts.
- Any additional skill implementation the user may choose beyond scouting and deeper opportunity investigation; those two skills are the required implementation floor, not the whole suite.

## Out of scope

- Scouting physical-product manufacturing businesses such as making cars; the user narrowed discovery to SaaS, software, and AI products. Software for those industries remains eligible.
- **Future infrastructure map:** automate building and provisioning the infrastructure appropriate to a selected startup idea. Retain this as the next separate effort, with prerequisites identified by the current blueprint.
- **Future first-customer map:** execute customer acquisition after that, including choosing leads, outreach, and closing the first customer. Designing customer, marketing, and sales capabilities now does not execute that later effort.
- Building a selected startup product, operating a company, and hiring a team during this map.
- Retrofitting or repairing the old passive-site project for its original AdSense strategy.
