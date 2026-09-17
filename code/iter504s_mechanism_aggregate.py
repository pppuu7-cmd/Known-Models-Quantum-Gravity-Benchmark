#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

INVALID='ITER504S_INVALID'

def one(root):
 ps=sorted(Path(root).rglob('*.json'))
 if len(ps)!=1: raise SystemExit(f'expected one json under {root}, got {len(ps)}')
 raw=ps[0].read_bytes(); return json.loads(raw),hashlib.sha256(raw).hexdigest()

def rho_map(rows): return {str(x['rho']):x for x in rows}

def projection(o):
 out={'classification':o.get('classification'),'threshold':o.get('threshold'),'robust_floor':o.get('robust_floor'),'center_D_is_control_only':o.get('center_D_is_control_only'),'cases':[]}
 for c in o.get('cases',[]):
  z={'root_box':c.get('root_box'),'location':c.get('location'),'amp_q':c.get('amp_q'),'rho':[],'per_R':{}}
  F=rho_map(c['full_D']['per_rho']);C=rho_map(c['center_D_sensitivity']['per_rho']);FF=rho_map(c['full_D']['fixed_channel']);CF=rho_map(c['center_D_sensitivity']['fixed_channel'])
  for rk in ('0.35','0.9','1.6','2.7'):
   f=F[rk];cc=C[rk];ff=FF[rk];cf=CF[rk]
   z['rho'].append({'rho':rk,'full_within':f['within_tolerance'],'full_gt_tol':float(f['drift_upper'])>0.05,'center_within':cc['within_tolerance'],'center_gt_tol':float(cc['drift_upper'])>0.05,
                    'full_candidates':ff['candidate_union'],'full_complete':ff['competition_test_complete'],'full_all_fixed_within':ff['all_candidate_fixed_channels_within_tolerance'],
                    'center_candidates':cf['candidate_union'],'center_complete':cf['competition_test_complete'],'center_all_fixed_within':cf['all_candidate_fixed_channels_within_tolerance']})
  for t in ('full_D','center_D_sensitivity'):
   z['per_R'][t]=[]
   for rr in c[t]['per_R']:
    z['per_R'][t].append({'R':rr['R'],'rho':[{'rho':str(q['rho']),'possible_indices':q['possible_indices'],'strict_unique_max':q['strict_unique_max']} for q in rr['rho']]})
  out['cases'].append(z)
 return out

def maxdiff(A,B):
 diffs={'full_drift':0.0,'center_drift':0.0,'full_S':0.0,'center_S':0.0}
 Bc={(c['root_box'],c['location'],c['amp_q']):c for c in B.get('cases',[])}
 for a in A.get('cases',[]):
  b=Bc.get((a['root_box'],a['location'],a['amp_q']))
  if not b: continue
  for t,pfx in [('full_D','full'),('center_D_sensitivity','center')]:
   ar=rho_map(a[t]['per_rho']); br=rho_map(b[t]['per_rho'])
   for k in ar:
    if k not in br: continue
    diffs[pfx+'_drift']=max(diffs[pfx+'_drift'],abs(float(ar[k]['drift_upper'])-float(br[k]['drift_upper'])))
    diffs[pfx+'_S']=max(diffs[pfx+'_S'],abs(float(ar[k]['S_lower'])-float(br[k]['S_lower'])))
 return diffs

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--a',required=True);ap.add_argument('--b',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
 A,Ah=one(a.a);B,Bh=one(a.b)
 pa=projection(A);pb=projection(B); discrete=pa==pb
 same_cls=A.get('classification')==B.get('classification') and A.get('classification')!=INVALID
 errors=[]
 if A.get('errors'):errors.append('A_invalid')
 if B.get('errors'):errors.append('B_invalid')
 if not discrete:errors.append('discrete_projection_disagreement')
 if not same_cls:errors.append('classification_disagreement')
 cls=A.get('classification') if not errors else INVALID
 out={'gate':A.get('gate'),'preregistration_commit':A.get('preregistration_commit'),'classification':cls,'errors':errors,
      'lane_a_json_sha256':Ah,'lane_b_json_sha256':Bh,'byte_identical':Ah==Bh,'discrete_projection_identical':discrete,
      'max_numeric_environment_difference':maxdiff(A,B),'threshold':A.get('threshold'),'robust_floor':A.get('robust_floor'),
      'root_location_count':A.get('root_location_count'),'case_count':A.get('case_count'),'endpoint_full_D_violation_count':A.get('endpoint_full_D_violation_count'),'center_D_violation_count':A.get('center_D_violation_count'),
      'maximum_full_D_drift_upper':A.get('maximum_full_D_drift_upper'),'maximum_center_D_drift_upper':A.get('maximum_center_D_drift_upper'),'minimum_full_D_S_lower':A.get('minimum_full_D_S_lower'),'maximum_possible_count':A.get('maximum_possible_count'),'strict_unique_max_certificate_count':A.get('strict_unique_max_certificate_count'),
      'center_D_is_control_only':True,'claim_ceiling':'Iter504S nine-point mechanism diagnostic only; cross-environment consumer compares frozen discrete decisions and identities'}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['aggregate_sha256']=hashlib.sha256(payload).hexdigest()
 p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
