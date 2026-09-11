#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

PUBLISHED = {
    "Newton_response_G": 23.200280752211107,
    "mass_gap": 0.4863395672466658,
    "dimensionless_gravity_number_G_gap2": 5.487473657582965,
    "mixed_geometry_matter_response": 13.102173996407302,
}


def rel_delta(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), 1.0e-30)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.input)
    records: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        try:
            item = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if item.get("probe_type") in {"hilbert_cutoff", "quartic_coupling", "mixed_response_step"}:
            item["_source"] = str(path)
            records.append(item)
    if not records:
        raise SystemExit("no probe records found")

    cutoffs = sorted(
        [r for r in records if r["probe_type"] == "hilbert_cutoff"],
        key=lambda r: r["result"]["cutoff"],
    )
    quartics = sorted(
        [r for r in records if r["probe_type"] == "quartic_coupling"],
        key=lambda r: r["quartic_factor"],
    )
    steps = sorted(
        [r for r in records if r["probe_type"] == "mixed_response_step"],
        key=lambda r: r["result"]["sigma_step"],
    )

    required_cutoffs = {4, 6, 8, 10, 12, 14, 16}
    required_quartics = {0.0, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0}
    required_steps = {0.0005, 0.001, 0.002, 0.005, 0.01}
    if {int(r["result"]["cutoff"]) for r in cutoffs} != required_cutoffs:
        raise SystemExit("incomplete cutoff probe set")
    if {float(r["quartic_factor"]) for r in quartics} != required_quartics:
        raise SystemExit("incomplete quartic probe set")
    if {float(r["result"]["sigma_step"]) for r in steps} != required_steps:
        raise SystemExit("incomplete mixed-response step probe set")

    cutoff8 = next(r["result"] for r in cutoffs if int(r["result"]["cutoff"]) == 8)
    quartic1 = next(r["result"] for r in quartics if float(r["quartic_factor"]) == 1.0)
    step001 = next(r["result"] for r in steps if math.isclose(float(r["result"]["sigma_step"]), 0.001))

    base_checks = {
        "cutoff8_Newton_response_G": rel_delta(cutoff8["Newton_response_G"], PUBLISHED["Newton_response_G"]),
        "cutoff8_mass_gap": rel_delta(cutoff8["mass_gap"], PUBLISHED["mass_gap"]),
        "cutoff8_dimensionless_gravity": rel_delta(cutoff8["dimensionless_gravity_number_G_gap2"], PUBLISHED["dimensionless_gravity_number_G_gap2"]),
        "quartic1_Newton_response_G": rel_delta(quartic1["Newton_response_G"], PUBLISHED["Newton_response_G"]),
        "step001_mixed_response": rel_delta(step001["mixed_geometry_matter_response"], PUBLISHED["mixed_geometry_matter_response"]),
    }
    base_reproduction_pass = max(base_checks.values()) <= 1.0e-8

    cutoff_rows = [r["result"] for r in cutoffs]
    cutoff_high = cutoff_rows[-1]
    cutoff_prev = cutoff_rows[-2]
    cutoff_summary = {
        "rows": cutoff_rows,
        "positive_Newton_all_cutoffs": all(float(r["Newton_response_G"]) > 0.0 for r in cutoff_rows),
        "G_relative_change_cutoff14_to16": rel_delta(cutoff_prev["Newton_response_G"], cutoff_high["Newton_response_G"]),
        "gap_relative_change_cutoff14_to16": rel_delta(cutoff_prev["mass_gap"], cutoff_high["mass_gap"]),
        "gamma_relative_change_cutoff14_to16": rel_delta(cutoff_prev["dimensionless_gravity_number_G_gap2"], cutoff_high["dimensionless_gravity_number_G_gap2"]),
        "cutoff8_to16_G_relative_change": rel_delta(cutoff8["Newton_response_G"], cutoff_high["Newton_response_G"]),
        "interpretation_rule": "diagnostic only; no cutoff-convergence threshold authorizes family-level promotion",
    }

    quartic_rows = [
        {
            "factor": float(r["quartic_factor"]),
            **r["result"],
        }
        for r in quartics
    ]
    quartic_summary = {
        "rows": quartic_rows,
        "positive_Newton_over_declared_grid": all(float(r["Newton_response_G"]) > 0.0 for r in quartic_rows),
        "G_min": min(float(r["Newton_response_G"]) for r in quartic_rows),
        "G_max": max(float(r["Newton_response_G"]) for r in quartic_rows),
        "gamma_min": min(float(r["dimensionless_gravity_number_G_gap2"]) for r in quartic_rows),
        "gamma_max": max(float(r["dimensionless_gravity_number_G_gap2"]) for r in quartic_rows),
        "interpretation_rule": "finite grid robustness only; not proof for arbitrary coupling or family scope",
    }

    step_rows = [r["result"] for r in steps]
    responses = [float(r["mixed_geometry_matter_response"]) for r in step_rows]
    step_summary = {
        "rows": step_rows,
        "response_span": max(responses) - min(responses),
        "response_relative_span": (max(responses) - min(responses)) / max(abs(sum(responses) / len(responses)), 1.0e-30),
        "smallest_step_error_estimate": min(float(r["Richardson_error_estimate"]) for r in step_rows),
        "interpretation_rule": "numerical discretization robustness only",
    }

    summary = {
        "schema_version": "1.0",
        "status": "PASS_PROBE_BATCH" if base_reproduction_pass else "FAIL_BASE_REPRODUCTION",
        "claim_boundary": "These probes can strengthen or weaken the scoped fixed-band robustness assessment. They cannot close the all-band/background-independent RQCP family blocker or authorize D7.",
        "published_base_reproduction": {
            "pass": base_reproduction_pass,
            "relative_deltas": base_checks,
            "maximum_allowed_relative_delta": 1.0e-8,
        },
        "hilbert_cutoff_probe": cutoff_summary,
        "quartic_coupling_probe": quartic_summary,
        "mixed_response_step_probe": step_summary,
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if base_reproduction_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
