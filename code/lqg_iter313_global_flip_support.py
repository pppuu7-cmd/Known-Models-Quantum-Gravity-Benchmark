#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter313_source_cplus_unit_sum.json'))
edges=list(itertools.combinations(range(5),2))
counts={}
for sig in itertools.product((-1,1),repeat=5):
    k=tuple(sig[a]*sig[b] for a,b in edges)
    counts[k]=counts.get(k,0)+1
multiplicities=sorted(set(counts.values()))
ok=(sum(counts.values())==32 and len(counts)==16 and multiplicities==[2] and
    p['prospectively_frozen_claims']['raw_sigma_assignment_count']==32 and
    p['prospectively_frozen_claims']['global_flip_multiplicity_per_cplus_wedge_pattern']==2 and
    p['prospectively_frozen_claims']['distinct_cplus_wedge_patterns']==16)
out={'probe':'global_flip_support','pass':bool(ok),'iteration':313,'raw_sigma_assignments':32,
     'distinct_wedge_patterns':len(counts),'multiplicity_set':multiplicities,
     'interpretation':'sigma and -sigma give the same ten wedge signs, so each distinct C+ pattern has exactly two raw representatives'}
pathlib.Path('build/lqg-iter313').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter313/global_flip_support.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
