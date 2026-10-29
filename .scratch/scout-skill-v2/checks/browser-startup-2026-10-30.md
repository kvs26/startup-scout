# Browser startup diagnosis — 2026-10-30

Status: partially repaired. The official package refresh removed the blocked
`node:process` import. This session still lacks the trusted desktop browser
service, so no browser page was opened. This records the user's request to fix
startup, separately from the completed scout instruction changes.

## Initial reproduction and findings

The originally installed entry point failed even when imported alone:

```js
await import("/Users/i42492/.codex/plugins/cache/openai-bundled/browser/26.727.51351/scripts/browser-client.mjs");
```

Observed error: `Importing module "node:process" is not allowed in node_repl`.
This happens before setup, browser selection or navigation. It says nothing
about YouTube or Instagram access, authentication or bot detection.

Three hypotheses were checked: an incompatible browser bundle, a stale installed
bundle, and session state. The first two have concrete evidence; resetting the
JavaScript session did not supply the missing browser service.

| Component | Observed state |
| --- | --- |
| Cached Browser and Chrome | Both version `26.727.51351`; identical 1,016,127-byte entry points containing one static `node:process` import. |
| Cached entry-point hash | `f204d340535055781952b10ed396de20b842f00a19e430852f7e121ad1ce91f6` (SHA-256). |
| Installed desktop app | `/Applications/ChatGPT.app`, version `26.1013.40934`, build `20770`. |
| Official app-bundled Browser and Chrome | Version `26.1013.40934`; identical 169,663-byte entry points, without a `node:process` import. |
| Official entry-point hash | `78f5a38ab02f23b68e4650e3bfe9ec2f269c5e004f30a1f59eee927a221a2e2f` (SHA-256). |
| Configured bundled marketplace before desktop launch | Pointed to `~/.codex/.tmp/bundled-marketplaces/openai-bundled`, whose Browser package was the older version. |
| Configured Node MCP command | `/Applications/ChatGPT.app/Contents/Resources/cua_node/bin/node_repl`; no command arguments. A standalone executable registration does not prove that a desktop browser service is attached. |
| Local CLI | `codex-cli 0.162.1`. |

## Repair attempts and exact outcomes

1. A narrow compatibility experiment replaced the old bundle's single
   `import{env as ly}from"node:process";` with `const ly=processShim.env;`.
   The bundle already supplied that empty-environment shim. No process access,
   module allowlist, trust setting or sandbox permission was added.
2. The import error disappeared, but setup then failed with
   `privileged native pipe bridge is not available; browser-client is not trusted`.
   This does **not** establish that the edit caused the trust failure: the
   original import failed before reaching that stage. The experiment was
   reverted byte-for-byte and the original hash verified. The unsuccessful
   patch utility was removed. Backup: `/private/tmp/scout-browser-runtime-repair-20261030/browser-browser-client.mjs`.
3. Tried the supported marketplace command to use the app's official bundled
   marketplace. It refused with `marketplace 'openai-bundled' is reserved and
   cannot be added from this source`. No marketplace/configuration change was
   made. This was a CLI validation failure, **not** an automatic approval rejection.
4. Read the newer official Browser skill and tested its documented bootstrap
   against the unmodified official app entry point in a fresh JavaScript session:

   ```js
   const { setupBrowserRuntime } = await import("/Applications/ChatGPT.app/Contents/Resources/plugins/openai-bundled/plugins/browser/scripts/browser-client.mjs");
   const agent = await setupBrowserRuntime();
   ```

   Observed error: `Browser use requires a trusted Node REPL browser service`.
5. `codex doctor --summary` reported the desktop app was not running. Opened the
   installed desktop app and this workspace using `codex app <workspace>`;
   that launch command succeeded. Reset the JavaScript session and repeated the
   official bootstrap: the same missing-service error remained. Opening the
   app alone did not attach its service to the existing tool session.
6. After the desktop app finished starting, it automatically refreshed the
   bundled marketplace and both installed plugins to `26.1013.40934`, removing
   the older cached version. Browser, Chrome and Chrome's `latest` alias now
   all have the exact official entry-point hash above. Both plugins remain
   enabled. No manual marketplace override or source patch remains.
7. Retested the installed refreshed Browser entry point at
   `~/.codex/plugins/cache/openai-bundled/browser/26.1013.40934/scripts/browser-client.mjs`.
   Import succeeded: the `node:process` failure is gone. Calling its documented
   `setupBrowserRuntime()` still returned
   `Browser use requires a trusted Node REPL browser service`.

The official Browser/Chrome package refresh is verified. A working browser
connection, page navigation, transcript retrieval and audiovisual inspection
remain unverified. No trust check was disabled or impersonated. No paid
provider was connected.

## Remaining supported step

The user subsequently confirmed this conversation runs in the **Codex VS Code
extension**. That explains why launching the desktop app did not attach its
native browser service to the existing IDE conversation.
The [official Browser documentation](https://learn.chatgpt.com/docs/browser)
states that the built-in browser requires the desktop app and is unavailable
in Codex CLI/IDE. The [official browser-extension troubleshooting](https://learn.chatgpt.com/docs/chrome-extension)
also recommends a new desktop chat to clear chat-specific connection state,
and checking Settings → Computer Use for the browser connection.

For native browser verification, continue in a fresh Codex chat in the desktop
app already opened. If its native Browser integration still fails, use `/feedback`
with these exact errors and versions. Do not assume that manually launching its
Node MCP executable supplies the native service.

The IDE remains usable for coding and hosted web search. The [official web
search documentation](https://learn.chatgpt.com/docs/web-search) explicitly
supports searching in the IDE and distinguishes hosted search from local
command networking. Earlier web-search results did not depend on browser
startup and did not establish that videos or Instagram pages were inspected.

Suggested continuation prompt:

> Continue the browser startup repair from
> `.scratch/scout-skill-v2/checks/browser-startup-2026-10-30.md`.
> Use the desktop app's native Browser integration. First verify startup, then
> open YouTube and the supplied Instagram reel and report exactly what loads.

Verification targets: `https://www.youtube.com/watch?v=9wsAINkaGjo` and
`https://www.instagram.com/reel/De9SZVFyqvZ/`. A loaded page alone does not count
as reading a transcript or inspecting video/audio. Any sign-in or content
access blocker must be reported before source-dependent scouting resumes.
