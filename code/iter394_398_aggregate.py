#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter394-398-results')
objs=[]
for p in root.rglob('*.json'):
 try: objs.append(json.loads(p.read_text()))
 except Exception: pass
iho=[o for o in objs if o.get('mode')=='iho_payload']
nl=[o for o in objs if o.get('mode')=='nonlocal_theorem_scope']
rq=[o for o in objs if o.get('mode')=='rqcp_holdout']
coverage=(len(iho)==10 and len(nl)==4 and len(rq)==9)
all_pass=coverage and all(o.get('pass') for o in iho+nl+rq)
full=sum(bool(o.get('full_slot_satisfied')) for o in iho)
partial=len(iho)-full
analytic=next((o for o in nl if o.get('case')=='analytic_eom_tree'),{})
rq_summary={}
for obs in ('G','gap','prod'):
 rows=sorted([o for o in rq if o.get('observable')==obs],key=lambda x:x['train_max'])
 rq_summary[obs]={
  'train_maxima':[o['train_max'] for o in rows],
  'targets':[o['target_cutoff'] for o in rows],
  'worst_relative_holdout_error_across_windows':max((o['worst_relative_holdout_error'] for o in rows),default=None),
  'last_window_worst_relative_holdout_error':rows[-1]['worst_relative_holdout_error'] if rows else None,
  'last_window_model_prediction_disagreement':rows[-1]['relative_model_prediction_disagreement'] if rows else None
 }
out={
 'iteration_bundle':'394-398','coverage_complete':coverage,'all_jobs_pass':all_pass,
 'iho_payload_jobs':len(iho),'iho_minimum_payload_full_slots':full,'iho_minimum_payload_partial_or_open_slots':partial,
 'iho_full_slots':sorted([o['field'] for o in iho if o.get('full_slot_satisfied')]),
 'iho_partial_open_slots':sorted([{'field':o['field'],'status':o['status']} for o in iho if not o.get('full_slot_satisfied')],key=lambda x:x['field']),
 'iho_branch_map_v2_required':True,'iho_family_terminal':False,
 'nonlocal_scope_jobs':len(nl),'nonlocal_analytic_eom_tree_residual':analytic.get('comparator_residual'),
 'nonlocal_tree_subfamily_terminal_candidate':analytic.get('subfamily_terminal_candidate',False),
 'nonlocal_family_terminal':False,
 'rqcp_holdout_jobs':len(rq),'rqcp_holdout_summary':rq_summary,
 'D2':'NOT_CLOSED_COVERAGE_AND_OBJECTS','D4':'PARTIAL_GLOBAL_NOT_CLOSED','D7':'NOT_CLOSED_NOT_YET_AUTHORIZED','candidate_gravity_activation':False,
 'classification':'PASS_SOURCE_AWARE_PARALLEL_CLOSURE_WAVE__IHO_BRANCH_PAYLOAD_SHARPENED__NONLOCAL_TREE_COMPARATOR_QUOTIENT_CLOSED_IN_THEOREM_SUBFAMILY__RQCP_HOLDOUT_CONVERGENCE_TESTED__GLOBAL_GATES_REMAIN_OPEN' if all_pass else 'INCOMPLETE_OR_FAILED_SOURCE_AWARE_PARALLEL_CLOSURE_WAVE',
 'scientific_boundary':'Theorem-scoped nonlocal tree equivalence is not family-level nonlocal-QG equivalence; source-defined IHO/DQFT unitarity is not an independent KMQGB all-loop proof; finite RQCP holdouts are not a cutoff-removal theorem.'
}
Path('iter394-398-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
if not all_pass: raise SystemExit(2)
