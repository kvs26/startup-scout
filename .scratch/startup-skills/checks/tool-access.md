# Live tool access checks

Checked 2026-10-10 for [Guide and verify the selected tool setup](../issues/13-guide-tool-setup.md). Read keys from root `.env` without shell evaluation. Sent each key only to its provider in a request header; no key values, raw contact details, or full account profiles were printed or saved. Initial sandbox requests failed without a service response; the following checks succeeded through approved network escalation.

Current outcome: Tavily is configured and tested through the VS Code launch configuration; optional Hunter/Apollo MCP is deferred. Earlier sections below preserve the checks in order; the [local configuration check](#local-vs-code-mcp-configuration--2026-10-10) supersedes their pending-registration notes.

| Service / operation | Observed result | Limits / credit use |
| --- | --- | --- |
| Apollo `GET /api/v1/auth/health` | HTTP 200; `healthy=true`, `is_logged_in=true` | Confirms authentication only. User reports choosing a master key. |
| Apollo `POST /api/v1/mixed_people/api_search` | HTTP 403; `API_INACCESSIBLE`. Provider states People Search is excluded from this account's Free plan, even with a master key. | One sample attempted for a sales role at `apollo.io`, one result requested; repeated once to inspect the error. No profile or contact data returned. Published documentation lists zero credits for this operation; account usage was not separately retrieved. No upgrade or alternative endpoint was attempted. |
| Hunter `GET /v2/account` | HTTP 200; Free plan; initially 50 credits remaining | Account checks are free. |
| Hunter `GET /v2/domain-search` | HTTP 200; one generic business address for `apollo.io`, matching the requested domain, with two cited sources and provider verification status `valid` | `type=generic`, `limit=1`; credit balance fell from 50 to 49. Contact value was not saved. This is a vendor assertion and a tiny functionality sample, not independent deliverability verification, named-buyer discovery, or broad market coverage. |
| Tavily `GET /usage` | HTTP 200; Researcher; account `plan_usage=0`, `plan_limit=1000`, `paygo_usage=0`, `paygo_limit=null`; key usage 0 and limit null | Confirms authentication and reported quota. The earlier screenshot showed 1,500 monthly credits; discrepancy remains unresolved. Null paygo limit does not prove pay-as-you-go is disabled. No retrieval operation performed yet. |

The `apollo.io` domain is a bounded provider-company test fixture, not a selected startup opportunity, country preference, or outreach target. No messages, sequences, saved leads, phone enrichment, paid upgrade, or overage were initiated.

## Authentication and remaining work before MCP setup

- Apollo: use `X-Api-Key`, following its [authentication guide](https://docs.apollo.io/reference/authentication). The URL-parameter deprecation does not require replacing a valid key. The account's actual denial takes precedence over generic documentation describing possible free access. Defer the unavailable API search capability under the agreed free-only rule; website access and other endpoints are not proven by this check.
- Hunter: used `X-API-KEY`, supported by the [API reference](https://hunter.io/api-documentation/v2). Domain lookup is verified; Email Finder and a fresh Email Verifier operation remain unchecked. Stored provider verification status is not a new verification call.
- Tavily: used `Authorization: Bearer`, as documented for [usage](https://docs.tavily.com/documentation/api-reference/endpoint/usage). Awaiting the user's response about the visibly enabled pay-as-you-go setting before the next manual setup step; search/extraction/crawl and the selected official MCP route remain unverified.

These are direct provider API checks from the local environment. They do not install or enable the administratively unavailable in-app Hunter/Apollo connectors or establish persistent MCP configuration. The setup ticket remains unresolved until its required retrieval and runtime setup checks are complete.

## Requested authentication recheck — 2026-10-10

The user requested another check of every saved key and completed Hunter/Apollo entries in root `TODO.md`. Repeated only the official read-only account/health calls, with header authentication and sanitized output:

- Hunter: HTTP 200, Free plan, 49 credits remaining.
- Apollo: HTTP 200, `healthy=true`, `is_logged_in=true`.
- Tavily: HTTP 200, Researcher, plan usage 0 of 1,000; paygo usage 0 and limit null.

All three keys passed. No credit-consuming lookup was repeated. This recheck does not remove Apollo's observed People Search denial or establish Tavily retrieval/MCP readiness. `TODO.md` marks account/key setup separately from remaining integration work.

## Tavily retrieval and official MCP checks — 2026-10-10

After the user asked whether setup was resolved, completed the remaining read-only retrieval checks through `https://mcp.tavily.com/mcp/` with Bearer authentication. The official server successfully initialized using MCP protocol `2025-03-26` and listed search, extraction, map, crawl, and research tools. Research was not invoked. The bounded [verification script](verify-tavily.py) is a planning/test artifact, not a runtime integration or a registered client.

| Operation | Bound | Result |
| --- | --- | --- |
| `tavily_search` | Basic search, one result, `ycombinator.com` | Returned the relevant YC Requests for Startups page. |
| `tavily_extract` | One URL, basic extraction | Returned one result for the requested page; response contained about 19,000 characters including metadata and page content. |
| `tavily_map` | Depth/breadth/page limit 1; external links disabled | Returned the requested URL. This tests basic mapping, not multi-page coverage. |
| `tavily_crawl` | Same one-page bound; basic extraction | Returned one result with a short excerpt, mostly navigation in the visible output. Treat content as partial and use extraction for fuller reading. |

All four calls returned no JSON-RPC error and no tool-error flag. Successful calls do not establish complete page content or broad crawl coverage. Usage preflight verified 1,000 included plan credits remaining and required a conservative 10-credit buffer before running the strictly bounded requests. Immediate post-check counters remained `plan_usage=0` and `paygo_usage=0`; this may reflect delayed reporting and is not proof that the operations cost zero. No billing setting was changed, and pay-as-you-go toggle status remains unconfirmed. Its prior screenshot is not a blocker for these bounded tests within verified included credits, but future use must continue checking allowance and avoid paid overages.

Local Codex help confirms `mcp add --url` and `mcp login`. A fresh read of local configuration still lists only `computer-use` and `node_repl`; there is no project MCP configuration. The in-app plugin directory also reports Tavily as `DISABLED_BY_ADMIN` / `NOT_AVAILABLE`, uninstalled. This is separate from the successfully tested official server; no plugin or client setting was modified.

For an allowed Codex CLI connection, the documented manual route is `codex mcp add tavily --url https://mcp.tavily.com/mcp/` followed, if needed, by `codex mcp login tavily`, completing the provider's browser authorization. This configures that client; it does not enable an administratively disabled in-app plugin or establish availability in every app. Verify the intended client's loaded tools after registration. Any policy refusal remains a restriction, not a reason to bypass it. Sources: [official Tavily MCP guide](https://docs.tavily.com/documentation/mcp), [OpenAI MCP setup](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).

## Local VS Code MCP configuration — 2026-10-10

The user explicitly selected `.vscode/mcp.json` and delegated local MCP setup. The [VS Code configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration) supports this location and `envFile` for stdio servers, but does not support `envFile` on HTTP server entries. Installed the pinned [mcp-remote bridge](https://github.com/geelen/mcp-remote) locally under `.vscode/mcp/`, with a lockfile and install scripts disabled. A 24-line launcher supplies a literal environment-variable placeholder to the bridge, which expands it into the Bearer header inside the process. No secrets are copied into JSON, process arguments or URLs; Hunter/Apollo keys are removed from the bridge's environment. Runtime dependencies and local authentication state are ignored. The published package was inspected directly: its header-file option is absent, despite appearing on the upstream main branch, so that option is not used.

The exact command, arguments and environment specified in `.vscode/mcp.json` were launched from this workspace and checked over stdio:

- Valid JSON; missing-key startup fails with an actionable message.
- MCP initialization passed with protocol `2025-03-26`.
- Tool discovery returned `tavily_search`, `tavily_extract`, `tavily_map`, and `tavily_crawl`. The unselected `tavily_research` tool is filtered by the bridge.
- One basic search limited to one result on `ycombinator.com` returned the expected public source without RPC/tool errors. Usage preflight reported 0/1,000 included credits; no broader or repeated retrieval test was needed.
- Captured stdout/stderr contained none of the saved key values; stderr was empty. The verification process was stopped afterward.

This is a live test of the configured server process, not observation of the VS Code UI. Normal first use remains **MCP: List Servers → tavily → Start**, then inspect its tools in Chat. VS Code/Copilot uses this configuration; it does not register a server in Codex's separate MCP configuration or change this app's connector policy. Restore dependencies with `npm ci --prefix .vscode/mcp --ignore-scripts` if needed.

The optional providers' documented MCP endpoints were checked with header authentication and read-only initialization/tool-list requests only:

| Provider | Endpoint | Observed outcome |
| --- | --- | --- |
| [Hunter MCP](https://hunter.io/mcp) | `https://mcp.hunter.io/mcp` | HTTP 403 with Cloudflare error 1000, DNS points to prohibited IP. This is a provider endpoint problem, not proof of an invalid key or Free-plan denial. |
| [Apollo MCP](https://docs.apollo.io/docs/apollo-mcp) | `https://mcp.apollo.io/mcp` | HTTP 403 with Cloudflare error 1010, client signature denied; provider says owner action is required. No retries or alternate clients were attempted after identifying this refusal. This is separate from the earlier REST People Search plan denial. |

Only the working Tavily server was registered. Hunter/Apollo MCP remain explicitly deferred under the blueprint's conditional-access rule; existing account/key checks remain valid, and Hunter's tested direct API lookup remains distinct from MCP availability. No sending/campaign tools were activated. These optional gaps do not block skill implementation; no paid entitlement, broad contact coverage or fresh email verification is claimed.
