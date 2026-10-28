# A personal food assistant that helps you choose—and remembers the result

When the cook is away and you are hungry, choosing delivery can become a long search through dishes you do not quite trust. You want something enjoyable, reasonably priced and compatible with your preferences. The proposed business is software that does that search through conversation, offers a small useful shortlist, and remembers what you actually liked after eating. Checkout is optional. Cooking, groceries and reminders remain part of the broader ambition; delivery is the first experience to investigate.

**Imagined example:** you ask for a filling dinner within today's budget. The assistant knows that your usual burger is a reluctant fallback, that you disliked a particular spicy dish, and that you want something different tonight. It searches an authorized current menu source and presents a few available dishes, explains the trade-offs, and distinguishes listed item prices from a verified delivered total. Each suggestion should include a usable route to the actual dish; exact item-link support still needs verification. You choose where to order. Later, a short optional reply records whether you would have that meal again. It must not turn an uncertain ingredient or guessed calorie count into a confident promise.

The proposed customer is an adult who orders delivery often enough for this memory to matter and finds choosing frustrating. That is a candidate segment, not an established market. The individual would use, approve and pay for the product. A working offer to test is ₹149 for 30 days and up to 20 decision sessions; food costs are separate. Nobody has accepted that price. Occasional users may fit a small prepaid pack better than a subscription.

**Assessment, 2026-10-27: worth a focused customer comparison; a full build is not yet justified.** Your reported problem is specific, and a better experience could win in an existing market. But conversation and memory are already offered by competitors, menu data has important gaps, and we have no payment or repeat-use evidence. This is a usable first investigation round, with hands-on benchmarking still outstanding.

## What has become clearer

The [original account](../../.agents/skills/startup-idea-scout/references/user-leads.md#2026-10-24--clarified-food-planner-account) supports your personal experience. Friends reportedly share it, but we have not interviewed them independently. We do not yet know whether the strongest buyers are frequent delivery users, people temporarily without a cook, or another group. Gym interest alone does not establish demand.

In your [follow-up report](results/R001-founder-assistant-experience.md), you said an assistant you tried gave answers that were too general and did not provide a direct food link. That sharpens the desired outcome: a specific obtainable meal you can open, with little searching left. You subsequently clarified that this was ordinary ChatGPT/Claude use on your Android phone, without food-specific setup. It does not yet show how a connected food assistant performs. You are willing to try an existing product and report the gaps.

The strongest business doubt is that a well-configured existing assistant may already be good enough. Our proposed advantage must be an observable improvement: less choosing effort, fewer rejected suggestions, or meals people are happier to repeat. Remembering more information is useful only if it improves those outcomes with little extra work. It is not yet a demonstrated advantage, and we have not established that competitors lack it. [Claims and evidence](research.md#c002).

| Alternative | What it already offers | What remains uncertain |
| --- | --- | --- |
| Claude + official Swiggy connector | Documented conversational discovery plus Claude's general memory; web setup carries over to Android | Actual food recall, exact dish links, account access and repeat-choice quality; combination untested here |
| ChatGPT + Swiggy Food | Official Swiggy repository publishes a plugin link | Directory search here found no match; user access and Android experience untested |
| Alexa+ | Documented conversational delivery with Grubhub/Uber Eats and preference personalization | Region/device access; checked India material still calls Swiggy delivery forthcoming |
| ChewIQ | Advertises restaurant conversation and learning from dining feedback | Linked app listing emphasizes cooking/nutrition; installed restaurant capability and India coverage unconfirmed |
| Choozin | Advertises conversation, menu reading and saved preferences; credit pricing | Website says coming soon; app-listing access failed |
| MyOrderGuide | Advertises free nearby dish shortlists | India coverage, full conversation and outcome memory unconfirmed |
| Healthify+ | Broader coaching/tracking; checked promotional ₹399/month or ₹1,499/year | Not established as delegated local delivery search; competes for health-related spending |
| Native discovery, favorites and friends | Familiar tools or recommendations without another product to adopt | Some people may already be satisfied; others may want variety or less searching |

These are documentation comparisons, not tested rankings. [Sources and qualifications](research.md#e020). General-assistant access is not necessarily an expensive paid dependency: Anthropic currently documents memory and web connectors on free plans, though actual limits and this food flow need testing. Requiring an extra app, profile setup, account connection and feedback creates switching costs even if the subscription is inexpensive.

## What a credible first offer requires

The first useful outcome should arrive after a short preference setup: search on the user's behalf and give specific dishes and usable links without making them collect menus. Check whether each link opens the intended dish, just a restaurant menu, or an unhelpful app homepage; measure any remaining manual search. Exact dish links are a proposed requirement, not a verified integration capability. Ask only for what matters to that meal, then let them correct the profile. Requiring menu uploads may help an early ranking experiment, but would fail to test the full search-delegation promise.

Repeated value could come from remembered disappointments, sensible variety, changing budgets and fewer corrections. Repetition may also reduce the need for the service once someone has found several reliable dishes. The product must earn a place in the next ordering occasion; notifications and logging are not evidence of value.

The largest delivery dependency is approved access to current supply. Swiggy documents a developer application route, with conflicting development/staging instructions that need clarification. Zomato's current published connector policy disallows third-party apps. Commercial permissions, charges and operating limits for this founder are unknown. Leaving checkout to the user reduces transaction work, but does not remove menu-data permissions. [Access evidence](research.md#e016).

There is also a concrete information limit: the two checked Swiggy menu schemas do not guarantee structured calories, protein, allergens or spice intensity. Descriptions might include some information; coverage and accuracy remain unmeasured. A restaurant's preparation can vary. Prioritize preference-based discovery and clearly sourced disclosures; accurate nutritional or medical guidance would require evidence and qualified review beyond this investigation. [Data evidence](research.md#e018).

User-entered preferences and platform-derived history need distinct handling. Retention, consent, deletion and model-processing locations are delivery requirements under the checked provider policy. Rights to maintain the intended long-term memory must be confirmed. A qualified contract/privacy review may be needed for the selected design; its cost is unpriced. [Provider conditions](research.md#e017).

## How this could make money—and what could consume it

A subscription is a hypothesis for frequent use, not the default answer. A prepaid pack could serve infrequent occasions, but yields less revenue per buyer. Delivery commissions and sponsored placements are not assumed: no agreement exists, and incentives could undermine trusted recommendations. Selling to gyms or restaurants would introduce a different buyer and requires separate research.

At a hypothetical 100 subscribers paying ₹149, monthly collections are ₹14,900. With 20 sessions each, 300 additional trial sessions, a ₹1,000 fixed-cost allowance, ₹4,000 acquisition spend and illustrative recurring-payment fees, a ₹2/session cost leaves about ₹4,774. At ₹5/session it loses about ₹2,126. Both exclude your pay, sales taxes, refunds, specialist review and unpriced contract obligations. These are sensitivity cases, not forecasts. [Formulas, sourced inputs and limits](economics.md).

Text generation itself may be inexpensive. But free users, long searches, failed calls, support and customer acquisition can consume the margin. Even ten support minutes per month for each of 100 payers is 16.7 hours, before development and recruitment. Manually selecting every meal would be much harder to fit into your usual 10–19 hours/week. The roughly ₹5,000 monthly budget can support a bounded comparison using existing tools; affordability of a reliable production service is not established.

## Reaching customers and founder fit

You report being able to recruit friends, and want the first trial limited to them. Start with friends who actually face the problem and agree to compare a few natural ordering occasions; no individual agreement is recorded yet. Friends can reveal usability failures, but their praise or willingness to help is weak evidence of a wider paying market. Access beyond friends remains unresolved and is not needed to begin this first comparison. The buying sequence to examine is introduction → actual meal-choice comparison → optional paid offer → voluntary use → later renewal. Track organizer/recruitment time as well as cash. A creator showing a real useful choice might become a later channel, but audience size and low-cost acquisition cannot be assumed.

Your firsthand problem experience and ability to direct AI production are useful starting points. The less familiar work is evaluating suggestions independently, handling incomplete restaurant data, managing integration failures, and understanding consent and product promises. A computer-science background and small published sites do not yet demonstrate those capabilities. Broadening immediately into delivery, cooking, grocery shopping and nutrition coaching would add dependencies before we know which use earns payment.

A useful learning order is to reconstruct a few actual orders, compare what was known before eating with what was learned afterward, and try the best existing assistant with explicit preferences. Then inspect current menu data and the reasons suggestions failed. Before implementing nutrition rules, have a suitably qualified practitioner review their scope and evidence; the price and availability of that help are unknown. Do not infer mastery from a few days of reading.

## Next decision and handoff

**Recommendation:** first try Claude with Swiggy on Android using the [personal trial instructions](tests/T001-existing-alternatives.md#android-founder-trial), then decide whether to extend [T001: existing-alternative comparison](tests/T001-existing-alternatives.md) to friends. Current Claude documentation allows one custom connector on Free; setup and useful output remain to be verified. The Swiggy-published ChatGPT plugin is an optional alternative with account access unconfirmed ([sources](research.md#e032)). Find out whether the ordinary app, a properly configured assistant, or a dedicated available competitor already solves the recurring problem. If it does, the next decision may be to use that solution or change the offer. If a repeated consequential failure remains, specify the improvement before requesting production work. Only then proceed to [T002: actual payment and continued use](tests/T002-payment-and-repeat-use.md).

**User selection:** on 2026-10-27 you selected this opportunity for proper investigation. You have not selected a build, launch, price, country restriction or live test. Your later answers are saved in [R001](results/R001-founder-assistant-experience.md): general answers/no food link from ordinary ChatGPT/Claude on Android, willingness to try a connected product personally, and friends only for the first recruited trial. No connected trial result has yet been supplied.

**Immediate next owner: user**, to try an existing connected product on Android over a few natural meal decisions and return the actual suggestions, link outcomes and later preference corrections. **startup-opportunity-investigator** then reassesses the gaps. Bring the review with: “Reassess `opportunities/personal-food-assistant/` using my T001 Android trial notes; distinguish setup, link, recommendation and memory failures.”

If a friend comparison is still useful, **startup-customer-connect** prepares it. That skill is available but has not run. Later handoff:

> Use `opportunities/personal-food-assistant/summary.md`, `research.md` and `tests/T001-existing-alternatives.md`, plus `FOUNDER-PROFILE.md`. Prepare recruitment and learning conversations with adults who face repeated delivery decisions, including satisfied users of favorites or existing assistants. Preserve delegated search, conversation and memory as the requirement; checkout is optional. Use the first-trial constraint of friends only. Read `results/R001-founder-assistant-experience.md`; check actual dish links and remaining manual search. Confirm individual participation instead of assuming agreement. Do not claim a product exists, nutrition is verified, or participants have agreed. Prepare only; do not send messages or run tests. Return actual observations to startup-opportunity-investigator under this opportunity path.

## Research limits and saved work

Public research refreshed the closest alternatives, provider rules, menu schemas and cost inputs. A browser connection failed before the public demo could be used; no logged-in product benchmark occurred. Some app listings, original discussion pages and one reported hands-on review could not be opened. Search extracts and vendor advertisements remain qualified. Sources skew toward English-speaking, digitally active users; no representative market-size or willingness-to-pay estimate is warranted.

This round stops because the next decisive facts are real comparative behavior, provider approval and payment/return behavior. More similar marketing pages would not resolve them. No outreach, purchase, order, implementation or live customer test occurred.

Folder identity: `personal-food-assistant`  
Current assessment: 2026-10-27  
Stage: first investigation complete; awaiting comparative/customer evidence  
[Research](research.md) · [Economics](economics.md) · [Initial round](rounds/2026-10-27-business-investigation.md) · [Food-link round](rounds/2026-10-27-actionable-food-links.md) · [Android trial round](rounds/2026-10-27-android-product-trial.md) · [History](history.md) · [Earlier scout](../../scouting-runs/2026-10-24-personal-food-assistant.md)
