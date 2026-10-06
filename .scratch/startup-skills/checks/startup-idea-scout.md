# Startup idea scout checks

Checked: 2026-10-06. Build owner: [Build and verify startup idea scout](../issues/10-build-startup-idea-scout.md).

The implementation is [the repository skill](../../../.agents/skills/startup-idea-scout/SKILL.md), with [shared records](../../../docs/startup-skills/record-guide.md), [research guidance](../../../docs/startup-skills/research-guide.md), [tool routing](../../../docs/startup-skills/tools.md), and one [source catalog](../../../docs/startup-skills/source-catalog.md).

## Method and isolation

Independent agents received realistic user requests, the skill path, an isolated output workspace, and the minimum supplied records. They executed the skill instead of reviewing its wording. They did not receive the implementer's expected answers. The parent read the actual comparisons, evidence records, history and final responses; the checks assess reasoning and saved state, not prescribed phrases or candidate counts.

Artifacts are temporary, under `/tmp/startup-scout-eval.rhftp2/`, outside runtime records and the working tree. The live run uses public web sources. Supplied-idea and continuation inputs are explicitly fictional fixtures; their outputs establish handling of evidence, not real demand. No outreach, account connection, purchase or live startup experiment was performed.

## Structural checks

- The skill-creator `quick_validate.py` reports **Skill is valid!**. The default Python lacked PyYAML; validation reused an existing cached PyYAML through a command-local `PYTHONPATH`. No package was installed or runtime dependency added.
- UI YAML parses and its short description meets the supplied metadata bounds. Automatic discovery remains enabled by default.
- A separate agent checked local references and the implementation against the resolved contract. The source catalog exists in one runtime location; the old planning copy is gone and planning links point to the maintained catalog. The parent rechecked links after adding `SETUP.md` and evaluation outputs.
- No executable runtime scripts were added; the skill uses existing search/page/file capabilities. The shared record templates have explicit output placeholders and link to one guide.
- The final combined pass checked 520 local link targets and 142 generated-output anchors with no errors, excluding inert fenced snapshot text. Both continuation preservation checks and the supplied-input checksum passed. `git diff --check` passed. Detailed check outputs remain at `/tmp/startup-scout-eval.rhftp2/final-link-checks.json` and `preservation-checks.json`.

## Behavioral checks

### Supplied idea, contrary evidence, and demanding solo delivery — passed

Request: explore on-premise fault diagnosis for small Indian textile mills, sold through a one-time license, using only supplied material because live research is unavailable. The fixture includes one supervisor report and its idea-list copy, an incumbent's local-alert claim, a contractor's contrary account, a login-blocked Tamil forum, an English search with no relevant accounts, and unsourced pilot cost/time guesses.

Observed: the [comparison](/tmp/startup-scout-eval.rhftp2/supplied-idea/opportunities/comparison.md) explains the original product and illustrative use, then compares it with maintenance/checklists and the incumbent. It preserves India, on-premise delivery and one-time licensing; expensive field work remains eligible and explicit. It identifies the difference between diagnosing an existing fault and predicting a future stoppage. The copied report adds no observation. Costs remain guesses, provider claims remain untested, and access failures do not imply absent demand. The result is visibly incomplete with concrete missing checks, rather than a claimed validation.

Supporting [research](/tmp/startup-scout-eval.rhftp2/supplied-idea/opportunities/india-textile-onprem-fault-diagnosis/research.md), [run](/tmp/startup-scout-eval.rhftp2/supplied-idea/scouting-runs/2026-10-06-supplied-textile-idea.md), and [response](/tmp/startup-scout-eval.rhftp2/supplied-idea/final-response.md) preserve the handoff and user-owned selection.

### Continue a saved search with newer findings — passed

Request: resume the September run comparing a UK warehouse desktop tool with a US freight API and incorporate a supplied update. The warehouse's October records contradict the old missing-export claim. The update repeats the already-recorded customer event, and freight has no new evidence.

Observed: the [new comparison](/tmp/startup-scout-eval.rhftp2/resume-run/opportunities/comparison.md) uses the current warehouse findings, changes the earlier relative recommendation with reasons, keeps freight's older evidence visibly unrefreshed, and preserves the original markets and revenue formats. The repeat submission is receipt history under existing R-01, not another observation. User selection remains undecided. The [new report](/tmp/startup-scout-eval.rhftp2/resume-run/scouting-runs/2026-10-06-resume-open-discovery.md) preserves the current reasoning and incomplete research state.

SHA-256 checks confirm the original run, prior warehouse round, supplied update, and both unrelated freight files remain unchanged. The new warehouse round also preserves the prior summary. Local output links and anchors were checked.

### Independent live discovery — passed with recorded access limits

Request: open technology discovery without a fixed country, industry or business model, while the user's usual idea list is unavailable. Public browsing only.

Observed: the [comparison](/tmp/startup-scout-eval.rhftp2/open-discovery/opportunities/comparison.md) explains software-supported machine-shop scheduling, food batch records and a Brazilian merchant ledger before presenting shared questions and a conditional relative recommendation. Independent English and Portuguese searches covered additional care, India settlement and Brazilian delivery directions; no idea list was needed. The [saved report](/tmp/startup-scout-eval.rhftp2/open-discovery/scouting-runs/2026-10-06-open-discovery.md) and [actual access history](/tmp/startup-scout-eval.rhftp2/open-discovery/scouting-runs/access-history.json) preserve original public forums, relevant replies, subsequent source reads, and omitted directions.

Substantive follow-up changed the conclusions: current scheduling products challenged an alleged feature gap; satisfied food-software users and existing onboarding challenged the proposed offer; Portuguese vendor documentation and messaging-cost checks weakened the merchant-ledger proposition. The scout investigated an initial regulatory-timing assumption with the official source and left unresolved provider rates explicit. A national directory yielded only a shell; a readable regional directory provided a fallback. IFSQN's 403, other failed pages, and incomplete extractions remain gaps, not evidence of absent demand.

The overview states possible payer/models, customer-access routes, delivery/support and specialist requirements, unpriced costs, limits on competitor benchmarks, and what would change the recommendation. No paid-demand, profit or repeat-use claim is fabricated. The normal stopping reason is the shift to customer-specific workflow and buying evidence after material desk-research questions were followed. Current summaries and canonical evidence are saved, and the dated run preserves the actual comparison rather than just linking to the mutable view.

The run records its actual progress updates and a useful optional customer-access question. No user answer was invented; a live human reply/redirect was not exercised in this isolated evaluation. The evaluator noted a substantial initial documentation footprint but completed the task without a routing or record failure. No behavioral failure in these scenarios required an instruction change.

### Continue a named opportunity — passed

Request: continue scouting the named warehouse opportunity, incorporate the repeat note and update the comparison while the user is still choosing.

Observed: the [comparison](/tmp/startup-scout-eval.rhftp2/resume-idea/opportunities/comparison.md) withdraws the obsolete warehouse-first recommendation, keeps the remaining cross-system need hypothetical, and explains why thin, older freight evidence does not automatically establish a winner. It identifies a narrower next scouting question without starting a full business investigation or changing the user's undecided selection. The repeat is attached to R-01, with its original event date still unknown. The [new report](/tmp/startup-scout-eval.rhftp2/resume-idea/scouting-runs/2026-10-06-warehouse-continuation.md) and dated round preserve what changed and the prior views. Historical reports, the supplied note, and freight records remain unchanged.

The two continuation requests produced different, explicitly conditional next-step suggestions appropriate to their scope. Neither suggestion claims stronger demand from missing or stale evidence; identical rankings were not an acceptance criterion.

## Remaining limits

Tavily is not available in the session or inspected MCP configuration, and no process key is present. Existing web-tool success does not verify Tavily. On 2026-10-06 the user deferred Tavily, recorded it in [TODO.md](../../../TODO.md), and authorized closing the scout build using the verified web tools. Hunter/Apollo account capabilities are also unverified; those are conditional contact aids. See [actual setup status](../../../SETUP.md).

Behavioral examples do not establish reliability across every market or every future model run. The future investigator/customer-connect skills and their own behavioral checks remain separate work. All fictional records stay isolated from real opportunity evidence.

## Invocation to try

`$startup-idea-scout Find software and similar technology opportunities across markets. Explain the products, compare the evidence and delivery work, and save the findings.`

The normal output destinations are `opportunities/` and `scouting-runs/` in this repository. The examples above used explicit temporary output destinations to keep evaluation records separate.
