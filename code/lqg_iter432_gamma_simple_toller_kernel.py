#!/usr/bin/env python3
"""Iter432: source-faithful gamma-simple Toller kernel audit.

Authority: Bianchi, Chen, Gamonal, Phys. Rev. D 114, 046014 (2026),
arXiv:2604.24945, Eqs. (15), (45), (46) and the large-boost decay statement.

This implements the published closed forms for gamma-simple reduced Wigner d and
Toller t^(+/-) matrices (k=j=l, rho=gamma*j) with high precision.  It checks
T+ + T- = D pointwise and the branch-specific large-beta decay exponents.
It is a kernel-level prerequisite for a direct causal-vertex quadrature, not a
vertex finiteness theorem or normalized-vertex certificate.  D7-S2/S3 remain
open and D7-S4 remains partial.
"""
import argparse, json, os
import mpmath as mp

mp.mp.dps = 80

J_VALUES = [mp.mpf('0.5'), mp.mpf('1'), mp.mpf('1.5'), mp.mpf('2')]
GAMMAS = [mp.mpf('0.1'), mp.mpf('0.2375'), mp.mpf('0.5')]
BETA_GRID = [mp.mpf(x) for x in ('0.15','0.35','0.75','1.5','3','5')]
TAIL_BETAS = (mp.mpf('6'), mp.mpf('8'))


def wigner_d(j, m, rho, beta):
    z = 1 - mp.e**(-2*beta)
    return (mp.e**(-(j - 1j*rho + m + 1)*beta)
            * mp.hyp2f1(j+m+1, j+1-1j*rho, 2*j+2, z))


def toller_t(sign, j, m, rho, beta):
    z = mp.e**(-2*beta)
    if sign == +1:
        return (mp.e**(-(j - 1j*rho + m + 1)*beta)
                * mp.gamma(2*j+2) * mp.gamma(1j*rho-m)
                / (mp.gamma(j-m+1) * mp.gamma(j+1+1j*rho))
                * mp.hyp2f1(j+m+1, j+1-1j*rho,
                             1+m-1j*rho, z))
    return (mp.e**(-(j + 1j*rho - m + 1)*beta)
            * mp.gamma(2*j+2) * mp.gamma(-1j*rho+m)
            / (mp.gamma(j+m+1) * mp.gamma(j+1-1j*rho))
            * mp.hyp2f1(j-m+1, j+1+1j*rho,
                         1-m+1j*rho, z))


def f(x):
    return float(x)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', type=int, required=True)
    a = ap.parse_args()
    i = a.index
    if not 0 <= i < 24:
        raise SystemExit('index must be 0..23')

    j = J_VALUES[i % 4]
    gamma = GAMMAS[(i // 4) % 3]
    # Two independent magnetic sectors per (j,gamma): extremal and one step in.
    m = -j if (i // 12) == 0 else (-j + 1)
    rho = gamma * j

    max_forward = mp.mpf('0')
    max_backward = mp.mpf('0')
    max_condition = mp.mpf('0')
    rows = []
    for beta in BETA_GRID:
        d = wigner_d(j, m, rho, beta)
        tp = toller_t(+1, j, m, rho, beta)
        tm = toller_t(-1, j, m, rho, beta)
        residual = tp + tm - d
        floor = mp.mpf('1e-100')
        forward = abs(residual) / max(abs(d), floor)
        backward = abs(residual) / max(abs(tp)+abs(tm)+abs(d), floor)
        condition = (abs(tp)+abs(tm)) / max(abs(d), floor)
        max_forward = max(max_forward, forward)
        max_backward = max(max_backward, backward)
        max_condition = max(max_condition, condition)
        rows.append({'beta': f(beta), 'forward_relative_error': f(forward),
                     'backward_relative_error': f(backward),
                     'cancellation_condition': f(condition)})

    b0, b1 = TAIL_BETAS
    slope_errors = {}
    slopes = {}
    for sign, label in ((+1, 'plus'), (-1, 'minus')):
        y0 = abs(toller_t(sign, j, m, rho, b0))
        y1 = abs(toller_t(sign, j, m, rho, b1))
        slope = (mp.log(y1)-mp.log(y0))/(b1-b0)
        # Published |t^(+/-)| ~ exp[-(1+|k +/- m|) beta], k=j.
        expected = -(1 + abs(j + sign*m))
        slopes[label] = {'observed': f(slope), 'expected': f(expected)}
        slope_errors[label] = abs(slope-expected)

    # Precision-aware decomposition gate + asymptotic-law gate.
    identity_ok = max_forward < mp.mpf('1e-40') and max_backward < mp.mpf('1e-50')
    tail_ok = max(slope_errors.values()) < mp.mpf('2e-4')
    passed = bool(identity_ok and tail_ok)

    out = {
        'iteration': 432,
        'profile_index': i,
        'j': f(j), 'm': f(m), 'gamma': f(gamma), 'rho': f(rho),
        'beta_grid': [f(x) for x in BETA_GRID],
        'max_forward_relative_additivity_error': f(max_forward),
        'max_backward_relative_additivity_error': f(max_backward),
        'max_cancellation_condition': f(max_condition),
        'tail_slopes': slopes,
        'max_tail_slope_error': f(max(slope_errors.values())),
        'pointwise_rows': rows,
        'numerical_pass': passed,
        'classification': ('PASS_SOURCE_FAITHFUL_GAMMA_SIMPLE_TOLLER_KERNEL'
                           if passed else 'FAIL_GAMMA_SIMPLE_TOLLER_KERNEL'),
        'source_authority': [
            'Bianchi-Chen-Gamonal, Toller matrices and the Feynman i-epsilon in spinfoams, Phys Rev D 114 046014 (2026), arXiv:2604.24945',
            'Eqs. (15), (45), (46); large-beta decay |t^(+/-)| ~ exp[-(1+|k +/- m|) beta]'
        ],
        'd7_s2': 'OPEN', 'd7_s3': 'OPEN',
        'd7_s4': 'PARTIAL_GLOBAL_NOT_CLOSED', 'd7_status': 'OPEN',
        'candidate_gravity_authorized': False,
        'scope_guard': ('Exact published gamma-simple one-wedge kernels only. This does not prove '
                        'fixed-Toller causal-vertex integrability, multi-wedge contraction finiteness, '
                        'lambda_f-weighted complete-stack cutoff removal, or same-realization UV-to-GR transport.')
    }
    os.makedirs('build/lqg-iter432', exist_ok=True)
    with open(f'build/lqg-iter432/profile_{i}.json', 'w') as fh:
        json.dump(out, fh, indent=2, sort_keys=True); fh.write('\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(2)

if __name__ == '__main__':
    main()
