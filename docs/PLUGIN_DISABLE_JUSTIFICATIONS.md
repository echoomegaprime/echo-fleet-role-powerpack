# Plugin disable justifications (skills budget + role ambiguity)

Incident: Codex headless launch 2026-08-25 — `Exceeded skills context budget` (603 skills dropped), then `echo-fleet-roles:echo-judge-power` invisible → CLAUDE.md ROLE-SWITCH law broken.

## Canonical decision

| Item | Value |
|---|---|
| **Winner (sole role-skills plugin)** | `echo-fleet-roles@echo-omega-prime-marketplace` |
| **Retired (skills plugin)** | `echo-fleet-role-powerpack@echoomegaprime` |
| **Why winner** | Doctrine invokes `echo-fleet-roles:<role>-power`. Marketplace SKILL.md bodies are the rich production set. |
| **Merge retained from loser** | `echo-role-switching` body from the Codex powerpack plugin (larger / more complete than marketplace copy). Also retained `echo-fleet-base` from marketplace (powerpack lacked it). |
| **Trap avoided** | Did **not** disable by name similarity alone. Compared skill lists + SHA-256 of every `SKILL.md`. |

The MCP HTTP connector in this repo (`echo-fleet-role-powerpack`) remains a **separate capability**. It must not be re-enabled as a second *skills* plugin alongside the winner.

## Per-plugin disables

| Plugin | Action | Why |
|---|---|---|
| `echo-fleet-role-powerpack@echoomegaprime` | **disable** | Duplicate role-power skills with **different** SKILL.md hashes vs marketplace — resolution-order correctness hazard. Role-switching content merged into winner first. |
| `vercel@openai-curated` | **disable** | True duplicate product vs Claude official vercel; 47 skills; not required for FORGE fleet builder loops. |
| `vercel@claude-plugins-official` | **disable** | Second vercel enablement (30 skills). Same product family; budget bloat. |
| `figma@openai-curated` | **disable** | True duplicate vs Claude official figma; design SaaS irrelevant to fleet builds on FORGE. |
| `figma@claude-plugins-official` | **disable** | Second figma enablement. |
| `anthropic-skills@claude-cowork` | **disable** | Largest single contributor (54 skills) in the overflow table; not used by Codex fleet role doctrine. |
| `huggingface-skills@claude-plugins-official` | **disable** | 25 skills; HF workflows not part of FORGE builder seat path. |
| `hugging-face@openai-curated` | **disable** | Parallel HF surface; budget. |
| `cloudflare@openai-curated` | **disable** + quarantine cache | Startup fatal: unauthenticated `mcp.cloudflare.com` → `AuthRequired` / transport closed. Also conflicts with NO CLOUDFLARE doctrine for app deploys. Remediator also sets `[features] apps = false` because Codex Apps can still probe Cloudflare MCP even when the plugin is not installed. |
| `canva@openai-curated` | **disable** | SaaS design tooling; irrelevant to fleet role / builder work. |
| `notion@openai-curated` | **disable** | SaaS notes; fleet uses Crystal Memory / throne docs. |
| `slack@openai-curated` | **disable** | Prefer Echo comms plugins; cuts skill catalog noise. |
| `gmail@openai-curated` | **disable** | SaaS mail; not required for builder seats. |
| `google-drive@openai-curated` | **disable** | Large skill tree; not on critical path. |
| `openai-templates@openai-curated` | **disable** | Template pack skill volume. |
| `superpowers@openai-curated` | **disable** (optional lean) | Large skill surface; enable only when explicitly needed. |
| `data-analytics@openai-curated` | **disable** (optional lean) | Large skill surface; enable only when explicitly needed. |

## Keeplist (lean mode)

When `scripts/remediate_codex_plugins.py --lean` runs, only these stay enabled (if present):

- `echo-fleet-roles@echo-omega-prime-marketplace` (**required**)
- `codex-security@…`
- `echo-grounding@…`, `echo-security@…`, `echo-forge@…`, `echo-foreman@…`
- `phoenix-recovery@…`, `crystal-memory@…`

Everything else enabled at remediation time is disabled with reason `lean-pass-not-required-for-fleet-builder`.

## Apply

```bash
python3 scripts/remediate_codex_plugins.py --lean
python3 scripts/verify_role_skills_budget.py
```
