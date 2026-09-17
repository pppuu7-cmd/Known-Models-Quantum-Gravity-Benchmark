#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
GATE='ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION';PREREG='aa2b0256ce60d605574a18ec86c0bad5b5df1512';REPAIR_PREREG='adc7bfb9df77a90455cac1b0f0cb7255d80c44d5';INVALID='ITER504T_INVALID'
def load(p):raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def decision_projection(o):
 out=[]
 for r in o.get('roots',[]):
  k=r.get('root_box')
  for x in r.get('leaves',[]):
   out.append((k,x.get('amp_lower_q'),x.get('amp_upper_q'),x.get('depth'),x.get('certified'),tuple((float(q.get('rho')),q.get('slope_floor_satisfied'),q.get('drift_within_tolerance'),q.get('certified')) for q in x.get('per_rho',[])),tuple((q.get('R'),float(q.get('rho')),tuple(q.get('indices',[]))) for q in x.get('possible_max',[]))))
 return out
def main():
 p=argparse.ArgumentParser();p.add_argument('--a',required=True);p.add_argument('--b',required=True);p.add_argument('--out',required=True);a=p.parse_args();A,Ah=load(a.a);B,Bh=load(a.b);errs=[]
 for tag,o in (('a',A),('b',B)):
  if o.get('gate')!=GATE:errs.append(tag+':gate')
  if o.get('preregistration_commit')!=PREREG:errs.append(tag+':prereg')
  if o.get('repair_preregistration_commit')!=REPAIR_PREREG:errs.append(tag+':repair_prereg')
  if o.get('errors'):errs.append(tag+':errors')
  if o.get('threshold_exact')!='1/20' or o.get('robust_floor_exact')!='1':errs.append(tag+':exact_constants')
  if o.get('partition_identity_verified')!='exact_rational_dyadic_cells':errs.append(tag+':partition')
  if o.get('r_cohort_binding_implemented') is not True:errs.append(tag+':r_cohort_binding')
  if o.get('componentwise_parent_inclusion_control_implemented') is not True:errs.append(tag+':parent_inclusion_binding')
 same_cls=A.get('classification')==B.get('classification') and A.get('classification')!=INVALID
 cross=decision_projection(A)==decision_projection(B)
 if not same_cls:errs.append('classification_disagreement')
 if not cross:errs.append('scientific_projection_disagreement')
 cls=A.get('classification') if not errs else INVALID
 out={'gate':GATE,'preregistration_commit':PREREG,'repair_preregistration_commit':REPAIR_PREREG,'classification':cls,'errors':errs,'lane_a_sha256':Ah,'lane_b_sha256':Bh,'cross_environment_exact_decision_agreement':cross,'threshold_exact':'1/20','robust_floor_exact':'1','partition_identity_verified':'exact_rational_dyadic_cells','r_cohort_binding_implemented':not any('r_cohort' in x for x in errs),'componentwise_parent_inclusion_control_implemented':not any('parent_inclusion' in x for x in errs),'total_unresolved_leaves':A.get('total_unresolved_leaves') if not errs else None,'total_terminal_leaves':A.get('total_terminal_leaves') if not errs else None,'total_visited_nodes':A.get('total_visited_nodes') if not errs else None,'claim_ceiling':'Cross-environment Iter504T decision aggregate only'}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['aggregate_payload_sha256']=hashlib.sha256(payload).hexdigest();q=Path(a.out);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
