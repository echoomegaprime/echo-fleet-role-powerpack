# echo-fleet-role-powerpack

Two surfaces, one repo:

1. **MCP HTTP connector** — list roles, show active role, activate high-risk roles only with `confirm=EXECUTE`.
2. **Canonical Codex role-skills plugin** — `echo-fleet-roles@echo-omega-prime-marketplace` (sole role-power skills source after the 2026-08-25 budget/ambiguity fix).

## Why the skills plugin lives here

Codex had **two** enabled plugins with same-named role skills and **different** `SKILL.md` bodies, while 101 plugins overflowed the skills context budget (603 skills dropped). Role skills vanished from the model-visible catalog and broke mandatory `echo-fleet-roles:<role>-power` invocation.

**Decision:** keep **one** skills plugin — `echo-fleet-roles`. Merge powerpack-only richness (`echo-role-switching`) into it. **Retire** `echo-fleet-role-powerpack@…` as a *skills* plugin (this MCP server may still run). See [`docs/CANONICAL_ROLE_SKILLS.md`](docs/CANONICAL_ROLE_SKILLS.md).

## Codex install / remediate

```bash
# Point Codex at this repo's marketplace, enable canonical plugin, disable duplicates
python3 scripts/remediate_codex_plugins.py --lean

# Fresh-launch checks: no budget warning; judge/commander/builder/role-switching resolve; hashes pin
python3 scripts/verify_role_skills_budget.py
```

Doctrine invocations that must resolve:

- `echo-fleet-roles:echo-judge-power`
- `echo-fleet-roles:echo-commander-power`
- `echo-fleet-roles:echo-builder-power`
- `echo-fleet-roles:echo-role-switching`

Pinned hashes: [`docs/SKILL_HASH_PIN.json`](docs/SKILL_HASH_PIN.json)  
Disable justifications: [`docs/PLUGIN_DISABLE_JUSTIFICATIONS.md`](docs/PLUGIN_DISABLE_JUSTIFICATIONS.md)

## MCP resource

- Path: `/oauth-mcp-powerpack-v1`
- Production edge (when routed): `https://mcp.echo-op.com/oauth-mcp-powerpack-v1`

## Tools

See `src/tools.ts` — every tool is implemented.

## Run (MCP)

```bash
npm ci
npm run typecheck
npm test
npm run build
npm start
# MCP: http://127.0.0.1:8788/mcp
# Health: http://127.0.0.1:8788/health
```

## Governed mutates

Any write/control tool requires:

```json
{ "confirm": "EXECUTE" }
```

without that field the tool returns `confirm_required`.

## Data

Runtime state is written under `./data/` (gitignored): proposals, jobs, audit log.

## Identity

Commits: ECHO OMEGA PRIME \<bobbymcwilliams@echo-op.com\>
