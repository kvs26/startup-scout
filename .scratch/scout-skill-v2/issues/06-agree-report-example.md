# Agree a concrete scout report with business labels and source coverage

Parent: [Research and deliver startup idea scout version 2](../map.md)
Labels: wayfinder:prototype
Type: prototype
Mode: HITL
Status: resolved
Assignee: Codex
Blocked by: 01, 04, 05, 10

## Question

What should the user see in scout v2's main recommendation, alternatives and source-coverage explanation?

Use the prototype skill to prepare a small throwaway example using clearly fictional or existing appropriately qualified opportunities, showing starting model, possible scale, evidence/uncertainty, source contributions and why one option is recommended. Show a small owned novelty app aimed at early revenue alongside a longer-term startup, and an overseas-to-India lead. Compare the first two under each selected search priority so the different rankings are understandable. Keep details in the canonical research record and make the chat understandable independently. Ask for actual user feedback before resolving. This example is not a real completed scouting run.

Carry the source-selection decision into the example: show an emerging small opportunity, why attention might grow, a concrete audience/channel and promotion or sharing experiment, expected effort/cost and the path from attention to payment. Label virality as uncertain. Demonstrate a linked request for a user-supplied transcript and continuing despite missing Instagram coverage. Keep research/preparation separate from executing promotion.

Show the agreed opening brief and how the candidate mix reflects the user's answers, including a mixed search and distinction between priority and exclusion.

Present the actual opening options as single-choice menus for the user to review. The earlier multi-select proposal is superseded. Separate customer type and geography into clear single-choice prompts; include explicit broad choices and show concrete industry/lead options or named multi-area bundles. Verify that the user can answer with one option per prompt, and that the agent does not silently select a scope or balance for them.

Include the newly requested freelance/client-work category and a concrete paid-assignment example alongside owned small products, repeatable services/agencies and longer-term startups. Show that the all-categories choice includes paid client work without conflating freelance rates with secured income or owned-product revenue.

## Comments

2026-10-29 — Claimed by Codex after checking that all listed prerequisites are resolved. Read wayfinder, prototype, grilling/domain-modeling guidance and the relevant settled decisions and existing record/explanation contracts. The ticket specifically asks for a report example, so the throwaway artifact is Markdown, rather than an application UI or state-machine demo.

Prepared [Scout report prototype — for discussion](/private/tmp/scout-report-prototype-zp0te4yf/repo/.scratch/scout-skill-v2/scout-report-prototype.md): explicit single-choice opening menus, an illustrative mixed brief, freelance recommendation and three alternatives covering owned novelty software, a longer-term startup and an overseas-to-India repeatable service. Includes conditional priority comparisons, payment/cost assumptions, source-role contributions, a linked transcript-request example, missing Instagram coverage, and progress/interruption/resumption examples. All business evidence and numerical fixtures are explicitly fictional; no campaign or promotion ran. Existing creator research supplies only the historical transcript link/access gap.

Awaiting actual user feedback on the proposed report and menus. This ticket remains claimed; no report decision, runtime implementation or prototype branch capture is claimed yet. Capture the agreed prototype on a disposable branch at resolution, then leave the decision and context pointer here for implementation.

2026-10-29 — Subsequent user feedback supersedes the preceding pending state. The user found the initial explanation long and hard to read, and reiterated that category selection must come before research. After seeing the six-part plain-language explanation below, the user replied “yeah this works.” This accepts the simple results structure, not the verbose prototype wording, fictional opportunities or illustrative search answers.

## Answer

Resolved 2026-10-29 through the user's explicit acceptance.

A fresh search first asks for the opportunity category and other missing choices under the [opening-question decision](12-decide-opening-questions.md#answer), waits for the user's answers, then researches. Explain results separately from opening questions; do not show both stages together as one confusing preview. Exact fixture wording is not a newly approved questionnaire or a selected brief.

After research, present this understandable, self-contained result in chat:

1. **The best idea:** what you would sell, who would buy it, and why.
2. **How you could earn:** how to find customers, what they might pay, and the likely costs.
3. **What it takes:** your work, learning and time.
4. **Why this idea leads:** supporting evidence, biggest doubts, and what remains unknown.
5. **3–5 alternatives:** a short explanation of each.
6. **The next step:** what to investigate before building.

Use short sentences and everyday language. Explain one point at a time; avoid dense paragraphs, repeated process explanations and unnecessary terminology. Keep the detailed research, source contributions and calculations in the linked canonical run. Chat must still explain the business without requiring the reader to open that file. Include source gaps in chat when they affect the recommendation; no separate long source inventory is required there. This changes presentation, not research depth, evidence standards, model/scale distinctions, selected priorities or the incomplete/no-winner rules already agreed.

Prototype capture: isolated local clone `/private/tmp/scout-report-prototype-zp0te4yf/repo`, branch `prototype/scout-report-2026-10-29`, commit `5bd972aa309513dd68c9f6cfff601427d3cd3927`. Artifact: `.scratch/scout-skill-v2/scout-report-prototype.md` at that commit, linked above. The archive includes the planning context and the acceptance correction at the top; the earlier verbose draft is retained only as a historical fixture. Verified the committed artifact matches the revised prototype and the archive working tree is clean. The disposable clone is temporary; the accepted decision is fully recorded here and does not depend on retaining the archive. Removed the throwaway prototype from the main working checkout after capture.

Next owner: [Update and verify the agreed scout version 2](07-update-verify-scout.md) carries this structure into runtime instructions and examples, with readability checks. That task still awaits [Connect and verify the agreed research access routes](09-connect-research-access.md), the next open frontier ticket. No new decision ticket or glossary term is needed. Runtime report changes have not been implemented by this decision ticket.
