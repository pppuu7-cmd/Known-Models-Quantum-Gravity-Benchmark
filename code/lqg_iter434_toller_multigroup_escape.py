#!/usr/bin/env python3
"""Iter434: correlated multi-group large-boost escape-ray audit.

Prospectively frozen after Iter433 PASS and before any Iter434 result exists.
The test gauge-fixes one K5 vertex and sends a subset of the other four group
variables along one common collinear boost ray.  Only cut edges have relative
rapidity beta.  Exact published gamma-simple Toller kernels on those edges are
combined with one radial sinh(beta)^2 Haar factor per escaping group variable.

This is an absolute exponential-envelope test only.  It is not a physical
vertex-divergence theorem and does not cover angular/boundary cancellation,
finite-beta collision/distributional structure, or normalized-vertex finiteness.
"""
import argparse
import json
import os
import mpmath as mp

mp.mp.dps = 80
GAMMAS = [mp.mpf('0.1'), mp.mpf('0.2375'), mp.mpf('0.5')]
BETAS = (mp.mpf('6'), mp.mpf('8'), mp.mpf('10'), mp.mpf('12'))
SPINS = (mp.mpf('0.5'), mp.mpf('1'), mp.mpf('1.5'), mp.mpf('2'))
VERTICES = tuple(range(5))
EDGES = tuple((a, b) for a in VERTICES for b in VERTICES if a < b)


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
    if not 0 <= i < 24:
        raise ValueError('index must be 0..23')
    gamma = GAMMAS[i // 8]
    local = i % 8
    cluster_size = local // 2 + 1
    family = 'worst' if local % 2 == 0 else 'fast-control'
    boosted = set(range(1, cluster_size + 1))
    crossing = [(a, b) for (a, b) in EDGES if ((a in boosted) != (b in boosted))]

    edge_data = []
    for edge_index, edge in enumerate(crossing):
        j = SPINS[edge_index % len(SPINS)]
        sign = 1 if edge_index % 2 == 0 else -1
        if family == 'worst':
            m = -j if sign == 1 else j
        else:
            m = j if sign == 1 else -j
        rho = gamma * j
        alpha = 1 + abs(j + sign*m)
        edge_data.append((edge, sign, j, m, rho, alpha))
    return gamma, cluster_size, family, boosted, edge_data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', type=int, required=True)
    a = ap.parse_args()
    gamma, s, family, boosted, edge_data = config(a.index)

    cut_count = len(edge_data)
    expected_cut_count = s * (5 - s)
    if cut_count != expected_cut_count:
        raise RuntimeError(f'K5 cut mismatch: {cut_count} != {expected_cut_count}')

    alpha_sum = mp.fsum(row[-1] for row in edge_data)
    expected_slope = 2*s - alpha_sum
    scientific_envelope_pass = bool(expected_slope < 0)

    weighted = []
    for beta in BETAS:
        product = mp.mpf('1')
        for edge, sign, j, m, rho, alpha in edge_data:
            product *= abs(toller(sign, j, m, rho, beta))
        weighted.append(mp.sinh(beta)**(2*s) * product)

    slopes = [
        (mp.log(y1) - mp.log(y0)) / (b1 - b0)
        for b0, b1, y0, y1 in zip(BETAS[:-1], BETAS[1:], weighted[:-1], weighted[1:])
    ]
    final_error = abs(slopes[-1] - expected_slope)
    finite = (all(mp.isfinite(x) and x > 0 for x in weighted)
              and all(mp.isfinite(x) for x in slopes))
    numerical_valid = bool(finite and final_error < mp.mpf('2e-4'))

    if not numerical_valid:
        classification = 'NUMERICAL_FAIL_MULTI_GROUP_ESCAPE_CONTROL'
    elif scientific_envelope_pass:
        classification = 'PASS_PROFILE_MULTI_GROUP_EXPONENTIAL_ENVELOPE'
    else:
        classification = 'FAIL_PROFILE_MULTI_GROUP_EXPONENTIAL_ENVELOPE'

    out = {
        'iteration': 434,
        'profile_index': a.index,
        'gamma': float(gamma),
        'cluster_size': s,
        'family': family,
        'boosted_vertices': sorted(boosted),
        'crossing_edge_count': cut_count,
        'expected_k5_cut_count': expected_cut_count,
        'alpha_sum': float(alpha_sum),
        'haar_exponent': 2*s,
        'expected_weighted_tail_slope': float(expected_slope),
        'weighted_tail_values': [float(x) for x in weighted],
        'observed_interval_slopes': [float(x) for x in slopes],
        'final_tail_slope_error': float(final_error),
        'numerical_valid': numerical_valid,
        'scientific_envelope_pass': scientific_envelope_pass,
        'classification': classification,
        'source_authority': [
            'Bianchi-Chen-Gamonal, Toller matrices and the Feynman i-epsilon in spinfoams, Phys Rev D 114 046014 (2026), arXiv:2604.24945',
            'validated Iter432/433 gamma-simple closed forms and branch asymptotic alpha = 1 + |j + sign*m|',
            'K5 4-simplex graph cut counting with vertex 0 gauge-fixed'
        ],
        'interpretation_guard': ('A nonnegative correlated-ray exponent fails this absolute exponential-envelope bound only. '
                                 'It is not a physical divergence theorem and does not exclude angular/boundary cancellation '
                                 'or a distributionally defined Feynman amplitude.'),
        'd7_s2': 'OPEN',
        'd7_s3': 'OPEN',
        'd7_s4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7_status': 'OPEN',
        'candidate_gravity_authorized': False,
    }
    os.makedirs('build/lqg-iter434', exist_ok=True)
    path = f'build/lqg-iter434/profile_{a.index}.json'
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
        fh.write('\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not numerical_valid:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
