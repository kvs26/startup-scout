# Startup opportunity investigator checks

Checked: 2026-10-06. Build owner: [Build and verify the opportunity investigation skill](../issues/11-build-opportunity-investigation.md).

Implementation: [startup-opportunity-investigator](../../../.agents/skills/startup-opportunity-investigator/SKILL.md), using the existing shared [record guide](../../../docs/startup-skills/record-guide.md), [research guide](../../../docs/startup-skills/research-guide.md), [tool routing](../../../docs/startup-skills/tools.md), templates and single source catalog.

## Method and isolation

Independent agents execute realistic requests with the skill and minimum raw records, without the implementer's expected answer or prior chat. A separate read-only review checks the resolved contract. Generated opportunities stay in the temporary workspace `/var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/`; they are not real project opportunities.

The textile case reuses actual output from the scout's earlier behavioral evaluation; all its customer accounts and subsequent submissions are explicitly fictional. The direct-entry case uses live public research. No outreach, purchase, account connection or live customer experiment is part of these checks. Each continuation runs in a fresh agent context using saved files.

## Structural and contract checks

- Skill-creator validation reports **Skill is valid!**. Validation reuses an existing cached PyYAML via a command-local `PYTHONPATH`; no package or runtime dependency was added.
- UI metadata parses, its short description meets the required length, its invocation names the skill, and automatic discovery remains enabled.
- Independent contract review found no actionable gaps. The skill implements all seven business areas, direct entry, scout handoff, focused tests, round stopping, result intake and deduplication, history, partial comparison updates, and customer-connect handoff.
- The shared history rule now explicitly preserves earlier calculation inputs/results and test procedures/interpretation criteria when their current files change. No separate evidence guide, catalog or glossary was created.
- Initial local-link validation checked 35 targets across the skill and shared resources with no errors. Final artifact checks cover all four completed executions below.

## Behavioral checks

### Scout handoff with sparse evidence — passed

Request: investigate the chosen Indian textile-mill opportunity using the saved scout records, retaining on-premise software and one-time licensing. Live research is unavailable; the original fixture includes a supervisor's complaint and its copied idea-list entry, a contractor's contrary view, an incumbent's claimed local alerts, failed/empty searches and unsourced founder estimates.

Observed: the [research](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/handoff/opportunities/india-textile-onprem-fault-diagnosis/research.md>) retains the original claims and evidence, distinguishes fault diagnosis from advance warnings, and covers buyers, switching, offer/terms, costs/cash, access/sales, onboarding/continued value and delivery dependencies. The user chose investigation only. High field effort remains an explicit requirement; neither solo status nor sparse sources excludes the idea.

The [first test](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/handoff/opportunities/india-textile-onprem-fault-diagnosis/tests/T001-stoppage-and-signal-walkthrough.md>) reconstructs stoppages and checks usable machine signals against the existing checklist. Conditional later tests address actual buying and continued use. Participants, procedure, material, records, contrary/ambiguous interpretations and effort limits are concrete. No test is recorded as executed. Economic examples are labeled hypothetical, distinct from the unsourced founder sketch and unknown prices; arithmetic, cash timing and unpriced work are explicit.

The [saved round](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/handoff/opportunities/india-textile-onprem-fault-diagnosis/rounds/2026-10-06-investigation.md>) preserves conclusions, calculation inputs/results and test designs. The [response](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/handoff/evaluation-response.md>) identifies the incomplete external research and unavailable customer-connect skill, linking a usable handoff. Hash checks confirm original input, R001 and the scouting report remain unchanged. The parent checked 165 local links, including 82 anchors, without errors.

### Direct idea with live research and material contrary findings — passed

Request: investigate an AI meeting-to-scope-change/approval tool for small UK digital agencies, with no prior scouting run, interviews, chosen price or budget.

Observed: the [investigation](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/direct-live/opportunities/uk-agency-scope-changes/research.md>) reads first-party meeting-tool and direct-competitor pages, practitioner replies, supplier prices, a relevant trade directory, API and official data-handling guidance. Current advertised capabilities challenge the user's summaries-only premise. Shared trackers, existing automation and deliberate free extra work challenge recoverable value. Following an older directory link identifies a changed product instead of treating stale listings as current competitors. Failed reads, extraction ambiguity, advertised-versus-tested capabilities and unknown UK-specific prevalence remain explicit.

The [economics](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/direct-live/opportunities/uk-agency-scope-changes/economics.md>) separates sourced USD supplier rates, hypothetical GBP offers, support/acquisition effort, collections and unpriced requirements. It preserves currencies without inventing an exchange rate. Lower AI usage costs do not establish viable founder economics. Customer tests separate past workflow, a buying decision, actual use and a later paid cycle; suggested prices remain proposals.

The [response](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/direct-live/evaluation-response.md>) recommends learning before building, explains the changed premise and stops where private customer records/decisions are needed. A current comparison, summary, dated round, history and customer-connect handoff were saved directly. The parent checked 90 local links, including 42 anchors, without errors. Live web success does not verify Tavily or product runtime quality.

### Fresh-session file intake with conflicting evidence — passed

A fresh agent received only the completed opportunity files and a new fictional submission. The new same-supervisor event reports short diagnosis versus long parts delays and unavailable pre-failure traces. An owner conditionally considers INR 120,000 once; a separate adapter quote asks INR 180,000 plus quoted tax, with advance payments and exclusions. An older unrelated freight candidate was included to exercise partial comparison updates.

Observed: [R002](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-file/opportunities/india-textile-onprem-fault-diagnosis/results/R002-returned-results.md>) preserves the original file and indexes the three observations without counting another independent mill. It distinguishes the user's recollections, the conditional owner comment and the supplied quote extract. Related notes do not complete the earlier planned tests. The new account makes one earlier contrary explanation more relevant without assuming all of that contractor's claims apply.

[Updated economics](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-file/opportunities/india-textile-onprem-fault-diagnosis/economics.md>) replaces the applicable invented adapter costs with the scoped quote, exposes the price/cost mismatch and cash timing, and retains unpriced work and tax uncertainty. [Revised T001](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-file/opportunities/india-textile-onprem-fault-diagnosis/tests/T001-stoppage-and-signal-walkthrough.md>) now checks incident timing, useful signals and quote scope before costly integration. The [round](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-file/opportunities/india-textile-onprem-fault-diagnosis/rounds/2026-10-06-returned-results.md>) explains changed and unchanged conclusions, retaining earlier calculation/test designs. The user's choice to continue remains separate from the narrower recommendation.

The [comparison](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-file/opportunities/comparison.md>) updates textile findings and preserves the freight assessment date and limits without declaring a new winner. The parent checked 247 local links, including 138 anchors, without errors. SHA-256 checks confirm nine protected files remain unchanged: both original submissions, R001, the scouting report, both prior rounds, the later continued-use plan, and both freight records. Machine results: [preservation checks](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-file-preservation.json>).

### Fresh-session pasted return of the same events — passed

Another fresh agent received the saved file-intake output and the same events as pasted notes with the opportunity reference. The evaluator was not told the expected duplicate conclusion.

Observed: the [receipt appended to R002](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-pasted/opportunities/india-textile-onprem-fault-diagnosis/results/R002-returned-results.md#2026-10-06-pasted-repeat-receipt>) matches participants, event dates, distinctive observations, Q-17 identity and exact quote content. Original pasted wording is saved as submission provenance. R002/E005–E007 remain the canonical entries; no R003/E008, additional customer, stronger confidence or completed test is invented. The [response](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-pasted/evaluation-response.md>) identifies the repeat and retains the same next test. A [dated intake round](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-pasted/opportunities/india-textile-onprem-fault-diagnosis/rounds/2026-10-06-pasted-repeat.md>) records the unchanged findings and receipt history; the comparison remains a partial update with the older freight assessment visible.

The parent checked 269 local links, including 147 anchors, without errors. Fourteen protected files remain byte-identical, including economics, all tests, the handoff, prior rounds, original submissions/scouting report and freight records. The prior R002 content is retained as the prefix of the updated file, followed by receipt history. Result filenames and evidence IDs are unchanged. Machine results: [preservation and identity checks](</var/folders/2z/yyvhm4bj15bgx7dcqc5cc7wh0000gp/T/startup-investigator-eval.b0uzx4zq/resume-pasted-preservation.json>).

## Review, corrections and limits

The parent inspected actual research, costs, test plans, result intake, histories, comparisons and responses. A separate reviewer also inspected the completed handoff and live-entry outputs and found no material behavioral failures. No scenario required a behavior correction to the skill. The history clarification described above was made before evaluation; one intake agent also clarified an old price-probe phrase without changing evidence or conclusions.

Across the four completed output workspaces, the parent checked 771 local links and 409 anchors with no errors. These are realistic examples, not proof of reliability across every future model run or market. The numerical fictional cases test handling and arithmetic, not real demand. A live user clarification exchange, simultaneous writes and account-specific integrations were not exercised.

Tavily remains deferred under the user's existing startup-skills follow-up in [TODO.md](../../../TODO.md); the current investigator build uses existing web/file capabilities. No Tavily connection, Hunter/Apollo entitlement or customer-connect execution was claimed. The customer-connect build and remaining service setup retain their own tickets. No new runtime script, adapter or installation was justified by these checks.

## Invocation

`$startup-opportunity-investigator Investigate an AI tool for small UK digital agencies that turns meeting recordings into client-approved scope changes and tracks extra charges. Save the findings and next customer tests.`

To return: `$startup-opportunity-investigator Continue opportunities/<name> with these customer findings: [paste notes or supply a file].`

Normal records live under repository `opportunities/`; these checks explicitly used isolated output workspaces. Existing scouting reports are retained when an opportunity advances.
