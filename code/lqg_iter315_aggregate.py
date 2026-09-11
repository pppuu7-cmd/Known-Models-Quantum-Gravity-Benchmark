#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter315-results')
files=sorted(root.glob('triangle_*.json'))
rows=[json.loads(f.read_text()) for f in files]
expected={'012','013','014','023','024','034','123','124','134','234'}
seen={r.get('triangle') for r in rows}
if seen!=expected or len(rows)!=10 or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'triangle barrier failed: seen={seen}, expected={expected}')
if not all(r['nonzero_unnormalized_components']==128 and r['normalized_squared_tensor_norm']=='1/8' and r['distinct_Cplus_external_branch_patterns']==16 for r in rows):
    raise SystemExit('nonuniform triangle residue result')
contract=json.load(open('benchmarks/lqg_iter315_k3_contracted_residue_tensor.json'))
out={
 'iteration':315,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
 'triangles':sorted(seen),'triangle_jobs':len(rows),
 'nonzero_components_each':128,'positive_components_each':64,'negative_components_each':64,
 'normalized_component_magnitude':'1/32','normalized_squared_tensor_norm_each':'1/8',
 'distinct_Cplus_external_branch_patterns_each':16,
 'fixed_sector_internal_K3_residue_tensor_nonzero_all_10':True,
 'formal_Cplus_duplicate_monomial_cancellation_forced':False,
 'explicit_physical_external_Toller_evaluation_nonzero_proven':False,
 'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
 'next_required_object':'evaluate or constrain the seven external Toller matrices on an explicit physical configuration and test the C+ formal K3 residue there; in parallel audit K4 full branch-polynomial cancellation'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'; pathlib.Path('build/lqg-iter315-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest(); pathlib.Path('build/lqg-iter315-summary.sha256').write_text(digest+'  lqg-iter315-summary.json\n')
