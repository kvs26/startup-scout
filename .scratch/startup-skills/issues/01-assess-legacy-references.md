# Assess what the passive-site references contribute

Parent: [Design the startup skill suite and ship the first scout](../map.md)
Labels: wayfinder:task
Type: task
Mode: AFK
Status: resolved
Assignee: prior-session-review
Blocked by: none

## Question

What do the copied passive-site skills, template, and scripts actually contain, and which useful practices, inherited restrictions, or reliability limitations should inform the new startup skill design?

## Comments

Imported from the completed review in the preceding conversation turn. This preserves prior work in the map's tracker structure; it is not a newly resolved human design decision during charting. Proposed treatments in the review are recommendations, not adopted suite policy. The user's subsequent scope choices are recorded in the map Notes.

## Answer

All six source files in `my_old_resoures/` were reviewed: two skills, their comparison template, and three Python scripts. Their useful contribution is evidence discipline and research tooling patterns. Their opportunity selection and validation rules encode a passive-site strategy and should not become the requirements for the startup suite.

This is a static review, not an implementation or a live source audit. The scripts were not executed; credentials were not inspected; API availability, quotas, program rates, search statistics, and revenue benchmarks quoted in the old files were not independently verified. The compiled Python cache is not an additional source file. Proposed design directions below remain open for the wayfinder discussion.

### What is worth carrying forward

- **Traceable evidence and explicit unknowns.** Claims link to observed sources; calculations expose their inputs; failed searches remain recorded. Preserve the separation between observed facts and judgment. See [Idea Scout](../../../my_old_resoures/idea-scout/SKILL.md), lines 25–31, and [Idea Validate](../../../my_old_resoures/idea-validate/SKILL.md), lines 16–19 and 47–59.
- **More than one route to a hypothesis.** The scout combines complaints with generation from buying moments, datasets, and tool shapes. The transferable practice is generating alternatives and subjecting them to the same evidence standard, not mandating those particular idea shapes. See Idea Scout, lines 49–55.
- **Inspect actual alternatives.** Opening a competing product before asserting a gap is useful. The new design should also consider manual work, services, internal tools, and doing nothing. See Idea Scout, lines 30 and 75.
- **Preserve reasons and history.** Source logs, rejected ideas, canonical idea records, and derived comparison views can help future sessions avoid repeating work. The exact old folder layout is not a requirement. See Idea Scout, lines 107 and 155; Idea Validate, lines 168–195; and the [comparison template](../../../my_old_resoures/idea-validate/comparison-brief-template.md), lines 6–20.
- **Calculate operational effort from its drivers.** Frequency of work multiplied by effort per task is useful input to operating costs. The old fixed upkeep cap is a separate preference that should not transfer. See Idea Validate, lines 42 and 99.
- **Bound investigation.** Discovery and deeper investigation have different costs. A run should be able to stop, expose uncertainty, or produce no convincing candidates instead of satisfying a quota. This is a proposed revision to Idea Scout, lines 8 and 71, and Idea Validate, lines 91–93.

### Old strategy assumptions to leave behind

| Assumption in the old resources | Location | Proposed treatment for the startup suite |
| --- | --- | --- |
| Every idea must combine a curated dataset, interactive computation, many search pages, and ads or affiliates | Idea Scout, lines 14–21 | Design around customer problems and possible business models; do not mandate a product shape. |
| US default, with non-US demand a rejection gate | Idea Scout, lines 10 and 94; Idea Validate, line 12 | Select and record the market per opportunity, including India, the US, or elsewhere. |
| No accounts, databases, backends, paid APIs, or more than roughly three hours of weekly upkeep | Idea Scout, lines 90–91 | Establish founder resources and operating appetite afresh. |
| A purpose-built incumbent serving the hook kills the idea | Idea Scout, lines 75 and 92 | Investigate the target segment, alternatives, switching reasons, and a credible entry point. |
| Ads and affiliates are the eligible monetization routes | Idea Scout, lines 95–99; Idea Validate, line 41 | Consider revenue models suited to the idea, without preselecting one. |
| Search results, AI Overviews, and Keyword Planner control advancement | Idea Validate, lines 39, 87 and 195 | Treat search evidence as relevant only to the claim and channel it actually informs. |
| A fixed four-week evidence window, three-candidate comparison threshold, and passive-site revenue target | Idea Validate, lines 10, 116–121 and 195 | Decide freshness, comparison timing, and economic goals in context. |
| Historical source bans, quotas, and project access failures are permanent policy | Idea Scout, lines 61–69 | Treat these as unverified historical observations; choose sources according to the target customer and current access. |

The supplied files refer to a prior graveyard analysis and a ticket containing earnings research, but those supporting artifacts were not supplied. Their conclusions should not silently acquire authority in this project.

### The main validation problem

The old workflow uses `validated` for a completed dossier without a narrow disqualifying finding. Weak evidence can still advance, while a missing Keyword Planner export prevents advancement. See Idea Validate, lines 18, 176–195. This is a research workflow state; it does not establish that customers want, buy, or continue using the proposed offering.

The startup design therefore needs a decision about which claims are being tested, what evidence each claim needs, and what action the evidence justifies. A researched hypothesis, an interview report, observed behavior, an experiment result, and a paid commitment should remain distinguishable. The suite also needs to allow a negative finding to be well supported.

Other evidence weaknesses to address:

- Different threads are automatically treated as independent evidence, although they may repeat the same people or source story. See Idea Validate, line 47.
- Confidence is introduced as confidence in the evidence, but weak demand forces low confidence even when a negative conclusion might be strongly supported. See Idea Validate, lines 79–87.
- Query phrases and forum complaints do not identify the economic buyer, purchasing authority, ability to reach that buyer, or a purchase commitment. See Idea Scout, lines 45–71, and Idea Validate, line 38.
- Manual data assembly and search page coverage are treated as defensibility without a separate test of customer value or replication economics. See Idea Scout, line 91, and Idea Validate, line 43.
- Re-fetching an old page verifies availability and wording; it does not make the underlying observation recent. The new design should distinguish observation date, publication date, and retrieval date. See Idea Validate, line 28.
- The ban on invented observations is useful, but a startup cost model must be able to show explicitly labeled assumptions, estimates, ranges, and sensitivity. These must not be presented as measurements. See Idea Validate, line 16.

### Script review

#### Autocomplete fanout

[fanout.py](../../../my_old_resoures/scripts/fanout.py) expands seed queries with alphabet suffixes and question prefixes, deduplicates suggestions, and prints them. It uses only Python standard library modules, Google autocomplete, and a local cache.

- Google is fixed to English and the US. Despite the skill's multi-engine fanout description, this script only expands Google queries; the separate suggest adapter queries one engine at a time. See lines 26–28 and Idea Scout, line 45.
- Cache entries have no expiry or retrieval timestamp. Any request exception becomes an empty list that is cached indefinitely. An access failure can therefore look like persistent absence of suggestions. See lines 23–39.
- The documented `--mode alpha` form is not implemented: parsing recognizes `--mode=alpha`; the former treats `alpha` as another seed and uses the default expansion. See lines 4 and 43–48.
- Output discards which seed and request produced each suggestion. Query expansion and deduplication are useful patterns, but this output is a lead list rather than a complete evidence record. See lines 49–61.

#### Pain source fetcher

[pain-fetch.py](../../../my_old_resoures/scripts/pain-fetch.py) provides fourteen adapters for communities, search, reviews, autocomplete, and product listings. It reads optional credentials from the current working directory's `.env`, makes network requests, and caches response bodies. It uses standard library modules and Python syntax requiring a modern interpreter.

- A small adapter interface and central fetch function are useful patterns. The implementation provides no cache expiry, retrieval timestamps, explicit refresh, or consistent structured result status. See lines 46–62 and 386–407.
- Titles and truncated snippets often lose publication dates, precise review/comment links, full context, and query scope. Some review adapters print no individual source URL; the archive adapter requests creation timestamps and then omits them. See lines 96–102, 191–206, 224–250 and 347–364.
- Limited result slices and no pagination mean these are discovery samples. Empty or repeated output cannot establish absence or prevalence of a customer problem. See lines 68, 92, 119, 232 and 240.
- Several adapters assume US geography or storefronts. Geography, language, and source population would need explicit treatment for this user's intended scope. See lines 97 and 145–154.
- Cache identity excludes authentication headers, so responses may be reused across different access contexts. Authenticated GitHub search bodies can include nonpublic material and are saved locally. See lines 47–61 and 86–93.
- Error handling varies by adapter; markup changes can appear as no results. Google Play uses an undocumented protocol; Product Hunt is marked unverified in its own exception comment. These are static code observations, not claims about whether the services work today. See lines 77–83, 192–209, 216–221 and 279.
- `.env` parsing is a simple split, and there is no copied `.gitignore` establishing the credential protection claimed by the skills. The cache and configuration paths depend on the working directory. See lines 34–43.

#### Keyword Planner report

[planner-report.py](../../../my_old_resoures/scripts/planner-report.py) reads a local UTF-16, tab-separated export with two preamble rows and English column names. It prints a normalized table with currency, bids, and search metrics. It has no network or write operations.

- Normalizing a difficult export and preserving original currency are useful techniques. See lines 36–46 and 68.
- It always describes search values as order-of-magnitude buckets without detecting that property, groups blank metrics under “Zero/no-data,” and prompts conversion to USD. A new resource should preserve measurement definitions, missing values, ranges, and the idea's chosen currencies explicitly. See lines 54–59 and 68–80.
- This should only inspire optional search-channel tooling if later decisions justify it. It should not become a prerequisite for assessing every startup idea.

The historical `scripts/...` commands in the skills are not runnable at the current repository root as written: the copied files are under `my_old_resoures/scripts/`. Neither fetched-source caches nor the old pipeline records were supplied. The comparison template is still labeled as a prototype draft.

### Questions the map should examine

These are proposed decision areas, not an agreed skill inventory or implementation backlog:

1. What founder outcomes, capabilities, time, capital, and operating preferences should shape opportunity selection, and which should be configurable per run?
2. How should scouting connect a problem to a customer, user, buyer, existing workaround, and first market without assuming that public search demand is the opportunity?
3. What evidence and experiment outcomes justify investigating further, testing with customers, changing direction, pausing, or stopping?
4. How should the suite analyze alternatives, differentiation, pricing, revenue models, delivery costs, acquisition costs, cash needs, and uncertainty?
5. What should customer research, positioning, marketing, sales, onboarding, retention, and operating feasibility contribute before infrastructure and acquisition execution begin?
6. Which responsibilities deserve separate skills, which share resources, and how do evidence, assumptions, decisions, and next actions pass between them?
7. Which tool integrations and scripts are justified after those responsibilities are clear, and how will the new skills be evaluated on contrasting examples?

The [map](../map.md) preserves the confirmed scope and future-map intentions. This review does not resolve the startup skill architecture or validation policy.
