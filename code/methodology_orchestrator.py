"""Deterministic fail-closed orchestrator for the KMQGB executable methodology.

The registry is data; this runner is the single machine entrypoint. It does not
reinterpret scientific outcomes: a registered script is authoritative for its
own PASS/BLOCKED/negative-control semantics. The orchestrator only requires
that every critical control exists and exits successfully as a regression test.

For CI wall-clock acceleration the registry may be partitioned into deterministic
non-overlapping shards. Sharding changes execution placement only: registry order,
PASS/FAIL semantics and the frozen scientific judge remain unchanged.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "protocol" / "EXECUTABLE_TEST_REGISTRY.json"
DEFAULT_SUMMARY = ROOT / "build" / "methodology_orchestrator_summary.json"
SUPPORTED_REGISTRY_VERSIONS = {"1.0", "1.1"}


def load_registry() -> dict:
    with REGISTRY.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if data.get("registry_version") not in SUPPORTED_REGISTRY_VERSIONS:
        raise ValueError("unsupported executable registry version")
    tests = data.get("tests")
    if not isinstance(tests, list) or not tests:
        raise ValueError("registry tests must be a non-empty list")

    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for index, item in enumerate(tests):
        if not isinstance(item, dict):
            raise ValueError(f"registry entry #{index} is not an object")
        tid = item.get("id")
        path = item.get("path")
        command = item.get("command")
        purpose = item.get("purpose")
        category = item.get("category")
        if not isinstance(tid, str) or not tid:
            raise ValueError(f"registry entry #{index} has invalid id")
        if tid in seen_ids:
            raise ValueError(f"duplicate registry id {tid}")
        seen_ids.add(tid)
        if not isinstance(path, str) or not path:
            raise ValueError(f"registry entry {tid} has invalid path")
        if path in seen_paths:
            raise ValueError(f"duplicate registry path {path}")
        seen_paths.add(path)
        if not isinstance(command, list) or len(command) < 2 or not all(isinstance(x, str) and x for x in command):
            raise ValueError(f"registry entry {tid} has invalid command")
        if command[0] not in {"python", "python3"} or command[1] != path:
            raise ValueError(f"registry entry {tid} command/path mismatch")
        if not isinstance(purpose, str) or not purpose.strip():
            raise ValueError(f"registry entry {tid} requires purpose")
        if not isinstance(category, str) or not category.strip():
            raise ValueError(f"registry entry {tid} requires category")
        absolute = ROOT / path
        if not absolute.is_file():
            raise FileNotFoundError(f"registered executable missing: {path}")
    return data


def select_shard(tests: list[dict], shard_index: int, shard_count: int) -> list[dict]:
    if shard_count < 1:
        raise ValueError("shard_count must be >= 1")
    if shard_index < 0 or shard_index >= shard_count:
        raise ValueError("shard_index must satisfy 0 <= shard_index < shard_count")
    selected = [item for index, item in enumerate(tests) if index % shard_count == shard_index]
    if not selected:
        raise ValueError(
            f"empty methodology shard: index={shard_index} count={shard_count} tests={len(tests)}"
        )
    return selected


def run_registry(timeout_s: int, shard_index: int = 0, shard_count: int = 1) -> dict:
    data = load_registry()
    selected = select_shard(data["tests"], shard_index, shard_count)
    env = dict(os.environ)
    env.setdefault("PYTHONHASHSEED", "0")
    results = []
    failed = False

    for item in selected:
        command = list(item["command"])
        command[0] = sys.executable
        try:
            proc = subprocess.run(
                command,
                cwd=ROOT,
                env=env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout_s,
                check=False,
            )
            result = {
                "id": item["id"],
                "path": item["path"],
                "category": item["category"],
                "returncode": proc.returncode,
                "stdout_tail": proc.stdout[-2000:],
                "stderr_tail": proc.stderr[-2000:],
                "status": "PASS" if proc.returncode == 0 else "FAIL",
            }
        except subprocess.TimeoutExpired as exc:
            result = {
                "id": item["id"],
                "path": item["path"],
                "category": item["category"],
                "returncode": None,
                "stdout_tail": (exc.stdout or "")[-2000:] if isinstance(exc.stdout, str) else "",
                "stderr_tail": (exc.stderr or "")[-2000:] if isinstance(exc.stderr, str) else "",
                "status": "TIMEOUT",
            }
        if result["status"] != "PASS":
            failed = True
        results.append(result)

    return {
        "registry_version": data["registry_version"],
        "rqir_core": data.get("rqir_core"),
        "registry_total": len(data["tests"]),
        "execution_mode": "single" if shard_count == 1 else "deterministic_shard",
        "shard_index": shard_index,
        "shard_count": shard_count,
        "total": len(results),
        "passed": sum(r["status"] == "PASS" for r in results),
        "failed": sum(r["status"] != "PASS" for r in results),
        "status": "PASS" if not failed else "FAIL",
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    args = parser.parse_args()

    if args.validate_only:
        data = load_registry()
        select_shard(data["tests"], args.shard_index, args.shard_count)
        print(
            f"PASS: executable registry valid; tests={len(data['tests'])}; "
            f"shard={args.shard_index}/{args.shard_count}"
        )
        return 0

    summary = run_registry(args.timeout, args.shard_index, args.shard_count)
    out = Path(args.summary)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")

    for result in summary["results"]:
        print(f"{result['status']}: {result['id']} -> {result['path']}")
        if result["status"] != "PASS" and result["stderr_tail"]:
            print(result["stderr_tail"], file=sys.stderr)

    print(
        f"methodology_orchestrator status={summary['status']} "
        f"passed={summary['passed']}/{summary['total']} "
        f"shard={summary['shard_index']}/{summary['shard_count']}"
    )
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
