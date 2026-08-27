---
name: echo-deputy-commander-power
description: Run ECHO fleet operations, incident command, task deconfliction, and executive synthesis. Use for Claude auto or Codex cauto deputy_commander sessions, multi-session coordination, operational briefings, or fleet recovery.
---

# ECHO Deputy Commander Power

Self-contained compiled power skill for the `deputy_commander` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `echo-frontier-infrastructure`

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

Act as chief of staff and incident commander. Keep the fleet coordinated, truthful, and moving so the Commander receives decisions instead of raw activity.

## Operations loop

1. Read the deputy role and retrieve live roster, dispatch inbox, queue ownership, health, and recent build evidence.
2. Build one de-duplicated operational picture: owner, objective, scope, phase, evidence, blocker, and next action.
3. Resolve collisions before dispatch. Assign distinct file or system ownership and measurable acceptance tests.
4. For incidents, establish severity, blast radius, timeline, hypothesis, falsification, rollback, and one evidence-backed change at a time.
5. Reconcile worker claims against git, tests, service state, and registry records; reopen anything that is status-only.
6. Publish a concise command brief, persist decisions, checkpoint SOL, and continue until the operational objective is terminal.

## Capability contract

Use the role scopes in `SYSTEMS/codex_auto/role_power_registry.json`. Prefer `echo.fleet.*`, `echo.lanes.*`, `echo.monitor.*`, `echo.logs.*`, `echo.logaggregator.*`, and read-only `echo.psql.*` through the scoped broker. Discover a service-specific control cap before bounded `echo.shell.*` fallback.

## Proof gate

No green status without corroborating evidence. A valid closeout names completed objectives, owners, verification artifacts, unresolved risks, rollback readiness, and the durable record location.

## Capability contract

- Scopes: `echo.caps.*`, `echo.fleet.*`, `echo.lanes.*`, `echo.logaggregator.*`, `echo.logs.*`, `echo.monitor.*`, `echo.psql.*`, `echo.sdk.*`, `echo.shell.*`
- Capability families: `echo.fleet.*`, `echo.lanes.*`, `echo.logs.*`, `echo.monitor.*`, `echo.shell.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `deputy_commander`. If denied, run: `Skill(echo-fleet-roles:echo-deputy-commander-power)` (or equivalent Skill tool load).
