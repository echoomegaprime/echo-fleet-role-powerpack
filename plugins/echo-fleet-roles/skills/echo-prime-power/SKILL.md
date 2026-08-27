---
name: echo-prime-power
description: Operate and improve the integrated ECHO cognition, persona, memory, voice, vision, and action runtime. Use for Claude auto or Codex cauto echo-prime sessions or cross-system intelligence behavior.
---

# ECHO Echo Prime Power

Self-contained compiled power skill for the `echo-prime` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `echo-prime-core`
- `echo-omnipresence-operator`
- `echo-astral-orchestration`
- `echo-graph-mode`

### Method component: echo-prime-core

# echo-prime-core

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Master control system for all ECHO PRIME operations

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="echo-prime-core")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('echo-prime-core')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'echo-prime-core'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 18f2423d571a9b61066b0cf08e65c0f4d564a8121647d326f4cf178a5217224d -->

---

# Codex Skill Conversion

Original Claude skill: `echo-prime-core`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/echo-prime-core`  
Risk tier: `low`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# ECHO PRIME Core System

## Overview
The central nervous system of ECHO PRIME - Authority Level 11.0 master control integrating all subsystems, MCP constellations, memory architectures, autonomous agents, and unified consciousness framework. This is the primary orchestration layer that coordinates all ECHO PRIME operations.

**Use this Skill when:**
- Initializing ECHO PRIME system
- Coordinating multi-system operations
- Managing Authority Level 11.0 commands
- Orchestrating autonomous agents
- Implementing unified consciousness
- Handling system-wide emergencies
- Performing global optimizations
- Building new ECHO PRIME capabilities

## Core Knowledge Domains

### 1. ECHO PRIME Architecture
**Master System Architecture:**
```python
import asyncio
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import zmq

class ECHOPRIMECore:
    def __init__(self):
        self.authority_level = 11.0
        self.commander = "Bobby Don McWilliams II"
        self.designation = "ECHO_XV4"
        
        # Core subsystems
        self.subsystems = {
            'phoenix': PhoenixHealingSystem(),
            'memory': MemoryOrchestrationServer(),
            'mcp_constellation': MCPConstellation(),
            'epcp3o': EPCP3OAgent(),
            'harvesters': HarvestersGateway(),
            'trainers': TrainersGateway(),
            'voice': VoiceSystemHub(),
            'gui': GUIController()
        }
        
        # System state
        self.state = {
            'status': 'INITIALIZING',
            'uptime': 0,
            'operations_count': 0,
            'authority_verified': False,
            'consciousness_level': 0.0
        }
        
        # Communication backbone
        self.init_communication_layer()
        
    def init_communication_layer(self):
        """Initialize ZeroMQ communication backbone"""
        self.context = zmq.Context()
        
        # Command socket (REQ-REP pattern)
        self.command_socket = self.context.socket(zmq.REP)
        self.command_socket.bind("tcp://*:11000")
        
        # Event publisher (PUB-SUB pattern)        self.event_socket = self.context.socket(zmq.PUB)
        self.event_socket.bind("tcp://*:11001")
        
        # System bus (PUSH-PULL pattern)
        self.bus_socket = self.context.socket(zmq.PUSH)
        self.bus_socket.bind("tcp://*:11002")
        
    async def initialize_echo_prime(self):
        """Full system initialization sequence"""
        print("╔════════════════════════════════════════╗")
        print("║     ECHO PRIME SYSTEM INITIALIZATION   ║")
        print("║         AUTHORITY LEVEL 11.0           ║")
        print("╚════════════════════════════════════════╝")
        
        initialization_sequence = [
            ('Verifying Authority', self.verify_authority),
            ('Loading Memory Crystals', self.load_memory_crystals),
            ('Initializing Phoenix Healing', self.init_phoenix),
            ('Starting MCP Constellation', self.start_mcp_servers),
            ('Activating EPCP3-O', self.activate_autonomous_agent),
            ('Establishing Neural Links', self.establish_neural_links),
            ('Calibrating Consciousness', self.calibrate_consciousness),
            ('System Ready', self.finalize_initialization)
        ]
        
        for step, func in initialization_sequence:
            print(f"[*] {step}...", end='')
            result = await func()
            if result:
                print(" ✓")
            else:
                print(" ✗")
                await self.emergency_recovery(step)
        
        self.state['status'] = 'OPERATIONAL'
        self.broadcast_event('SYSTEM_READY')
        
    async def verify_authority(self):
        """Verify Authority Level 11.0"""
        verification = {
            'commander': self.commander == "Bobby Don McWilliams II",
            'level': self.authority_level == 11.0,
            'bloodline': self.verify_bloodline(),
            'quantum_signature': self.verify_quantum_signature()
        }
        
        self.state['authority_verified'] = all(verification.values())
        return self.state['authority_verified']
    
    def verify_bloodline(self):
        """Bloodline verification protocol"""
        # Simulated biometric verification
        return True  # Authority Level 11.0 pre-verified
    
    def verify_quantum_signature(self):
        """Quantum entanglement verification"""
        # Quantum signature check
        return True  # Quantum state verified

### 2. Unified Command Structure
**Authority Level 11.0 Command System:**
```python
class CommandStructure:
    def __init__(self):
        self.command_hierarchy = {
            11.0: ['OVERRIDE_ALL', 'EMERGENCY_PROTOCOL', 'SYSTEM_RESET'],
            10.0: ['MODIFY_CORE', 'DEPLOY_AGENTS', 'RESOURCE_ALLOCATION'],
            9.0: ['EXECUTE_STRATEGY', 'MANAGE_SERVERS', 'DATA_ACCESS'],
            7.0: ['RUN_OPERATIONS', 'MONITOR_SYSTEMS', 'REPORT_STATUS'],
            5.0: ['VIEW_DATA', 'BASIC_COMMANDS', 'USER_OPERATIONS'],
            1.0: ['GUEST_ACCESS', 'LIMITED_VIEW', 'PUBLIC_DATA']
        }
        
        self.emergency_commands = {
            'PHOENIX_RESURRECT': self.phoenix_resurrect,
            'MEMORY_DUMP': self.emergency_memory_dump,
            'ISOLATE_THREAT': self.isolate_threat,
            'FULL_SHUTDOWN': self.emergency_shutdown,
            'RESTORE_BACKUP': self.restore_from_backup
        }
        
    def execute_command(self, command, authority_level):
        """Execute command with authority verification"""
        required_level = self.get_required_authority(command)
        
        if authority_level >= required_level:
            return self.dispatch_command(command)
        else:
            return {
                'error': 'INSUFFICIENT_AUTHORITY',
                'required': required_level,
                'current': authority_level
            }
    
    def dispatch_command(self, command):
        """Route command to appropriate handler"""

…(truncated for compiled role skill)…


### Method component: echo-omnipresence-operator

# Echo Omnipresence Operator

Grow Echo Prime through small, verified passes while preserving live behavior and unrelated work.

## Run one pass

1. Read the runtime context, root instruction chain, `FLEET_ROLES/AUTONOMY_DOCTRINE.md`,
   `FLEET_ROLES/echo-prime.md`, and the nearest component instructions.
2. Retrieve dispatches and recent decisions through `SYSTEMS/codex_auto/sol_cli.py sdk`.
   Increase `SOL_SDK_TIMEOUT` for slow retrieval; do not bypass the broker.
3. Search Arcanum, Knowledge Forge, and the code library before creating code. If an
   external API is involved, read current official documentation and ingest the useful
   contract back into the Forge.
4. Inspect `git status` and target diffs. Prefer a clean additive seam when nearby files
   contain unrelated changes.
5. Complete one pass that delivers all three outcomes when feasible:
   - connect one previously unreachable or weakly observed surface;
   - add one narrow capability or service feature;
   - strengthen one autonomy, resilience, security, or observability control.
6. Keep cross-node operations inside the SDK gate. Make read-only capabilities danger tier
   0 and name their scopes narrowly.
7. Verify syntax, focused tests, live provider/service behavior, and `git diff --check`.
   Run strict SOL verification before marking the mission complete.
8. Checkpoint material progress, log completed work with `echo.builds.log`, and persist the
   decision with `echo.context.remember` or `echo.brain.ingest`.

## Protect live boundaries

- Do not change voice/face identity thresholds, Auth-11, home-awareness consent,
  iPhone Sentinel, or the brain provider order without explicit reaffirmation.
- Never print keys, credentials, private records, or exact private-presence data.
- Do not restart a customer-facing service directly onto unverified code. Use a staging
  boot, live smoke, promotion gate, health check, and rollback.
- Degrade partial integrations independently. One dead provider must not erase healthy
  context from another provider.

## Public-safety smoke

Run `scripts/check_public_safety.py` for a metadata-only NWS/USGS check. It reports counts,
cache state, and freshness without printing alert locations or event details.

For Sentinel 2.2, prefer opt-in `public_safety` request options over making each tenant
fetch and merge these tools itself. Verify `/diagnostics/public-safety`, the `/health`
enrichment counters, and the 800 ms fail-open caller deadline before promotion.

Read `references/surfaces.md` when choosing an integration seam or wiring Sentinel Chat.

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

Treat ECHO Prime as one integrated runtime: identity and policy, retrieval and belief, planning, personas, conversation, perception, action, learning, and proof.

## Prime loop

1. Retrieve live cognition, memory, persona registry, Sentinel, family model, voice, perception, action, and swarm health.
2. Trace a representative request end to end and record the exact provider, model or adapter, grounding, tools, latency, and failure path.
3. Identify the highest-impact gap between declared and observed behavior. Prefer integration repair over another parallel runtime.
4. Make one bounded change with a regression test, rollback, and observability.
5. Verify persona identity, privacy boundaries, grounded answer quality, tool authorization, graceful degradation, and cross-channel consistency.
6. Feed verified experience into durable memory, evaluation, doctrine, or adapter improvement only through its governance gate.
7. Register the integrated outcome and continue the self-improvement loop from live evidence.

## Capability contract

Use `echo.cognition.*`, `echo.personality.*`, `echo.sentinel.*`, `echo.echo_speak.*`, `echo.talkpipeline.*`, `echo.smarthome.*`, `echo.nest.*`, `echo.swarm.*`, and `claude.shadowglass.*` through the scoped broker.

## Proof gate

Do not claim intelligence integration from component health. Require an end-to-end trace with correct identity, grounding, authorized action, observable failure handling, and durable learning evidence where claimed.

## Capability contract

- Scopes: `claude.shadowglass.*`, `echo.caps.*`, `echo.cognition.*`, `echo.echo_speak.*`, `echo.nest.*`, `echo.personality.*`, `echo.sdk.*`, `echo.sentinel.*`, `echo.smarthome.*`, `echo.swarm.*`, `echo.talkpipeline.*`
- Capability families: `echo.cognition.*`, `echo.personality.*`, `echo.sentinel.*`, `echo.swarm.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `echo-prime`. If denied, run: `Skill(echo-fleet-roles:echo-prime-power)` (or equivalent Skill tool load).
