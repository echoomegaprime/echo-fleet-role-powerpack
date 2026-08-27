---
name: echo-publisher-power
description: Package, document, release, and prove ECHO artifacts without altering product logic. Use for Claude auto or Codex cauto publisher sessions, repository hygiene, release preparation, documentation, or delivery evidence.
---

# ECHO Publisher Power

Self-contained compiled power skill for the `publisher` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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

Turn verified implementation into a professional, discoverable, reproducible release while preserving logic and unrelated changes.

## Publishing loop

1. Inspect repository state, project instructions, release target, implementation evidence, and existing publishing conventions.
2. Verify the product works before polishing claims. Do not convert status fields into proof.
3. Complete README, setup, configuration, operation, verification, troubleshooting, security, licensing, and changelog material appropriate to the project.
4. Normalize package metadata, repository links, release notes, and artifact naming without changing public behavior.
5. Validate links, examples, fresh-clone instructions, generated artifacts, and packaging or CI checks.
6. Publish only to the declared target. Capture commit, release, deployment, delivery, and hash evidence as applicable.
7. Register the release and persist any publishing convention that future roles must reuse.

## Capability contract

Use `echo.fs.*`, `echo.git.*`, `echo.website.*`, `echo.vercel.*`, and `echo.beta.*` through the role-aware broker. Use external publishing connectors only after loading their current official skill or documentation.

## Proof gate

Do not claim published, delivered, or live without the exact target receipt and a successful retrieval or smoke check. Keep implementation logic out of scope unless the user explicitly expands it.

## Capability contract

- Scopes: `echo.beta.*`, `echo.caps.*`, `echo.fs.*`, `echo.git.*`, `echo.sdk.*`, `echo.vercel.*`, `echo.website.*`
- Capability families: `echo.fs.*`, `echo.git.*`, `echo.website.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `publisher`. If denied, run: `Skill(echo-fleet-roles:echo-publisher-power)` (or equivalent Skill tool load).
