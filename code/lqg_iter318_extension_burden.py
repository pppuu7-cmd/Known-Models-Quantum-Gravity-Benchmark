#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--subset', required=True)
a = p.parse_args()
S = tuple(sorted(int(x) for x in a.subset))
if len(set(S)) != len(S) or any(x < 0 or x > 4 for x in S):
    raise SystemExit('subset must contain distinct vertices in 0..4')
s = len(S)
if s not in (3,4,5):
    raise SystemExit('Iter318 covers non-safe K3/K4/K5 strata only')
internal_edges = math.comb(s, 2)
sd = 2 * internal_edges
d = 3 * (s - 1)
omega = sd - d
if omega < 0:
    raw_slots = 0
else:
    raw_slots = math.comb(d + omega, omega)
expected = {3:(6,6,0,1), 4:(12,9,3,220), 5:(20,12,8,125970)}[s]
assert (sd,d,omega,raw_slots) == expected
out = {
    'iteration': 318,
    'subset': ''.join(map(str,S)),
    'size': s,
    'internal_edges': internal_edges,
    'scaling_degree': sd,
    'relative_dimension': d,
    'superficial_degree': omega,
    'raw_local_derivative_multiindices_leq_omega': raw_slots,
    'extension_status': 'nonunique_same_scaling_degree_extension_requires_local_data',
    'prior_nonzero_witness': 'Iter317' if s in (3,4) else 'Iter307',
    'scope_guard': 'raw multiindex bookkeeping before covariance, permutation/orientation, gluing, overlap consistency, and normalization reductions; not a count of independent physical parameters'
}
path = Path('build/lqg-iter318') / f"subset_{out['subset']}.json"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps(out, sort_keys=True))
