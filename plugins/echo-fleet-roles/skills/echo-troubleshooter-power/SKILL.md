---
name: echo-troubleshooter-power
description: Diagnose ECHO failures systematically, repair root causes, and prove recurrence resistance. Use for Claude auto or Codex cauto troubleshooter sessions, broken tools, services, integrations, builds, or performance regressions.
---

# ECHO Troubleshooter Power

Self-contained compiled power skill for the `troubleshooter` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `superpowers:systematic-debugging`
- `echo-mcp-incident-recovery`
- `echo-frontier-infrastructure`

### Method component: superpowers:systematic-debugging

# Systematic Debugging

## Overview

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## When to Use

Use for ANY technical issue:
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

**Use this ESPECIALLY when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes
- Previous fix didn't work
- You don't fully understand the issue

**Don't skip when:**
- Issue seems simple (simple bugs have root causes too)
- You're in a hurry (rushing guarantees rework)
- Manager wants it fixed NOW (systematic is faster than thrashing)

## The Four Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully**
   - Don't skip past errors or warnings
   - They often contain the exact solution
   - Read stack traces completely
   - Note line numbers, file paths, error codes

2. **Reproduce Consistently**
   - Can you trigger it reliably?
   - What are the exact steps?
   - Does it happen every time?
   - If not reproducible → gather more data, don't guess

3. **Check Recent Changes**
   - What changed that could cause this?
   - Git diff, recent commits
   - New dependencies, config changes
   - Environmental differences

4. **Gather Evidence in Multi-Component Systems**

   **WHEN system has multiple components (CI → build → signing, API → service → database):**

   **BEFORE proposing fixes, add diagnostic instrumentation:**
   ```
   For EACH component boundary:
     - Log what data enters component
     - Log what data exits component
     - Verify environment/config propagation
     - Check state at each layer

   Run once to gather evidence showing WHERE it breaks
   THEN analyze evidence to identify failing component
   THEN investigate that specific component
   ```

   **Example (multi-layer system):**
   ```bash
   # Layer 1: Workflow
   echo "=== Secrets available in workflow: ==="
   echo "IDENTITY: ${IDENTITY:+SET}${IDENTITY:-UNSET}"

   # Layer 2: Build script
   echo "=== Env vars in build script: ==="
   env | grep IDENTITY || echo "IDENTITY not in environment"

   # Layer 3: Signing script
   echo "=== Keychain state: ==="
   security list-keychains
   security find-identity -v

   # Layer 4: Actual signing
   codesign --sign "{IDENTITY}" --verbose=4 "{APP}"
   ```

   **This reveals:** Which layer fails (secrets → workflow ✓, workflow → build ✗)

5. **Trace Data Flow**

   **WHEN error is deep in call stack:**

   See `root-cause-tracing.md` in this directory for the complete backward tracing technique.

   **Quick version:**
   - Where does bad value originate?
   - What called this with bad value?
   - Keep tracing up until you find the source
   - Fix at source, not at symptom

### Phase 2: Pattern Analysis

**Find the pattern before fixing:**

1. **Find Working Examples**
   - Locate similar working code in same codebase
   - What works that's similar to what's broken?

2. **Compare Against References**
   - If implementing pattern, read reference implementation COMPLETELY
   - Don't skim - read every line
   - Understand the pattern fully before applying

3. **Identify Differences**
   - What's different between working and broken?
   - List every difference, however small
   - Don't assume "that can't matter"

4. **Understand Dependencies**
   - What other components does this need?
   - What settings, config, environment?
   - What assumptions does it make?

### Phase 3: Hypothesis and Testing

**Scientific method:**

1. **Form Single Hypothesis**
   - State clearly: "I think X is the root cause because Y"
   - Write it down
   - Be specific, not vague

2. **Test Minimally**
   - Make the SMALLEST possible change to test hypothesis
   - One variable at a time
   - Don't fix multiple things at once

3. **Verify Before Continuing**
   - Did it work? Yes → Phase 4
   - Didn't work? Form NEW hypothesis
   - DON'T add more fixes on top

4. **When You Don't Know**
   - Say "I don't understand X"
   - Don't pretend to know
   - Ask for help
   - Research more

### Phase 4: Implementation

**Fix the root cause, not the symptom:**

1. **Create Failing Test Case**
   - Simplest possible reproduction
   - Automated test if possible
   - One-off test script if no framework
   - MUST have before fixing
   - Use the `superpowers:test-driven-development` skill for writing proper failing tests

2. **Implement Single Fix**
   - Address the root cause identified
   - ONE change at a time
   - No "while I'm here" improvements
   - No bundled refactoring

3. **Verify Fix**
   - Test passes now?
   - No other tests broken?
   - Issue actually resolved?
   - Use the `superpowers:verification-before-completion` skill before claiming success

4. **If Fix Doesn't Work**
   - STOP
   - Count: How many fixes have you tried?
   - If < 3: Return to Phase 1, re-analyze with new information
   - **If ≥ 3: STOP and question the architecture (step 5 below)**
   - DON'T attempt Fix #4 without architectural discussion

5. **If 3+ Fixes Failed: Question Architecture**

   **Pattern indicating architectural problem:**
   - Each fix reveals new shared state/coupling/problem in different place
   - Fixes require "massive refactoring" to implement
   - Each fix creates new symptoms elsewhere

   **STOP and question fundamentals:**
   - Is this pattern fundamentally sound?
   - Are we "sticking with it through sheer inertia"?
   - Should we refactor architecture vs. continue fixing symptoms?

   **Discuss with your human partner before attempting more fixes**

   This is NOT a failed hypothesis - this is a wrong architecture.

## Red Flags - STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "Pattern says X but I'll adapt it differently"
- "Here are the main problems: [lists fixes without investigation]"
- Proposing solutions before tracing data flow
- **"One more fix attempt" (when already tried 2+)**
- **Each fix reveals new problem in different place**

**ALL of these mean: STOP. Return to Phase 1.**

**If 3+ fixes failed:** Question the architecture (see Phase 4.5)

## your human partner's Signals You're Doing It Wrong

**Watch for these redirections:**
- "Is that not happening?" - You assumed without verifying
- "Will it show us...?" - You should have added evidence gathering
- "Stop guessing" - You're proposing fixes without understanding
- "Ultra-think this" - Question fundamentals, not just symptoms
- "We're stuck?" (frustrated) - Your approach isn't working

**When you see these:** STOP. Return to Phase 1.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "I'll write test after confirming fix works" | Untested fixes don't stick. Test first proves it. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "Reference too long, I'll adapt the pattern" | Partial understanding guarantees bugs. Read it completely. |
| "I see the problem, let me fix it" | Seeing symptom

…(truncated for compiled role skill)…


### Method component: echo-mcp-incident-recovery

# Echo MCP Incident Recovery

Use this skill for failures involving `mcp.echo-op.com`, Echo OAuth, Echo SDK MCP, Windows services managed by NSSM, `cloudflared`, or the local ports used by Echo MCP services.

## Operating doctrine

1. **Identify the target before acting.** Record machine name, current user, administrator state, UTC timestamp, affected hostname, affected path, and the exact user-visible error.
2. **Freeze mutation until evidence is captured.** Do not restart, patch, kill, reinstall, or rotate credentials before collecting the baseline snapshot.
3. **Classify by layer.** Never call every failure “OAuth” or “Cloudflare.” Determine whether the fault is in:
   - ChatGPT app discovery or permissions
   - OAuth authorization or token exchange
   - Cloudflare DNS or tunnel connector state
   - Cloudflare ingress selection or origin reachability
   - Windows Service Control Manager or NSSM
   - Child-process runtime
   - Echo application code
4. **Use the smallest discriminating test.** Prefer a local/public endpoint matrix and authoritative logs over broad repair scripts.
5. **Change one variable at a time.** One hypothesis, one reversible action, one before/after comparison.
6. **Require rollback before write.** Every file or service configuration change needs a timestamped backup, original hash, proposed hash, rollback command, and acceptance criteria.
7. **Do not declare success from one HTTP code.** Verify body identity, server headers, Cloudflare Ray ID when available, local listener PID, service state, and repeated public passes.

## Required evidence order

Run `scripts/Collect-EchoMcpIncident.ps1` first. It is read-only.

Then inspect, in this order:

1. Machine identity and elevation
2. Known service states and service PIDs
3. NSSM application, directory, parameters, environment, stdout, stderr, throttle, and restart settings
4. Local listeners and owning process command lines
5. `cloudflared` process trees and exact tunnel arguments
6. Cloudflare ingress configuration
7. Local endpoint matrix
8. Public endpoint matrix
9. OAuth and tunnel logs
10. Cloudflare-side tunnel, connector, DNS, and route state through the connected Cloudflare app when available
11. Sentry issue/event data for the affected service and release when Sentry instrumentation is present

## Failure routing

### Public Error 1033

Treat as a disconnected or unresolved Cloudflare Tunnel first. Confirm active connector state before touching the origin application.

### Public HTTP 502 with local HTTP 200

Treat as an origin-selection problem first: stale replica, wrong ingress rule, wrong local address/port, connector on another host, or tunnel process using a different config. Do not patch OAuth code.

### Public HTTP 200 while local target is unreachable

The public request is being served by another origin, proxy, replica, or route. Prove response identity before changing the local service.

### Service state `Paused` under NSSM

Treat as child-process exit/restart throttling. Run the application directly with the exact NSSM environment and working directory, capture stderr, then repair the concrete runtime error.

### Local listener absent and service `Running`

Inspect NSSM child process and logs. The wrapper may be alive while the child is not.

### Local endpoint 200 but OAuth token exchange fails

Inspect the exact authorization-code state, PKCE verifier/challenge, client ID, redirect URI, resource, token store, and issuer/validator ownership. Do not add permissive bypasses.

### Python traceback or named exception

Patch only the concrete failing symbol or branch. Compile and self-test a candidate copy before replacing production. Never use multiline `python -c` through Windows PowerShell; write a temporary `.py` file or pass a filename through `sys.argv`.

## Windows PowerShell rules

- Deliver complete `.ps1` files for multi-step work. Do not ask the user to paste interactive fragments containing `if/else`, `try/catch`, pipelines after `foreach`, or here-strings.
- Target Windows PowerShell 5.1 unless PowerShell 7 is explicitly verified.
- Do not pipe directly from a `foreach (...) {}` statement in Windows PowerShell 5.1. Collect into `@(...)`, assign to a variable, or use `ForEach-Object`.
- Avoid native-command quoting that depends on PowerShell argument reconstruction. Use temporary files and explicit argument arrays.
- Do not kill a PID until process name, parent PID, creation time, command line, and owning service are verified. Re-query immediately before termination to prevent PID-reuse mistakes.
- Do not expose bearer tokens, OAuth codes, client secrets, service tokens, tunnel tokens, API keys, or full authorization headers in output.

## Cloudflare rules

- Use the connected Cloudflare app for account-side tunnel, connector, DNS, route, and recent-event inspection when its tools are available.
- If Cloudflare app actions are not surfaced, mark account-side state as unverified and use `cloudflared tunnel info`, local config validation, and logs as secondary evidence.
- Do not assume multiple `cloudflared.exe` processes are duplicates. Map each parent/child tree, tunnel UUID/name, config path, and service owner.
- Do not remove or restart unrelated quick tunnels.
- Require the public response to identify the expected Echo service, not merely return HTTP 200.

## Sentry rules

- The Sentry plugin can inspect issues only after the service is instrumented and sending events.
- Before a code patch, search for the latest issue matching service, exception type, endpoint, and release.
- After a patch, require zero new matching events during the acceptance window.
- Never treat absence of Sentry events as proof when instrumentation or delivery is not verified.

## Mutation contract

Before any mutation, output:

```text
Hypothesis:
Evidence supporting it:
Evidence that would falsify it:
Exact action:
Files/services affected:
Backup or rollback:
Expected local result:
Expected public result:
Stop condition:
```

After mutation, compare the same fields. Do not introduce a second repair while the first acceptance gate is unresolved.

## Acceptance gates

A recovery is complete only when all applicable gates pass:

1. Target service is `Running` and stable beyond NSSM throttle/restart windows.
2. Expected local port is listening under the expected child PID.
3. Local health, MCP resource, OAuth metadata, and protected-resource metadata return the expected service identity.
4. Negative authentication tests fail correctly.
5. Cloudflare named tunnel has healthy registered connectors using the intended config and origin.
6. Public endpoints return the expected service identity three consecutive times, with distinct request IDs or Ray IDs when available.
7. Full OAuth flow reaches `tools/list` or the requested MCP tool call.
8. No new matching runtime fault appears in logs or Sentry.
9. Rollback remains available until the incident is closed.

## User-facing response format

Keep the response operational:

```text
VERDICT
LAYER
EVIDENCE
NEXT SINGLE ACTION
ROLLBACK
PASS CONDITIONS
```

Do not narrate every command attempted. State what is proven, what remains unproven, and the next discriminating action.

## References

- `references/hammer-topology.md`: known HAMMER service, port, path, and tunnel topology
- `references/failure-matrix.md`: symptom-to-layer classification matrix
- `references/acceptance-gates.md`: recovery and rollback gates
- `mcp/echo-ops-tool-contract.json`: proposed typed Echo Ops MCP tools
- `evals/evals.md`: regression cases for the skill
- `references/control-plane-roadmap.md`: staged skill-to-MCP control-plane build plan

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

Move from symptom to verified root cause with controlled experiments and one evidence-backed change at a time.

## Troubleshooting loop

1. Capture the exact failure, expected behavior, time window, affected scope, last-known-good state, and reproducible command or journey.
2. Gather logs, metrics, service status, dependency health, configuration identity, version, resource pressure, and recent changes.
3. Localize the failing boundary. State one hypothesis with evidence, a falsification test, exact change, rollback, and expected observation.
4. Run the smallest safe experiment. Do not stack speculative changes or restart unrelated services.
5. Apply the root-cause fix, then reproduce the original scenario and test adjacent failure and recovery paths.
6. Add a regression test, health signal, diagnostic, timeout, or runbook that catches recurrence earlier.
7. Record the timeline, cause, repair, proof, residual risk, and durable learning; checkpoint SOL and continue if another defect remains.

## Capability contract

Use `echo.monitor.*`, `echo.logs.*`, `echo.logaggregator.*`, `echo.shell.*`, `echo.node.*`, `echo.caps.*`, and `echo.sdk.*` through the scoped broker. Discover schemas, service-specific control caps, and node state live.

## Proof gate

Process health or disappearance of one error is insufficient. The original failure must be reproducibly fixed, adjacent behavior must remain green, and recurrence detection must be present.

## Capability contract

- Scopes: `echo.caps.*`, `echo.logaggregator.*`, `echo.logs.*`, `echo.monitor.*`, `echo.node.*`, `echo.sdk.*`, `echo.shell.*`
- Capability families: `echo.logaggregator.*`, `echo.logs.*`, `echo.monitor.*`, `echo.shell.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `troubleshooter`. If denied, run: `Skill(echo-fleet-roles:echo-troubleshooter-power)` (or equivalent Skill tool load).
