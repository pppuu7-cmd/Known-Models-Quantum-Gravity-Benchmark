#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
GATE='ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION';PREREG='aa2b0256ce60d605574a18ec86c0bad5b5df1512';REPAIR_PREREG='adc7bfb9df77a90455cac1b0f0cb7255d80c44d5';ROOTS=(13,14,15);MAX_DEPTH=3
RGRID=(6,8,10,12);RHOS=(0.35,0.9,1.6,2.7)
PASS='ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED';INC='ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED';INVALID='ITER504T_INVALID'
def load(p):raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyadic_cell_valid(k,x):
 d=int(x.get('depth',-1));a=Fraction(x['amp_lower_q']);b=Fraction(x['amp_upper_q']);lo=Fraction(16+k,12800);hi=Fraction(17+k,12800)
 if d<0 or d>MAX_DEPTH:return False
 w=(hi-lo)/(2**d)
 if b-a!=w:return False
 q=(a-lo)/w
 return q.denominator==1 and 0<=q.numerator<2**d
def _nid(d,a,b):return (int(d),Fraction(a),Fraction(b))
def validate_inclusion_records(o,k):
 e=[];recs=o.get('componentwise_parent_inclusion_records')
 if not isinstance(recs,list):return ['missing_parent_inclusion_records']
 if o.get('componentwise_parent_inclusion_record_count')!=len(recs):e.append('parent_inclusion_record_count')
 if len(recs)!=o.get('visited_node_count',0)-1:e.append('parent_inclusion_vs_visited_count')
 lo=Fraction(16+k,12800);hi=Fraction(17+k,12800);root=_nid(0,lo,hi);nodes={root};child_ids=[];parent_to_children={}
 expected_pairs=[(R,rho) for R in RGRID for rho in RHOS]
 for rec in recs:
  try:
   d=int(rec['depth']);a=Fraction(rec['amp_lower_q']);b=Fraction(rec['amp_upper_q']);pd=int(rec['parent_depth']);pa=Fraction(rec['parent_amp_lower_q']);pb=Fraction(rec['parent_amp_upper_q'])
   if d!=pd+1:e.append('parent_depth_relation')
   if not dyadic_cell_valid(k,rec):e.append('parent_inclusion_non_dyadic_child')
   mid=(pa+pb)/2
   if (a,b) not in ((pa,mid),(mid,pb)):e.append('parent_child_midpoint_relation')
   cid=_nid(d,a,b);pid=_nid(pd,pa,pb);child_ids.append(cid);nodes.add(cid);parent_to_children.setdefault(pid,[]).append(cid)
  except Exception:
   e.append('parent_inclusion_identity_parse');continue
  haar=rec.get('haar_log_inclusion_by_R')
  if not isinstance(haar,dict) or set(haar)!=set(str(R) for R in RGRID) or any(type(haar.get(str(R))) is not bool for R in RGRID):e.append('haar_inclusion_shape')
  rows=rec.get('channel_inclusion_rows')
  if not isinstance(rows,list) or len(rows)!=len(expected_pairs):e.append('channel_inclusion_row_count');continue
  pairs=[]
  for row in rows:
   try:pairs.append((int(row.get('R')),float(row.get('rho'))))
   except Exception:pairs.append((None,None))
   bits=row.get('componentwise_inclusion')
   if not isinstance(bits,list) or len(bits)!=243 or any(type(x) is not bool for x in bits):e.append('channel_inclusion_component_shape')
  if pairs!=expected_pairs:e.append('channel_inclusion_R_rho_identity')
  if type(rec.get('all_componentwise_parent_inclusion')) is not bool:e.append('parent_inclusion_summary_type')
 if len(child_ids)!=len(set(child_ids)):e.append('duplicate_parent_inclusion_child')
 if len(nodes)!=o.get('visited_node_count'):e.append('visited_node_identity_count')
 for pid,kids in parent_to_children.items():
  if pid not in nodes:e.append('parent_inclusion_missing_parent_node')
  if len(kids)!=2:e.append('parent_inclusion_missing_sibling')
 try:
  leaf_ids={_nid(x['depth'],x['amp_lower_q'],x['amp_upper_q']) for x in o.get('leaves',[])}
  if not leaf_ids.issubset(nodes):e.append('leaf_missing_in_inclusion_tree')
 except Exception:e.append('leaf_inclusion_identity_parse')
 return e
def validate(o,k):
 e=[]
 for key,val in [('gate',GATE),('preregistration_commit',PREREG),('repair_preregistration_commit',REPAIR_PREREG),('root_box',k),('precision_bits',384),('python_flint','0.9.0'),('full_channel_count',243),('channel_pruning_used',False),('max_depth',MAX_DEPTH),('partition_rule','deterministic_dyadic_midpoint'),('local_derivative_recomputed_each_visited_node',True),('threshold_exact','1/20'),('robust_floor_exact','1'),('r_cohort_consumed',list(RGRID)),('rho_cohort_consumed',list(RHOS)),('cover_valid',True)]:
  if o.get(key)!=val:e.append(key)
 if o.get('invalid'):e.append('producer_invalid')
 leaves=o.get('leaves',[])
 if len(leaves)!=o.get('terminal_leaf_count'):e.append('leaf_count')
 if sum(not x.get('certified',False) for x in leaves)!=o.get('unresolved_leaf_count'):e.append('unresolved_count')
 expected_pm=[(R,rho) for R in RGRID for rho in RHOS]
 for x in leaves:
  if x.get('scientific_decision_transport')!='exact_arb_booleans_float_bounds_display_only':e.append('transport')
  if not x.get('validated_local_derivative'):e.append('local_derivative')
  try:
   if not dyadic_cell_valid(k,x):e.append('non_dyadic_cell')
  except Exception:e.append('dyadic_parse')
  if tuple(float(r.get('rho')) for r in x.get('per_rho',[]))!=RHOS:e.append('rhos')
  for r in x.get('per_rho',[]):
   if r.get('certified') is not bool(r.get('slope_floor_satisfied') and r.get('drift_within_tolerance')):e.append('boolean_consistency')
  try:pm=[(int(r.get('R')),float(r.get('rho'))) for r in x.get('possible_max',[])]
  except Exception:pm=[]
  if pm!=expected_pm:e.append('possible_max_R_rho_cohort')
  for r in x.get('possible_max',[]):
   inds=r.get('indices',[])
   if len(inds)!=len(set(inds)) or any(not isinstance(i,int) or i<0 or i>=243 for i in inds):e.append('possible_max')
 try:
  spans=sorted((Fraction(x['amp_lower_q']),Fraction(x['amp_upper_q'])) for x in leaves);lo=Fraction(16+k,12800);hi=Fraction(17+k,12800)
  if not spans or spans[0][0]!=lo or spans[-1][1]!=hi or any(spans[i][1]!=spans[i+1][0] for i in range(len(spans)-1)):e.append('cover')
 except Exception:e.append('cover_parse')
 e += validate_inclusion_records(o,k)
 return e
def main():
 p=argparse.ArgumentParser();[p.add_argument(f'--root{k}',required=True) for k in ROOTS];p.add_argument('--out',required=True);a=p.parse_args();errs=[];roots=[];hs={}
 for k in ROOTS:
  o,h=load(getattr(a,f'root{k}'));errs += [f'{k}:{x}' for x in validate(o,k)];roots.append(o);hs[str(k)]=h
 unresolved=sum(o.get('unresolved_leaf_count',0) for o in roots);cls=INVALID if errs else (PASS if unresolved==0 else INC)
 out={'gate':GATE,'preregistration_commit':PREREG,'repair_preregistration_commit':REPAIR_PREREG,'classification':cls,'errors':errs,'root_sha256':hs,'root_count':len(roots),'total_terminal_leaves':sum(o.get('terminal_leaf_count',0) for o in roots),'total_unresolved_leaves':unresolved,'total_visited_nodes':sum(o.get('visited_node_count',0) for o in roots),'threshold_exact':'1/20','robust_floor_exact':'1','max_depth':MAX_DEPTH,'r_cohort_binding_implemented':not any('r_cohort' in x or 'R_rho_cohort' in x or 'inclusion_R_rho_identity' in x for x in errs),'componentwise_parent_inclusion_control_implemented':not any('inclusion' in x for x in errs),'partition_identity_verified':'exact_rational_dyadic_cells','scientific_decision_transport':'producer_exact_arb_booleans','roots':roots,'claim_ceiling':'Three-root bounded local-D mechanism test only'}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['payload_sha256']=hashlib.sha256(payload).hexdigest();q=Path(a.out);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='roots'},indent=2,sort_keys=True));return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
