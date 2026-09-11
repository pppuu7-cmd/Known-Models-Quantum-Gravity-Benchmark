#!/usr/bin/env python3
import argparse, itertools, json, math
from pathlib import Path

V = tuple(range(5))
PERMS = list(itertools.permutations(V))
assert len(PERMS) == 120

def fs(s):
    return frozenset(int(c) for c in s)

def act_subset(S,p):
    return frozenset(p[i] for i in S)

def canon_forest(F):
    return tuple(sorted((tuple(sorted(S)) for S in F), key=lambda x:(len(x),x)))

def canon_pair(P):
    return tuple(sorted((tuple(sorted(S)) for S in P), key=lambda x:(len(x),x)))

def encode(obj):
    return '|'.join(''.join(map(str,S)) for S in obj) if obj else 'EMPTY'

CASES = {
    'forest_empty': ('forest', tuple(), 1, 120),
    'forest_single_k3': ('forest', (fs('012'),), 10, 12),
    'forest_single_k4': ('forest', (fs('0123'),), 5, 24),
    'forest_single_k5': ('forest', (fs('01234'),), 1, 120),
    'forest_pair_k3_k4': ('forest', (fs('012'),fs('0123')), 20, 6),
    'forest_pair_k3_k5': ('forest', (fs('012'),fs('01234')), 10, 12),
    'forest_pair_k4_k5': ('forest', (fs('0123'),fs('01234')), 5, 24),
    'forest_triple_k3_k4_k5': ('forest', (fs('012'),fs('0123'),fs('01234')), 20, 6),
    'overlap_k3_k3_i1': ('overlap', (fs('012'),fs('034')), 15, 8),
    'overlap_k3_k3_i2': ('overlap', (fs('012'),fs('013')), 30, 4),
    'overlap_k3_k4_i2': ('overlap', (fs('012'),fs('0134')), 30, 4),
    'overlap_k4_k4_i3': ('overlap', (fs('0123'),fs('0124')), 10, 12),
}

p=argparse.ArgumentParser()
p.add_argument('--case',required=True,choices=sorted(CASES))
a=p.parse_args()
kind, rep, expected_orbit, expected_stab = CASES[a.case]
canon = canon_forest if kind=='forest' else canon_pair
rep_canon = canon(rep)
orbit=set()
stab=0
for perm in PERMS:
    moved=canon(tuple(act_subset(S,perm) for S in rep))
    orbit.add(moved)
    if moved==rep_canon:
        stab += 1
assert len(orbit)==expected_orbit, (a.case,len(orbit),expected_orbit)
assert stab==expected_stab, (a.case,stab,expected_stab)
assert len(orbit)*stab==math.factorial(5)

out={
 'iteration':321,
 'case':a.case,
 'kind':kind,
 'representative':encode(rep_canon),
 'orbit_size':len(orbit),
 'stabilizer_order':stab,
 'orbit_stabilizer_product':len(orbit)*stab,
 'members':sorted(encode(x) for x in orbit),
 'classification':'exact S5 orbit/stabilizer census',
 'scope_guard':'This quotients only combinatorial support/forest cases under vertex relabeling. It does not count independent physical counterterms or prove extension uniqueness.'
}
path=Path('build/lqg-iter321')/f'{a.case}.json'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
