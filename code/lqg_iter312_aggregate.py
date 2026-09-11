#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter312-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'subset_sign_identity','unit_sum_census','class_weight_coefficients','weight_solution_guard','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter312_partial_diagonal_causal_sign_cancellation.json'))
out={
  'iteration':312,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),
  'causal_sector_count':16,'class_multiplicities':[1,5,10],
  'K3_unit_sum':'-16 on each of 10 triangles','K4_unit_sum':'0 on each of 5 K4 subsets','K5_unit_sum':16,
  'class_weight_forms':{'K3':'-(w0+5w1+10w2)','K4':'w0-3w1+2w2','K5':'w0+5w1+10w2'},
  'nontrivial_nonnegative_class_weights_cancel_K3_or_K5':False,
  'signed_scalar_null_direction':[-5,-1,1],
  'signed_scalar_null_direction_source_grounded':False,
  'full_tensor_residue_cancellation_under_signed_direction_proven':False,
  'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
  'next_required_object':'source-level causal-structure weighting audit plus exact contracted K3 residue witnesses; then decide whether the signed (-5,-1,+1) loophole is physically admissible and whether it cancels full distributions rather than only scalar branch signs'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter312-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter312-summary.sha256').write_text(digest+'  lqg-iter312-summary.json\n')
