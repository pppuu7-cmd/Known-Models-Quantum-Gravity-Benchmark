#!/usr/bin/env python3
"""Iter442: source-faithful spectral Feynman-i-epsilon / Toller-pole gate.

Extends the old j=1/2 finite-epsilon checks to the source-faithful gamma-simple
j=2,5 matrix used by Iter439-440.  The epsilon shift is in spectral rho-tilde,
never in beta.  This is deliberately nonterminal for D7.
"""
import argparse
import json
import os

import mpmath as mp

BETAS = ("0.5", "2.0", "8.0")
EPSILONS = ("1e-2", "1e-4", "1e-6", "1e-8")
POLE_DELTAS = ("1e-8", "1e-10", "1e-12")
SOURCE_GAMMAS = (7.0, 8.0)
SOURCE_JS = (2, 5)
DPS = 140
RESIDUE_TOL = mp.mpf("1e-6")
POLE_CAUCHY_TOL = mp.mpf("1e-6")
MIN_SEPARATION = mp.mpf("10")
KERNEL_NORM_TOL = mp.mpf("1e-80")


def source_valid(gamma, j, m):
    return gamma in SOURCE_GAMMAS and j in SOURCE_JS and isinstance(m, int) and -j <= m <= j


def eval_source_rho(j, m, rho, beta, dps=DPS):
    """Bianchi-Chen-Gamonal Eq.(45),(46), gamma-simple k=j=l, arbitrary complex rho."""
    with mp.workdps(dps):
        rho = mp.mpc(rho)
        beta = mp.mpf(str(beta))
        j_m = mp.mpf(j)
        m_m = mp.mpf(m)
        z = mp.e ** (-2 * beta)

        d = mp.e ** (-(j_m - 1j * rho + m_m + 1) * beta) * mp.hyp2f1(
            j_m + m_m + 1,
            j_m + 1 - 1j * rho,
            2 * j_m + 2,
            1 - z,
        )
        t_plus = (
            mp.e ** (-(j_m - 1j * rho + m_m + 1) * beta)
            * mp.gamma(2 * j_m + 2)
            * mp.gamma(1j * rho - m_m)
            / (mp.gamma(j_m - m_m + 1) * mp.gamma(j_m + 1 + 1j * rho))
            * mp.hyp2f1(
                j_m + m_m + 1,
                j_m + 1 - 1j * rho,
                1 + m_m - 1j * rho,
                z,
            )
        )
        t_minus = (
            mp.e ** (-(j_m + 1j * rho - m_m + 1) * beta)
            * mp.gamma(2 * j_m + 2)
            * mp.gamma(-1j * rho + m_m)
            / (mp.gamma(j_m + m_m + 1) * mp.gamma(j_m + 1 - 1j * rho))
            * mp.hyp2f1(
                j_m - m_m + 1,
                j_m + 1 + 1j * rho,
                1 - m_m + 1j * rho,
                z,
            )
        )
        return mp.mpc(d), mp.mpc(t_plus), mp.mpc(t_minus)


def toller_kernel(j, rhotilde, rho):
    """Published Eq.(16) specialized to l=j."""
    with mp.workdps(DPS + 20):
        rhotilde = mp.mpc(rhotilde)
        rho = mp.mpc(rho)
        out = mp.mpc(1)
        for n in range(0, 2 * j + 1):
            out *= (1j * rhotilde - (n - j)) / (1j * rho - (n - j))
        return out


def finite_complex(z):
    return bool(mp.isfinite(z.real) and mp.isfinite(z.imag))


def scaled_error(a, b):
    with mp.workdps(DPS + 20):
        return abs(a - b) / max(mp.mpf(1), abs(a), abs(b))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gamma", type=float, required=True)
    ap.add_argument("--j", type=int, required=True)
    ap.add_argument("--m", type=int, required=True)
    args = ap.parse_args()

    valid = source_valid(args.gamma, args.j, args.m)
    rho = mp.mpf(str(args.gamma)) * args.j
    toller_ps = list(range(-args.j, args.j + 1))

    kernel_norm_error = abs(toller_kernel(args.j, rho, rho) - 1)
    min_separation = mp.inf
    for eps_s in EPSILONS:
        eps = mp.mpf(eps_s)
        for sign in (+1, -1):
            feynman_pole = mp.mpc(rho, sign * eps)
            for p in toller_ps:
                toller_pole = -1j * p
                min_separation = min(min_separation, abs(feynman_pole - toller_pole))

    residue_rows = []
    pole_rows = []
    all_finite = True
    all_monotone = True
    max_final_residue_error = mp.mpf(0)
    max_pole_cauchy = mp.mpf(0)

    for beta_s in BETAS:
        beta = mp.mpf(beta_s)
        _, tp0, tm0 = eval_source_rho(args.j, args.m, rho, beta)
        all_finite &= finite_complex(tp0) and finite_complex(tm0)

        for branch, target, sign in (("plus", tp0, +1), ("minus", tm0, -1)):
            errs = []
            points = []
            for eps_s in EPSILONS:
                eps = mp.mpf(eps_s)
                shifted = mp.mpc(rho, sign * eps)
                _, tp, tm = eval_source_rho(args.j, args.m, shifted, beta)
                t = tp if branch == "plus" else tm
                residue = toller_kernel(args.j, shifted, rho) * t
                err = scaled_error(residue, target)
                errs.append(err)
                all_finite &= finite_complex(residue) and mp.isfinite(err)
                points.append({
                    "epsilon": eps_s,
                    "scaled_error": float(err),
                    "abs_residue": float(abs(residue)),
                    "abs_target": float(abs(target)),
                })
            monotone = all(errs[i + 1] <= errs[i] for i in range(len(errs) - 1))
            all_monotone &= monotone
            max_final_residue_error = max(max_final_residue_error, errs[-1])
            residue_rows.append({
                "beta": beta_s,
                "branch": branch,
                "monotone_convergence": monotone,
                "points": points,
            })

        # At each published Toller-pole location, Eq.(16) must cancel the
        # meromorphic pole of each branch.  Probe a fixed real approach and
        # require the last two scales to be Cauchy-stable in a scaled norm.
        for branch in ("plus", "minus"):
            for p in toller_ps:
                values = []
                finite_here = True
                for delta_s in POLE_DELTAS:
                    delta = mp.mpf(delta_s)
                    shifted = mp.mpc(delta, -p)  # i*rhotilde = p at delta -> 0
                    _, tp, tm = eval_source_rho(args.j, args.m, shifted, beta)
                    t = tp if branch == "plus" else tm
                    projected = toller_kernel(args.j, shifted, rho) * t
                    finite_here &= finite_complex(projected)
                    values.append(projected)
                cauchy = scaled_error(values[-1], values[-2])
                all_finite &= finite_here and mp.isfinite(cauchy)
                max_pole_cauchy = max(max_pole_cauchy, cauchy)
                pole_rows.append({
                    "beta": beta_s,
                    "branch": branch,
                    "toller_integer_p": p,
                    "toller_pole_rho_real": 0.0,
                    "toller_pole_rho_imag": float(-p),
                    "finite_all_deltas": finite_here,
                    "last_pair_scaled_difference": float(cauchy),
                    "abs_projected_last": float(abs(values[-1])),
                })

    controls = {
        "source_parameters_valid": valid,
        "kernel_normalization": bool(kernel_norm_error <= KERNEL_NORM_TOL),
        "feynman_toller_poles_separated": bool(min_separation >= MIN_SEPARATION),
        "all_values_finite": all_finite,
        "residue_errors_monotone": all_monotone,
        "residue_final_error_below_frozen_tolerance": bool(max_final_residue_error <= RESIDUE_TOL),
        "toller_pole_products_cauchy_stable": bool(max_pole_cauchy <= POLE_CAUCHY_TOL),
        "epsilon_is_spectral_not_beta": True,
    }
    controls_valid = all(controls.values())
    classification = (
        "SOURCE_SPECTRAL_PROJECTOR_AND_TOLLER_POLE_CANCELLATION_REALIZED"
        if controls_valid else "SOURCE_SPECTRAL_PROJECTOR_CONTROL_OR_GATE_INVALID"
    )

    out = {
        "iteration": 442,
        "gamma": args.gamma,
        "j": args.j,
        "m": args.m,
        "rho": float(rho),
        "beta_grid": list(BETAS),
        "epsilon_grid": list(EPSILONS),
        "pole_delta_grid": list(POLE_DELTAS),
        "dps": DPS,
        "kernel_normalization_error": float(kernel_norm_error),
        "minimum_feynman_to_toller_pole_distance": float(min_separation),
        "max_final_residue_scaled_error": float(max_final_residue_error),
        "max_toller_pole_last_pair_scaled_difference": float(max_pole_cauchy),
        "controls": controls,
        "controls_valid": controls_valid,
        "classification": classification,
        "residue_rows": residue_rows,
        "pole_rows": pole_rows,
        "source_equations": "Bianchi-Chen-Gamonal 2026 Eq.(11),(16)-(20),(45),(46), gamma-simple k=j=l",
        "scope_guard": "Source spectral projector/pole-cancellation gate only; not full K5 Haar/angular causal-vertex convergence, cutoff removal, family terminality, D7-S3/S4 closure, terminal D7, or Candidate Gravity activation.",
        "d7_s2": "STRENGTHENED_BUT_NOT_CLOSED" if controls_valid else "NOT_CLOSED",
        "d7_s3": "NOT_CLOSED",
        "d7_s4": "PARTIAL_GLOBAL_NOT_CLOSED",
        "d7": "NOT_CLOSED / NOT_YET_AUTHORIZED",
        "candidate_gravity_authorized": False,
    }

    os.makedirs("build/lqg-iter442", exist_ok=True)
    tag = str(args.gamma).replace(".", "p")
    path = f"build/lqg-iter442/g{tag}_j{args.j}_m{args.m}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not controls_valid:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
