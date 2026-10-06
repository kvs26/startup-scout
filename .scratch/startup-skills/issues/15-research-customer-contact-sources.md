# Research customer contact sources and access across markets

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:research
Type: research
Mode: AFK
Status: resolved
Assignee: customer-contact-research
Blocked by: none

## Question

How can `startup-customer-connect` identify suitable organizations, relevant people, and usable business contact routes for an opportunity, with no fixed market preference and sources chosen according to each opportunity?

Use current primary sources to compare LinkedIn and its API access, company websites, market-relevant business/industry directories and event or association lists (the initial checked examples are Indian), local business discovery, and a small shortlist of business-contact services such as Hunter or Apollo. Explain which resources identify organizations, roles, individual people, or contact routes; do not confuse these outputs. Check whether ordinary browsing, human account use, or an API is appropriate, and record documented account/access/cost restrictions and source/storage limits that affect the proposed workflow. Do not assume coverage in any selected market from global marketing claims or promise contact accuracy or response.

Explain a practical workflow by opportunity type, including fallback to a business inbox, contact form, association, or introduction when a named contact is unavailable. Separate public source evidence, vendor-supplied data, inferred details, and unknowns. No collection of real prospect lists, account creation, installation, paid trial, or outreach is authorized by this research.

Write cited findings directly under `## Answer` using the map's no-Git research exception. Findings inform [Agree the startup skill suite blueprint](08-decide-suite-blueprint.md); tool adoption remains a live decision, and [Guide and verify the selected tool setup](13-guide-tool-setup.md) owns later setup and actual connection checks.

## Comments

### 2026-10-03 — Contact-source research requested

The user accepted task-specific customer-connection preparation but asked how contacts will actually be found, whether LinkedIn and other sources need APIs, and how the approach changes with the idea and target market. The initial research interpreted their India comment as a preference; the user explicitly corrected that interpretation below. This ticket supplies facts needed for the pending blueprint choice.

### 2026-10-03 — No market preference; industry scope reaffirmed

The user explicitly removed any India-first preference. Market choice depends on the idea; India, the US, other developed markets, and other relevant markets are all eligible. They highlighted that SaaS/technology may suit US or other developed markets without imposing those as the new default. The title, question, and workflow have been corrected. The Indian directory examples remain bounded research findings, not a preferred-market rule.

The suite discovers software, AI, and similar technology opportunities serving any industry. Clinic examples are illustrations only. Apollo here means the business-contact service at `apollo.io`; its inclusion does not impose a healthcare focus and it has not been adopted.

## Answer

### Resolution — 2026-10-03

The skill can combine organization discovery, identification of relevant roles or people, and lookup of a usable business contact route. These are three different steps. A company listing is not a decision-maker, a job title is not proof of buying authority, and an email lookup is not proof that someone wants the product. There is no fixed market preference. Choose the country or countries, city where relevant, industry, company type, and buyer role according to each opportunity. India, the US, other developed markets, and other suitable markets remain open; SaaS and technology opportunities may warrant investigating the US or other developed markets without making those a universal default.

These findings establish available approaches, not provider adoption. No prospect list was collected, account connected, subscription purchased, or outreach sent. [Agree the startup skill suite blueprint](08-decide-suite-blueprint.md) owns adoption; [Guide and verify the selected tool setup](13-guide-tool-setup.md) owns account-specific connection and capability checks.

### Sources and what each contributes

| Resource | Useful output | Access and limitations |
| --- | --- | --- |
| Company websites | Evidence about the organization; team/leadership names when published; contact page, business inbox, switchboard, or enquiry form | Search and ordinary page reading often suffice. Look for each company's actual published contact route; do not invent an email from its naming pattern. No universal API or completeness assumption. This is a workflow recommendation, not a claim that every company publishes these fields. |
| LinkedIn / Sales Navigator | People and company discovery; role, geography, function, seniority, company-size filters; possible warm introductions | Human use of an authorized account is a viable route. Sales Navigator is a subscription product; exact access depends on the plan. Its search interface is not a general-purpose public people-search API. [Official filters](https://business.linkedin.com/sell/sales-navigator/advanced-search-filters), [usage guide](https://business.linkedin.com/sell/sales-navigator/how-to-use). |
| ACMA | India automotive-component organization discovery | Its public homepage exposes Member Search separately from Member Login. This check establishes the entry point, not full results access, downloadable contacts, or a supported API. [ACMA](https://www.acma.in/). |
| IMTEX | Manufacturing-sector companies with country, website, hall and stall | The public exhibitors table is readable without an API. Use it to find relevant organizations and then inspect their own sites. An exhibitor can be a supplier, partner, competitor, or customer; participation alone does not establish buyer fit. [Official exhibitor list](https://www.imtex.in/exhibitor_list.php). |
| CII member directory | Indian organizations, capabilities, products and services | CII documents online directory subscriptions; do not promise free full access or an open API. Check current access and price only if selected. [CII directory](https://www.cii.in/MembersDirectory/index.html). |
| Google Maps / Places | Local establishments and locations, with business details available through the product/API | Maps browsing and Places API integration are different access modes. Places requires enabled billing and API authentication, with request/field-dependent charges. It is primarily place discovery, not a database of named buyers. [Usage and billing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing). |
| Hunter | Domain-to-business-email search; a known person's likely email; verification | Browser product or official API with an account/key and available credits. Domain Search can return generic or named professional addresses, showing sources and inferred labels. Finder and verifier are separate operations. [Domain Search](https://help.hunter.io/en/articles/1830792-domain-search-find-emails-from-companies), [API guide](https://help.hunter.io/en/articles/1970956-hunter-api), [API reference](https://hunter.io/api-documentation). |
| Apollo | Filtered company/person discovery and separate contact enrichment | All plans have at least basic API access, but endpoint/plan/credit limits apply. People Search returns limited person/company information, **not email addresses or phone numbers**; enrichment is separate. Free-account access to that search requires a work email and may have additional eligibility checks. [People Search](https://docs.apollo.io/reference/people-api-search), [developer FAQ](https://docs.apollo.io/docs/developer-faqs), [credit rules](https://docs.apollo.io/docs/api-pricing). |

The association/event examples are starting sources for particular industries, not a fixed catalog for every idea. No documented public API was verified for ACMA, IMTEX, or CII during this bounded review.

### Important integration distinctions

**LinkedIn:** official developer documentation distinguishes open permissions from approved programs. Sales integrations require approval as a Sales Navigator Application Platform (SNAP) partner. Buying Sales Navigator does not itself establish developer approval or authorize a general people-search API. LinkedIn also prohibits scraping and unauthorized website automation. The practical initial design is agent-prepared search criteria, human LinkedIn/Sales Navigator use where needed, and company-site or separately licensed contact lookup. Do not make a LinkedIn scraper a hidden dependency. [API access documentation](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access), [LinkedIn automation restrictions](https://www.linkedin.com/help/linkedin/answer/a1341387/prohibited-software-and-extensions).

**Google Places and saved records:** Google's policy restricts storing Places content beyond allowed exceptions; place IDs are explicitly exempt. Attribution requirements also apply to displayed results. A permanent Markdown prospect database must not blindly retain raw Places responses. If adopted, design storage around permitted fields and independently sourced company-site facts with their own provenance. A fact copied from a Places response does not become independently sourced simply by changing its citation. [Places policy](https://developers.google.com/maps/documentation/places/web-service/policies), [place IDs](https://developers.google.com/maps/documentation/places/web-service/place-id). This review did not establish a bulk-extraction entitlement for ordinary Maps browsing.

**Hunter versus Apollo:** Hunter is a direct candidate when the company domain or person's name is already known and the missing item is an email route. Hunter distinguishes public sources from inferred addresses, provides source links/dates, and marks verification uncertainty; retain those distinctions. Apollo is a candidate when identifying people by role/company/location is itself the gap; search and enrichment have different outputs and costs. Apollo's location filters distinguish a person's location from an employer's headquarters, so an India-headquarters filter can exclude Indian employees of overseas firms. [Hunter source and verification explanation](https://help.hunter.io/en/articles/1830792-domain-search-find-emails-from-companies), [Apollo filters](https://docs.apollo.io/reference/people-api-search).

Hunter calls use credits according to endpoint and account type; Apollo enrichment and some organization operations also consume credits, with account-specific and legacy-plan differences. Do not estimate a subscription cost from a remembered price or treat free search as free revealed contacts. The setup ticket should verify the selected account's endpoint eligibility, credit debit, quota and export/storage rights before a real run. [Hunter API credit rules](https://help.hunter.io/en/articles/1970956-hunter-api), [Apollo API credit rules](https://docs.apollo.io/docs/api-pricing). This review did not establish unrestricted redistribution rights for either vendor.

### Proposed opportunity-adaptive workflow

1. Read the saved opportunity and immediate goal: learning conversation, pilot offer, sales meeting, or negotiation. Propose relevant market(s), customer segment, location where useful, and role based on the opportunity and evidence; expose assumptions about who uses, influences, and pays for the product.
2. Choose sources according to that segment. For a clinic or local retailer idea, investigate local establishments and their own sites. For software serving auto-component factories, start with an appropriate association/event list and company sites. For enterprise software, investigate companies and relevant functions, with LinkedIn or Apollo as possible people-finding routes. For a consumer idea, community organizers and voluntary research recruitment may be more useful than business-email databases. These are proposed routes, not empirically validated coverage claims.
3. Confirm organization fit and current role before spending contact-reveal credits. Use a small, explicitly bounded sample in later setup/testing to measure how many relevant organizations, named people and usable routes each provider actually returns.
4. Prefer the route appropriate to the purpose: a published business contact, named professional email when supported, company enquiry form, switchboard, association introduction, or a warm introduction the user can request. If a named contact cannot be found, preserve that unknown and offer the organizational route.
5. Save only permitted information: organization and market; proposed role and why it matters; named person if supported; contact route; source URL/vendor and observation date; public, vendor-supplied, inferred, or unknown status; verification status/date; current-employer uncertainty; fallback and next action. Separate deliverability evidence from role relevance and willingness to engage.
6. Prepare the introduction, questions or offer around that goal, with the user deciding whether to act. Feed actual replies and meeting notes back to investigation later.

### Remaining uncertainty

No market-specific coverage or accuracy rate was established for Hunter, Apollo or LinkedIn, and no authenticated provider calls were made. Country filters and global database claims do not demonstrate coverage in India, the US, other developed markets, particular cities, or a particular buyer role. The directly checked association/event examples are Indian; they illustrate a source family rather than constituting a worldwide directory review. Find and check appropriate local sources when an opportunity warrants another market. No source can promise a reachable named person or a response. The blueprint can specify this adaptable method now; the setup ticket should test any selected provider against a representative, authorized small sample and keep useful fallbacks when coverage is weak.
