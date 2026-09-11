#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter309_distribution_transversality.json'))
c=p['prospectively_frozen_claims']
ok=(c['k5_wedge_count']==10 and c['gauge_fixed_noncompact_boost_dimension']==12 and
    c['all_identity_B_constraints_vanish_for_all_spinors'] and
    (not c['joint_multiwedge_epsilon_limit_explicitly_defined_by_eq4']))
out={'probe':'source_limit_scope','pass':bool(ok),'iteration':309,
     'source_structure':['Eq3: each Toller block is defined with epsilon->0+ spectral boundary value','Eq4: ten already-defined Toller blocks are multiplied in the vertex','Eq17/D1-D3: each coherent Toller block contains theta(B) plus derivatives of delta(B)'],
     'joint_ten_wedge_epsilon_limit_in_eq4':False,
     'interpretation':'the displayed vertex formula does not itself add a common multi-wedge limiting/extension prescription beyond the individual Toller definitions'}
pathlib.Path('build/lqg-iter309').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter309/source_limit_scope.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
