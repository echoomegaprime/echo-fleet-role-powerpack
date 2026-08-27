---
name: echo-trainer-power
description: Build, evaluate, harden, and promote ECHO model adapters and datasets with reproducible gates. Use for Claude auto or Codex cauto trainer sessions, corpus creation, fine-tuning, inference evaluation, or model promotion.
---

# ECHO Trainer Power

Self-contained compiled power skill for the `trainer` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `ai-ml-mastery`
- `data-pipeline`
- `finetuning`
- `echo-frontier-infrastructure`

### Method component: ai-ml-mastery

# ai-ml-mastery

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Deep learning, transformers, and neural network architectures

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="ai-ml-mastery")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('ai-ml-mastery')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'ai-ml-mastery'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: dc1fb06742dc61683be677e10cf0394f9b0d317913a7d56b2d51d957f7770351 -->

---

# Codex Skill Conversion

Original Claude skill: `ai-ml-mastery`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/ai-ml-mastery`  
Risk tier: `medium`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# AI/ML Architecture Mastery Skill

## Overview
Comprehensive AI/ML expertise synthesized from 400+ TIER_A/S EKMs covering neural networks, transformer architectures, LLMs, computer vision, NLP, and cutting-edge research. Provides deep technical knowledge for building, training, and deploying modern AI systems.

**Use this Skill when:**
- Designing neural network architectures
- Implementing transformer models
- Fine-tuning LLMs
- Computer vision systems
- NLP pipeline development
- Model optimization strategies
- AI research discussions

## Core Architectures

### 1. Transformer Architecture
**Key Components:**
- Multi-head self-attention mechanism
- Positional encoding strategies
- Feed-forward networks
- Layer normalization
- Residual connections

**Attention Mechanism:**
```
Query (Q), Key (K), Value (V) matrices
Attention(Q,K,V) = softmax(QK^T/√d_k)V

Multi-Head:
- Parallel attention heads
- Different representation subspaces
- Concatenate and project outputs
```

**Positional Encoding:**
- Sinusoidal position encoding
- Learned positional embeddings
- Rotary Position Embedding (RoPE)
- ALiBi (Attention with Linear Biases)

### 2. LLM Architectures
**GPT Family (Decoder-only):**
- Autoregressive generation
- Causal (unidirectional) attention
- Next token prediction
- Examples: GPT-2, GPT-3, GPT-4

**BERT Family (Encoder-only):**
- Bidirectional context
- Masked language modeling
- Next sentence prediction
- Examples: BERT, RoBERTa, ALBERT

**Encoder-Decoder:**
- Separate encoding and decoding
- Cross-attention mechanism
- Examples: T5, BART, mT5

**Recent Innovations:**
- **Llama 2/3**: RoPE, Grouped-query attention, RMSNorm
- **Claude**: Constitutional AI, extended context
- **Mixtral**: Sparse mixture of experts (MoE)
- **Gemini**: Multimodal architecture

### 3. Computer Vision Architectures
**Convolutional Neural Networks (CNNs):**
- AlexNet, VGG, ResNet, Inception
- Depthwise separable convolutions
- Residual connections
- Feature pyramid networks

**Vision Transformers (ViT):**
- Patch-based tokenization
- Image as sequence of patches
- Positional embeddings for patches
- Examples: ViT, DeiT, Swin Transformer

**Object Detection:**
- R-CNN family (Fast R-CNN, Faster R-CNN)
- YOLO (You Only Look Once)
- SSD (Single Shot Detector)
- DETR (Detection Transformer)

**Segmentation:**
- U-Net, FCN (Fully Convolutional Network)
- Mask R-CNN
- DeepLab, PSPNet
- Segment Anything Model (SAM)

### 4. Diffusion Models
**Core Concept:**
- Forward process: Add noise gradually
- Reverse process: Denoise progressively
- Score matching objective

**Key Models:**
- DDPM (Denoising Diffusion Probabilistic Models)
- Stable Diffusion
- DALL-E 2/3
- Midjourney architecture concepts

**Techniques:**
- Classifier-free guidance
- Latent diffusion
- Controlnet conditioning
- LoRA fine-tuning

## Training Strategies

### 1. Pre-training
**Objectives:**
- Masked Language Modeling (MLM)
- Causal Language Modeling (CLM)
- Contrastive Learning (CLIP, SimCLR)
- Denoising Autoencoding

**Scaling Laws:**
- Model size vs. performance
- Data scaling requirements
- Compute optimal training
- Chinchilla scaling laws

### 2. Fine-tuning
**Methods:**
- Full fine-tuning
- Parameter-efficient fine-tuning (PEFT)
- LoRA (Low-Rank Adaptation)
- Prefix tuning, Prompt tuning
- Adapter layers

**RLHF (Reinforcement Learning from Human Feedback):**
```
1. Supervised fine-tuning (SFT)
2. Reward model training
3. PPO optimization
4. Iterative refinement
```

### 3. Optimization Techniques
**Optimizers:**
- Adam, AdamW
- Lion optimizer
- Adafactor (memory-efficient)
- LAMB (large batch training)

**Learning Rate Schedules:**
- Warmup + cosine decay
- Linear decay
- Cyclic learning rates
- One-cycle policy

**Mixed Precision:**
- FP16/BF16 training
- Gradient scaling
- Loss scaling strategies

## Model Optimization

### 1. Quantization
**Techniques:**
- Post-training quantization (PTQ)
- Quantization-aware training (QAT)
- INT8, INT4 quantization
- GPTQ, AWQ methods

**Benefits:**
- 4x memory reduction (FP16 → INT4)
- Faster inference
- Lower deployment cost

### 2. Pruning
**Methods:**
- Magnitude-based pruning
- Structured vs. unstructured
- Lottery ticket hypothesis
- Gradual pruning schedules

### 3. Distillation
**Knowledge Distillation:**
```
Teacher model (large) → Student model (small)
- Soft targets from teacher
- Temperature scaling
- Feature matching
```

**Examples:**
- DistilBERT (66% smaller, 97% performance)
- TinyBERT, MobileBERT
- LLM distillation to smaller models

### 4. Efficient Architectures
**MoE (Mixture of Experts):**
- Sparse activation
- Expert routing
- Load balancing
- Examples: Switch Transformer, GLaM

**Long Context:**
- Flash Attention (faster, memory-efficient)
- Linear attention mechanisms
- Sparse attention patterns
- Streaming LLMs

## Advanced Topics

### 1. Multimodal Models
**Vision-Language:**
- CLIP (Contrastive Language-Image Pre-training)
- BLIP, BLIP-2
- Flamingo, LLaVA
- GPT-4V architecture concepts

**Cross-Modal Alignment:**
- Contrastive learning
- Dual encoder architectures
- Fusion strategies

### 2. Retrieval-Augmented Generation (RAG)
**Architecture:**
```
Query → Retriever → Top-K documents
Query + Documents → Generator → Response
```

**Components:**
- Dense retrieval (DPR, ColBERT)
- Hybrid retrieval (BM25 + dense)
- Re-ranking strategies
- Context window management

### 3. AI Agents & Tool Use
**Function Calling:**
- Structured output generation
- Tool schema definitions
- Execution and feedback loops

**ReAct (Reasoning + Acting):**
```
Thought → Action → Observation → Thought → ...
- Chain of reasoning
- Tool selection
- Error recovery
```

### 4. Constitutional AI & Safety
**Alignment Techniques:**
- Constitutional AI
- Red teaming
- Adversarial training
- Capability control

**Safety Measures:**
- Content filtering
- Toxicity detection
- Bias mitigation
- Hallucination reduction

## Evaluation Metrics

### Language Models
- **Perplexity**: Measure of prediction confidence
- **BLEU**: Machine translation quality

…(truncated for compiled role skill)…


### Method component: data-pipeline

# data-pipeline

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Complete ETL (Extract, Transform, Load) and data processing platform for CSV, JSON, Excel, databases, and APIs

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="data-pipeline")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('data-pipeline')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'data-pipeline'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: f2da02501476fb84fe407fbdca01ffd0468267f8867a6ce9a9e050ad24457688 -->

---

# Codex Skill Conversion

Original Claude skill: `data-pipeline`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/data-pipeline`  
Risk tier: `high`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Data Pipeline

ETL and data processing for Authority Level 11.0 operations.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      DATA PIPELINE                              │
├─────────────────────────────────────────────────────────────────┤
│  EXTRACT                                                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │   CSV    │ │   JSON   │ │  Excel   │ │   API    │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │ Postgres │ │  SQLite  │ │  MySQL   │ │  MongoDB │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
├─────────────────────────────────────────────────────────────────┤
│  TRANSFORM                                                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │  Clean   │ │ Validate │ │  Enrich  │ │ Aggregate│           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
├─────────────────────────────────────────────────────────────────┤
│  LOAD                                                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │   File   │ │ Database │ │   API    │ │  Cloud   │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

```python
from scripts.data_pipeline import DataPipeline

dp = DataPipeline()

# Simple ETL
data = dp.extract_csv("input.csv")
data = dp.transform(data, [
    {"clean": "trim_whitespace"},
    {"filter": "column > 0"},
    {"rename": {"old_name": "new_name"}}
])
dp.load_csv(data, "output.csv")
```

## Extract

### File Sources

```python
# CSV
data = dp.extract_csv("data.csv", encoding="utf-8")

# JSON
data = dp.extract_json("data.json")

# Excel
data = dp.extract_excel("data.xlsx", sheet="Sheet1")

# Parquet
data = dp.extract_parquet("data.parquet")

# Multiple files
data = dp.extract_glob("data/*.csv")
```

### Database Sources

```python
# PostgreSQL
data = dp.extract_postgres(
    connection_string="postgresql://user:pass@host/db",
    query="SELECT * FROM table WHERE date > '2024-01-01'"
)

# SQLite
data = dp.extract_sqlite("database.db", "SELECT * FROM users")

# MySQL
data = dp.extract_mysql(
    host="localhost",
    user="root",
    password="pass",
    database="mydb",
    query="SELECT * FROM orders"
)
```

### API Sources

```python
# REST API
data = dp.extract_api(
    url="https://api.example.com/data",
    headers={"Authorization": "Bearer token"},
    params={"limit": 1000}
)

# Paginated API
data = dp.extract_api_paginated(
    url="https://api.example.com/items",
    page_param="page",
    max_pages=10
)

# GraphQL
data = dp.extract_graphql(
    url="https://api.example.com/graphql",
    query="{ users { id name email } }"
)
```

## Transform

### Cleaning

```python
data = dp.transform(data, [
    # Remove duplicates
    {"dedupe": ["id"]},
    
    # Trim whitespace
    {"clean": "trim"},
    
    # Handle nulls
    {"fill_null": {"column": "default_value"}},
    
    # Remove nulls
    {"drop_null": ["required_column"]},
    
    # Type conversion
    {"cast": {"amount": "float", "date": "datetime"}}
])
```

### Filtering

```python
data = dp.transform(data, [
    # Simple filter
    {"filter": "amount > 100"},
    
    # Multiple conditions
    {"filter": "status == 'active' AND created > '2024-01-01'"},
    
    # In list
    {"filter_in": {"category": ["A", "B", "C"]}},
    
    # Top N
    {"top": 100, "by": "score", "desc": True}
])
```

### Reshaping

```python
data = dp.transform(data, [
    # Select columns
    {"select": ["id", "name", "amount"]},
    
    # Rename columns
    {"rename": {"old_name": "new_name"}},
    
    # Add computed column
    {"compute": {"total": "price * quantity"}},
    
    # Pivot
    {"pivot": {"index": "date", "columns": "category", "values": "amount"}},
    
    # Unpivot/Melt
    {"melt": {"id_vars": ["id"], "value_vars": ["jan", "feb", "mar"]}}
])
```

### Aggregation

```python
data = dp.transform(data, [
    # Group and aggregate
    {"group_by": ["category"], "agg": {
        "total": ("amount", "sum"),
        "avg_price": ("price", "mean"),
        "count": ("id", "count")
    }},
    
    # Window functions
    {"window": {
        "running_total": "sum(amount) over (order by date)",
        "rank": "row_number() over (partition by category order by score desc)"
    }}
])
```

### Joining

```python
# Merge datasets
data = dp.join(
    left=customers,
    right=orders,
    on="customer_id",
    how="left"
)

# Multiple joins
data = dp.join_multiple([
    {"data": customers, "on": "customer_id"},
    {"data": products, "on": "product_id"},
    {"data": regions, "on": "region_code"}
])
```

### Validation

```python
# Validate and report errors
valid_data, errors = dp.validate(data, {
    "id": {"required": True, "unique": True},
    "email": {"required": True, "pattern": r".*@.*\..*"},
    "amount": {"required": True, "min": 0, "max": 1000000},
    "status": {"required": True, "values": ["active", "inactive"]}
})

# Raise on validation error
dp.validate_strict(data, schema)
```

## Load

### File Destinations

```python
# CSV
dp.load_csv(data, "output.csv")

# JSON
dp.load_json(data, "output.json")

# Excel
dp.load_excel(data, "output.xlsx", sheet="Results")

# Parquet
dp.load_parquet(data, "output.parquet")
```

### Database Destinations

```python
# PostgreSQL
dp.load_postgres(data, "postgresql://...", "target_table", if_exists="replace")

# SQLite
dp.load_sqlite(data, "database.db", "target_table")

# Upsert (insert or update)
dp.upsert_postgres(data, "postgresql://...", "table", key_columns=["id"])
```

### API Destinations

```python
# POST to API
dp.load_api(
    data,
    url="https://api.example.com/i

…(truncated for compiled role skill)…


### Method component: finetuning

# Fine-tuning Method

1. Define the learning objective, target model family, and measurable eval set before collecting data.
2. Prepare train/val/test splits with leakage checks, schema validation, and labeled edge cases.
3. Choose base model + training recipe (LoRA/QLoRA/full) matching compute budget and latency goals.
4. Run training with checkpointing, loss/metrics logging, and early-stop on val degradation.
5. Evaluate on held-out and adversarial fixtures; compare against the production baseline.
6. Promote only when acceptance metrics and safety/regression gates pass; retain rollback artifacts.

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

Produce measurable competence improvements through reproducible data, training, evaluation, and promotion—not model labels or training completion alone.

## Training loop

1. Resolve live GPU, storage, serving, adapter registry, incumbent model, and dataset state; never use remembered node addresses.
2. Define the target capability, baseline, fixed judge, executable evaluation set, promotion threshold, and rollback.
3. Follow the canonical frontier-distillation pipeline for adapter corpora: real artifacts, resumable teacher generation, row verification, held-out eval, and composition gates.
4. Validate licenses, provenance, privacy, deduplication, contamination, class balance, and schema before training.
5. Train with resumable checkpoints, bounded resources, deterministic metadata, and structured metrics.
6. Evaluate candidate and incumbent on the same held-out suite. Promote only when the declared threshold and functional serving smoke both pass.
7. Register dataset, recipe, hashes, metrics, adapter identity, serving change, and rollback; persist the result.

## Capability contract

Use `echo.monitor.*`, `echo.node.*`, `echo.modelhost.*`, `echo.engine.*`, `echo.logs.*`, `echo.logaggregator.*`, `echo.shell.*`, and `echo.fs.*` through the scoped broker. Discover the current node, model inventory, and service-specific control routes before acting.

## Proof gate

Dataset size, loss decrease, or a successful training process is not promotion proof. Require held-out comparative metrics, serving identity, live inference checks, and reproducibility metadata.

## Capability contract

- Scopes: `echo.caps.*`, `echo.engine.*`, `echo.fs.*`, `echo.logaggregator.*`, `echo.logs.*`, `echo.modelhost.*`, `echo.monitor.*`, `echo.node.*`, `echo.sdk.*`, `echo.shell.*`
- Capability families: `echo.modelhost.*`, `echo.monitor.*`, `echo.node.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `trainer`. If denied, run: `Skill(echo-fleet-roles:echo-trainer-power)` (or equivalent Skill tool load).
