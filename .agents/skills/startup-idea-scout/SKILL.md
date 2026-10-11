---
name: startup-idea-scout
description: Find and research one software, AI, or similar technology business idea at a time, tailored to the founder's profile. Use for open discovery, initial research of a supplied idea, or continuation; hand a selected opportunity to startup-opportunity-investigator for deeper investigation.
---

# Startup idea scout

Help the user decide whether one business deserves deeper investigation. Deliver a substantial, understandable summary supported by research and an explicit assessment against the founder's profile, with durable records another session can continue.

Each discovery round presents **one idea at a time**. Screen possible directions during research, then develop one opportunity for the user to evaluate. Keep screened leads as brief search notes rather than additional pitches or opportunity folders. A request for another idea starts a new round; a request to deepen the current idea stays with that record. If no researched idea merits consideration, explain the findings and blocker rather than inventing a recommendation. Compare saved ideas only when explicitly requested.

## Orient

Resolve the repository root from this skill's location (`../../..`). Shared instructions live under that root's `docs/startup-skills/`; opportunity output normally lives at the repository root. An explicitly supplied output workspace overrides the output root, not the shared-resource location. Resolve existing run/opportunity references before writing.

Read the [record guide](../../../docs/startup-skills/record-guide.md), [research guide](../../../docs/startup-skills/research-guide.md), and [tool routing](../../../docs/startup-skills/tools.md). Consult the [source catalog](../../../docs/startup-skills/source-catalog.md) when choosing sources; follow sources beyond it as the customer and question require. Use [CONTEXT.md](../../../CONTEXT.md) for domain terms. Runtime work does not require reading the planning tracker or the old project.

Read the shared [founder profile](../../../FOUNDER-PROFILE.md) before choosing search directions or assessing fit. Use its current experience, domain-learning limits, market, time, budget and preferences; automatically maintain it under the record guide's [profile rules](../../../docs/startup-skills/record-guide.md#founder-profile) when interactions supply new relevant information. Read recorded rejections as well: a request for a fresh idea should not automatically restore a declined or deleted proposal.

The eligible scope is software, AI, and similar technology serving **any industry and market**. SaaS and AI are examples, not requirements. Software serving factories is eligible; manufacturing cars itself is outside scope. There is no default country or closed list of product types. The founder starts solo: expose delivery effort, capital and specialist needs, without silently excluding demanding ideas. Use supplied constraints; weekly time, budget, funding preference and income targets can remain unknown for broad discovery.

Choose the entry path from the request:

- **Open discovery:** begin varied searches around customers and their work, guided by the profile. Explain why the directions are plausible for this founder and which assumptions need checking. Broaden beyond the first familiar technology community, then concentrate research on one promising opportunity.
- **Supplied idea/problem:** retain and research the original proposition. Nearby alternatives may help compare, but must not replace the brief. Follow explicit market constraints and relevant local terms/languages.
- **Continue a search:** read its saved `scouting-runs/` report for the brief, searched directions, unfinished leads and access gaps; then read the current opportunity's summary and relevant evidence/history. Continue that idea or research one fresh idea according to the request.
- **Continue an idea:** read its current opportunity folder first, following earlier runs where search context matters. If the request is deeper investigation of an already selected idea, hand off with the current record instead of running open discovery again. If the investigator is unavailable, give a usable handoff and say so; do not claim it ran.

Ask a short question only when the answer materially changes scope or resolves an ambiguous saved reference. Continue independent useful work while waiting. Tell the user where research is starting and give progress updates on findings, uncertainties and the next checks.

## Discover and pursue the questions that matter

Use independent web searches and relevant public forums to discover customer problems through tasks, frustrations, workarounds and local terminology. Follow relevant pages and links selectively. Idea lists and investor prompts are supplementary inputs; a list failure does not end discovery. Save original sources and meaningful search/access history.

Read original accounts and relevant replies, linked corrections and resolutions. Separate the reported problem from the author's proposed solution. Investigate promising leads with corroboration where available, existing products, manual processes, services and doing nothing. Search for satisfied customers and reasons the proposed product might be unnecessary. Check whether an alleged missing feature already exists or the complaint was resolved.

Follow consequential gaps beyond the first result: identify the customer and possible payer, plausible revenue mechanism, reasons to switch or stay, ways to reach customers, initial build/support work, material costs and dependencies. Use current first-party information for changing product, price or supplier claims. The research guide explains evidence limits and estimates; a candidate needs useful initial findings, not a complete business plan.

Research the chosen idea deeply enough to explain a particular customer's work, the purchase and the founder's obligations. A few complaints plus a feature list do not establish that understanding. Follow the actual workflow and the strongest alternative; investigate whether the proposed advantage matters in the target market. Where an answer depends on private customer information, state the exact unknown, why it affects the decision and what observation would resolve it.

Assess founder fit before presenting the idea as worth pursuing. Connect the actual domain learning, ability to judge output quality, customer access, technical dependencies, startup and monthly spend, and ongoing support to the profile's constraints. Explain a plausible first version and what must be learned, obtained or tested before delivery. Interests and willingness to learn are starting points, not established competence or buyer access. If a material requirement exceeds the founder's limits, make that conflict part of the recommendation. A supplied idea still receives an honest assessment of its fit.

Keep uncertain but specific opportunities visible. An investigated idea may remain weakly supported; a purely speculative idea is an unresearched lead. A competitor, limited public evidence, unknown customer access or high solo effort is a finding to evaluate, not an automatic veto. Tie confidence to individual claims, including negative findings. Research and user selection do not establish purchase or repeat-use evidence.

Before ending research, check whether accessible follow-up could change the recommendation. Pursue such questions or name the concrete blocker. A normal round can stop when the reader can evaluate the business and its founder fit, and the remaining material uncertainty needs customer evidence or targeted follow-up mainly repeats findings. Repetition in one narrow source family does not establish wider coverage. Save an explicitly incomplete round when access or the requested time/depth prevents material checks. Delivering one idea or collecting a number of links does not establish completion.

## Explain domain knowledge and learning needs

Every opportunity's `summary.md` must include a **Domain knowledge needed** section before its next steps. Explain what the founder needs to understand about this particular industry and customer task to build and deliver the proposed offer reliably. Name specific concepts, workflows, documents, quality checks or specialist judgments, and connect each to a product decision or mistake it helps prevent. General software skills and knowledge of the customer's industry are separate requirements.

Make the section useful for deciding whether to learn and pursue the idea:

- **What to understand and why:** explain each necessary topic in everyday words, with a concrete connection to the offer. Support consequential requirements from the research; label tentative ones.
- **When it is needed:** distinguish basic understanding for customer conversations and a prototype from the deeper knowledge needed for reliable delivery. Identify work requiring an experienced reviewer, partner or qualification where the actual task warrants it.
- **What the founder already knows:** use the shared profile and new supplied experience to distinguish familiar topics, learning gaps and unassessed areas. Without that information, state that the founder's knowledge is unassessed. A job title or coding ability alone does not establish domain competence.
- **How to start learning:** give a short learning order and a practical exercise or practitioner walkthrough. Say what the founder should be able to explain or check afterward. Add verified introductory resources when useful; learning-time estimates need a stated basis. Leave a detailed curriculum for a selected idea's investigation.

For example, a document checker for machining shops needs knowledge of drawing versions, units and how orders are approved. A useful learning exercise is to compare a sample order, quote and drawing with a knowledgeable shop reviewer, then explain which differences require clarification before production. Match the depth of knowledge to the founder's role and the proposed task.

If personalization would help and the user wants an interview, use manageable MCQ rounds followed by questions tailored to their answers. Cover specific industries and tasks, depth and recency of hands-on experience, ability to judge outputs, relevant technical skills, access to practitioners, and willingness/time to learn or involve specialists. Ask for concrete examples where capability matters; record answers as self-reported experience. Reuse supplied answers and leave unanswered areas unknown. Broad scouting can continue without an interview, and unfamiliar domains remain eligible with their learning and specialist needs visible.

Before saving a summary, check that the reader can identify the knowledge needed, why it matters, a practical first learning step and any expert dependency without opening other files.

## Save and explain the one idea

Use the record guide's templates as aids, filling only useful records. Save canonical evidence in `opportunities/<stable-name>/research.md`, the main decision page in that folder's `summary.md`, and the search trail and dated conclusion in `scouting-runs/`. A normal scouting round creates or updates one opportunity; it does not require `opportunities/comparison.md`. Preserve earlier outputs and record what changed unless the user explicitly requests deletion. Re-read affected files immediately before updating them so concurrent/newer findings survive.

When writing the summary or final answer, follow [explaining ideas](../../../docs/startup-skills/explaining-ideas.md) and use the [summary template](../../../docs/startup-skills/templates/opportunity-summary.md). The summary is a self-contained explanation and assessment, not a teaser for `research.md`. Use enough connected prose and concrete detail to teach an unfamiliar business; brevity is useful only when it preserves meaning.

The summary must let the reader understand and assess:

1. **Customer and present problem:** a specific customer group and market, the situation that creates the need, how people handle it now and the consequences supported by research.
2. **What we would sell:** the first offer, an imagined walkthrough from input to useful output, human responsibilities and approvals, and the scope of the initial version.
3. **Purchase and continued value:** who uses, pays and approves; what one payment buys; the proposed charging basis; why another use, renewal or purchase might occur. Keep accepted price and repeat demand unknown unless observed.
4. **Evidence and alternatives:** explain important source findings and their limits on the page, the strongest existing option and a supported or still-unproven reason to choose this offer. Source links supplement the explanation.
5. **Finding the first customers:** a concrete route suited to the target market, what it lets the founder do, and access or buying-process gaps. A directory or community is a route, not an established relationship.
6. **Building and running it:** required inputs, data access, integrations, quality checks, onboarding, exceptions and support; what can plausibly be automated and what still requires someone. Explain startup, monthly and usage costs, unpaid work and unpriced dependencies. Any numerical scenario shows its assumptions and calculation.
7. **Fit and domain learning:** explain what fits this founder, which gaps must be closed, and how learning, spend and recurring work compare with the recorded limits. Include the domain-knowledge section above. Leave unsupported feasibility or learning-time estimates unknown.
8. **Recommendation and limits:** the strongest reason to pursue and to decline, what could change the assessment, the next decision-changing question, research coverage and why the round stopped. Link the detailed evidence and dated run as optional reading.

Before saving, complete the explanation guide's comprehension check and check the practical decision: can the reader explain the business, its strongest support and weakness, what they personally would need to learn and do, and which costs or access requirements remain unresolved using this page alone? Repair missing steps and vague claims rather than adding headings or padding. Keep recommendations separate from the user's selection; avoid overall startup scores and unsupported profit or demand rankings.

On continuation, current opportunity evidence governs the new summary. Old runs preserve what was searched and concluded then; they must not overwrite later findings. For an explicitly requested comparison of saved ideas, follow the record guide's comparison rules without generating additional candidates.

Finish with a clear explanation of the one idea, the main findings and recommendation, meaningful limits, why research stopped, links to its summary/report, and the next useful choice. The user chooses whether to advance it. A handoff to `startup-opportunity-investigator` carries the current opportunity path, proposition, sources, contrary evidence, assumptions, dependencies and unfinished questions. Scouting authorizes no outreach, purchases or live customer tests.
