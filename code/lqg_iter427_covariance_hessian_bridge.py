#!/usr/bin/env python3
"""Iter427: covariance/Hessian bridge validation with explicit gauge/null modes.

This is deliberately a controlled-fixture validation.  It does NOT provide a
source-backed EPRL/spin-foam Hessian or covariance.  The purpose is to make the
numerical bridge safe before such an input is ingested: no raw inverse or raw
Cholesky is allowed on a matrix carrying expected null modes.
"""
import argparse
import json
import math
import os

import numpy as np

N = 10


def rel_fro(a, b):
    den = max(float(np.linalg.norm(b, ord="fro")), 1.0e-300)
    return float(np.linalg.norm(a - b, ord="fro") / den)


def symmetry_error(a):
    den = max(float(np.linalg.norm(a, ord="fro")), 1.0e-300)
    return float(np.linalg.norm(a - a.T, ord="fro") / den)


def analyze_bridge(h, expected_rank=None):
    """Return physical-subspace data or an explicit rejection reason."""
    h = np.asarray(h, dtype=float)
    if h.ndim != 2 or h.shape[0] != h.shape[1]:
        return {"accepted": False, "reason": "NOT_SQUARE"}
    sym_err = symmetry_error(h)
    if sym_err > 1.0e-11:
        return {"accepted": False, "reason": "NON_SYMMETRIC", "symmetry_error": sym_err}

    hs = 0.5 * (h + h.T)
    vals, vecs = np.linalg.eigh(hs)
    scale = max(float(np.max(np.abs(vals))), 1.0)
    tol = max(1.0e-12 * scale, 1.0e-14)
    negative = vals < -tol
    if np.any(negative):
        return {
            "accepted": False,
            "reason": "INDEFINITE_PHYSICAL_HESSIAN",
            "symmetry_error": sym_err,
            "min_eigenvalue": float(np.min(vals)),
            "tolerance": tol,
        }

    pos = vals > tol
    rank = int(np.count_nonzero(pos))
    nullity = int(len(vals) - rank)
    if rank == 0:
        return {"accepted": False, "reason": "NO_PHYSICAL_SUBSPACE"}
    if expected_rank is not None and rank != expected_rank:
        return {
            "accepted": False,
            "reason": "UNEXPECTED_NUMERICAL_RANK",
            "rank": rank,
            "expected_rank": int(expected_rank),
            "tolerance": tol,
        }

    vp = vecs[:, pos]
    ep = vals[pos]
    vn = vecs[:, ~pos]
    p_phys = vp @ vp.T
    p_null = np.eye(h.shape[0]) - p_phys
    h_phys = vp @ np.diag(ep) @ vp.T
    covariance = vp @ np.diag(1.0 / ep) @ vp.T
    log_pdet = float(np.sum(np.log(ep)))
    return {
        "accepted": True,
        "reason": "ADMISSIBLE_PROJECTED_HESSIAN",
        "symmetry_error": sym_err,
        "rank": rank,
        "nullity": nullity,
        "tolerance": tol,
        "eigen_min_physical": float(np.min(ep)),
        "eigen_max_physical": float(np.max(ep)),
        "condition_number_physical": float(np.max(ep) / np.min(ep)),
        "log_pseudodeterminant": log_pdet,
        "H_projected": h_phys,
        "C_projected": covariance,
        "P_phys": p_phys,
        "P_null": p_null,
        "V_null": vn,
    }


def orthogonal(seed, n=N):
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(n, n))
    q, r = np.linalg.qr(a)
    # Deterministic sign convention removes QR sign ambiguity.
    d = np.sign(np.diag(r))
    d[d == 0.0] = 1.0
    return q @ np.diag(d)


def controlled_fixture(index):
    ranks = [4, 5, 6, 7, 8, 9]
    condition_exponents = [1, 2, 3, 5]
    rank = ranks[index % len(ranks)]
    cond_exp = condition_exponents[index // len(ranks)]
    cond = 10.0 ** cond_exp
    # Hessian physical eigenvalues span [1/cond, 1]. Exact gauge modes are zero.
    physical = np.geomspace(1.0, 1.0 / cond, rank)
    spectrum = np.concatenate([physical, np.zeros(N - rank)])
    q = orthogonal(427000 + index)
    h = q @ np.diag(spectrum) @ q.T
    return h, rank, N - rank, cond_exp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", type=int, required=True)
    args = ap.parse_args()
    idx = args.index
    if not 0 <= idx < 24:
        raise SystemExit("index must be in 0..23")

    h, expected_rank, expected_nullity, cond_exp = controlled_fixture(idx)
    base = analyze_bridge(h, expected_rank=expected_rank)
    if not base["accepted"]:
        raise SystemExit("controlled fixture unexpectedly rejected: " + json.dumps(base, default=str))

    hp = base["H_projected"]
    cp = base["C_projected"]
    pp = base["P_phys"]
    pn = base["P_null"]

    # Moore-Penrose / physical-subspace inverse identities.
    left_inverse_error = rel_fro(h @ cp, pp)
    right_inverse_error = rel_fro(cp @ h, pp)
    mp_hch_error = rel_fro(h @ cp @ h, h)
    mp_chc_error = rel_fro(cp @ h @ cp, cp)
    projection_idempotence_error = rel_fro(pp @ pp, pp)
    null_annihilation_error = float(np.linalg.norm(h @ pn, ord="fro") / max(np.linalg.norm(h, ord="fro"), 1.0e-300))
    reconstruction_error = rel_fro(hp, h)

    # Orthogonal basis invariance of rank/nullity and pseudodeterminant.
    r = orthogonal(428000 + idx)
    h_rot = r @ h @ r.T
    rot = analyze_bridge(h_rot, expected_rank=expected_rank)
    rotation_rank_ok = bool(rot.get("accepted") and rot.get("rank") == base["rank"] and rot.get("nullity") == base["nullity"])
    rotation_logpdet_error = abs(float(rot["log_pseudodeterminant"]) - float(base["log_pseudodeterminant"])) if rot.get("accepted") else math.inf

    # Regulator identity on the *known null subspace* only:
    # det(H + eps P_null) = pdet(H) eps^nullity.
    regulator_eps = [1.0e-3, 1.0e-5, 1.0e-7, 1.0e-9]
    regulator_residuals = []
    regulator_signs = []
    for eps in regulator_eps:
        sign, logdet = np.linalg.slogdet(h + eps * pn)
        expected = float(base["log_pseudodeterminant"]) + expected_nullity * math.log(eps)
        regulator_signs.append(float(sign))
        regulator_residuals.append(abs(float(logdet) - expected))
    max_regulator_logdet_residual = max(regulator_residuals)

    # Negative control 1: genuine non-symmetry must be rejected.
    h_nonsym = h.copy()
    h_nonsym[0, 1] += 1.0e-4
    nonsym = analyze_bridge(h_nonsym)
    nonsym_rejected = (not nonsym["accepted"] and nonsym["reason"] == "NON_SYMMETRIC")

    # Negative control 2: a symmetric negative physical mode must be rejected.
    vals, vecs = np.linalg.eigh(0.5 * (h + h.T))
    positive_ids = np.where(vals > base["tolerance"])[0]
    j = int(positive_ids[0])  # smallest positive mode
    h_indef = h - 2.5 * vals[j] * np.outer(vecs[:, j], vecs[:, j])
    indef = analyze_bridge(h_indef)
    indefinite_rejected = (not indef["accepted"] and indef["reason"] == "INDEFINITE_PHYSICAL_HESSIAN")

    numerical_pass = bool(
        base["rank"] == expected_rank
        and base["nullity"] == expected_nullity
        and left_inverse_error < 2.0e-8
        and right_inverse_error < 2.0e-8
        and mp_hch_error < 2.0e-8
        and mp_chc_error < 2.0e-8
        and projection_idempotence_error < 2.0e-10
        and null_annihilation_error < 2.0e-9
        and reconstruction_error < 2.0e-9
        and rotation_rank_ok
        and rotation_logpdet_error < 2.0e-7
        and all(s > 0.0 for s in regulator_signs)
        and max_regulator_logdet_residual < 2.0e-6
        and nonsym_rejected
        and indefinite_rejected
    )

    out = {
        "iteration": 427,
        "profile_index": idx,
        "fixture_kind": "CONTROLLED_GAUGE_NULL_HESSIAN",
        "dimension": N,
        "expected_rank": expected_rank,
        "expected_nullity": expected_nullity,
        "condition_exponent": cond_exp,
        "measured_rank": base["rank"],
        "measured_nullity": base["nullity"],
        "physical_condition_number": base["condition_number_physical"],
        "left_inverse_error": left_inverse_error,
        "right_inverse_error": right_inverse_error,
        "moore_penrose_hch_error": mp_hch_error,
        "moore_penrose_chc_error": mp_chc_error,
        "projection_idempotence_error": projection_idempotence_error,
        "null_annihilation_error": null_annihilation_error,
        "reconstruction_error": reconstruction_error,
        "rotation_rank_ok": rotation_rank_ok,
        "rotation_logpdet_error": rotation_logpdet_error,
        "regulator_eps": regulator_eps,
        "regulator_logdet_residuals": regulator_residuals,
        "max_regulator_logdet_residual": max_regulator_logdet_residual,
        "negative_controls": {
            "nonsymmetric_rejected": bool(nonsym_rejected),
            "indefinite_rejected": bool(indefinite_rejected),
            "nonsymmetric_reason": nonsym["reason"],
            "indefinite_reason": indef["reason"],
        },
        "numerical_pass": numerical_pass,
        "classification": "PASS_BRIDGE_FRAMEWORK_VALIDATION" if numerical_pass else "FAIL_BRIDGE_FRAMEWORK_VALIDATION",
        "physical_input_status": "SOURCE_BACKED_EPRL_SPINFOAM_INPUT_ABSENT",
        "d7_status": "OPEN",
        "scope_guard": "Controlled gauge/null-mode Hessian fixtures only. This validates the covariance/Hessian bridge, projection, pseudoinverse, pseudodeterminant and regulator accounting; it is not a physical EPRL/spin-foam covariance or Hessian, does not derive causal-measure transport, and does not close D7/NEW_REQUIRED.",
    }

    os.makedirs("build/lqg-iter427", exist_ok=True)
    path = f"build/lqg-iter427/profile_{idx}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not numerical_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
