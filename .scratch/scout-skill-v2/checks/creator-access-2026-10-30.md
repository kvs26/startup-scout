# YouTube and Instagram runtime access checks

Date: 2026-10-30. Supports [Research usable YouTube and Instagram access for scouting](../issues/14-research-youtube-instagram-access.md). These checks concern retrieval capability, not a new scouting campaign. The [primary-source research](../youtube-instagram-access-research.md) owns provider documentation and cost findings; this file records what happened in this environment.

## Available connectors

- Queried the available/deferred tool registry for YouTube and Instagram: no provider-specific content tool was exposed.
- Queried the plugin directory for `YouTube Instagram`. It returned vidIQ, Metricool, Canva and Windsor.ai, all with `DISABLED_BY_ADMIN`, `NOT_AVAILABLE` and `installed: false`. vidIQ was the directly relevant candidate: its directory description advertises YouTube/Instagram/TikTok outlier discovery, YouTube transcripts and video/Shorts/Reel visual analysis. These are advertised capabilities, not tested results. Its returned ID was `plugin_asdk_app_69dd11f3e50c8191b1ca48d03cf7e2ad`.
- No installation suggestion or activation was attempted because the relevant result was unavailable under workspace policy. That is a directory availability status, not an automatic tool-approval rejection.
- A separate directory query for `Supadata Apify` returned no plugins. The directory is not exhaustive; [other plugins may exist](https://chatgpt.com/plugins). Their vendor-documented hosted MCP routes require separate setup; no connected tool was found or used here.

## Browser route

Read and followed the available Browser skill. Attempted the supported browser-client bootstrap, intending to inspect an Instagram reference. It failed before browser selection/navigation with: `Importing module "node:process" is not allowed in node_repl`.

No page, transcript UI, media, signed-in state or browser session was inspected. The failure does not establish whether the user is signed in or whether Instagram would permit access in a working browser. No alternative browser automation, cookie export or authentication bypass was attempted. The same bootstrap limitation had been recorded on October 29.

Later repair attempt: [startup diagnosis and exact results](browser-startup-2026-10-30.md) found an older cached package and a missing trusted browser service. A local compatibility experiment was reverted. Opening the desktop app automatically refreshed both Browser and Chrome to the newer official bundle, removing the blocked import. Setup still reports a missing trusted browser service in this session; creator-page access remains unverified.

## Direct web reads

| Exact target | Observed result | Content inspected |
| --- | --- | --- |
| [Buildercult supplied carousel](https://www.instagram.com/p/DeZi486k5vV/?img_index=8) | Cache miss / failed fetch | None; earlier notes in the lead notebook are historical evidence only. |
| [New supplied reel](https://www.instagram.com/reel/De9SZVFyqvZ/) | Cache miss / failed fetch | None; speech, frames, author and date remain unverified here. |
| [Other campaign's supplied carousel](https://www.instagram.com/p/DebW3bIm0Kh/) | Cache miss / failed fetch | None. |
| [YouTube sample from the maintained catalog](https://www.youtube.com/watch?v=9wsAINkaGjo) | Fetch error | None; no transcript or audiovisual inspection. |

The first two links were recovered from the existing fresh-discovery record, matching the user's quoted failure. The other carousel was checked before identifying the exact originating run. No contents or current trends were inferred from failed links. Existing campaign records were read for context, not rewritten or retrospectively upgraded.

## Practical result

No automated end-to-end route for the required YouTube/Instagram content was established in this session. Provider research identifies testable candidates, not a solved connection. The maintained [creator access routes](../../../docs/startup-skills/source-catalog.md#creator-access-routes) carries this distinction into the scout.

Next concrete capability check: use an available, connected free provider or repaired browser to retrieve one relevant YouTube item's speech/visuals, the supplied carousel's needed slides/caption and the supplied Reel's speech/visuals. Check identity, publication date, omissions, cost/allowance and actual inspectability. A failed pilot leaves source-dependent scouting paused until the user supplies material or changes scope. This session requested instruction repair and access research; it did not authorize account creation, payment or a new idea campaign.
