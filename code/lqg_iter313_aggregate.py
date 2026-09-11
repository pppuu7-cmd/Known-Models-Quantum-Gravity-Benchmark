#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter313-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'global_flip_support','source_decomposition_count','cplus_partial_sign_sum','global_flip_normalization','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows): raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter313_source_cplus_unit_sum.json'))
out={'iteration':313,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
     'independent_probes':sorted(seen),'raw_sigma_assignments':32,'distinct_Cplus_patterns':16,'global_flip_multiplicity':2,
     'distinct_Cminus_patterns':16,'Cplus_Cminus_overlap':0,'noncausal_patterns':992,
     'source_Cplus_coefficients':'unit','signed_class_weight_loophole_in_source':False,
     'Cplus_minspin_leading_sign_sums':{'K3':-16,'K4':0,'K5':16},
     'global_flip_normalization_affects_cancellation_pattern':False,
     'full_contracted_K3_residue_nonzero_proven':False,
     'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
     'next_required_object':'exact contracted K3 residue witness and C+/C- combined support audit; then partial-diagonal extension/normalization conditions'}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'; pathlib.Path('build/lqg-iter313-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest(); pathlib.Path('build/lqg-iter313-summary.sha256').write_text(digest+'  lqg-iter313-summary.json\n')
