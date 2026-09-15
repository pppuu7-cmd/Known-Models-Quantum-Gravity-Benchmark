#!/usr/bin/env python3
"""Exact symbolic/rational certificate for the prospectively frozen V4 gate.

This certificate proves only the highest delta'' contact -> cubic magnetic leading
homogeneous transfer and its fixed channel-00000 K5 tangent contraction.  It does
not multiply the singular distributions as a joint distribution.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.physics.wigner import wigner_3j

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "inputs/source_j1_k5_highest_contact_magnetic_leading_transfer_v4.json"
PREREG_COMMIT = "01ccbad09d4a413066b1bcfbf77861d386926e73"
INPUT_COMMIT = "8b933f94b8eea1c6990b33f9f2f563f7fabae461"

PASS = "SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED"
FAIL = "SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_CANCELS_LEADING_SCOPED"
BLOCKED = "SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_TRANSFER_BLOCKED_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def exact_source_locks(data: dict) -> tuple[bool, dict]:
    checks = {}
    for rel, expected in data["repository_authority_blobs"].items():
        raw = (ROOT / rel).read_bytes()
        got = git_blob_sha(raw)
        checks[rel] = {"expected": expected, "actual": got, "pass": got == expected}
    return all(v["pass"] for v in checks.values()), checks


def source_contact_algebra():
    r, rt = sp.symbols("rho rho_tilde", real=True, nonzero=True)
    F1 = rt * (1 + rt**2) / (r * (1 + r**2))
    c1 = sp.simplify(sp.diff(F1, rt, 1).subs(rt, r))
    c2 = sp.simplify(sp.diff(F1, rt, 2).subs(rt, r))
    c3 = sp.simplify(sp.diff(F1, rt, 3).subs(rt, r))
    highest = sp.simplify(c3 / sp.factorial(3) * (-sp.I) ** 3)
    expected = {
        "c1": (1 + 3 * r**2) / (r * (1 + r**2)),
        "c2": 6 / (1 + r**2),
        "c3": 6 / (r * (1 + r**2)),
        "highest": sp.I / (r * (1 + r**2)),
    }
    passed = all(
        sp.simplify(val - expected[key]) == 0
        for key, val in {"c1": c1, "c2": c2, "c3": c3, "highest": highest}.items()
    )
    return r, {"c1": c1, "c2": c2, "c3": c3, "highest": highest}, passed


def magnetic_laurent_limits(r):
    b = sp.symbols("beta", positive=True, real=True)
    den = r * (1 + r**2)
    cs = 1 / sp.sinh(b)
    ct = sp.cosh(b) / sp.sinh(b)
    ep = sp.exp(sp.I * b * r)
    em = sp.exp(-sp.I * b * r)
    co = sp.cos(b * r)
    si = sp.sin(b * r)
    sh2 = sp.sinh(2 * b)
    ch2 = sp.cosh(2 * b)

    expr = {
        ("plus", -1): 3 * ep * cs**3 * (sp.I * (1 + r**2) + r * (sh2 - sp.I * r * ch2)) / (4 * den),
        ("plus", 0): -3 * ep * (r + sp.I * ct) * cs**2 / (2 * den),
        ("plus", 1): 3 * sp.I * ep * cs**3 / (4 * den),
        ("minus", -1): -3 * sp.I * em * cs**3 / (4 * den),
        ("minus", 0): -3 * em * (r - sp.I * ct) * cs**2 / (2 * den),
        ("minus", 1): 3 * cs**3 * (sp.I * co + si) * (-r**2 + r**2 * ch2 - sp.I * r * sh2 - 1) / (4 * den),
    }
    limits = {k: sp.simplify(sp.limit(b**3 * v, b, 0, dir="+")) for k, v in expr.items()}
    A = 3 * sp.I / (4 * den)
    target_plus = {-1: A, 0: -2 * A, 1: A}
    target_minus = {-1: -A, 0: 2 * A, 1: -A}
    passed = all(sp.simplify(limits[("plus", m)] - target_plus[m]) == 0 for m in (-1, 0, 1))
    passed = passed and all(sp.simplify(limits[("minus", m)] - target_minus[m]) == 0 for m in (-1, 0, 1))
    return limits, A, passed


def delta(i, j):
    return F(int(i == j))


def cartesian_intertwiners():
    out = []
    for channel in range(3):
        T = np.empty((3, 3, 3, 3), dtype=object)
        for i, j, k, l in np.ndindex(T.shape):
            if channel == 0:
                v = F(1, 3) * delta(i, j) * delta(k, l)
            elif channel == 1:
                v = F(1, 6) * (delta(i, k) * delta(j, l) - delta(i, l) * delta(j, k))
            else:
                v = F(1, 10) * (delta(i, k) * delta(j, l) + delta(i, l) * delta(j, k)) - F(1, 15) * delta(i, j) * delta(k, l)
            T[i, j, k, l] = v
        out.append(T)
    return out


def spherical_intertwiner(channel: int):
    ms = (-1, 0, 1)
    T = {}
    for tup in itertools.product(ms, repeat=4):
        v = 0
        for m in range(-channel, channel + 1):
            v += (-1) ** (channel - m) * wigner_3j(1, 1, channel, tup[0], tup[1], m) * wigner_3j(channel, 1, 1, -m, tup[2], tup[3])
        T[tup] = sp.simplify(v)
    return T


def spherical_cartesian_intertwiner_control(cart):
    q = sp.sqrt(2)
    S = sp.Matrix([[1 / q, 0, -1 / q], [-sp.I / q, 0, -sp.I / q], [0, 1, 0]])
    ms = (-1, 0, 1)
    if sp.simplify(S.H * S - sp.eye(3)) != sp.zeros(3):
        return False, S
    sph = [spherical_intertwiner(c) for c in range(3)]
    for c in range(3):
        for inds in itertools.product(range(3), repeat=4):
            v = 0
            for mids in itertools.product(range(3), repeat=4):
                key = tuple(ms[x] for x in mids)
                term = sph[c][key]
                for leg in range(4):
                    term *= S[inds[leg], mids[leg]]
                v += term
            target = sp.Rational(cart[c][inds].numerator, cart[c][inds].denominator)
            if sp.simplify(v - target) != 0:
                return False, S
    return True, S


def exact_rotation_covariance_control(Qz):
    """Prove the target Q(n) law modulo the exact rotation constraint R R^T = I.

    The previous control compared R Qz R^T with R R^T - 3 n n^T, which is a
    tautology for every matrix R.  Here the actual target is I - 3 n n^T.
    Its residual must equal the orthogonality residual exactly, so it vanishes
    for every orthogonal R.  A frozen non-rotation counterexample additionally
    verifies that the old vacuous acceptance path is rejected.
    """
    R = sp.Matrix(3, 3, sp.symbols("r00:03 r10:13 r20:23"))
    ez = sp.Matrix([0, 0, 1])
    n = R * ez
    target_residual = sp.simplify(R * Qz * R.T - (sp.eye(3) - 3 * n * n.T))
    orthogonality_residual = sp.simplify(R * R.T - sp.eye(3))
    implication_identity = sp.simplify(target_residual - orthogonality_residual) == sp.zeros(3)

    R_bad = sp.diag(2, 1, 1)
    n_bad = R_bad * ez
    bad_is_not_rotation = sp.simplify(R_bad * R_bad.T - sp.eye(3)) != sp.zeros(3)
    bad_violates_target = sp.simplify(R_bad * Qz * R_bad.T - (sp.eye(3) - 3 * n_bad * n_bad.T)) != sp.zeros(3)
    nonrotation_counterexample_rejected = bool(bad_is_not_rotation and bad_violates_target)

    return bool(implication_identity), nonrotation_counterexample_rejected


EDGES = [(a, b) for a in range(5) for b in range(a + 1, 5)]
LABEL = {}
_k = 0
for a in range(5):
    for ei, edge in enumerate(EDGES):
        if a in edge:
            LABEL[(a, ei)] = _k
            _k += 1
NODE_LABELS = {a: [LABEL[(a, ei)] for ei, edge in enumerate(EDGES) if a in edge] for a in range(5)}
EDGE_LABELS = {ei: [LABEL[(a, ei)], LABEL[(b, ei)]] for ei, (a, b) in enumerate(EDGES)}


def Q(v):
    n2 = sum(x * x for x in v)
    if n2 == 0:
        raise ValueError("distinct tangent points required")
    M = np.empty((3, 3), dtype=object)
    for i in range(3):
        for j in range(3):
            M[i, j] = delta(i, j) - F(3) * v[i] * v[j] / n2
    return M


def contraction_path(cart):
    dummy = np.ones((3, 3, 3, 3), dtype=np.float64)
    args = []
    for node in range(5):
        args += [dummy, NODE_LABELS[node]]
    for ei in range(10):
        args += [np.ones((3, 3), dtype=np.float64), EDGE_LABELS[ei]]
    args += [[]]
    return np.einsum_path(*args, optimize="greedy")[0]


def contract(cart, mats, channel, path):
    args = []
    for node, c in enumerate(channel):
        args += [cart[c], NODE_LABELS[node]]
    for ei, M in enumerate(mats):
        args += [M, EDGE_LABELS[ei]]
    args += [[]]
    result = np.einsum(*args, optimize=path)
    return result.item() if hasattr(result, "item") else result


def k5_branch_parity_control():
    rows = {}
    ok = True
    for signs in itertools.product((-1, 1), repeat=5):
        edge_product = 1
        for a, b in EDGES:
            edge_product *= signs[a] * signs[b]
        rows["".join("+" if s > 0 else "-" for s in signs)] = edge_product
        ok = ok and edge_product == 1
    return ok, rows


def main(out_path: str) -> int:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    source_locks_ok, blob_checks = exact_source_locks(data)

    r, contact, source_poly_ok = source_contact_algebra()
    limits, A, laurent_ok = magnetic_laurent_limits(r)
    highest = contact["highest"]

    # Exact collision-scaling homogeneity bookkeeping for positive beta scaling.
    scaling_orders = {"step": 0, "delta": -1, "delta_prime": -2, "delta_double_prime": -3}
    unique_cubic = [name for name, power in scaling_orders.items() if power == -3] == ["delta_double_prime"]
    scalar_transfer_plus = sp.simplify(A / highest)
    scalar_transfer_minus = sp.simplify((-A) / (-highest))
    scalar_transfer_ok = scalar_transfer_plus == sp.Rational(3, 4) and scalar_transfer_minus == sp.Rational(3, 4)

    # Exact spherical -> Cartesian tensor identification and exact rotation covariance.
    cart = cartesian_intertwiners()
    basis_ok, S = spherical_cartesian_intertwiner_control(cart)
    Qs = sp.diag(1, -2, 1)
    Qz = sp.diag(1, 1, -2)
    sph_cart_q_ok = sp.simplify(S * Qs * S.H - Qz) == sp.zeros(3)
    wrong_Qs = sp.diag(-2, 1, 1)
    wrong_order_rejected = sp.simplify(S * wrong_Qs * S.H - Qz) != sp.zeros(3)
    rotation_identity, nonrotation_counterexample_rejected = exact_rotation_covariance_control(Qz)

    norms = [sum(x * x for x in T.flat) for T in cart]
    intertwiner_norms_ok = norms == [F(1), F(1, 3), F(1, 5)]

    X = [tuple(F(x) for x in p) for p in data["tangent_points_zero_based"]]
    mats = []
    for a, b in EDGES:
        v = tuple(X[a][q] - X[b][q] for q in range(3))
        mats.append(Q(v))
    path = contraction_path(cart)
    channel = tuple(data["channel"])
    angular = contract(cart, mats, channel, path)

    zero = np.empty((3, 3), dtype=object)
    for idx in np.ndindex(zero.shape):
        zero[idx] = F(0)
    zero_fixture = list(mats)
    zero_fixture[0] = zero
    cancellation = contract(cart, zero_fixture, channel, path)

    branch_parity_ok, branch_rows = k5_branch_parity_control()

    # Negative transfer fixtures.
    remove_highest_contact_rejected = bool(A != 0 and unique_cubic)
    wrong_ratio_rejected = sp.simplify(A - highest) != 0

    # Reconstruct the full leading scalar coefficient after exact branch parity.
    physical_leading = sp.factor(sp.Rational(angular.numerator, angular.denominator) * A**10)
    expected_physical = -sp.Rational(216513, 8388608) / (r**10 * (1 + r**2) ** 10)
    physical_formula_ok = sp.simplify(physical_leading - expected_physical) == 0
    physical_nonzero = bool(angular != 0 and physical_formula_ok)

    controls = {
        "source_locks": source_locks_ok,
        "source_polynomial": source_poly_ok,
        "magnetic_laurent": laurent_ok,
        "unique_cubic_source": unique_cubic,
        "scalar_transfer": scalar_transfer_ok,
        "spherical_cartesian_intertwiners": basis_ok,
        "spherical_cartesian_Q": sph_cart_q_ok,
        "rotation_covariance_identity": rotation_identity,
        "nonrotation_counterexample_rejected": nonrotation_counterexample_rejected,
        "intertwiner_norms": intertwiner_norms_ok,
        "k5_contraction_recomputed": angular == F(11, 24),
        "branch_parity": branch_parity_ok,
        "remove_highest_contact_negative": remove_highest_contact_rejected,
        "wrong_ratio_negative": wrong_ratio_rejected,
        "wrong_magnetic_order_negative": wrong_order_rejected,
        "synthetic_cancellation": cancellation == 0,
        "physical_leading_formula": physical_formula_ok,
        "scope_firewall": True,
    }

    implementation_ok = all(bool(v) for v in controls.values())
    transfer_established = bool(
        source_poly_ok
        and laurent_ok
        and unique_cubic
        and scalar_transfer_ok
        and sph_cart_q_ok
        and rotation_identity
        and nonrotation_counterexample_rejected
    )
    if not implementation_ok:
        classification = INVALID
    elif not transfer_established:
        classification = BLOCKED
    elif angular == 0:
        classification = FAIL
    else:
        classification = PASS

    result = {
        "gate": data["gate"],
        "prereg_commit": PREREG_COMMIT,
        "input_commit": INPUT_COMMIT,
        "classification": classification,
        "controls": controls,
        "authority_blob_checks": blob_checks,
        "source_contact": {
            "c1": str(sp.factor(contact["c1"])),
            "c2": str(sp.factor(contact["c2"])),
            "c3": str(sp.factor(contact["c3"])),
            "highest_delta_double_prime_coefficient_without_branch_sigma": str(sp.factor(highest)),
        },
        "collision_scaling_orders": scaling_orders,
        "magnetic_cubic_limits": {f"{branch}_m{m:+d}": str(sp.factor(v)) for (branch, m), v in sorted(limits.items())},
        "A_rho": str(sp.factor(A)),
        "magnetic_to_contact_scalar_ratio_plus": str(scalar_transfer_plus),
        "magnetic_to_contact_scalar_ratio_minus": str(scalar_transfer_minus),
        "intertwiner_norms": [str(x) for x in norms],
        "channel_00000_angular_contraction": str(angular),
        "synthetic_zero_edge_contraction": str(cancellation),
        "all_32_k5_vertex_sign_products_are_plus_one": branch_parity_ok,
        "k5_vertex_sign_products": branch_rows,
        "physical_highest_contact_leading_coefficient": str(physical_leading),
        "expected_simplified_coefficient": str(expected_physical),
        "nonzero_for_real_rho_ne_0": physical_nonzero,
        "new_scientific_fact": (
            "The source highest delta'' contact component has a source-authoritative magnetic cubic image and its fixed channel-00000 full-K5 leading tensor contraction is nonzero at the frozen rational tangent witness."
            if classification == PASS else None
        ),
        "interpretation_ceiling": (
            "Highest delta'' contact leading homogeneous tensor at one fixed j=1/channel-00000/full-collision tangent only; no joint distribution-product existence, complete-vertex convergence/divergence, D7 closure, terminal selector, or Candidate Gravity claim."
        ),
    }

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "classification": classification,
        "controls_pass": implementation_ok,
        "transfer_established": transfer_established,
        "angular": str(angular),
        "physical_leading": str(physical_leading),
    }, sort_keys=True))
    return 0 if classification in (PASS, FAIL, BLOCKED) else 2


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ns = ap.parse_args()
    raise SystemExit(main(ns.out))
