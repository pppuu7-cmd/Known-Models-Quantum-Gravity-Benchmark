#!/usr/bin/env python3
"""Iter433: four-wedge single-group large-boost radial-envelope audit.

Prospectively frozen after Iter432 PASS and before GitHub result inspection.
Uses the published gamma-simple Toller closed forms and large-boost exponents.
For the four wedges incident on one tetrahedral SL(2,C) group integration, it
combines |T| tails with the radial Haar growth sinh(beta)^2.  This can only close
the single-group large-boost tail obstruction; it is not a full causal-vertex
integrability or normalized-vertex certificate.
"""
import argparse, json, os
import mpmath as mp

mp.mp.dps = 80
GAMMAS = [mp.mpf('0.1'), mp.mpf('0.2375'), mp.mpf('0.5')]
JS = [mp.mpf('0.5'), mp.mpf('1'), mp.mpf('1.5'), mp.mpf('2')]
BETAS = (mp.mpf('6'), mp.mpf('8'), mp.mpf('10'), mp.mpf('12'))


def toller(sign, j, m, rho, beta):
    z = mp.e**(-2*beta)
    if sign == 1:
        return (mp.e**(-(j - 1j*rho + m + 1)*beta)
                * mp.gamma(2*j+2) * mp.gamma(1j*rho-m)
                / (mp.gamma(j-m+1) * mp.gamma(j+1+1j*rho))
                * mp.hyp2f1(j+m+1, j+1-1j*rho, 1+m-1j*rho, z))
    return (mp.e**(-(j + 1j*rho - m + 1)*beta)
            * mp.gamma(2*j+2) * mp.gamma(-1j*rho+m)
            / (mp.gamma(j+m+1) * mp.gamma(j+1-1j*rho))
            * mp.hyp2f1(j-m+1, j+1+1j*rho, 1-m+1j*rho, z))


def config(i):
    gamma = GAMMAS[(i // 8) % 3]
    mode = i % 8
    wedges = []
    for w, j in enumerate(JS):
        if mode == 0:
            sign, m = 1, -j                 # worst + branch per wedge
        elif mode == 1:
            sign, m = -1, j                 # worst - branch per wedge
        elif mode == 2:
            sign = 1 if w % 2 == 0 else -1
            m = -j if sign == 1 else j       # mixed worst branches
        elif mode == 3:
            sign = 1 if w % 2 == 0 else -1
            m = j if sign == 1 else -j       # mixed fast branches
        elif mode == 4:
            sign, m = 1, j
        elif mode == 5:
            sign, m = -1, -j
        elif mode == 6:
            sign = 1 if w < 2 else -1
            m = -j + 1 if sign == 1 else j - 1
        else:
            sign = -1 if w < 2 else 1
            m = j - 1 if sign == -1 else -j + 1
        wedges.append((sign, j, m, gamma*j))
    return gamma, mode, wedges


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', type=int, required=True)
    a = ap.parse_args()
    i = a.index
    if not 0 <= i < 24:
        raise SystemExit('index 0..23')

    gamma, mode, wedges = config(i)
    # Published |t^(+/-)| ~ exp[-(1+|j +/- m|) beta].
    alphas = [1 + abs(j + sign*m) for sign, j, m, rho in wedges]
    # sinh(beta)^2 contributes +2 beta asymptotically.
    expected_slope = mp.mpf('2') - sum(alphas)
    margin = -expected_slope

    vals = []
    for beta in BETAS:
        product = mp.mpf('1')
        for sign, j, m, rho in wedges:
            product *= abs(toller(sign, j, m, rho, beta))
        vals.append(mp.sinh(beta)**2 * product)

    slopes = []
    for b0, b1, y0, y1 in zip(BETAS[:-1], BETAS[1:], vals[:-1], vals[1:]):
        slopes.append((mp.log(y1) - mp.log(y0))/(b1-b0))

    final_err = abs(slopes[-1] - expected_slope)
    monotone = all(vals[k+1] < vals[k] for k in range(len(vals)-1))

    # Frozen gates: analytic worst-case margin >=2; exact-kernel numerical tail
    # agrees within 2e-4, decreases throughout beta=6..12, and retains at least
    # 1.5 units of exponential decay after radial Haar growth.
    analytic_ok = margin >= mp.mpf('2')
    numeric_ok = (final_err < mp.mpf('2e-4') and monotone
                  and slopes[-1] < -mp.mpf('1.5'))
    passed = bool(analytic_ok and numeric_ok)

    out = {
        'iteration': 433,
        'profile_index': i,
        'gamma': float(gamma),
        'mode': mode,
        'expected_weighted_tail_slope': float(expected_slope),
        'analytic_decay_margin_over_haar': float(margin),
        'weighted_tail_values': [float(x) for x in vals],
        'observed_interval_slopes': [float(x) for x in slopes],
        'final_tail_slope_error': float(final_err),
        'strictly_decreasing': bool(monotone),
        'numerical_pass': passed,
        'classification': ('PASS_SINGLE_GROUP_LARGE_BOOST_RADIAL_ENVELOPE'
                           if passed else 'FAIL_SINGLE_GROUP_LARGE_BOOST_RADIAL_ENVELOPE'),
        'source_authority': [
            'Bianchi-Chen-Gamonal, Toller matrices and the Feynman i-epsilon in spinfoams, Phys Rev D 114 046014 (2026), arXiv:2604.24945',
            'gamma-simple Toller closed forms and |t^(+/-)| ~ exp[-(1+|j +/- m|) beta]'
        ],
        'd7_s2': 'OPEN',
        'd7_s3': 'OPEN',
        'd7_s4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7_status': 'OPEN',
        'candidate_gravity_authorized': False,
        'scope_guard': ('Four incident published gamma-simple Toller kernels times radial sinh(beta)^2 Haar growth only. '
                        'No finite-beta pole/collision control, angular or simultaneous multi-group escape control, '
                        'boundary-contracted normalized vertex certificate, stack cutoff removal, or terminal D7 classification.')
    }
    os.makedirs('build/lqg-iter433', exist_ok=True)
    with open(f'build/lqg-iter433/profile_{i}.json', 'w') as fh:
        json.dump(out, fh, indent=2, sort_keys=True); fh.write('\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
