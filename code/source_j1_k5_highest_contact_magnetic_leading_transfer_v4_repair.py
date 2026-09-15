#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp

import source_j1_k5_highest_contact_magnetic_leading_transfer_v4 as base

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "inputs/source_j1_k5_highest_contact_magnetic_leading_transfer_v4.json"
PREREG_COMMIT = "01ccbad09d4a413066b1bcfbf77861d386926e73"
INPUT_COMMIT = "8b933f94b8eea1c6990b33f9f2f563f7fabae461"
CRITIC_COMMIT = "c0358e348bbb225719bb1617f905e38d91f33e21"
ROTATION_REPAIR_COMMIT = "f903669dd08c6ae6fa9ac4d140ff85f294dd36c1"
REPAIR_PROTOCOL_COMMIT = "91bcaadc83be2934e09ec3e32b17709b3306d059"
BASE_IMPLEMENTATION_BLOB = "b9b9e7104f13f8f3b38722eea76fc02c93444148"

PASS = base.PASS
FAIL = base.FAIL
BLOCKED = base.BLOCKED
INVALID = base.INVALID


def exact_delta_pullback_exponent(n: int) -> tuple[int, sp.Expr]:
    """Derive delta^(n)(beta*x) weight from its test-function action for beta>0."""
    if n < 0:
        raise ValueError("delta derivative order must be nonnegative")
    beta, y = sp.symbols("beta y", positive=True, real=True)
    phi = y**n / sp.factorial(n)
    base_action = sp.simplify((-1) ** n * sp.diff(phi, y, n).subs(y, 0))
    scaled_phi = sp.expand(phi.subs(y, y / beta))
    scaled_action = sp.simplify((1 / beta) * (-1) ** n * sp.diff(scaled_phi, y, n).subs(y, 0))
    ratio = sp.factor(sp.simplify(scaled_action / base_action))
    powers = ratio.as_powers_dict()
    exponent = sp.Integer(powers.get(beta, 0))
    reconstructed = sp.simplify(ratio / beta**exponent)
    if reconstructed != 1:
        raise AssertionError((n, ratio, exponent, reconstructed))
    return int(exponent), ratio


def build_source_split(contact: dict[str, sp.Expr], sigma: int, include_highest: bool = True) -> list[dict]:
    if sigma not in (-1, 1):
        raise ValueError("sigma must be +/-1")
    terms = [
        {
            "label": "step",
            "kind": "step",
            "derivative_order": None,
            "coefficient": sp.Integer(1),
        }
    ]
    for n, key in enumerate(("c1", "c2", "c3")):
        if n == 2 and not include_highest:
            continue
        coefficient = sp.factor(
            sp.Integer(sigma)
            * contact[key]
            / sp.factorial(n + 1)
            * (-sp.I) ** (n + 1)
        )
        terms.append(
            {
                "label": ("delta", "delta_prime", "delta_double_prime")[n],
                "kind": "delta_derivative",
                "derivative_order": n,
                "coefficient": coefficient,
            }
        )
    return terms


def derive_source_scaling(terms: list[dict]) -> tuple[dict[str, int], dict[str, str]]:
    orders: dict[str, int] = {}
    proofs: dict[str, str] = {}
    for term in terms:
        if term["kind"] == "step":
            orders[term["label"]] = 0
            proofs[term["label"]] = "theta(sigma*beta*x)=theta(sigma*x) for beta>0"
        elif term["kind"] == "delta_derivative":
            exponent, ratio = exact_delta_pullback_exponent(int(term["derivative_order"]))
            orders[term["label"]] = exponent
            proofs[term["label"]] = str(ratio)
        else:
            raise ValueError(term)
    return orders, proofs


def transfer_classifier(source_terms: list[dict], magnetic_scalar: sp.Expr, angular) -> dict:
    orders, proofs = derive_source_scaling(source_terms)
    active = [t for t in source_terms if sp.simplify(t["coefficient"]) != 0]
    cubic = [t for t in active if orders[t["label"]] == -3]
    out = {
        "scaling_orders": orders,
        "scaling_proofs": proofs,
        "cubic_labels": [t["label"] for t in cubic],
        "transfer_established": False,
        "scalar_ratio": None,
        "contact_scalar": None,
        "reason": None,
        "classification": BLOCKED,
    }
    if len(cubic) != 1 or cubic[0]["label"] != "delta_double_prime" or cubic[0]["derivative_order"] != 2:
        out["reason"] = "NO_UNIQUE_CUBIC_SOURCE_COMPONENT"
        return out

    contact_scalar = sp.factor(cubic[0]["coefficient"])
    ratio = sp.factor(sp.simplify(magnetic_scalar / contact_scalar))
    out["contact_scalar"] = str(contact_scalar)
    out["scalar_ratio"] = str(ratio)
    if ratio != sp.Rational(3, 4):
        out["reason"] = "SCALAR_RATIO_MISMATCH"
        return out

    out["transfer_established"] = True
    out["reason"] = "TRANSFER_ESTABLISHED"
    out["classification"] = FAIL if angular == 0 else PASS
    return out


def main(out_path: str) -> int:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    source_locks_ok, blob_checks = base.exact_source_locks(data)

    r, contact, source_poly_ok = base.source_contact_algebra()
    limits, A, laurent_ok = base.magnetic_laurent_limits(r)

    plus_split = build_source_split(contact, +1, include_highest=True)
    minus_split = build_source_split(contact, -1, include_highest=True)
    plus_orders, plus_scaling_proofs = derive_source_scaling(plus_split)
    minus_orders, minus_scaling_proofs = derive_source_scaling(minus_split)
    expected_orders = {
        "step": 0,
        "delta": -1,
        "delta_prime": -2,
        "delta_double_prime": -3,
    }
    unique_cubic = plus_orders == expected_orders and minus_orders == expected_orders

    cart = base.cartesian_intertwiners()
    basis_ok, S = base.spherical_cartesian_intertwiner_control(cart)
    Qs = sp.diag(1, -2, 1)
    Qz = sp.diag(1, 1, -2)
    sph_cart_q_ok = sp.simplify(S * Qs * S.H - Qz) == sp.zeros(3)
    wrong_Qs = sp.diag(-2, 1, 1)
    wrong_order_rejected = sp.simplify(S * wrong_Qs * S.H - Qz) != sp.zeros(3)
    rotation_identity, nonrotation_counterexample_rejected = base.exact_rotation_covariance_control(Qz)

    norms = [sum(x * x for x in T.flat) for T in cart]
    intertwiner_norms_ok = norms == [F(1), F(1, 3), F(1, 5)]

    X = [tuple(F(x) for x in p) for p in data["tangent_points_zero_based"]]
    mats = []
    for a, b in base.EDGES:
        v = tuple(X[a][q] - X[b][q] for q in range(3))
        mats.append(base.Q(v))
    path = base.contraction_path(cart)
    channel = tuple(data["channel"])
    angular = base.contract(cart, mats, channel, path)

    zero = np.empty((3, 3), dtype=object)
    for idx in np.ndindex(zero.shape):
        zero[idx] = F(0)
    zero_fixture = list(mats)
    zero_fixture[0] = zero
    cancellation_angular = base.contract(cart, zero_fixture, channel, path)

    branch_parity_ok, branch_rows = base.k5_branch_parity_control()

    production_plus = transfer_classifier(plus_split, A, angular)
    production_minus = transfer_classifier(minus_split, -A, angular)

    negative_plus_split = build_source_split(contact, +1, include_highest=False)
    negative_minus_split = build_source_split(contact, -1, include_highest=False)
    negative_plus = transfer_classifier(negative_plus_split, A, angular)
    negative_minus = transfer_classifier(negative_minus_split, -A, angular)
    lower_labels_expected = ["step", "delta", "delta_prime"]
    remove_highest_contact_rejected = bool(
        [t["label"] for t in negative_plus_split] == lower_labels_expected
        and [t["label"] for t in negative_minus_split] == lower_labels_expected
        and not negative_plus["transfer_established"]
        and not negative_minus["transfer_established"]
        and negative_plus["reason"] == "NO_UNIQUE_CUBIC_SOURCE_COMPONENT"
        and negative_minus["reason"] == "NO_UNIQUE_CUBIC_SOURCE_COMPONENT"
    )

    highest_plus = sp.factor(plus_split[-1]["coefficient"])
    wrong_ratio = transfer_classifier(plus_split, highest_plus, angular)
    wrong_ratio_rejected = bool(
        not wrong_ratio["transfer_established"]
        and wrong_ratio["reason"] == "SCALAR_RATIO_MISMATCH"
        and wrong_ratio["scalar_ratio"] == "1"
    )

    synthetic_cancellation = transfer_classifier(plus_split, A, cancellation_angular)
    synthetic_cancellation_ok = bool(
        synthetic_cancellation["transfer_established"]
        and synthetic_cancellation["classification"] == FAIL
        and cancellation_angular == 0
    )

    scalar_transfer_ok = bool(
        production_plus["transfer_established"]
        and production_minus["transfer_established"]
        and production_plus["scalar_ratio"] == "3/4"
        and production_minus["scalar_ratio"] == "3/4"
    )

    physical_leading = sp.factor(sp.Rational(angular.numerator, angular.denominator) * A**10)
    expected_physical = -sp.Rational(216513, 8388608) / (r**10 * (1 + r**2) ** 10)
    physical_formula_ok = sp.simplify(physical_leading - expected_physical) == 0

    controls = {
        "source_locks": source_locks_ok,
        "source_polynomial": source_poly_ok,
        "magnetic_laurent": laurent_ok,
        "unique_cubic_source_executable": unique_cubic,
        "scalar_transfer_common_classifier": scalar_transfer_ok,
        "spherical_cartesian_intertwiners": basis_ok,
        "spherical_cartesian_Q": sph_cart_q_ok,
        "rotation_covariance_identity": rotation_identity,
        "nonrotation_counterexample_rejected": nonrotation_counterexample_rejected,
        "intertwiner_norms": intertwiner_norms_ok,
        "k5_contraction_recomputed": angular == F(11, 24),
        "branch_parity": branch_parity_ok,
        "remove_highest_contact_negative_common_classifier": remove_highest_contact_rejected,
        "wrong_ratio_negative_common_classifier": wrong_ratio_rejected,
        "wrong_magnetic_order_negative": wrong_order_rejected,
        "synthetic_cancellation_common_classifier": synthetic_cancellation_ok,
        "physical_leading_formula": physical_formula_ok,
        "scope_firewall": True,
    }

    implementation_ok = all(bool(v) for v in controls.values())
    transfer_established = bool(
        production_plus["transfer_established"]
        and production_minus["transfer_established"]
    )
    if not implementation_ok:
        classification = INVALID
    elif not transfer_established:
        classification = BLOCKED
    elif angular == 0:
        classification = FAIL
    else:
        classification = PASS

    def serialize_limits():
        return {
            f"{branch}:{m}": str(sp.factor(value))
            for (branch, m), value in sorted(limits.items())
        }

    result = {
        "gate": data["gate"],
        "repair": "V4_SAME_CONTRACT_IMPLEMENTATION_REPAIR",
        "prereg_commit": PREREG_COMMIT,
        "input_commit": INPUT_COMMIT,
        "critic_commit": CRITIC_COMMIT,
        "rotation_repair_commit": ROTATION_REPAIR_COMMIT,
        "repair_protocol_commit": REPAIR_PROTOCOL_COMMIT,
        "base_implementation_blob": BASE_IMPLEMENTATION_BLOB,
        "classification": classification,
        "controls": controls,
        "authority_blob_checks": blob_checks,
        "derived_scaling_orders_plus": plus_orders,
        "derived_scaling_orders_minus": minus_orders,
        "derived_scaling_proofs_plus": plus_scaling_proofs,
        "derived_scaling_proofs_minus": minus_scaling_proofs,
        "production_classifier_plus": production_plus,
        "production_classifier_minus": production_minus,
        "remove_highest_classifier_plus": negative_plus,
        "remove_highest_classifier_minus": negative_minus,
        "wrong_ratio_classifier": wrong_ratio,
        "synthetic_cancellation_classifier": synthetic_cancellation,
        "source_contact": {
            "c1": str(sp.factor(contact["c1"])),
            "c2": str(sp.factor(contact["c2"])),
            "c3": str(sp.factor(contact["c3"])),
            "highest_plus": str(highest_plus),
            "highest_minus": str(sp.factor(minus_split[-1]["coefficient"])),
        },
        "A_rho": str(sp.factor(A)),
        "magnetic_cubic_limits": serialize_limits(),
        "magnetic_to_contact_scalar_ratio_plus": production_plus["scalar_ratio"],
        "magnetic_to_contact_scalar_ratio_minus": production_minus["scalar_ratio"],
        "channel_00000_angular_contraction": str(angular),
        "synthetic_cancellation_angular_contraction": str(cancellation_angular),
        "all_32_k5_vertex_sign_products_are_plus_one": branch_parity_ok,
        "k5_vertex_sign_products": branch_rows,
        "physical_highest_contact_leading_coefficient": str(physical_leading),
        "expected_simplified_coefficient": str(expected_physical),
        "nonzero_for_real_rho_ne_0": bool(angular != 0 and physical_formula_ok),
        "new_scientific_fact": (
            "The source highest delta'' contact component has an exact magnetic cubic image and the fixed channel-00000 full-K5 leading tensor contraction is nonzero at the frozen rational tangent witness; the mandatory removal and scaling controls are now executed through the same classifier."
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
        "remove_highest_rejected": remove_highest_contact_rejected,
        "derived_orders": plus_orders,
    }, sort_keys=True))
    return 0 if classification in (PASS, FAIL, BLOCKED) else 2


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    raise SystemExit(main(args.out))
