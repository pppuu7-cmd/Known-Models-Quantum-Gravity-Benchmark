#!/usr/bin/env python3
import json, pathlib, hashlib
root=pathlib.Path('build/lqg-iter304-results')
files=sorted(root.glob('*.json'))
expected={'source_theorem_scope','polynomial_bound_nonintegrability_witness','transfer_fail_closed_guard','scope_guard'}
rows=[json.loads(p.read_text()) for p in files]
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}')
contract=json.load(open('benchmarks/lqg_iter304_toller_finiteness_transfer.json'))
out={
 'iteration':304,
 'family':'LQG_SPINFOAM',
 'classification':contract['frozen_classification_target'],
 'independent_probes':sorted(seen),
 'standard_eprl_finiteness_theorem_exists':True,
 'toller_polynomially_bounded':True,
 'fixed_toller_branch_sl2c_representation':False,
 'automatic_standard_theorem_transfer_ready':False,
 'polynomial_boundedness_alone_sufficient_for_noncompact_integrability':False,
 'causal_vertex_finiteness_proven':False,
 'causal_vertex_divergence_proven':False,
 'lambda_f_weighted_causal_stack_finiteness_normalization_cutoff_control_proven':False,
 'same_realization_uv_to_causal_regge_gr_transport_proven':False,
 'family_terminal':False,
 'd7_authorized':False,
 'terminal_count':'1/15',
 'next_required_object':'explicit Toller-kernel integrability/decay bound or theorem extending the relevant 3-edge-connected EPRL integrability class; after vertex finiteness, lambda_f-weighted complete-stack normalization/cutoff control'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
path=pathlib.Path('build/lqg-iter304-summary.json'); path.write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter304-summary.sha256').write_text(digest+'  lqg-iter304-summary.json\n')
