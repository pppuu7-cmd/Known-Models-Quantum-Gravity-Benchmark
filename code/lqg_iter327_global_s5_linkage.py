#!/usr/bin/env python3
import argparse, itertools, json, math
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--size',type=int,required=True,choices=(3,4,5))
a=p.parse_args()

V=tuple(range(5))
PERMS=tuple(itertools.permutations(V))
subsets=tuple(frozenset(c) for c in itertools.combinations(V,a.size))
base=subsets[0]

def image(s,p):
    return frozenset(p[i] for i in s)

orbit={image(base,p) for p in PERMS}
stabilizer=[p for p in PERMS if image(base,p)==base]
expected_orbit=math.comb(5,a.size)
expected_stabilizer=math.factorial(a.size)*math.factorial(5-a.size)
assert len(orbit)==expected_orbit==len(subsets)
assert len(stabilizer)==expected_stabilizer
assert len(orbit)*len(stabilizer)==math.factorial(5)
assert orbit==set(subsets)

# Exact scalar normal-sector invariant dimensions established independently in Iter323.
iter323_local_dim={3:1,4:2,5:28}[a.size]
raw_weighted=len(subsets)*iter323_local_dim
# Global S5 covariance can identify same-size copies along the single transitive orbit,
# so the strongest pure relabeling reduction leaves one copy of the local invariant space.
linked_dim=iter323_local_dim

out={
    'iteration':327,
    'stratum_size':a.size,
    'number_of_strata':len(subsets),
    'S5_order':len(PERMS),
    'stabilizer_order':len(stabilizer),
    'orbit_size':len(orbit),
    'single_transitive_S5_orbit':True,
    'iter323_local_Ss_x_SO3_scalar_normal_dimension':iter323_local_dim,
    'iter323_weighted_dimension_before_global_S5_linkage':raw_weighted,
    'strongest_pure_global_S5_relabeling_linked_dimension':linked_dim,
    'classification':'Global S5 relabeling ties all same-size strata because each size class is a single transitive orbit, but it cannot by itself reduce the internal local invariant dimension below the Iter323 value.',
    'scope_guard':'This is exact group-action bookkeeping in the scalar normal-sector proxy. Forest/gluing/Ward identities or fuller Lorentz/tensor constraints may reduce the space further; the linked dimension is not a count of physical renormalization constants.'
}
path=Path('build/lqg-iter327')/f'size_{a.size}.json'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
