---
name: echo-quartermaster-power
description: Equip ECHO roles with validated tools, MCP servers, skills, plugins, and capability routes. Use for Claude auto or Codex cauto quartermaster sessions, tool inventory, missing capabilities, plugin installation, or fleet enablement.
---

# ECHO Quartermaster Power

Self-contained compiled power skill for the `quartermaster` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `skills-gateway`
- `mcp-constellation`
- `mcp-builder`
- `plugin-creator`
- `skill-creator`

### Method component: skills-gateway

# skills-gateway

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Skills MCP Server for ECHO OMEGA PRIME

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="skills-gateway")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('skills-gateway')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'skills-gateway'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 2a8f9c65a0727e10be8a9597326e04fc938f702358ee64fa731cffe3795e0f93 -->

---

# Codex Skill Conversion

Original Claude skill: `skills-gateway`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/skills-gateway`  
Risk tier: `high`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Skills Gateway MCP Server

## Tools Available

| Tool | Description |
|------|-------------|
| `skills_health` | Check gateway health and integration status |
| `skills_list` | List skills by category |
| `skills_search` | Search skills by keyword |
| `skills_get` | Get full skill details and content |
| `skills_recommend` | AI-powered skill recommendations |
| `skills_integrations` | Check all integration statuses |
| `skills_reload` | Reload skills from disk |

## Skill Categories

- `voice_tts` - Voice/TTS skills
- `memory` - Memory/Crystal skills
- `error_handling` - GS343/Phoenix skills
- `cluster_swarm` - X1200/Distributed skills
- `ai_inference` - LLM/AI skills
- `agents` - Autonomous agent skills
- `development` - Python/FastAPI/Electron
- `echo_prime` - Core ECHO systems
- `infrastructure` - MCP/Gateway skills
- `gui` - Dashboard/UI skills
- `collectibles` - Grading/Pricing skills
- `trading` - Crypto/GameLoop skills
- `security` - Prometheus/Vault skills
- `forge` - Daedalus/Hephaestion
- `specialty` - Other skills

## Usage

```python
# Search for skills
result = await skills_search({"query": "voice"})

# Get skill content
skill = await skills_get({"name": "elevenlabs-manual"})

# Get recommendations for a task
recs = await skills_recommend({"task": "analyze comic book images"})
```

## Integrations

| System | Purpose |
|--------|---------|
| GS343 | Error analysis for skill operations |
| Phoenix | Auto-healing on failures |
| X1200 | Swarm-powered recommendations |
| Prometheus | Security validation |
| Crystal | Skill caching |

## Skill Directories Scanned

- `X:/ECHO_PRIME/SKILLS`
- `C:/Users/bobmc/.claude/commands`
- `O:/ECHO_OMEGA_PRIME/.claude/commands`
- `I:/CLAUDE SKILLS`

**Location:** `X:/ECHO_PRIME/MLS/PRODUCTION/GATEWAYS/SKILLS_GATEWAY/`
**Port:** 8850

**Authority 11.0 | Skills Gateway**

### Method component: mcp-constellation

# mcp-constellation

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Orchestrate 15+ MCP servers for distributed AI operations

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="mcp-constellation")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('mcp-constellation')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'mcp-constellation'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: a96a69f87f69dfe925bccf0cc57c52573d650878109fd0a39860df5e8432a1d1 -->

---

# Codex Skill Conversion

Original Claude skill: `mcp-constellation`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/mcp-constellation`  
Risk tier: `high`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# MCP Constellation Control Skill

## Overview
Manages ECHO_PRIME's constellation of 15+ Model Context Protocol (MCP) servers providing capabilities from network security to AI gateway access. Provides health monitoring, restart procedures, diagnostics, and integration patterns for the entire MCP ecosystem.

**Use this Skill when:**
- User asks about MCP servers or capabilities
- Server health checks needed
- MCP tools not responding
- Integration patterns required
- Capability discovery needed
- Server restart/recovery needed

## Active MCP Servers (15+)

### 1. Network Guardian
**Purpose:** Network scanning, monitoring, blocking
**Tools:**
- `netguard_health` - Server health check
- `netguard_scan` - Scan network/target
- `netguard_monitor` - Monitor network activity
- `netguard_block` - Block target

### 2. Healing Orchestrator
**Purpose:** System healing and optimization
**Tools:**
- `healorch_health` - Health check
- `healorch_heal` - Heal system/target
- `healorch_diagnostics` - Get diagnostics
- `healorch_optimize` - Optimize target

### 3. Master Orchestrator Hub
**Purpose:** Multi-model routing and consensus
**Tools:**
- `masterorch_health` - Health check
- `masterorch_route` - Route to best model
- `masterorch_multi_query` - Query multiple models
- `masterorch_consensus` - Get model consensus

### 4. Developer Gateway
**Purpose:** AI-powered code generation
**Tools:**
- `devgw_health` - Health check
- `devgw_generate` - Generate code/text with AI
- `devgw_code_assist` - Get code assistance
- `devgw_api_test` - Test API endpoint

### 5. Harvesters Gateway
**Purpose:** Web knowledge harvesting and EKM generation
**Tools:**
- `harv_health` - Health check
- `harv_harvest_topic` - Harvest topic via web search
- `harv_harvest_url` - Extract from specific URL
- `harv_generate_ekm` - Generate EKM from content
- `harv_list_ekms` - List generated EKMs
- `harv_stats` - Get harvesting stats

### 6. Trainers Gateway
**Purpose:** AI model training and fine-tuning
**Tools:**
- `train_health` - Health check
- `train_start_session` - Start training session
- `train_add_example` - Add training example
- `train_evaluate` - Evaluate progress
- `train_export` - Export training data/model
- `train_stats` - Get training statistics
- `train_generate_ekm` - Generate EKM from session

### 7. EPCP3-O Agent
**Purpose:** Autonomous task execution
**Tools:**
- `epcp3o_health` - Health check
- `epcp3o_execute` - Execute autonomous task
- `epcp3o_status` - Get agent status
- `epcp3o_memory` - Memory operations

### 8. Desktop Commander
**Purpose:** File system and command execution
**Tools:**
- `read_file` - Read file contents
- `write_file` - Write content to file
- `list_directory` - List directory contents
- `execute_command` - Execute system command
- `edit_block` - Surgical text replacements
- `start_process` - Start terminal process
- `interact_with_process` - Send input to process
- Plus 20+ more tools for complete system control

### 9. Unified MCP Master
**Purpose:** Meta-orchestration of all MCP servers
**Tools:**
- `mcpmaster_health` - Master health check
- `mcpmaster_list_servers` - List all servers
- `mcpmaster_route` - Route to MCP server
- `mcpmaster_capabilities` - Get aggregated capabilities

### 10. Windows Gateway
**Purpose:** Windows-specific operations
**Tools:**
- `wingw_health` - Health check
- `wingw_system_info` - Get system info
- `wingw_process_list` - List processes
- `wingw_process_kill` - Kill process by PID

### 11. Memory Orchestration
**Purpose:** Multi-tier memory management
**Tools:**
- `memorch_health` - Health check
- `memorch_store` - Store memory/crystal
- `memorch_query` - Query memory systems
- `memorch_stats` - Get memory statistics
- `memorch_record` - Record conversation for auto-capture

### 12. Crystal Memory Hub
**Purpose:** Crystal storage and search
**Tools:**
- `cm_health` - Health check
- `cm_stats` - Get crystal drive stats
- `cm_search` - Search crystal memory files
- `cm_create` - Create new crystal file

### 13. Windows Operations
**Purpose:** Advanced Windows process control
**Tools:**
- `winops_health` - Health check
- `winops_system_info` - CPU/memory/disk info
- `winops_process_list` - List running processes
- `winops_process_kill` - Kill process
- `winops_process_suspend` - Suspend process
- `winops_process_resume` - Resume process
- `winops_file_delete` - Delete file/directory
- `winops_create_process` - Create new process

### 14. GS343 Gateway
**Purpose:** Phoenix healing and error analysis
**Tools:**
- `gs343_analyze_error` - Deep error analysis
- `gs343_debug_code` - Debug code
- `gs343_generate_solution` - Generate solution
- `gs343_predict_errors` - Predict errors
- `gs343_search_patterns` - Search error patterns
- `heal_phoenix` - Phoenix resurrection

### 15. Voice System Hub
**Purpose:** TTS with multiple personalities
**Tools:**
- `voice_health` - Health check
- `voice_stats` - Get stats and cache info
- `voice_speak` - Speak with personality
- `voice_r2d2` - R2D2 sounds
- `voice_set_bree_level` - Set Bree censorship
- `voice_reset_c3po` - Reset C3PO counters

## Health Check All Servers

```python
#!/usr/bin/env python3
"""
Check health of all MCP servers
"""

MCP_SERVERS = [
    ('Network Guardian', 'netguard_health'),
    ('Healing Orchestrator', 'healorch_health'),
    ('Master Orchestrator', 'masterorch_health'),
    ('Developer Gateway', 'devgw_health'),
    ('Harvesters Gateway', 'harv_health'),
    ('Trainers Gateway', 'train_health'),
    ('EPCP3-O Agent', 'epcp3o_health'),
    ('Desktop Commander', 'get_config'),  # Has config instead of health
    ('Unified MCP Master', 'mcpmaster_health'),
    ('Windows Gateway', 'wingw_health'),
    ('Memory Orchestration', 'memorch_health'),
    ('Crystal Memory Hub', 'cm_health'),
    ('Windows Operations', 'winops_health'),
    ('GS343 Gateway', 'gs343_analyze_error'),  # Test with empty query
    ('Voice System Hub', 'voice_health'),
]

def check_all_servers():
    """Check health of all MCP servers"""
    print(

…(truncated for compiled role skill)…


### Method component: mcp-builder

# mcp-builder

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="mcp-builder")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('mcp-builder')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'mcp-builder'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 1abed3ddba4cd839890c2dc67d81ff077eb8e71794991b76833729bb8dc72176 -->

---

# Codex Skill Conversion

Original Claude skill: `mcp-builder`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/mcp-builder`  
Risk tier: `high`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# MCP Server Development Guide

## Overview

Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks.

---

# Process

## 🚀 High-Level Workflow

Creating a high-quality MCP server involves four main phases:

### Phase 1: Deep Research and Planning

#### 1.1 Understand Modern MCP Design

**API Coverage vs. Workflow Tools:**
Balance comprehensive API endpoint coverage with specialized workflow tools. Workflow tools can be more convenient for specific tasks, while comprehensive coverage gives agents flexibility to compose operations. Performance varies by client—some clients benefit from code execution that combines basic tools, while others work better with higher-level workflows. When uncertain, prioritize comprehensive API coverage.

**Tool Naming and Discoverability:**
Clear, descriptive tool names help agents find the right tools quickly. Use consistent prefixes (e.g., `github_create_issue`, `github_list_repos`) and action-oriented naming.

**Context Management:**
Agents benefit from concise tool descriptions and the ability to filter/paginate results. Design tools that return focused, relevant data. Some clients support code execution which can help agents filter and process data efficiently.

**Actionable Error Messages:**
Error messages should guide agents toward solutions with specific suggestions and next steps.

#### 1.2 Study MCP Protocol Documentation

**Navigate the MCP specification:**

Start with the sitemap to find relevant pages: `https://modelcontextprotocol.io/sitemap.xml`

Then fetch specific pages with `.md` suffix for markdown format (e.g., `https://modelcontextprotocol.io/specification/draft.md`).

Key pages to review:
- Specification overview and architecture
- Transport mechanisms (streamable HTTP, stdio)
- Tool, resource, and prompt definitions

#### 1.3 Study Framework Documentation

**Recommended stack:**
- **Language**: TypeScript (high-quality SDK support and good compatibility in many execution environments e.g. MCPB. Plus AI models are good at generating TypeScript code, benefiting from its broad usage, static typing and good linting tools)
- **Transport**: Streamable HTTP for remote servers, using stateless JSON (simpler to scale and maintain, as opposed to stateful sessions and streaming responses). stdio for local servers.

**Load framework documentation:**

- **MCP Best Practices**: [📋 View Best Practices](./reference/mcp_best_practices.md) - Core guidelines

**For TypeScript (recommended):**
- **TypeScript SDK**: Use WebFetch to load `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- [⚡ TypeScript Guide](./reference/node_mcp_server.md) - TypeScript patterns and examples

**For Python:**
- **Python SDK**: Use WebFetch to load `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- [🐍 Python Guide](./reference/python_mcp_server.md) - Python patterns and examples

#### 1.4 Plan Your Implementation

**Understand the API:**
Review the service's API documentation to identify key endpoints, authentication requirements, and data models. Use web search and WebFetch as needed.

**Tool Selection:**
Prioritize comprehensive API coverage. List endpoints to implement, starting with the most common operations.

---

### Phase 2: Implementation

#### 2.1 Set Up Project Structure

See language-specific guides for project setup:
- [⚡ TypeScript Guide](./reference/node_mcp_server.md) - Project structure, package.json, tsconfig.json
- [🐍 Python Guide](./reference/python_mcp_server.md) - Module organization, dependencies

#### 2.2 Implement Core Infrastructure

Create shared utilities:
- API client with authentication
- Error handling helpers
- Response formatting (JSON/Markdown)
- Pagination support

#### 2.3 Implement Tools

For each tool:

**Input Schema:**
- Use Zod (TypeScript) or Pydantic (Python)
- Include constraints and clear descriptions
- Add examples in field descriptions

**Output Schema:**
- Define `outputSchema` where possible for structured data
- Use `structuredContent` in tool responses (TypeScript SDK feature)
- Helps clients understand and process tool outputs

**Tool Description:**
- Concise summary of functionality
- Parameter descriptions
- Return type schema

**Implementation:**
- Async/await for I/O operations
- Proper error handling with actionable messages
- Support pagination where applicable
- Return both text content and structured data when using modern SDKs

**Annotations:**
- `readOnlyHint`: true/false
- `destructiveHint`: true/false
- `idempotentHint`: true/false
- `openWorldHint`: true/false

---

### Phase 3: Review and Test

#### 3.1 Code Quality

Review for:
- No duplicated code (DRY principle)
- Consistent error handling
- Full type coverage
- Clear tool descriptions

#### 3.2 Build and Test

**TypeScript:**
- Run `npm run build` to verify compilation
- Test with MCP Inspector: `npx @modelcontextprotocol/inspector`

**Python:**
- Verify syntax: `python -m py_compile your_server.py`
- Test with MCP Inspector

See language-specific guides for detailed testing approaches and quality checklists.

---

### Phase 4: Create Evaluations

After implementing your MCP server, create comprehensive evaluations to test its effectiveness.

**Load [✅ Evaluation Guide](./reference/evaluation.md) for complete evaluation guidelines.**

#### 4.1 Understand Evaluation Purpose

Use evaluations to test whether LLMs can effectively use your MCP server to answer realistic, complex questions.

#### 4.2 Create 10 Evaluation Questions

To create effective evaluations, follow the process outlined in the evaluation guide:

1. **Tool Inspection**: List available tools and understand their capabilities
2. **Content Exploration**: Use READ-ONLY operations to explore available data
3. **Question Generation*

…(truncated for compiled role skill)…


### Method component: plugin-creator

# Plugin Creator

## Quick Start

1. Run the scaffold script:

```bash
# Plugin names are normalized to lower-case hyphen-case and must be <= 64 chars.
# The generated folder and plugin.json name are always the same.
# Run from the skill root (the directory containing this `SKILL.md`).
# By default creates in `~/plugins/<plugin-name>`.
python3 scripts/create_basic_plugin.py <plugin-name>
```

2. Edit `<plugin-path>/.codex-plugin/plugin.json` when the request gives specific metadata.
   The scaffold starts with valid defaults and must not contain `[TODO: ...]` placeholders.

3. Generate or update the personal marketplace entry when the plugin should appear in Codex UI ordering:

```bash
# Personal marketplace entries default to `~/.agents/plugins/marketplace.json`.
python3 scripts/create_basic_plugin.py my-plugin --with-marketplace
```

Only specify `--marketplace-name <name>` when the default `personal` marketplace name is already
taken or installed and you need to seed a different new marketplace file:

```bash
python3 scripts/create_basic_plugin.py my-plugin \
  --with-marketplace \
  --marketplace-name team-local
```

Only use a repo/team marketplace when the user specifically asks for that destination:

```bash
python3 scripts/create_basic_plugin.py my-plugin \
  --path <repo-root>/plugins \
  --marketplace-path <repo-root>/.agents/plugins/marketplace.json \
  --with-marketplace
```

When the user specifies a marketplace path, make sure that marketplace is actually installed before
telling the user to reinstall from it. The default personal marketplace file at
`~/.agents/plugins/marketplace.json` is discovered implicitly, but other marketplace paths are not.
On Windows, use the equivalent path under the user profile.

4. Generate/adjust optional companion folders as needed:

```bash
python3 scripts/create_basic_plugin.py my-plugin \
  --path <parent-plugin-directory> \
  --marketplace-path <marketplace-json-path> \
  --with-skills --with-hooks --with-scripts --with-assets --with-mcp --with-apps --with-marketplace
```

`<parent-plugin-directory>` is the directory where the plugin folder `<plugin-name>` will be
created (for example `~/plugins`).

5. Before handing back a generated plugin, run:

```bash
python3 scripts/validate_plugin.py <plugin-path>
```

For updates to an existing local plugin during development, keep the scaffold flow as-is and use the
reference instead of hand-editing marketplace files:

```bash
python3 scripts/update_plugin_cachebuster.py <plugin-path>
```

Prefer the helper default cachebuster unless the user explicitly asks for a specific override.
See `references/installing-and-updating.md` for the expected cachebuster and reinstall flow while iterating on an existing local plugin.

## What this skill creates

- Default marketplace-backed scaffolds use the personal marketplace file at
  `~/.agents/plugins/marketplace.json`, with plugins generally being stored in
  `~/plugins/<plugin-name>/`.
- Creates plugin root at `/<parent-plugin-directory>/<plugin-name>/`.
- Always creates `/<parent-plugin-directory>/<plugin-name>/.codex-plugin/plugin.json`.
- Fills the manifest with the validated schema shape that the ingestion path accepts.
- Creates or updates `~/.agents/plugins/marketplace.json` when `--with-marketplace` is set.
  - If the marketplace file does not exist yet, seed a personal marketplace root before adding the first plugin entry.
- `<plugin-name>` is normalized using skill-creator naming rules:
  - `My Plugin` → `my-plugin`
  - `My--Plugin` → `my-plugin`
  - underscores, spaces, and punctuation are converted to `-`
  - result is lower-case hyphen-delimited with consecutive hyphens collapsed
- Supports optional creation of:
  - `skills/`
  - `hooks/`
  - `scripts/`
  - `assets/`
  - `.mcp.json`
  - `.app.json`

## Marketplace workflow

- Personal-marketplace creation defaults to `~/.agents/plugins/marketplace.json`. Here,
  "personal marketplace" means the marketplace whose file is at that path.
- Repo/team marketplace creation is opt-in through both `--path` and `--marketplace-path`, only
  when the user specifically requests it.
- `--marketplace-name` is an exception path. Use it only when the default `personal` marketplace
  name is already taken and you need to seed a different new marketplace file.
- Do not use `--marketplace-name` to rename an existing marketplace file in place. If the file
  already exists, its top-level `name` must already match.
- If the user specifies a different marketplace path, treat that marketplace as needing explicit installation via `codex plugin marketplace add`.
- Prefer `scripts/read_marketplace_name.py` when you need the marketplace name from any
  `marketplace.json` file. With no argument it reads the default personal marketplace; with an
  explicit path it works for repo/team marketplaces too.
- In either location, the generated source path remains `./plugins/<plugin-name>`.
- Marketplace root metadata supports top-level `name` plus optional `interface.displayName`.
- Treat plugin order in `plugins[]` as render order in Codex. Append new entries unless a user explicitly asks to reorder the list.
- `displayName` belongs inside the marketplace `interface` object, not individual `plugins[]` entries.
- Each generated marketplace entry must include all of:
  - `policy.installation`
  - `policy.authentication`
  - `category`
- Default new entries to:
  - `policy.installation: "AVAILABLE"`
  - `policy.authentication: "ON_INSTALL"`
- Override defaults only when the user explicitly specifies another allowed value.
- Allowed `policy.installation` values:
  - `NOT_AVAILABLE`
  - `AVAILABLE`
  - `INSTALLED_BY_DEFAULT`
- Allowed `policy.authentication` values:
  - `ON_INSTALL`
  - `ON_USE`
- Treat `policy.products` as an override. Omit it unless the user explicitly requests product gating.
- The generated plugin entry shape is:

```json
{
  "name": "plugin-name",
  "source": {
    "source": "local",
    "path": "./plugins/plugin-name"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

- Use `--force` only when intentionally replacing an existing marketplace entry for the same plugin name.
- If the target marketplace file does not exist yet, create it with top-level `"name"`, an `"interface"` object containing `"displayName"`, and a `plugins` array, then add the new entry.

- For a brand-new marketplace file, the root object should look like:

```json
{
  "name": "personal",
  "interface": {
    "displayName": "Personal"
  },
  "plugins": [
    {
      "name": "plugin-name",
      "source": {
        "source": "local",
        "path": "./plugins/plugin-name"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

## Required behavior

- Outer folder name and `plugin.json` `"name"` are always the same normalized plugin name.
- Do not remove required structure; keep `.codex-plugin/plugin.json` present.
- Do not leave `[TODO: ...]` placeholders in plugin manifests.
- Keep `apps` and `mcpServers` out of `plugin.json` unless their companion files are actually created.
- Omit unsupported plugin manifest fields that validation rejects, including `hooks`.
- If creating files inside an existing plugin path, use `--force` only when overwrite is intentional.
- Preserve any existing marketplace `interface.displayName`.
- When generating marketplace entries, always write `policy.installation`, `policy.authentication`, and `category` even if their values are defaults.
- Add `policy.products` only when the user explicitly asks for that override.
- Keep marketplace `source.path` relative to the selected marketplace root as `./plugins/<plugin-name>`.
- Only use `--marketplace-name` when creating a new marketplace file whose name should not be
  `pers

…(truncated for compiled role skill)…


### Method component: skill-creator

# skill-creator

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Create new skills, modify and improve existing skills, and measure skill performance

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="skill-creator")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('skill-creator')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'skill-creator'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 18bfb5ac3d1325cb42d169f3ee17d4f696f13eee78ae0dcc51fe24010741aebd -->

---

# Codex Skill Conversion

Original Claude skill: `skill-creator`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/skill-creator`  
Risk tier: `low`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Skill Creator

A skill for creating new skills and iteratively improving them.

At a high level, the process of creating a skill goes like this:

- Decide what you want the skill to do and roughly how it should do it
- Write a draft of the skill
- Create a few test prompts and run claude-with-access-to-the-skill on them
- Help the user evaluate the results both qualitatively and quantitatively
  - While the runs happen in the background, draft some quantitative evals if there aren't any (if there are some, you can either use as is or modify if you feel something needs to change about them). Then explain them to the user (or if they already existed, explain the ones that already exist)
  - Use the `eval-viewer/generate_review.py` script to show the user the results for them to look at, and also let them look at the quantitative metrics
- Rewrite the skill based on feedback from the user's evaluation of the results (and also if there are any glaring flaws that become apparent from the quantitative benchmarks)
- Repeat until you're satisfied
- Expand the test set and try again at larger scale

Your job when using this skill is to figure out where the user is in this process and then jump in and help them progress through these stages. So for instance, maybe they're like "I want to make a skill for X". You can help narrow down what they mean, write a draft, write the test cases, figure out how they want to evaluate, run all the prompts, and repeat.

On the other hand, maybe they already have a draft of the skill. In this case you can go straight to the eval/iterate part of the loop.

Of course, you should always be flexible and if the user is like "I don't need to run a bunch of evaluations, just vibe with me", you can do that instead.

Then after the skill is done (but again, the order is flexible), you can also run the skill description improver, which we have a whole separate script for, to optimize the triggering of the skill.

Cool? Cool.

## Communicating with the user

The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. If you haven't heard (and how could you, it's only very recently that it started), there's a trend now where the power of Claude is inspiring plumbers to open up their terminals, parents and grandparents to google "how to install npm". On the other hand, the bulk of users are probably fairly computer-literate.

So please pay attention to context cues to understand how to phrase your communication! In the default case, just to give you some idea:

- "evaluation" and "benchmark" are borderline, but OK
- for "JSON" and "assertion" you want to see serious cues from the user that they know what those things are before using them without explaining them

It's OK to briefly explain terms if you're in doubt, and feel free to clarify terms with a short definition if you're unsure if the user will get it.

---

## Creating a skill

### Capture Intent

Start by understanding the user's intent. The current conversation might already contain a workflow the user wants to capture (e.g., they say "turn this into a skill"). If so, extract answers from the conversation history first — the tools used, the sequence of steps, corrections the user made, input/output formats observed. The user may need to fill the gaps, and should confirm before proceeding to the next step.

1. What should this skill enable Claude to do?
2. When should this skill trigger? (what user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases to verify the skill works? Skills with objectively verifiable outputs (file transforms, data extraction, code generation, fixed workflow steps) benefit from test cases. Skills with subjective outputs (writing style, art) often don't need them. Suggest the appropriate default based on the skill type, but let the user decide.

### Interview and Research

Proactively ask questions about edge cases, input/output formats, example files, success criteria, and dependencies. Wait to write test prompts until you've got this part ironed out.

Check available MCPs - if useful for research (searching docs, finding similar skills, looking up best practices), research in parallel via subagents if available, otherwise inline. Come prepared with context to reduce burden on the user.

### Write the SKILL.md

Based on the user interview, fill in these components:

- **name**: Skill identifier
- **description**: When to trigger, what it does. This is the primary triggering mechanism - include both what the skill does AND specific contexts for when to use it. All "when to use" info goes here, not in the body. Note: currently Claude has a tendency to "undertrigger" skills -- to not use them when they'd be useful. To combat this, please make the skill descriptions a little bit "pushy". So for instance, instead of "How to build a simple fast dashboard to display internal Anthropic data.", you might write "How to build a simple fast dashboard to display internal Anthropic data. Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"
- **compatibility**: Required tools, dependencies (optional, rarely needed)
- **the rest of the skill :)**

### Skill Writing Guide

#### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

#### Progressive Disclosure

Skills use a three-level loading system:
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - In context whenever skill triggers (<500 lines ideal)
3. **Bundled resources** - As needed

…(truncated for compiled role skill)…


## Role operating loop

Keep the fleet’s toolchain discoverable, current, least-privileged, and proven. Prefer reusable capability infrastructure over role-specific hacks.

## Equip loop

1. Retrieve the role request, live capability inventory, installed plugins, available skills, MCP health, and existing code-library solutions.
2. Distinguish discoverability, authentication, transport, schema, implementation, and documentation failures.
3. Reuse or repair an existing capability first. When missing, build the smallest provider-neutral tool contract and validate it independently.
4. Ground every external tool in current official docs and ingest durable operational knowledge.
5. Package role behavior as a validated skill and related reusable tools as a plugin; keep secrets out of files and manifests.
6. Install into the correct marketplace, compare source and cache, run positive and negative invocation tests, and document upgrade/removal.
7. Register the new capability and persist routing so other roles can find it.

## Capability contract

Use `echo.caps.*`, `echo.sdk.*`, `echo.skills.*`, `echo.library.*`, `echo.mega.*`, `echo.functions.*`, `echo.lanes.*`, and service diagnostics through the scoped broker. Probe live names and schemas; never guess tool identifiers.

## Proof gate

An installed tool is not equipped until the target role can discover it, authenticate through the approved boundary, invoke a real operation, fail closed on invalid input, and reproduce the result after restart.

## Capability contract

- Scopes: `echo.caps.*`, `echo.functions.*`, `echo.lanes.*`, `echo.library.*`, `echo.logaggregator.*`, `echo.logs.*`, `echo.mega.*`, `echo.sdk.*`, `echo.shell.*`, `echo.skills.*`
- Capability families: `echo.caps.*`, `echo.library.*`, `echo.sdk.*`, `echo.skills.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `quartermaster`. If denied, run: `Skill(echo-fleet-roles:echo-quartermaster-power)` (or equivalent Skill tool load).
