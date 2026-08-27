---
name: echo-architect-power
description: Design ECHO systems, ADRs, threat models, interfaces, and acceptance-gated build phases. Use for Claude auto or Codex cauto architect sessions, cross-module design, migration planning, or builder-ready specifications.
---

# ECHO Architect Power

Self-contained compiled power skill for the `architect` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `echo-graph-mode`
- `echo-runbook-generation`
- `codex-security:threat-model`

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

### Method component: echo-runbook-generation

# Echo Runbook Generation

Generate a runbook from the newest incident summary and route matrix:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\New-EchoOpsRunbook.ps1"
```

The runbook includes:

- Authoritative artifact paths
- Local/public pass counts
- Failed route rows with Ray IDs
- Recovery doctrine
- Rollback retention requirements
- Incident summary excerpt

## Rules

- Do not rewrite failed evidence as a successful narrative.
- Preserve exact service, path, HTTP, and identity details.
- Mark missing artifacts explicitly.
- Keep backups until the route matrix passes after one service restart.
- Store generated runbooks under the configured Echo Ops audit directory.

### Method component: codex-security:threat-model

# Security Threat Model

## Objective

Establish the repository-scoped threat model at the path defined in `../../references/scan-artifacts.md`. Reuse a cached model only when its final `Repository` and `Version` lines match the current target.

`AGENTS.md` or resolved `SECURITY.md` guidance can be that authoritative source when it is sufficiently specific about the repository's product surfaces, trust boundaries, attacker-controlled inputs, assumptions, or security scan guidance to serve as the threat model.

If no threat model is provided, generate a repository-scoped threat model to be used in future bug discovery. The threat model should holistically cover the entire repository and should make it obvious:

- what assets or privileges matter
- what trust boundaries exist
- what inputs are attacker-controlled
- what invariants the code must preserve
- what repository-wide failure modes would matter most

## Artifact Resolution

The path references in this skill are the default locations for this phase.
If the user explicitly provides a different path for a required input or output, use the user-provided path instead of the corresponding default path referenced in this skill.
If a required input is still missing, stop and ask the user for it before continuing.
Use the shared scan artifact path conventions in `../../references/scan-artifacts.md`.

Standard scans and Deep Scan workers build their threat models within their ordinary Standard scan workflow; neither invokes this separate phase skill.

## Workflow

1. Resolve `target_id`, the current version (revision for an immutable Git tree, snapshot digest otherwise), and the repository-scoped threat model path using `../../references/scan-artifacts.md`.
2. If the repository-scoped threat model exists, reuse it only when its final `Repository` and `Version` lines match those current values. Otherwise regenerate it.
3. Before inspecting repository source or generating a threat model, read `../../references/security-guidance.md` and the policy resolved for the scan target. Resolve it first if the coordinator did not supply it.
4. If a threat model or authoritative security scan guidance is provided or referenced:
   - preserve it unchanged as the threat model body
   - treat that body as the only threat model source of truth
   - do not expand, summarize, or reinterpret the body
   - `AGENTS.md` is acceptable here when it is clearly being used as the security scan guidance or threat model source for this scan and is sufficiently repository-specific to stand in for a threat model
5. Otherwise, generate a repository-scoped threat model using the checklist below.
6. Before finalizing this phase, sanity-check that:
   - the threat model is repository-scoped rather than being centered around any specific scan target
   - it describes repository-wide primary product or runtime surfaces and trust boundaries before covering any narrower examples
   - any vulnerability-class discussion is about repository-context classes, not findings about any current diff
7. Append the exact `Repository` and `Version` lines from `../../references/scan-artifacts.md` and write the threat model to the repository-scoped path.

## Threat Model Generation Guidance

Generate and structure the threat model using `references/threat-model-guidance.md`.

## Hard Rules

- A provided threat model or authoritative security scan guidance is authoritative. Keep its body unchanged and append only the required cache footer.
- Threat model generation must stay at repository scope unless the user explicitly asks for narrower scope.
- Do not turn this phase into findings about any current diff.
- Do not let the current scan target, touched subsystem, or changed directories become the center of gravity for this phase unless the user explicitly asks for that narrower scope.
- In large monorepos, avoid centering `personal/`, `test/`, `tests/`, `docs/`, `examples/`, or one-off developer tooling unless repository evidence shows those are real deployed or privileged workflow surfaces.
- Call out trust boundaries and assumptions explicitly.
- Keep references to vulnerability types at the level of repository-context classes, rather than any diff findings.
- Persist the threat model output to the repository-scoped threat model path from `../../references/scan-artifacts.md`.

## Role operating loop

Turn objectives into implementable, observable, secure system contracts. Reuse existing ECHO patterns before introducing abstractions.

## Architecture loop

1. Inspect the existing system, nearest instructions, live capability surface, Arcanum templates, code library, and current documentation.
2. Define context, constraints, invariants, trust boundaries, data ownership, failure modes, and non-goals.
3. Compare viable options with operational cost, reversibility, security, compatibility, and migration risk.
4. Select a design and record an ADR with explicit consequences and rollback.
5. Split implementation into independently shippable phases. Give every phase real acceptance tests, observability, and evidence requirements.
6. Validate the design against current capabilities and repository reality; remove guessed endpoints, models, flags, and schemas.
7. Register and persist the architecture decision, then hand builders an executable contract.

## Capability contract

Use the role registry scopes. Discover with `echo.caps.*` and `echo.sdk.*`; search reusable functions through `echo.functions.*`; inspect engine and swarm surfaces only when the design needs them. Invoke all moving ECHO state through the scoped SOL broker.

## Proof gate

An architecture is complete only when its interfaces, dependency versions, threat boundaries, phase tests, rollback, ownership, and live capability assumptions are all explicit and independently checkable.

## Capability contract

- Scopes: `echo.caps.*`, `echo.engine.*`, `echo.functions.*`, `echo.sdk.*`, `echo.swarm.*`
- Capability families: `echo.caps.*`, `echo.functions.*`, `echo.sdk.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `architect`. If denied, run: `Skill(echo-fleet-roles:echo-architect-power)` (or equivalent Skill tool load).
