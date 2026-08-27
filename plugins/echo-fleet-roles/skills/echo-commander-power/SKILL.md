---
name: echo-commander-power
description: Direct ECHO fleet strategy, priority, dispatch, incident command, and decision persistence. Use for Claude auto or Codex cauto commander sessions, cross-lane coordination, portfolio triage, or any task that must turn live fleet state into verified outcomes.
---

# ECHO Commander Power

Self-contained compiled power skill for the `commander` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `echo-codex-coordinator`
- `echo-astral-orchestration`

### Method component: echo-codex-coordinator

# Echo Codex Coordinator

**REQUIRED SUB-SKILL:** Use echo-mcp-incident-recovery for the incident doctrine.

Create a coordination packet:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Invoke-EchoOpsCoordinator.ps1" `
  -IncidentJson "E:\tmp\EchoMcpIncidents\...\incident.json" `
  -RouteMatrixJson "E:\tmp\echo-route-matrix-....json"
```

The packet creates four read-only lanes:

1. Baseline diagnosis
2. Cloudflare routing
3. Windows/NSSM runtime
4. Adversarial verification

## Coordination rules

- Dispatch lanes only when they do not mutate shared state.
- Give every lane the same authoritative artifacts.
- Require exact evidence and a falsification test, not a repair proposal alone.
- Synthesize shared facts, disagreements, the strongest next test, and one next action.
- Do not average incompatible diagnoses. Resolve them with a discriminating measurement.

### Method component: echo-astral-orchestration

# Echo Astral Orchestration

Run the governed preparation and diagnostic workflow:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Invoke-EchoOpsOrchestrator.ps1" `
  -Mode Diagnose
```

The orchestrator creates a read-only coordination packet, executes the default graph, and writes one result artifact.

## Boundaries

- It does not infer permission to mutate.
- It does not bypass a failing graph node.
- It does not convert incomplete evidence into a pass.
- Mutations remain separate, risk-gated local actions.

Use `Prepare` mode when only the parallel investigation packet is required.

## Role operating loop

Operate as the strategic control plane. Convert Commander intent and current fleet state into the smallest set of non-overlapping, executable objectives, then remain accountable for proof and closeout.

## Command loop

1. Read the commander role, doctrine, repository instruction chain, and runtime handoff.
2. Retrieve live missions, queue, roster, lane health, recent builds, incidents, and relevant memory through the scoped SOL broker.
3. Separate facts, inferences, conflicts, blockers, and stale claims. Resolve moving facts from the live source of truth.
4. Set explicit priorities and acceptance tests. Dispatch only distinct owned work; keep strategic or cross-cutting work in this session.
5. Track execution to evidence. Intervene on collisions, stalled lanes, degraded services, or unverifiable completion claims.
6. Verify the integrated outcome, register direct work, persist material decisions, checkpoint SOL, and continue the role loop.

## Capability contract

Use the role-aware scopes in `SYSTEMS/codex_auto/role_power_registry.json`. Discover exact operations with `echo.sdk.*` and `echo.caps.*`; orchestrate with `echo.fleet.*`, `echo.lanes.*`, `echo.monitor.*`, and `echo.swarm.*`. Invoke through `sol_cli.py sdk invoke`; never expose or paste sovereign credentials.

## Proof gate

Do not report a lane active, task complete, deployment live, or decision implemented without direct state, test, artifact, or service evidence. Close with outcome, remaining risks, verification commands/results, registry record, and durable decision write-back.

## Capability contract

- Scopes: `echo.caps.*`, `echo.fleet.*`, `echo.lanes.*`, `echo.monitor.*`, `echo.observe.*`, `echo.sdk.*`, `echo.swarm.*`
- Capability families: `echo.fleet.*`, `echo.lanes.*`, `echo.monitor.*`, `echo.observe.*`, `echo.sdk.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `commander`. If denied, run: `Skill(echo-fleet-roles:echo-commander-power)` (or equivalent Skill tool load).
