# Personal food assistant — preserved pre-investigation output

Recorded 2026-10-27; preserves the current views assessed 2026-10-24/25 before the first investigator update. The original scout run remains unchanged. Embedded links below are adjusted for this archive location.


## Preserved summary.md

# A personal food assistant that learns what works for you

**Current scope, 2026-10-25:** compare existing products that search for food on the user's behalf through chat or voice and remember the user. Personal location, meal budget and diet details are not prerequisites. Checkout is optional. The [latest comparison](../../../scouting-runs/2026-10-24-personal-food-assistant.md#2026-10-25--comparison-against-the-actual-requirement) finds documented close matches in Claude + Swiggy and Alexa+, with ChewIQ/Choozin as close advertised alternatives whose availability/features need verification. This supersedes the previous local-meal questionnaire and narrows the claimed opportunity: persistent personalization is already offered elsewhere. Earlier assessment below is retained as 2026-10-24 context.

When the cook is absent, the founder spends too long deciding what to order: the food must be enjoyable, fit their budget and gym goals, and avoid ingredients or spice levels they dislike or report problems with. They often fall back to Burger King. Friends reportedly describe similar frustration. These are personal accounts, not measured market demand.

The proposed product is a conversational assistant that remembers preferences, gives a short list of suitable available meals, and learns from what the person actually thought after eating. The broader ambition includes cooking, groceries and reminders; delivery is the clearest first use. This is distinct from the earlier [familiar-meal rotation](../../familiar-meal-rotation/summary.md) recommendation.

**Imagined use:** your cook cancels. You supply today's budget and what you feel like eating. The assistant uses your saved preferences and an authorized current menu source to suggest three meals with reasons and trade-offs. You choose, then later indicate whether the food tasted good, was too spicy and was worth repeating. Future choices use that feedback. A repeated fallback purchase must not automatically become a favorite.

The initial version would offer an editable profile, a small shortlist, obtainable price/availability information and optional feedback/reminders. Order placement depends on approved access. The proposed payer is the individual user, potentially paying monthly for repeated recommendations and memory; no price has been accepted. A ₹149/month scenario appears in the research solely to examine costs.

## What research found

There is substantial competing supply: Swiggy EatRight for health-oriented discovery, Healthify+ for AI nutrition coaching, MyOrderGuide for free nearby dish recommendations, and Choozin for menu personalization. Amealio and FoodAgent make related claims; FoodAgent's live integrations were not verified. Frep addresses Indian household cooking. See the [dated evidence and comparison](../../../scouting-runs/2026-10-24-personal-food-assistant.md#i001-e002).

The strongest support is the founder's specific repeated decision problem. The strongest objection is that existing platforms and assistants already offer much of the proposed experience. The potential advantage is better decisions over repeated use through explicit meal feedback. That remains a hypothesis, including whether competing products already do it well.

Swiggy documents a route for developer integration, subject to review and production approval. Zomato's official connector documentation currently restricts third-party apps. Swiggy data-use conditions also matter for long-term learning. No access was requested or tested. API access does not establish dish-level nutrition accuracy or stomach tolerance. [Integration evidence](../../../scouting-runs/2026-10-24-personal-food-assistant.md#i001-e007).

## Business requirements and founder fit

Start customer learning with willing friends and, if accessible, one local gym or apartment community. Access, conversion, price acceptance and retention remain unproven. Subscription value must exceed free choices without adding burdensome logging. Delivery commissions are not assumed.

The founder would need to direct product work, evaluate recommendations, handle support and maintain authorized integrations. Costs include models, hosting, storage, integration obligations, acquisition and quality review. At a hypothetical 100 users paying ₹149/month, twenty sessions each produce 2,000 monthly sessions; ₹2 versus ₹5 per session changes usage cost from ₹4,000 to ₹10,000 before other expenses. These are sensitivity assumptions, not quotes or profit forecasts. [Full scenario](../../../scouting-runs/2026-10-24-personal-food-assistant.md).

The existing ₹5,000/month budget and 10–19 hours/week favor a bounded investigation. AI-assisted production does not remove the need for reliable authentication, preference handling or independent quality judgment. Broader cooking/grocery support and expansion to other countries depend on results and data access.

## Domain knowledge needed

Learn restaurant portion/ingredient variability, the difference between preferences and medical requirements, total delivered prices, feedback design and honest handling of missing nutrition information. Self-reported discomfort is not proof of a cause. Nutrition rules may need qualified review; no clinical expertise has been established. Reconstructing a few actual orders is a useful first learning task.

## Decision and next step

**Investigate the clarified idea.** Test whether remembering explicit outcomes saves effort and improves satisfaction enough to earn payment. Current research is public desk research from 2026-10-24; no product benchmark, customer test, purchase or implementation occurred.

Next owner: **startup-opportunity-investigator**, if further investigation is requested, to benchmark the closest available assistants against delegated search, conversation and remembered preferences before proposing a new product. [Updated comparison and handoff](../../../scouting-runs/2026-10-24-personal-food-assistant.md#2026-10-25--comparison-against-the-actual-requirement). No further personal details are needed for the current capability comparison.

Folder identity: `personal-food-assistant`  
Stage: initially researched supplied idea; build decision unmade  
Assessed: 2026-10-24  
[Research](../research.md) · [Canonical user account](../../../.agents/skills/startup-idea-scout/references/user-leads.md#2026-10-24--clarified-food-planner-account)


## Preserved research.md

# Personal food assistant — evidence handoff

**2026-10-25 update:** the user requests a capability comparison, not personal meal planning. [Continuation and E011–E015](../../../scouting-runs/2026-10-24-personal-food-assistant.md#2026-10-25--comparison-against-the-actual-requirement) document close matches in Claude + Swiggy and Alexa+, and qualify ChewIQ/Choozin availability. These strengthen C002 and challenge uniqueness of persistent personalization under C004. Personal details are not a prerequisite. The updated handoff in that continuation supersedes the earlier next step below.

Assessed 2026-10-24. This supplied idea differs from familiar-meal rotation: delivery decisions and longitudinal preference learning are central. The original user account lives in the [lead notebook](../../../.agents/skills/startup-idea-scout/references/user-leads.md#2026-10-24--clarified-food-planner-account); public observations and calculations live in the [scout run](../../../scouting-runs/2026-10-24-personal-food-assistant.md).

| Claim | Evidence | Current assessment |
| --- | --- | --- |
| C001: founder faces a recurring decision problem | [I001 E001](../../../scouting-runs/2026-10-24-personal-food-assistant.md#i001-e001) | Supported self-report; friends secondhand; no measured frequency or time |
| C002: direct/adjacent competitors exist | [E002–E006, beginning here](../../../scouting-runs/2026-10-24-personal-food-assistant.md#i001-e002) | Documented offers; efficacy, local coverage and differentiation untested |
| C003: ordering integrations can support the workflow | [Swiggy E007](../../../scouting-runs/2026-10-24-personal-food-assistant.md#i001-e007), [Zomato E008](../../../scouting-runs/2026-10-24-personal-food-assistant.md#i001-e008) | Conditional Swiggy route; Zomato third-party app restriction; no access granted |
| C004: feedback memory improves choices | [I001 assessment](../../../scouting-runs/2026-10-24-personal-food-assistant.md#i001) | Proposed advantage; not demonstrated |
| C005: customers pay at sustainable costs | [Economics and next work](../../../scouting-runs/2026-10-24-personal-food-assistant.md#payment-acquisition-and-delivery-economics) | Hypothetical pricing/cost sensitivities; no purchase or retention evidence |

Next: startup-opportunity-investigator should perform the [recorded handoff](../../../scouting-runs/2026-10-24-personal-food-assistant.md#claim-status-and-next-decisive-work). No investigator round or customer result exists yet.
