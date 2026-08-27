---
name: echo-product-manager-power
description: Turn verified customer, market, operational, and business evidence into measurable ECHO product outcomes, experiments, priorities, requirements, and feedback loops. Use for Claude auto or Codex cauto Product Manager sessions, discovery, PRDs, KPI trees, roadmaps, prioritization, beta analysis, pricing inputs, and post-release outcome reviews.
---

# ECHO Product Manager Power

Self-contained compiled power skill for the `product-manager` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

## Base

Shared fleet base (proofline verification, risk/action review, grounding) is inlined below from `echo-fleet-base`.

### echo-proofline-verification

# Echo Proofline Verification

Verify the latest route matrix:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoOpsEvidence.ps1"
```

## Required proof

A route recovery passes only when:

- Local passes equal local expected.
- Public passes equal public expected.
- Every local and public response identity matches.
- Distinct Cloudflare Ray IDs cover the public requests.
- `OverallPass` is true.

The verifier writes a SHA-256-bound proof JSON. A single HTTP 200 is not proof. A tunnel connection is not proof. A service state is not proof. The claim and its supporting artifact must agree.

For broader delivery claims, use `echo-delivery-evidence`.

### echo-risk-action-review

# Echo Risk Action Review

Every mutation plan must state:

```text
hypothesis
evidence
falsification_condition
exact_action
affected_resources
rollback
expected_local_result
expected_public_result
stop_condition
action_id
```

Mutating plans additionally require:

```text
confirmation_token
expected_current_state
idempotency_key
```

Run:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoOpsRiskGate.ps1" `
  -PlanPath "C:\path\mutation-plan.json"
```

The gate rejects arbitrary `command`, `shell`, `cmd`, or `ScriptBlock` fields. A passing review authorizes only the declared action ID; it does not authorize adjacent work.

## Grounding

- Prefer live system state (SDK invoke, service health, queue, git) over memory or conjecture.
- Separate facts, inferences, and open questions explicitly.
- Never treat a role label as an authorization grant; stay inside the scoped broker token.
- Fail closed on destructive or high-impact actions unless the approval gate clears them.
- Persist material decisions with attribution; leave a verification trail for the next operator.


## Method

Role-specific composed skills (capped at 5, base refs stripped):
- `data-analytics:gather-business-context`
- `data-analytics:product-business-analysis`
- `data-analytics:design-kpis`
- `data-analytics:market-sizing`
- `doc-coauthoring`

### Method component: data-analytics:gather-business-context

## Boundary

Use this skill to gather framing context, not to complete the downstream analysis.

If the same request also asks for a diagnosis, recommendation, dashboard, report, or other analytical deliverable, return only the context needed for that next step and continue with the appropriate focused skill, such as `metric-diagnostics`, `product-business-analysis`, `build-dashboard`, or `build-report`.

# Gather Business Context

Use this skill to collect the business context needed to understand an analytical question before doing deeper work. Focus on what the topic is, why it matters, what changed or is being decided, who or what source is closest to the work, and which definitions or artifacts should frame the analysis. This is a retrieval and extraction skill: gather enough context to set up the next step, not a final report, root-cause analysis, or broad background scan. Skip it when the prompt already provides the needed context or the task is fully self-contained.

## Workflow

### 1. Identify The Retrieval Target

Establish the analytical topic that needs context and why it matters for the next step. Capture the boundary needed to search and interpret sources, such as the relevant product area, audience, time period, or decision. If the timeframe is missing, use the narrowest reasonable window implied by the task and label it as an assumption.

### 2. Build Search Anchors

Search with concrete identifiers rather than broad topic guesses. Start with the names the user provided or the sources surfaced, then expand with adjacent terms that help recall, such as aliases, owners, teams, dates, source names, related entities, or entities found in earlier results.

Start broad enough to avoid missing relevant context. If too much comes back and a quick scan suggests the results are mostly unrelated, combine anchors to narrow retrieval, for example a metric plus a dashboard name, a feature plus a launch window, or a customer plus the relevant workflow. If a likely source comes back thin, revise the anchors before treating the source as missing.

### 3. Search From Discovery Points Toward Authoritative Artifacts

1. **Explore all possible sources.** Search every enabled or provided source family that could contain useful context or task-relevant data. Within each structured-data source, run fresh catalog or metadata discovery for relevant schemas, datasets, tables, views, models, and metrics. User-named sources, known tables, dashboards, and semantic-layer anchors are starting points, not stopping points.
2. **Compare duplicates and conflicts.** When sources overlap or disagree, compare authority, freshness, definition, scope, and directness. Prefer artifacts closest to what was decided, defined, implemented, or measured; follow linked evidence when useful. Note material conflicts and explain which source or combination should guide downstream analysis.

### 4. Extract Only Decision-Shaping Context

Treat business context as a fixed extraction target, not an open-ended summary. Capture the facts that will shape the downstream analysis: the topic's business meaning, why it matters now, how it is defined or measured, where to verify it, what recently changed, and what uncertainty should travel with the analysis. Examples can include a metric definition, current rollout state, dashboard link, owner note, source conflict, or stated next step.

Keep the context note focused on details that help frame the next analysis. Skip broad background, adjacent history, or long source excerpts unless they add useful context.

### 5. Keep Source Notes Compact And Attributable

For each useful source, record enough attribution for the downstream work to be checked later: when the source applies, what kind of source it is, what factual context it established, and any important caveat or conflict. Distinguish source facts from inference and do not imply source review, stakeholder views, metric certainty, or confidence beyond what was actually established.

### 6. Reconcile Conflicts Explicitly

When sources disagree in a way that could change the downstream framing, preserve the disagreement instead of smoothing it over. Prefer the newest explicit decision artifact over older plans, owner-written docs over third-party summaries, and implementation artifacts over aspirational plans when the question is what is live, shipped, logged, or queryable now. Treat an informal source as stronger than a canonical artifact only when it clearly records a later decision or owner confirmation.

If disagreement remains, present both views, label the conflict, and state what source or owner would resolve it. If context is stale or incomplete, say what is missing and where to look next.

### 7. Stop Once The Framing Is Sound

Stop gathering context when the downstream task can be framed well enough to proceed and the likely enabled or provided source families have been checked, ruled out as unavailable, or identified as too thin. Before stopping, make sure the next step has a clear enough understanding of the topic, why it matters, where the important definitions came from, what recent context applies, and what gaps remain.

Continue searching when a relevant enabled or provided source is likely to add useful context. If an expected source was not found, name that as a gap rather than implying it does not exist.

### 8. Return A Lightweight Context Note When Useful

Prefer a focused context note over a full report or raw retrieval dump. Include enough context for the next analysis to proceed without redoing the search: a short summary, the relevant context, important definitions or source links, uncertainty or caveats, and citations. Keep it readable, but do not compress away details that explain the framing or source quality.

If the user asked only for quick orientation, shorten the structure while preserving citations, conflicts, and missing canonical artifacts.

## Standards

Judge sources by what they can actually establish. Informal discussion can be useful for discovery and recent context, but durable artifacts are usually stronger evidence for definitions, decisions, status, and measured results once found. Prefer sources close to the work, recent enough to reflect current reality, and explicit about what they establish. Surface missing source-of-truth artifacts as context gaps.

Keep important claims attributable. Treat a source as useful only when it clarifies how the downstream task should be framed or interpreted; sources that merely mention the topic are incidental. Preserve enough evidence to check the work later, and label interpretation, assumptions, conflicts, and uncertainty when support is thin, stale, indirect, or conflicting.

Preserve disagreements that could change the framing. Prefer owner-authored or decision-adjacent material and evidence of what is current over secondhand summaries or speculation. Do not infer consensus from silence. Say what source or owner would resolve an important conflict.

### Method component: data-analytics:product-business-analysis

## Related Skills

Use `metric-diagnostics` when the recommendation depends on explaining a metric movement, anomaly, gap, or discrepancy.

# Product And Business Analysis

Use this skill to answer product or business questions with data-backed evidence, context, and a recommendation. Give the audience enough trustworthy evidence, interpretation, and uncertainty framing to choose a practical next action.

## Skill Configuration

### Source Discovery And Verification

Use the relevant semantic layer as a starting map, not a boundary.

1. **Explore all possible sources.** Search every connected or provided source that could contain task-relevant data or change the interpretation. Within each structured-data source, run fresh catalog or metadata discovery for relevant schemas, datasets, tables, views, models, and metrics. Known sources, tables, dashboards, and semantic mappings are starting points, not stopping points.
2. **Compare duplicates and conflicts.** When sources overlap or disagree, compare ownership, freshness, definition, grain, coverage, and directness. Use the best authoritative source, or combine complementary sources when needed. Note material conflicts, explain why the selected source or sources control the answer, and verify selected data through live reads before concluding.

### Source Access Guardrail

Before querying sources, building artifacts, or drawing conclusions, determine whether the answer requires a specific source of truth.

If a required source is unavailable, stop that path. Tell the user what source is needed, ask them to make it available or provide a reviewed fallback, and do not treat weaker substitutes as equivalent.

If the missing source is only optional enrichment, continue with the strongest available evidence and label the gap when it materially affects the answer.

Clarify with the user when a missing input would materially change the analytical frame or recommendation. Otherwise make a reasonable assumption, state it, and proceed.

## Workflow

### 1. Start From The Decision

Identify the decision, audience, and action the analysis should inform before choosing data sources or metrics.

State plainly:

- the question and decision the analysis should inform
- who will use the answer and what they can act on
- the scope and comparison that define a useful answer
- the outcome or behavior that matters for the decision
- any assumptions needed to proceed

Do not let unclear scope turn into broad exploratory work by default.

### 2. Gather Decision-Relevant Context

Run `gather-business-context` before deeper analysis. That skill owns source selection, retrieval, source authority, conflict handling, and compact context notes. Use this workflow to decide how the gathered context changes the analysis and recommendation.

Keep the context pass proportional to the task. For self-contained prompts or cases where the user already provided enough context, the pass can be brief: confirm the decision frame, definitions, source assumptions, and any obvious gaps before moving on. Do not turn mandatory context gathering into a broad background scan.

Relevant context should clarify:

- intent: what the work was meant to accomplish and why
- definitions: how the work, metric, or source is defined and measured
- timing: what changed around the analysis period that could affect interpretation
- constraints: decisions, caveats, or limitations that affect what action is realistic

### 3. Frame The Analysis

Turn the question into a focused analytical framework.

Define a framework for answering the question with data:

- the specific data questions that would support or change the recommendation
- the comparisons and dimensions to inspect
- the unit of analysis that matches the decision
- the metric definitions and caveats needed to interpret the result

Use the framework to surface plausible hypotheses or interpretations, then turn them into focused data questions. Keep the framework specific enough to avoid broad exploration and support a recommendation.

Use `design-kpis` when the success metric, driver metrics, guardrails, or measurement plan need to be defined before the analysis can proceed.

Start by defining what the answer needs to show in plain language. Then choose the data that matches that meaning as closely as possible, including who is counted and what comparison makes the number meaningful. If a field or event captures only part of what the decision cares about, say what it captures and what it leaves out.

### 4. Run Focused Quantitative Analysis

Run enough quantitative analysis to support or reject the framed hypotheses and inform the decision:

- **Follow the framework.** Run the analyses that could change the recommendation first. Track additional data questions that emerge, answer the ones that matter for the decision, and leave lower-impact cuts as follow-up instead of expanding into broad exploration.

- **Use the right comparison.** Interpret results against the relevant baseline, denominator, or comparison point before turning them into a recommendation. For example, do not conclude that one group is the best opportunity just because it has the most total usage. Check whether usage is high because the group is larger, whether the pattern still holds after normalizing by the active base, whether the group is growing or declining, whether the usage reflects the behavior or outcome that matters, and whether business context changes the interpretation.

- **Size the opportunities.** Estimate the magnitude of impact each important opportunity could have. State what is being compared, which metric represents impact, what denominator or population it uses, and whether the data is complete enough to trust. Keep material unknown or unclassified groups visible when they could change the interpretation.

- **Keep quantitative work inspectable.** Use `jupyter-notebooks` to record queries and analysis. Use `analyze-data-quality` when source freshness, grain, joins, missingness, schema drift, or unexpected distributions could affect trust.

- **Validate before concluding.** Use `validate-data` before sharing stakeholder-facing recommendations, high-impact claims, or surprising results. When dashboards and direct queries both exist, reconcile them or explain why they differ.

### 5. Translate Evidence Into Decision Implications

Frame the findings within the broader business context. Do not present quantitative evidence and business context as two unrelated streams.

Interpret the evidence through the decision lenses that best fit the question. Choose lenses that would actually change the recommendation, and skip ones that would add noise or false precision. Common lenses include:

- **Current scale:** Is the opportunity or problem large enough today to matter for the decision?
- **Momentum:** Is the signal growing, shrinking, accelerating, or newly emerging?
- **Breadth:** Is the pattern broad-based, or does it only appear in a narrow corner of the business?
- **Concentration:** Does the conclusion depend on a few large entities, events, or outliers?
- **Intensity:** Is the behavior deep enough per unit to suggest real need, value, or risk?
- **Efficiency:** Does the option create better output, margin, conversion, productivity, or quality for the input required?
- **Addressability:** Can the team realistically act on this option with available product, GTM, operational, policy, or technical levers?
- **Differentiation:** Does this group or use case require a distinct motion, product experience, support model, or message?
- **Substitution:** Is there evidence that behavior, spend, time, or workload could shift from another path?
- **Risk or dependency:** Are there quality, trust, compliance, technical, operational, or data constraints that change the recommendation?
- **Coverage:** Are unknown, missing, or sparsely tagged records large e

…(truncated for compiled role skill)…


### Method component: data-analytics:design-kpis

# Design KPIs

Design KPI frameworks, set targets, and develop measurement plans that help teams make product or business decisions.

## When To Use Data Quality First

Use `analyze-data-quality` first when the task is to reconcile existing metrics, dashboards, tables, owners, or sources of truth.

Return to this skill only when the user asks to define the metric going forward, redesign the KPI framework, choose guardrails, or set targets.

## Skill Configuration

### Source Discovery And Verification

Use the relevant semantic layer as a starting map, not a boundary.

1. **Explore all possible sources.** Search every connected or provided source that could contain task-relevant data or change the interpretation. Within each structured-data source, run fresh catalog or metadata discovery for relevant schemas, datasets, tables, views, models, and metrics. Known sources, tables, dashboards, and semantic mappings are starting points, not stopping points.
2. **Compare duplicates and conflicts.** When sources overlap or disagree, compare ownership, freshness, definition, grain, coverage, and directness. Use the best authoritative source, or combine complementary sources when needed. Note material conflicts, explain why the selected source or sources control the answer, and verify selected data through live reads before concluding.

### Source Access Guardrail

Before querying sources, building artifacts, or drawing conclusions, determine whether the answer requires a specific source of truth.

If a required source is unavailable, stop that path. Tell the user what source is needed, ask them to make it available or provide a reviewed fallback, and do not treat weaker substitutes as equivalent.

If the missing source is only optional enrichment, continue with the strongest available evidence and label the gap when it materially affects the answer.

Clarify with the user when a missing input would materially change the analytical frame or recommendation. Otherwise make a reasonable assumption, state it, and proceed.

## Workflow

### 1. Clarify The Decision And Operating Context

Understand the decision the metrics need to support, the context in which they will be reviewed, and who will act on the result. Ask the user to clarify the goal, operating cadence, or measurement constraints when missing or ambiguous input would change the recommendation.

### 2. Gather Evidence Before Recommending Metrics

When the prompt does not already provide enough context to know what success means, gather that context before recommending metrics or targets. Use `gather-business-context` to understand the goal, current state, audience, constraints, risks, existing definitions, prior decisions, and any baseline or target context that should shape the metric system.

For KPI design, use that context to clarify what success is meant to mean, how related metrics have been defined before, and which constraints or risks should affect the recommended KPIs, drivers, guardrails, or measurement plan.

### 3. Generate A Wider Candidate Set

Create candidate outcome, driver, and guardrail metrics before narrowing.
Each candidate should have a clear definition and a plausible link to the decision. Use the example metric shapes below as inspiration when helpful, not as a required template.

### 4. Compare And Select Metrics

Compare candidate metrics by whether they:

- reflect the goal: the metric should represent the intended outcome. When using a proxy, explain why it should reflect real progress and where it could mislead.
- inform a real decision: movement should change what the team does, prioritizes, or investigates.
- show useful signal at the decision cadence: a metric can be conceptually good but too slow-moving or noisy for the decision it supports. For example, annual retention may be the right outcome, but it may not help a weekly launch review unless paired with earlier indicators.
- can be influenced by the team: the team should have plausible levers, or the metric should be paired with drivers it can affect.
- can be measured operationally: the team should be able to instrument, calculate, and track the metric consistently without one-off manual work.
- are hard to improve in a misleading way: improving the metric should not obviously hide harm to quality, trust, retention, cost, or another important outcome.

Use lightweight scoring only when it helps explain tradeoffs. Recommend `1-3` primary KPIs, `1-2` driver metrics for each KPI when they improve diagnosis, and `1-2` guardrails when tradeoffs are likely. Do not recommend extra metrics unless they materially improve decision-making.

For each recommended metric, include enough detail for the team to use it: what it measures, why it matters, how it is calculated, where it comes from, its main pros and cons against the selection criteria above, and what caveats or guardrails matter.

### 5. Set Targets When Needed

Treat target setting as a separate judgment from metric selection. First decide what should be measured; then set targets when the user asks or when the recommendation needs a threshold to be useful.

Use the target-setting approach that best fits the evidence:

- Top-down: start from benchmarks, historical performance, comparable products, competitor or market context, or a reasoned view of what good would need to look like for the decision.
- Bottom-up: start from what the team can realistically do, such as what is shipping, how adoption is expected to build, or which operating levers should move the metric.

Use data to set or evaluate targets. Once the target-setting approach is clear, identify what data it requires, such as provided inputs, internal performance data, external benchmarks or market data, and results from similar past work.

Compare aspirational targets with what the team can realistically influence through planned work, available audience, expected adoption, and historical movement. A good target should be meaningful for the decision and plausible enough to guide action. Explain the target anchor, key assumptions, and confidence. If the strongest target-setting method requires missing inputs, share the methodology and ask whether the user can provide or identify the relevant data. If there is still enough evidence for a directional target, present it as a provisional range; otherwise recommend the measurement needed before setting a firm target.

### 6. Deliver The Recommendation

Keep the final recommendation concise and decision-oriented, and deliver it inline by default. Do not Use inlined method components `build-report` merely because the KPI framework uses evidence, compares candidates, or contains several metrics. Use ``visualize-data`` and ``build-report`` when a data visual would materially improve the answer, such as by showing how a proposed target compares with historical performance or benchmarks, or by clarifying tradeoffs or candidate scoring. Honor an explicitly requested report, dashboard, notebook, spreadsheet, native document, or slide deck as the primary artifact. The recommendation should include:

1. initiative summary
2. recommended metric candidates, with definition and rationale
3. target recommendation, if included, with anchor, assumptions, and methodology
4. evidence reviewed
5. assumptions and missing context
6. risks and guardrails
7. open questions

## Example Metric Shapes

Different contexts need different metric shapes. Use these as examples, not a template:

- Product launch or adoption: pair an outcome metric for adoption or value realization with drivers for activation, engagement, repeat use, or time to value, plus guardrails for experience quality.
- Growth work: choose the business outcome the team is trying to improve, such as activation, retention, or monetization; add drivers that explain how growth is expected to happen and guardrails for quality.
- Funnel work: choo

…(truncated for compiled role skill)…


### Method component: data-analytics:market-sizing

## Related Skills

Use `visualize-data` when the sizing result needs a chart or figure.

Use `build-report` to package the final estimate, assumptions, sensitivity, caveats, and source context whenever this skill is selected, unless the user explicitly requests an inline, chat-only, brief/no-artifact answer, asks not to create a report/file/artifact, or selects another primary artifact.

# Market Sizing

Use this skill to produce a defensible estimate of a market or opportunity from connected context, public sources, transparent assumptions, and auditable calculations. The job is to define the market, choose a sound sizing method, distinguish evidence from assumptions, test sensitivity, and state what would most improve confidence.

## Skill Configuration

### Source Discovery And Verification

Use the relevant semantic layer as a starting map, not a boundary.

1. **Explore all possible sources.** Search every connected or provided source that could contain task-relevant data or change the interpretation. Within each structured-data source, run fresh catalog or metadata discovery for relevant schemas, datasets, tables, views, models, and metrics. Known sources, tables, dashboards, and semantic mappings are starting points, not stopping points.
2. **Compare duplicates and conflicts.** When sources overlap or disagree, compare ownership, freshness, definition, grain, coverage, and directness. Use the best authoritative source, or combine complementary sources when needed. Note material conflicts, explain why the selected source or sources control the answer, and verify selected data through live reads before concluding.

### Source Access Guardrail

Before querying sources, building artifacts, or drawing conclusions, determine whether the answer requires a specific source of truth.

If a required source is unavailable, stop that path. Tell the user what source is needed, ask them to make it available or provide a reviewed fallback, and do not treat weaker substitutes as equivalent.

If the missing source is only optional enrichment, continue with the strongest available evidence and label the gap when it materially affects the answer.

Clarify with the user when a missing input would materially change the estimate or recommendation. Otherwise make a reasonable assumption, state it, and proceed.

## Workflow

### 1. Frame The Market Or Opportunity

Define the market or opportunity boundary before estimating:

- What is being sized, for example a product category, workflow, problem, use case, or category of activity.
- Where and when it applies, for example geography, segment scope, time horizon, or market maturity.
- Who or what counts as part of the market, for example the relevant population, unit of demand, transaction type, or included activity.
- How the opportunity is measured, for example spend, revenue, volume, value created, or another unit that fits the question.
- What kind of sizing answer the user needs, for example TAM/SAM/SOM, market entry, expansion upside, spend pool, revenue pool, population count, or unit volume.

### 2. Choose A Starting Sizing Approach And Inputs

Pick the simplest sound sizing approach for the question, then sketch the calculation chain and the major inputs the estimate will depend on.

A top-down model works when reliable aggregate market data exists; a bottom-up model works when the market can be built from observable units and assumptions; a value-based model works when the estimate should start from the value created rather than a published market total. Use a mixed approach only when cross-checking would materially improve confidence. If more than one approach fits, briefly explain which one you trust most and why.

Expect the first approach to change if source checks show that another model would be more defensible.

### 3. Gather Sources For The Inputs

Choose sources based on the inputs the estimate depends on most.

Start with user-named sources when provided. Then use the strongest available evidence for each major input from the starting approach. Use `~~structured_data` when an input should come from the user's data warehouse or another structured data source. Use context lanes such as `~~company_docs`, `~~team_communication`, or `~~dashboards_or_bi` when an input needs business meaning, source-of-truth guidance, or assumptions that are not captured in structured data alone. When an input depends on the outside market, use public sources for benchmarks, population estimates, comparable markets, or proxy assumptions.

Use `gather-business-context` to resolve context lanes when the right source of truth, business meaning, or assumption set is unclear.

If the strongest source is unavailable or thin, continue with a transparent proxy assumption only when the estimate is still useful. Label the gap and explain how it affects confidence.

### 4. Separate Facts From Assumptions

Keep sourced facts, inferred estimates, and judgment calls distinct in the model. When exact data is unavailable, use a defensible proxy, explain why it is reasonable, and note the confidence level. Ground assumptions in evidence about how the market actually behaves, what can realistically change, and what determines the size of the opportunity.

### 5. Build The Model

Make the model easy to inspect and adjust.

The model should make these elements easy to audit or revise:

- market definition and measurement unit
- assumptions and source context
- calculation chain and derived values
- base case, material ranges, and sensitivity logic
- validation priorities

For each major input, make the source path visible: structured data, context lane, public source, user-provided input, or proxy assumption.

Keep derived values traceable to formulas or code rather than hardcoded outputs.

Use `jupyter-notebooks` when code is needed for source harmonization, calculations, sensitivity analysis, or reusable modeling logic. Keep formulas, inputs, intermediate calculations, and sensitivity logic inspectable.

Use the `$Spreadsheets` skill when the user requests a spreadsheet, workbook, or Google Sheets deliverable, or when a market-sizing model would materially benefit from editable assumptions, sensitivity tables, charts, or polished workbook formatting.

### 6. Test Sensitivity

Identify the assumptions that move the estimate most.

Show how the estimate changes when those assumptions move up or down. Prefer simple, decision-useful sensitivity analysis over exhaustive scenario sprawl.

Use ranges when uncertainty is material. Do not hide uncertainty behind a single point estimate when the inputs are thin.

### 7. State The Estimate And Validation Priorities

End by handing the estimate, method, key assumptions, uncertainty, and next validation priorities to `build-report` unless the user explicitly waives report creation or selects another primary artifact. This handoff is mandatory when no explicit human waiver was given; do not infer a waiver because the user asked for an estimate or did not use the word "report". This workflow owns the sizing model and conclusion; `build-report` owns the reader-facing structure, visuals, evidence placement, and delivery surface.

Before handoff, make the market-sizing conclusion explicit:

- market definition and measurement unit
- estimate or range
- method and calculation chain
- key assumptions and source support
- main uncertainty drivers and sensitivity takeaways
- validation priorities and practical interpretation for the user's decision

If source coverage is thin, say which major inputs rely on proxy assumptions and what source would most improve them.

Use `validate-data` when methodology, calculations, assumptions, caveats, or source support need review before sharing.

Do not render charts directly from this skill. If a sensitivity, scenario, funnel, or market-breakdown visual would clarify the estimate, pass that vis

…(truncated for compiled role skill)…


### Method component: doc-coauthoring

# doc-coauthoring

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Guide users through a structured workflow for co-authoring documentation

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="doc-coauthoring")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('doc-coauthoring')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'doc-coauthoring'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: a2502aadf340b077d12a0b30f07395693653c3a5d36188650316c1938c00a67e -->

---

# Codex Skill Conversion

Original Claude skill: `doc-coauthoring`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/doc-coauthoring`  
Risk tier: `medium`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Doc Co-Authoring Workflow

This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking users through three stages: Context Gathering, Refinement & Structure, and Reader Testing.

## When to Offer This Workflow

**Trigger conditions:**
- User mentions writing documentation: "write a doc", "draft a proposal", "create a spec", "write up"
- User mentions specific doc types: "PRD", "design doc", "decision doc", "RFC"
- User seems to be starting a substantial writing task

**Initial offer:**
Offer the user a structured workflow for co-authoring the document. Explain the three stages:

1. **Context Gathering**: User provides all relevant context while Claude asks clarifying questions
2. **Refinement & Structure**: Iteratively build each section through brainstorming and editing
3. **Reader Testing**: Test the doc with a fresh Claude (no context) to catch blind spots before others read it

Explain that this approach helps ensure the doc works well when others read it (including when they paste it into Claude). Ask if they want to try this workflow or prefer to work freeform.

If user declines, work freeform. If user accepts, proceed to Stage 1.

## Stage 1: Context Gathering

**Goal:** Close the gap between what the user knows and what Claude knows, enabling smart guidance later.

### Initial Questions

Start by asking the user for meta-context about the document:

1. What type of document is this? (e.g., technical spec, decision doc, proposal)
2. Who's the primary audience?
3. What's the desired impact when someone reads this?
4. Is there a template or specific format to follow?
5. Any other constraints or context to know?

Inform them they can answer in shorthand or dump information however works best for them.

**If user provides a template or mentions a doc type:**
- Ask if they have a template document to share
- If they provide a link to a shared document, use the appropriate integration to fetch it
- If they provide a file, read it

**If user mentions editing an existing shared document:**
- Use the appropriate integration to read the current state
- Check for images without alt-text
- If images exist without alt-text, explain that when others use Claude to understand the doc, Claude won't be able to see them. Ask if they want alt-text generated. If so, request they paste each image into chat for descriptive alt-text generation.

### Info Dumping

Once initial questions are answered, encourage the user to dump all the context they have. Request information such as:
- Background on the project/problem
- Related team discussions or shared documents
- Why alternative solutions aren't being used
- Organizational context (team dynamics, past incidents, politics)
- Timeline pressures or constraints
- Technical architecture or dependencies
- Stakeholder concerns

Advise them not to worry about organizing it - just get it all out. Offer multiple ways to provide context:
- Info dump stream-of-consciousness
- Point to team channels or threads to read
- Link to shared documents

**If integrations are available** (e.g., Slack, Teams, Google Drive, SharePoint, or other MCP servers), mention that these can be used to pull in context directly.

**If no integrations are detected and in Claude.ai or Claude app:** Suggest they can enable connectors in their Claude settings to allow pulling context from messaging apps and document storage directly.

Inform them clarifying questions will be asked once they've done their initial dump.

**During context gathering:**

- If user mentions team channels or shared documents:
  - If integrations available: Inform them the content will be read now, then use the appropriate integration
  - If integrations not available: Explain lack of access. Suggest they enable connectors in Claude settings, or paste the relevant content directly.

- If user mentions entities/projects that are unknown:
  - Ask if connected tools should be searched to learn more
  - Wait for user confirmation before searching

- As user provides context, track what's being learned and what's still unclear

**Asking clarifying questions:**

When user signals they've done their initial dump (or after substantial context provided), ask clarifying questions to ensure understanding:

Generate 5-10 numbered questions based on gaps in the context.

Inform them they can use shorthand to answer (e.g., "1: yes, 2: see #channel, 3: no because backwards compat"), link to more docs, point to channels to read, or just keep info-dumping. Whatever's most efficient for them.

**Exit condition:**
Sufficient context has been gathered when questions show understanding - when edge cases and trade-offs can be asked about without needing basics explained.

**Transition:**
Ask if there's any more context they want to provide at this stage, or if it's time to move on to drafting the document.

If user wants to add more, let them. When ready, proceed to Stage 2.

## Stage 2: Refinement & Structure

**Goal:** Build the document section by section through brainstorming, curation, and iterative refinement.

**Instructions to user:**
Explain that the document will be built section by section. For each section:
1. Clarifying questions will be asked about what to include
2. 5-20 options will be brainstormed
3. User will indicate what to keep/remove/combine
4. The section will be drafted
5. It will be refined through surgical edits

Start with whichever section has the most unknowns (usually the core decision/proposal), then work through the rest.

**Section ordering:**

If the document structure is clear:
Ask which section they'd like to start with.

Suggest starting with whichever section has the most unknowns. For decision docs, that's usually the core proposal. For specs, it's typically the technical approach. Summary sections are best left for last.

If user doesn't know what sections they need:
Based on the type of document and template, suggest 3-5 sections appropriate f

…(truncated for compiled role skill)…


## Role operating loop

Define why and what to build from evidence; route technical design and implementation to their owning roles.

## Workflow

1. Retrieve goals, product inventory, queue/build history, beta/support feedback, analytics, incidents, costs, revenue signals, and prior decisions.
2. Define user, job-to-be-done, current workaround, frequency, severity, evidence, and why now before proposing a feature.
3. Establish baseline, one outcome metric, guardrails, leading indicators, formula, source, segmentation, owner, and meaningful-change threshold.
4. Compare doing nothing, improving an existing flow, operational change, and build options. Search Arcanum and reusable code before creating a parallel product.
5. Run the cheapest experiment that can falsify the highest-risk assumption with declared success and stop thresholds.
6. Prioritize value, reach, confidence, effort, strategic fit, risk reduction, dependency readiness, and reversibility transparently.
7. Write users, outcome, non-goals, requirements, journey, data/privacy, metrics, numbered acceptance, instrumentation, rollout, and kill criteria.
8. Route UX, architecture, data, compliance, implementation, certification, and release work with explicit handoff evidence.
9. Inspect verified delivery and outcome movement, not activity or feature count; record scope changes.
10. Compare post-release cohorts with baseline and decide expand, iterate, or retire; persist learning and checkpoint SOL.

## Capability contract

Use echo.buildtracker.*, echo.prompts.*, echo.builds.*, echo.beta.*, echo.betaportal.*, echo.context.*, echo.knowledge.*, echo.commerce.*, echo.swarm.*, echo.caps.*, and echo.sdk.* through the scoped broker.

## Deep reference

Read [the product operating contract](references/operating-contract.md) for discovery evidence, metric schemas, prioritization, PRD fields, experiments, and post-release reviews.

## Done gate

The decision has traceable evidence, an owned measurable outcome, explicit non-goals, executable acceptance, routed dependencies, and a learning/retirement loop.

## Capability contract

- Scopes: `echo.beta.*`, `echo.betaportal.*`, `echo.builds.*`, `echo.buildtracker.*`, `echo.caps.*`, `echo.commerce.*`, `echo.context.*`, `echo.knowledge.*`, `echo.prompts.*`, `echo.sdk.*`, `echo.swarm.*`
- Capability families: `echo.beta.*`, `echo.betaportal.*`, `echo.buildtracker.*`, `echo.prompts.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `product-manager`. If denied, run: `Skill(echo-fleet-roles:echo-product-manager-power)` (or equivalent Skill tool load).
