# Startup skill tools

Existing capabilities are reused for scouting and investigation. All three keys passed authentication checks on 2026-10-10. Tavily is configured locally for VS Code and its configured process passed a live search; Hunter/Apollo MCP connections are deferred. Details: [Guide and verify the selected tool setup](.scratch/startup-skills/issues/13-guide-tool-setup.md#answer).

| Tool or service | Setup/location | Why we use it | Status/check date |
| --- | --- | --- | --- |
| Web search and page reading | Existing session tools | Research customer problems, alternatives and business inputs | Reused; search and YC page retrieval rechecked, 2026-10-06; broader site access varies |
| Local Markdown files | `.agents/skills/`, `docs/startup-skills/`; outputs in `opportunities/` and `scouting-runs/` | Preserve evidence, test plans and history across sessions | Scout and investigator each passed structural checks and four behavioral scenarios, 2026-10-06; outputs isolated in temporary workspaces |
| Tavily | [.vscode/mcp.json](.vscode/mcp.json); loads root `.env`: `TAVILY_API_KEY`; Bearer header | Selected supporting search/extraction/crawl service | 2026-10-10: all four operations passed; configured launch also passed tool discovery and search. Crawl content partial; VS Code UI start not observed |
| Hunter | Root `.env`: `HUNTER_API_KEY`; `X-API-KEY` header | Optional business-email lookup and verification | 2026-10-10: account/domain lookup passed; last checked balance 49. MCP deferred: provider DNS error 1000; fresh email verification unchecked |
| Apollo | Root `.env`: `APOLLO_API_KEY`; `X-Api-Key` header; user chose master key | Optional company/person research | 2026-10-10: authentication passed; People Search excluded from this Free plan. MCP deferred: provider denied this client's connection (1010) |

In VS Code, run **MCP: List Servers → tavily → Start**, then check its four tools in Chat. This config serves VS Code's MCP client; Codex's separate configuration is unchanged. It uses existing Node and locally installed `mcp-remote@0.1.38`; to restore the bridge, run `npm ci --prefix .vscode/mcp --ignore-scripts`. The small launcher lets VS Code reuse `.env` without copying keys into config. The unselected Tavily research tool is filtered out.

[Live access checks](.scratch/startup-skills/checks/tool-access.md#local-vs-code-mcp-configuration--2026-10-10) record limits. Tavily's API reports 1,000 included credits versus screenshot 1,500; paygo-off status is unconfirmed, so check allowance before use. Existing web tools remain fallbacks. In-app plugins remain administratively unavailable. No paid upgrade, overage, sending or campaign setup was performed.
