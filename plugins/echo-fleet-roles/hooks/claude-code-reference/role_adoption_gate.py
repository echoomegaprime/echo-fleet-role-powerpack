#!/usr/bin/env python3
"""Plugin-local entrypoint — delegates to SYSTEMS/codex_auto/role_adoption_gate.py."""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
CANDIDATES = [
    HERE.parents[4] / "SYSTEMS" / "codex_auto" / "role_adoption_gate.py",  # repo root via marketplace
    HERE.parents[5] / "SYSTEMS" / "codex_auto" / "role_adoption_gate.py",
    Path(__file__).resolve().parents[2] / ".." / ".." / ".." / ".." / "SYSTEMS" / "codex_auto" / "role_adoption_gate.py",
]


def _find() -> Path:
    # Walk up looking for SYSTEMS/codex_auto/role_adoption_gate.py
    for parent in [HERE] + list(HERE.parents):
        candidate = parent / "SYSTEMS" / "codex_auto" / "role_adoption_gate.py"
        if candidate.is_file():
            return candidate
    # Marketplace layout: CLAUDE_CODE_MARKETPLACE/plugins/echo-fleet-roles/hooks -> repo root = parents[3]
    alt = HERE.parents[3] / "SYSTEMS" / "codex_auto" / "role_adoption_gate.py"
    if alt.is_file():
        return alt
    raise FileNotFoundError("role_adoption_gate.py not found relative to plugin hooks")


if __name__ == "__main__":
    target = _find()
    sys.argv[0] = str(target)
    runpy.run_path(str(target), run_name="__main__")
