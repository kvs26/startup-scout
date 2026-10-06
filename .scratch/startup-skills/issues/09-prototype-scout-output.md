# Try the scout output before implementing the skill

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:prototype
Type: prototype
Mode: HITL
Status: resolved
Assignee: Codex
Blocked by: 06, 07

## Question

Does the proposed scout output give the user enough evidence, commercial context, uncertainty, and clear next actions to compare opportunities without overwhelming them or hiding ideas behind preference filters?

Use the prototype skill to create a small example under this map's directory and discuss it with the user. Include contrasting software, AI, or similar technology opportunities across industries and markets; SaaS is one possible example, not a required category. Include an incumbent, sparse evidence, and a demanding solo launch. Show what a chosen candidate passes to the deeper investigation skill. Synthetic examples must be visibly synthetic; use real citations only when actually checked. Test both open discovery and a user-supplied idea or problem.

Decide what belongs in the concise comparison and what stays in supporting records, then capture the user's reaction and agreed changes in this ticket. Link any prototype asset from here; do not turn an illustrative report into a claim that an actual startup has been validated.

Show the agreed storage relationship from [Decide shared opportunity records and skill handoffs](06-decide-shared-records.md): a short `opportunities/comparison.md` overview links to individual opportunity folders and fuller saved reports in `scouting-runs/`. Keep this planning prototype under the map's directory; it illustrates the future runtime layout rather than creating real opportunity records.

Illustrate the [scout workflow](07-decide-scout-workflow.md#answer): a useful progress update during research, the reason a round stopped or remains incomplete, and continuation that combines the saved run's search history with the opportunity folders' current findings. The comparison criteria are agreed; this prototype owns their readable presentation.

## Comments

### 2026-10-04 — Report prototype ready for discussion

Claimed by Codex after reading the map and confirming the shared-record and scout-workflow prerequisites are resolved. Applied the prototype skill to the agreed Markdown report surface; used local files under this map rather than an application or a Git branch. A read-only subagent checked the requirements against the shared records, workflow and blueprint.

The [throwaway scout-output prototype](../prototypes/scout-output/README.md) offers three presentation structures using the same visibly fictional examples: short idea cards, a comparison table, and a recommendation followed by shared questions. The proposed starting point is short cards with six compact lines per idea, important contrary evidence and delivery requirements visible, and detailed records linked. This is a recommendation awaiting the user's reaction.

The linked files illustrate open discovery, a supplied idea, sparse evidence, an incumbent, demanding solo delivery, an incomplete round, an alternate normal stopping message, continuation using newer findings without overwriting an old report, and a hypothetical investigator handoff. All records stay inside the prototype directory. No live research, runtime skill implementation or user selection is claimed.

Pending discussion: preferred presentation; whether the overview contains enough to choose the next investigation; and changes to the split between overview and supporting detail. Status remains claimed. No resolution or map decision is recorded before the live discussion.

### 2026-10-06 — User requests clear product explanations and an actual comparison

The user found that the first version merely listed different points for each idea instead of comparing them. They said a table might work, explicitly requested one block comparing the ideas, and said the language was too vague to understand the ideas from “Problem and evidence.” Earlier they asked whether every summary, research file and scouting run needed reading; the intended reader path is one self-contained comparison, with supporting files optional for the human and available to the skills.

Revised [the comparison](../prototypes/scout-output/opportunities/comparison.md) to explain each product and a concrete imagined use before presenting evidence, followed by a common comparison table and a dedicated block comparing the ideas directly. The block states relative evidence strength and delivery demands, reasons for the suggested investigation order, and what could change that order. Costs and profit remain unknown; comparative claims are limited to what the fictional records and clearly labeled delivery assumptions support.

Recorded requirements from the user's feedback: understandable product explanations, everyday language, and an explicit cross-idea comparison block. The table and exact arrangement remain a proposal; “might work” is not acceptance. The previous six-short-lines proposal is superseded. The ticket remains claimed pending reaction to the revision; no map resolution has been recorded.

### 2026-10-06 — Revised presentation accepted

After reviewing the rewritten product explanation and direct comparison, the user confirmed: “yeah this sounds good.” This accepts the revised presentation; it does not select or validate any fictional opportunity.

## Answer

Resolved 2026-10-06 through the live prototype discussion. The accepted [comparison example](../prototypes/scout-output/opportunities/comparison.md) establishes the presentation below. The [prototype guide](../prototypes/scout-output/README.md) links supporting scenarios. All example findings remain fictional.

### One understandable comparison page

Use this order in `opportunities/comparison.md`:

1. **Explain each idea first.** Say who would use the product, what it would do, and give a concrete example of someone using it. Explain the customer's work before discussing evidence. Mark imagined examples as illustrations, not observed behavior. Briefly explain what supports the problem and the main reason the proposed product might be unnecessary.
2. **Compare the ideas in a table.** Put the same questions side by side: evidence for the problem, reasons to change from existing solutions, who might pay and how, ways to find customers, what must be built and supported, costs or unpriced requirements, and the biggest doubt.
3. **Add one explicit comparison block.** Explain why one idea deserves investigation before another, where evidence is stronger or weaker, and how delivery demands differ. State the reasons and what could change the recommendation. Separate per-idea descriptions alone do not meet this requirement. Keep the user's choice open.
4. **Explain unfinished work.** Show any access failure, important unknown, older finding or unreviewed idea that limits the comparison, and why the round stopped.
5. **Link optional supporting detail.** A reader should understand the ideas and their trade-offs from this page without opening every opportunity folder or scouting report.

Use everyday words and concrete explanations. Avoid compressing an unfamiliar idea into labels such as “Problem and evidence” or unexplained phrases such as “incumbent capability.” Brevity must not make the product or comparison difficult to understand. The three fictional examples are not a required number of ideas, and their order is not a general preference for an industry or country.

### What belongs in supporting records

The overview includes decision-relevant evidence summaries, contrary findings, business requirements, assumptions and doubts. Detailed source entries, claim-specific confidence and dates, search history, access-failure detail, calculations, older conclusions and complete research reports stay in linked records. Important limitations must remain visible in the overview, even when their detail is elsewhere.

Keep the existing storage contract: `opportunities/comparison.md` is a derived current view; each opportunity has its own folder with current findings and evidence; `scouting-runs/` retains historical reports and search context. The skills read these records to continue work. The user may open them for detail but is not required to read all of them to compare ideas. Save each observation once and link to it.

### Boundaries and handoff

Relative recommendations must follow available evidence and explicit assumptions. Do not invent a cheapest, most profitable or highest-demand ranking when costs, payment behavior or relevant observations are missing. Keep confidence tied to particular claims rather than an overall startup score. Sparse evidence and demanding solo delivery stay visible without becoming automatic exclusions.

The supporting prototype illustrates [open discovery](../prototypes/scout-output/scouting-runs/01-open-discovery.md), [a supplied idea](../prototypes/scout-output/scouting-runs/03-supplied-idea.md), [continuation](../prototypes/scout-output/scouting-runs/02-continuation.md), and [investigator handoff](../prototypes/scout-output/handoff.md). Continuation combines saved search history with current opportunity findings; it never replaces newer findings with an old report. Selection carries the current proposition, evidence, contrary findings and unfinished questions into investigation; selection itself adds no demand evidence.

The accepted change is presentation, not a change to the research workflow or shared-record contract. [Build and verify startup idea scout](10-build-startup-idea-scout.md) owns implementation and behavioral evaluation against this resolution. No new decision ticket is needed; this discussion revealed no concrete need for another adapter, specialist resource or change in scope.
