Two related output patterns follow. Use the [record guide](../record-guide.md), replace `{{...}}`, and copy only the needed pattern. A completed round preserves its conclusions at that time; the history entry is a short pointer to it.

## Dated round pattern

Save under `opportunities/<stable-name>/rounds/<dated-round-id>.md`.

```markdown
# {{Opportunity name}} — {{Round purpose}}

Recorded: {{date/time and time zone where needed}}
Findings as of: {{assessment date}}
Current proposition then: {{customer, problem, market and offer/version}}
Starting context: {{previous round/run and current records read}}
Round state: {{usable result / waiting for customer evidence / incomplete with blocker}}

## Findings and recommendation at this time

{{Preserve the actual conclusions, important doubts, strongest contrary findings,
recommendation and its reasons. Link stable evidence/results. Do not replace
this snapshot with only a link to the changing current summary.}}

User selection at this time: {{none recorded, or explicit choice/date/reason}}

## What changed and why

{{Prior finding -> current finding, cause and evidence links. Include changed
offer, calculations or tests; preserve disagreements and corrections. Retain
the prior calculation inputs/results and test procedure/interpretation criteria
here or in linked versioned artifacts when updating their current files.}}

## Work performed and limits

{{New research queries/routes and outcomes, supplied results, coverage, access
failures and consequential gaps. Link any existing run log instead of copying it.}}

## Next step and handoff

{{What to investigate/test next, blocker if any, and existing record links.}}
```

## History entry pattern

Append to `opportunities/<stable-name>/history.md`. Use a stable heading/reference for the entry if other records will link to it.

```markdown
## {{Dated unique entry ID}}

{{Date/time}} — {{What changed, why, and whether this is a new finding,
correction, offer revision, or explicit user decision.}}
Basis: {{canonical evidence/result links}}.
Saved output: {{relative link to the dated round}}.
Comparison effect: {{updated affected content / not yet reassessed, with reason}}.
```
