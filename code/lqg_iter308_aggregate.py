#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter308-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'causal_support_factor','unrestricted_support_cancellation','unit_causal_sum_witness','nonnegative_weight_guard','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter308_causal_support_pole_cancellation.json'))
out={
  'iteration':308,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),
  'causal_support':'16 inequivalent sigma-induced sectors (1+5+10)',
  'leading_factor_per_causal_sector':1,
  'unit_weight_causal_leading_factor':16,
  'unit_weight_causal_witness_coefficient':'-2/[81*(1+gamma^2)^10] * delta^-20',
  'nontrivial_nonnegative_causal_weights_cancel':False,
  'unrestricted_support':'1024 independent wedge-sign sectors',
  'unrestricted_leading_factor_counts':{'positive':512,'negative':512},
  'unrestricted_unit_weight_leading_factor_sum':0,
  'causal_support_restores_eprl_local_pole_cancellation':False,
  'distributional_or_regularized_causal_sum_nonexistence_proven':False,
  'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
  'next_required_object':'source-grounded signed/complex causal weighting or local distributional/renormalized prescription compatible with causal interpretation, gluing, normalization and cutoff control; otherwise D7_S2 causal endpoint remains blocked by explicit local absolute nonintegrability'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter308-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter308-summary.sha256').write_text(digest+'  lqg-iter308-summary.json\n')
