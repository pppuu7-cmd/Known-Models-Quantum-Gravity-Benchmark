#!/usr/bin/env python3
import hashlib, json, pathlib
kroot=pathlib.Path('build/lqg-iter316-k4-results'); groot=pathlib.Path('build/lqg-iter316-guard-results')
krows=[json.loads(p.read_text()) for p in sorted(kroot.glob('k4_*.json'))]
grows=[json.loads(p.read_text()) for p in sorted(groot.glob('*.json'))]
expected_k4={'0123','0124','0134','0234','1234'}; seen={r.get('subset') for r in krows}
expected_guards={'star_support','formal_factorization','scope_guard'}; gseen={r.get('probe') for r in grows}
if seen!=expected_k4 or len(krows)!=5 or not all(r.get('pass') is True for r in krows): raise SystemExit(f'K4 barrier failed: {seen}')
if gseen!=expected_guards or not all(r.get('pass') is True for r in grows): raise SystemExit(f'guard barrier failed: {gseen}')
if not all(r['nonzero_unnormalized_components']==16 and r['distinct_Cplus_external_star_patterns']==16 for r in krows): raise SystemExit('K4 tensor invariant mismatch')
contract=json.load(open('benchmarks/lqg_iter316_k4_full_branch_residue.json'))
out={'iteration':316,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
     'k4_subsets':sorted(seen),'k4_jobs':len(krows),'guard_jobs':len(grows),
     'nonzero_components_each':16,
     'normalized_component_magnitudes':{r['subset']:r['normalized_component_magnitude'] for r in krows},
     'normalized_squared_norms':{r['subset']:r['normalized_squared_tensor_norm'] for r in krows},
     'Cplus_external_star_patterns_each':16,
     'Cplus_formal_K4_branch_polynomial':'tensor_product_four(Tplus-Tminus)',
     'formal_monomial_count':16,'unit_scalar_specialization':0,
     'zero_scalar_sum_implies_full_residue_zero':False,
     'explicit_physical_external_Toller_evaluation_nonzero_proven':False,
     'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
     'next_required_object':'explicit physical evaluation or source theorem showing Tplus-Tminus is nonzero on admissible external edges, then forest-compatible extensions for K3/K4/K5 strata'}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'; pathlib.Path('build/lqg-iter316-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest(); pathlib.Path('build/lqg-iter316-summary.sha256').write_text(digest+'  lqg-iter316-summary.json\n')
