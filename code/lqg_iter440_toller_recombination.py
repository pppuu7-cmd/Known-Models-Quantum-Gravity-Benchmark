#!/usr/bin/env python3
"""Iter440: source-faithful gamma-simple Toller recombination audit.

Frozen by recovery/ITER439_RESULT_AND_ITER440_PREREG_TOLLER_RECOMBINATION_2026-09-12.md.
This validates Eq. (45)/(46) normalization/phase and t+ + t- = d only.
"""
import argparse
import json
import math
import os

import mpmath as mp

BETAS = (0.5, 1.0, 2.0, 4.0, 8.0)
SOURCE_GAMMAS = (7.0, 8.0)
SOURCE_JS = (2, 5)
STD_DPS = 80
TIGHT_DPS = 120
CROSS_TOL = mp.mpf('1e-35')
IDENTITY_TOL = mp.mpf('1e-30')


def source_valid(gamma, j, m):
    return gamma in SOURCE_GAMMAS and j in SOURCE_JS and isinstance(m, int) and -j <= m <= j


def eval_source(gamma, j, m, beta, dps):
    with mp.workdps(dps):
        gamma_m = mp.mpf(str(gamma))
        beta_m = mp.mpf(str(beta))
        j_m = mp.mpf(j)
        m_m = mp.mpf(m)
        rho = gamma_m * j_m
        z = mp.e ** (-2 * beta_m)

        d = mp.e ** (-(j_m - 1j * rho + m_m + 1) * beta_m) * mp.hyp2f1(
            j_m + m_m + 1,
            j_m + 1 - 1j * rho,
            2 * j_m + 2,
            1 - z,
        )

        t_plus = (
            mp.e ** (-(j_m - 1j * rho + m_m + 1) * beta_m)
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
            mp.e ** (-(j_m + 1j * rho - m_m + 1) * beta_m)
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


def scaled_abs_difference(a, b):
    den = max(mp.mpf(1), abs(a), abs(b))
    return abs(a - b) / den


def identity_residual(d, tp, tm):
    den = max(mp.mpf(1), abs(d), abs(tp) + abs(tm))
    return abs(tp + tm - d) / den


def finite_complex(z):
    return bool(mp.isfinite(z.real) and mp.isfinite(z.imag))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gamma', type=float, required=True)
    ap.add_argument('--j', type=int, required=True)
    ap.add_argument('--m', type=int, required=True)
    args = ap.parse_args()

    src_ok = source_valid(args.gamma, args.j, args.m)
    rows = []
    all_finite = True
    max_cross = mp.mpf(0)
    max_identity_std = mp.mpf(0)
    max_identity_tight = mp.mpf(0)

    for beta in BETAS:
        d80, tp80, tm80 = eval_source(args.gamma, args.j, args.m, beta, STD_DPS)
        d120, tp120, tm120 = eval_source(args.gamma, args.j, args.m, beta, TIGHT_DPS)

        # Numerical-repair note: eval_source intentionally computes at 80/120 dps,
        # but mpmath restores the ambient default precision after workdps exits.
        # All cross-precision and recombination residual arithmetic must therefore
        # also be evaluated in a high-precision context; otherwise the exact source
        # identity is spuriously rounded at the ~1e-18 level. Frozen equations,
        # matrix, thresholds and interpretation are unchanged.
        with mp.workdps(TIGHT_DPS + 20):
            finite = all(finite_complex(z) for z in (d80, tp80, tm80, d120, tp120, tm120))
            cross_d = scaled_abs_difference(d80, d120)
            cross_p = scaled_abs_difference(tp80, tp120)
            cross_m = scaled_abs_difference(tm80, tm120)
            cross = max(cross_d, cross_p, cross_m)
            eps80 = identity_residual(d80, tp80, tm80)
            eps120 = identity_residual(d120, tp120, tm120)

        all_finite &= finite
        max_cross = max(max_cross, cross)
        max_identity_std = max(max_identity_std, eps80)
        max_identity_tight = max(max_identity_tight, eps120)

        rows.append({
            'beta': beta,
            'finite': finite,
            'scaled_cross_precision_d': float(cross_d),
            'scaled_cross_precision_t_plus': float(cross_p),
            'scaled_cross_precision_t_minus': float(cross_m),
            'scaled_identity_residual_80dps': float(eps80),
            'scaled_identity_residual_120dps': float(eps120),
            'abs_d_120dps': float(abs(d120)),
            'abs_t_plus_120dps': float(abs(tp120)),
            'abs_t_minus_120dps': float(abs(tm120)),
        })

    controls = {
        'source_parameters_valid': src_ok,
        'all_values_finite': all_finite,
        'cross_precision_agreement': bool(max_cross <= CROSS_TOL),
        'identity_residual_80dps': bool(max_identity_std <= IDENTITY_TOL),
        'identity_residual_120dps': bool(max_identity_tight <= IDENTITY_TOL),
        'branches_independently_evaluated': True,
    }
    controls_valid = all(controls.values())
    classification = (
        'SOURCE_TOLLER_RECOMBINATION_IDENTITY_REALIZED'
        if controls_valid else 'CONTROL_OR_IDENTITY_INVALID'
    )

    out = {
        'iteration': 440,
        'gamma': args.gamma,
        'j': args.j,
        'm': args.m,
        'rho': args.gamma * args.j,
        'beta_grid': list(BETAS),
        'standard_dps': STD_DPS,
        'tight_dps': TIGHT_DPS,
        'cross_precision_tolerance': float(CROSS_TOL),
        'identity_tolerance': float(IDENTITY_TOL),
        'max_scaled_cross_precision_difference': float(max_cross),
        'max_scaled_identity_residual_80dps': float(max_identity_std),
        'max_scaled_identity_residual_120dps': float(max_identity_tight),
        'controls': controls,
        'controls_valid': controls_valid,
        'classification': classification,
        'rows': rows,
        'source_equations': 'Bianchi-Chen-Gamonal 2026 Eq.(45),(46), gamma-simple k=j=l, rho=gamma*j; t(+)+t(-)=d',
        'scope_guard': (
            'Source-level gamma-simple reduced Toller/Wigner finite-beta recombination validation only; '
            'not full K5 Haar/angular contraction, causal-vertex convergence/divergence, spectral collision theorem, '
            'cutoff removal, family promotion, or terminal D7.'
        ),
        'd2': 'NOT_CLOSED_COVERAGE_AND_OBJECTS',
        'd4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7_s2': 'NOT_CLOSED',
        'd7_s3': 'NOT_CLOSED',
        'd7_s4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7': 'NOT_CLOSED / NOT_YET_AUTHORIZED',
        'candidate_gravity_authorized': False,
    }

    os.makedirs('build/lqg-iter440', exist_ok=True)
    tag = str(args.gamma).replace('.', 'p')
    path = f'build/lqg-iter440/g{tag}_j{args.j}_m{args.m}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not controls_valid:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
