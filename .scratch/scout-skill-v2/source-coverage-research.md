# Source coverage and category research for scout version 2

Checked: 2026-10-28. Research for [Research source categories, coverage and remaining access gaps](issues/03-research-source-coverage.md). These are proposals for the human decisions, not adopted runtime policy. Creator names and platform details belong to the sibling creator research.

## Main finding

The strongest addition is a portfolio of complementary evidence roles, not a longer mandatory website checklist. Existing discovery already requires original customer accounts, current alternatives, costs and contrary evidence. The new launch directories, problem banks and creator material can broaden the candidate pool while preserving that depth. Category workers should discover and explain leads; a coordinator should merge them and commission full assessments of distinct propositions.

## Existing contracts to preserve or explicitly revise

- [Scout](../../.agents/skills/startup-idea-scout/SKILL.md) and [discovery](../../.agents/skills/startup-idea-scout/references/discovery.md): software/AI/similar technology; user-chosen scope when broad; at least 50 distinct deeply researched propositions across an open campaign. Source entries and quick screenings do not count. Supplied-idea and explicit smaller exercises are exceptions.
- [Current source catalog](../../docs/startup-skills/source-catalog.md): already covers practitioner communities, forums, reviews, GitHub issues, occupational work maps, public procurement, official market context, YC RFS and a source-linked ideas repository. These must not disappear beneath startup launch sites.
- [Research guide](../../docs/startup-skills/research-guide.md): a source supports a specific claim; launch attention, founder revenue claims and customer experience are different kinds of evidence. Follow original accounts and relevant replies.
- [Record guide](../../docs/startup-skills/record-guide.md): one canonical run file, stable namespaced evidence anchors, one stored observation per underlying event. Temporary worker notes may be consolidated; persistent category dossiers would change this contract.
- [Tool guide](../../docs/startup-skills/tools.md): supports ordinary web reading and conditional selected tools; currently says additional research agents have not been selected. The requested category delegation will require updating this statement together with scout instructions after design decisions.

## Proposed category boundaries

Assign by the role of the evidence, rather than making every domain exclusive to one worker. Give each URL/query batch one owner to avoid duplicate retrieval. A company can appear in several categories without becoming several ideas.

| Category job | Candidate starting sources | Distinct contribution and stopping point |
| --- | --- | --- |
| Customer situations and problem banks | Razorpay Fix My Itch; chosen practitioner community; relevant product forum/review channel; Startup India briefs | Collect attributable situations, workarounds and desired experiences. Separate a curated problem prompt from a direct customer account. Follow a prompt toward the latter. |
| New products and overseas models | YC Directory; BetaList; Product Hunt; Show HN; Peerlist if accessible | Identify actual offers, users and geographic coverage. Capture the named original product, not just a generic idea. A launch does not establish adoption. |
| Business economics and failures | Indie Hackers; public Starter Story entries; Microns summaries; Failory | Find business models, acquisition paths, operating effort and failure causes. Identify self-reports, estimates and seller claims; trace important numbers. |
| Creator-led ideas | YouTube/Instagram and original associated sites, selected after sibling research | Extract specific propositions and cited businesses; distinguish first-hand operations from advice, promotion and resold narratives. Do not infer scale from platform or views. |
| Changes, themes and context | YC RFS; relevant official datasets/challenges; Springwise or trend sources when useful | Identify changing conditions and neglected audiences. Investor/editorial themes and search interest are context, not customer validation. |
| India fit and alternatives | YourStory; local company sites; regional practitioner sources; SaaSHub/AlternativeTo as pointers; official local context | For shortlisted overseas models, search Indian and global substitutes serving India, reachable customers and meaningful adaptation. For a non-India brief, use the chosen market instead. |

These groups need not all run before any result is integrated. The India/alternatives job is often more useful after the first foreign leads arrive. Ask HN customer accounts belong in the first job; Show HN launches in the second. A founder interview linked from a launch can be handed to the economics job. An original interview republished on several sites remains one underlying source.

Portfolio options for discussion:

- **Balanced initial option:** cover all relevant roles with roughly 10–14 named source families in an ordinary broad campaign: Razorpay + one relevant customer community + one review/forum channel; YC Directory + BetaList + Show HN; Indie Hackers + Microns or a readable Starter Story selection + Failory; a small creator sample chosen by the other ticket; YourStory + direct Indian competitor pages; YC RFS or relevant official context. Overlap and substitutions mean this is an effort estimate, not a verified optimum or fixed completion gate.
- **Broader option:** add Product Hunt and one theme-matched trend/innovation source; use additional creator viewpoints or regional-language sources when they expose a real missing population. Prefer this to reading many similar launch directories.
- **Licensed-data option:** only when an unresolved query needs structured company coverage, evaluate Tracxn, Dealroom, Crunchbase or Inc42 exports. Their presence on a list does not justify subscriptions or API setup.

The dated [28-entry report](2026-10-28-discovery-websites-research.md) holds provider details and original citations for these options. Its API claims were documentation checks, not authenticated integrations; this audit does not silently upgrade them.

## Fresh access checks and material gaps

| Source / route | Observed in this research | Practical implication |
| --- | --- | --- |
| [Razorpay Fix My Itch](https://razorpay.com/m/fix-my-itch/#all-problems) | Public reader returned top-ten prompts and the initial B2B table, with category labels. Desktop/mobile copies duplicate rows. Full category contents, details and pagination remain unverified. | Useful bounded Indian problem sample today. Do not claim all advertised problems were enumerated. A working interactive browser or provider export is needed only if selection depends on wider coverage. Prior browser initialization failure was not repeated. |
| [BetaList homepage](https://betalist.com/) and [help](https://betalist.com/help) | Public reader returned dated listings and a next-page link. Official help describes pre-launch and live products, paid submissions, and API access approved case by case. No authenticated API or next-page interaction tested. | Public selective discovery works without Playwright. Account/API integration is optional; editorial/payment selection affects coverage. |
| [Official HN API](https://github.com/HackerNews/API) and [Show list endpoint](https://hacker-news.firebaseio.com/v0/showstories.json) | Documentation describes item/comment retrieval and up to 200 Ask/Show IDs. The Show endpoint returned JSON IDs through the web tool. A selected item endpoint subsequently failed through that tool. | There is a supported structured route, with a partially successful runtime test. Do not claim full comment traversal works in this environment. Public HN pages remain the ordinary-reading fallback. |
| [Trend Hunter RSS page](https://www.trendhunter.com/rssfeeds) and [feed](https://www.trendhunter.com/rss) | Official RSS page readable; web feed reader rejected text/xml. A Python urllib attempt failed with hostname/DNS error before XML parsing. | Feed contents remain unverified here. This is a tool/network limit, not evidence of a dead feed or a need for Playwright. Defer it or use public editorial articles. |

No paid account, provider contact, installation or authenticated call was performed. No full directory was crawled. A bounded access question can remain open without blocking selection of a useful public-source portfolio. Revisit blocked providers only if they offer coverage that accessible substitutes cannot supply.

## Proposed coverage and sampling rules

A source-family count alone is a weak quality measure. Suggested audit fields per category: intended audience and geography; search terms/language; date range and selection method; records actually inspected; relevant leads; duplicates; access state; evidence roles present; and the next material gap. Distinguish not attempted, access failure, searched with no relevant results, and findings.

Use a mixture of recent listings and older operating businesses; popular and ordinary entries; positive use and failure accounts. Sample by the chosen industries and buyer roles, not only the homepage trending list. For themes with local buyers, include local terminology and relevant language searches. Describe sample bounds honestly; do not label a convenient list random or representative.

Suggested completion checks for source coverage are substantive: each chosen search area has an explained search path; promising leads have original/customer and alternative evidence beyond the seed site; foreign-to-India ideas received a local substitute check; commercial claims have provenance; concentration by audience/motive/model is visible; unavailable channels have a useful fallback or explicit gap. Exact minimum families and per-category sampling budgets are policy choices still for the user. None replaces the existing 50-deep-assessment requirement.

## Proposed delegation and integration

The available runtime for this session allows four agents total, including the coordinator. That means at most three simultaneous research workers here. Future runs should inspect their actual capacity and queue categories in waves; do not hard-code six simultaneous spawns or assume each category needs a permanently running worker. If delegation is unavailable, execute the same category briefs sequentially and disclose that fallback.

Give each worker: chosen scope and founder constraints; owned role and source shortlist; related known ideas/rejections; bounded retrieval questions; expected provenance fields; and a temporary output destination. Require leads to contain customer, offer, paying reason, geography, original business/source URL, source dates, claimed traction type, contradictory information and access limits. Any potential-scale label is provisional and depends on the later human-approved taxonomy.

After each wave, the coordinator merges leads into a registry using both canonical product/domain identity and the commercial proposition (audience, offer, buying reason, route to market). Preserve name/domain aliases and cross-post provenance. A distinct original company is not automatically a distinct proposed opportunity; multiple companies can illustrate the same model. A different segment counts separately only with a changed commercial case and its own substantive assessment, as the existing discovery guide requires.

Then allocate full research by distinct proposition or small related batches. Category discovery and full assessment are separate work states. The coordinator owns canonical IDs, deduplication, depth audit, final comparison and run-file writes. Workers can supply temporary evidence; they should not race to edit one shared report. On interruption, consolidate available work and save an incomplete checkpoint with the actual distinct completed count. Three worker lists of twenty leads are not sixty completed assessments.

## Remaining human decisions and next owner

The user, through the map's decision tickets, should choose the source breadth policy, creator/source selection, scale taxonomy, whether India adaptation is standard or brief-specific, and acceptable per-category effort. Implementation can then update scout discovery instructions, the shared source catalog/tool guide, report/assessment templates and any affected workflow-map responsibility wording together. Preserve canonical evidence and research/production boundaries.

Research capture: this artifact is to be committed on a disposable research branch; the exact clone path, branch and commit are recorded in the owning ticket so the artifact does not require a self-referential commit hash.
