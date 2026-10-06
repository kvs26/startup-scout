# Guide and verify the selected tool setup

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:task
Type: task
Mode: HITL
Status: claimed
Assignee: Codex
Blocked by: 08

## Question

Can the user complete the setup needed by the scout, investigator, and customer-connect skill, with clear manual guidance, agent execution of individual steps when requested, and a very short root-level record of what is ready and why it is needed?

This task was explicitly requested on 2026-10-03. It prepares the tools selected in [Agree the startup skill suite blueprint](08-decide-suite-blueprint.md) before the three skill build tasks. The research shortlist is input to that selection, not a list of everything to install. This is setup for the startup skill suite, not infrastructure for a chosen startup.

## Working approach

The selected/conditional setup is specified in the [resolved blueprint](08-decide-suite-blueprint.md#sources-tools-and-setup-handoff). Verify existing search/page/file tools, connect Tavily, and check and add Hunter/Apollo capabilities when available free. Tavily account creation is user-reported; credentials, connection, and actual capabilities remain unverified. For Hunter/Apollo, check the actual account's free eligibility, API/MCP access, included credits, lookup versus enrichment permissions, and limits before enabling a capability. A free website account is not proof of free access to every API endpoint. Do not enable paid plans, paid overages, or purchase credits under this instruction. If a needed Hunter/Apollo feature is paid-only or unavailable, record the limit and defer that part while retaining public-source fallbacks; this conditional deferral does not block the required skills. Tavily connection/checks remain required.

Use current official integrations where usable. Verify a small relevant free retrieval/contact task, recording the difference between connection success, quality, and market coverage; no market or industry is the default. Do not activate sending/campaign features. Record unsupported actions, quota exhaustion, or inconclusive contact verification honestly. Any small adapter required for a selected capability must be justified and checked, rather than silently adding an unrelated integration.

1. Read the agreed blueprint and inspect the existing setup. Identify the tools, accounts, API connections, MCP servers, and local dependencies actually needed. Reuse working installations. Explain each item's purpose in a short sentence, which skill uses it, whether it is required or optional, and any account or cost requirements. Check current official setup instructions before giving commands.
2. Guide the user manually by default, one manageable step at a time. Give the exact command or dashboard action, where to perform it, and what success should look like. Wait for the user's result before continuing to a dependent step; troubleshoot failures and save progress in this ticket so another session can resume.
3. For each item, allow the user to say “do this for me.” That request delegates the named step to the agent: execute it where tools and permissions allow, verify the result, and continue without asking for the same authorization again. Delegating one step does not switch all later steps to automatic execution. If a login, verification, or other action requires the human, explain the remaining action precisely and resume after it is complete. Use the wizard skill when human-only setup steps benefit from its guided workflow; respect the user's manual-first preference for the other steps.
4. Configure credentials through the appropriate local or provider mechanism. Record configuration locations and variable names where useful, never secret values in this ticket, chat output, or the final summary. Identify any paid prerequisite before the user takes that step; this ticket does not itself authorize purchases.
5. Verify each required tool with a small real check from the environment that will run the skills: for example, confirm the server connects and retrieves a public page. Installing a package alone does not establish a working connection. Record success, failure, or any human-reported result that the agent could not independently check. Leave required setup open while it is still missing or failing; optional items may be explicitly deferred with a reason.
6. Finally create `SETUP.md` in the repository root. Keep it very short: a brief overview and one compact table with **Tool or service**, **Setup/location**, **Why we use it**, and **Status/check date**. Include installed/configured items and existing tools being reused, distinguishing them clearly. Briefly mention any deferred optional item that affects use. Link back to this ticket for detailed steps and checks instead of copying the setup diary. If the blueprint needs no additional installation, record the verified existing tools and that outcome honestly.

## Completion criteria

- Required setup chosen in the blueprint is complete and checked; optional deferrals and remaining limitations are explicit.
- The user was guided manually unless they delegated a particular step, and completed steps and check results are saved under this ticket's comments/answer.
- Root-level `SETUP.md` accurately and briefly explains the actual setup, what was installed or reused, and the reason for each item, without secrets.
- The scout, investigator, and customer-connect build tasks can use the prepared tools. Their later behavioral checks still belong to those build tasks; update the summary if implementation changes the actual setup.

## Comments

### 2026-10-03 — User-requested setup workflow

The user requested a separate ticket for manual setup guidance, with the option to ask the agent to perform each individual step, followed by a very short file in the repository root explaining the setup, installed tools, and reasons. Creating this ticket does not begin installation or select tools on the user's behalf.

### 2026-10-03 — Blueprint resolved; setup handoff received

The user reported creating a Tavily account and instructed completion of the blueprint. They also requested Hunter and Apollo if free, with access checks and setup handled here. The blueprint is resolved, so this task is now unblocked. No credentials or connections have been verified, and no setup steps have been executed by closing the blueprint. The manual-first and per-step delegation rules still apply.

### 2026-10-06 — Read-only setup observations during the scout build

The user requested work on [Build and verify startup idea scout](10-build-startup-idea-scout.md). Existing local file tools work, and an independent scout check has retrieved public sources using the existing web tools. Tavily is not exposed in the current session, does not appear among the inspected Codex MCP configuration names, and `TAVILY_API_KEY` is absent from the process environment. This does not rule out credentials or setup elsewhere; no secret values were printed. No service was installed, account connected, credential changed, or contact lookup performed.

A short [SETUP.md](../../../SETUP.md) records these actual partial checks and remaining gaps. Tavily setup remains required under the blueprint unless the user changes that choice. Hunter/Apollo account-specific free capabilities remain unverified. This observation does not resolve the setup ticket or replace its manual-first workflow.

### 2026-10-06 — Tavily deferred; scout completion authorized

The user explicitly instructed leaving Tavily for later, recording it as one line in root [TODO.md](../../../TODO.md), and finishing [Build and verify startup idea scout](10-build-startup-idea-scout.md#answer). Tavily therefore no longer blocks that build. It remains unconnected and unverified; the scout uses its tested existing web tools. This setup ticket stays open for the remaining work, with the manual-first workflow preserved.

### 2026-10-06 — Setup resumed; baseline and available connections checked

Claimed by Codex at the user's request. Preserve the existing Tavily deferral and manual-first workflow. A background research agent is checking current official Hunter/Apollo setup, free capabilities, and limits; published plan descriptions do not verify the user's accounts.

- Existing web search returned results and page reading retrieved [YC Requests for Startups](https://www.ycombinator.com/rfs) in this session. Local reads and the ticket claim write succeeded. This verifies basic retrieval and file access, not broad crawling or contact coverage.
- Read-only local inspection found `codex`, `node`, `npm`, `npx`, and `python3` available. The inspected `~/.codex/config.toml` lists only `computer-use` and `node_repl`; no project `.codex/config.toml` exists. `TAVILY_API_KEY`, `HUNTER_API_KEY`, and `APOLLO_API_KEY` are absent from the current process environment. Other credential locations were not searched; secret values were not printed.
- The plugin directory lists Hunter and Apollo.io, both uninstalled with `DISABLED_BY_ADMIN` and `NOT_AVAILABLE`. Neither can be connected through this app's plugin route under the current policy. No attempt was made to bypass the restriction. The Hunter listing describes company-level discovery/enrichment, not personal contact lookup; listing presence is not evidence of usable email-finding capability.
- Asked the user whether they already have Hunter and/or Apollo accounts. Their answer is needed to choose the first manual account step. No account was created, credential configured, provider lookup run, or sending feature enabled.

The ticket remains claimed and unresolved. Next: use the user's account status and official documentation to guide one manageable account check; distinguish any website-only use from a verified agent connection. Tavily remains in [TODO.md](../../../TODO.md).

### 2026-10-06 — Official free-access research saved; waiting for account status

The research subagent saved [current contact-tool setup findings](../checks/contact-tool-setup-research.md), including official sources and exact account/dashboard routes. Hunter documents Free API/MCP access with a shared monthly allowance; Apollo documents endpoint-specific free eligibility, including a work-email prerequisite for relevant search/enrichment, with inconsistencies between general pricing and endpoint documentation. The findings distinguish no-credit people search from credit-consuming contact retrieval/enrichment, and Hunter lookup enrichment from paid saved-Lead enrichment.

These are published provider capabilities, not verified account entitlements. Neither provider connection nor a live contact sample has been checked. The in-app connector restriction remains in effect; alternate technical routes in the research are not instructions to bypass it. [SETUP.md](../../../SETUP.md) now records the observed connection restriction and pending account checks.

**Pending user input:** whether accounts already exist for Hunter, Apollo, both, or neither. No answer has been received at this checkpoint. After the answer, guide the first applicable account check and request only nonsecret plan/credit information (and work-versus-personal registration type for Apollo). Do not request keys in chat. Preserve one-step manual guidance and per-step delegation. Do not mark setup resolved on the basis of documentation alone.

### 2026-10-06 — No contact-service accounts yet; Hunter signup step

The user reports having neither Hunter nor Apollo. Rechecked Hunter's [official signup](https://hunter.io/users/sign_up) and [Free-plan details](https://help.hunter.io/en/articles/11060999-what-s-included-in-hunter-s-free-plan): the published Free plan includes 50 credits/month and API access without a credit card. Signup offers Google sign-in or a work-email field. Actual signup eligibility and account allowance remain unverified.

First manual step provided: create a free Hunter account, complete email verification if requested, and report the displayed plan name and remaining credits. Skip mailbox/campaign setup and paid offers. If signup refuses the user's email or requires payment, report the message before continuing. Awaiting completion; Apollo signup, credentials, integration access, and live lookup checks have not begun. The existing in-app connection restriction still applies; account creation alone will not verify an agent connection.
