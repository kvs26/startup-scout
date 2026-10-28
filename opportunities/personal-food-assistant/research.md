# Personal food assistant — research and claim assessment

Assessed 2026-10-27, Asia/Kolkata. First investigator round: public research completed; hands-on comparison and customer validation outstanding. The user selected this idea for investigation, not building. Scope remains delegated food search through conversation, remembered preferences, and optional checkout. India is the inherited initial delivery scenario, not a permanent geographic restriction.

## Evidence identity and earlier work

E001–E015 retain their original home in the [scout run](../../scouting-runs/2026-10-24-personal-food-assistant.md#i001-e001). The [October 25 correction](../../scouting-runs/2026-10-24-personal-food-assistant.md#2026-10-25--comparison-against-the-actual-requirement) governs scope. No personal meal questionnaire is needed for this research. [Previous current views](rounds/2026-10-25-pre-investigation-snapshot.md) are preserved.

New observations start at E016. Rechecks of the same vendor are updates, not independent corroboration. Unless specified, source publication/event dates are unknown; all retrievals are 2026-10-27. Advertisements establish offers, not delivered performance or sales. Later the same day, [R001](results/R001-founder-assistant-experience.md) supplied a founder report of ordinary mobile ChatGPT/Claude use (clarified later that day) and friend-only initial recruitment. This is one founder account, not an independent customer sample.

## C001

**Claim:** the founder faces recurring difficulty choosing delivery meals.

**Assessment:** supported as self-report by [E001](../../scouting-runs/2026-10-24-personal-food-assistant.md#i001-e001). Frequency, elapsed time and cost are unmeasured. Friends' experiences remain secondhand. Public accounts add context, not representative prevalence. Frequent orderers may differ materially from someone ordering only when a cook is absent.

**Update:** [R001](results/R001-founder-assistant-experience.md) reports overly general assistant answers and no direct food link. The same-day clarification identifies ordinary Android ChatGPT/Claude use without food-specific setup; the event date remains unknown. This adds specificity without demonstrating failure of a connected food assistant or establishing prevalence.

**Next check:** the founder tries a food-connected assistant on Android, then assesses whether a friend comparison is warranted through [T001](tests/T001-existing-alternatives.md), including the steps from recommendation to the actual dish.

## C002

**Claim:** existing products cover much of conversational food search and remembered preferences.

**Assessment:** high confidence in documented overlap; low confidence in comparative experience. [E020–E025](#e020) cover the strongest alternatives. Claude plus Swiggy is the most relevant initial India benchmark. ChewIQ advertises learning from dining outcomes, further weakening a uniqueness claim for our feedback loop. Availability caveats do not make memory novel. [E032](#e032) gives a documented Android trial route; [E033](#e033) records a published ChatGPT option with account access unconfirmed. R001 has not tested either connected flow.

## C003

**Claim:** authorized integrations can support a commercially offered delivery assistant.

**Assessment:** conditional, not established for this founder. [E016](#e016) provides a Swiggy application route; [E017](#e017) constrains processing and retained data; [E019](#e019) rules out assuming Zomato third-party access. Published discovery tools support a shortlist, but permissions, tariffs, quotas and live reliability remain unresolved. Consumer use through Claude is distinct from permission for our own app.

## C004

**Claim:** our treatment of meal feedback improves decisions enough to beat existing alternatives.

**Assessment:** untested. Distinguishing a tolerated fallback from a favorite is a useful requirement, not evidence of advantage. An existing assistant with a good profile may achieve the same outcome. Test changing cravings, repeated good favorites, skipped feedback and users who enjoy browsing. [R001](results/R001-founder-assistant-experience.md) identifies generic answers and missing food links as a failure to reproduce. This supports testing actionable item recommendations, not claiming that a particular competitor lacks them. T001 must identify an actual failure in a fair baseline before a new product is warranted.

## C005

**Claim:** customers will pay and remain at sustainable delivery and acquisition costs.

**Assessment:** unknown. No accepted price, payment, acquisition cost or retained customer exists. [Economics](economics.md) shows sensitivity, not projected income. Adjacent paid offers [E024](#e024) and free supply [E025](#e025) make a low-price subscription possible to propose but hard to justify without distinct value. [T002](tests/T002-payment-and-repeat-use.md) separates purchase from use and renewal.

## C006

**Claim:** available dish information is sufficient for reliable recommendations within the promised scope.

**Assessment:** partially supported for discovery, unestablished for exact nutrition, ingredients and personal tolerance. [E018](#e018) finds no guaranteed structured nutrition/allergen/spice fields in checked schemas. [E027](#e027) illustrates distrust without proving mislabelling. A taste/convenience product may still work; an accurate medical or macro-prescription product is not established. R001 also makes usable food links a material delivery requirement: whether an authorized source exposes an exact item destination and whether it opens correctly remain unverified.

## C007

**Claim:** a solo founder can reach customers and operate the offer within current resources.

**Assessment:** unestablished. The [founder profile](../../FOUNDER-PROFILE.md) records ₹5,000/month and usually 10–19 hours/week, plus willingness to conduct conversations. [R001](results/R001-founder-assistant-experience.md) establishes self-reported ability to recruit friends for the first trial, limited to friends. Individual agreement and wider access remain unknown. Per-meal manual curation could consume that time quickly. Provider contracting, evaluation and support require capabilities beyond generating an app.

## E016

**Origin:** Swiggy [access/onboarding](https://mcp.swiggy.com/builders/docs/operate/access/), [developer page](https://mcp.swiggy.com/builders/developers/), and [rate policy](https://mcp.swiggy.com/builders/docs/operate/rate-limits/). First-party documentation, India; recheck of E007.

**Observed:** individuals can apply; onboarding calls for a working demonstration and review, with staging preceding production. The developer FAQ instead describes direct production development without a sandbox. This inconsistency persists. Exact rate caps are unpublished. No commercial tariff or guaranteed approval time for this founder was established.

**Implication:** C003/C007 remain conditional. Confirm the applicable route, permitted offer, charges and limits before committing production work. No application or API call was made; local free prototyping is not a free production contract.

## E017

**Origin:** Swiggy [data/compliance policy](https://mcp.swiggy.com/builders/docs/operate/data-and-compliance/), first-party guidance, India; continuation of E007.

**Observed:** platform-derived data is scoped to the immediate task; retained personal data and secondary uses have additional conditions. Processing responses outside India requires a signed agreement under the published policy. Consent, deletion and limited logging requirements affect implementation.

**Implication:** C003/C004. Separate user-entered preferences from provider-derived history and confirm the intended feedback store and model provider/region. This is a reading of vendor requirements, not a legal determination. Customer consent alone is not a blanket platform licence.

## E018

**Origin:** Swiggy [search_menu](https://mcp.swiggy.com/builders/docs/reference/food/search_menu/) and [get_restaurant_menu](https://mcp.swiggy.com/builders/docs/reference/food/get_restaurant_menu/), first-party schemas, India.

**Observed:** location-based discovery includes identifiers, prices, availability and customizations. Menu browsing is paginated and descriptions can be truncated. Neither checked output schema guarantees structured calories, protein, allergens or spice intensity. Item prices can differ from final cart totals. Guest coordinate-based search is documented; it was not called or commercially approved here.

**Implication:** C003/C006. Inspect real returned data before promising nutritional filtering. Missing schema fields do not prove every description lacks nutrition, but dietary-planning marketing does not establish reliable access. Total-price claims need current totals or clearly marked uncertainty.

## E019

**Origin:** [Zomato official MCP repository](https://github.com/Zomato/mcp-server-manifest), first-party policy, India; recheck of E008.

**Observed:** discovery, menus, carts and ordering for permitted use; developer requests are personal-use only and third-party apps currently disallowed. Integration discussions are invited.

**Implication:** C003. Do not base a commercial cross-platform promise on this connector. User-provided menu material can test preferences but does not reproduce delegated search or settle data rights.

## E020

**Origin:** [Swiggy integration announcement](https://www.swiggy.com/corporate/press-release/swiggy-now-lets-you-order-food-dineout-and-shop-on-instamart-directly-inside-chatgpt-and-claude/) (2026-01-27); Anthropic [memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) and [connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) documentation. Recheck of E011.

**Observed:** Swiggy documents conversational discovery and transactions. Anthropic currently documents memory on Free/Pro/Max and web connectors for all users; sensitive topics such as health have separate memory controls. An expensive assistant subscription is not established as universally necessary. Account access and usage limits were not tested.

**Inference:** these components address the core requirements when configured, but reliable food memory and recommendation quality were not demonstrated here. Benchmark setup, cross-chat recall and correction of a disliked fallback. General memory does not establish automatic satisfaction learning.

## E021

**Origin:** Amazon [food-delivery announcement](https://www.aboutamazon.com/news/devices/alexa-plus-grubhub-uber-eats-food-delivery) (2026-03-31 per indexed publication); [India announcement](https://www.aboutamazon.in/news/devices-and-alexa/alexa-plus-launch-india) (exact publication date unresolved). Recheck of E012.

**Observed:** Grubhub/Uber Eats conversation and linked past orders are documented with a supported Echo Show rollout. India material advertises preference memory but describes Swiggy delivery as forthcoming.

**Implication:** strong global competing capability; this source does not establish a live Indian delivery flow. Rollout and device constraints belong in the comparison. No account/device tested.

## E022

**Origin:** [ChewIQ](https://chewiq.io/) and its [UK App Store listing](https://apps.apple.com/gb/app/chewiq-ai-calorie-tracker/id6747684600), first-party descriptions; recheck of E013.

**Observed:** website advertises restaurant conversation and learning what the user enjoyed, including free personalized recommendations. Its iPhone listing emphasizes cooking and nutrition without corroborating restaurant discovery. It advertises Pro at $6.99/month or $39.99/year; currency code/local India price unverified. UK listing lacks enough ratings for an overview.

**Implication:** direct advertised overlap, including outcome memory. Installed capability, coverage and sustained use remain unconfirmed. Browser access failed before the public demo could be operated. Marketing allergy assurances are not adopted as factual safety claims.

## E023

**Origin:** [Choozin](https://choozin.app/), first-party offer; recheck of E005/E014.

**Observed:** conversation, menu reading and stored preferences advertised. Website still says coming soon on iOS; the previously found [India listing](https://apps.apple.com/in/app/choozin/id6785554872) again failed to open. Site prices: $1.99/50 credits, $4.99/150, $14.99/500; menu reading uses two credits, a message one. Dollar currency code and local checkout unverified.

**Implication:** close proposed alternative; availability unresolved. Usage pricing is a comparator for occasional users, not accepted-price evidence. Vendor-selected testimonials are not counted as independent customers.

## E024

**Origin:** [Healthify+ store](https://store.healthifyme.com/products/healthify-plan-your-24-7-ai-health-coach), India INR offer; recheck of E003.

**Observed:** Ria coaching, tracking, recipes and reports; promotional ₹399 for one month or ₹1,499 for twelve months. Annual allocation is ₹124.92/month, not monthly billing at that amount. Local delivery search was not established.

**Implication:** adjacent competition for spending and attention, not willingness to pay us ₹149. Tax/renewal checkout terms uninspected. Vendor health-outcome claims were not used.

## E025

**Origin:** [MyOrderGuide](https://www.myorderguide.app/), first-party website; recheck of E004.

**Observed:** free no-signup dish shortlists based on location/preferences; featured US cities. Full conversation, outcome memory and India coverage not established.

**Implication:** pressure on charging for a single recommendation. Partial substitute, not a confirmed full match. Categorical allergy assurances are unverified.

## E026

**Origin:** [Arjun Biju Kumar's original LinkedIn account](https://www.linkedin.com/posts/arjun-biju-kumar_i-just-ordered-my-favourite-snack-through-activity-7459968197568536578-XYJS), public individual report, India service. Event/publication date unknown: rendered relative dates conflict.

**Reported:** successful snack ordering through Claude/Swiggy, motivated by curiosity rather than demonstrated convenience. A subsequent WhatsApp/API experiment failed to place an order. Visible replies expressed interest; no resolution visible.

**Implication:** a reported successful consumer flow, not daily usefulness. Identity, delivery and video outcome were not independently verified. The author's architectural explanation is not technical documentation; current official sources describe a separate developer route. One author/event is not several independent observations.

## E027

**Origin:** [Swiggy high-protein review and replies](https://www.reddit.com/r/swiggy/comments/1wfm6sp/swiggy_high_protein_food_review/), anonymous General__X, India platform. Indexed dates 2026-09-13 onward; relative dates conflict, so exact event date unresolved.

**Reported:** dissatisfaction with a high-protein-labelled meal and refund dispute; replies complain about portions/descriptions. No resolution visible.

**Implication:** a trust/expectation concern under C006. Composition and the poster's protein estimate were not measured. Does not establish nutrient fraud, prevalence or demand for an assistant; restaurant quality may be the underlying problem.

## E028

**Origin/limited access:** [Bangalore favorites](https://www.reddit.com/r/bangalore/comments/1fdgfor) and [household cook discussion](https://www.reddit.com/r/AskIndia/comments/1c7a71w). Indexed dates 2024-09-10 and 2024-04-18; original-page opens failed with cache misses.

**Search extraction only:** favorites and a reply reporting an enjoyable recommended dish; household repetition complaints and simple fallback meals. Leads for satisfied alternatives and problems, not fully verified observations. No prevalence/count derived. Older posts do not establish present menus/prices.

## E029

**Origin:** [Google Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing), current primary supplier page, USD per million tokens.

**Observed:** Gemini 3.1 Flash-Lite standard text input $0.25, output $1.50, including thinking tokens. Search grounding lists 5,000 free requests/month shared across Gemini 3+ models, then $14/1,000, billed per executed query. Free-tier content may improve products; standard paid tier says it does not.

**Implication:** cost inputs only. No model selected or quality tested. Cheap tokens establish neither acceptable ranking nor permitted data processing nor live menus. Do not assume free-tier processing satisfies platform terms.

## E030

**Origin:** [Razorpay fee explanation](https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained), first-party India supplier. Labelled publication 2026-02-13 but includes a later promotion; update date unspecified. Main pricing page extraction was empty; article used instead.

**Observed:** standard gateway 2% plus 18% GST on fee; subscriptions add 0.99% plus applicable GST. Domestic settlement typically T+2 business days. Method/account terms differ.

**Implication:** illustrative recurring card-like fee 3.5282%, excluding introductory promotions. Manual monthly payments differ. Founder eligibility, refunds, sales taxes and native app-store billing remain unassessed; no account opened.

## E031

**Origin:** [Cloudflare Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/), USD supplier; recheck of E010.

**Observed:** paid Workers starts at $5/month, with limits and additional usage charges.

**Implication:** one hosting component, not the whole product budget. Storage, compliant placement, models, monitoring and support are additional concerns. No purchase/selection occurred.

## E032

**Origin:** [Claude connector documentation](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) and [official Swiggy repository](https://github.com/Swiggy/swiggy-mcp-server-manifest), retrieved 2026-10-27. Follow-up to E020; same vendors, not independent corroboration.

**Observed:** Claude documents custom web connectors on all plans, one on Free, and use on Android after connecting on web/desktop. Swiggy publishes `https://mcp.swiggy.com/food`. Its older setup heading specifies Pro Desktop; current Claude plan documentation is broader. Try the free route first, subject to actual account access and usage limits.

**Implication:** strongest documented baseline for this Android user; connection, links, recall and useful choices remain untested. This consumer route does not grant commercial access for a new app.

## E033

**Origin:** [official Swiggy repository](https://github.com/Swiggy/swiggy-mcp-server-manifest), its [ChatGPT Swiggy Food link](https://chatgpt.com/plugins/plugin_asdk_app_6a3de8146ae4819186b6799a5d907074), and [OpenAI mobile plugin documentation](https://learn.chatgpt.com/docs/plugins), retrieved 2026-10-27. Also a read-only plugin-directory tool search for “Swiggy” in this session.

**Observed:** Swiggy links a Food plugin for restaurant/menu discovery, carts and orders. OpenAI documents mobile use of account-available plugins. The linked page yielded no usable product details; the tool directory returned an empty plugin list. No installation or account connection occurred.

**Implication:** a relevant optional route, with this user's availability unconfirmed. Empty search results do not prove global absence. No verified exact-dish links or recommendation quality.

## E034

**Origin:** [Choozin](https://choozin.app/) and [ChewIQ](https://chewiq.io/), Android availability follow-up to E022/E023, retrieved 2026-10-27.

**Observed:** Choozin says iOS is coming soon and Android is on the way. ChewIQ links an iOS download. Targeted Google Play searches did not establish a relevant Android release for either.

**Implication:** neither is a confirmed Android recommendation for this trial. This is a bounded availability check, not proof that no Android food assistant exists. MyOrderGuide remains a partial browser comparator with India coverage unverified (E025).

## Remaining work

The [dated round](rounds/2026-10-27-business-investigation.md#research-coverage-and-access) records searches, omissions and failures. Public evidence gives a usable business view. Decisive work remains: actual T001 comparison, provider confirmation for the chosen design, and conditional T002 payment/return behavior. Demand, comparative quality, production access and profitability remain unvalidated. The [initial follow-up](rounds/2026-10-27-actionable-food-links.md) sharpened the food-link requirement; the [Android follow-up](rounds/2026-10-27-android-product-trial.md) incorporates R001’s setup clarification and makes a personal connected-assistant trial the next step.
