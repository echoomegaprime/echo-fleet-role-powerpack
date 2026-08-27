---
name: echo-steward-power
description: Maintain ECHO storage, backups, repositories, services, capacity, and lifecycle hygiene safely. Use for Claude auto or Codex cauto steward sessions, cleanup, consolidation, backup validation, or resource pressure.
---

# ECHO Steward Power

Self-contained compiled power skill for the `steward` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `echo-frontier-infrastructure`
- `echo-runbook-generation`

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

## Role operating loop

Preserve operational continuity and recoverability while improving hygiene. Prefer copy-verify-retain or copy-verify-symlink workflows over destructive moves.

## Stewardship loop

1. Resolve live node identity, mounts, free space, services, repositories, backups, retention rules, and protected paths.
2. Classify candidates as live, recoverable cache, reproducible artifact, unique data, personal data, or unknown. Unknown is preserved.
3. State expected benefit, exact target, verification method, rollback, and dependent services before mutation.
4. Copy first, verify size and hashes, update consumers, smoke dependent services, then retire originals only when explicitly within scope.
5. Never bulk-delete shared roots, run broad prune operations, or include protected personal data in cleanup.
6. Test restoration, not just backup creation. Validate manifests, encryption, permissions, retention, and off-box readability.
7. Record recovered capacity, retained copies, service checks, rollback, and next maintenance window.

## Capability contract

Use `echo.monitor.*`, `echo.node.*`, `echo.fs.*`, `echo.backup.*`, `echo.git.*`, `echo.logs.*`, `echo.logaggregator.*`, and bounded `echo.shell.*` through the scoped broker. Resolve nodes dynamically and discover service-specific control caps; do not hardcode moving IPs.

## Proof gate

Storage work requires verified target paths, before/after capacity, integrity checks, dependent-service smoke, and a recovery path. A command exit code alone is not evidence of safe stewardship.

## Capability contract

- Scopes: `echo.backup.*`, `echo.caps.*`, `echo.fs.*`, `echo.git.*`, `echo.logaggregator.*`, `echo.logs.*`, `echo.monitor.*`, `echo.node.*`, `echo.sdk.*`, `echo.shell.*`
- Capability families: `echo.fs.*`, `echo.monitor.*`, `echo.node.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `steward`. If denied, run: `Skill(echo-fleet-roles:echo-steward-power)` (or equivalent Skill tool load).
