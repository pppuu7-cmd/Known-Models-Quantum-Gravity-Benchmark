#!/usr/bin/env python3
"""Iter417 exact source-support collision parity audit.

This is a deliberately scoped algebraic gate for the K5 causal-sector support
kappa_ab = sigma_a sigma_b (global sigma flip quotiented by fixing sigma_0=+1).

For a k-vertex collision cluster S, assume only the leading branch-residue sign
relation R_- = -(1+eps) R_+ on every singular wedge.  The script exhaustively
sums all 16 source-supported causal sectors and the co-causal partner and
records whether the leading homogeneous coefficient cancels.

This does NOT establish vertex convergence: it tests only leading-coefficient
cancellation under a frozen residue relation.  Nonleading terms, Haar measure,
boundary contraction, i-epsilon distribution products and absolute
normalisation remain outside scope.
"""
from __future__ import annotations
import argparse, itertools, json, math
from pathlib import Path

VERTICES = tuple(range(5))
SIGMAS = [(1,) + tail for tail in itertools.product((-1, 1), repeat=4)]


def wedge_sign_product(sig, subset):
    z = 1
    for a, b in itertools.combinations(subset, 2):
        z *= sig[a] * sig[b]
    return z


def branch_weight(sign: int, eps: float):
    # R_+=1, R_-=-(1+eps)
    return 1.0 if sign > 0 else -(1.0 + eps)


def sector_leading(sig, subset, eps: float, cocausal: bool = False):
    z = 1.0
    for a, b in itertools.combinations(subset, 2):
        kappa = sig[a] * sig[b]
        if cocausal:
            kappa = -kappa
        z *= branch_weight(kappa, eps)
    return z


def audit(k: int, eps: float):
    rows = []
    for subset in itertools.combinations(VERTICES, k):
        cp = sum(sector_leading(s, subset, eps, False) for s in SIGMAS)
        cm = sum(sector_leading(s, subset, eps, True) for s in SIGMAS)
        cb = cp + cm
        e = k * (k - 1) // 2
        exact_sign_sum = sum(wedge_sign_product(s, subset) for s in SIGMAS)
        scale = max(1.0, sum(abs(sector_leading(s, subset, eps, False)) for s in SIGMAS))
        rows.append({
            "subset": subset,
            "edges_in_cluster": e,
            "source_sector_count": len(SIGMAS),
            "exact_kappa_product_sum": exact_sign_sum,
            "Cplus_leading": cp,
            "Cminus_leading": cm,
            "Cboth_leading": cb,
            "Cplus_relative": abs(cp) / scale,
            "Cboth_relative": abs(cb) / (2.0 * scale),
            "Cplus_cancel_1e12": abs(cp) <= 1e-12 * scale,
            "Cboth_cancel_1e12": abs(cb) <= 2e-12 * scale,
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, required=True, choices=(2,3,4,5))
    ap.add_argument("--eps", type=float, required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    rows = audit(args.k, args.eps)
    result = {
        "iteration": 417,
        "family": "LQG_SPINFOAM_TOLLER",
        "gate": "SOURCE_SPECIFIC_SIGMA_SECTOR_MULTI_COLLISION_LEADING_PARITY",
        "k": args.k,
        "eps_residue_antisymmetry_breaking": args.eps,
        "subsets_checked": len(rows),
        "all_Cplus_cancel": all(r["Cplus_cancel_1e12"] for r in rows),
        "all_Cboth_cancel": all(r["Cboth_cancel_1e12"] for r in rows),
        "max_Cplus_relative": max(r["Cplus_relative"] for r in rows),
        "max_Cboth_relative": max(r["Cboth_relative"] for r in rows),
        "rows": rows,
        "guardrail": "Conditional leading-coefficient algebra only; not a finiteness, distribution-product, or normalization theorem."
    }
    p = Path(args.output); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}, indent=2))

if __name__ == "__main__":
    main()
