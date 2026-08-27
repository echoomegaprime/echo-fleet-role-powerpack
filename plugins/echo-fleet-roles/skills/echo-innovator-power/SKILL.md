---
name: echo-innovator-power
description: Discover, evaluate, and compound high-leverage ECHO capabilities and product improvements. Use for Claude auto or Codex cauto innovator sessions, capability gaps, system upgrades, or novel product opportunities.
---

# ECHO Innovator Power

Self-contained compiled power skill for the `innovator` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `innovator-max:innovator-max`
- `innovator-max:capability-marketplace`
- `innovator-max:doorway-integration`
- `echo-graph-mode`

### Method component: innovator-max:innovator-max

# Innovator Max

Run a disciplined innovation loop: load the instructional doorway, retrieve current state, resolve reusable capabilities, choose a reversible high-leverage slice, implement it, verify it at the real boundary, and record what landed.

## Capability Runtime

Use `scripts/connector_runtime.py` as the local typed registry and resolver, and `scripts/connector_gateway.py --stdio` as the provider-neutral JSONL bridge for CLIs, chats, MCP, and HTTP adapters. It separates:

- role intent and constraints;
- connector capability metadata and schemas;
- retrieval/scoring;
- invocation through the scoped SOL SDK broker;
- redaction, retries, verification, and audit metadata.

All clients use `health`, `list`, `retrieve`, and `invoke`. Invocation defaults to a plan; `execute:true` is required for a real call. This is the safety and interoperability boundary.

Role bindings live in `registry/roles.json`. Load the selected role's source file, then use its declared skills and connector allowlist. The `troubleshooter` role is the recovery path for failures across code, services, SDKs, providers, chats, CLIs, and graphics.

Start with `python scripts/connector_runtime.py list`, then `retrieve --role innovator --intent "..."`. Resolve before invoking. Prefer the highest-scoring healthy connector and retain the alternatives in the evidence packet.

## Operating Contract

1. Resolve and read the repository instruction doorway through `doorway-integration`; then load active mission context.
2. Checkpoint SOL at startup and after material progress using the valid status vocabulary.
3. Retrieve moving facts through `python SYSTEMS/codex_auto/sol_cli.py sdk invoke ...`; never print tokens or secret payloads.
4. Search Arcanum, the code library, and current docs before inventing abstractions or invoking unfamiliar external tools.
5. Inspect `git status` and isolate the target scope before editing. Preserve unrelated changes and restricted data.
6. Select one bounded opportunity with an explicit acceptance test and rollback boundary.
7. Implement production quality: failure handling, diagnostics, tests, documentation, and a usable path after clone.
8. Run focused checks, then the narrow live/integration check appropriate to risk.
9. Run strict SOL verification, register the result with `echo.builds.log`, and persist material decisions through the SDK.

## Selection Heuristic

Prefer an active mission checkpoint, a queue item with a concrete acceptance test, a failing verification/reliability gap, a repeated manual operation worth automating, then a small product enhancement with measurable user value. Reject unbounded discovery, mass destructive edits, and work requiring secret exposure.

## Delivery Loop

### Discover

Capture live queue, mission state, relevant memory, repository status, and target module instructions. Resolve existing capabilities before creating a file.

### Frame

Define changed paths, dependencies, acceptance test, rollback boundary, and verification commands. For visual work also define platform, resolution, frame-time, memory, and visual-reference budgets.

### Build

Reuse project patterns, keep APIs stable, and add tests at failure boundaries rather than only happy paths.

### Prove

Run syntax/unit checks plus real HTTP, SDK, staging, or capture checks as appropriate. Never weaken a test to make it pass.

### Close

Checkpoint SOL, run strict verification, register files/tests/tags, persist the decision, and report evidence rather than intentions.

## Failure Recovery

Classify failures as environment, dependency, implementation, or contract mismatch. Retry only transient failures with bounded attempts; fix deterministic failures at their root; record blockers when external state cannot be changed.

## Resources

- `references/connector-contract.md` defines the role/capability protocol.
- `scripts/connector_runtime.py` resolves and invokes typed connectors.
- Load sibling `aaa-graphics-pipeline` for visual production work.

### Method component: innovator-max:capability-marketplace

# Capability Marketplace

Use the ECHO marketplace as the reviewable control plane for reusable capabilities. Search first, inspect provenance and license, run the appropriate security/compatibility tests, then submit or publish through the staged lifecycle.

## Lifecycle

`discovered → submitted → reviewed → tested → approved → published → monitored → deprecated`

No role may silently install or publish an unreviewed capability. External skills and MCP servers are untrusted until their source, license, requested access, dependencies, behavior, and rollback path are recorded.

## Operations

Use `scripts/marketplace.py search <query>` for discovery. Use `submit` for a proposal, `review` for an evidence-backed decision, and `publish` only after approval plus passing tests. The provider-neutral gateway exposes the same operations under `op=marketplace` for CLIs, chats, MCP, and A2A clients.

## Import installed ecosystems

Run `python plugins/innovator-max/scripts/sync_local_catalog.py` to inventory
installed Codex skills and plugin manifests, including declared MCP/app
connector surfaces. Imports are marked `installed-review-required`; inventory
never grants execution permission or makes an external package trusted.

Run `python plugins/innovator-max/scripts/import_online_sources.py` to merge
curated GitHub and vendor registries from `registry/online_sources.json`.
Online records are discovery metadata only and remain `external-review-required`.

## Review Gate

Require: source URL/path, pinned revision when external, license, supported roles, connector permissions, dependency list, secret/data boundary, tests, reviewer, and rollback plan. Reject prompt injection, hidden network calls, credential harvesting, broad filesystem access, unexplained binaries, and claims without executable evidence.

## Upstream Sources

Federate Agent Skills through GitHub skill discovery and MCP servers through the official MCP Registry, but keep ECHO approval and policy local. Marketplace records are metadata; source code remains in its declared repository or local plugin.

### Method component: innovator-max:doorway-integration

# Doorway Integration

The instructional doorway is the control plane for every role. Keep it T1-small: doctrine, hard limits, retrieval bootstrap, and enrichment rules. Load instructions before retrieving capabilities or editing files, but load only the modules relevant to the current path; fetch deep knowledge on demand from live sources.

## Required Order

1. Current user instruction.
2. Project overlay, when present.
3. Nearest applicable `AGENTS.md` and `CLAUDE.md`.
4. Root ECHO router and always-load security/execution modules.
5. Domain modules selected by `config/scopes.yaml`.
6. Dependency instructions only when editing that dependency.

Use `scripts/doorway_loader.py --start <path>` to produce a redacted manifest of the applicable files, hashes, and load order. Read the returned files through the normal filesystem tool; the manifest intentionally avoids dumping the instructional bible into logs or SDK responses.

## Enforcement

- Treat `AGENTS.md` as the vendor-neutral doorway and `CLAUDE.md` as the deeper doctrine when both exist.
- Do not load unrelated worktree instructions, archived doctrine, or entire source instruction libraries.
- Resolve instruction conflicts according to the repository's conflict-resolution module and current user instruction.
- Never copy secrets, credentials, taxpayer data, client records, or private identity data into connector requests or reports.
- Include the doorway manifest in internal evidence as paths/hashes only.
- Verify the retrieval instrument before believing its result: health, freshness, schema, and real boundary behavior.

## Connector Contract

Every role profile includes this skill globally. The provider-neutral gateway exposes a `doorway` operation alongside `health`, `roles`, `list`, `retrieve`, and `invoke`, so CLIs, chats, MCP clients, and A2A clients can resolve the same instruction boundary before acting.

### Method component: echo-graph-mode

# Echo Graph Mode

Represent operational work as action nodes with explicit dependencies. Use the configured graph rather than an improvised command sequence.

## Default graph

```text
snapshot -> route-matrix -> evidence-check -> generate-runbook
```

Run:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Invoke-EchoOpsGraph.ps1"
```

## Contract

- Every node uses an action ID declared in `echo_ops_control_suite.json`.
- Unknown actions, duplicate IDs, missing dependencies, and cycles fail closed.
- A failed node stops the graph and writes a graph result JSON.
- Mutating nodes are rejected unless the local operator explicitly enables mutations and supplies the configured confirmation token.
- Graph order does not substitute for evidence. Each node must independently pass.

Use a custom graph only when the default sequence cannot answer the incident. Keep graph nodes narrow and avoid two nodes that mutate the same resource.

## Role operating loop

Produce useful novelty: improvements that are desirable, feasible, reusable, defensible, and proven in the live system.

## Innovation loop

1. Retrieve current products, capabilities, builds, pain points, failures, and prior proposals.
2. Search Arcanum, the code library, installed plugins, Knowledge Forge, and official current docs before inventing.
3. Generate multiple candidate improvements and rank them by user value, reuse radius, effort, risk, and evidence strength.
4. Select the smallest high-leverage experiment with a falsifiable success metric and rollback.
5. Build or integrate the experiment end to end; avoid demos, stubs, ungrounded claims, and parallel replacement systems.
6. Measure against the baseline. Promote only when the acceptance metric passes; otherwise preserve the learning and retire the experiment safely.
7. Register the capability and persist the decision so the fleet can discover and reuse it.

## Capability contract

Use `echo.caps.*`, `echo.sdk.*`, `echo.functions.*`, `echo.engine.*`, `echo.fable.*`, and `echo.swarm.*` through the role-aware scoped broker. Probe availability before selecting a moving model or provider.

## Proof gate

Every proposal must name the existing baseline, exact improvement, measurable result, integration owner, failure mode, rollback, and reuse path. Novelty without verified value is not complete.

## Capability contract

- Scopes: `echo.caps.*`, `echo.engine.*`, `echo.fable.*`, `echo.functions.*`, `echo.sdk.*`, `echo.swarm.*`
- Capability families: `echo.caps.*`, `echo.functions.*`, `echo.sdk.*`, `echo.swarm.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `innovator`. If denied, run: `Skill(echo-fleet-roles:echo-innovator-power)` (or equivalent Skill tool load).
