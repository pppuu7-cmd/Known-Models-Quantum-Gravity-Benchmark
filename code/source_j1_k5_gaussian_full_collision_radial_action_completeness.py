#!/usr/bin/env python3
"""Exact certificate for the full-collision radial action space through derivative order 26."""

from __future__ import annotations

import argparse
import json
from math import comb, factorial
from pathlib import Path

DIM = 4
ORDER_CAP = 26
PARENT_RESULT = "results/SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_TERMINAL_2026-09-15.md"
A_CAL = ("0.50","0.60","0.70","0.80","0.90","1.00","1.10","1.20","1.30","1.40","1.50","1.60","1.70","1.80")
A_TEST = ("0.55","0.95","1.35","1.75","1.95")


def multiindices_leq(dim: int, cap: int):
    out = []
    def rec(prefix, remaining_dim, remaining_cap):
        if remaining_dim == 1:
            for v in range(remaining_cap + 1):
                out.append(tuple(prefix + [v]))
            return
        for v in range(remaining_cap + 1):
            rec(prefix + [v], remaining_dim - 1, remaining_cap - v)
    rec([], dim, cap)
    return out


def radial_action(beta):
    """Return (degree, exact integer coefficient), or None if the radial action vanishes."""
    if any(b % 2 for b in beta):
        return None
    ms = [b // 2 for b in beta]
    degree = sum(ms)
    # <partial^beta delta, phi> = (-1)^|beta| partial^beta phi(0).
    # Surviving |beta| is even, so the distributional outer sign is +1.
    coeff = 1
    for m in ms:
        coeff *= ((-1) ** m) * factorial(2 * m) // factorial(m)
    return degree, coeff


def polynomial_add(a, b):
    out = dict(a)
    for d, c in b.items():
        out[d] = out.get(d, 0) + c
        if out[d] == 0:
            del out[d]
    return out


def polynomial_scale(a, k):
    return {d: c * k for d, c in a.items() if c * k}


def derivative_1d_even(m: int):
    """d^(2m) exp(-alpha x^2)|0 as alpha-polynomial."""
    return {m: ((-1) ** m) * factorial(2 * m) // factorial(m)}


def derivative_with_x2_factor(order: int):
    """d^order [exp(-alpha x^2)*(1+x^2)] at x=0 as exact alpha-polynomial."""
    if order % 2:
        return {}
    m = order // 2
    base = derivative_1d_even(m)
    # Leibniz contribution from x^2: choose(order,2)*2!*d^(order-2) exp(-alpha x^2)|0.
    if order >= 2:
        prev = derivative_1d_even(m - 1)
        extra = polynomial_scale(prev, comb(order, 2) * 2)
        base = polynomial_add(base, extra)
    return base


def synthetic_nonradial_distinguishability():
    # psi_alpha(x)=exp(-alpha|x|^2)*(1+x1^2).
    # Compare beta=(2,0,0,0) and beta=(0,2,0,0): same total order, different actions.
    b1 = derivative_with_x2_factor(2)
    b2 = derivative_1d_even(1)
    return b1 != b2, {"beta_2000": b1, "beta_0200": b2}


def laplacian_power_action(j: int):
    """Exact coefficient of alpha^j in Delta^j exp(-alpha |x|^2)|0 in R^4."""
    total = 0
    for m1 in range(j + 1):
        for m2 in range(j - m1 + 1):
            for m3 in range(j - m1 - m2 + 1):
                m4 = j - m1 - m2 - m3
                ms = (m1, m2, m3, m4)
                multinomial = factorial(j)
                for m in ms:
                    multinomial //= factorial(m)
                beta = tuple(2 * m for m in ms)
                act = radial_action(beta)
                assert act is not None and act[0] == j
                total += multinomial * act[1]
    return total


def certificate(cap: int = ORDER_CAP):
    indices = multiindices_leq(DIM, cap)
    expected_count = comb(cap + DIM, DIM)
    actions = [radial_action(beta) for beta in indices]
    nonzero = [(beta, act) for beta, act in zip(indices, actions) if act is not None]
    zero = [(beta, act) for beta, act in zip(indices, actions) if act is None]
    degree_set = sorted({act[0] for _, act in nonzero})
    witnesses = {}
    for j in range(cap // 2 + 1):
        beta = (2 * j, 0, 0, 0)
        act = radial_action(beta)
        witnesses[str(j)] = {"beta": list(beta), "degree": act[0] if act else None, "coefficient": act[1] if act else None}

    odd_zero_ok = all(any(b % 2 for b in beta) for beta, _ in zero)
    even_nonzero_ok = all(all(b % 2 == 0 for b in beta) and act[1] != 0 for beta, act in nonzero)
    witness_ok = all(v["degree"] == int(j) and v["coefficient"] != 0 for j, v in witnesses.items())

    laplacian = {}
    laplacian_ok = True
    for j in range(cap // 2 + 1):
        observed = laplacian_power_action(j)
        expected = ((-4) ** j) * factorial(j + 1)
        laplacian[str(j)] = {"observed": observed, "expected": expected, "match": observed == expected}
        laplacian_ok &= observed == expected

    return {
        "dimension": DIM,
        "order_cap": cap,
        "multiindex_count": len(indices),
        "expected_multiindex_count": expected_count,
        "nonzero_radial_actions": len(nonzero),
        "zero_radial_actions": len(zero),
        "degree_set": degree_set,
        "rank": len(degree_set),
        "witnesses": witnesses,
        "laplacian_controls": laplacian,
        "checks": {
            "multiindex_count": len(indices) == expected_count,
            "odd_components_map_to_zero": odd_zero_ok,
            "all_even_map_nonzero": even_nonzero_ok,
            "degree_set_complete": degree_set == list(range(cap // 2 + 1)),
            "rank_expected": len(degree_set) == cap // 2 + 1,
            "monomial_witnesses": witness_ok,
            "laplacian_identity": laplacian_ok,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    main_cert = certificate(26)
    control24 = certificate(24)
    nonradial_ok, nonradial_detail = synthetic_nonradial_distinguishability()

    adversarial = {
        "order24_degree_ceiling_12": control24["degree_set"] == list(range(13)),
        "order24_rank_13": control24["rank"] == 13,
        "nonradial_same_order_distinguishable": nonradial_ok,
    }
    positive = dict(main_cert["checks"])
    positive["order26_degree_ceiling_13"] = main_cert["degree_set"] == list(range(14))
    positive["order26_rank_14"] = main_cert["rank"] == 14
    pass_gate = all(positive.values()) and all(adversarial.values())

    classification = (
        "AUX_GAUSSIAN_FULL_COLLISION_ORDER26_RADIAL_ACTION_SPACE_EXHAUSTED_SCOPED"
        if pass_gate
        else "SCIENTIFIC_FAIL_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS"
    )

    out = {
        "gate": "SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS_GATE",
        "classification": classification,
        "pass": pass_gate,
        "parent_result": PARENT_RESULT,
        "parent_alpha_cal_source_lock": list(A_CAL),
        "parent_alpha_test_source_lock": list(A_TEST),
        "main_certificate": main_cert,
        "order24_negative_control": {
            "degree_set": control24["degree_set"],
            "rank": control24["rank"],
            "multiindex_count": control24["multiindex_count"],
        },
        "nonradial_control": nonradial_detail,
        "positive_controls": positive,
        "adversarial_controls": adversarial,
        "claim_ceiling": "Exact completeness of the order<=26 full-collision action on the frozen radial Gaussian family only; does not exclude proper-stratum counterterms, higher order under separately justified power counting, or source-defined extensions; no D7 closure.",
    }

    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "classification": classification,
        "pass": pass_gate,
        "multiindex_count": main_cert["multiindex_count"],
        "nonzero_radial_actions": main_cert["nonzero_radial_actions"],
        "degree_set": main_cert["degree_set"],
        "rank": main_cert["rank"],
        "adversarial_controls": adversarial,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
