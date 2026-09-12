#!/usr/bin/env python3
"""Iter436: local magnetic-closure survival audit for Iter435 slow-extremal profiles.

Frozen prospectively in recovery/ITER435_RESULT_AND_ITER436_PREREG_2026-09-12.md.
This is a necessary local SU(2) magnetic-closure diagnostic only, not a full
intertwiner projector or physical vertex test.
"""
import argparse
import itertools
import json
import os

SPINS = (0.5, 1.0, 1.5, 2.0)
VERTICES = tuple(range(5))
EDGES = tuple((a, b) for a in VERTICES for b in VERTICES if a < b)


def twice(x):
    return int(round(2.0 * x))


def values_for_j(j):
    tj = twice(j)
    return [m2 / 2.0 for m2 in range(-tj, tj + 1, 2)]


def sector(index):
    if not 0 <= index < 16:
        raise ValueError('index must be 0..15')
    sigma = {0: 1}
    for k in range(4):
        sigma[k + 1] = 1 if ((index >> k) & 1) else -1
    kappa = {(a, b): sigma[a] * sigma[b] for a, b in EDGES}
    return sigma, kappa


def outgoing_m(edge, vertex, m_edge):
    a, b = edge
    if vertex == a:
        return m_edge
    if vertex == b:
        return -m_edge
    raise ValueError('vertex not incident to edge')


def exact_bruteforce_closure(fixed_outgoing, free_js):
    if not free_js:
        return abs(sum(fixed_outgoing)) < 1e-12
    for vals in itertools.product(*(values_for_j(j) for j in free_js)):
        if abs(sum(fixed_outgoing) + sum(vals)) < 1e-12:
            return True
    return False


def independent_interval_parity_closure(fixed_outgoing, free_js):
    # Work in doubled magnetic integers. For SU(2) j, allowed m2 have the same
    # parity as 2j and fill the interval in steps of 2. Minkowski sums therefore
    # fill the summed interval with parity equal to sum(2j) mod 2.
    target2 = -sum(twice(m) for m in fixed_outgoing)
    max2 = sum(twice(j) for j in free_js)
    parity = sum(twice(j) for j in free_js) % 2
    return (-max2 <= target2 <= max2) and (target2 % 2 == parity)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', type=int, required=True)
    ap.add_argument('--cluster-size', type=int, choices=(3, 4), required=True)
    args = ap.parse_args()

    sigma, kappa = sector(args.index)
    s = args.cluster_size
    boosted = set(range(1, s + 1))
    crossing = [e for e in EDGES if ((e[0] in boosted) != (e[1] in boosted))]

    edge_data = {}
    alphas = []
    for r, e in enumerate(crossing):
        j = SPINS[r % len(SPINS)]
        sign = kappa[e]
        m = -j if sign == 1 else j
        alpha = 1.0 + abs(j + sign * m)
        alphas.append(alpha)
        edge_data[e] = {'j': j, 'm': m, 'sign': sign, 'fixed': True, 'cross_index': r}

    lam = 2.0 * s - sum(alphas)

    # Frozen diagnostic completion for noncrossing legs.
    for r, e in enumerate(EDGES):
        if e not in edge_data:
            edge_data[e] = {'j': SPINS[r % len(SPINS)], 'm': None, 'sign': kappa[e], 'fixed': False, 'global_index': r}

    vertex_rows = []
    controls_valid = lam >= 0.0
    for v in VERTICES:
        incident = [e for e in EDGES if v in e]
        if len(incident) != 4:
            controls_valid = False
        fixed_out = []
        free_js = []
        edge_rows = []
        for e in incident:
            d = edge_data[e]
            if d['fixed']:
                j, m = d['j'], d['m']
                valid_m = abs(m) <= j + 1e-12 and ((twice(j) - twice(m)) % 2 == 0)
                controls_valid = controls_valid and valid_m
                mout = outgoing_m(e, v, m)
                fixed_out.append(mout)
                edge_rows.append({'edge': list(e), 'j': j, 'fixed_m_edge': m, 'm_out': mout, 'fixed': True})
            else:
                free_js.append(d['j'])
                edge_rows.append({'edge': list(e), 'j': d['j'], 'fixed': False})
        brute = exact_bruteforce_closure(fixed_out, free_js)
        analytic = independent_interval_parity_closure(fixed_out, free_js)
        agree = brute == analytic
        controls_valid = controls_valid and agree
        vertex_rows.append({
            'vertex': v,
            'fixed_outgoing_sum': sum(fixed_out),
            'free_leg_spins': free_js,
            'bruteforce_closure_exists': brute,
            'interval_parity_closure_exists': analytic,
            'independent_checks_agree': agree,
            'edges': edge_rows,
        })

    all_vertices_allow = all(r['bruteforce_closure_exists'] for r in vertex_rows)
    if not controls_valid:
        classification = 'CONTROL_INVALID'
    elif all_vertices_allow:
        classification = 'MAGNETIC_CLOSURE_ALLOWS_SLOW_EXTREMAL_PROFILE'
    else:
        classification = 'MAGNETIC_CLOSURE_EXCLUDES_SLOW_EXTREMAL_PROFILE'

    out = {
        'iteration': 436,
        'sector_index': args.index,
        'cluster_size': s,
        'sigma': {str(k): val for k, val in sigma.items()},
        'lambda': lam,
        'iter435_obstruction_reproduced': lam >= 0.0,
        'crossing_edges': [list(e) for e in crossing],
        'edge_data': {f'{a}-{b}': d for (a, b), d in edge_data.items()},
        'vertices': vertex_rows,
        'all_vertices_allow_local_closure': all_vertices_allow,
        'controls_valid': controls_valid,
        'classification': classification,
        'scope_guard': ('Necessary local magnetic-closure diagnostic under one preregistered spin completion only; '
                        'not a full SU(2) invariant-projector test, angular contraction, physical divergence result, '
                        'or D7 promotion.'),
        'd2': 'NOT_CLOSED_COVERAGE_AND_OBJECTS',
        'd4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7_s2': 'NOT_CLOSED',
        'd7_s3': 'NOT_CLOSED',
        'd7_s4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7': 'NOT_CLOSED / NOT_YET_AUTHORIZED',
        'candidate_gravity_authorized': False,
    }
    os.makedirs('build/lqg-iter436', exist_ok=True)
    path = f'build/lqg-iter436/sector_{args.index}_s{s}.json'
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
        fh.write('\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not controls_valid:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
