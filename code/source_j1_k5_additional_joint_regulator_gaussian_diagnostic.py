#!/usr/bin/env python3
"""High-precision Gaussian-moment diagnostic for an auxiliary K5 joint regulator.

Scientific authority:
  research/prereg/SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_2026-09-15.md
  research/prereg/SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_PROTOCOL_2026-09-15.md

P0 is exploratory reproduction only. Scientific classification consumes only P1-P3.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
import json
import statistics

import mpmath as mp

mp.mp.dps = 160

VERTICES = (1, 2, 3, 4, 5)
FREE_VERTICES = (2, 3, 4, 5)
EDGES = tuple(combinations(VERTICES, 2))
EDGE_NAMES = tuple(f"{a}{b}" for a, b in EDGES)
K_GRID = (3, 4, 5, 6, 7, 8)
PATHS = {
    "P0": (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    "P1": (1, 1, 1, 1, 2, 2, 2, 2, 2, 2),
    "P2": (2, 2, 2, 2, 1, 1, 1, 1, 1, 1),
    "P3": (1, 2, 3, 4, 2, 3, 4, 3, 4, 4),
}
NEW_PATHS = ("P1", "P2", "P3")


def incidence_row(a: int, b: int):
    row = [mp.mpf("0")] * 4
    if a != 1:
        row[FREE_VERTICES.index(a)] += 1
    if b != 1:
        row[FREE_VERTICES.index(b)] -= 1
    return row


def build_A(mapped_vertices=None):
    """Rows are attached to original edge slots; optional map relabels geometry."""
    if mapped_vertices is None:
        mapped_vertices = {v: v for v in VERTICES}
    rows = []
    for a, b in EDGES:
        aa, bb = mapped_vertices[a], mapped_vertices[b]
        if aa > bb:
            aa, bb = bb, aa
        rows.append(incidence_row(aa, bb))
    return mp.matrix(rows)


A = build_A()


def leading_principal_minors_positive(M):
    for n in range(1, 5):
        sub = mp.matrix([[M[i, j] for j in range(n)] for i in range(n)])
        if not (mp.det(sub) > 0):
            return False
    return True


def gaussian_pairing(eps, A_matrix=A, return_debug=False):
    eps = tuple(mp.mpf(e) for e in eps)
    if len(eps) != 10 or any(e <= 0 for e in eps):
        raise ValueError("all ten epsilon values must be positive")

    M = mp.eye(4)
    for e in range(10):
        inv = 1 / (eps[e] ** 2)
        for i in range(4):
            for j in range(4):
                M[i, j] += A_matrix[e, i] * A_matrix[e, j] * inv

    if not leading_principal_minors_positive(M):
        raise ArithmeticError("precision/control failure: M not positive definite")

    Sigma = mp.inverse(M) / 2
    C = A_matrix * Sigma * A_matrix.T

    sym_err = max(abs(C[i, j] - C[j, i]) for i in range(10) for j in range(10))
    if sym_err > mp.mpf("1e-120"):
        raise ArithmeticError(f"covariance symmetry control failed: {sym_err}")

    @lru_cache(None)
    def moment(counts):
        if sum(counts) == 0:
            return mp.mpf(1)
        if sum(counts) % 2:
            return mp.mpf(0)
        c = list(counts)
        i = next(k for k, v in enumerate(c) if v)
        c[i] -= 1
        total = mp.mpf(0)
        # Isserlis recursion: pair the distinguished copy i with every
        # remaining variable, including multiplicity.
        for j, v in enumerate(c):
            if v:
                multiplicity = v
                c[j] -= 1
                total += multiplicity * C[i, j] * moment(tuple(c))
                c[j] += 1
        return total

    # Independent low-order Wick controls.
    for i in (0, 4, 9):
        counts = [0] * 10
        counts[i] = 2
        if abs(moment(tuple(counts)) - C[i, i]) > mp.mpf("1e-120"):
            raise ArithmeticError("second-moment Wick control failed")
    i, j = 0, 4
    counts = [0] * 10
    counts[i] = counts[j] = 2
    expected_22 = C[i, i] * C[j, j] + 2 * C[i, j] ** 2
    if abs(moment(tuple(counts)) - expected_22) > mp.mpf("1e-115"):
        raise ArithmeticError("fourth-moment Wick control failed")

    expectation = mp.mpf(0)
    for mask in range(1 << 10):
        counts = [0] * 10
        coeff = mp.mpf(1)
        for e in range(10):
            if (mask >> e) & 1:
                counts[e] = 2
                coeff *= 4 / (eps[e] ** 4)
            else:
                coeff *= -2 / (eps[e] ** 2)
        expectation += coeff * moment(tuple(counts))

    mollifier_norm = mp.mpf(1)
    for e in range(10):
        mollifier_norm /= mp.sqrt(mp.pi) * eps[e]

    value = mollifier_norm * (mp.pi ** 2 / mp.sqrt(mp.det(M))) * expectation
    if return_debug:
        return value, {
            "covariance_symmetry_error": mp.nstr(sym_err, 20),
            "det_M": mp.nstr(mp.det(M), 30),
            "moment_cache_size": moment.cache_info().currsize,
        }
    return value


def zero_edge_control():
    return mp.pi ** 2


def one_edge_pairing(eps):
    # Exact 4D fixture for incidence row x1 and phi=exp(-|x|^2):
    # integral phi delta_epsilon''(x1) d^4x
    return -2 * mp.pi ** (mp.mpf(3) / 2) / (1 + eps ** 2) ** (mp.mpf(3) / 2)


def one_edge_direct_formula(eps):
    alpha = 1 + 1 / eps ** 2
    one_d = (1 / (mp.sqrt(mp.pi) * eps)) * (
        (4 / eps ** 4) * (mp.sqrt(mp.pi) / (2 * alpha ** (mp.mpf(3) / 2)))
        - (2 / eps ** 2) * (mp.sqrt(mp.pi) / mp.sqrt(alpha))
    )
    return one_d * mp.pi ** (mp.mpf(3) / 2)


def evaluate_path(exponents, A_matrix=A):
    values = []
    debug = []
    for k in K_GRID:
        t = mp.mpf(2) ** (-k)
        eps = [t ** p for p in exponents]
        val, dbg = gaussian_pairing(eps, A_matrix=A_matrix, return_debug=True)
        values.append(val)
        debug.append(dbg)

    growth = []
    for a, b in zip(values[:-1], values[1:]):
        if a == 0 or b == 0:
            growth.append(None)
        else:
            growth.append(mp.log(abs(b / a), 2))

    tail = growth[-3:]
    if any(g is None for g in tail):
        g_tail = None
    else:
        g_tail = sorted(tail)[1]

    absvals = [abs(v) for v in values]
    increasing_tail = absvals[-3] < absvals[-2] < absvals[-1]
    divergent = bool(increasing_tail and g_tail is not None and g_tail >= 2)

    diffs = [abs(values[i + 1] - values[i]) for i in range(len(values) - 1)]
    decreasing_diff_tail = diffs[-3] > diffs[-2] > diffs[-1]
    rel_change = abs(values[-1] - values[-2]) / max(abs(values[-1]), abs(values[-2]), mp.mpf("1e-300"))
    finite_compatible = bool(decreasing_diff_tail and rel_change <= mp.mpf("1e-8"))

    if divergent:
        status = "UNRENORMALIZED_DIVERGENT_DIAGNOSTIC"
    elif finite_compatible:
        status = "FINITE_LIMIT_COMPATIBLE_DIAGNOSTIC"
    else:
        status = "INCONCLUSIVE_DIAGNOSTIC"

    return {
        "status": status,
        "values": [mp.nstr(v, 50) for v in values],
        "abs_values": [mp.nstr(v, 30) for v in absvals],
        "growth_log2_abs_ratio": [None if g is None else mp.nstr(g, 30) for g in growth],
        "g_tail": None if g_tail is None else mp.nstr(g_tail, 30),
        "final_relative_change": mp.nstr(rel_change, 30),
        "sign_tail": [int(mp.sign(v)) for v in values[-3:]],
        "debug": debug,
    }


def classify(path_results, controls_pass):
    if not controls_pass:
        return "INVALID_IMPLEMENTATION"

    statuses = {p: path_results[p]["status"] for p in NEW_PATHS}
    divergent = [p for p, s in statuses.items() if s == "UNRENORMALIZED_DIVERGENT_DIAGNOSTIC"]
    finite = [p for p, s in statuses.items() if s == "FINITE_LIMIT_COMPATIBLE_DIAGNOSTIC"]

    # Frozen precedence: path-dependence before generic rejection.
    incompatible = bool(divergent and finite)
    if len(finite) >= 2:
        finals = [mp.mpf(path_results[p]["values"][-1]) for p in finite]
        for i in range(len(finals)):
            for j in range(i + 1, len(finals)):
                rel = abs(finals[i] - finals[j]) / max(abs(finals[i]), abs(finals[j]), mp.mpf("1e-300"))
                if rel > mp.mpf("1e-8"):
                    incompatible = True

    if incompatible:
        return "AUX_GAUSSIAN_JOINT_REGULATOR_PATH_DEPENDENCE_WITNESS_SCOPED"
    if len(divergent) >= 2:
        return "AUX_GAUSSIAN_JOINT_REGULATOR_REJECTED_UNRENORMALIZED_SCOPED"
    if len(finite) == 3:
        finals = [mp.mpf(path_results[p]["values"][-1]) for p in NEW_PATHS]
        scale = max(max(abs(v) for v in finals), mp.mpf("1e-300"))
        if max(finals) - min(finals) <= mp.mpf("1e-8") * scale:
            return "AUX_GAUSSIAN_JOINT_REGULATOR_SURVIVES_DIAGNOSTIC_SCOPED"
    return "AUX_GAUSSIAN_JOINT_REGULATOR_DIAGNOSTIC_INCONCLUSIVE"


def main():
    controls = {}

    z = zero_edge_control()
    controls["zero_edge_gaussian_integral"] = bool(abs(z - mp.pi ** 2) <= mp.mpf("1e-140"))

    eps_fixture = mp.mpf(2) ** -3
    one_a = one_edge_pairing(eps_fixture)
    one_b = one_edge_direct_formula(eps_fixture)
    controls["one_edge_closed_formula"] = bool(
        abs(one_a - one_b) / max(abs(one_a), mp.mpf("1e-300")) <= mp.mpf("1e-120")
    )

    path_results = {name: evaluate_path(exp) for name, exp in PATHS.items()}

    # Vertex permutation control on a NEW anisotropic assignment, k=3.
    swap23 = {1: 1, 2: 3, 3: 2, 4: 4, 5: 5}
    A_perm = build_A(swap23)
    t = mp.mpf(2) ** -3
    eps_p3 = [t ** p for p in PATHS["P3"]]
    base_perm_val = gaussian_pairing(eps_p3, A_matrix=A)
    transformed_val = gaussian_pairing(eps_p3, A_matrix=A_perm)
    perm_rel = abs(base_perm_val - transformed_val) / max(abs(base_perm_val), abs(transformed_val), mp.mpf("1e-300"))
    controls["vertex_relabel_invariance"] = bool(perm_rel <= mp.mpf("1e-100"))

    controls_pass = all(controls.values())
    classification = classify(path_results, controls_pass)

    result = {
        "classification": classification,
        "precision_decimal_digits": mp.mp.dps,
        "edge_order": list(EDGE_NAMES),
        "k_grid": list(K_GRID),
        "paths": {k: list(v) for k, v in PATHS.items()},
        "p0_role": "EXPLORATORY_REPRODUCTION_ONLY",
        "new_scientific_paths": list(NEW_PATHS),
        "controls": controls,
        "controls_pass": controls_pass,
        "vertex_permutation_relative_error": mp.nstr(perm_rel, 30),
        "path_results": path_results,
        "claim_ceiling": (
            "Auxiliary Gaussian approximate-identity diagnostic on the aligned highest-contact K5 witness only. "
            "Rejection is not Eq4 distributional nonexistence; survival is not source equivalence or D7 closure."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
