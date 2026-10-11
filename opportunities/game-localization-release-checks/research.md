# Game localization release checks — research

Current claim assessment: 2026-10-11  
Scope: Small game teams checking localized interfaces across builds. iOS developer and Steam studio evidence; country and initial supported engine open.

## C001

**Claim:** Game translation can leave context, font, layout and integration defects that string-only review misses.

**Assessment and confidence:** Concrete self-reported experiences in two projects support this task ([E001](#e001), [E002](#e002)); they do not establish prevalence, recurring spend or new-tool economics. The studio's budget constraints are a contrary signal.

**Next useful check:** Inspect a recent build, defect discovery and actual consequences. Separate translation quality from configuration/coordination issues and defects cheaply caught already.

## C002

**Claim:** A new tool could improve repeated checks enough to be purchased.

**Assessment and confidence:** Strongly challenged for generic screenshot/overflow checks. Final targeted searches found LocaDiff, an Unreal screenshot-matrix plugin, Unity hooks, Gridly and hourly native testing ([E003](#e003)–[E007](#e007)). Screenshots/delta checks are not established unique features.

**Proposed variation, unverified:** One engine/platform with approved screens, reproducible captures and reports that fit a small team's actual release process. Choosing Unity/mobile rather than Unreal/Win64 narrows development, without proving a gap. Automation requires scene access/configuration and human contextual review.

**Next useful check:** Compare accessible tools and manual checks on an actual release. Proceed only if a material failure remains they cannot address satisfactorily.

## C003

**Claim:** Tooling/setup or a scoped audit are possible revenue models, without demonstrated advantage or economics.

**Assessment and confidence:** Unresolved. A studio owner/producer is a possible payer, with authority unverified. License/setup/support and release-audit fees are proposals; no accepted price. Published tools/tester rates are alternatives, not prices customers accept for our offer ([E004](#e004), [E005](#e005)).

**Initial work:** One-engine capture runner, scene/state configuration, locale/resolution switching, source references, baseline approval, comparisons and export. Dynamic scenes and font changes create false differences; coverage and engine maintenance require testing. Linguistic judgment requires native reviewers.

**Unpriced requirements:** Development, devices/build agents, private build access, hosted storage/compute if used, release support and native reviewers. Supplier availability, terms and quotes unknown. Advertised hourly rates are benchmarks, not subcontracting permission or full project costs. No benchmark, complete estimate or paying studio established.

**Next useful check:** Obtain appropriate build access and an unsolved task before choosing architecture or buying testing capacity.

## C004

**Claim:** Public game communities and creator pages offer relevant discovery routes.

**Assessment and confidence:** Discussions/listings accessible ([E001](#e001), [E002](#e002), [E008](#e008)); recruitment, budget and recurring localization activity unknown. Hobby/jam developers are not automatically paying studio customers.

**Next useful check:** Identify a team with a forthcoming multilingual update and publishing authority; clarify why it would evaluate another supplier. No contact made.

## E001

**Origin:** [Localized my game into four languages solo](https://www.reddit.com/r/gamedev/comments/1s2cyej/localized_my_game_into_4_languages_solo_and/), r/gamedev; JBitPro. Original/relevant replies read.

**What it reports:** iOS developer describes overflow/clipping, confusing abbreviations and defects found while playing rather than reading strings. Replies discuss longer-label design, fonts and prioritizing English audiences. A false claim that Thai is right-to-left is corrected in a reply and is not used here.

**Context:** One small mobile project; identity/outcomes/store interpretations unverified.

**Dates:** Event/exact publication unknown (search roughly spring 2026); retrieved 2026-10-11.

**Claims and limits:** C001–C004. Experienced task, without quantified losses or automation purchase.

## E002

**Origin:** [Finished localization of 15 languages](https://www.reddit.com/r/gamedev/comments/1hya58a/just_finished_localization_of_15_languages_and/), r/gamedev; OpinionateThis reporting Rocket Adrift/Psychroma. Original/relevant replies read.

**What it reports:** Three-person studio describes months of volunteer localization, hard-coded UI/custom integration, font issues and coordination/version confusion. Reports limited remaining budget and disappointing non-English audience results. Replies propose earlier localization structure and existing workflows.

**Context:** Steam PC/Linux volunteer project; outcomes not verified financially. Organizational issues cannot all be fixed by screen checks.

**Dates:** Search indexed January 2025; exact day unknown; project occurred before posting; retrieved 2026-10-11.

**Claims and limits:** C001–C004. Different project, weak ability-to-pay signal. No general claim that localization is unprofitable.

## E003

**Origin:** [Unity locales](https://docs.unity.com/en-us/engine/6000.7/manual/localization/locales), first-party Unity 6.7 beta docs.

**What it documents:** Locale selection/fallbacks and a post-processing interface for pseudo-localization, including stretching text/swapping characters to test layout.

**Context:** Versioned beta docs; no engine version selected/tested.

**Dates:** Publication unknown; retrieved 2026-10-11.

**Claims and limits:** C002–C003. Existing engine testing support; not proof of turnkey coverage or stable-version compatibility for a customer.

## E004

**Origin:** [Patchworld](https://patchworld.win/), vendor-owned offer.

**What it documents:** Native build testing, screenshot/reproduction reports and retesting. Standard $38/hour; Lead $45/hour; one-hour minimum; listed scarce languages add $10/hour. Delta/patch checking advertised.

**Context:** “$” displayed; currency code/geographic billing and tax unspecified in extraction. TestFlight/Steam and other build routes. Performance and cultural/regulatory marketing claims were not verified/adopted.

**Dates:** Publication unknown; offer retrieved 2026-10-11.

**Claims and limits:** C002–C003. Human-service substitute; capacity, quality, total hours and subcontracting terms unknown.

## E005

**Origin:** [LocaDiff demo](https://theluckyduck666.itch.io/locadiff) and [Pro](https://theluckyduck666.itch.io/locadiff-pro), creator listings by TheLuckyDuck666.

**What it documents:** Local/browser screenshot comparisons, overflow/clipping, expansion analysis, placeholders and exports. Demo: 100 strings and a language pair, exports locked. Pro: unlimited strings/languages, exports, no subscription/seat limit, minimum one-time $9.99 USD purchase.

**Context:** Advertised tool; no execution/purchase. Tax unspecified. Two pages represent one product family.

**Dates:** Search/listing material indicates October 2026 release; exact date not retained from the opened page; retrieved 2026-10-11.

**Claims and limits:** C002–C003. Direct inexpensive feature overlap; sales, quality and satisfaction unestablished.

## E006

**Origin:** [L10N Visual QA — Localization Screenshot Matrix](https://www.fab.com/listings/770fac6e-d828-41a5-aaf5-983e02eb74e4), creator metyatech's Fab listing.

**What it documents:** Unreal targets across cultures/resolutions, editor/runtime captures, baseline comparison, CI commandlet and reports. Version 0.1.0 supports Win64; automatic target discovery and packaged-build testing explicitly excluded.

**Context:** Unreal, rather than chosen Unity/mobile scope; price not rendered; no runtime test.

**Dates:** Publication/update dates unknown; retrieved 2026-10-11.

**Claims and limits:** C002–C003. Repeatable capture competitor. Scope boundaries raise questions without proving valuable unmet demand.

## E007

**Origin:** [Gridly localization QA](https://www.gridly.com/localization-qa/), first-party page.

**What it documents:** Screenshots/localization data, automated string checks, issue workflow and continuous checks on changed content. Vendor-hosted customers describe successful use; selected marketing accounts, not independently verified performance.

**Context:** Team platform; pricing/small-studio offer not examined.

**Dates:** Publication unknown; retrieved 2026-10-11.

**Claims and limits:** C002–C003. Workflow alternative; neither affordability nor unsuitable small-team fit established.

## E008

**Origin:** [itch.io developer page](https://itch.io/developers), platform's public site.

**What was observed:** Creator/game browsing, developer logs and community routes available; no list of actual multilingual studio buyers produced.

**Context:** Independent creators/tools/hobby projects; purchasing ability varies.

**Dates:** Interface retrieved 2026-10-11; individual creator dates unknown.

**Claims and limits:** C004. Discovery route, without verified access or interest.

## Research still needed

No studio conversation, private build, competitor execution, benchmark, accepted price or repeat use. A specific payer and residual gap require customer evidence. Final searches weakened the generic proposition; retain this finding.

[Search/access history](../../scouting-runs/2026-10-11-creative-consumer-discovery.md#search-trail-and-coverage).

