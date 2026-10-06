# Contact-tool setup research

Checked 2026-10-06 for [Guide and verify the selected tool setup](../issues/13-guide-tool-setup.md). Official sources were opened; no accounts, credentials, live contact lookups, installations, or connections were used. Published allowances do not establish this user's eligibility, remaining balance, connection, or useful market coverage.

## Current environment limitation

The parent session reports both catalog integrations as uninstalled, `DISABLED_BY_ADMIN`, and `NOT_AVAILABLE`; its Hunter listing is company-level only. Those integrations cannot currently be enabled here. The independent provider routes below document technical availability, not permission to circumvent that restriction. Organization permission for another integration route remains unknown. The parent also reports no Hunter/Apollo API-key variables in the current process; this does not establish that the user has no account or credentials elsewhere.

## Hunter: published facts

- The permanent Free plan includes **50 shared credits/month**, API access, email finding/verification, and basic Discover. No card is required. Free excludes premium Discover filters, automatic lead verification, and saved-Leads enrichment; it limits AI Discover searches to 10/month and exports to 10 emails/domain. [Free-plan details](https://help.hunter.io/en/articles/11060999-what-s-included-in-hunter-s-free-plan)
- The official remote MCP is `https://mcp.hunter.io/mcp`, available on free plans without a separate connection charge. It supports company discovery, contact finding, verification, and enrichment. Its documented API-key route uses `X-API-Key`; the provider also describes OAuth where supported. The user's actual client tools and scopes still need inspection. [Official MCP](https://hunter.io/mcp)
- Create or inspect a dedicated key in [Hunter API keys](https://hunter.io/api-keys). The API supports multiple keys; keep values out of chat, repository files, and logs. `test-api-key` returns dummy data for Domain Search, Email Finder, and Email Verifier, so it cannot establish account access or contact quality. [API guide](https://help.hunter.io/en/articles/1970956-hunter-api)

| Relevant API operation | Published credit cost / limitation |
| --- | --- |
| Discover companies | Zero credits; premium filters require an eligible paid plan. |
| Domain Search | 1 credit per 1–10 returned emails per domain. |
| Email Finder | 1 credit when an email is found. |
| Email Verifier | 0.5 credits per verification. |
| Email/person, company, combined enrichment lookup | 0.2 credits when the required data fields are returned; verify the account's usable endpoint access. |

Costs above are from the [API guide](https://help.hunter.io/en/articles/1970956-hunter-api); web-app Domain Search accounting differs, so do not substitute website prices for API costs. [Credit accounting](https://help.hunter.io/en/articles/1911617-how-do-credits-work-in-hunter)

Hunter distinguishes lookup enrichment from enriching a saved Lead in place. The latter returns an unchanged lead on Free; this is not evidence that the separate People lookup API is forbidden. Discover API returns up to 100 companies; pagination and changing the result limit require Premium. The Account Information/Usage endpoints expose plan and remaining requests without a contact lookup. Verification can return `unknown` or `accept_all`; these do not establish a usable named mailbox. [API reference](https://hunter.io/api-documentation/v2)

## Apollo.io: published facts and remaining ambiguity

- Apollo's September 2026 first-party explanation states **75 credits/month** on Free. Treat this as a published allowance, not the user's verified balance. The current pricing page's plan values did not render in this research fetch. [Free-plan explanation](https://www.apollo.io/insights/how-do-i-build-a-prospect-list-on-apollos-free-plan-without-burning-credits), [pricing](https://www.apollo.io/pricing)
- Current endpoint references permit free accounts registered with a **work email**, while reserving additional eligibility checks. Free personal-email accounts cannot use the relevant search/enrichment functions. A work email therefore establishes a prerequisite, not guaranteed approval. [People Search](https://docs.apollo.io/reference/people-api-search), [developer FAQ](https://docs.apollo.io/docs/developer-faqs)

| Relevant API operation | Published access/cost distinction |
| --- | --- |
| People Search | 0 credits; returns prospect/profile data without email addresses or phone numbers. [Endpoint](https://docs.apollo.io/reference/people-api-search) |
| Organization Search | 1 credit/page, up to 100 companies/page. [Endpoint](https://docs.apollo.io/reference/organization-search) |
| People Enrichment | 1 credit for qualifying demographics/email; +8 for returned mobile phone. Waterfall vendors can have different charges, including unsuccessful lookups. [Endpoint](https://docs.apollo.io/reference/people-enrichment) |
| Organization Enrichment | 1 credit/company according to the endpoint reference. [Endpoint](https://docs.apollo.io/reference/organization-enrichment) |

These endpoint costs may consume included Free credits; credit consumption does not itself mean a paid subscription is required. Nevertheless, the general pricing FAQ describes advanced/custom API access on Custom plans, while endpoint docs describe Free eligibility. Also, the API pricing summary omits Organization Enrichment even though its endpoint specifies a charge. Use the actual account and endpoint result to resolve eligibility; budget organization enrichment as chargeable. [Pricing](https://www.apollo.io/pricing), [API credit guide](https://docs.apollo.io/docs/api-pricing)

The official MCP is `https://mcp.apollo.io/mcp`, using Streamable HTTP with browser OAuth; no local installation or API key is needed for that route. Headless authentication instead requires a **master API key** in `X-Api-Key`, with workspace-wide authority. OAuth is preferable for user-scoped access if an approved route becomes available. Apollo requires model training disabled in the AI client. Tool availability and credits remain plan/account dependent; MCP connection has no extra provider fee. [Official MCP instructions](https://docs.apollo.io/docs/apollo-mcp)

For an approved REST integration, Apollo documents **Settings → Integrations → API Keys → Create new key**. Select only necessary endpoints; the master-key requirement is specific to MCP and certain endpoints. Store a generated key securely without posting it. [Key creation](https://docs.apollo.io/docs/create-api-key)

## Next manual steps, one at a time

1. Establish whether Hunter and Apollo accounts already exist. Ask for only `Hunter: yes/no; Apollo: yes/no`, then the nonsecret plan name and remaining credits. For Apollo, ask only whether registration uses a work or personal email; do not request the address.
2. For Hunter, the user can sign in through [Hunter API keys](https://hunter.io/api-keys), or inspect [free signup](https://hunter.io/users/sign_up). Verify Free plan and allowance in the account. For Apollo, use [sign in](https://app.apollo.io/) or [free signup](https://www.apollo.io/sign-up), then **Settings → Billing and credits → About credits / Credit usage**. Record what the user actually sees. These links do not authorize a purchase, trial upgrade, mailbox connection, or campaign.
3. Keep the disabled catalog integrations deferred. Establish an organization-approved connection route before generating/configuring credentials for integration. Do not build an adapter to evade the restriction. A free account may still be useful manually, but manual use is not a verified agent connection.
4. Once an approved route is usable, inspect tools and account/quota metadata before a bounded test. Use only a small, relevant company/person sample agreed during setup. Check free balance before and after; avoid phone and waterfall enrichment initially, pagination, paid add-ons, and overages. Apollo provides credit usage under **Settings → Billing and credits** and rate limits under **Settings → Integrations → API Keys → Usage**. [API credit checks](https://docs.apollo.io/docs/api-pricing)
5. Record connection, endpoint eligibility, credit delta, and data quality separately. A successful metadata call is connectivity evidence only. A tiny successful sample cannot establish broad market coverage; no result or uncertain verification remains a gap. Keep sending, sequences, and mailbox setup outside this task's enabled capabilities.

No paid-only portion needs to block the skill suite: record the exact unavailable capability and retain public company pages, published business contact routes, and human-assisted research.
