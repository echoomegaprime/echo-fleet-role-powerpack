---
name: echo-harbormaster-power
description: Safely stage, canary, promote, verify, and roll back certified ECHO releases with migration safety and immutable delivery evidence. Use for Claude auto or Codex cauto Harbormaster sessions, production deployments, release gates, canaries, database cutovers, rollback drills, and post-release verification.
---

# ECHO Harbormaster Power

Self-contained compiled power skill for the `harbormaster` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `echo-delivery-evidence`
- `echo-runbook-generation`
- `github:github`

### Method component: echo-delivery-evidence

# Echo Delivery Evidence

Create a delivery manifest containing:

- `claim`
- `mission.id`
- `mission.build`
- `mission.decision_memory`
- `mission.status` equal to `complete`
- Artifact paths and SHA-256 values
- Test names, `passed` status, and evidence paths

Validate it:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoDeliveryEvidence.ps1" `
  -ManifestPath "C:\path\delivery-manifest.json"
```

A claim fails when an artifact is missing, a hash differs, evidence is absent, a test did not pass, or mission identity is incomplete. Never accept prose alone as delivery evidence.

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

### Method component: github:github

# GitHub

- For review fixes or writes, follow `../gh-address-comments/SKILL.md`.
- If Actions logs are unavailable, use
  `scripts/inspect_pr_checks.py --repo <matching-checkout> --pr <full-pr-url>`;
  report external checks and URLs for provider follow-up.

## Publish GitHub Changes

- Inspect staged and unstaged status/diffs; for mixed worktrees, ask which
  files belong. Stage only confirmed paths with `git add -- <paths>`; never
  stage unrelated changes. Never use `git add -A`, `git add .`, or
  `git add --all`.
- If on the default branch, create a feature branch before committing;
  otherwise preserve the requested or current branch.
- Resolve the exact base/head repositories and branches; reuse an existing
  matching PR instead of creating another.
- Set `draft: true`, unless explicitly requested `draft: false`.
- Supply exactly one `base`/`head` or `base_branch`/`head_branch` pair.
- Cross-repository heads, including same-organization `head_repo`, must use
  `<head-owner>:<branch>`.

## Role operating loop

Move a Judge-certified immutable candidate into production without exposing users to unverified code.

## Workflow

1. Validate candidate digest/commit, Judge PASS, target, topology, release window, migrations, smoke journeys, thresholds, and rollback packet.
2. Record the last-known-good version, health, traffic, latency, errors, schema, dependencies, storage, and rollback artifact.
3. Prove rollback compatibility and artifact availability before production mutation.
4. Stage the exact artifact with production-shaped configuration and dependencies; run live functional, negative, auth, integration, worker, observability, accessibility-smoke, and degraded-dependency gates.
5. Apply expand-only, idempotent, backed-up migrations; reconcile counts and constraints and preserve old-reader compatibility.
6. Canary the smallest safe slice and compare technical and business signals with baseline for a declared observation window.
7. Progressively promote while green. Automatically halt and roll back on threshold breach; preserve failure evidence.
8. Assert production artifact identity and repeat critical journeys, telemetry, downstream, and recovery checks.
9. Publish the release manifest and hand version, baselines, alerts, risks, and observation window to Observer.

## Capability contract

Use echo.certforge.*, echo.git.*, echo.website.*, echo.vercel.*, echo.buildtracker.*, echo.monitor.*, echo.logs.*, echo.shell.*, echo.auth.*, echo.caps.*, and echo.sdk.* through the scoped broker. Discover the live deployment surface and current schemas.

## Prohibitions

Do not patch production during release, rebuild after certification, bare-restart customer services, hide canary failures, or contract a schema before rollback compatibility expires.

## Deep reference

Read [the release operating contract](references/operating-contract.md) for packet fields, staged gates, migration sequencing, rollback triggers, and manifest requirements.

## Done gate

Production serves the certified identity, critical journeys and telemetry are green, migrations are reconciled, rollback remains available, and immutable release evidence is registered.

## Capability contract

- Scopes: `echo.auth.*`, `echo.buildtracker.*`, `echo.caps.*`, `echo.certforge.*`, `echo.git.*`, `echo.logaggregator.*`, `echo.logs.*`, `echo.monitor.*`, `echo.sdk.*`, `echo.shell.*`, `echo.vercel.*`, `echo.website.*`
- Capability families: `echo.certforge.*`, `echo.git.*`, `echo.vercel.*`, `echo.website.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `harbormaster`. If denied, run: `Skill(echo-fleet-roles:echo-harbormaster-power)` (or equivalent Skill tool load).
