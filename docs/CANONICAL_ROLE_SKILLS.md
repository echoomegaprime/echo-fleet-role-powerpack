# Canonical role skills (post-merge)

## Problem

Two enabled Codex plugins shipped same-named role skills with **different** bodies:

1. `echo-fleet-role-powerpack@echoomegaprime` (31 skills)
2. `echo-fleet-roles@echo-omega-prime-marketplace` (30–32 skills depending on cache revision)

With 101 plugins enabled, the skills context budget overflowed (603 skills stripped). Role skills became invisible, breaking mandatory `echo-fleet-roles:<role>-power` invocation.

## Decision

**Canonical skills plugin:** `echo-fleet-roles@echo-omega-prime-marketplace` (published from this repo under `.agents/plugins/marketplace.json`).

**Retired skills plugin:** `echo-fleet-role-powerpack@echoomegaprime` — do not co-enable.

### Merge policy (skill-by-skill)

| Skill | Winner body | Notes |
|---|---|---|
| All `echo-*-power` + `echo-reverse-engineering` + `echo-fleet-base` | Marketplace / CLAUDE_CODE_MARKETPLACE rich SKILL.md | Powerpack Codex stubs were much smaller |
| `echo-role-switching` | Powerpack Codex plugin | Only skill where powerpack body was richer |

Hashes for the surviving tree are pinned in [`SKILL_HASH_PIN.json`](./SKILL_HASH_PIN.json).

## Layout in this repo

```
.agents/plugins/marketplace.json          # marketplace name: echo-omega-prime-marketplace
plugins/echo-fleet-roles/                 # sole role-skills plugin (name: echo-fleet-roles)
  .codex-plugin/plugin.json
  skills/*/SKILL.md
  hooks/
  config/role_power_registry.json         # default_plugin -> echo-fleet-roles@…
```

The MCP HTTP server under `src/` is unrelated to skills enablement. Keep MCP if you need governed role activation over HTTP; never treat it as a second skills catalog.

## Operator commands

```bash
# Sync marketplace into ~/.codex/marketplaces/echo-omega-prime-marketplace,
# enable canonical plugin, disable duplicates / budget hogs, set features.apps=false
python3 scripts/remediate_codex_plugins.py --lean

# Verify: no "Exceeded skills context budget" warning; hashes match; role skills resolve
python3 scripts/verify_role_skills_budget.py
```

The remediator copies `.agents/` + `plugins/` to a durable `CODEX_HOME/marketplaces/` path so ephemeral build-target checkouts do not break the marketplace after cleanup.

Doctrine invocation examples (must resolve):

- `echo-fleet-roles:echo-judge-power`
- `echo-fleet-roles:echo-commander-power`
- `echo-fleet-roles:echo-builder-power`
- `echo-fleet-roles:echo-role-switching`
