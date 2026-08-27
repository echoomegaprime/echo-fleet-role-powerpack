#!/usr/bin/env python3
"""Remediate Codex plugin enablement for ECHO fleet role-skill correctness + budget.

Canonical decision (2026-08-25 overflow / ambiguity incident #34144):
  WINNER:  echo-fleet-roles@echo-omega-prime-marketplace
  RETIRED: echo-fleet-role-powerpack@echoomegaprime  (as a *skills* plugin only;
           this MCP connector package may still run as an HTTP MCP server)

Also cuts true duplicates and high-churn irrelevant plugins that blew the
skills context budget (603 skills dropped; role skills became invisible).

Every disable is justified in docs/PLUGIN_DISABLE_JUSTIFICATIONS.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))

# Marketplace id published by this repo's .agents/plugins/marketplace.json
CANONICAL_MARKETPLACE = "echo-omega-prime-marketplace"
CANONICAL_PLUGIN = "echo-fleet-roles"
CANONICAL_ID = f"{CANONICAL_PLUGIN}@{CANONICAL_MARKETPLACE}"

# Skills-plugin identity that must NEVER be co-enabled with the canonical plugin.
RETIRED_SKILLS_PLUGIN_IDS = (
    "echo-fleet-role-powerpack@echoomegaprime",
    "echo-fleet-role-powerpack@echoomegaprime-fleet-roles",
)

# Justified disables: plugin_id -> reason key (see docs/PLUGIN_DISABLE_JUSTIFICATIONS.md)
FORCE_DISABLE: dict[str, str] = {
    # True duplicates (same product, two marketplaces)
    "vercel@claude-plugins-official": "duplicate-vercel-claude-official",
    "vercel@openai-curated": "duplicate-vercel-keep-none-fleet-irrelevant",
    "figma@claude-plugins-official": "duplicate-figma-claude-official",
    "figma@openai-curated": "duplicate-figma-keep-none-fleet-irrelevant",
    # Massive skill contributors irrelevant to FORGE fleet builder work
    "anthropic-skills@claude-cowork": "budget-anthropic-skills-54",
    "huggingface-skills@claude-plugins-official": "budget-huggingface-25",
    "hugging-face@openai-curated": "budget-huggingface-openai-curated",
    "cloudflare@openai-curated": "cloudflare-mcp-unauthenticated-transport-fatal",
    "canva@openai-curated": "fleet-irrelevant-design-saas",
    "notion@openai-curated": "fleet-irrelevant-saas",
    "slack@openai-curated": "fleet-irrelevant-saas-use-echo-comms",
    "gmail@openai-curated": "fleet-irrelevant-saas",
    "google-drive@openai-curated": "budget-google-drive-skills",
    "openai-templates@openai-curated": "budget-openai-templates",
    "superpowers@openai-curated": "optional-large-skill-surface",
    "data-analytics@openai-curated": "optional-large-skill-surface",
    # Retired dual role-skills source
    "echo-fleet-role-powerpack@echoomegaprime": "retired-duplicate-role-skills-plugin",
}

# Keeplist when --lean is set: only these plugins stay enabled (plus canonical).
LEAN_KEEP_PREFIXES = (
    f"{CANONICAL_PLUGIN}@",
    "codex-security@",
    "echo-grounding@",
    "echo-security@",
    "echo-forge@",
    "echo-foreman@",
    "phoenix-recovery@",
    "crystal-memory@",
)


def _backup(path: Path) -> Path:
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = path.with_name(f"{path.name}.bak_skills_budget_{ts}")
    shutil.copy2(path, bak)
    return bak


def _parse_simple_toml_plugin_sections(text: str) -> dict[str, dict[str, str]]:
    """Minimal parser for [plugins."id"] enabled = bool sections.

    Avoids adding a tomllib dependency for older runtimes; only handles the
    shapes Codex writes for marketplaces/plugins.
    """
    sections: dict[str, dict[str, str]] = {}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1]
            sections[current] = {}
            continue
        if current is None or "=" not in line:
            continue
        key, _, val = line.partition("=")
        sections[current][key.strip()] = val.strip()
    return sections


def _render_config(existing_text: str, *, enable: list[str], disable: list[str]) -> str:
    """Rewrite/append plugin enablement while preserving non-plugin sections."""
    lines = existing_text.splitlines(keepends=True)
    out: list[str] = []
    skip_section = False

    managed_ids = set(enable) | set(disable)
    # Always drop prior managed plugin blocks + our features block (rewritten).
    drop_features = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            current_header = stripped[1:-1]
            if current_header == "features":
                # Drop entire features section; we re-append a known-good one.
                skip_section = True
                drop_features = True
                i += 1
                continue
            if current_header.startswith("plugins."):
                name = current_header[len("plugins.") :]
                if name.startswith('"') and name.endswith('"'):
                    name = name[1:-1]
                if name in managed_ids or name in RETIRED_SKILLS_PLUGIN_IDS:
                    skip_section = True
                    i += 1
                    continue
            skip_section = False
            out.append(line)
            i += 1
            continue
        if skip_section:
            i += 1
            continue
        out.append(line)
        i += 1

    body = "".join(out)
    if body and not body.endswith("\n"):
        body += "\n"
    if body and not body.endswith("\n\n"):
        body += "\n"

    blocks: list[str] = []
    # Avoid unauthenticated Cloudflare / apps MCP transport fatals at init.
    blocks.append("[features]")
    blocks.append("apps = false")
    blocks.append("")
    blocks.append("# --- managed by echo-fleet-role-powerpack scripts/remediate_codex_plugins.py ---")
    blocks.append(f"# canonical role skills: {CANONICAL_ID}")
    for pid in sorted(set(enable)):
        blocks.append(f'[plugins."{pid}"]')
        blocks.append("enabled = true")
        blocks.append("")
    for pid in sorted(set(disable)):
        blocks.append(f'[plugins."{pid}"]')
        blocks.append("enabled = false")
        blocks.append("")
    _ = drop_features  # lint quiet
    return body + "\n".join(blocks).rstrip() + "\n"


def sync_stable_marketplace(codex_home: Path, repo: Path, dry_run: bool) -> Path:
    """Copy marketplace surfaces into a durable CODEX_HOME path.

    Build-target checkouts are ephemeral; installing the marketplace from the
    repo worktree would break after the builder cleans up. Sync `.agents/` +
    `plugins/` into ~/.codex/marketplaces/<name>.
    """
    stable = codex_home / "marketplaces" / CANONICAL_MARKETPLACE
    if dry_run:
        print(f"DRY_RUN: sync {repo} -> {stable}")
        return stable
    if stable.exists():
        shutil.rmtree(stable)
    stable.mkdir(parents=True)
    for name in (".agents", "plugins"):
        src = repo / name
        if not src.exists():
            raise SystemExit(f"missing marketplace surface: {src}")
        shutil.copytree(src, stable / name)
    print(f"synced marketplace -> {stable}")
    return stable


def ensure_marketplace(codex_home: Path, repo: Path, dry_run: bool) -> None:
    stable = sync_stable_marketplace(codex_home, repo, dry_run)
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    cmd = ["codex", "plugin", "marketplace", "add", str(stable), "--json"]
    if dry_run:
        print("DRY_RUN:", " ".join(cmd))
        return
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True)
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    cfg = codex_home / "config.toml"
    text = cfg.read_text() if cfg.exists() else ""
    header = f"[marketplaces.{CANONICAL_MARKETPLACE}]"
    block = (
        f"{header}\n"
        f'source_type = "local"\n'
        f'source = "{stable}"\n'
    )
    if header not in text:
        with cfg.open("a") as f:
            f.write("\n" + block)
        print(f"appended marketplace {CANONICAL_MARKETPLACE} -> {stable}")
    else:
        # Force source path to the stable sync location.
        import re

        text2 = re.sub(
            rf"\[marketplaces\.{re.escape(CANONICAL_MARKETPLACE)}\][\s\S]*?(?=\n\[|\Z)",
            block + "\n",
            text,
            count=1,
        )
        cfg.write_text(text2)
        print(f"normalized marketplace source -> {stable}")

def install_canonical(codex_home: Path, dry_run: bool) -> None:
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    cmd = ["codex", "plugin", "add", CANONICAL_ID, "--json"]
    if dry_run:
        print("DRY_RUN:", " ".join(cmd))
        return
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True)
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    if proc.returncode != 0:
        raise SystemExit(f"failed to install {CANONICAL_ID}: exit {proc.returncode}")


def collect_disable_list(codex_home: Path, lean: bool) -> list[str]:
    disable = list(FORCE_DISABLE.keys())
    cfg = codex_home / "config.toml"
    if cfg.exists():
        sections = _parse_simple_toml_plugin_sections(cfg.read_text())
        for header, vals in sections.items():
            if not header.startswith("plugins."):
                continue
            name = header[len("plugins.") :]
            if name.startswith('"') and name.endswith('"'):
                name = name[1:-1]
            enabled = vals.get("enabled", "true").lower() == "true"
            if not enabled:
                continue
            if name == CANONICAL_ID:
                continue
            if any(name.startswith(p) for p in LEAN_KEEP_PREFIXES):
                continue
            if lean:
                disable.append(name)
            elif name in RETIRED_SKILLS_PLUGIN_IDS:
                disable.append(name)
    # always retire skills powerpack ids
    disable.extend(RETIRED_SKILLS_PLUGIN_IDS)
    # dedupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for d in disable:
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out


def write_justifications_snapshot(path: Path, disable: list[str]) -> None:
    rows = []
    for pid in disable:
        reason = FORCE_DISABLE.get(pid, "lean-pass-not-required-for-fleet-builder")
        if pid in RETIRED_SKILLS_PLUGIN_IDS:
            reason = "retired-duplicate-role-skills-plugin"
        rows.append({"plugin": pid, "enabled": False, "reason_key": reason})
    path.write_text(
        json.dumps(
            {
                "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                "canonical": CANONICAL_ID,
                "disabled": rows,
            },
            indent=2,
        )
        + "\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--codex-home", type=Path, default=DEFAULT_CODEX_HOME)
    ap.add_argument("--repo", type=Path, default=REPO)
    ap.add_argument("--lean", action="store_true", help="Disable every non-keeplist enabled plugin")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-install", action="store_true")
    args = ap.parse_args()

    codex_home: Path = args.codex_home
    codex_home.mkdir(parents=True, exist_ok=True)
    cfg = codex_home / "config.toml"
    if not cfg.exists():
        cfg.write_text("")

    if not args.dry_run:
        bak = _backup(cfg)
        print(f"backup: {bak}")

    ensure_marketplace(codex_home, args.repo.resolve(), args.dry_run)
    if not args.skip_install:
        install_canonical(codex_home, args.dry_run)

    disable = collect_disable_list(codex_home, lean=args.lean)
    enable = [CANONICAL_ID]

    new_text = _render_config(cfg.read_text(), enable=enable, disable=disable)
    if args.dry_run:
        print("--- proposed config.toml (plugins section managed) ---")
        print(new_text)
    else:
        cfg.write_text(new_text)
        snap = args.repo / "docs" / "DISABLED_PLUGINS_SNAPSHOT.json"
        write_justifications_snapshot(snap, disable)
        print(f"wrote {cfg}")
        print(f"wrote {snap}")
        print(f"enabled={enable}")
        print(f"disabled_count={len(disable)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
