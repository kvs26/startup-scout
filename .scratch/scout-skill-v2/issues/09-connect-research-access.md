# Connect and verify the agreed research access routes

Parent: [Research and deliver startup idea scout version 2](../map.md)
Labels: wayfinder:task
Type: task
Mode: AFK/HITL
Status: resolved
Assignee: Codex
Blocked by: 04, 08, 11

## Question

Under the user's request to add available APIs, connect the agreed accessible source APIs/supporting routes and demonstrate what each actually retrieves. Which routes are ready for scout use, and which still require credentials, provider approval or a priced subscription choice?

Use the source-selection decision and API inventory. Perform agent-accessible setup and read-only tests; use a precise human checklist only for steps that genuinely require the user. Before paid activation show the concrete service, price, billing/renewal and budget impact; a willingness to consider low charges is not an unspecified purchase instruction. Preserve secrets outside research records. Record available versus configured versus successfully tested status and partial data coverage, with web/browser/user-assisted fallback for gaps.

A provider's refusal or lack of public API does not require an unsupported scraper. Resolve with verified routes and explicit agreed deferrals; leave unresolved mandatory coverage as a real blocker. Update the applicable setup/tool records and pass actual capability limits to the skill-update task.

Use the complete selected-source free/cheap audit, not only HN/Tavily/YouTube/SaaSHub. Prioritize those initial routes while accounting for the remaining selected resources and conditional access. Prefer YouTube for creator retrieval; preserve links and precise requests for user-provided transcripts when needed. Missing Instagram alone is not a completion blocker under the source-selection decision.

## Answer

Resolved 2026-10-29. [Verified research access](../checks/research-access.md) records actual payloads, the complete selected-source reconciliation, failures, fallbacks and optional deferrals. [Sanitized API results](../checks/api-results.json) and the [bounded verification script](../checks/verify-access.py) make the structured checks reviewable.

- HN Ask/Show lists plus a story/comment, GitHub issue/comment, Stack Exchange question/answer and existing Tavily authenticated search/extraction passed. Anonymous Stack Exchange returned quota 300; Tavily reported 108/1,000 included credits used and zero PAYG usage, with immediate counters possibly lagging. Tests stayed within a verified included-credit buffer. No paid service or overage was activated.
- Public samples cover the selected website portfolio, with explicit exceptions/partial results. YC root extraction was empty but individual profiles worked; Indie Hackers stories extraction was mostly navigation and search reported a post-path restriction; G2 timed out. Public SaaSHub alternatives worked, but no project credential or numeric API entitlement was established. Conditional and brief-dependent sources are individually reconciled, not silently omitted or reported as newly tested.
- YouTube Data API remains unconfigured in the checked project locations. Video fetch failed and browser bootstrap failed before navigation. A publisher-hosted Creator Science transcript and substantive creator articles were readable. Preserve these as distinct routes; no arbitrary YouTube caption or full audiovisual access is claimed. Targeted user-transcript requests are recorded for future relevant briefs.
- Optional YouTube/SaaSHub APIs, signup-only access, licensed APIs, paid retrieval and supplementary Instagram are deferred under the user's existing missing-source policy in [Choose source coverage and the India-adaptation route](04-select-source-portfolio.md#answer). No new human decision is invented and no mandatory source remains a blocker to this setup task. A future candidate still needs essential evidence or a provisional assessment.
- Updated [SETUP](../../../SETUP.md) and [research tools](../../../docs/startup-skills/tools.md). Today's Tavily success is direct REST; existing VS Code MCP configuration remains, while MCP/map/crawl verification retains its October 10 date. This chat did not expose Tavily as a native tool. No new client registration is claimed.

Validation: four bounded API routes passed; script syntax, local links and whitespace checks passed; scanned changed records/artifacts for the local credential values and found none. No source accounts, messages, subscriptions or billing settings changed.

Next owner: [Update and verify the agreed scout version 2](07-update-verify-scout.md), now unblocked. Consolidate the existing source catalog and test the accepted workflow with these real access limits. Its ticket carries the connection handoff; the access record includes a ready-to-use prompt. This session resolves only the connection task and does not start the skill-update task.
