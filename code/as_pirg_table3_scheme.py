#!/usr/bin/env python3
import argparse
from as_pirg_table3_common import ROWS, SOURCE, write_json


def get(action, procedure, completion):
    return next(r for r in ROWS if r["action"] == action and r["procedure"] == procedure and r["g_completion"] == completion)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    results = {}
    for action in ("a", "b"):
        flow_back = get(action, "flow", "back")
        flow_fluc = get(action, "flow", "fluc")
        nielsen_back = get(action, "nielsen", "back")
        rows = {}
        for key in ("lambda", "g", "theta1", "theta2"):
            completion_shift = abs(flow_fluc[key] - flow_back[key])
            procedure_shift = abs(nielsen_back[key] - flow_back[key])
            rows[key] = {
                "beta_g_completion_shift": completion_shift,
                "flow_vs_nielsen_shift_same_back_completion": procedure_shift,
                "procedure_to_completion_shift_ratio": None if completion_shift == 0 else procedure_shift / completion_shift,
            }
        results[action] = rows
    write_json(args.output, {
        "probe": "table3_scheme_sensitivity_decomposition",
        "source": SOURCE,
        "by_action": results,
        "interpretation_boundary": "Finite Table-III decomposition of two documented choices; not a complete regulator/truncation uncertainty budget.",
    })


if __name__ == "__main__":
    main()
