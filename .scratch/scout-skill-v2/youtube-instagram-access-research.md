# YouTube and Instagram: discovery, inspection and usable access

Checked **2026-10-30** for [Research usable YouTube and Instagram access for scouting](issues/14-research-youtube-instagram-access.md). This is primary-documentation research, not a successful integration test. No accounts, subscriptions, installations, credentials, browser cookies or paid calls were used. The coordinator records this environment's connector/browser tests separately. The [earlier API inventory](api-access-research.md) and [source audit](selected-source-access-audit.md) remain history; this note adds specific retrieval candidates and their limitations.

## Recommendation

Use **YouTube's official API for discovery and metadata, native transcripts for speech, and actual frames for visual claims**. For Instagram, pilot **Apify's maintained Instagram Scraper for discovery/carousel retrieval** and **Supadata for supplied video transcripts**, using included free allowances only after the connection is available. Both publish hosted MCP routes; neither is connected or proven reliable here. Prefer one bounded sample of the user's actual links over a new broad research run.

Reliability must mean successful retrieval of the required material, correct attribution and visible failure handling. A connector listing, transcript, thumbnail or creator interview does not establish that a carousel was read, a reel was watched, or a topic is currently spreading. If a supplied reference defines the category or intended idea and cannot be inspected, report the exact gap and request the missing screenshots/transcript/video before starting dependent discovery.

## Official platform routes

| Route | What the documentation supports | What it does not establish |
| --- | --- | --- |
| YouTube Data API | Search videos/channels with query, date, ordering and region filters; retrieve video metadata/statistics and region/category `mostPopular` results. [Search reference](https://developers.google.com/youtube/data/reference/rest/v3/search/list), [video reference](https://developers.google.com/youtube/data/reference/rest/v3/videos/list). Published comments can be paginated separately. [Comment threads](https://developers.google.com/youtube/data/reference/rest/v3/commentThreads/list) | Metadata and comments are separate from speech and visual/audio inspection. A current popular chart or high lifetime view count alone does not establish category growth. |
| YouTube native transcript | The user-facing **Show transcript** control exposes text for captioned videos and supports jumping to caption timestamps. [YouTube Help](https://support.google.com/youtube/answer/15930243) | Availability for a particular video still needs testing. Reading a transcript is speech/text inspection; it is not visual inspection or listening to the audio. |
| YouTube captions API | Caption download requires OAuth and permission to **edit the video**. [Download reference](https://developers.google.com/youtube/data/reference/rest/v3/captions/download) | A general public-data API key cannot download arbitrary creators' transcripts through this endpoint. More quota does not change ownership permissions. |
| Instagram API with Facebook Login | Professional account plus linked Facebook Page; own media/comments, hashtagged media, and basic metadata/metrics about other businesses/creators. Consumer/personal accounts are excluded. [Meta-owned collection, indexed documentation](https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api?entity=request-23987686-b217bc6c-d9fb-4d65-bf5e-fcadf650ad5c) | This is not a general arbitrary-personal-account reader. It does not establish access to every public reel, all other accounts' comment text, arbitrary keyword search or spoken transcripts. Business Discovery/hashtag field, permission, review and quota details need scoped confirmation before implementation. |
| Instagram API with Instagram Login | Meta separately documents management of professional accounts, with its own permission names and limitations. [Meta-owned collection](https://www.postman.com/meta/instagram/folder/1z5vxzu/instagram-api-with-instagram-login) | Do not assume Facebook Login's discovery capabilities transfer to this setup. No arbitrary-public-content access was established here. |
| Meta Content Library | Public Facebook/Instagram research data through UI/API; API access runs inside SOMAR's Virtual Data Enclave or Meta's Secure Research Environment. [Current ICPSR overview](https://www.icpsr.umich.edu/sites/somar/meta-content-library). Meta describes eligibility for qualified academic/nonprofit researchers doing scientific/public-interest work. [Meta announcement](https://about.fb.com/news/2023/11/new-tools-to-support-independent-research/) | No eligibility for this commercial startup-scout use case has been established. This is an application-based research program, not an available generic connector. The current eligibility page could not be fetched; do not treat historical criteria as a fresh approval decision. |

**Current YouTube quota correction:** Google's quota page, updated 2026-10-15, specifies **100 `search.list` calls/day in a separate bucket**, plus **10,000 daily units for other endpoints**; ordinary video/channel/playlist/comment list calls cost one unit. Search pagination consumes additional search calls. Confirm the actual project's quota; older vendor articles describing 100 shared units per search are stale. [Official quota table](https://developers.google.com/youtube/data/determine_quota_cost)

**Documentation access limitation:** Direct Meta Business Discovery, hashtag, Instagram Login and Content Library eligibility pages returned HTTP 429 or failed retrieval here. Meta's own Postman collection was readable in search-indexed text; some direct documentation opens returned only a shell. Therefore this note deliberately does **not** assert a freshly verified numeric hashtag limit, minimal approval scope or exact Business Discovery field set. That gap does not prevent choosing a small third-party/browser pilot.

## Two concrete connector candidates

### Apify: discovery, carousel children and media retrieval

Apify's own maintained `apify/instagram-scraper` documents public profile/post/reel/hashtag/place retrieval, profile/hashtag/place search, captions, timestamps, metrics, comments, image/video URLs and carousel children. Retrieving those URLs is only the first step: inspect each relevant carousel child and record which slides were actually seen. [Actor documentation](https://apify.com/apify/instagram-scraper)

The maintained `apify/instagram-reel-scraper` adds optional transcripts/downloads; its ordinary output includes recent comments rather than an automatic complete comment corpus. [Reel actor](https://apify.com/apify/instagram-reel-scraper). These are **Apify-maintained third-party scrapers**, not Meta-approved APIs or a promise of universal access.

The hosted endpoint is `https://mcp.apify.com`, with OAuth or bearer-token authentication. It can discover/run actors and read results. Anonymous tools cover actor discovery/docs, not free authenticated scraping. Pin the small actor set needed for this task. [Apify MCP documentation](https://docs.apify.com/mcp)

| Current published price | Implication for a pilot |
| --- | --- |
| Free plan: **$5/month** included, no card required; access stops after the allowance. Starter: **$19/month plus usage**. [Plan pricing](https://apify.com/pricing) | Use Free initially; do not enable an upgrade or payment mechanism. This is one shared allowance across actors. |
| Instagram Scraper Free tier: **$2.70/1,000 results**, platform costs included. [Actor pricing](https://apify.com/apify/instagram-scraper/pricing) | 100 returned items model as $0.27 of included credit. The headline $1.50 rate is a higher plan's discount. |
| Reel Scraper Free tier: **$2.60/1,000 reels**, $0.001 start event. Add-on table lists transcript **$48/1,000**, download **$20/1,000**, shares **$7/1,000**. [Reel pricing](https://apify.com/apify/instagram-reel-scraper/pricing) | The input reference says transcript billing is per audio minute and download billing per MB. Combining those pages implies $0.048/minute and $0.020/MB, but **confirm event units in Console before running**. Shares are described as paid-users-only despite a Free-column price. [Input reference](https://apify.com/apify/instagram-reel-scraper/input-schema) |

Do not estimate thousands of fully inspected reels from the base-rate marketing allowance: transcript and media add-ons materially change it. The first test should retrieve one supplied carousel and one supplied reel with explicit result/cost caps, recording actual event units and charges.

### Supadata: a bounded video transcript test

Supadata documents a hosted OAuth MCP at `https://api.supadata.ai/mcp`, exposing transcript, metadata and video-analysis tools. It is a vendor integration, not a YouTube/Meta API. No local client compatibility or successful connection is claimed here. [MCP documentation](https://docs.supadata.ai/integrations/mcp)

Its transcript endpoint accepts YouTube and Instagram video URLs, returns timestamped segments, and supports `native`, `auto` and `generate`. Default `auto` may generate speech recognition when captions are absent; `native` avoids that fallback. Restricted/login-required videos are not supported. Empty generated output can mean no speech, and may still be charged. Transcript-unavailable status 206 costs one credit. [Transcript documentation](https://docs.supadata.ai/get-transcript)

The separate extraction endpoint analyzes what is seen/heard and returns AI-generated structured observations. It is not a raw frame archive or a guarantee of accurate visual coverage; preserve provenance and verify decisive visual details. It costs **5 credits per started minute**, minimum five per call. [Extraction documentation](https://docs.supadata.ai/get-extract)

Current plan: **100 free credits/month**, no card required; native transcript **1 credit**, generated transcript **2 credits/minute**. Basic's advertised **$5/month is annual-only: $60 upfront**, 300 credits/month, with optional recharge priced separately. Pro is $17/month. Do not activate recharge. [Pricing](https://supadata.ai/pricing)

Example pilot: five native YouTube transcript requests plus five one-minute generated reel transcripts use approximately 15 credits; five one-minute visual-extraction calls add 25. This is a planning estimate, not a success claim; check actual video lengths, request status and the account's remaining credits. For long videos, explicitly choose native mode first so a missing transcript cannot silently consume the entire monthly allowance.

**Open-source alternative:** `youtube-transcript-api` retrieves captions without an API key, but its own README documents IP blocks, currently broken cookie authentication and reliance on an undocumented endpoint. It is a useful optional fallback, not the dependable foundation promised to the user. No installation or test was performed. [Maintainer README](https://github.com/jdepoix/youtube-transcript-api)

## Budget and acceptance

Start with public/included routes: **₹0 new subscription spend**. The prior ₹1,000/month cap is combined planning context, not permission to purchase. Using the previous report's illustrative ₹90/$ plus 20% fee/tax buffer, Apify Starter models as ₹2,052/month, and Supadata Basic as ₹540/month equivalent but **₹6,480 annual upfront**. These are assumptions, not current exchange-rate quotes or checkout totals; neither paid plan is needed for the first samples.

Before marking either platform usable for a chosen category:

1. **Resolve the supplied reference first.** Test the exact original URL; for a carousel include the requested slide index and surrounding context. Capture the actual access error. If still unreadable, ask for the relevant slides, caption, transcript or video, with the original URL/date. Earlier notes remain earlier notes.
2. **Prove the required modalities.** Record original URL, creator, publication date, retrieval time, method, text/transcript provenance, slide/frame/timestamp coverage, metric observation time and comment sample. A media URL alone is not inspection; a transcript alone cannot support claims about layouts, demonstrations or on-screen text.
3. **Prove discovery separately.** Use a defined recent date window, category-specific queries/hashtags and multiple independent creators. Keep query/filter/results evidence, including counterexamples. A successful supplied-link transcript does not prove platform discovery works.
4. **State the strength of spread evidence.** Multiple recent independent examples support a current pattern. A stronger claim about growth needs dated comparable observations or a clearly described baseline. One lifetime view count, an old interview or a personalized feed cannot establish platform-wide momentum. This is the research method recommended here, not a platform guarantee.
5. **Fail visibly.** If the required platform or modality remains inaccessible, mark the category/run incomplete and put that limitation in the user-facing result. Do not substitute accessible Reddit/product pages and label the required creator-platform research complete.

**Next owner:** the coordinator can incorporate these requirements into scout instructions and the canonical source catalog now. A subsequent connection task should use the smallest free pilot above, plus the user's exact carousel/reel, before any fresh category discovery. Still undecided: available account connection, runtime success, complete media coverage, actual per-event usage and any later paid plan. No new broad scouting run is needed to resolve these access questions.
