#!/usr/bin/env python3
import argparse
from as_pirg_table3_common import ROWS, SOURCE, symmetric_relative_difference, write_json


def get(action, procedure, completion):
    return next(r for r in ROWS if r["action"] == action and r["procedure"] == procedure and r["g_completion"] == completion)


def delta(a, b):
    return {
        k: {
            "absolute": abs(a[k] - b[k]),
            "symmetric_relative": symmetric_relative_difference(a[k], b[k]),
        }
        for k in ("lambda", "g", "theta1", "theta2")
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    matched = {}
    for procedure, completion in (("flow", "back"), ("flow", "fluc"), ("nielsen", "back")):
        key = f"{procedure}_{completion}"
        matched[key] = delta(get("a", procedure, completion), get("b", procedure, completion))
    direct_vs_nielsen = {
        action: delta(get(action, "flow", "back"), get(action, "nielsen", "back"))
        for action in ("a", "b")
    }
    write_json(args.output, {
        "probe": "table3_matched_method_consistency",
        "source": SOURCE,
        "a_vs_b_matched": matched,
        "flow_vs_nielsen_same_back_completion": direct_vs_nielsen,
        "interpretation_boundary": "Matched comparisons quantify formulation/procedure sensitivity; they do not define equivalence of the target actions.",
    })


if __name__ == "__main__":
    main()
