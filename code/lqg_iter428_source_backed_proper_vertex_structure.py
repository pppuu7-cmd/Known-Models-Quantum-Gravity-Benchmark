#!/usr/bin/env python3
"""Iter428: source-backed EPRL/proper-vertex Hessian structure audit.

Literature authority:
  A. Shirazi, J. Engle, I. Vilensky, arXiv:1511.03644,
  especially Eqs. (27), (30), (31).
  E. Bianchi, Y. Ding, arXiv:1109.6538 provides the EPRL graviton-propagator
  context inherited by the proper-vertex calculation.

What is source-backed here:
  * the 10 + 64 block decoupling in Eq. (27),
  * the 44 + 10 + 10 zero/coupling pattern of H^R in Eq. (30),
  * det(-H^R)=det(-H_{zeta,barzeta})^2 det(-H^EPRL), Eq. (31).

What is NOT source-backed here:
  * numerical entries of H^EPRL, Q_jj or mixed blocks. Those remain controlled
    complex fixtures chosen only to stress-test the exact published identities.

No claim of a physical EPRL covariance, causal-measure transport, or D7 closure
is made by this iteration.
"""

import argparse
import json
import math
import os

import numpy as np

N_SPIN = 10
N_G = 24
N_Z = 10
N_ZBAR = 10
N_EPRL = N_G + N_Z + N_ZBAR   # 44
N_ETA = 10
N_HR = N_EPRL + 2 * N_ETA     # 64
N_FULL = N_SPIN + N_HR         # 74


def orthogonal(rng, n):
    q, r = np.linalg.qr(rng.normal(size=(n, n)))
    d = np.sign(np.diag(r))
    d[d == 0.0] = 1.0
    return q @ np.diag(d)


def positive_real_complex_symmetric(rng, n, cond_exp, imag_strength):
    """Return H with Re(-H) SPD and controlled real-part condition number."""
    u = orthogonal(rng, n)
    eig = np.geomspace(1.0, 10.0 ** (-cond_exp), n)
    real_spd = u @ np.diag(eig) @ u.T
    s = rng.normal(size=(n, n))
    s = 0.5 * (s + s.T)
    s /= max(float(np.linalg.norm(s, ord=2)), 1.0e-300)
    imag = imag_strength * math.sqrt(float(np.min(eig) * np.max(eig))) * s
    return -(real_spd + 1j * imag)


def slog_identity(lhs, rhs_parts):
    """Compare det(lhs) with the product of det(rhs_parts) stably."""
    sign_l, log_l = np.linalg.slogdet(lhs)
    if abs(sign_l) == 0.0:
        return math.inf, math.inf, False
    sign_r = 1.0 + 0.0j
    log_r = 0.0
    for m, power in rhs_parts:
        sign, logabs = np.linalg.slogdet(m)
        if abs(sign) == 0.0:
            return math.inf, math.inf, False
        sign_r *= sign ** power
        log_r += power * float(logabs)
    phase_ratio = sign_l / sign_r
    phase_error = float(abs(phase_ratio - 1.0))
    logabs_error = float(abs(float(log_l) - log_r))
    return phase_error, logabs_error, True


def rel_fro(a, b):
    return float(np.linalg.norm(a - b, ord="fro") / max(float(np.linalg.norm(b, ord="fro")), 1.0e-300))


def build_profile(index):
    cond_exponents = [1, 2, 3, 5]
    coupling_strengths = [0.01, 0.03, 0.10]
    spin_scales = [0.5, 1.0]
    cond_exp = cond_exponents[index % 4]
    coupling_strength = coupling_strengths[(index // 4) % 3]
    spin_scale = spin_scales[(index // 12) % 2]
    imag_strength = [0.05, 0.15, 0.30][(index // 2) % 3]

    rng = np.random.default_rng(428000 + index)
    eprl = positive_real_complex_symmetric(rng, N_EPRL, cond_exp, imag_strength)

    # Eq. (30): only the g,z rows couple into zeta; zbar->zeta is exactly zero.
    c = np.zeros((N_EPRL, N_ETA), dtype=complex)
    raw = rng.normal(size=(N_G + N_Z, N_ETA)) + 1j * rng.normal(size=(N_G + N_Z, N_ETA))
    raw /= max(float(np.linalg.norm(raw, ord=2)), 1.0e-300)
    c[: N_G + N_Z, :] = coupling_strength * raw
    d = c.T  # complex Hessian symmetry uses transpose, not Hermitian adjoint.

    # Eq. (31)/(text below): H_{zeta,barzeta}=-2 j_ab delta.
    j = spin_scale * np.geomspace(0.6, 2.4, N_ETA)
    jblock = -2.0 * np.diag(j).astype(complex)

    z_e = np.zeros((N_EPRL, N_ETA), dtype=complex)
    z_ec = np.zeros((N_ETA, N_EPRL), dtype=complex)
    z_eta = np.zeros((N_ETA, N_ETA), dtype=complex)

    # Eq. (30), grouped as [EPRL core | zeta | bar-zeta].
    hr = np.block([
        [eprl, c, z_e],
        [d, z_eta, jblock],
        [z_ec, jblock.T, z_eta],
    ])

    # Eq. (27): spin block Q_jj is decoupled from H^R.
    qjj = positive_real_complex_symmetric(rng, N_SPIN, min(cond_exp, 3), imag_strength)
    full = np.block([
        [qjj, np.zeros((N_SPIN, N_HR), dtype=complex)],
        [np.zeros((N_HR, N_SPIN), dtype=complex), hr],
    ])
    return {
        "cond_exp": cond_exp,
        "coupling_strength": coupling_strength,
        "spin_scale": spin_scale,
        "imag_strength": imag_strength,
        "eprl": eprl,
        "c": c,
        "d": d,
        "jblock": jblock,
        "hr": hr,
        "qjj": qjj,
        "full": full,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True, type=int)
    args = ap.parse_args()
    idx = args.index
    if not 0 <= idx < 24:
        raise SystemExit("index must be 0..23")

    p = build_profile(idx)
    eprl, hr, qjj, full, jblock = p["eprl"], p["hr"], p["qjj"], p["full"], p["jblock"]

    # Published Eq. (31). Dimensions 44, 10 and 64 are all even, but we retain
    # the exact minus signs from the paper rather than simplifying them away.
    det_phase_error, det_logabs_error, nonsingular = slog_identity(
        -hr,
        [(-jblock, 2), (-eprl, 1)],
    )

    # Published Eq. (27): inverse of block diagonal full Hessian must preserve
    # the spin inverse exactly and have vanishing spin/rest inverse couplings.
    inv_full = np.linalg.inv(full)
    inv_q = np.linalg.inv(qjj)
    spin_inverse_error = rel_fro(inv_full[:N_SPIN, :N_SPIN], inv_q)
    cross_top = float(np.linalg.norm(inv_full[:N_SPIN, N_SPIN:], ord="fro"))
    cross_bottom = float(np.linalg.norm(inv_full[N_SPIN:, :N_SPIN], ord="fro"))
    spin_cross_inverse_norm = max(cross_top, cross_bottom)

    # Positive-real-part admissibility is the branch-control condition quoted
    # after Eq. (31), tested here for the controlled EPRL and spin blocks.
    min_real_eprl = float(np.min(np.linalg.eigvalsh(np.real(-eprl))))
    min_real_qjj = float(np.min(np.linalg.eigvalsh(np.real(-qjj))))
    branch_control_fixture_ok = min_real_eprl > 0.0 and min_real_qjj > 0.0

    # Negative control A: violate the exact zero block bar-zeta -> EPRL core.
    rng = np.random.default_rng(429000 + idx)
    broken_zero = hr.copy()
    perturb = rng.normal(size=(N_ETA, N_EPRL)) + 1j * rng.normal(size=(N_ETA, N_EPRL))
    perturb /= max(float(np.linalg.norm(perturb, ord=2)), 1.0e-300)
    broken_zero[N_EPRL + N_ETA :, :N_EPRL] = 0.08 * perturb
    neg_zero_phase, neg_zero_log, neg_zero_ns = slog_identity(
        -broken_zero,
        [(-jblock, 2), (-eprl, 1)],
    )
    broken_zero_detected = bool(neg_zero_ns and max(neg_zero_phase, neg_zero_log) > 1.0e-7)

    # Negative control B: violate H_{bar-zeta,bar-zeta}=0 while keeping all
    # other published blocks untouched.
    broken_diag = hr.copy()
    broken_diag[N_EPRL + N_ETA :, N_EPRL + N_ETA :] = 0.05 * np.eye(N_ETA)
    neg_diag_phase, neg_diag_log, neg_diag_ns = slog_identity(
        -broken_diag,
        [(-jblock, 2), (-eprl, 1)],
    )
    broken_diag_detected = bool(neg_diag_ns and max(neg_diag_phase, neg_diag_log) > 1.0e-7)

    numerical_pass = bool(
        nonsingular
        and det_phase_error < 5.0e-10
        and det_logabs_error < 5.0e-10
        and spin_inverse_error < 5.0e-10
        and spin_cross_inverse_norm < 5.0e-12
        and branch_control_fixture_ok
        and broken_zero_detected
        and broken_diag_detected
    )

    out = {
        "iteration": 428,
        "profile_index": idx,
        "dimensions": {"spin": N_SPIN, "eprl_core": N_EPRL, "proper_rest": N_HR, "full": N_FULL},
        "condition_exponent": p["cond_exp"],
        "coupling_strength": p["coupling_strength"],
        "spin_scale": p["spin_scale"],
        "imag_strength": p["imag_strength"],
        "determinant_identity_phase_error": det_phase_error,
        "determinant_identity_logabs_error": det_logabs_error,
        "spin_inverse_block_error": spin_inverse_error,
        "spin_cross_inverse_norm": spin_cross_inverse_norm,
        "min_real_minus_eprl_eigenvalue": min_real_eprl,
        "min_real_minus_qjj_eigenvalue": min_real_qjj,
        "negative_controls": {
            "broken_barzeta_to_core_zero_detected": broken_zero_detected,
            "broken_barzeta_barzeta_zero_detected": broken_diag_detected,
            "broken_zero_identity_residual": max(neg_zero_phase, neg_zero_log),
            "broken_diag_identity_residual": max(neg_diag_phase, neg_diag_log),
        },
        "numerical_pass": numerical_pass,
        "classification": "PASS_SOURCE_BACKED_STRUCTURE_IDENTITY" if numerical_pass else "FAIL_SOURCE_BACKED_STRUCTURE_IDENTITY",
        "source_authority": {
            "proper_vertex": "arXiv:1511.03644 Eqs. (27),(30),(31)",
            "eprl_context": "arXiv:1109.6538",
        },
        "physical_input_status": "LITERATURE_STRUCTURE_SOURCE_BACKED__NUMERICAL_EPRL_ENTRIES_CONTROLLED",
        "d7_status": "OPEN",
        "scope_guard": "Exact published EPRL/proper-vertex block and determinant identities are tested at their true 44/64/74 dimensions, but numerical EPRL Hessian entries remain controlled fixtures. This does not yet constitute ingestion of a physical critical-point Hessian/covariance or causal-measure transport and does not close D7/NEW_REQUIRED.",
    }

    os.makedirs("build/lqg-iter428", exist_ok=True)
    with open(f"build/lqg-iter428/profile_{idx}.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not numerical_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
