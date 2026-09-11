#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter314-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'cocausal_flip_rule','cminus_sign_sums','cplus_cminus_combined','noncausal_restoration','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter314_cplus_cminus_noncausal_cancellation.json'))
out={
  'iteration':314,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),
  'support_counts':{'Cplus':16,'Cminus':16,'noncausal':992,'unrestricted':1024},
  'Cminus_minspin_leading_sign_sums':{'K3':16,'K4':0,'K5':16},
  'Cplus_plus_Cminus_sums':{'K3':0,'K4':0,'K5':32},
  'noncausal_sums':{'K3':0,'K4':0,'K5':-32},
  'unrestricted_EPRL_sums':{'K3':0,'K4':0,'K5':0},
  'noncausal_sector_required_for_full_K5_scalar_sign_cancellation':True,
  'Cplus_plus_Cminus_restores_full_K5_cancellation':False,
  'full_tensor_residue_cancellation_proven':False,
  'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
  'next_required_object':'exact contracted K3 residue witnesses and total-K5 residue extension audit for the source C+ and C++C- definitions; then a forest-compatible renormalization/normalization scheme or explicit obstruction'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter314-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter314-summary.sha256').write_text(digest+'  lqg-iter314-summary.json\n')
