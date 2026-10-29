# Research usable YouTube and Instagram access for scouting

Parent: [Research and deliver startup idea scout version 2](../map.md)
Labels: wayfinder:research
Type: research
Mode: AFK
Status: resolved
Assignee: Codex research agent
Blocked by: none

## Question

Which official APIs, available connectors, browser routes and third-party retrieval services can actually support discovery and inspection of YouTube videos and Instagram posts, carousels and reels? Distinguish metadata, transcripts, visual/audio content, comments and trend evidence; document what is verified here, what requires setup or payment, and how to handle failures without concealing missing coverage.

## Comments

- 2026-10-30: Research authorized by the user. Existing ₹1,000/month paid-API planning cap is context, not a purchase authorization. Coordinator checks the available plugin directory and browser routes; research agent checks primary documentation and records facts in an isolated research branch. Do not install, subscribe, export browser cookies or claim untested integrations work.

## Answer

Resolved 2026-10-30 as an access investigation, not a completed connection. [Primary-source research](../youtube-instagram-access-research.md) compares official APIs, native transcripts, Apify, Supadata and the open-source transcript fallback. [Runtime checks](../checks/creator-access-2026-10-30.md) record actual plugin discovery, browser bootstrap and exact supplied-link failures.

- YouTube's official API supports discovery/metadata/comments; caption download requires video-edit permission. Speech and relevant visuals require separate inspection. Meta's professional-account APIs do not supply unrestricted public personal-account research.
- Recommend a bounded free pilot: Apify's maintained Instagram actor for discovery/carousel media, Supadata for YouTube/Instagram transcripts, plus inspection of the relevant visual material. Both document hosted MCP connections. Published free allowances are $5/month and 100 credits/month respectively; actor add-ons and generated transcript lengths affect usage. No provider was connected or successfully tested here, and no paid plan was selected.
- The plugin directory returned a directly relevant vidIQ listing, but it is disabled by the workspace administrator and unavailable to install here. Supadata/Apify directory search returned no entries; that does not rule out their documented custom MCP routes or other directory results.
- Browser bootstrap failed before navigation. The user's original Buildercult carousel and new reel both failed direct fetching. Neither was freshly inspected. No automatic end-to-end route is verified in this session.

Research isolation: disposable clone `/private/tmp/scout-youtube-instagram-research-20261030`, branch `research/youtube-instagram-access`, commit `95539866844de337eb54f944d36df58145faf0fd`. Only the single research artifact was committed there and copied into this checkout by the coordinator; the main checkout was not switched or committed.

The maintained catalog and setup status now distinguish documented, unavailable and runtime-tested routes. The companion instruction correction consumes the findings. Next owner for optional connection work: user supplies an available account connection, then the agent runs the bounded pilot against the actual supplied links and verifies identity, dates, modalities, omissions and usage before source-dependent scouting. Existing source access remains a real limitation, not a resolved reliability claim.
