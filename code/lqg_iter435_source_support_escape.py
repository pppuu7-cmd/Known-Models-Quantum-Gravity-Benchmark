#!/usr/bin/env python3
"""Iter435: source-induced K5 causal-support survival audit.

Prospectively frozen in recovery/ITER434_RESULT_AND_ITER435_PREREG_2026-09-12.md
before any Iter435 result exists.  This is a sign-support/envelope compatibility
audit only; it does not establish magnetic/intertwiner admissibility or physical
causal-vertex divergence.
"""
import argparse
import itertools
import json
import os

SPINS = (0.5, 1.0, 1.5, 2.0)
VERTICES = tuple(range(5))
EDGES = tuple((a, b) for a in VERTICES for b in VERTICES if a < b)
TRIANGLES = tuple(itertools.combinations(VERTICES, 3))


def sector(index):
    if not 0 <= index < 16:
        raise ValueError('index must be 0..15')
    sigma = {0: 1}
    for k in range(4):
        sigma[k + 1] = 1 if ((index >> k) & 1) else -1
    kappa = {(a, b): sigma[a] * sigma[b] for a, b in EDGES}
    return sigma, kappa


def triangle_product(kappa, tri):
    a, b, c = tri
    return kappa[tuple(sorted((a, b)))] * kappa[tuple(sorted((b, c)))] * kappa[tuple(sorted((a, c)))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', type=int, required=True)
    args = ap.parse_args()
    sigma, kappa = sector(args.index)

    triangle_products = {','.join(map(str, tri)): triangle_product(kappa, tri) for tri in TRIANGLES}
    cycle_control = all(v == 1 for v in triangle_products.values())

    rows = []
    for s in range(1, 5):
        boosted = set(range(1, s + 1))
        crossing = [(a, b) for a, b in EDGES if ((a in boosted) != (b in boosted))]
        expected_cut = s * (5 - s)
        cut_valid = len(crossing) == expected_cut
        for family in ('slow-extremal', 'fast-control'):
            alphas = []
            edge_rows = []
            for edge_index, edge in enumerate(crossing):
                j = SPINS[edge_index % len(SPINS)]
                sign = kappa[edge]
                if family == 'slow-extremal':
                    m = -j if sign == 1 else j
                else:
                    m = j if sign == 1 else -j
                alpha = 1.0 + abs(j + sign * m)
                alphas.append(alpha)
                edge_rows.append({'edge': list(edge), 'sign': sign, 'j': j, 'm': m, 'alpha': alpha})
            lam = 2.0 * s - sum(alphas)
            rows.append({
                'cluster_size': s,
                'family': family,
                'boosted_vertices': sorted(boosted),
                'crossing_edge_count': len(crossing),
                'expected_crossing_edge_count': expected_cut,
                'cut_valid': cut_valid,
                'lambda': lam,
                'envelope_pass': lam < 0.0,
                'edges': edge_rows,
            })

    fast_control_valid = all(r['envelope_pass'] for r in rows if r['family'] == 'fast-control')
    slow_failures = [r for r in rows if r['family'] == 'slow-extremal' and not r['envelope_pass']]
    structural_valid = bool(cycle_control and all(r['cut_valid'] for r in rows) and fast_control_valid)
    if not structural_valid:
        classification = 'CONTROL_INVALID'
    elif slow_failures:
        classification = 'SOURCE_SUPPORTED_SECTOR_RETAINS_SLOW_ENVELOPE_OBSTRUCTION'
    else:
        classification = 'SOURCE_SUPPORTED_SECTOR_REMOVES_SLOW_ENVELOPE_OBSTRUCTION'

    edge_sign_pattern = [kappa[e] for e in EDGES]
    out = {
        'iteration': 435,
        'sector_index': args.index,
        'sigma': {str(k): v for k, v in sigma.items()},
        'edge_order': [list(e) for e in EDGES],
        'edge_sign_pattern': edge_sign_pattern,
        'triangle_products': triangle_products,
        'cycle_control_valid': cycle_control,
        'fast_control_valid': fast_control_valid,
        'structural_valid': structural_valid,
        'slow_failure_count': len(slow_failures),
        'slow_failing_cluster_sizes': sorted({r['cluster_size'] for r in slow_failures}),
        'classification': classification,
        'profiles': rows,
        'scope_guard': ('Source-induced K5 sign support and asymptotic absolute-envelope exponents only. '
                        'No magnetic/intertwiner admissibility, angular cancellation, distributional amplitude, '
                        'physical vertex divergence or D7 family promotion is established.'),
        'd2': 'NOT_CLOSED_COVERAGE_AND_OBJECTS',
        'd4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7_s2': 'NOT_CLOSED',
        'd7_s3': 'NOT_CLOSED',
        'd7_s4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7': 'NOT_CLOSED / NOT_YET_AUTHORIZED',
        'candidate_gravity_authorized': False,
    }
    os.makedirs('build/lqg-iter435', exist_ok=True)
    path = f'build/lqg-iter435/sector_{args.index}.json'
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
        fh.write('\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not structural_valid:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
