#!/usr/bin/env python3
import itertools, json, math, pathlib
p=json.load(open('benchmarks/lqg_iter311_partial_diagonal_subdivergence_census.json'))
rows=[]; ok=True
for s in range(2,6):
    internal=math.comb(s,2)
    singular=2*internal
    dim=3*(s-1)
    omega=singular-dim
    count=math.comb(5,s)
    expected={2:-1,3:0,4:3,5:8}[s]
    ok &= omega==expected
    rows.append({'s':s,'subset_count':count,'internal_edges':internal,'singular_power':singular,'relative_dimension':dim,'omega':omega,'status':'safe' if omega<0 else ('marginal' if omega==0 else 'divergent')})
ok &= p['prospectively_frozen_claims']['subset_degree_formula']=='omega(s)=(s-1)(s-3)'
out={'probe':'subset_degree_census','pass':bool(ok),'iteration':311,'rows':rows}
pathlib.Path('build/lqg-iter311').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter311/subset_degree_census.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
