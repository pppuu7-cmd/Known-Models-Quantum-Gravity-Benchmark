#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
INVALID='ITER504S_INVALID'

def one(root):
    ps=sorted(Path(root).rglob('*.json'))
    if len(ps)!=1:raise SystemExit(f'expected one json under {root}, got {len(ps)}')
    raw=ps[0].read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def fixed_projection(rr):
    return {'rho':str(rr['rho']),'candidate_union':rr['candidate_union'],'ineligible_candidates':rr['ineligible_candidates'],
            'competition_test_complete':rr['competition_test_complete'],'violating_channel_indices':rr['violating_channel_indices'],
            'all_within':rr['all_candidate_fixed_channel_drifts_within_tolerance']}
def projection(o):
    out={'classification':o.get('classification'),'threshold_exact':o.get('threshold_exact'),'robust_floor_exact':o.get('robust_floor_exact'),
         'transport':o.get('scientific_decision_transport'),'semantics':o.get('fixed_channel_competition_semantics'),'cases':[]}
    for c in o.get('cases',[]):
        z={'root_box':c['root_box'],'location':c['location'],'amp_q':c['amp_q'],'rho':[],'R':[]}
        for i in range(4):
            F=c['full_D']['per_rho'][i];C=c['center_D_sensitivity']['per_rho'][i];FF=c['full_D']['fixed_channel'][i];CF=c['center_D_sensitivity']['fixed_channel'][i]
            z['rho'].append({'rho':str(F['rho']),'full_floor':F['slope_floor_satisfied'],'full_drift_ok':F['drift_within_tolerance'],'full_within':F['within_tolerance'],
              'center_floor':C['slope_floor_satisfied'],'center_drift_ok':C['drift_within_tolerance'],'center_within':C['within_tolerance'],
              'full_fixed':fixed_projection(FF),'center_fixed':fixed_projection(CF),'mechanism':c['mechanism_flags'][i]})
        for t in ('full_D','center_D_sensitivity'):
            for rr in c[t]['per_R']:
                z['R'].append((t,rr['R'],[(str(q['rho']),q['possible_indices'],q['strict_unique_max']) for q in rr['rho']]))
        out['cases'].append(z)
    return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',required=True);ap.add_argument('--b',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
    A,Ah=one(a.a);B,Bh=one(a.b);pa=projection(A);pb=projection(B);errors=[]
    if A.get('errors'):errors.append('A_invalid')
    if B.get('errors'):errors.append('B_invalid')
    if pa!=pb:errors.append('exact_discrete_projection_disagreement')
    if A.get('classification')!=B.get('classification') or A.get('classification')==INVALID:errors.append('classification_disagreement')
    cls=A.get('classification') if not errors else INVALID
    out={'gate':A.get('gate'),'preregistration_commit':A.get('preregistration_commit'),'repair_preregistrations':A.get('repair_preregistrations'),
      'classification':cls,'errors':errors,'lane_a_json_sha256':Ah,'lane_b_json_sha256':Bh,'byte_identical':Ah==Bh,
      'exact_discrete_projection_identical':pa==pb,'threshold_exact':'1/20','robust_floor_exact':'1',
      'scientific_decision_transport':'exact_arb_booleans_float_bounds_display_only','fixed_channel_competition_semantics':'drift_only_exact_producer_booleans',
      'root_location_count':A.get('root_location_count'),'case_count':A.get('case_count'),'endpoint_full_D_violation_count':A.get('endpoint_full_D_violation_count'),
      'center_D_violation_count':A.get('center_D_violation_count'),'claim_ceiling':'Iter504S exact-decision cross-environment consumer only'}
    payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['aggregate_sha256']=hashlib.sha256(payload).hexdigest()
    p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
