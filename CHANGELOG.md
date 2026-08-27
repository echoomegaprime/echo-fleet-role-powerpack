# Changelog

## 1.3.0 — 2026-08-26

- Canonical Codex skills plugin: `echo-fleet-roles@echo-omega-prime-marketplace` (sole role-skills source)
- Merged marketplace rich role SKILL.md bodies + powerpack `echo-role-switching`; retained `echo-fleet-base`
- Retired dual-enable of `echo-fleet-role-powerpack@echoomegaprime` as a skills plugin (MCP connector unchanged)
- Added `scripts/remediate_codex_plugins.py` (lean allowlist + per-plugin disable justifications)
- Added `scripts/verify_role_skills_budget.py` (no budget warning; skill resolve; hash pins)
- Pinned surviving skill hashes in `docs/SKILL_HASH_PIN.json`

## 1.0.0 — 2026-08-10

- Full governed MCP server implementation (not a scaffold)
- Streamable HTTP `/mcp` JSON-RPC tools
- Durable JSON store + audit log
- CI: typecheck, test, build
