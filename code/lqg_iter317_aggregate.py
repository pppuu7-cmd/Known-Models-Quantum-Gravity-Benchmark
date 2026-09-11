#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter317-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('subset_*.json'))]
expected={'012','013','014','023','024','034','123','124','134','234','0123','0124','0134','0234','1234'}
seen={r.get('subset') for r in rows}
if seen!=expected or len(rows)!=15 or not all(r.get('pass') is True for r in rows): raise SystemExit(f'subset barrier failed: {seen}')
k3=[r for r in rows if r['subset_size']==3]; k4=[r for r in rows if r['subset_size']==4]
if not all(abs(Fraction(r['Cplus_prefactor_without_Cgamma10']))==Fraction(1,128) for r in k3): raise SystemExit('K3 prefactor mismatch')
if not all(abs(Fraction(r['Cplus_prefactor_without_Cgamma10']))==Fraction(1,72) for r in k4): raise SystemExit('K4 prefactor mismatch')
contract=json.load(open('benchmarks/lqg_iter317_nested_physical_residue_witness.json'))
out={'iteration':317,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
     'subset_jobs':15,'K3_jobs':10,'K4_jobs':5,
     'K3_scaling':'delta^-6 epsilon^-14','K3_abs_prefactor_without_Cgamma10':'1/128',
     'K4_scaling':'delta^-12 epsilon^-8','K4_abs_prefactor_without_Cgamma10':'1/72',
     'Cgamma':'2/(1+gamma^2)','finite_real_gamma_zero':False,
     'Cplus_nonzero_physical_nested_witness_all_15':True,
     'Cplus_plus_Cminus_prefactor_relation':'2*Cplus on the full two-scale leading term',
     'physical_external_evaluation_loophole':'CLOSED_FOR_CHOSEN_VALID_BOUNDARY_STATE_AND_ALL_15_K3_K4_STRATA',
     'global_distribution_extension_unique':False,'complete_stack_control_proven':False,
     'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
     'next_required_object':'construct or constrain a forest-compatible distributional extension on the simultaneously nonzero K3/K4/K5 strata and determine whether source symmetries/gluing/normalization fix the local counterterm ambiguities'}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'; pathlib.Path('build/lqg-iter317-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest(); pathlib.Path('build/lqg-iter317-summary.sha256').write_text(digest+'  lqg-iter317-summary.json\n')
