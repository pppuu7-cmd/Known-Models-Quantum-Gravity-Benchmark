#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

PRESENT_MATCH = "PRESENT_IDENTITY_MATCH"
PRESENT_MISMATCH = "PRESENT_IDENTITY_MISMATCH"
MISSING = "MISSING_OR_UNAVAILABLE"
DOWNLOAD_FAILED = "DOWNLOAD_FAILED"
NOT_EXERCISED = "NOT_EXERCISED_CONTROL"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_cmd(argv: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, text=True, capture_output=True, check=False)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--simulate-missing-role")
    ap.add_argument("--control-only", action="store_true")
    args = ap.parse_args()

    authority = load_json(Path(args.authority))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    terminal_run = authority["terminal_run"]
    run_id = int(terminal_run["id"])

    run_proc = run_cmd(["gh", "api", f"repos/{args.repo}/actions/runs/{run_id}"])
    run_observed: dict[str, Any] | None = None
    run_identity_ok = False
    if run_proc.returncode == 0:
        try:
            run_observed = json.loads(run_proc.stdout)
            run_identity_ok = (
                run_observed.get("id") == run_id
                and run_observed.get("status") == terminal_run.get("status")
                and run_observed.get("conclusion") == terminal_run.get("conclusion")
                and run_observed.get("head_sha") == terminal_run.get("head_sha")
            )
        except Exception:
            run_observed = None

    artifacts_proc = run_cmd([
        "gh", "api", f"repos/{args.repo}/actions/runs/{run_id}/artifacts?per_page=100"
    ])
    artifacts: list[dict[str, Any]] = []
    if artifacts_proc.returncode == 0:
        try:
            artifacts = json.loads(artifacts_proc.stdout).get("artifacts", [])
        except Exception:
            artifacts = []

    entries: list[dict[str, Any]] = []
    simulated_role = args.simulate_missing_role
    nonexistent_name = authority["boundary_control"]["nonexistent_name"]

    for req in authority["required_terminal_artifacts"]:
        role = req["role"]
        if args.control_only and role != simulated_role:
            entries.append({
                "role": role,
                "required_name": req["name"],
                "lookup_name": req["name"],
                "state": NOT_EXERCISED,
                "download_attempted": False,
                "download_returncode": None,
                "local_path": None,
            })
            continue

        lookup_name = nonexistent_name if role == simulated_role else req["name"]
        matches = [a for a in artifacts if a.get("name") == lookup_name]
        observed = matches[0] if len(matches) == 1 else None
        role_dir = out_dir / role
        role_dir.mkdir(parents=True, exist_ok=True)
        expected_local = role_dir / req["relative_path"]

        entry: dict[str, Any] = {
            "role": role,
            "required_name": req["name"],
            "lookup_name": lookup_name,
            "expected_id": req["id"],
            "expected_digest": req["digest"],
            "metadata_match_count": len(matches),
            "observed_id": observed.get("id") if observed else None,
            "observed_digest": observed.get("digest") if observed else None,
            "observed_expired": observed.get("expired") if observed else None,
            "download_attempted": False,
            "download_returncode": None,
            "local_path": None,
            "local_file_sha256": None,
        }

        if observed is not None and role != simulated_role:
            identity_match = (
                observed.get("id") == req["id"]
                and observed.get("digest") == req["digest"]
            )
            if not identity_match:
                entry["state"] = PRESENT_MISMATCH
                entries.append(entry)
                continue

        should_attempt_download = True
        if should_attempt_download:
            dl = run_cmd([
                "gh", "run", "download", str(run_id),
                "--repo", args.repo,
                "--name", lookup_name,
                "--dir", str(role_dir),
            ])
            entry["download_attempted"] = True
            entry["download_returncode"] = dl.returncode

        if role == simulated_role:
            entry["state"] = MISSING if entry["download_returncode"] != 0 else PRESENT_MISMATCH
            entries.append(entry)
            continue

        if observed is None or observed.get("expired") is True:
            entry["state"] = MISSING
            entries.append(entry)
            continue

        if entry["download_returncode"] != 0:
            entry["state"] = DOWNLOAD_FAILED
            entries.append(entry)
            continue

        if not expected_local.exists():
            entry["state"] = DOWNLOAD_FAILED
            entries.append(entry)
            continue

        entry["state"] = PRESENT_MATCH
        entry["local_path"] = str(expected_local)
        entry["local_file_sha256"] = sha256_file(expected_local)
        entries.append(entry)

    manifest = {
        "gate": authority["gate"],
        "mode": "boundary_control" if simulated_role else "production",
        "terminal_run_expected": terminal_run,
        "run_query_returncode": run_proc.returncode,
        "run_observed": {
            "id": run_observed.get("id") if run_observed else None,
            "status": run_observed.get("status") if run_observed else None,
            "conclusion": run_observed.get("conclusion") if run_observed else None,
            "head_sha": run_observed.get("head_sha") if run_observed else None,
        },
        "run_identity_ok": run_identity_ok,
        "artifact_query_returncode": artifacts_proc.returncode,
        "simulate_missing_role": simulated_role,
        "entries": entries,
    }
    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":"))
    manifest["manifest_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(args.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(args.manifest).write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "mode": manifest["mode"],
        "run_identity_ok": run_identity_ok,
        "states": {e["role"]: e["state"] for e in entries},
        "manifest_sha256": manifest["manifest_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
