#!/usr/bin/env python3
"""Iter439: source-faithful finite-beta gamma-simple Toller asymptotic audit.

Frozen by:
- recovery/ITER438_RESULT_AND_ITER439_PREREG_TOLLER_FINITE_BETA_2026-09-12.md
- recovery/ITER439_PREREG_NUMERICAL_CONTROL_AMENDMENT_2026-09-12.md

This is a branch-level source-formula realization test only, not a full causal-vertex
integrability/finiteness/divergence result.
"""
import argparse
import cmath
import json
import math
import os

BETAS = (2.0, 3.0, 4.0, 6.0, 8.0, 10.0)
SOURCE_JS = (2, 5)
SOURCE_GAMMAS = (7.0, 8.0)
STD_TOL = 1e-14
TIGHT_TOL = 1e-16
STD_MAX = 20000
TIGHT_MAX = 40000
AGREE_TOL = 5e-12
R10_TOL = 5e-8
ALPHA_EFF_TOL = 1e-6


def hypergeom_2f1_series(a, b, c, z, tol, max_terms):
    term = 1.0 + 0.0j
    total = 1.0 + 0.0j
    for n in range(1, max_terms + 1):
        denom = (c + (n - 1)) * n
        if denom == 0:
            return total, n, False
        term *= ((a + (n - 1)) * (b + (n - 1)) / denom) * z
        total += term
        if abs(term) <= tol * max(1.0, abs(total)):
            return total, n, True
    return total, max_terms, False


def parameters(gamma, j, m, branch):
    rho = gamma * j
    if branch == 'plus':
        alpha = j + m + 1
        a = complex(j + m + 1, 0.0)
        b = complex(j + 1, -rho)
        c = complex(1 + m, -rho)
    elif branch == 'minus':
        alpha = j - m + 1
        a = complex(j - m + 1, 0.0)
        b = complex(j + 1, rho)
        c = complex(1 - m, rho)
    else:
        raise ValueError(branch)
    return rho, alpha, a, b, c


def valid_source(gamma, j, m, branch):
    return (
        gamma in SOURCE_GAMMAS
        and j in SOURCE_JS
        and isinstance(m, int)
        and -j <= m <= j
        and branch in ('plus', 'minus')
        and gamma > 0
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gamma', type=float, required=True)
    ap.add_argument('--j', type=int, required=True)
    ap.add_argument('--m', type=int, required=True)
    ap.add_argument('--branch', choices=('plus', 'minus'), required=True)
    args = ap.parse_args()

    source_valid = valid_source(args.gamma, args.j, args.m, args.branch)
    rho, alpha, a, b, c = parameters(args.gamma, args.j, args.m, args.branch)

    rows = []
    all_converged = True
    max_std_tight_difference = 0.0
    for beta in BETAS:
        z = math.exp(-2.0 * beta)
        std, n_std, conv_std = hypergeom_2f1_series(a, b, c, z, STD_TOL, STD_MAX)
        tight, n_tight, conv_tight = hypergeom_2f1_series(a, b, c, z, TIGHT_TOL, TIGHT_MAX)
        diff = abs(std - tight)
        max_std_tight_difference = max(max_std_tight_difference, diff)
        all_converged = all_converged and conv_std and conv_tight
        rows.append({
            'beta': beta,
            'z': z,
            'std_re': std.real,
            'std_im': std.imag,
            'tight_re': tight.real,
            'tight_im': tight.imag,
            'std_terms': n_std,
            'tight_terms': n_tight,
            'std_converged': conv_std,
            'tight_converged': conv_tight,
            'std_tight_abs_difference': diff,
            'R_abs_hypergeom': abs(std),
        })

    r8 = rows[-2]['R_abs_hypergeom']
    r10 = rows[-1]['R_abs_hypergeom']
    r10_correction = abs(r10 - 1.0)
    r8_correction = abs(r8 - 1.0)
    alpha_eff = alpha - (math.log(r10) - math.log(r8)) / 2.0
    alpha_eff_error = abs(alpha_eff - alpha)

    controls = {
        'source_parameters_valid': source_valid,
        'all_series_converged': all_converged,
        'std_tight_agreement': max_std_tight_difference <= AGREE_TOL,
        'R10_tail_control': r10_correction <= R10_TOL,
        'effective_exponent_control': alpha_eff_error <= ALPHA_EFF_TOL,
        'late_tail_correction_decreases': r10_correction <= r8_correction,
    }
    controls_valid = all(controls.values())
    classification = (
        'SOURCE_TOLLER_FINITE_BETA_ASYMPTOTIC_REALIZED'
        if controls_valid else 'CONTROL_INVALID'
    )

    out = {
        'iteration': 439,
        'gamma': args.gamma,
        'j': args.j,
        'm': args.m,
        'branch': args.branch,
        'rho': rho,
        'analytic_alpha': alpha,
        'alpha_eff_8_10': alpha_eff,
        'alpha_eff_abs_error': alpha_eff_error,
        'R8_abs_correction': r8_correction,
        'R10_abs_correction': r10_correction,
        'max_std_tight_complex_abs_difference': max_std_tight_difference,
        'controls': controls,
        'controls_valid': controls_valid,
        'classification': classification,
        'beta_rows': rows,
        'source_equation': 'Bianchi-Chen-Gamonal 2026 Eq.(46), gamma-simple k=j=l, rho=gamma*j',
        'scope_guard': (
            'Gamma-simple minimal-channel individual Toller-branch finite-beta/large-beta '
            'source-formula validation only; not full K5 Haar/angular contraction, causal-vertex '
            'absolute convergence/divergence, i-epsilon collision theorem, cutoff removal, family '
            'promotion, or terminal D7.'
        ),
        'd2': 'NOT_CLOSED_COVERAGE_AND_OBJECTS',
        'd4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7_s2': 'NOT_CLOSED',
        'd7_s3': 'NOT_CLOSED',
        'd7_s4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7': 'NOT_CLOSED / NOT_YET_AUTHORIZED',
        'candidate_gravity_authorized': False,
    }

    os.makedirs('build/lqg-iter439', exist_ok=True)
    gamma_tag = str(args.gamma).replace('.', 'p')
    path = f'build/lqg-iter439/g{gamma_tag}_j{args.j}_m{args.m}_{args.branch}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not controls_valid:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
