#!/usr/bin/env python3
"""Exact V3K cross-source Toller projector kernel equivalence verifier."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp

PREREG_COMMIT = "d9b95dee3f090f828eb54cfed4432fb20f13a625"
SOURCE_INPUT_COMMIT = "98034792ccd2f87e05ab0d9b4fde46cd1bcf3033"
SOURCE_INPUT = Path("inputs/source_j1_coherent_magnetic_toller_bridge_v3.json")


def main(out_path: str) -> int:
    source = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    fs = source["formula_strings"]
    source_lock = (
        source["sources"]["A"]["arxiv"] == "2601.23162v1"
        and source["sources"]["B"]["arxiv"] == "2604.24945v1"
        and "Gamma(-j-i*rho)" in fs["A_EQ3"]
        and "prod_n=0^(j+l)" in fs["B_EQ20"]
    )

    # x=i*tilde_rho, y=i*rho.  Gamma recurrence gives
    # Gamma(2-x)/Gamma(-1-x)=(1-x)(-x)(-1-x)=x(1-x^2).
    x, y = sp.symbols("x y")
    recurrence_x = sp.expand((1 - x) * (-x) * (-1 - x))
    recurrence_y = sp.expand((1 - y) * (-y) * (-1 - y))
    recurrence_x_ok = sp.expand(recurrence_x - x * (1 - x**2)) == 0
    recurrence_y_ok = sp.expand(recurrence_y - y * (1 - y**2)) == 0

    # Source-A gamma ratio after exact recurrence reduction.
    fa_num = sp.expand(x * (1 - x**2))
    fa_den = sp.expand(y * (1 - y**2))

    # Source-B Eq. (20) finite product for j=l=1, n=0,1,2.
    fb_num = sp.expand((x + 1) * x * (x - 1))
    fb_den = sp.expand((y + 1) * y * (y - 1))

    cross_difference = sp.expand(fa_num * fb_den - fb_num * fa_den)

    # Negative controls.
    missing_middle_num = sp.expand((x + 1) * (x - 1))
    missing_middle_den = sp.expand((y + 1) * (y - 1))
    missing_middle_difference = sp.expand(
        fa_num * missing_middle_den - missing_middle_num * fa_den
    )

    wrong_range_num = sp.expand((x + 1) * x)  # two factors, j+l=1 fixture
    wrong_range_den = sp.expand((y + 1) * y)
    wrong_range_difference = sp.expand(
        fa_num * wrong_range_den - wrong_range_num * fa_den
    )

    controls = {
        "source_lock": bool(source_lock),
        "gamma_recurrence_x": bool(recurrence_x_ok),
        "gamma_recurrence_y": bool(recurrence_y_ok),
        "exact_cross_difference_zero": bool(cross_difference == 0),
        "negative_missing_middle_rejected": bool(missing_middle_difference != 0),
        "negative_wrong_range_rejected": bool(wrong_range_difference != 0),
    }
    passed = all(controls.values())
    classification = (
        "SOURCE_J1_TOLLER_PROJECTOR_KERNEL_EQUIVALENCE_CONFIRMED_SCOPED"
        if passed else "INVALID_IMPLEMENTATION"
    )
    out = {
        "gate": "SOURCE_J1_TOLLER_PROJECTOR_KERNEL_EQUIVALENCE_V3K",
        "prereg_commit": PREREG_COMMIT,
        "source_input_commit": SOURCE_INPUT_COMMIT,
        "classification": classification,
        "controls": controls,
        "derived_source_A_numerator": str(fa_num),
        "derived_source_A_denominator": str(fa_den),
        "source_B_numerator": str(fb_num),
        "source_B_denominator": str(fb_den),
        "cross_difference": str(cross_difference),
        "negative_missing_middle_difference": str(missing_middle_difference),
        "negative_wrong_range_difference": str(wrong_range_difference),
        "interpretation_ceiling": "Exact scalar projector-kernel equality for j=l=1 only; no full bridge, K5 contact, D7 closure, selector, or Candidate Gravity claim.",
    }
    p = Path(out_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"classification": classification, "controls_pass": passed, "cross_difference": str(cross_difference)}, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ns = ap.parse_args()
    raise SystemExit(main(ns.out))
