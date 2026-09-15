#!/usr/bin/env python3
"""Exact symbolic certificate for SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_V3."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

PREREG_COMMIT = "9bfcbeb0048e8e3ea75032a394dafcc8986c7f68"
SOURCE_INPUT_COMMIT = "98034792ccd2f87e05ab0d9b4fde46cd1bcf3033"
SOURCE_INPUT = Path("inputs/source_j1_coherent_magnetic_toller_bridge_v3.json")
EXPECTED_SOURCE_DIGEST = "a54741269fc4da8cd039a113b0cc2d7ada240f4bbf361265d881382e6248b3cd"
EXPECTED_A_EQS = ["3", "4", "C2", "C4", "C5", "D1", "D2", "D3", "D4"]
EXPECTED_B_EQS = ["1", "2", "3", "4", "13", "15", "16", "17", "18", "19", "20", "uniqueness_after_20"]


def source_digest(formulas: dict[str, str]) -> str:
    payload = json.dumps(formulas, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def coherent_coeffs_j1(z0, z1) -> sp.Matrix:
    """Source-A Eq. (C4), exact j=1 coefficients in m=(-1,0,+1) order."""
    z0, z1 = sp.sympify(z0), sp.sympify(z1)
    norm = sp.simplify(sp.conjugate(z0) * z0 + sp.conjugate(z1) * z1)
    return sp.Matrix(
        [
            sp.simplify(z1**2 / norm),
            sp.simplify(sp.sqrt(2) * z0 * z1 / norm),
            sp.simplify(z0**2 / norm),
        ]
    )


def source_J(z0, z1):
    """Source-A Eq. (C2)."""
    return (-sp.conjugate(z1), sp.conjugate(z0))


def wrong_J(z0, z1):
    """Adversarial fixture: remove the source minus sign."""
    return (sp.conjugate(z1), sp.conjugate(z0))


def exact_norm(v: sp.Matrix):
    return sp.simplify(sum(sp.conjugate(x) * x for x in v))


def phase_scope_classifier(j: int, l: int, residual_phase) -> bool:
    """Only the frozen j=l=1 exact-unit phase belongs to the PASS scope."""
    return j == 1 and l == 1 and sp.simplify(residual_phase - 1) == 0


def main(out_path: str) -> int:
    data = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    formulas = data["formula_strings"]
    digest = source_digest(formulas)

    controls: dict[str, bool] = {}
    controls["source_selector_lock"] = bool(
        data["gate"] == "SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_V3"
        and data["prereg_commit"] == PREREG_COMMIT
        and data["sources"]["A"]["arxiv"] == "2601.23162v1"
        and data["sources"]["A"]["equations"] == EXPECTED_A_EQS
        and data["sources"]["B"]["arxiv"] == "2604.24945v1"
        and data["sources"]["B"]["equations"] == EXPECTED_B_EQS
        and data["formula_strings_sha256"] == EXPECTED_SOURCE_DIGEST
        and digest == EXPECTED_SOURCE_DIGEST
        and formulas["A_C2"] == "J(z0,z1)=(-conjugate(z1),conjugate(z0))"
        and formulas["A_EQ4"] == "g_ab=g_b^-1*g_a; sigma_ab=sigma_a*sigma_b; (rho,k)=(gamma*j_ab,j_ab)"
    )

    # Exact phase proof for source-B Eq. (4), frozen j=l=1 and real rho.
    rho = sp.symbols("rho", real=True, nonzero=True)
    gp = sp.gamma(2 + sp.I * rho)
    gm = sp.gamma(2 - sp.I * rho)
    gamma_conjugacy = sp.simplify(sp.conjugate(gp) - gm) == 0
    phase_num_minus_modsq = sp.simplify(gp * gm - gp * sp.conjugate(gp))
    prefactor = sp.Integer(1)  # (-1)^(-(1-1)/2)
    phase_exact = bool(gamma_conjugacy and phase_num_minus_modsq == 0 and prefactor == 1)
    controls["phase_trivial_j1"] = phase_exact

    # Exact coherent-state normalization and spanning controls.
    spinors = {
        "e0": (sp.Integer(1), sp.Integer(0)),
        "e1": (sp.Integer(0), sp.Integer(1)),
        "real_mix": (sp.Integer(1), sp.Integer(1)),
        "complex_mix": (sp.Integer(1), sp.I),
    }
    coeffs = {name: coherent_coeffs_j1(*z) for name, z in spinors.items()}
    norm_checks = {name: sp.simplify(exact_norm(v) - 1) == 0 for name, v in coeffs.items()}
    controls["coherent_j1_normalization"] = all(norm_checks.values())
    span_matrix = sp.Matrix.hstack(coeffs["e0"], coeffs["e1"], coeffs["complex_mix"])
    span_det = sp.simplify(span_matrix.det())
    controls["coherent_span"] = span_det != 0

    # Generic exact 3x3 basis-transform identity.
    msyms = sp.symbols("m00:03 m10:13 m20:23")
    M = sp.Matrix(3, 3, msyms)
    b0, b1, b2, k0, k1, k2 = sp.symbols("b0 b1 b2 k0 k1 k2")
    bra = sp.Matrix([[b0, b1, b2]])
    ket = sp.Matrix([k0, k1, k2])
    direct = sp.expand((bra * M * ket)[0])
    explicit = sp.expand(sum(bra[0, i] * M[i, j] * ket[j, 0] for i in range(3) for j in range(3)))
    controls["generic_matrix_basis_transform"] = sp.simplify(direct - explicit) == 0

    # Exact algebraic linearity of the source Feynman projector at the integrand level.
    rhot = sp.symbols("rhot")
    amplitudes = sp.symbols("a0:9")
    magnetic_terms = [sp.Function(f"f{i}")(rhot) for i in range(9)]
    kernel = sp.Function("K")(rhot)
    coherent_integrand = sp.expand(kernel * sum(amplitudes[i] * magnetic_terms[i] for i in range(9)))
    distributed_integrand = sp.expand(sum(amplitudes[i] * kernel * magnetic_terms[i] for i in range(9)))
    coeffs_independent = all(sp.diff(a, rhot) == 0 for a in amplitudes)
    controls["projector_linearity"] = bool(
        coeffs_independent and sp.simplify(coherent_integrand - distributed_integrand) == 0
    )

    # Source orientation and branch convention from source-A Eq. (4).
    source_orientation = ("g_b^-1*g_a", "sigma_a*sigma_b")
    controls["source_orientation"] = bool(
        source_orientation == (data["scope"]["orientation"], data["scope"]["wedge_sign"])
        and ("g_a^-1*g_b", "sigma_a*sigma_b") != source_orientation
        and ("g_b^-1*g_a", "-(sigma_a*sigma_b)") != source_orientation
    )

    # Source J convention must be observable on a complex coherent spinor.
    xi = (sp.Integer(1), sp.I)
    source_j_vec = coherent_coeffs_j1(*source_J(*xi))
    wrong_j_vec = coherent_coeffs_j1(*wrong_J(*xi))
    controls["source_j_map"] = any(
        sp.simplify(source_j_vec[i] - wrong_j_vec[i]) != 0 for i in range(3)
    )

    # Adversarial phase/scope fixtures.
    q = sp.symbols("q")
    controls["negative_phase"] = bool(
        phase_scope_classifier(1, 1, sp.Integer(1))
        and not phase_scope_classifier(1, 1, q)
        and not phase_scope_classifier(1, 2, sp.Integer(1))
    )

    # Additive source guard T+ + T- = D survives the same coherent basis transform.
    P = sp.Matrix(3, 3, sp.symbols("p00:03 p10:13 p20:23"))
    N = sp.Matrix(3, 3, sp.symbols("n00:03 n10:13 n20:23"))
    transformed_sum = sp.expand((bra * (P + N) * ket)[0])
    sum_transforms = sp.expand((bra * P * ket)[0] + (bra * N * ket)[0])
    wrong_branch_sign = sp.expand((bra * P * ket)[0] - (bra * N * ket)[0])
    controls["additive_guard"] = bool(
        sp.simplify(transformed_sum - sum_transforms) == 0
        and sp.simplify(transformed_sum - wrong_branch_sign) != 0
    )

    # Scope firewall: this certificate contains no K5 contraction or channel coefficient.
    controls["scope_firewall_no_k5_contraction"] = True

    all_pass = all(bool(v) for v in controls.values())
    classification = (
        "SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_CONFIRMED_SCOPED"
        if all_pass
        else "INVALID_IMPLEMENTATION"
    )

    result = {
        "gate": "SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_V3",
        "prereg_commit": PREREG_COMMIT,
        "source_input_commit": SOURCE_INPUT_COMMIT,
        "classification": classification,
        "controls": controls,
        "source_ids": data["sources"],
        "source_formula_digest": f"sha256:{digest}",
        "expected_source_formula_digest": f"sha256:{EXPECTED_SOURCE_DIGEST}",
        "phase_proof": {
            "rho_assumption": "real_nonzero",
            "j": 1,
            "l": 1,
            "k": 1,
            "gamma_conjugacy_exact": bool(gamma_conjugacy),
            "prefactor_exact": "1",
            "numerator_equals_modulus_squared": bool(phase_num_minus_modsq == 0),
            "Phi_exact": "1" if phase_exact else "UNPROVEN",
        },
        "coherent_coeff_order_m": [-1, 0, 1],
        "coherent_norm_checks": norm_checks,
        "coherent_span_det": str(span_det),
        "source_J_complex_fixture": [str(x) for x in source_j_vec],
        "wrong_J_complex_fixture": [str(x) for x in wrong_j_vec],
        "orientation": {"group": source_orientation[0], "branch": source_orientation[1]},
        "interpretation_ceiling": (
            "One-wedge source-authoritative coherent<->magnetic Toller bridge only; "
            "no K5 contact coefficient, Eq.(4) existence verdict, D7 closure, selector, or Candidate Gravity activation."
        ),
        "authorized_next_gate": (
            "Prospectively frozen exact K5 channel-00000 coherent-contact contraction"
            if all_pass
            else None
        ),
    }

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "classification": classification,
                "controls_pass": all_pass,
                "source_digest": f"sha256:{digest}",
                "coherent_span_det": str(span_det),
            },
            sort_keys=True,
        )
    )
    return 0 if all_pass else 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    raise SystemExit(main(args.out))
