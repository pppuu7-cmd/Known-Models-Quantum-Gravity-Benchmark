"""Fail-closed merger for deterministic KMQGB methodology shards.

Each registered executable test must appear exactly once across the shard
summaries. The merger restores canonical registry order and refuses to emit a
PASS summary if any shard is missing, duplicated, malformed, or non-PASS.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from methodology_orchestrator import DEFAULT_SUMMARY, load_registry


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", default="build/shards")
    parser.add_argument("--expected-shards", type=int, required=True)
    parser.add_argument("--output", default=str(DEFAULT_SUMMARY))
    args = parser.parse_args()

    if args.expected_shards < 1:
        raise SystemExit("expected_shards must be >= 1")

    root = Path(args.input_dir)
    files = sorted(root.rglob("shard-*.json"))
    if len(files) != args.expected_shards:
        raise SystemExit(
            f"expected {args.expected_shards} shard summaries, found {len(files)} in {root}"
        )

    registry = load_registry()
    expected_order = [item["id"] for item in registry["tests"]]
    expected_ids = set(expected_order)
    seen_shards: set[int] = set()
    results_by_id: dict[str, dict] = {}

    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("registry_version") != registry["registry_version"]:
            raise SystemExit(f"registry version mismatch in {path}")
        if data.get("rqir_core") != registry.get("rqir_core"):
            raise SystemExit(f"RQIR core mismatch in {path}")
        if data.get("shard_count") != args.expected_shards:
            raise SystemExit(f"shard_count mismatch in {path}")
        shard_index = data.get("shard_index")
        if not isinstance(shard_index, int) or not 0 <= shard_index < args.expected_shards:
            raise SystemExit(f"invalid shard_index in {path}")
        if shard_index in seen_shards:
            raise SystemExit(f"duplicate shard_index {shard_index}")
        seen_shards.add(shard_index)
        if data.get("status") != "PASS":
            raise SystemExit(f"non-PASS shard {shard_index}: {data.get('status')}")

        results = data.get("results")
        if not isinstance(results, list) or not results:
            raise SystemExit(f"missing results in {path}")
        for result in results:
            tid = result.get("id")
            if tid not in expected_ids:
                raise SystemExit(f"unexpected test id {tid!r} in {path}")
            if tid in results_by_id:
                raise SystemExit(f"duplicate test result {tid}")
            if result.get("status") != "PASS" or result.get("returncode") != 0:
                raise SystemExit(f"non-PASS test result {tid}")
            results_by_id[tid] = result

    if seen_shards != set(range(args.expected_shards)):
        raise SystemExit(
            f"shard coverage mismatch: observed={sorted(seen_shards)} "
            f"expected={list(range(args.expected_shards))}"
        )

    missing = [tid for tid in expected_order if tid not in results_by_id]
    extra = sorted(set(results_by_id) - expected_ids)
    if missing or extra:
        raise SystemExit(f"test coverage mismatch: missing={missing} extra={extra}")

    ordered_results = [results_by_id[tid] for tid in expected_order]
    summary = {
        "registry_version": registry["registry_version"],
        "rqir_core": registry.get("rqir_core"),
        "registry_total": len(expected_order),
        "execution_mode": "parallel_deterministic_shards",
        "shard_count": args.expected_shards,
        "total": len(ordered_results),
        "passed": len(ordered_results),
        "failed": 0,
        "status": "PASS",
        "results": ordered_results,
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    print(
        f"methodology_shard_merge status=PASS passed={summary['passed']}/{summary['total']} "
        f"shards={args.expected_shards}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
