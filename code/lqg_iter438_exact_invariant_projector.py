#!/usr/bin/env python3
"""Iter438: exact source-backed K5 invariant-projector/global-magnetic support audit.

Frozen in recovery/ITER438_PREREG_EXACT_INVARIANT_PROJECTOR_2026-09-12.md.
"""
import argparse
import itertools
import json
import math
import os
from fractions import Fraction

VERTICES = tuple(range(5))
EDGES = tuple((a, b) for a in VERTICES for b in VERTICES if a < b)
SURVIVORS = {
    (10,3),(10,4),(11,3),(12,3),(12,4),(13,3),(14,3),
    (3,4),(5,4),(6,4),(9,3),(9,4),
}


def source_spin(edge):
    return 5 if 0 in edge else 2


def m_values(j):
    return list(range(-j, j + 1))


def sector(index):
    sigma = {0: 1}
    for k in range(4):
        sigma[k + 1] = 1 if ((index >> k) & 1) else -1
    return sigma, {(a,b): sigma[a] * sigma[b] for a,b in EDGES}


def outgoing(edge, vertex, m):
    a,b = edge
    return m if vertex == a else -m


def triangle(j1,j2,j3):
    return abs(j1-j2) <= j3 <= j1+j2


def wigner3j_racah_sum(j1,j2,j3,m1,m2,m3):
    """Return the exact rational Racah sum factor; 3j is zero iff this is zero
    after standard selection rules. Spins and m are integer in the frozen gate.
    """
    if m1 + m2 + m3 != 0 or not triangle(j1,j2,j3):
        return Fraction(0,1)
    if any(abs(m) > j for j,m in ((j1,m1),(j2,m2),(j3,m3))):
        return Fraction(0,1)
    # All factorial arguments outside the z-dependent terms must be nonnegative.
    static = [j1+j2-j3, j1-j2+j3, -j1+j2+j3,
              j1+m1,j1-m1,j2+m2,j2-m2,j3+m3,j3-m3]
    if min(static) < 0:
        return Fraction(0,1)
    zmin = max(0, j2-j3-m1, j1-j3+m2)
    zmax = min(j1+j2-j3, j1-m1, j2+m2)
    total = Fraction(0,1)
    for z in range(zmin, zmax+1):
        args = [z, j1+j2-j3-z, j1-m1-z, j2+m2-z,
                j3-j2+m1+z, j3-j1-m2+z]
        if min(args) < 0:
            continue
        den = 1
        for a in args:
            den *= math.factorial(a)
        total += Fraction(-1 if z % 2 else 1, den)
    return total


def cg_nonzero(j1,m1,j2,m2,k,M):
    if M != m1 + m2 or abs(M) > k:
        return False
    return wigner3j_racah_sum(j1,j2,k,m1,m2,-M) != 0


def projector_support(js, ms, pairing):
    a,b,c,d = pairing
    j1,j2,j3,j4 = js[a],js[b],js[c],js[d]
    m1,m2,m3,m4 = ms[a],ms[b],ms[c],ms[d]
    if m1+m2+m3+m4 != 0:
        return False
    kmin = max(abs(j1-j2), abs(j3-j4))
    kmax = min(j1+j2, j3+j4)
    M = m1+m2
    for k in range(kmin, kmax+1):
        if cg_nonzero(j1,m1,j2,m2,k,M) and cg_nonzero(j3,m3,j4,m4,k,-M):
            return True
    return False


def source_pattern_valid():
    if not all(source_spin((0,b)) == 5 for b in range(1,5)):
        return False
    if not all(source_spin((a,b)) == 2 for a in range(1,5) for b in range(a+1,5)):
        return False
    for v in VERTICES:
        js = [source_spin(e) for e in EDGES if v in e]
        tjs = [2*j for j in js]
        if max(tjs) > sum(tjs)-max(tjs) or sum(tjs) % 2:
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', type=int, required=True)
    ap.add_argument('--cluster-size', type=int, choices=(3,4), required=True)
    args = ap.parse_args()
    profile = (args.index, args.cluster_size)
    frozen_profile = profile in SURVIVORS
    sigma,kappa = sector(args.index)
    boosted = set(range(1,args.cluster_size+1))
    crossing = [e for e in EDGES if ((e[0] in boosted) != (e[1] in boosted))]
    fixed = {}
    alphas = []
    controls = source_pattern_valid() and frozen_profile
    for e in crossing:
        j = source_spin(e)
        sign = kappa[e]
        m = -j if sign == 1 else j
        fixed[e] = m
        controls &= (m in m_values(j))
        alphas.append(1 + abs(j + sign*m))
    expected_tail_lambda = 2*args.cluster_size - sum(alphas)
    controls &= expected_tail_lambda >= 0
    free_edges = [e for e in EDGES if e not in fixed]

    supported_A = []
    supported_B = []
    pairing_A = (0,1,2,3)
    pairing_B = (0,2,1,3)

    grids = [m_values(source_spin(e)) for e in free_edges]
    assignments_tested = 0
    for vals in itertools.product(*grids):
        assignments_tested += 1
        em = dict(fixed)
        em.update(dict(zip(free_edges, vals)))
        key = tuple(vals)
        okA = True
        okB = True
        for v in VERTICES:
            inc = sorted(e for e in EDGES if v in e)
            js = [source_spin(e) for e in inc]
            ms = [outgoing(e,v,em[e]) for e in inc]
            okA &= projector_support(js,ms,pairing_A)
            okB &= projector_support(js,ms,pairing_B)
            if not okA and not okB:
                break
        if okA:
            supported_A.append(key)
        if okB:
            supported_B.append(key)

    setA, setB = set(supported_A), set(supported_B)
    pairing_agreement = setA == setB
    controls &= pairing_agreement
    survives = bool(setA)
    if not controls:
        classification = 'CONTROL_INVALID'
    elif survives:
        classification = 'SOURCE_BACKED_PROFILE_SURVIVES_EXACT_INVARIANT_PROJECTOR'
    else:
        classification = 'SOURCE_BACKED_PROFILE_EXCLUDED_BY_EXACT_INVARIANT_PROJECTOR'

    out = {
        'iteration': 438,
        'sector_index': args.index,
        'cluster_size': args.cluster_size,
        'frozen_iter437_survivor': frozen_profile,
        'source_pattern_valid': source_pattern_valid(),
        'crossing_edges': [list(e) for e in crossing],
        'free_edges': [list(e) for e in free_edges],
        'assignments_tested': assignments_tested,
        'supported_assignment_count_pairing_A': len(setA),
        'supported_assignment_count_pairing_B': len(setB),
        'pairing_support_sets_agree_exactly': pairing_agreement,
        'example_supported_free_m': list(next(iter(setA))) if setA else None,
        'expected_tail_lambda': expected_tail_lambda,
        'iter435_slow_obstruction_reproduced': expected_tail_lambda >= 0,
        'controls_valid': bool(controls),
        'classification': classification,
        'scope_guard': ('Exact discrete SU(2) invariant-projector/global-magnetic support under one frozen published '
                        'Lorentzian boundary-spin pattern only; not full Haar/angular contraction, causal-vertex '
                        'divergence/finiteness, cutoff removal, family promotion, or terminal D7.'),
        'd2': 'NOT_CLOSED_COVERAGE_AND_OBJECTS',
        'd4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7_s2': 'NOT_CLOSED', 'd7_s3': 'NOT_CLOSED', 'd7_s4': 'PARTIAL_GLOBAL_NOT_CLOSED',
        'd7': 'NOT_CLOSED / NOT_YET_AUTHORIZED',
        'candidate_gravity_authorized': False,
    }
    os.makedirs('build/lqg-iter438', exist_ok=True)
    path = f'build/lqg-iter438/sector_{args.index}_s{args.cluster_size}.json'
    with open(path,'w') as f:
        json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not controls:
        raise SystemExit(2)

if __name__ == '__main__':
    main()
