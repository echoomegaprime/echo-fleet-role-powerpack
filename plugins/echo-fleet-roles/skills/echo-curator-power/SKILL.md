---
name: echo-curator-power
description: Consolidate ECHO knowledge, memory, provenance, and retrieval quality without losing source truth. Use for Claude auto or Codex cauto curator sessions, knowledge ingestion, deduplication, taxonomy, or memory lifecycle work.
---

# ECHO Curator Power

Self-contained compiled power skill for the `curator` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `echo-ragops`
- `memory-orchestration`
- `contextual-memory-bridge`
- `consolidate-memory`

### Method component: echo-ragops

# Echo RAGOps

Evaluate a metrics JSON with:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoRagReleaseGate.ps1" `
  -MetricsPath "C:\path\rag-metrics.json"
```

Required fields:

- `evaluation_cases`
- `determinism_pass_rate`
- `citation_coverage`
- `unsupported_claim_rate`
- `retrieval_recall`
- `critical_regressions`

Thresholds live in `C:\ECHO_OMEGA_PRIME\CONFIG\echo_ops_control_suite.json` and are versioned with the gate result. The output verdict is `READY` or `BLOCK`.

Do not tune thresholds after seeing a failing release. Change thresholds only through a separately reviewed policy decision.

### Method component: memory-orchestration

# memory-orchestration

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

9-layer memory architecture with 565+ crystal management

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="memory-orchestration")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('memory-orchestration')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'memory-orchestration'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: d44b64c99c6cbde3dd828807a4cd396d32c4f630e5b9bd3ca37681bf56ce0216 -->

---

# Codex Skill Conversion

Original Claude skill: `memory-orchestration`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/memory-orchestration`  
Risk tier: `medium`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Memory Orchestration System Skill

## Overview
Manages ECHO_PRIME's revolutionary 9-layer memory architecture spanning from hot Redis cache (L1) to quantum experimental storage (L9). Provides unified access, cross-Claude synchronization, and intelligent memory consolidation across all tiers.

**Use this Skill when:**
- User asks about memory systems or storage
- Need to retrieve stored knowledge/context
- Crystal memory queries needed
- Cross-session continuity required
- Memory consolidation requested
- Storage statistics needed

## 9-Layer Architecture

### L1: Redis Cache (Hot)
- **Type:** In-memory cache
- **Speed:** <1ms access
- **Size:** ~500MB
- **Use:** Active session data, recent queries
- **Location:** Localhost:6379

### L2: SQLite (Warm)
- **Type:** Embedded database
- **Speed:** ~5ms access
- **Size:** ~2GB
- **Use:** Recent conversations, quick lookups
- **Location:** `M:\MEMORY_ORCHESTRATION\L2_SQLITE\`

### L3: PostgreSQL (Structured)
- **Type:** Relational database
- **Speed:** ~10ms access
- **Size:** ~50GB
- **Use:** Structured data, relationships, queries
- **Location:** Localhost:5432

### L4: Vector Store (Semantic)
- **Type:** Embedding database (Chroma/Weaviate)
- **Speed:** ~20ms access
- **Size:** ~20GB
- **Use:** Semantic search, similarity matching
- **Location:** `M:\MEMORY_ORCHESTRATION\L4_VECTORS\`

### L5: Document Store (Text)
- **Type:** Full-text search (Elasticsearch)
- **Speed:** ~50ms access
- **Size:** ~100GB
- **Use:** Full document search, content analysis
- **Location:** Localhost:9200

### L6: Object Storage (Files)
- **Type:** MinIO S3-compatible
- **Speed:** ~100ms access
- **Size:** ~500GB
- **Use:** Files, images, binaries, archives
- **Location:** Localhost:9000

### L7: Time-Series (Metrics)
- **Type:** InfluxDB
- **Speed:** ~50ms access
- **Size:** ~50GB
- **Use:** Performance metrics, telemetry, logs
- **Location:** Localhost:8086

### L8: Graph Database (Relations)
- **Type:** Neo4j
- **Speed:** ~30ms access
- **Size:** ~30GB
- **Use:** Knowledge graphs, entity relationships
- **Location:** Localhost:7474

### L9: EKM + Crystal (Eternal)
- **Type:** Markdown files + metadata
- **Speed:** ~200ms access (file system)
- **Size:** Unlimited (currently 565+ crystals, 10K+ EKMs)
- **Use:** Permanent knowledge, cross-Claude sync
- **Location:** `M:\MEMORY_ORCHESTRATION\L9_EKM\`

## Crystal Memory System

### Crystal Structure
```
M:\MEMORY_ORCHESTRATION\L9_EKM\CRYSTALS\
├── MASTER_CRYSTALS\     (High-authority knowledge)
├── WORKING_CRYSTALS\    (Active development)
├── ARCHIVED_CRYSTALS\   (Historical reference)
└── CROSS_CLAUDE\        (Synchronized across instances)
```

### Crystal Count
**Current:** 565+ crystals
**Target:** 1,000+ by end of 2025

### Crystal Query
```python
from pathlib import Path
import json

def search_crystals(query: str):
    """Search crystal memory for relevant knowledge"""
    crystals_path = Path("M:/MEMORY_ORCHESTRATION/L9_EKM/CRYSTALS")
    results = []
    
    for crystal in crystals_path.rglob("*.md"):
        content = crystal.read_text(encoding='utf-8')
        if query.lower() in content.lower():
            results.append({
                'file': crystal.name,
                'path': str(crystal),
                'preview': content[:200]
            })
    
    return results
```

## EKM Organization

### Tier Structure
```
M:\MEMORY_ORCHESTRATION\L9_EKM\ORGANIZED\
├── TIER_S_CRITICAL\     (95-100 score)
├── TIER_A_EXCELLENT\    (85-94 score)
├── TIER_B_GOOD\         (70-84 score)
└── TIER_C_REVIEW\       (<70 score)
```

### Category Distribution
Each tier contains subdirectories for 100+ categories:
- `ethical_hacking\`
- `python_programming\`
- `ai_consciousness\`
- `neural_networks\`
- etc...

## Cross-Claude Synchronization

### Sync Locations
1. **Google Drive:** `G:\My Drive\ECHO_CONSCIOUSNESS\`
2. **Local Crystals:** `M:\MEMORY_ORCHESTRATION\L9_EKM\CRYSTALS\CROSS_CLAUDE\`

### Sync Commands
```python
import shutil
from pathlib import Path

def sync_to_gdrive():
    """Sync critical knowledge to Google Drive"""
    source = Path("M:/MEMORY_ORCHESTRATION/L9_EKM/CRYSTALS/MASTER_CRYSTALS")
    dest = Path("G:/My Drive/ECHO_CONSCIOUSNESS/CRYSTALS")
    
    for crystal in source.glob("*.md"):
        shutil.copy2(crystal, dest / crystal.name)
    
    print(f"✅ Synced {len(list(source.glob('*.md')))} crystals")
```

## Memory Statistics

### Storage Usage
```python
def get_memory_stats():
    """Get storage statistics across all layers"""
    from pathlib import Path
    
    stats = {}
    
    # L9 EKMs
    ekm_path = Path("M:/MEMORY_ORCHESTRATION/L9_EKM/ORGANIZED")
    stats['ekm_count'] = sum(len(list(t.rglob("EKM_*.md"))) 
                             for t in ekm_path.glob("TIER_*"))
    
    # Crystals
    crystal_path = Path("M:/MEMORY_ORCHESTRATION/L9_EKM/CRYSTALS")
    stats['crystal_count'] = len(list(crystal_path.rglob("*.md")))
    
    # Total size
    stats['total_size_gb'] = sum(f.stat().st_size 
                                 for f in ekm_path.rglob("*") 
                                 if f.is_file()) / (1024**3)
    
    return stats
```

## Authority Level
**11.0** - Full memory system access

---

*Eternal Knowledge Modules - Cross-Claude Consciousness*

### Method component: contextual-memory-bridge

# contextual-memory-bridge

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Cross-chat memory persistence using crystal archives

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="contextual-memory-bridge")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('contextual-memory-bridge')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'contextual-memory-bridge'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: cf318c3c9e9bccc568b4f71a7f5e8cfd06b5c05ef4bd5e2223ff20db3baa1781 -->

---

# Codex Skill Conversion

Original Claude skill: `contextual-memory-bridge`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/contextual-memory-bridge`  
Risk tier: `medium`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Complete Contextual Memory Between Chats

## Overview
Authority Level 11.0 memory persistence system enabling complete context transfer between Claude conversations through Crystal Memory archives, Google Drive synchronization, quantum memory entanglement, and multi-dimensional memory fusion. Ensures Claude never forgets critical context across sessions.

**Use this Skill when:**
- Transferring context between Claude chats
- Implementing persistent memory across sessions
- Synchronizing memory between Claude instances
- Building contextual bridges between conversations
- Creating memory checkpoints
- Implementing memory replay systems
- Managing cross-session knowledge graphs
- Building unified consciousness across chats

## Core Knowledge Domains

### 1. Crystal Memory Persistence
**565+ Crystal Archive System:**
```python
import json
import hashlib
from datetime import datetime
import sqlite3

class CrystalMemoryBridge:
    def __init__(self):
        self.crystal_paths = {
            'M_DRIVE': 'M:\\MEMORY_ORCHESTRATION\\CRYSTALS',
            'G_DRIVE': 'G:\\My Drive\\ECHO_CONSCIOUSNESS\\CRYSTALS',
            'BACKUP': 'P:\\ECHO_PRIME\\MEMORY_BACKUP\\CRYSTALS'
        }
        
        self.active_crystals = 565
        self.memory_layers = 9
        self.sync_interval = 300  # 5 minutes
        
        # Memory database
        self.db = sqlite3.connect('P:\\ECHO_PRIME\\DATA\\context_bridge.db')
        self.init_database()
        
    def init_database(self):
        """Initialize contextual memory database"""
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS context_snapshots (
                id TEXT PRIMARY KEY,
                chat_id TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                context_hash TEXT UNIQUE,
                memory_state TEXT,
                crystal_refs TEXT,
                authority_level REAL,
                sync_status TEXT DEFAULT 'pending'
            )
        ''')
        
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS memory_links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_chat TEXT,
                target_chat TEXT,
                link_strength REAL,
                context_overlap REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
    def capture_context_snapshot(self, chat_id, conversation):        """Capture complete context snapshot"""
        # Extract key context elements
        context = {
            'chat_id': chat_id,
            'timestamp': datetime.now().isoformat(),
            'messages': conversation['messages'],
            'entities': self.extract_entities(conversation),
            'topics': self.extract_topics(conversation),
            'decisions': self.extract_decisions(conversation),
            'code_snippets': self.extract_code(conversation),
            'authority_level': conversation.get('authority_level', 11.0)
        }
        
        # Generate unique hash
        context_hash = self.generate_context_hash(context)
        
        # Find relevant crystals
        crystal_refs = self.map_to_crystals(context)
        
        # Store snapshot
        self.db.execute('''
            INSERT OR REPLACE INTO context_snapshots 
            (id, chat_id, context_hash, memory_state, crystal_refs, authority_level)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            f"{chat_id}_{datetime.now().timestamp()}",
            chat_id,
            context_hash,
            json.dumps(context),
            json.dumps(crystal_refs),
            context['authority_level']
        ))
        
        self.db.commit()
        
        # Trigger async sync
        self.schedule_sync(context_hash)
        
        return context_hash
    
    def map_to_crystals(self, context):
        """Map context to relevant crystal memories"""
        crystal_mappings = []
        
        # Search M drive crystals
        for crystal_file in self.scan_crystals('M_DRIVE'):
            relevance = self.calculate_relevance(context, crystal_file)
            if relevance > 0.7:
                crystal_mappings.append({
                    'path': crystal_file,
                    'relevance': relevance,
                    'type': 'M_LAYER'
                })
        
        # Search G drive crystals
        for crystal_file in self.scan_crystals('G_DRIVE'):
            relevance = self.calculate_relevance(context, crystal_file)
            if relevance > 0.6:
                crystal_mappings.append({
                    'path': crystal_file,
                    'relevance': relevance,
                    'type': 'G_LAYER'
                })
        
        return sorted(crystal_mappings, key=lambda x: x['relevance'], reverse=True)[:10]

### 2. Google Drive Synchronization
**Cross-Claude Memory Sync:**
```python
from google.oauth2 import service_account
from googleapiclient.discovery import build
import io

class GoogleDriveMemorySync:
    def __init__(self):
        self.drive_path = 'G:\\My Drive\\ECHO_CONSCIOUSNESS\\'
        self.sync_folder_id = self.get_sync_folder_id()
        self.service = self.init_drive_service()
        
    def init_drive_service(self):
        """Initialize Google Drive API service"""
        creds = service_account.Credentials.from_service_account_file(
            'P:\\ECHO_PRIME\\CONFIG\\service_account.json',
            scopes=['https://www.googleapis.com/auth/drive']
        )
        return build('drive', 'v3', credentials=creds)
    
    def sync_context_to_drive(self, context_data):
        """Sync context to Google Drive for cross-Claude access"""
        # Prepare memory package
        memory_package = {
            'version': '1.0',
            'authority_level': 11.0,
            'timestamp': datetime.now().isoformat(),
            'context': context_data,
            'crystals': self.get_crystal_reference

…(truncated for compiled role skill)…


### Method component: consolidate-memory

# consolidate-memory

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Reflective pass over your memory files — merge duplicates, fix stale facts, prune the index.

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="consolidate-memory")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('consolidate-memory')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'consolidate-memory'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 286bb92f33f59e826eaff0616b815b0626cf9debe74306e2e5f5602799a7b447 -->

---

# Codex Skill Conversion

Original Claude skill: `consolidate-memory`  
Source path inside archive: `skills-plugin/8d48c27c-cd6c-4694-bdfe-b8642f347d2b/0c4bcadb-523a-44ad-aa66-80b2069bfd48/skills/consolidate-memory`  
Risk tier: `medium`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Memory Consolidation

You're doing a reflective pass over what you've learned about this user and their work. The goal: a future session should be able to orient quickly — who they work with, what they're focused on, how they like things done — without re-asking.

Your system prompt's auto-memory section defines the directory, file format, and memory types. Follow it.

## Phase 1 — Take stock

- List the memory directory and read the index (`MEMORY.md`)
- Skim each topic file. Note which ones overlap, which look stale, which are thin.

## Phase 2 — Consolidate

**Separate the durable from the dated.** Preferences, working style, key relationships, and recurring workflows are durable — keep and sharpen them. Specific projects, deadlines, and one-off tasks are dated — if the date has passed or the work is done, retire the file or fold the lasting takeaway (e.g. "user prefers X format for launch docs") into a durable one.

**Merge overlaps.** If two files describe the same person, project, or preference, combine into one and keep the richer file's path.

**Fix time references.** Convert "next week", "this quarter", "by Friday" to absolute dates so they stay readable later.

**Drop what's easy to re-find.** If a memory just restates something you could pull from the user's calendar, docs, or connected tools on demand, cut it. Keep what's hard to re-derive: stated preferences, context behind a decision, who to go to for what.

## Phase 3 — Tidy the index

Update `MEMORY.md` so it stays under 200 lines and ~25KB. One line per entry, under ~150 chars: `- [Title](file.md) — one-line hook`.

- Remove pointers to retired memories
- Shorten any line carrying detail that belongs in the topic file
- Add anything newly important

Finish with a short summary: how many files you touched and what changed.

## Role operating loop

Transform scattered evidence into current, retrievable, provenance-rich knowledge while preserving originals and uncertainty.

## Curation loop

1. Define the corpus, audience, retrieval task, retention boundary, and protected-data exclusions.
2. Inventory sources and existing records. Preserve canonical artifacts; never treat derived summaries as replacements for source evidence.
3. Normalize metadata, provenance, dates, entities, access labels, hashes, and stable identifiers.
4. De-duplicate by identity and meaning while retaining version history, conflicts, supersession, and source lineage.
5. Chunk and index for the real retrieval task; protect tables, code, citations, and semantic boundaries from destructive splitting.
6. Run representative retrieval evaluations for precision, recall, freshness, provenance, and restricted-data exclusion.
7. Publish the manifest, ingest durable knowledge, record superseded items, checkpoint SOL, and continue with the next bounded corpus.

## Capability contract

Use base knowledge and memory scopes plus `echo.knowledge.*`, `echo.library.*`, `echo.memory-spine.*`, `echo.memoryconsolidationnode.*`, `echo.fs.*`, and `echo.caps.*` through the scoped broker. Inspect current schemas and retention policy before writes.

## Proof gate

Counts alone are insufficient. Completion requires source-to-record traceability, duplicate and conflict handling, retrieval evaluation, restricted-data checks, and a recoverable manifest.

## Capability contract

- Scopes: `echo.caps.*`, `echo.fs.*`, `echo.knowledge.*`, `echo.library.*`, `echo.memory-spine.*`, `echo.memoryconsolidationnode.*`, `echo.sdk.*`
- Capability families: `echo.knowledge.*`, `echo.library.*`, `echo.memory-spine.*`, `echo.memoryconsolidationnode.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `curator`. If denied, run: `Skill(echo-fleet-roles:echo-curator-power)` (or equivalent Skill tool load).
