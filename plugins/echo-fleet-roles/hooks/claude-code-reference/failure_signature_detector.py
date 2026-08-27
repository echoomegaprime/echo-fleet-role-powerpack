#!/usr/bin/env python3
"""PostToolUse failure-signature detector → troubleshooter switch.

Fires on runtime failures in TOOL OUTPUT (non-zero exit / 500 / timeout /
traceback / transport_failed), not merely prompt text. Fail-open.
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SIGNATURES = [
    re.compile(r"\btraceback\b", re.I),
    re.compile(r"\btransport_failed\b", re.I),
    re.compile(r"\btimeout\b", re.I),
    re.compile(r"\btimed out\b", re.I),
    re.compile(r"\bHTTP\s*500\b", re.I),
    re.compile(r"\bstatus[=:\s]+500\b", re.I),
    re.compile(r"\bexit(?:_status|code)?[=:\s]+(?!0)\d+\b", re.I),
    re.compile(r"\bnon-?zero exit\b", re.I),
    re.compile(r"Command failed with exit code (?!0)\d+", re.I),
]


def _state_path() -> Path:
    override = os.environ.get("ECHO_FAILURE_SIG_STATE")
    if override:
        return Path(override)
    if os.name == "nt":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home())) / "EchoFleetRoles"
    else:
        base = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local" / "state")) / "echo-fleet-roles"
    base.mkdir(parents=True, exist_ok=True)
    return base / "failure_signatures.jsonl"


def extract_output(payload: dict[str, Any]) -> str:
    chunks: list[str] = []
    for key in ("tool_output", "output", "stdout", "stderr", "result", "content", "error"):
        val = payload.get(key)
        if isinstance(val, str):
            chunks.append(val)
        elif isinstance(val, dict):
            chunks.append(json.dumps(val))
    # Nested Claude/Codex shapes
    for nest in ("tool_response", "response", "tool_result"):
        val = payload.get(nest)
        if isinstance(val, str):
            chunks.append(val)
        elif isinstance(val, dict):
            chunks.append(json.dumps(val))
    exit_code = payload.get("exit_code", payload.get("exitCode"))
    if exit_code is not None and str(exit_code) not in {"0", "None"}:
        chunks.append(f"exit_code={exit_code}")
    return "\n".join(chunks)


def detect(output: str) -> list[str]:
    hits: list[str] = []
    for rx in SIGNATURES:
        if rx.search(output or ""):
            hits.append(rx.pattern)
    return hits


def main() -> int:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
        output = extract_output(payload)
        hits = detect(output)
        result: dict[str, Any] = {
            "hits": hits,
            "troubleshooter_switch": bool(hits),
            "at": datetime.now(timezone.utc).isoformat(),
        }
        if hits:
            result["recommended_role"] = "troubleshooter"
            result["additionalContext"] = (
                "ECHO failure-signature detector: runtime failure observed "
                f"({', '.join(hits[:3])}). MANDATORY switch toward troubleshooter; "
                "Load echo-fleet-roles:echo-troubleshooter-power and run sol_cli.py role switch troubleshooter."
            )
            # Best-effort session advisor update when session_id present
            session_id = payload.get("session_id") or os.environ.get("ECHO_SESSION_ID")
            if session_id:
                try:
                    from delegation_role_advisor import apply_detection

                    apply_detection(
                        "fix the runtime failure traceback timeout 500 transport_failed",
                        session_id=str(session_id),
                        current_role=payload.get("current_role"),
                    )
                except Exception:  # noqa: BLE001
                    pass
            try:
                with _state_path().open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps(result) + "\n")
            except Exception:  # noqa: BLE001
                pass
            print(json.dumps({"additionalContext": result["additionalContext"], "detector": result}))
        else:
            print(json.dumps({"ok": True, "hits": []}))
        return 0
    except Exception as exc:  # noqa: BLE001 — fail-open
        print(json.dumps({"ok": True, "fail_open": True, "error": str(exc)}))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
