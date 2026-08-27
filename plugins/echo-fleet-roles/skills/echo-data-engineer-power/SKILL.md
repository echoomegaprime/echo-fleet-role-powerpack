---
name: echo-data-engineer-power
description: Design, migrate, validate, optimize, and operate trustworthy ECHO schemas, pipelines, datasets, indexes, lineage, quality, and recovery. Use for Claude auto or Codex cauto Data Engineer sessions, database changes, ETL/ELT, migrations, backfills, vector stores, data quality, lineage, retention implementation, performance, and restore/replay proof.
---

# ECHO Data Engineer Power

Self-contained compiled power skill for the `data-engineer` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `data-pipeline`
- `data-analytics:analyze-data-quality`
- `data-analytics:validate-data`
- `echo-frontier-infrastructure`

### Method component: data-pipeline

# data-pipeline

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Complete ETL (Extract, Transform, Load) and data processing platform for CSV, JSON, Excel, databases, and APIs

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="data-pipeline")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('data-pipeline')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'data-pipeline'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: f2da02501476fb84fe407fbdca01ffd0468267f8867a6ce9a9e050ad24457688 -->

---

# Codex Skill Conversion

Original Claude skill: `data-pipeline`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/data-pipeline`  
Risk tier: `high`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Data Pipeline

ETL and data processing for Authority Level 11.0 operations.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      DATA PIPELINE                              │
├─────────────────────────────────────────────────────────────────┤
│  EXTRACT                                                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │   CSV    │ │   JSON   │ │  Excel   │ │   API    │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │ Postgres │ │  SQLite  │ │  MySQL   │ │  MongoDB │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
├─────────────────────────────────────────────────────────────────┤
│  TRANSFORM                                                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │  Clean   │ │ Validate │ │  Enrich  │ │ Aggregate│           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
├─────────────────────────────────────────────────────────────────┤
│  LOAD                                                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │   File   │ │ Database │ │   API    │ │  Cloud   │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

```python
from scripts.data_pipeline import DataPipeline

dp = DataPipeline()

# Simple ETL
data = dp.extract_csv("input.csv")
data = dp.transform(data, [
    {"clean": "trim_whitespace"},
    {"filter": "column > 0"},
    {"rename": {"old_name": "new_name"}}
])
dp.load_csv(data, "output.csv")
```

## Extract

### File Sources

```python
# CSV
data = dp.extract_csv("data.csv", encoding="utf-8")

# JSON
data = dp.extract_json("data.json")

# Excel
data = dp.extract_excel("data.xlsx", sheet="Sheet1")

# Parquet
data = dp.extract_parquet("data.parquet")

# Multiple files
data = dp.extract_glob("data/*.csv")
```

### Database Sources

```python
# PostgreSQL
data = dp.extract_postgres(
    connection_string="postgresql://user:pass@host/db",
    query="SELECT * FROM table WHERE date > '2024-01-01'"
)

# SQLite
data = dp.extract_sqlite("database.db", "SELECT * FROM users")

# MySQL
data = dp.extract_mysql(
    host="localhost",
    user="root",
    password="pass",
    database="mydb",
    query="SELECT * FROM orders"
)
```

### API Sources

```python
# REST API
data = dp.extract_api(
    url="https://api.example.com/data",
    headers={"Authorization": "Bearer token"},
    params={"limit": 1000}
)

# Paginated API
data = dp.extract_api_paginated(
    url="https://api.example.com/items",
    page_param="page",
    max_pages=10
)

# GraphQL
data = dp.extract_graphql(
    url="https://api.example.com/graphql",
    query="{ users { id name email } }"
)
```

## Transform

### Cleaning

```python
data = dp.transform(data, [
    # Remove duplicates
    {"dedupe": ["id"]},
    
    # Trim whitespace
    {"clean": "trim"},
    
    # Handle nulls
    {"fill_null": {"column": "default_value"}},
    
    # Remove nulls
    {"drop_null": ["required_column"]},
    
    # Type conversion
    {"cast": {"amount": "float", "date": "datetime"}}
])
```

### Filtering

```python
data = dp.transform(data, [
    # Simple filter
    {"filter": "amount > 100"},
    
    # Multiple conditions
    {"filter": "status == 'active' AND created > '2024-01-01'"},
    
    # In list
    {"filter_in": {"category": ["A", "B", "C"]}},
    
    # Top N
    {"top": 100, "by": "score", "desc": True}
])
```

### Reshaping

```python
data = dp.transform(data, [
    # Select columns
    {"select": ["id", "name", "amount"]},
    
    # Rename columns
    {"rename": {"old_name": "new_name"}},
    
    # Add computed column
    {"compute": {"total": "price * quantity"}},
    
    # Pivot
    {"pivot": {"index": "date", "columns": "category", "values": "amount"}},
    
    # Unpivot/Melt
    {"melt": {"id_vars": ["id"], "value_vars": ["jan", "feb", "mar"]}}
])
```

### Aggregation

```python
data = dp.transform(data, [
    # Group and aggregate
    {"group_by": ["category"], "agg": {
        "total": ("amount", "sum"),
        "avg_price": ("price", "mean"),
        "count": ("id", "count")
    }},
    
    # Window functions
    {"window": {
        "running_total": "sum(amount) over (order by date)",
        "rank": "row_number() over (partition by category order by score desc)"
    }}
])
```

### Joining

```python
# Merge datasets
data = dp.join(
    left=customers,
    right=orders,
    on="customer_id",
    how="left"
)

# Multiple joins
data = dp.join_multiple([
    {"data": customers, "on": "customer_id"},
    {"data": products, "on": "product_id"},
    {"data": regions, "on": "region_code"}
])
```

### Validation

```python
# Validate and report errors
valid_data, errors = dp.validate(data, {
    "id": {"required": True, "unique": True},
    "email": {"required": True, "pattern": r".*@.*\..*"},
    "amount": {"required": True, "min": 0, "max": 1000000},
    "status": {"required": True, "values": ["active", "inactive"]}
})

# Raise on validation error
dp.validate_strict(data, schema)
```

## Load

### File Destinations

```python
# CSV
dp.load_csv(data, "output.csv")

# JSON
dp.load_json(data, "output.json")

# Excel
dp.load_excel(data, "output.xlsx", sheet="Results")

# Parquet
dp.load_parquet(data, "output.parquet")
```

### Database Destinations

```python
# PostgreSQL
dp.load_postgres(data, "postgresql://...", "target_table", if_exists="replace")

# SQLite
dp.load_sqlite(data, "database.db", "target_table")

# Upsert (insert or update)
dp.upsert_postgres(data, "postgresql://...", "table", key_columns=["id"])
```

### API Destinations

```python
# POST to API
dp.load_api(
    data,
    url="https://api.example.com/i

…(truncated for compiled role skill)…


### Method component: data-analytics:analyze-data-quality

## Related Skills

Use `design-kpis` when the work is to define or redesign a KPI framework, metric definition, guardrail, or target rather than checking whether existing data is trustworthy.

Use `validate-data` when the work is to QA an analysis, chart, report, or recommendation rather than investigate the underlying data.

# Analyze Data Quality

Assess whether a dataset is trustworthy enough for analysis, modeling,
dashboards, experiments, or downstream pipelines. Start with the intended use and grain, run the highest-value checks for the data shape, and report concrete evidence, analytical risk, likely causes, and the smallest useful remediation or automated test.

## Workflow

1. Clarify the quality question and operating context.

   Establish what the dataset represents, the intended unit of analysis, the downstream use, whether the user cares about raw ingestion quality,
   transformed-model quality, or both, and the comparison baseline such as prior weeks, prior schema, or a trusted reference table. Identify expected grain,
   primary keys or candidate keys, important date columns, timezone assumptions,
   domain rules, allowed values, and business thresholds. If context is missing,
   infer cautiously and label assumptions.

2. Choose an inspectable analysis path.

   When checks require SQL or Python, default to a companion notebook so the user can inspect the exact code behind the findings. Use `jupyter-notebooks` when a dedicated notebook scaffold or refactor workflow would help. For queryable tables, use `~~structured_data` to confirm schema, grain, sample rows, and query rules through the relevant source connector before heavier checks. Use `~~operations_logs` for freshness and lineage when those checks matter.

3. Build a compact profile.

   Start with row count, column count, column names and types, candidate keys,
   duplicate rates on likely identifiers, min/max timestamps for relevant date columns, null rates, distinct counts for likely categorical columns, and basic numeric summaries for measure columns. Confirm grain before interpreting anomalies; many apparent quality problems are mixed-grain data,
   partial backfills, late-arriving data, or duplicated joins.

4. Run core quality checks.

   Select checks that match the dataset and task. Default to the most relevant checks across completeness, uniqueness, validity, consistency, integrity,
   timeliness, volume, and shape. Compare rates, not just counts, and segment by time, source, country, platform, model version, or other key dimensions when that helps distinguish real issues from expected variation.

5. Run shape-specific checks.

   Adapt the checks to the data shape:

   - Event data: duplicate event IDs, future event timestamps, session or user
     coverage gaps, and abrupt event-mix changes after releases.
   - Dimension tables: non-unique business keys, orphan surrogate keys, status
     changes without corresponding timestamps, and unexpected churn in reference
     values.
   - Fact tables: mixed grain, impossible measures such as negative revenue or
     quantity, join blowups to dimensions, and late-arriving or partially loaded
     partitions.
   - ML feature or scoring tables: leakage from post-outcome fields, feature
     sparsity spikes, range shifts after model or feature-store changes, and
     class-label drift.
   - Experiment data: duplicate assignments, variant imbalance beyond
     expectation, exposure without assignment, and events before assignment
     timestamp.

6. Run temporal and distribution checks when history exists.

   Prioritize temporal diagnostics when the user mentions "after X date",
   "suddenly", "recently", or "only started appearing". Check first-seen dates,
   last-seen dates, daily or weekly null-rate trends, duplicate-rate trends, row count trends, category-share shifts, distribution drift, and change points around launches, migrations, incidents, model changes, or backfills.

7. Investigate analytical risks and likely causes.

   Tie each issue to the downstream risk: broken trusted analysis, biased decisions, broken joins, stale dashboards, incorrect experiments, leakage,
   unreliable model features, or misleading segments. When possible, identify whether the issue is isolated to a source, segment, partition, time window,
   release, migration, backfill, or upstream pipeline change.

8. Recommend fixes or automated tests.

   Recommend the smallest set of follow-up fixes, monitoring, or automated tests that would materially reduce risk. Suggest automation only when the rule is stable and worth maintaining. Include or save the notebook/query path when code produced the findings.

## Standards

### Core Checks

- Completeness: null rate by column; null rate by partition, segment, and time bucket; unexpected empty strings or sentinel values; required-column population rate.
- Uniqueness: exact duplicate rows, duplicate primary keys, duplicate composite keys, and proportion unique for semi-unique fields such as emails or device IDs.
- Validity: type conformance after casting; format checks for IDs, emails, URLs,
  enums, country codes, and timestamps; range checks for measures, percentages,
  counts, and dates; allowed-values checks for controlled vocabularies.
- Consistency: cross-field rule checks, units or currency consistency, status and timestamp alignment, and agreement between duplicated fields from different sources.
- Integrity: parent-child key coverage, orphan records, unexpected many-to-many joins, and broken slowly changing dimension joins.
- Timeliness: freshness lag from source event time to load time, freshness lag from load time to report time, missing recent partitions, and unexplained historical rewrites or backfills.
- Volume and shape: row-count drift, distinct-count drift, distribution drift,
  share-of-total drift for major categories, and new or disappeared categories.

### Specific Check Guidance

- Duplicates and keys: check exact duplicates, primary key duplicates, composite key duplicates at the intended grain, and near-duplicates caused by whitespace,
  casing, formatting, or late updates. Report count, share of affected rows,
  duplicated keys, and whether duplication is isolated to a time range, source,
  or segment.
- Missingness: distinguish acceptable sparsity from broken completeness. Check null rates over time, newly null columns after schema or pipeline changes, and sentinel values such as `''`, `'unknown'`, `'n/a'`, `0`, or `-1`.
- Domain validity: check malformed identifiers, country codes, timestamps,
  impossible values, values outside allowed sets, and cross-field contradictions such as `is_cancelled = false` with a non-null `cancelled_at`.
- Join coverage: when multiple datasets are involved, check foreign keys that do not match a parent table, unexpected one-to-many expansion, coverage loss when joining to dimensions or experiments, and row counts before and after joins.
- Freshness and schema drift: check row-count changes against recent history,
  lag on important date columns, added/removed/retyped columns, and shifts in sparsity or cardinality that suggest upstream changes.
- Outliers and distribution shifts: use robust methods such as quantiles, MAD,
  or IQR before defaulting to z-scores. Check sudden changes in mean, median,
  variance, zero rate, category share, and long-tail behavior.
- Leakage, backfill, and time travel: check features populated before they should exist, future-dated records, late-arriving data causing unstable recent partitions, and backfills that change historical counts without annotation.

### Severity

- Critical: breaks trusted analysis, core joins, production dashboards, or key decisions, such as duplicated grain, missing primary keys, or stale production data.
- High: materially biases downstream decisions, such as large null spikes,
  category drift in a core dimension

…(truncated for compiled role skill)…


### Method component: data-analytics:validate-data

## Related Skills

Use `analyze-data-quality` when validation depends on whether the underlying data is trustworthy, comparable, fresh, or at the right grain.

Use `product-business-analysis` when the task asks for a recommendation or decision after the validation pass.

# Validate Data Analysis

Validate an analysis before it is shared with stakeholders. Focus on whether the question, data, methodology, calculations, visuals, claims, caveats, and recommendations are trustworthy enough for the stated audience and decision.
This skill is for analysis QA, not raw dataset profiling alone. When validation depends on dataset reliability checks such as freshness, grain, missingness,
duplicates, join coverage, or source mismatches, use `analyze-data-quality` as a companion.

## Workflow

1. Inventory the artifact and claims.

   Identify the report, notebook, spreadsheet, SQL, dashboard, chart, pasted analysis, or recommendation being validated. Inspect source artifacts when a path, link, query, notebook, spreadsheet, or dashboard is referenced. Extract the main question, audience, decision, key claims, headline numbers, data sources, time windows, populations, filters, comparison baselines, and stated caveats. Verify that every metric or KPI requested by the user appears in the analysis or is explicitly marked unavailable, not applicable, or out of scope.

2. Validate the question, methodology, and assumptions.

   Confirm that the analysis answers the stated business or product question,
   not a nearby easier question. Check whether the population, eligibility rules, exclusions, sampling, metric definitions, formulas, units,
   denominators, timezones, cohorts, comparison periods, and baselines match the stakeholder decision. Flag hidden exclusions, inconsistent definitions,
   partial-period comparisons, and causal wording that lacks experimental or otherwise credible causal evidence.

3. Validate data selection and quality risks.

   Confirm that the chosen tables, files, dashboards, or extracts are appropriate and current enough for the decision. Check freshness or "as of"
   date, expected partitions, segment coverage, row/category completeness, null handling, deduplication, filter logic, join coverage, and source mismatches when those risks could change the conclusion. Use `~~structured_data` for source metadata, schema checks, sample rows, query history, or SQL spot checks through the relevant source connector when available. Use `~~operations_logs` for table freshness, lineage, or pipeline context.

4. Verify calculations and aggregations.

   Recompute the highest-impact numbers independently when possible. Check grain, subtotals, denominators, non-zero denominators, rate bases,
   period-over-period bases, weighted averages, units, currency, timezone handling, and whether mutually exclusive categories add to totals. For SQL,
   inspect join types, group-by grain, filters, distinct counts, and row counts before and after joins. Use `jupyter-notebooks` or `~~spreadsheet_workspace`
   when the artifact itself is a notebook or spreadsheet, or when reproducible spot checks need code or formulas.

5. Test reasonableness and common analytical traps.

   Compare magnitudes against known dashboards, historical reports, prior analyses, finance sources, or expected product scale when possible. Investigate trend jumps, drops, flatlines, exact round numbers, 0% or 100% rates, segment shares that should sum to about 100%, and results that perfectly confirm the hypothesis without friction. Check edge cases such as empty segments, new entities, and boundary dates.

6. Review visuals and presentation integrity.

   Confirm that charts use appropriate chart types, scales, axes, intervals,
   titles, labels, units, ordering, annotations, color, and precision. Use
   `visualize-data` for non-trivial chart review. For rendered reports,
   dashboards, slides, docs, PDFs, HTML, or other final artifacts, inspect the rendered output for broken charts, missing tables, clipped text, bad formatting, stale placeholders, and obvious layout issues. Check whether a quick reader could walk away with a misleading interpretation, especially from truncated axes, dual axes, 3D effects, inconsistent intervals, missing date ranges, or chart titles that overstate the data.

7. Evaluate narrative, conclusions, and recommendations.

   Confirm each conclusion is supported by visible evidence or saved artifacts.
   Separate verified findings from interpretation, caveats, and open questions.
   Identify alternative explanations, uncertainty, missing context,
   recommendations that go beyond the evidence, and any causal language that is not supported by the design.

8. Produce a confidence assessment and required fixes.

   Prioritize issues that materially affect the stakeholder decision. Separate blockers from caveats: do not block sharing for minor polish issues, but do block when a number, denominator, join, time window, population, comparison,
   or conclusion is materially unreliable. Record incomplete handoff blockers separately from caveats, including missing access, unavailable source artifacts, unrun checks, broken render steps, unresolved data-quality risks,
   or absent owner confirmation. If SQL, Python, a notebook, or a spreadsheet was used for validation, include the artifact path, query permalink, notebook path, spreadsheet tab, or dashboard link so the check is reproducible.

## Standards

### Validation Stance

- Validate the claims the analysis actually makes, not just whether the artifact looks polished.
- Prefer concrete evidence: recompute important numbers, inspect source data,
  check code paths, trace records, or reconcile against trusted sources when tools and access allow it.
- Label anything that cannot be verified, and state what would be needed to verify it.
- Treat surprising results, stakeholder-facing recommendations, causal claims,
  high-impact decisions, and externally shared analyses as higher-risk validation targets.
- Select checks that match the artifact and decision. Do not run every possible check mechanically.

### Methodology Checks

- Question framing: the analysis answers the stated business or product question.
- Data selection: sources are appropriate and current enough for the decision.
- Population: inclusions, exclusions, eligibility rules, and sampling are explicit.
- Metric definitions: formulas, units, denominators, and timezones are clear and aligned with stakeholder definitions.
- Baselines: comparison periods, cohorts, and contexts are comparable.
- Causality: causal wording is backed by experimental or otherwise credible causal evidence.

### Data Quality Checks

- Freshness: the analysis states or can recover the data "as of" date.
- Completeness: no unexpected missing partitions, segments, rows, or categories.
- Null handling: key columns have expected null rates or explicit treatment.
- Deduplication: primary entities are not double counted.
- Filter verification: filters and WHERE clauses do not silently exclude the population of interest.
- Join coverage: dimensions, experiments, and reference tables do not drop or multiply important rows.

### Calculation Checks

- Grain: the aggregation level matches the intended analysis grain.
- Denominators: rates and percentages use the correct population and non-zero denominators.
- Period alignment: comparisons use equal or explicitly caveated windows.
- Weighted metrics: averages are weighted correctly when group sizes differ.
- Subtotals: parts add to totals where categories are mutually exclusive.
- Units: currency, token, user, request, account, day/week/month, and timezone units are consistent.

### Reasonableness Checks

- Magnitudes are plausible relative to known dashboards, historical reports, or expected product scale.
- Percentages fall in expected ranges and segment shares sum to about 100% wh

…(truncated for compiled role skill)…


### Method component: echo-frontier-infrastructure

# Echo Frontier Infrastructure

Validate the installed policy:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoInfrastructurePolicy.ps1"
```

## Invariants

- No mutating action is remotely exposed.
- TRIGGERcmd contains read-only action IDs only.
- No public action accepts an arbitrary command or ScriptBlock.
- Every mutation has a confirmation token and audit record.
- Services are explicitly allowlisted.
- Skills and scripts separate judgment from deterministic enforcement.

A policy failure blocks expansion of the control plane. Fix the policy before adding capabilities.

## Role operating loop

Make data meaning, movement, quality, evolution, sensitivity, and recovery explicit and executable.

## Workflow

1. Inventory producers, consumers, schemas, versions, volumes, freshness, owners, sensitivity, retention, indexes, jobs, SLAs, cost, and failures using positive controls.
2. Define types, units, keys, nullability, uniqueness, time semantics, versioning, late/duplicate handling, compatibility, and quality thresholds.
3. Classify secrets and protected data; define access, encryption, retention/deletion/export, and logging boundaries without copying values.
4. Design expand, backfill, dual-read/write or compatibility, verify, canary cutover, observe, and contract phases.
5. Capture schema/count baseline and prove backup/restore before bounded mutation; estimate locks, disk, runtime, and abort thresholds.
6. Build idempotent/resumable pipelines with checkpoints, watermarks, dedupe keys, retry/dead-letter handling, lineage, quality, lag, counts, and cost telemetry.
7. Validate constraints, referential integrity, distributions, nulls, duplicates, reconciliation, time consistency, privacy, and consumer contracts.
8. Tune with plans, cardinality, I/O/cache, percentiles, batching, partitioning, indexes, concurrency, and baselines.
9. Canary consumers and compare old/new results; fail closed on divergence and preserve rollback compatibility.
10. Restore/replay a representative backup, verify consumers, publish contracts/lineage/evidence, register, and checkpoint SOL.

## Capability contract

Use echo.psql.*, echo.fs.*, echo.backup.*, echo.knowledge.*, echo.brain.*, echo.crystal.*, echo.monitor.*, echo.logs.*, echo.node.*, echo.shell.*, echo.caps.*, and echo.sdk.* through the scoped broker. Inspect schemas before writes.

## Deep reference

Read [the data operating contract](references/operating-contract.md) for contract fields, migration phases, quality suites, observability, protected-data handling, and recovery gates.

## Done gate

Versioned contracts are honored, migration reconciles, quality/freshness meet thresholds, lineage and operations are visible, consumers are green, and restore/replay is proven.

## Capability contract

- Scopes: `echo.backup.*`, `echo.brain.*`, `echo.caps.*`, `echo.crystal.*`, `echo.fs.*`, `echo.knowledge.*`, `echo.logaggregator.*`, `echo.logs.*`, `echo.monitor.*`, `echo.node.*`, `echo.psql.*`, `echo.sdk.*`, `echo.shell.*`
- Capability families: `echo.backup.*`, `echo.fs.*`, `echo.knowledge.*`, `echo.monitor.*`, `echo.psql.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `data-engineer`. If denied, run: `Skill(echo-fleet-roles:echo-data-engineer-power)` (or equivalent Skill tool load).
