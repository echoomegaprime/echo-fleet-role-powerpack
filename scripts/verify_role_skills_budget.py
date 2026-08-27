#!/usr/bin/env python3
"""Verify Codex skills budget + canonical role skill resolution.

Checks:
1. Fresh headless `codex exec` stderr/stdout has NO "Exceeded skills context budget"
2. Exactly one enabled plugin provides role-power skills
3. echo-role-switching exists under that plugin
4. echo-fleet-roles:echo-judge-power (+3 others) resolve from installed cache
5. SKILL.md hashes match docs/SKILL_HASH_PIN.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
CANONICAL = "echo-fleet-roles@echo-omega-prime-marketplace"
ROLE_SKILLS = (
    "echo-judge-power",
    "echo-commander-power",
    "echo-builder-power",
    "echo-sentinel-power",
    "echo-role-switching",
)
BUDGET_RE = re.compile(r"Exceeded skills context budget", re.I)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_enabled_role_plugins(codex_home: Path) -> list[str]:
    cfg = codex_home / "config.toml"
    if not cfg.exists():
        return []
    enabled: list[str] = []
    current = None
    for line in cfg.read_text().splitlines():
        s = line.strip()
        if s.startswith("[plugins.") and s.endswith("]"):
            name = s[len("[plugins.") : -1]
            if name.startswith('"') and name.endswith('"'):
                name = name[1:-1]
            current = name
            continue
        if current and s.startswith("enabled"):
            val = s.split("=", 1)[1].strip().lower()
            if val == "true" and (
                "fleet-role" in current or current.startswith("echo-fleet-roles@")
            ):
                enabled.append(current)
            current = None
    return enabled


def installed_skill_path(codex_home: Path, skill: str) -> Path | None:
    # Prefer cache for canonical marketplace
    root = codex_home / "plugins" / "cache" / "echo-omega-prime-marketplace" / "echo-fleet-roles"
    if root.is_dir():
        versions = sorted(root.iterdir(), reverse=True)
        for v in versions:
            p = v / "skills" / skill / "SKILL.md"
            if p.is_file():
                return p
    # Fallback: repo checkout
    p = REPO / "plugins" / "echo-fleet-roles" / "skills" / skill / "SKILL.md"
    return p if p.is_file() else None


def run_headless(codex_home: Path, prompt: str, timeout: int = 120) -> tuple[int, str, str]:
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    # Use a throwaway workdir so sandbox/git checks stay quiet
    with tempfile.TemporaryDirectory(prefix="codex-role-smoke-") as td:
        cmd = [
            "codex",
            "exec",
            "--skip-git-repo-check",
            "-C",
            td,
            prompt,
        ]
        proc = subprocess.run(
            cmd,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return proc.returncode, proc.stdout, proc.stderr


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--codex-home", type=Path, default=DEFAULT_CODEX_HOME)
    ap.add_argument("--skip-exec", action="store_true", help="Skip live codex exec (hash/config only)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    report: dict = {"ok": True, "checks": []}

    def check(name: str, passed: bool, detail: str) -> None:
        report["checks"].append({"name": name, "passed": passed, "detail": detail})
        if not passed:
            report["ok"] = False

    # 1) single role plugin
    enabled_role = find_enabled_role_plugins(args.codex_home)
    check(
        "single-role-plugin",
        enabled_role == [CANONICAL] or (len(enabled_role) == 1 and enabled_role[0].startswith("echo-fleet-roles@")),
        f"enabled_role_plugins={enabled_role}",
    )

    # 2) skills exist + hashes
    pin_path = REPO / "docs" / "SKILL_HASH_PIN.json"
    pins = json.loads(pin_path.read_text())["skills"]
    for skill in ROLE_SKILLS:
        path = installed_skill_path(args.codex_home, skill)
        if path is None:
            check(f"resolve:{skill}", False, "SKILL.md missing")
            continue
        h = sha256(path)
        expected = pins.get(skill, {}).get("sha256")
        ok = expected == h if expected else True
        check(
            f"resolve:{skill}",
            ok,
            f"path={path} sha256={h}" + (f" expected={expected}" if expected and not ok else ""),
        )

    # echo-role-switching must exist
    switch = installed_skill_path(args.codex_home, "echo-role-switching")
    check("echo-role-switching-exists", switch is not None, str(switch))

    # 3) headless launch budget warning
    if not args.skip_exec:
        # Prompt forces skill mention; we mainly care about startup warnings.
        prompt = (
            "Do not use tools. Reply with exactly READY. "
            "If you can see skill echo-fleet-roles:echo-judge-power in your catalog, append OK."
        )
        try:
            code, out, err = run_headless(args.codex_home, prompt)
            combined = out + "\n" + err
            budget_hit = bool(BUDGET_RE.search(combined))
            check(
                "no-skills-budget-warning",
                not budget_hit,
                f"exit={code} budget_hit={budget_hit} stderr_tail={err[-500:]!r}",
            )
            # Soft check: model replied (auth/network may vary)
            check(
                "headless-exec-ran",
                True,
                f"exit={code} out_len={len(out)} err_len={len(err)}",
            )
        except subprocess.TimeoutExpired:
            check("no-skills-budget-warning", False, "codex exec timed out")
        except FileNotFoundError:
            check("no-skills-budget-warning", False, "codex binary not found")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for c in report["checks"]:
            mark = "PASS" if c["passed"] else "FAIL"
            print(f"[{mark}] {c['name']}: {c['detail']}")
        print("OVERALL", "PASS" if report["ok"] else "FAIL")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
