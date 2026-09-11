#!/usr/bin/env python3
import argparse
import statistics
from as_pirg_table3_common import ROWS, SOURCE, write_json


def stats(values):
    mean = statistics.fmean(values)
    sd = statistics.pstdev(values)
    return {
        "min": min(values),
        "max": max(values),
        "range": max(values) - min(values),
        "mean": mean,
        "population_sd": sd,
        "cv_abs_mean": None if mean == 0 else sd / abs(mean),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    metrics = {k: stats([r[k] for r in ROWS]) for k in ("lambda", "g", "theta1", "theta2")}
    by_action = {}
    for action in ("a", "b"):
        subset = [r for r in ROWS if r["action"] == action]
        by_action[action] = {k: stats([r[k] for r in subset]) for k in ("lambda", "g", "theta1", "theta2")}
    write_json(args.output, {
        "probe": "table3_global_dispersion",
        "source": SOURCE,
        "metrics": metrics,
        "by_action": by_action,
        "interpretation_boundary": "Descriptive dispersion only; no family-level status promotion is encoded.",
    })


if __name__ == "__main__":
    main()
