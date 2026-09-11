#!/usr/bin/env python3
import argparse
import math
from as_pirg_table3_common import ROWS, SOURCE, write_json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    c1, c2 = SOURCE["canonical_exponents"]
    rows = []
    for r in ROWS:
        d1 = (r["theta1"] - c1) / c1
        d2 = (r["theta2"] - c2) / c2
        rows.append({
            "id": r["id"],
            "theta1_relative_deviation_from_4": d1,
            "theta2_relative_deviation_from_2": d2,
            "two_exponent_relative_rms": math.sqrt((d1*d1 + d2*d2) / 2.0),
            "both_relevant_positive": r["theta1"] > 0 and r["theta2"] > 0,
        })
    write_json(args.output, {
        "probe": "table3_nearcanonical_relevance",
        "source": SOURCE,
        "rows": rows,
        "all_rows_keep_two_positive_relevant_exponents": all(x["both_relevant_positive"] for x in rows),
        "max_abs_theta1_relative_deviation": max(abs(x["theta1_relative_deviation_from_4"]) for x in rows),
        "max_abs_theta2_relative_deviation": max(abs(x["theta2_relative_deviation_from_2"]) for x in rows),
        "interpretation_boundary": "Tests Table-III relevance-counting stability only; does not establish UV-to-IR or scattering closure.",
    })


if __name__ == "__main__":
    main()
