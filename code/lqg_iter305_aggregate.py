#!/usr/bin/env python3
import hashlib, json, pathlib

root=pathlib.Path('build/lqg-iter305-results')
files=sorted(root.glob('*.json'))
expected={'gamma_simple_decay_floor','k5_kaminski_margin','physical_rho_pole_guard','local_identity_singularity','scope_guard'}
rows=[json.loads(p.read_text()) for p in files]
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter305_toller_tail_local_integrability_split.json'))
out={
  'iteration':305,
  'family':'LQG_SPINFOAM',
  'classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),
  'radial_tail_subproblem':'CLOSED_SCOPED',
  'gamma_simple_worst_tail_exponent':'1',
  'kaminski_k5_comparison_exponent':'19/20',
  'tail_exponent_margin':'1/20',
  'positive_real_gamma_simple_rho_hits_toller_pole':False,
  'explicit_local_identity_branch_singularity':'beta^-2 witness exists',
  'local_identity_neighborhood_integrability':'OPEN',
  'causal_vertex_finiteness_proven':False,
  'causal_vertex_divergence_proven':False,
  'lambda_f_weighted_causal_stack_finiteness_normalization_cutoff_control_proven':False,
  'same_realization_uv_to_causal_regge_gr_transport_proven':False,
  'family_terminal':False,
  'd7_authorized':False,
  'terminal_count':'1/15',
  'next_required_object':'local multi-group identity-neighborhood singularity power count/cancellation theorem or direct finite normalized fixed-causal vertex certificate; then lambda_f-weighted complete-stack normalization/cutoff control; then same-realization UV-to-causal-Regge/GR transport'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
path=pathlib.Path('build/lqg-iter305-summary.json'); path.write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter305-summary.sha256').write_text(digest+'  lqg-iter305-summary.json\n')
