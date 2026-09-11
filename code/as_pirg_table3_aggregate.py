#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from as_pirg_table3_common import SOURCE, write_json

EXPECTED = {
    "dispersion": "table3_global_dispersion",
    "nearcanonical": "table3_nearcanonical_relevance",
    "matched": "table3_matched_method_consistency",
    "scheme": "table3_scheme_sensitivity_decomposition",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    root = Path(args.input_dir)
    payloads = {}
    for label, probe in EXPECTED.items():
        path = root / f"{label}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("probe") != probe:
            raise SystemExit(f"unexpected probe for {label}: {data.get('probe')}")
        payloads[label] = data

    disp = payloads["dispersion"]["metrics"]
    near = payloads["nearcanonical"]
    summary = {
        "probe": "as_pirg_iter278_aggregate",
        "source": SOURCE,
        "all_four_independent_probes_present": True,
        "table3_global": {
            "lambda_range": disp["lambda"]["range"],
            "g_range": disp["g"]["range"],
            "theta1_cv_abs_mean": disp["theta1"]["cv_abs_mean"],
            "theta2_cv_abs_mean": disp["theta2"]["cv_abs_mean"],
            "all_rows_keep_two_positive_relevant_exponents": near["all_rows_keep_two_positive_relevant_exponents"],
            "max_abs_theta1_relative_deviation_from_canonical": near["max_abs_theta1_relative_deviation"],
            "max_abs_theta2_relative_deviation_from_canonical": near["max_abs_theta2_relative_deviation"],
        },
        "scientific_boundary": [
            "This audit independently quantifies the six published Table-III points.",
            "It supports a scoped positive statement about relevance-counting robustness, not a terminal Asymptotic-Safety family verdict.",
            "It does not supply the missing contact-complete s+t+u+A4 Lorentzian scattering package.",
            "It does not close the paper's explicitly deferred UV-to-IR phase structure, operator map, or comprehensive systematic-error budget.",
        ],
    }
    write_json(args.output, summary)


if __name__ == "__main__":
    main()
