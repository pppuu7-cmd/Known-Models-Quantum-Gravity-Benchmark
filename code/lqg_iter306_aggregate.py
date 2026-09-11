#!/usr/bin/env python3
import hashlib, json, pathlib

root=pathlib.Path('build/lqg-iter306-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'hypergeom_local_exponent','h3_local_measure_threshold','k5_subset_power_count','uniform_spin_threshold_map','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter306_toller_local_power_count.json'))
out={
  'iteration':306,
  'family':'LQG_SPINFOAM',
  'classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),
  'gamma_simple_local_candidate_power':'q=2j+1',
  'noncompact_local_dimension_per_independent_vertex':3,
  'minimal_spin_k5_subset_degrees':{'s2':-1,'s3':0,'s4':3,'s5':8},
  'component_level_power_count_risk_established':True,
  'full_intertwiner_contracted_leading_coefficient_nonzero_proven':False,
  'full_causal_vertex_divergence_proven':False,
  'full_causal_vertex_finiteness_proven':False,
  'family_terminal':False,
  'd7_authorized':False,
  'terminal_count':'1/15',
  'next_required_object':'compute the leading fixed-branch K5 tensor after SU(2)-invariant intertwiner/magnetic contraction and test whether the marginal/superficial singular terms cancel identically; only then classify local absolute integrability'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter306-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter306-summary.sha256').write_text(digest+'  lqg-iter306-summary.json\n')
