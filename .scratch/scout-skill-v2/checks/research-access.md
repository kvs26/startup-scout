# Verified research access for scout version 2

Checked **2026-10-29**, using the user's Asia/Kolkata session date. Supports [Connect and verify the agreed research access routes](../issues/09-connect-research-access.md). This is a dated test record, not another maintained source catalog. The [selected-source audit](../selected-source-access-audit.md) supplies the full documented inventory and historical prices; [source catalog](../../../docs/startup-skills/source-catalog.md) remains the runtime resource list, to be consolidated during the skill update.

## Outcome

Public reading plus HN, GitHub, Stack Exchange and the existing Tavily account provide usable starting routes. No new source subscription is required by these checks. YouTube Data API and SaaSHub API remain unconfigured in the checked project credential locations; their fallback routes and remaining limitations are explicit below. No account was created, credential changed, paid service activated, or message sent.

These are bounded access samples, not a scouting campaign, exhaustive source coverage, or verification of business claims. A page may be accessible through the web reader's index/cache without a fresh origin fetch: several results reported older crawl dates. Recheck the source and publication date before making time-sensitive claims. A title, menu or synopsis does not count as the original article, episode or transcript.

The user's [source-selection answer](../issues/04-select-source-portfolio.md#answer) already accepts continuing with missing-source limitations and precise requests for useful missing material. The deferrals below apply that decision; they do not assert that optional APIs were connected. No mandatory named-source coverage remains unresolved for this setup task. Essential evidence for a future candidate must still be obtained or that candidate kept provisional.

## Structured routes actually tested

The [sanitized results](api-results.json) record payload fields, sample URLs, counts and returned quota. The [bounded check script](verify-access.py) uses standard-library HTTP and reads only the existing Tavily entry in root `.env`; it does not source the file as shell code. The shell sandbox initially failed DNS resolution; the authorized network-enabled execution succeeded. These routes require network-capable execution, not a newly installed client or package.

| Route and configuration | Actual retrieval | Limits and current cost state |
| --- | --- | --- |
| [HN official Firebase API](https://github.com/HackerNews/API); no key required | `showstories.json`: 139 IDs; `askstories.json`: 19 IDs. Fetched [story 30186545](https://news.ycombinator.com/item?id=30186545) with title, author, text, time, score and child IDs, then one direct comment with 2,177 text characters and its child IDs. | One story/comment sample, not a complete tree or historical search. No paid activation. Follow children selectively and preserve parent context/deleted-item states. |
| [GitHub REST](https://docs.github.com/en/rest/issues/issues#get-an-issue); no token used | [ERPNext issue 59726](https://github.com/frappe/erpnext/issues/59726): open state, 2,210 body characters; first comment: 930 characters. | First response reported limit 60/hour/IP and 59 remaining. One comment only; no complete history/release verification. Read actual response limits on each run. |
| [Stack Exchange v2.3](https://api.stackexchange.com/docs); no key used | [Workplace question 203604](https://workplace.stackexchange.com/questions/203604/making-knowledge-transfer-without-giving-your-personal-notes) with `filter=withbody`: 2,536 body characters; one answer: 524 characters. | Returned `quota_max=300`, remaining 298 after two calls, no backoff. Use this observed anonymous quota, not a generic 10,000 assumption. Preserve author/link attribution and returned CC BY-SA 4.0 licensing when reusing content. |
| Tavily REST; existing `TAVILY_API_KEY` in ignored root `.env` | Authenticated usage, one basic search and one basic extraction passed. Search returned YC RFS with 1,331 content characters; extraction returned 23,486 characters, no failed URL. | Account reported Researcher, 108/1,000 included credits used, PAYG usage 0, PAYG limit null. Immediate before/after counters were unchanged: reporting may lag, so this does **not** establish zero credit consumption. Two-credit maximum for the bounded requests, after verifying a ten-credit buffer. No billing changes. |

Tavily's [usage endpoint](https://docs.tavily.com/documentation/api-reference/endpoint/usage) and [credit rules](https://docs.tavily.com/documentation/api-credits) support this preflight. Null `paygo_limit` does not establish that PAYG is disabled or capped. Future agents must check allowance and stay within included credits; no paid overage is authorized. The aggregate ₹1,000/month figure is a planning cap, not an active subscription or spending approval.

Tavily remains configured for VS Code through `.vscode/mcp.json` and `.vscode/mcp/tavily.mjs`. This chat's discovered tool list exposes no Tavily tool. Today's checks used direct REST, not that MCP client. The configured MCP launch/search and map/crawl successes remain historical October 10 checks in [SETUP](../../../SETUP.md); map/crawl and UI startup were not retested here. Do not claim a new Codex connection or an MCP test from these REST results.

## Selected website portfolio

Every named selected website is accounted for here. Web-reading successes require no new account configuration; none proves API entitlement, complete pagination or bulk extraction rights.

| Selected source | Sample and observed result today | Ready route / remaining gap |
| --- | --- | --- |
| Razorpay Fix My Itch | [Problem bank](https://razorpay.com/m/fix-my-itch/) exposes individual problem prompts, including used-car information and renter property hazards. | Public reading works for a sample. Entire bank enumeration and underlying respondent records unverified; no discovery API established. |
| YC Directory | [Directory root](https://www.ycombinator.com/companies) returned no extracted lines. Search found [industry listings](https://www.ycombinator.com/companies/industry/finance-and-accounting); an [individual company](https://www.ycombinator.com/companies/last-accounting-company) opened and redirected to Bear. | Search-to-profile reading works. Interactive directory filters/bulk directory retrieval remain unverified. Preserve canonical redirected URLs. |
| BetaList | [Homepage](https://betalist.com/) exposes dated listings; [Ascend profile](https://betalist.com/startups/ascend) opened with product information. | Public listings/profiles usable. API approval, volume and price remain deferred; submission fees are unrelated. |
| Show HN / Ask HN | Both official JSON lists and a story/comment passed, above. | Public API and HTML routes; historical/full-tree coverage not established by list success. |
| Product Hunt | [Launch homepage](https://www.producthunt.com/) and [Dedica product page](https://www.producthunt.com/products/dedica) returned content. | Selective public reading works. Token/API business-use clearance remains deferred under the [documented restriction](https://www.producthunt.com/v2/docs). |
| Indie Hackers | [Stories index](https://www.indiehackers.com/stories) exposes filters/navigation, with no dollar-denominated cases in the extraction. Search returned original-post snippets but also a robots restriction for `/post`. | Discovery/index access is partial; no complete current case-study body verified here. Follow a readable original operator account or request the exact missing passage. Do not call snippets full stories. |
| Starter Story | [Pat episode page](https://www.starterstory.com/pat) exposes synopsis, tool links and free-signup promotion; no chapters/transcript for this sample. | Public episode companion material is usable as a synopsis only. Signup-delivered database fields, account/export rights remain untested and deferred; no email submitted. |
| Microns | [Public marketplace](https://www.microns.io/) exposes business types, descriptions, annual revenue and asking prices. | Public summaries usable as seller claims, not audited economics. Private details/account access deferred; no Premium required for tested page. |
| Failory | [Interview index](https://www.failory.com/interviews) and [WePlate founder interview](https://www.failory.com/interview/weplate) opened. | Public interviews usable. Founder statements remain attributed accounts; no API established. |
| YC RFS | [Editorial page](https://www.ycombinator.com/rfs) readable in web and Tavily extraction. | Ready for context/seeds; investor requests do not establish customer demand. |
| YourStory | [Homepage](https://yourstory.com/) and [sample article](https://yourstory.com/2026/10/info-edge-steady-business-growth-leadership-transition) opened. | Public indexed articles usable. Gated products and complete archives not tested. |
| AlternativeTo | [Zoho Books alternatives](https://alternativeto.net/software/zoho-books/) returned product descriptions and alternatives. | Ready as pointers; confirm features/prices on vendor originals. No current API established. |
| SaaSHub | [Zoho Books alternatives](https://www.saashub.com/zoho-books-alternatives) returned alternatives; result reported an older crawl. [API docs](https://www.saashub.com/site/api) describe account-key lookup/top-ten alternatives and disclosure. | Public reading usable. No SaaSHub key found in project `.env` or relevant current environment variable names; no account test. Numeric API allowance/price remains unknown. API deferred; public reading is sufficient for the present task. |

## Creator access and transcript fallback

No YouTube credential was found in project `.env` or relevant current environment variable names. This says nothing about credentials the user may hold elsewhere. YouTube Data API was **not** called or configured. Its [documented caption-download permission](https://developers.google.com/youtube/v3/docs/captions/download) requires edit access; adding a metadata key will not unlock arbitrary creator transcripts.

- [MicroConf video](https://www.youtube.com/watch?v=545U5KzTBVE): web retrieval failed. The [companion page](https://microconf.com/on-air-episodes/microconf-tactics-7-new-saas-ideas-you-can-steal) opened but supplies a short synopsis and media links, not the seven ideas' spoken content.
- Browser fallback was attempted through the installed browser skill. Bootstrap failed with `Importing module "node:process" is not allowed in node_repl`, before browser selection/navigation. No YouTube UI, sign-in state, captions or audiovisual content was inspected. This is a browser-tool failure, not a provider refusal or evidence that the video lacks captions.
- [Jay Clouse's publisher-hosted episode](https://creatorscience.com/podcast/bts-april-2025/) exposes timestamped transcript text, including the 2:10 passage about AI work. This verifies a usable **publisher transcript** route for this episode; it is not a YouTube captions success or a promise for all episodes.
- [Noah Kagan's article](https://noahkagan.com/validate-a-business-idea/) and [TK Kader's article](https://www.tkkader.com/go-to-market-strategy/) opened as substantive creator-written material. They are not transcripts of their linked videos.

The complete creator pool is retained from [initial creator checks](../creator-source-research.md) and [additional creator checks](../additional-creator-research.md). Apart from the samples above and Starter Story, those prior checks were not repeated:

| Pool | Disposition |
| --- | --- |
| MicroConf, Greg Isenberg, My First Million, UpFlip, Chris Koerner, Think School | Shared YouTube route remains unconfigured; use previously identified original companion material where readable, distinguishing article, synopsis and episode. Only MicroConf was freshly retested here. |
| Ishan Sharma, Raj Shamani, Codie Sanchez, Ayushman Pandita | Conditional/access-limited originals remain conditional. No new full episode or Instagram entitlement established. |
| Marc Lou, Nick Saraev, Jay Clouse, TK Kader, Noah Kagan, Nate Herk | Preserve original-text evidence and provenance caveats from the additional research; Jay/TK/Noah freshly sampled above. Nate's asset provenance is still provisional. |
| Nathan Barry, Liam Ottley, Simon Høiberg, Ansh Mehra, Pat Walls, Dan Martell | Preserve synopsis/title/announcement limits where applicable. Pat overlaps Starter Story and is not an independent evidence family. Other video/transcript checks not repeated. |

When a chosen idea needs inaccessible spoken detail, a concrete request is: open [Ansh Mehra's linked episode](https://www.youtube.com/watch?v=iBqw4wShxJY), use **Show transcript** if available, and provide the passages naming the buyer, offer, delivery work, costs and evidence behind each idea. Preserve the video URL and displayed timestamps; if a claim depends on a diagram, include that frame and its surrounding explanation. Timestamps are currently unknown. This is a queued fallback for a relevant future brief, not a required user action now. Store supplied excerpts with their provenance and omissions; never label them independently watched or fetched.

Instagram is supplementary under the existing decision and remains unconfigured/untested. Cross-posted videos are one observation. Paid transcript vendors, courses and creator communities remain unselected.

## Community, review and context coverage

| Source/group from the audit | Fresh test or explicit deferral |
| --- | --- |
| Reddit | [Sample small-business thread](https://www.reddit.com/r/smallbusiness/comments/1mecoxb/small_business_needs_inventoryinvoicing/) opened with post/replies through the web reader. API commercial entitlement not established; no anonymous JSON workaround used. |
| Frappe / Discourse | [Sample topic](https://discuss.frappe.io/t/input-service-distributor-anyone-implemented-working-on-it/161555) opened. JSON/RSS not retested; public topic reading is the verified route. |
| Stack Exchange; GitHub ERPNext | APIs passed above. The separate fayerman-source idea repository was not retested; follow its dated catalog entry and recheck if selected. |
| Trustpilot | [Zoho review page](https://www.trustpilot.com/review/www.zoho.com) exposes dated reviews. Brand-wide sample mixes products; no licensed API entitlement established. |
| Shopify App Store | [Judge.me reviews](https://apps.shopify.com/judgeme/reviews) exposes dated merchant reviews and replies/links. Full pagination and review API not tested. |
| G2 | [Zoho Books reviews](https://www.g2.com/products/zoho-books/reviews) timed out. Use another relevant review source or precise user-supplied passages. Licensed API/MCP access remains deferred. |
| Local businesses, associations, product forums, first-party pricing (including Zoho Books India and AWS Lambda) | Select and recheck per future brief. No new all-site access claim or pricing validation; prior catalog examples remain dated. |
| O*NET; MoSPI/PIB ASUSE; World Bank Enterprise Surveys; YC Startup School | Public-reading examples retained from the audit/catalog; not retested today. O*NET API registration and World Bank microdata entitlement remain deferred. Public reports are not microdata access. |
| TED procurement | [Search API documentation](https://docs.ted.europa.eu/api/latest/search.html) rechecked: anonymous published-notice search documented. Swagger UI returned no extracted lines. No endpoint request was made; integration deferred until a procurement brief needs it. |
| India eProcurement | Retained public-portal route; detailed search/attachments not retested. No API connection claimed. |

## Conditional sources reconciled

All remaining audit entries stay available as conditional leads, not mandatory connections. No new account entitlement or current pricing was established for this group. Their detailed cost evidence and checked dates remain in the [audit](../selected-source-access-audit.md#conditional-sources-retained-from-the-original-research).

| Sources | Disposition and useful fallback |
| --- | --- |
| Google Trends | UI/CSV route documented previously; API alpha enrollment and actual CSV export untested. Defer until a brief needs trend comparison. |
| Trend Hunter | Public articles/official RSS documented; live feed parsing deferred. |
| Trends.vc, Springwise, Exploding Topics | Read accessible public reports/articles if relevant. Premium/quote-based API routes unselected; historical prices are not a new purchase recommendation. |
| IdeaBrowser, Peerlist Launchpad | Prior blocked/empty extraction remains an access gap. Browser route could not be tested in this session; use precise user material when useful. |
| Startup India idea bank, BHASKAR, Wellfound | Public briefs/profiles where readable; accounts, exports and discovery APIs unverified. No connection claimed. |
| Acquire.com | Public editorial or permitted account material only; no extraction entitlement or API assumed. |
| Dealroom, Crunchbase, Tracxn, Inc42 Datalabs | Licensed/paid/export access deferred. No quote or subscription selected; public editorial/company pages can serve limited contextual roles. |

## Handoff

Next owner: [Update and verify the agreed scout version 2](../issues/07-update-verify-scout.md). Fold these states into the existing source catalog, preserving the distinction between documented, configured, successfully tested, partial and deferred. The browser failure and missing YouTube/SaaSHub credentials must remain visible; avoid promising automatic transcripts or universally readable sites. Preserve the free/public starting route and account-allowance checks.

Ready-to-use prompt: “Use wayfinder with `.scratch/scout-skill-v2/map.md` to work on **Update and verify the agreed scout version 2**. Use `checks/research-access.md` and `checks/api-results.json` for actual connection results, consolidate the existing source catalog, and implement/test the already resolved decisions. Preserve transcript and account deferrals; do not report them as configured.”
