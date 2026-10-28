# Websites for finding startup ideas, early companies and models to adapt for India

Checked: **2026-10-28**. Research for discussion; no sources or integrations have been adopted into the scout skill.

## Finding

The existing scout permits product-led discovery, but its [source catalog](../../docs/startup-skills/source-catalog.md) emphasizes customer discussions and review channels. It includes YC Requests for Startups and a source-linked idea repository, but lacks systematic coverage of launch directories, founder business stories, company databases and geographic adaptation. The useful improvement is to give those sources distinct discovery roles, then independently investigate the resulting leads.

This report assesses 28 source entries (YC Directory and YC RFS are separate; Startup India Idea Bank/challenges are grouped), not startup opportunities. It is not a fifty-idea scouting campaign. Website claims establish what a provider advertises; they do not verify the listed businesses' revenue or customer demand. Access checks used public search/page reading and official documentation, with a separate browser attempt for Razorpay. Documented APIs were not authenticated or integrated. “No documented API found” means none was established in this review, not that none can exist. Ordinary page extraction does not establish full database access or permission for bulk collection.

## Proposed starting selection

Use **Razorpay Fix My Itch** for India-specific problem prompts; **YC Directory, Product Hunt, BetaList and Show HN** for emerging products; **Indie Hackers and Starter Story** for business and distribution patterns; **YourStory/Inc42** for Indian equivalents; **SaaSHub/AlternativeTo** for competition; and **Failory** to challenge attractive success stories. Choose among these after discussion rather than requiring every source in every run.

For overseas-to-India discovery, pair a foreign company or case study with an Indian competitor check and evidence from the intended Indian customer. A product launched in the USA is not necessarily popular there, profitable, unavailable in India, or suitable for an Indian buyer. Headquarters and customer geography are different fields.

Paid databases can wait until a specific research question cannot be answered efficiently from public pages. An API is worthwhile when repeated retrieval saves enough effort; it is not necessary to start using a source.

## Business stories, trends and alternative products

### Starter Story — business models and reported economics

**Contains/use:** searchable business ideas and case studies, revenue/startup-cost filters, tools and growth channels. Useful for discovering small businesses with a clear offer and acquisition story. [Database](https://www.starterstory.com/data).

**Observed:** public database rows and a [Tintim profile](https://www.starterstory.com/businesses/tintim) were readable. Crucially, that profile labels itself AI-researched from public sources, rather than founder-written, and calls its revenue an estimate. The database card and detail page displayed different revenue figures. Preserve source dates and follow the underlying evidence; do not inherit its scores or label every entry a verified founder interview.

**Access:** ordinary web reading for visible rows/previews; the sampled profile asks for newsletter signup to unlock all data. The current homepage advertises free access, so a blanket “paid-only” description would be inaccurate. No supported public API/export was established. Interactive search or authenticated detail access would need browser testing; no account was created. **Proposed priority: high, with provenance checks.**

### Indie Hackers — founder experience, products and stories

**Contains/use:** founder discussions, product updates, story and idea databases. Useful for identifying narrow paid products, first-customer channels, failed launches and repeat operational problems. The [homepage](https://www.indiehackers.com/) and [stories database](https://www.indiehackers.com/stories) exposed substantive content through ordinary page reads.

**Limit:** founder revenue and growth claims need corroboration; promotional posts and repeated stories can distort the apparent frequency of an opportunity. A listed product may now differ from the historical story.

**Access:** public web reading worked; subscription navigation also exists, so full access is not assumed. No current official general API established. The frequently suggested `https://www.indiehackers.com/feed` returned 404 in this check. Third-party RSS wrappers exist but are not official feeds and were not adopted. **Proposed priority: high.**

### Failory — failures as well as successes

**Contains/use:** [founder interviews](https://www.failory.com/interviews), failure analyses and a startup cemetery. The interview directory includes country, industry and failure/revenue categories. Use it to look for failed predecessors of an attractive overseas model and learn what made acquisition or delivery difficult.

**Observed:** index and the [WePlate interview](https://www.failory.com/interview/weplate) were readable without browser automation. That nutrition-software example is particularly relevant when evaluating food-related software: a plausible concept needs evidence of actual customer demand.

**Access/limit:** ordinary web pages and newsletter; no supported API/export established. Interviews are selective retrospective accounts and some are old; verify present-day conditions. **Proposed priority: high as a countercheck, not the only lead source.**

### Trends.vc — structured business-model briefs

**Contains/use:** short reports covering markets, players, opportunities and objections. The public [Micro-SaaS report](https://trends.vc/trends-0032-micro-saas/) distinguishes platform-dependent, integrated and independent businesses and links examples. Useful for widening the types of businesses considered rather than collecting only fashionable launches.

**Access:** public report text readable; expanded material is marketed as Trends Pro. No supported API/export established. Ordinary web reads suffice for sampled reports; paid sections require entitlement. **Limit:** editorial hypotheses and historical examples, not proof that an opportunity remains open today. **Proposed priority: optional enrichment.**

### Exploding Topics — emerging search topics, products and startups

**Contains/use:** trend discovery with growth metrics and startup/product collections. Useful for finding themes to research and checking whether interest is recent or sustained. [Product](https://explodingtopics.com/).

**Access:** public pages plus paid platform. An official [REST API](https://api.explodingtopics.com/) documents topics, products, startups, meta-trends and database search. The [API offer](https://explodingtopics.com/feature/et-api) lists a Business-plan prerequisite starting at US$249/month and an API add-on starting at US$1,000/month for 1,000 requests; commercial integration requires a custom arrangement. Those are advertised prices, not an account quote. Documentation reviewed, no key/call tested.

**Important limit:** the API offer says it does not provide custom keyword or geography-based lookups. Do not assume it can compare India against the USA. Search growth is not sales. **Proposed priority: public browsing only initially; defer API expense.**

### Google Trends — compare interest across markets

**Contains/use:** country/region/time comparisons and related searches. Use after finding a model, comparing category terms as well as the brand, with local-language variants where relevant. This is a supporting check rather than a startup directory.

**Access:** [CSV export is officially supported](https://support.google.com/trends/answer/4365538). The [official API page](https://developers.google.com/search/apis/trends) still describes restricted alpha applications, including country/subregion coverage and five years of data; access is not automatic. No alpha enrollment or runtime query was performed. Use the UI/export until actual API eligibility is established.

**Limit:** relative search interest does not measure revenue, purchase intent or the number of addressable buyers. **Proposed priority: useful supporting source.**

### SaaSHub — competitors and neighboring software categories

**Contains/use:** [software alternatives, categories and startup listings](https://www.saashub.com/). Starting with one foreign product, discover adjacent competitors and narrower versions. This can reveal that an apparently new idea already has free substitutes.

**Access:** public pages readable. Its official [beta JSON API](https://www.saashub.com/site/api) has product lookup and alternatives lookup, returning the matched product and up to ten alternatives. Requires an account API key and attribution/disclosure under its documentation. This is lookup, not a documented bulk dump or launch firehose. No key or quota tested.

**Limit:** listings/alternatives indicate supply, not adoption. Verify fit, current pricing and India availability directly with each product. **Proposed priority: high; a practical API candidate if later selected.**

### AlternativeTo — substitute products, including free options

**Contains/use:** [crowdsourced software alternatives](https://alternativeto.net/), with platform/license categories and user opinions. Useful for mapping the strongest substitutes and testing whether the proposed local version offers anything a buyer needs.

**Access:** public homepage/listing content was readable. No current supported public API established; the historical `/api/` path returned 404. That is not proof all API arrangements are absent. Use public pages; browser interactions may help filters. **Limit:** community recommendations are not market share, verified revenue or evidence of an India-specific gap. **Proposed priority: high supporting source; choose alongside or instead of SaaSHub.**

## How to access sources

Use the lightest supported route that returns the needed evidence:

1. **Search + ordinary page reading** for relevant public records and linked original sources. This already worked for many sources in this review.
2. **Documented API, feed or permitted export** for structured/repeated collection. Confirm the actual endpoint, entitlement, allowed use and fields rather than treating an API logo as full database access.
3. **Interactive browser/Playwright** for filters, pagination, expanded cards or authorized account pages when text extraction is incomplete. A dynamic site does not automatically require a custom scraper.
4. **Provider arrangement or manual review** when the site restricts extraction or requires licensed access. Playwright does not create data rights or unlock subscriptions.

Distinguish official APIs from third-party scraping services. A vendor describing its scraper as an “API” does not make it the website's supported API. Never infer that Razorpay's payment APIs expose Fix My Itch data, or that an unrelated company with a similar name provides a marketplace API.

## Proposed scouting method for adapting an overseas model

For each promising lead, record:

- The named source product, actual customer, task, offer and business model; source date and country served.
- Evidence of adoption: distinguish a launch/votes, founder-reported revenue, estimated revenue, customers and independently supported buying behavior.
- Why the customer need might recur in India, and which specific segment/city/language is meant.
- Existing Indian competitors, global products already serving India, offline providers, spreadsheets and free alternatives.
- A concrete adaptation hypothesis: local language, local workflow, integrations, onboarding, distribution or service requirements. “Same product at a lower price” needs its own viable economics.
- Reachable first customers, their alternatives and what they might pay; operating/support costs and dependencies.
- The decisive uncertainty and next comparison or customer conversation.

Example only: discovering an overseas trade-business scheduling tool should trigger searches for Indian providers and conversations about the actual scheduling/payment workflow. It should not immediately produce a recommendation to clone it. Likewise, a foreign WhatsApp product may suggest a relevant workflow, but WhatsApp usage alone does not establish unmet Indian demand.

Deduplicate the same company across Product Hunt, YC, news and founder interviews. Preserve genuinely independent observations rather than counting five links as five confirmations. Keep finding ideas from ordinary customer communities too: these curated sources introduce their own technology, English-language, promotional and survivor biases.

## Launch platforms and company databases

Checked 2026-10-28. Primary official sources used below. Suggested uses and source biases are researcher judgments. API availability is documentation-verified, not authenticated integration-tested. “No public API verified” does not establish that none exists. Browser fallback means inspect public UI when extraction is incomplete; it is not permission to bypass restrictions.

| Source | What it contains / useful scout use | Access and caveats | Sources |
|---|---|---|---|
| YC Startup Directory | Publicly launched YC companies, filterable by batch, industry, region, status, size and hiring. Excellent foreign business-model discovery and comparing US/European vs Indian companies in the same vertical. | Free public directory/profile pages. Main directory returned no extractable text in this audit: browser useful for filters; indexed company pages may work through search. No official bulk API verified. Third-party mirrors exist but are not YC API commitments. Funding/YC acceptance does not establish paying demand. | [Directory](https://www.ycombinator.com/companies), [official directory explanation](https://www.ycombinator.com/blog/the-yc-directory) (2020 explanation; do not reuse its historical company count as current). |
| YC Requests for Startups | Investor-written problem areas and startup theses. Useful for finding structural changes and software opportunities before companies become popular. | Free readable HTML; ordinary web fetch suffices. No API needed for this small editorial corpus. Treat as investment theses, not customer pain evidence; many are capital intensive or US-specific. | [RFS](https://www.ycombinator.com/rfs) |
| Product Hunt | Product launches, makers, topics and discussion; a broad way to find new software and comments describing missing functionality. | Official GraphQL v2 at `https://api.producthunt.com/v2/api/graphql`, token required; developer token available for simple scripts. Default API use is noncommercial; business use requires contacting Product Hunt. Do not assume an internal commercial scout is exempt. Public browsing is an alternative for research, not a way to evade API terms. Launch votes are exposure signals, not revenue validation. | [official API docs](https://www.producthunt.com/v2/docs), [site](https://www.producthunt.com/) |
| BetaList | New internet startups, including pre-launch waitlists, private betas and live products new to its audience. Useful early software and localized consumer-app patterns. | Public listing HTML was readable. Daily email digest exists. **Official API access exists on a case-by-case basis**: contact form with purpose/use case/request volume, then key and docs upon approval. API pricing not established. All startup submissions now paid, plus editorial review; take selection/promotion bias into account. | [home](https://betalist.com/), [FAQ/API access](https://betalist.com/help), [API documentation linked by BetaList](https://gist.github.com/marckohlbrugge/5a29bf1ba628bb4ca960) |
| Peerlist Launchpad | Weekly project launches by builders, with project pages and feedback. Useful small-team projects and spotting practical software already being attempted. | Public weekly archive/UI. No official public discovery API/RSS verified. Extraction returned a weekly page with an empty-state message, so do not interpret that as proof that no projects exist; use browser for actual listing verification. Help search identifies launch FAQ, but help fetch failed here. | [Launchpad](https://peerlist.io/launchpad), [official indexed FAQ](https://help.peerlist.io/individual/spotlight/frequently-asked-questions-about-spotlight-by-peerlist) |
| Hacker News: Show HN + Ask HN | Show HN offers working prototypes and direct builder/user discussion; Ask HN surfaces requests, frustrations and workarounds. Strong for developer/B2B ideas and problem language; audience skews technical. | Free official public Firebase JSON API, no key shown/required; `/v0/showstories.json`, `/v0/askstories.json`, `/v0/item/{id}.json` for posts and recursive comments. Lists provide up to 200 latest Ask/Show stories, not a full historical search. Docs currently state no rate limit; still cache and pace reads. No Playwright needed. | [official HN API](https://github.com/HackerNews/API), [Show HN](https://news.ycombinator.com/show), [Ask HN](https://news.ycombinator.com/ask) |
| Wellfound | Startup profiles, categories, locations, hiring and curated company lists. Useful checking whether foreign startup categories have actual teams and Indian equivalents. | Public discover page readable; filters/more-results may need browser. No general public company-discovery API verified. Official MCP **does exist**, but documented purpose is eligible recruiter accounts' companies/jobs/applicants, not global startup discovery. Don't mistake that for a startup database API. | [startup discovery](https://wellfound.com/discover/startups), [official MCP scope/access](https://help.wellfound.com/article/1219-connect-wellfound-to-your-ai-assistant) |
| Dealroom.co | Company, investor, funding, accelerator and ecosystem data. Good for Europe as well as US/India comparison, competitor maps and cohort checks. | Official API available by sales/account-manager approval and API key. Premium CSV/Excel exports and saved-search alerts also documented. Current official API entry page points toward newer developer docs; older knowledge-base docs describe premium v1. Confirm version at implementation time. Contract/licence governs internal use and data allowances. Do not confuse with dealroom.net, a different M&A product. | [API access](https://knowledge.dealroom.co/knowledge/dealroom-api-1), [current API entry](https://dealroom.co/api/get-started/), [CSV/Excel export and alerts](https://knowledge.dealroom.co/knowledge/how-to-create-and-save-searches), [terms](https://dealroom.co/terms-and-conditions) |
| Crunchbase | Company, funding, founders/relationships, industry/location and prediction data. Useful comparing funded foreign categories with Indian incumbents; paid enrichment rather than first source for raw pain. | Official read-only REST API v4, sales-provisioned key and licensed collections/fields. Auth header `X-cb-user-key`. Search supports company filtering and pagination. Current docs also advertise MCP, a separate access arrangement; no assumption it comes with a website subscription. Do not rely on old v3/free Open Data Map tutorials for new access. | [data portal](https://data.crunchbase.com/), [API access](https://data.crunchbase.com/docs/api-essentials), [search](https://data.crunchbase.com/docs/search-api-basics), [REST/MCP distinction](https://data.crunchbase.com/docs/make-your-first-api-request) |
| Tracxn | Company, funding, acquisition and news datasets; sector landscape/competition research. Useful deeper Indian competitor checks against overseas model candidates. | Official APIs with account token; annual subscription typically by unique companies accessed. CSV/JSON scheduled data dumps and Snowflake available; platform exports consume credits. Limited Lite/trials exist; API/data-solution scope and pricing are separate. Pricing explicitly distinguishes internal research licences from commercial redistribution. No Playwright needed when subscribed to API or exports. | [API FAQ](https://help.tracxn.com/en/articles/8512359-getting-started-with-tracxn-apis), [pricing/access/licences](https://tracxn.com/pricing) |


## Problem banks, India context and adaptation sources

Checked 2026-10-28 using primary public pages and targeted API/RSS searches. “No documented API found” is limited to this investigation; it is not proof of absence. Browser initialization failed before any interaction; details below.

| Source | Contents and scout value | Access actually observed / integration route | Limitations and priority |
|---|---|---|---|
| [Razorpay Fix My Itch](https://razorpay.com/m/fix-my-itch/#all-problems) | India-specific pain statements, categories and an “itch score”; examples include SME invoicing, supplier verification, industrial repair delays. Strong problem-first seed source. | Public text reader retrieved top-ten cards plus ten B2B rows with scores. It did **not** expose all categories’ contents, individual details, or pagination. Browser category/modal inspection is the next step. No official problem-bank API/export found; Razorpay payment APIs are unrelated. | High priority. The advertised 10,000+ verified problems / 50K people are publisher claims, not the number of records we retrieved or independent validation. Treat generated/curated scores as hypotheses. |
| [Startup India Idea Bank](https://www.startupindia.gov.in/content/sih/en/idea_bank.html) and [Programs/Challenges](https://www.startupindia.gov.in/) | Indian societal problems, possible solution avenues and responsible ministries; challenge briefs sometimes have concrete workflows. Useful India-native problem inventory and institutional buyers. | Idea Bank text fully readable via ordinary web fetch; public challenge pages/PDFs also usable. No public discovery API documented in this check. | Medium priority. Some Idea Bank statistics and initiatives are visibly historical; refresh underlying evidence. A challenge is a sponsor need, not evidence of recurring commercial demand. |
| [BHASKAR](https://www.startupindia.gov.in/bhaskar), [official FAQ](https://www.startupindia.gov.in/bhaskar/about) | Registry/network of Indian founders, investors, mentors and ecosystem participants; useful for finding local analogues and eventual expert interviews. | Public overview/FAQ readable. Profile/network experience requires follow-up in signed-in UI. Official FAQ says completed BHASKAR profiles become searchable. No public directory API confirmed; government-to-government portal integration references do not establish public access. | Supporting source, not primary idea generation. A registered profile does not establish commercial traction. |
| [Microns](https://www.microns.io/) | Micro SaaS, apps and small online businesses for sale; public summaries include annual revenue and asking price, with sold examples. Good for discovering narrow, monetized workflows that may be adaptable to India. | Ordinary page fetch returned many actual listings and sold cards. All listings link to account signup; email newsletter offered. No first-party listing API/RSS/export found in targeted search. | High-interest supplementary source. Revenue/sold amounts are marketplace claims, not audited proof; valuation and seller-selection bias. Public listing sample is enough for initial pattern discovery. |
| [Acquire.com](https://acquire.com/) | Online businesses for sale with financial and operational metrics; useful for studying monetization patterns and mature small-business categories. | Marketing page readable, listing application requires separate UI/login. No public marketplace API confirmed. **Exclude automated ingestion without written permission:** [buyer/seller terms](https://acquire.com/buyerseller/) prohibit automated and manual extraction of listing/profile data and automatic queries. The commonly found Acquire API is acquire.io, an unrelated customer-support product. | Defer as scout data feed; ask provider for licensed route if desired. Terms state seller/buyer data is not guaranteed by Acquire. Public editorial case studies may be more practical than marketplace extraction. |
| [YourStory](https://yourstory.com/) | Indian founder stories, launches, funding and sector reporting; helps check whether a foreign idea already has Indian competitors and understand local adaptations. | Homepage and article links available through ordinary web reader. RSS-named pages appear in search but provided only generic headings; `/rssFeed` fetch failed. **Working RSS not verified**; no public content API documented in check. Use public articles/search initially. | High priority for India cross-check, lower as demand validation. Funding/newsworthiness can bias coverage; follow through to company/product/customer evidence. |
| [Inc42 / Datalabs](https://inc42.com/datalabs/) | India startup database, funding/financials, sector filters and alerts. Strong structured check for Indian incumbents and category economics. | Official page explicitly advertises CSV, Excel, PDF exports and snapshots; [terms](https://inc42.com/terms-and-conditions/) confirm paid-plan structured exports and custom data requests. No public API verified. Prefer licensed export, not browser scraping; terms restrict automated extraction without express written consent. | Strong paid optional source. Exact pricing/trial claims vary even within the public page; confirm before buying. Exports licensed for internal use with plan limits; no account/export executed. |
| [Springwise](https://springwise.com/), [bespoke services](https://springwise.com/bespoke-services/) | Global editorial innovation database, filters by geography/industry/business model, with sustainability and impact emphasis. Good source of overseas operating models, especially climate, circular economy and infrastructure. | Public homepage and free content readable. Member database/login separate. **Official bespoke service explicitly offers curated data through API or file uploads.** This is a negotiated service, not a tested self-serve API; no credentials or endpoint tested. | High-interest optional source where climate/impact fits. Many entries concern hardware/research, not lean software opportunities. Geography coverage and editorial selection are not evidence an idea will work in India. |
| [Trend Hunter](https://www.trendhunter.com/), [RSS information](https://www.trendhunter.com/rssfeeds) | Consumer trends, new products, services, innovation concepts and reports; useful for spotting overseas formats to localize. | Homepage web text was a shell, RSS page readable but thin. `https://www.trendhunter.com/rss` returned content type `text/xml`, which this web reader cannot parse; endpoint presence observed, items not parsed. [Official terms](https://www.trendhunter.com/terms) explicitly document RSS use. No first-party data API verified. | Optional consumer inspiration source. RSS is a plausible route before browser automation, but validate XML and feed scope first. Trend/novelty signal is not paid-demand evidence; feed redistribution restrictions apply. |
| [IdeaBrowser](https://www.ideabrowser.com/idea-of-the-day) | Candidate curated/AI-assisted startup-idea database. Exact present feature set and pricing **not independently confirmed from primary page** in this check. | Root and daily-idea page returned HTTP 403; `/ideas` inaccessible. Targeted primary-domain search did not reveal usable API/RSS documentation. Browser access with normal permissions may work, but was not tested. | Keep on evaluation list, not verified shortlist. Third-party descriptions disagree on pricing and should not be used as current facts. Do not label “no API” conclusively. |

## Additional concrete primary example

[Startup India EODB challenge problem statements](https://www.startupindia.gov.in/content/sih/en/India_EODB_Grand_Challenge/problem-statement.html) give explicit workflows such as return filing for small businesses and matching small export consignments to partially filled shipping containers. Useful to illustrate why official challenge banks can produce more actionable seeds than generic idea lists, while recognizing archived briefs may already be solved.

## Razorpay browser follow-up

Read the installed browser skill and attempted its prescribed runtime setup. Initialization failed with `Importing module "node:process" is not allowed in node_repl`; no browser interaction occurred. Consequently, switching categories, opening individual problem details and enumerating the full dataset remain **unverified**, rather than proven to require Playwright. Ordinary web reading already works for the visible initial sample. The full ingestion decision needs a subsequent working-browser check or a provider-supported data export.

## Next decision

**Next owner: user**, to select the source mix and whether overseas-to-India adaptation should be a regular discovery route or an optional brief. Suggested discussion: start with free public sources, retain founder stories and failures, and defer paid database/API commitments. After selection, update the scout's source catalog/discovery instructions and any affected map entries together. No skill changes are part of this research round.
