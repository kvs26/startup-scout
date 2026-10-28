# T001 — Does an existing assistant already solve the recurring decision?

Prepared 2026-10-27; revised after [R001](../results/R001-founder-assistant-experience.md). The [earlier round](../rounds/2026-10-27-business-investigation.md#test-design-snapshot) preserves the initial design. Status: **proposed; no participants recruited or sessions performed**. [Current offer](../summary.md); claims [C001–C004](../research.md#c001) and [C006](../research.md#c006).

## Decision and participants

Decide whether there is a repeatable, valuable failure in existing alternatives that warrants a dedicated product. Begin with willing adult delivery users who report difficult choices and expect several naturally occurring orders soon. Include frequent orderers and occasional cook-absent users separately; include someone satisfied with reorders. Users are proposed payers/approvers. The first recruited group trial is limited to the founder’s friends, per R001; the founder first wants to try existing products personally. Their individual willingness and fit remain to be checked.

Start with the small number of friends who actually agree; no fixed cohort size is a prerequisite. The founder reports being able to approach friends, not that anyone has agreed. Friendship and helpfulness can bias praise, use and payment. Wider recruitment belongs to a later test, not this first run. Never induce extra food orders just to fill the study.

## Android founder trial

This is an exploratory personal review over two or three naturally occurring meal decisions, not customer validation. No extra order or paid subscription is required by this plan. Current sources and access caveats are in [E032–E034](../research.md#e032).

1. In the browser at [claude.ai](https://claude.ai), use the same account as the Android app. Open Customize → Connectors → Add → Custom → Web. Name it “Swiggy Food”; enter `https://mcp.swiggy.com/food`, then follow the authentication prompts. Claude currently documents one custom connector on Free. Record missing options, authentication failures or usage limits; do not classify them as recommendation failures.
2. Reopen Claude on Android with that account and enable Swiggy through the chat's connector menu. Verify that it actually uses the connector; an ordinary chat answer is not a connected test.
3. Optionally check the [Swiggy-published ChatGPT plugin](https://chatgpt.com/plugins/plugin_asdk_app_6a3de8146ae4819186b6799a5d907074). Its accessibility to this account is unconfirmed; the directory search here had no match. There is no need to test both products initially.

Suggested prompt, replacing brackets with real preferences:

> Use the Swiggy connection to find three specific meals available for my delivery location [area/address] now, within [budget]. My preferences are [likes, dislikes, dietary restrictions]. Give the exact dish and outlet, listed price, why it fits, and a real food link if the source provides one. Say whether delivery fees and taxes are included; label anything unverified. If you cannot provide an exact dish link, say so and show the best supported route. Do not invent links or nutrition figures. Do not place an order.

Record setup time separately from choosing time. Open each suggested link and note exact dish / correct restaurant menu / homepage / wrong or broken destination. Note any remaining search and whether the recommendations are actually appealing. Save the response with personal details removed if sharing it.

After a meal you independently chose to eat, supply brief honest feedback and ask it to remember your preference. On a later occasion start a new chat and see whether the correction affects suggestions. Include a reluctant fallback only if it is truly your experience; do not plant artificial preferences. Record no-order occasions and skipped feedback too.

Return: product and connection used; setup outcome; actual suggestions and link destinations; remaining effort; what you ate and liked if applicable; whether later suggestions used the correction; whether you would voluntarily use it again. A failed setup is useful evidence even if no meal session occurs.

## Procedure and material

R001 now identifies ordinary Android ChatGPT/Claude use without food-specific setup. A connected baseline has not been tried. Complete the personal trial below before deciding which failures friends should compare.

1. Reconstruct the last three actual delivery decisions: trigger, time spent choosing, discarded options, final spend, satisfaction, and what happened when the choice was easy. Ask to see relevant history only with permission. Distinguish dislike, price, lack of choice, dietary uncertainty and browsing for enjoyment. Ask what has already been tried; do not lead with our product.
2. Have each person use their ordinary method on an upcoming occasion. Record active time until an acceptable choice, including app switching. Capture whether a favorite was chosen willingly or reluctantly.
3. On comparable occasions try Claude with official Swiggy access, if available to that participant, using the same preferences and exclusions. Give the baseline a fair setup: save/edit the profile and explicitly record actual feedback. Record setup minutes separately. Confirm sensitive-memory settings with the participant; collect no unnecessary health history. A permitted available dedicated app can be another comparator, but inability to access it must remain an access result.
4. Use a new conversation on a later occasion. Test recall, a changed budget, a disliked fallback, and a request for variety without introducing preferences the participant never supplied. Optional voice comparison is useful only when available. Stop before checkout unless the participant independently wants to order normally.
5. After food is eaten, ask briefly whether it was enjoyable, too spicy for their preference, filling enough, and worth repeating. Record skipped replies and the time spent giving feedback. Later, leave the person free to choose their usual method without researcher prompting.

Material: ordinary delivery apps, an available existing assistant, a participant-owned editable preference note, and a simple observation sheet. No new app is required. If no connector is accessible, a user-supplied menu exercise can isolate ranking quality, but label it a partial test: it does not test delegated search or real-time availability.

For each suggestion, record whether it is general advice, a named dish/outlet, or an exact item/variant; the source and check time; whether a link is supplied; and where that link actually opens (broken, app homepage, restaurant menu, or intended dish). Check location-specific availability and price certainty. Measure remaining search, taps and time to an order-ready choice. A restaurant link requiring another hunt is not equivalent to an exact item link. Use sourced supported links; never invent a destination. If exact linking is unsupported, record and evaluate the fallback rather than promise direct access.

For each event record participant ID; date; meal context; method; pre-existing preferences; setup/decision/feedback time; rejected suggestions and why; corrections; available dish and price evidence; unverified nutrition statements; chosen item and actual total if ordered; after-meal report; and researcher assistance. Keep absent orders and skipped occasions in the record. One participant across many meals remains one participant.

## Interpretation

| Observation | Next decision | Limit |
| --- | --- | --- |
| General answers or missing food links disappear after correct setup | Investigate onboarding/setup value before claiming a missing product capability | Does not prove every participant can reproduce the setup |
| Specific choices still leave repeated manual searching or links open the wrong destination | Test whether authorized data can support a materially easier path to the dish | A plausible URL or positive friend comment is not a working experience |
| Existing assistant repeatedly gives acceptable choices, remembers corrections and is used voluntarily | Prefer using/configuring the existing solution; require a different specific unmet need before building | Does not prove every segment is served |
| Several participants independently encounter the same failure and experience a material consequence | Specify that failure as the proposed advantage; ask whether it can be fixed without unavailable data | Complaints alone are not payment evidence |
| Wrong choices arise from missing menu/ingredient data shared by all tools | Resolve data access or revise promise before product work | Better prompting alone is not a demonstrated fix |
| Feedback takes as much effort as it saves; participants stop returning | Revise memory/feedback expectations or target audience | Missing replies are ambiguous, not automatically rejection |
| Gains appear only with founder curation or repeated reminders | Record assisted-service value and labor separately | Does not establish self-operated software value |

Compare within-person occasions and inspect individual failure traces, not just an overall average. Different cravings, prices and menu availability prevent a clean causal experiment. Before examining outcomes, ask each participant what amount of effort or disappointment would make a change worthwhile; retain their criteria. Investigate disagreement rather than inventing a universal conversion percentage.

## Effort and return path

Planning allowance: 20–30 minutes initial walkthrough/person, several natural occasions over roughly two weeks, and 5–10 minutes final discussion. Founder scheduling/review may take 4–8 hours/week for a small batch; this is an unmeasured estimate. Low-frequency users may need longer. Participants buy only food they already intended to buy; incentives and paid assistant access remain unpriced/unapproved.

Immediate next owner: **user**, to try an existing connected product on Android and return a review. Then **startup-opportunity-investigator** assesses the actual gaps. If a group comparison is still useful, **startup-customer-connect** prepares friend-only recruitment/conversations before the **user** conducts voluntary comparisons. Return notes or files referencing `opportunities/personal-food-assistant/` and T001 to **startup-opportunity-investigator**. Preserve actual wording, access failures and contrary outcomes. No result IDs are allocated before real events.
