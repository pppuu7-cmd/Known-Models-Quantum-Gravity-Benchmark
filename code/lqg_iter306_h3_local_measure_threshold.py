#!/usr/bin/env python3
import json, pathlib

p=json.load(open('benchmarks/lqg_iter306_toller_local_power_count.json'))
# On H_+ the local radial volume is r^(3-1) dr. A component behaving as r^-q
# is locally integrable on one relative boost variable iff q < 3.
examples=[
 {'j':0.5,'q':2,'degree_q_minus_3':-1,'status':'single-edge locally integrable'},
 {'j':1.0,'q':3,'degree_q_minus_3':0,'status':'single-edge logarithmic/marginal'},
 {'j':1.5,'q':4,'degree_q_minus_3':1,'status':'single-edge superficial divergence risk'}
]
ok=(p['prospectively_frozen_claims']['noncompact_coset_local_dimension']==3 and
    p['prospectively_frozen_claims']['source_explicit_j_half_branch_has_beta_minus_2_singularity'] and
    p['prospectively_frozen_claims']['source_explicit_j_one_branch_has_beta_minus_3_singularity'])
out={'probe':'h3_local_measure_threshold','pass':bool(ok),'iteration':306,
     'local_noncompact_dimension':3,'criterion':'q<3 for one radial H3 relative coordinate',
     'examples':examples}
pathlib.Path('build/lqg-iter306').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter306/h3_local_measure_threshold.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
