#!/usr/bin/env python3
"""Mixed Taylor tensor-grid method pilot for the auxiliary P1 scalar forest operator."""

from __future__ import annotations

import argparse
from itertools import product
import json
import math
from pathlib import Path

import mpmath as mp

import source_j1_k5_p1_forest_numerical_kernel_pilot as kernel
import source_j1_k5_scalar_forest_operator_pilot as op

ALPHA = mp.mpf("0.55")
P1_EXPONENTS = (1, 1, 1, 1, 2, 2, 2, 2, 2, 2)
EXPECTED_OPERATOR_DIGEST = "c3e0ca0c5a5357887db79b7b0a1c5a0a1042c450ca13f7e2599c7e3801ef8a9c"
FORESTS = {
    "SINGLE15": ((frozenset({0, 1, 2, 3}),), (15,)),
    "NESTED27": ((frozenset({0, 1}), frozenset({0, 1, 2})), (2, 7)),
    "DISJOINT22": ((frozenset({0, 1}), frozenset({2, 3})), (2, 2)),
    "CHAIN2715": ((frozenset({0, 1}), frozenset({0, 1, 2}), frozenset({0, 1, 2, 3})), (2, 7, 15)),
}


def normalized_error(a, b):
    return abs(a - b) / max(mp.mpf(1), abs(a), abs(b))


def lagrange_weights(r, h):
    t = 1 / h
    weights = []
    for j in range(r + 1):
        w = mp.mpf(1)
        for m in range(r + 1):
            if m != j:
                w *= (t - m) / (j - m)
        weights.append(w)
    return tuple(weights)


def tensor_sum(grid, weights, axis_order):
    ndim = len(weights)
    indices = [0] * ndim

    def rec(depth):
        if depth == ndim:
            return grid[tuple(indices)]
        axis = axis_order[depth]
        total = mp.mpf(0)
        for j, w in enumerate(weights[axis]):
            indices[axis] = j
            total += w * rec(depth + 1)
        return total

    return rec(0)


def direct_tensor_sum_and_condition(grid, weights, projected):
    total = mp.mpf(0)
    abs_total = mp.mpf(0)
    ranges = [range(len(w)) for w in weights]
    for idx in product(*ranges):
        w = mp.mpf(1)
        for axis, j in enumerate(idx):
            w *= weights[axis][j]
        term = w * grid[idx]
        total += term
        abs_total += abs(term)
    kappa = abs_total / max(mp.mpf(1), abs(projected))
    return total, kappa


def polynomial_fixture_value(lams, orders):
    value = mp.mpf(1)
    for lam, r in zip(lams, orders):
        # Deterministic degree-r polynomial with rational coefficients.
        subtotal = mp.mpf(0)
        for n in range(r + 1):
            subtotal += mp.mpf(n + 1) / (r + 1) * lam ** n
        value *= subtotal
    return value


def polynomial_fixture_exact_at_one(orders):
    out = mp.mpf(1)
    for r in orders:
        out *= mp.mpf(r + 2) / 2
    return out


def adversarial_degree_r_plus_one(lams, orders):
    # First variable has one forbidden degree above the interpolation box.
    base = polynomial_fixture_value(lams, orders)
    return base + lams[0] ** (orders[0] + 1)


def make_grid(orders, h, evaluator):
    grid = {}
    for idx in product(*(range(r + 1) for r in orders)):
        lams = tuple(mp.mpf(j) * h for j in idx)
        value = evaluator(lams)
        if not mp.isfinite(value):
            raise ArithmeticError(f"nonfinite grid value at {idx}")
        grid[idx] = value
    return grid


def project_grid(grid, orders, h):
    weights = tuple(lagrange_weights(r, h) for r in orders)
    forward = tensor_sum(grid, weights, tuple(range(len(orders))))
    reverse = tensor_sum(grid, weights, tuple(reversed(range(len(orders)))))
    direct, kappa = direct_tensor_sum_and_condition(grid, weights, forward)
    return forward, reverse, direct, kappa


def gamma_pairing_evaluator(forest, k=5):
    incidence = kernel.base_incidence_matrix()
    t = mp.mpf(2) ** (-k)
    eps = tuple(t ** p for p in P1_EXPONENTS)
    cn = []
    for s in forest:
        c = kernel.to_mp_matrix(op.barycentric_collapse(s))
        n = mp.eye(4) - c
        cn.append((c, n))

    def evaluate(lams):
        g = mp.eye(4)
        for (c, n), lam in zip(cn, lams):
            g = g * (c + lam * n)
        test_matrix = ALPHA * (g.T * g)
        return kernel.gaussian_pairing_quadratic(eps, test_matrix, incidence)

    return evaluate


def structural_controls(repo_root):
    terminal = Path(repo_root) / "results/SOURCE_J1_K5_SCALAR_FOREST_OPERATOR_PILOT_TERMINAL_2026-09-15.md"
    digest_lock = terminal.exists() and EXPECTED_OPERATOR_DIGEST in terminal.read_text()

    scalar_orders = {2: 2, 3: 7, 4: 15}
    forest_controls = {}
    for name, (forest, orders) in FORESTS.items():
        expected_orders = tuple(scalar_orders[len(s)] for s in forest)
        laminar = all(op.compatible(a, b) for i, a in enumerate(forest) for b in forest[i + 1 :])
        commute = all(op.symbolic_gamma_commutes(a, b) for i, a in enumerate(forest) for b in forest[i + 1 :])
        forest_controls[name] = {
            "orders_match": orders == expected_orders,
            "laminar": laminar,
            "gamma_commute": commute,
        }

    nonlaminar = (frozenset({0, 1}), frozenset({1, 2}))
    nonlaminar_rejected = not op.compatible(*nonlaminar) and not op.symbolic_gamma_commutes(*nonlaminar)
    historical_order_rejected = FORESTS["SINGLE15"][1] != (9,)

    return digest_lock, forest_controls, nonlaminar_rejected, historical_order_rejected


def raw_parent_lock():
    incidence = kernel.base_incidence_matrix()
    t = mp.mpf(2) ** (-5)
    eps = tuple(t ** p for p in P1_EXPONENTS)
    raw = kernel.gaussian_pairing_quadratic(eps, ALPHA * mp.eye(4), incidence)
    parent = mp.mpf(kernel.PARENT_RAW_STRINGS[5])
    return normalized_error(raw, parent)


def run_scale(h_power):
    h = mp.mpf(2) ** (-h_power)
    actual = {}
    fixture = {}
    adversarial = {}

    for name, (forest, orders) in FORESTS.items():
        fixture_grid = make_grid(orders, h, lambda lams, o=orders: polynomial_fixture_value(lams, o))
        fp, fr, fd, fkappa = project_grid(fixture_grid, orders, h)
        fexact = polynomial_fixture_exact_at_one(orders)

        adv_grid = make_grid(orders, h, lambda lams, o=orders: adversarial_degree_r_plus_one(lams, o))
        ap, _, _, _ = project_grid(adv_grid, orders, h)

        actual_grid = make_grid(orders, h, gamma_pairing_evaluator(forest))
        p, rev, direct, kappa = project_grid(actual_grid, orders, h)
        log10k = mp.log10(max(mp.mpf(1), kappa))

        fixture[name] = {
            "normalized_error": mp.nstr(normalized_error(fp, fexact), 100),
            "forward_reverse_error": mp.nstr(normalized_error(fp, fr), 100),
            "forward_direct_error": mp.nstr(normalized_error(fp, fd), 100),
            "kappa": mp.nstr(fkappa, 80),
        }
        adversarial[name] = {
            "projected": mp.nstr(ap, 160),
        }
        actual[name] = {
            "projected": mp.nstr(p, 260),
            "forward_reverse_error": mp.nstr(normalized_error(p, rev), 100),
            "forward_direct_error": mp.nstr(normalized_error(p, direct), 100),
            "kappa": mp.nstr(kappa, 100),
            "log10_kappa": mp.nstr(log10k, 100),
            "remaining_decimal_margin": mp.nstr(mp.mp.dps - log10k, 100),
            "finite": mp.isfinite(p),
            "grid_evaluations": math.prod(r + 1 for r in orders),
        }

    return {
        "h_power": h_power,
        "h": mp.nstr(h, 100),
        "fixture": fixture,
        "adversarial": adversarial,
        "actual": actual,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=("LOW", "HIGH"), required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--repo-root", default=".")
    args = ap.parse_args()

    if args.lane == "LOW":
        mp.mp.dps = 1100
        powers = (100,)
        fixture_tol = mp.mpf("1e-120")
        order_tol = mp.mpf("1e-100")
    else:
        mp.mp.dps = 1500
        powers = (100, 140)
        fixture_tol = mp.mpf("1e-200")
        order_tol = mp.mpf("1e-180")

    digest_lock, forest_controls, nonlaminar_rejected, historical_order_rejected = structural_controls(args.repo_root)
    parent_error = raw_parent_lock()
    scales = {str(p): run_scale(p) for p in powers}

    fixture_ok = True
    tensor_order_ok = True
    finite_ok = True
    margin_ok = True
    for scale in scales.values():
        for name in FORESTS:
            fixture_ok &= mp.mpf(scale["fixture"][name]["normalized_error"]) <= fixture_tol
            tensor_order_ok &= mp.mpf(scale["actual"][name]["forward_reverse_error"]) <= order_tol
            tensor_order_ok &= mp.mpf(scale["actual"][name]["forward_direct_error"]) <= order_tol
            finite_ok &= bool(scale["actual"][name]["finite"])
            margin_ok &= mp.mpf(scale["actual"][name]["remaining_decimal_margin"]) >= 180

    adversarial_step_detected = True
    if args.lane == "HIGH":
        # A degree-(r+1) fixture must reveal the difference between the two frozen step scales.
        for name in FORESTS:
            a = mp.mpf(scales["100"]["adversarial"][name]["projected"])
            b = mp.mpf(scales["140"]["adversarial"][name]["projected"])
            adversarial_step_detected &= normalized_error(a, b) > mp.mpf("1e-50")

    controls = {
        "operator_digest_lock": digest_lock,
        "all_forest_structure_controls": all(all(v.values()) for v in forest_controls.values()),
        "nonlaminar_pair_rejected": nonlaminar_rejected,
        "historical_order9_rejected_for_single15": historical_order_rejected,
        "historical_parent_raw_lock": parent_error <= mp.mpf("1e-65"),
        "exact_polynomial_fixtures": fixture_ok,
        "tensor_reduction_order_and_direct_sum": tensor_order_ok,
        "all_actual_values_finite": finite_ok,
        "cancellation_margin_at_least_180_digits": margin_ok,
        "degree_r_plus_one_step_sensitivity_detected": adversarial_step_detected,
    }
    controls_pass = all(controls.values())
    classification = "P1_MIXED_TAYLOR_GRID_METHOD_LANE_VALID" if controls_pass else "INVALID_IMPLEMENTATION"

    out = {
        "classification": classification,
        "controls_pass": controls_pass,
        "controls": controls,
        "lane": args.lane,
        "dps": mp.mp.dps,
        "alpha": "0.55",
        "k": 5,
        "parent_raw_lock_error": mp.nstr(parent_error, 100),
        "forest_controls": forest_controls,
        "scales": scales,
        "claim_ceiling": "Mixed Taylor numerical method validation only; projected values are non-scientific in this gate.",
    }
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k not in ("scales", "forest_controls")}, sort_keys=True))


if __name__ == "__main__":
    main()
