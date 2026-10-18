# Agent skill release review — research

Current claim assessment: 2026-10-17, Asia/Kolkata.  
Scope: small India-first software/AI implementation teams that maintain their own Claude Code agent skills for client or internal work. Public English-language sources only; no buyer interview, product trial, or paid test.

## C001

**Claim:** Some teams struggle to review a changed agent skill before colleagues use it.

**Assessment and confidence:** Supported as a reported problem in particular teams, with low confidence in prevalence or India-specific frequency. [E001](#e001) describes a consultant team's informal review bottleneck; [E002](#e002) asks how to assess skill quality; [E003](#e003) and [E004](#e004) document misleading results in one official testing workflow. These sources do not show a buyer paying to solve it.

**Contrary evidence and alternatives:** [E005](#e005) describes a team that reviews skill changes as ordinary Git diffs. [E006](#e006), [E007](#e007), and [E008](#e008) already offer substantial testing, comparison, and distribution functions.

**Next useful check:** Watch a current small team review one real skill change, including the time spent assembling test cases, interpreting failures, and approving the change.

## C002

**Claim:** A simple local release report could add value beyond Git review and existing skill evaluation tools.

**Assessment and confidence:** Unresolved. The proposed advantage is an inference from a reviewer's workflow in [E001](#e001), not an observed product gap. Promptfoo already compares skill versions, records traces, and supports routing assertions [E006](#e006); Anthropic's skill-creator supports evals and comparisons [E007](#e007). A new product may merely repackage them.

**Next useful check:** Have a team use its current method and free Promptfoo on the same pending change. Observe which review decisions remain difficult and whether a concise release report changes them.

## C003

**Claim:** Small Indian firms are an accessible first customer segment.

**Assessment and confidence:** Weakly supported as a *search route*, not as demand or access. Indian developer discussions show people sharing or synchronizing agent instructions [E005](#e005), [E009](#e009). An India-based consultancy advertises team training and evaluation habits [E010](#e010), but that company is a possible alternative/partner, not a proven buyer. No warm introduction, decision maker, budget, or purchasing process is known.

**Next useful check:** Identify actual teams maintaining several client-specific skills and learn who authorizes a review tool, what data can leave the repo, and how they currently approve updates.

## C004

**Claim:** A solo founder can make a narrow, local prototype within the recorded ₹5,000/month budget.

**Assessment and confidence:** Plausible but untested. Reusing free local Promptfoo [E011](#e011) and a local Markdown report limits hosting needs; the customer would supply its own agent/model account. GitHub includes some private-repo runner minutes but bills overages to the repo owner [E012](#e012). Model/API usage, implementation time, support, compatibility changes, and any expert review are unpriced. The founder's limited independent debugging/verification experience is a material reliability risk [founder profile](../../FOUNDER-PROFILE.md).

**Next useful check:** Build a synthetic Claude Code skill fixture and measure setup time, run cost, false verdicts, and report interpretation with a technically experienced reviewer before suggesting paid use.

## E001

**Origin:** [Reddit r/ClaudeAI: reviewing and approving AI skills](https://www.reddit.com/r/ClaudeAI/comments/1x5bt9c/how_are_you_reviewing_and_approving_ai_skills/), first-person post by a self-described operations reviewer; identity and employer unverified.

**What it reports:** Technical consultants write Claude skills and small workflows in a shared GitHub repository. The author reviews them informally before use, checking input scope, missing data, metrics, and human review, and asks how to test variable outputs and keep non-engineer contributions from bottlenecking review. Replies recommend checking actual tool/API permission barriers with dummy data and using existing Claude session transcripts. This is one discussion, not independent evidence per reply.

**Context and dates:** Team location and size unknown; post displayed as recent (about three days old) when retrieved 2026-10-17. Original event date and exact publication date unknown.

**Relevant claims and limits:** Supports C001's existence in one reported team and suggests a review workflow. It does not establish Indian demand, paid budget, or that current tools fail for this team.

## E002

**Origin:** [Anthropic skills GitHub discussion #333](https://github.com/anthropics/skills/discussions/333), original question by ColinEberhardt and practitioner replies.

**What it reports:** The question asks how skill maintainers determine whether a skill performs as claimed or a pull request improves it. Replies propose representative prompts, negative trigger cases, behavior checks, comparisons, and human inspection. One commenter describes a self-built testing setup. A later reply discloses affiliation with another product; it is not counted as independent demand evidence.

**Context and dates:** Public technical community, country unknown. Question 2026-02-04; relevant replies March–April 2026; retrieved 2026-10-17.

**Relevant claims and limits:** Supports C001's technical review need, with self-selection and no purchasing evidence.

## E003

**Origin:** [Anthropic skills issue #1478](https://github.com/anthropics/skills/issues/1478), bug report by bonyohana.

**What it reports:** In a reported version of skill-creator's trigger test, subprocess errors are recorded as if the skill did not trigger; a negative test can therefore pass when a run crashed. The author supplies a code location and reproduction. GitHub showed the issue open at retrieval; current released behavior was not independently executed.

**Context and dates:** Claude skill-creator; country unknown. Opened 2026-07-25; retrieved 2026-10-17.

**Relevant claims and limits:** Supports the need to distinguish test failure from skill behavior in C001. It does not prove every installation remains affected or justify a whole new testing engine.

## E004

**Origin:** [Anthropic skills issue #1552](https://github.com/anthropics/skills/issues/1552), bug report by HiroSnow0413.

**What it reports:** The reporter captured a skill invocation while the description optimizer recorded very low trigger recall, tracing at least one cause to discarded buffered output. The issue was shown open at retrieval. No independent reproduction was performed for this research.

**Context and dates:** Claude skill-creator; country unknown. Opened 2026-08-12; retrieved 2026-10-17.

**Relevant claims and limits:** Corroborates a particular evaluation-reliability issue, not prevalence or a customer budget. Related reports about the same testing code were screened without counting them as separate customers.

## E005

**Origin:** [r/developersIndia discussion on CLAUDE.md and AGENT.md](https://www.reddit.com/r/developersIndia/comments/1tm7err/what_does_big_tech_have_in_their_claudemd_or/), reply by serene_dippity.

**What it reports:** The commenter says their team commits its `.claude` directory, including custom shared skills, to a repository and reviews diffs like other files. Other commenters mention separate context files and a separate skill repository.

**Context and dates:** India-oriented public developer forum; the commenter's own location/company unverified. Publication date not exposed as an absolute date in extraction; retrieved 2026-10-17.

**Relevant claims and limits:** Supports team use and a strong free/manual alternative. It does not say the team needs extra release software.

## E006

**Origin:** [Promptfoo: Test Agent Skills](https://www.promptfoo.dev/docs/guides/test-agent-skills/), first-party documentation.

**What it reports:** Promptfoo documents side-by-side tests of skill revisions, skill-used/not-used assertions, output checks, repetitions, trace inspection, and use with Claude, Codex, and OpenCode. Documentation, not an observed customer result.

**Context and dates:** Cross-market software tool; page shown updated 2026-10-15, retrieved 2026-10-17.

**Relevant claims and limits:** Strong contrary evidence to a missing testing capability under C001/C002. Usability, setup effort in a small team, and actual adoption are untested.

## E007

**Origin:** [Anthropic: Improving skill-creator](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills), first-party product description.

**What it reports:** Anthropic describes eval prompts with expectations, independent agent runs, comparison of skill versions or skill versus no skill, and description-trigger improvement.

**Context and dates:** Claude ecosystem, global. Publication date shown as roughly March 2026 in search; exact date not relied on. Retrieved 2026-10-17.

**Relevant claims and limits:** Shows that basic evaluation and comparison already exist. The bugs in E003/E004 concern reported versions and should not be generalized to all current installations.

## E008

**Origin:** [Tessl FAQ](https://docs.tessl.io/support/faqs) and [Tessl product page](https://tessl.io/), first-party product documentation and marketing for the same product.

**What it reports:** Tessl offers private workspaces, versioned skill distribution, inventory, activation checks, and before-and-after evaluations. The product page advertises a free tier; advertised security and quality results were not independently verified.

**Context and dates:** Global product, Indian availability/terms not checked. Retrieved 2026-10-17.

**Relevant claims and limits:** Strong alternative to registry, sync, and general release evaluation. Same vendor, counted as one alternative, not two independent observations.

## E009

**Origin:** [r/developersIndia multi-agent setup question](https://www.reddit.com/r/developersIndia/comments/1tniixs/multi_agent_setup_for_skills_files_mcp_configs/), original poster unverified.

**What it reports:** One developer asks how to keep skills, instruction files, MCP configuration, and environment variables synchronized when moving between Gemini, Claude, and Codex. The extract did not expose relevant human replies.

**Context and dates:** India-oriented public forum; location and buying role unknown. Exact publication date unknown; retrieved 2026-10-17.

**Relevant claims and limits:** A cross-tool management pain report, screened as a neighboring direction. Tessl already offers a multi-agent inventory/distribution answer [E008](#e008); one personal complaint is not team demand.

## E010

**Origin:** [SourceOfTruth Labs team training page](https://www.sotlabs.net/training), first-party India consultancy offer.

**What it reports:** A Jodhpur-based studio advertises Claude Code team workshops with team conventions and evaluation habits, with a published starting workshop price of ₹75,000 per day for up to 12 participants. This is an offered service price, not evidence of sales or a benchmark for this proposed product.

**Context and dates:** India market; retrieved 2026-10-17; offer publication date unknown.

**Relevant claims and limits:** Provides evidence of a public route to relevant firms and a service alternative. Does not show small consultancies will buy release-review software.

## E011

**Origin:** [Promptfoo pricing](https://www.promptfoo.dev/pricing/), first-party pricing page.

**What it reports:** Its Community edition is free for local/self-hosted use and advertises all core evaluation features; enterprise collaboration/support is custom-priced.

**Context and dates:** Global offer in USD/custom pricing; retrieved 2026-10-17.

**Relevant claims and limits:** Free competitor and possible underlying engine. Customer still incurs model/API and execution costs; no locally accepted price is inferred.

## E012

**Origin:** [GitHub Actions billing documentation](https://docs.github.com/en/billing/concepts/product-billing/github-actions), first-party billing terms.

**What it reports:** Private repositories receive plan-dependent included runner minutes and storage; the repository owner pays for overages. GitHub Free and Free for organizations show 2,000 included standard-runner minutes/month; usage beyond that and model/API calls are separate.

**Context and dates:** Global GitHub terms, USD for overages; retrieved 2026-10-17. No customer's plan or actual job duration known.

**Relevant claims and limits:** Bounds a possible CI supplier input under C004, not a complete product cost or guaranteed zero customer cost.

## E013

**Origin:** [OpenAI Developers: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills), first-party methodological guide.

**What it reports:** Describes defining success before writing a skill, capturing an agent run and artifacts, checking invocation and outputs, and comparing behavior over time.

**Context and dates:** Codex ecosystem; published 2026-01-22; retrieved 2026-10-17.

**Relevant claims and limits:** Useful learning method and another free alternative. It is guidance, not a report of Indian buyer demand.

## Research still needed

- Current India-based teams with multiple internally maintained skills, their real review/approval process, and a named payer. Public sources do not establish these.
- A same-task trial of Git review, free Promptfoo, and the proposed review report; especially whether a non-engineer reviewer can interpret it correctly and whether the report saves work.
- Product-specific model-run cost, API terms, test-fixture data sensitivity, permission isolation, founder support time, and deployment reliability. A local prototype and expert review are needed to price these.
- Whether reported skill-creator bugs remain in current releases. Their GitHub issue state was checked, but current behavior was not run.

The dated [scouting run](../../scouting-runs/2026-10-17-agent-skills.md) holds searched directions and access notes. No customer interview, outreach, purchase, API call, or live skill evaluation was performed.
