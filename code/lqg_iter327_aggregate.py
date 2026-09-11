#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('build/lqg-iter327-results')
files=sorted(root.glob('size_*.json'))
if len(files)!=3:
    raise SystemExit(f'expected 3 artifacts, got {len(files)}')
rows=[json.loads(p.read_text()) for p in files]
assert sorted(r['stratum_size'] for r in rows)==[3,4,5]
assert all(r['single_transitive_S5_orbit'] for r in rows)
weighted=sum(r['iter323_weighted_dimension_before_global_S5_linkage'] for r in rows)
linked=sum(r['strongest_pure_global_S5_relabeling_linked_dimension'] for r in rows)
assert weighted==48
assert linked==31
assert linked>1

summary={
    'iteration':327,
    'iter323_weighted_scalar_normal_sector_dimension':weighted,
    'after_strongest_pure_global_S5_same_size_linkage_dimension':linked,
    'breakdown':{str(r['stratum_size']):r['strongest_pure_global_S5_relabeling_linked_dimension'] for r in rows},
    'reduction_factor':weighted/linked,
    'uniqueness_from_global_S5_relabeling_alone':False,
    'classification':'Exact S5 orbit-stabilizer bookkeeping reduces the Iter323 weighted scalar normal-sector bookkeeping from 48 to 31 by tying symmetry-related same-size strata. A multidimensional ambiguity remains, so global relabeling symmetry alone does not select a unique extension.',
    'implication':'Any unique causal-spinfoam joint extension would still require additional forest/gluing/normalization/Ward or fuller Lorentz-tensor conditions beyond pure vertex relabeling.',
    'scope_guard':'31 is a conditional symmetry-linked scalar normal-sector dimension, not a number of physical counterterms. Additional valid constraints may reduce it further. This is not a terminal LQG FAIL and does not authorize D7/NEW_REQUIRED.'
}
out=Path('build/lqg-iter327-summary.json')
out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))
