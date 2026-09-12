#!/usr/bin/env python3
import json, math
from pathlib import Path

root=Path('iter389-393-results')
objs=[]
for p in root.rglob('*.json'):
    try: objs.append(json.loads(p.read_text()))
    except Exception: pass
rq=[o for o in objs if o.get('mode')=='rqcp_fit']
nl=[o for o in objs if o.get('mode')=='nonlocal_domain']
hd=[o for o in objs if o.get('mode')=='higher_derivative_branch']
cv=[o for o in objs if o.get('mode')=='coverage']
coverage=(len(rq)==12 and len(nl)==15 and len(hd)==1 and len(cv)==1)
passes=coverage and all(o.get('pass') for o in rq+nl+hd+cv)

rq_summary={}
for obs in ('G','gap','prod'):
    rows=sorted([o for o in rq if o['observable']==obs],key=lambda x:x['nmin'])
    late=[o for o in rows if o['nmin']>=14]
    vals=[]
    for o in late:
        vals += [o['power_model']['y_inf'],o['exponential_model']['y_inf']]
    if vals:
        mid=sum(vals)/len(vals)
        spread=(max(vals)-min(vals))/max(abs(mid),1e-30)
    else: spread=None
    rq_summary[obs]={
        'fit_windows':[o['nmin'] for o in rows],
        'late_model_relative_asymptote_envelope':spread,
        'last_value':rows[-1]['last_value'] if rows else None,
        'last_step_relative_change':rows[-1]['last_step_relative_change'] if rows else None,
    }

nonlocal_map={}
for o in sorted(nl,key=lambda x:(x['degree'],x['zmax'])):
    nonlocal_map[f"n{o['degree']}_z{o['zmax']}"]={
        'max_relative_error':o['max_relative_error'],
        'first_z_gt_1e-3':o['first_z_relative_error_gt_1e-3'],
        'first_z_gt_1e-2':o['first_z_relative_error_gt_1e-2']
    }

branch_reopen=(len(hd)==1 and hd[0].get('classification')=='BRANCH_MAP_REOPEN_REQUIRED_FOR_MATERIAL_CLASSIFICATION')
classification=(
    'PASS_PARALLEL_TERMINALIZATION_WAVE__RQCP_CUTOFF_EXTRAPOLATION_AND_NONLOCAL_FINITE_DOMAIN_MAP_SHARPENED__HIGHER_DERIVATIVE_BRANCH_MAP_REOPEN_IDENTIFIED__D2_D4_REMAIN_OPEN'
    if passes else 'INCOMPLETE_OR_FAILED_PARALLEL_TERMINALIZATION_WAVE'
)
out={
    'iteration_bundle':'389-393',
    'rqcp_fit_jobs':len(rq),'nonlocal_domain_jobs':len(nl),'higher_derivative_branch_jobs':len(hd),'coverage_jobs':len(cv),
    'coverage_complete':coverage,'all_jobs_pass':passes,'classification':classification,
    'rqcp_cutoff_extrapolation_summary':rq_summary,
    'nonlocal_finite_domain_comparator_map':nonlocal_map,
    'higher_derivative_branch_map_reopen_required_for_classification':branch_reopen,
    'higher_derivative_missing_payload_items':hd[0].get('missing_payload_items') if hd else None,
    'tier1_total':cv[0].get('tier1_total') if cv else None,
    'tier1_terminal':cv[0].get('terminal_count') if cv else None,
    'tier1_nonterminal':cv[0].get('nonterminal_count') if cv else None,
    'D2':'NOT_CLOSED_COVERAGE_AND_OBJECTS','D4':'PARTIAL_GLOBAL_NOT_CLOSED','D7':'NOT_CLOSED_NOT_YET_AUTHORIZED',
    'candidate_gravity_activation':False,
    'scientific_boundary':'This wave sharpens two compute-eligible closure axes and detects a branch-map classification gap. It does not convert finite extrapolation into a theorem, functional approximation into a physical amplitude certificate, or a newly classified branch into a family verdict.'
}
Path('iter389-393-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
if not passes: raise SystemExit(2)
