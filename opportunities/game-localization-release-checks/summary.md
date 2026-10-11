# Game localization release checks

We would sell small game studios a tool for checking translated screens before they release an update. Localization means adapting a game for another language. Even when a translation is correct, its text can be too long for a button, overlap another label or use characters the game's font cannot display.

The proposed tool would capture chosen screens in different languages and screen sizes, then compare them with earlier versions the team approved. A person would review the differences and decide which ones need fixing.

## An example

**Imagined example:** A studio updates its game menu. A translated button label no longer fits on a small phone screen.

1. The team configures which menu to open, which languages to check and which screen sizes to capture.
2. The tool captures those screens from the new game version and compares them with the approved earlier screenshots.
3. The reviewer sees the old and new screen together, identifies the cut-off label and passes the finding to a developer.

The team still needs people to judge translation quality. This example describes the proposed workflow; no working tool or studio trial has been completed.

## Who would pay, and for what?

A studio owner or person responsible for releases could pay for a tool license, with setup and support. Another possible offer is a fee for checking one agreed release on the studio's behalf. The model, price, payment terms and buyer's authority remain unconfirmed ([proposed offers](research.md#c003)).

## What the research tells us

Two small game projects describe problems with translated layouts, fonts and integrating translations. One also reports a tight budget and disappointing results from adding languages. These accounts support a real task, without proving that a studio would pay for our offer ([problem accounts](research.md#c001)).

Existing tools substantially weaken the general idea. LocaDiff and an Unreal game-engine plugin already advertise similar screenshot checks. Unity has testing support, and Gridly and human testers offer other ways to handle parts of the work. We have not found a valuable gap for a particular studio ([existing alternatives](research.md#c002)).

## What delivering it would take

We would have to choose an initial game engine and platform, obtain appropriate access to game versions and configure repeatable screen captures. Animations and other expected changes can create distracting differences. Maintaining compatibility, covering devices and providing support would create continuing work.

Development, devices, storage and specialist language review are unpriced ([delivery and costs](research.md#c003)). Game-development communities offer places to look for teams, but no suitable paying studio is known ([customer access](research.md#c004)).

## The next useful check

The existing recommendation puts this third among the three newer ideas and advises postponing a general build. Reconsider it with a reachable studio whose release process has a consequential problem that available tools do not handle well.

The key question is: **which repeated defect would that studio pay a new provider to catch?**

## Record details

- Folder identity: game-localization-release-checks
- Research assessed: 2026-10-11. Wording revised: 2026-10-11.
- Status: Initial research completed; the general offer faces close competition.
- Initial game engine, platform and country: Undecided.
- Your decision: No idea selected.

[Research](research.md) · [History](history.md) · [Comparison](../comparison.md) · [Scouting run](../../scouting-runs/2026-10-11-creative-consumer-discovery.md)
