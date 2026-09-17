#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,hashlib,json
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
 lo=Fraction(16+k,12800);hi=Fraction(17+k,12800);nodes={_nid(0,lo,hi)};child_ids=[];parent_to_children={}
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
 expected={'gate':GATE,'preregistration_commit':PREREG,'repair_preregistration_commit':REPAIR_PREREG,'root_box':k,'precision_bits':384,'python_flint':'0.9.0','full_channel_count':243,'channel_pruning_used':False,'max_depth':MAX_DEPTH,'partition_rule':'deterministic_dyadic_midpoint','local_derivative_recomputed_each_visited_node':True,'threshold_exact':'1/20','robust_floor_exact':'1','r_cohort_consumed':list(RGRID),'rho_cohort_consumed':list(RHOS),'cover_valid':True}
 for q,v in expected.items():
  if o.get(q)!=v:e.append(q)
 if o.get('invalid'):e.append('producer_invalid')
 leaves=o.get('leaves',[])
 if len(leaves)!=o.get('terminal_leaf_count'):e.append('terminal_leaf_count')
 if sum(not x.get('certified',False) for x in leaves)!=o.get('unresolved_leaf_count'):e.append('unresolved_leaf_count')
 try:
  spans=sorted((Fraction(x['amp_lower_q']),Fraction(x['amp_upper_q'])) for x in leaves);lo=Fraction(16+k,12800);hi=Fraction(17+k,12800)
  if not spans or spans[0][0]!=lo or spans[-1][1]!=hi or any(spans[i][1]!=spans[i+1][0] for i in range(len(spans)-1)):e.append('cover')
 except Exception:e.append('cover_parse')
 expected_pm=[(R,rho) for R in RGRID for rho in RHOS]
 for x in leaves:
  if x.get('scientific_decision_transport')!='exact_arb_booleans_float_bounds_display_only':e.append('transport')
  if x.get('validated_local_derivative') is not True:e.append('validated_local_derivative')
  try:
   if not dyadic_cell_valid(k,x):e.append('non_dyadic_cell')
  except Exception:e.append('dyadic_parse')
  prs=x.get('per_rho',[])
  if tuple(float(r.get('rho')) for r in prs)!=RHOS:e.append('rhos')
  for r in prs:
   if r.get('certified') is not bool(r.get('slope_floor_satisfied') and r.get('drift_within_tolerance')):e.append('exact_boolean_consistency')
  pmrows=x.get('possible_max',[])
  try:pairs=[(int(pm.get('R')),float(pm.get('rho'))) for pm in pmrows]
  except Exception:pairs=[]
  if pairs!=expected_pm:e.append('possible_max_R_rho_cohort')
  for pm in pmrows:
   inds=pm.get('indices',[])
   if len(inds)!=len(set(inds)) or any(not isinstance(i,int) or i<0 or i>=243 for i in inds):e.append('possible_max')
 e += validate_inclusion_records(o,k)
 return e
def classify(roots):
 unresolved=sum(roots[k].get('unresolved_leaf_count',0) for k in ROOTS)
 return PASS if unresolved==0 else INC
def projection(roots):
 out=[]
 for k in ROOTS:
  for x in roots[k]['leaves']:
   out.append((k,x['amp_lower_q'],x['amp_upper_q'],x['depth'],x['certified'],tuple((float(r['rho']),r['slope_floor_satisfied'],r['drift_within_tolerance'],r['certified']) for r in x['per_rho']),tuple((pm['R'],float(pm['rho']),tuple(pm['indices'])) for pm in x['possible_max'])))
 return out
def inclusion_stats(roots):
 records=0;false_components=0;total_components=0
 for k in ROOTS:
  for rec in roots[k].get('componentwise_parent_inclusion_records',[]):
   records+=1
   for v in rec.get('haar_log_inclusion_by_R',{}).values():total_components+=1;false_components+=int(v is False)
   for row in rec.get('channel_inclusion_rows',[]):
    for v in row.get('componentwise_inclusion',[]):total_components+=1;false_components+=int(v is False)
 return {'record_count':records,'component_count':total_components,'false_component_count':false_components,'all_components_included':false_components==0}
def negative_controls(base):
 tests={}
 def reject(name,mut):
  x=copy.deepcopy(base);mut(x);errs=[]
  for k in ROOTS:errs += [f'{k}:{q}' for q in validate(x[k],k)] if k in x else ['missing_root']
  tests[name]=bool(errs)
 reject('omitted_channel',lambda x:x[13].__setitem__('full_channel_count',242))
 reject('wrong_threshold',lambda x:x[13].__setitem__('threshold_exact','0.0500001'))
 reject('wrong_floor',lambda x:x[13].__setitem__('robust_floor_exact','0.9'))
 reject('float_reconstructed_predicate',lambda x:x[13]['leaves'][0].__setitem__('scientific_decision_transport','float_threshold'))
 reject('depth_increase',lambda x:x[13]['leaves'][0].__setitem__('depth',4))
 reject('outcome_dependent_non_dyadic_partition',lambda x:x[13]['leaves'][0].__setitem__('amp_upper_q',str(Fraction(x[13]['leaves'][0]['amp_upper_q'])+Fraction(1,10**12))))
 reject('missing_child_cover',lambda x:x[13]['leaves'].pop())
 reject('derivative_midpoint_truth',lambda x:x[13]['leaves'][0].__setitem__('validated_local_derivative',False))
 reject('reuse_root_derivative',lambda x:x[13].__setitem__('local_derivative_recomputed_each_visited_node',False))
 reject('channel_pruning',lambda x:x[13].__setitem__('channel_pruning_used',True))
 reject('wrong_rho_cohort',lambda x:x[13]['leaves'][0]['per_rho'][0].__setitem__('rho',0.36))
 reject('wrong_R_cohort_top_level',lambda x:x[13].__setitem__('r_cohort_consumed',[6,8,10,14]))
 reject('missing_R_cohort_top_level',lambda x:x[13].__setitem__('r_cohort_consumed',[6,8,10]))
 reject('extra_R_cohort_top_level',lambda x:x[13].__setitem__('r_cohort_consumed',[6,8,10,12,14]))
 def mutate_possible_R(x):
  for leaf in x[13]['leaves']:
   for row in leaf['possible_max']:
    if row['R']==6:row['R']=7
 reject('R_6_to_7_possible_max',mutate_possible_R)
 reject('missing_parent_inclusion_record',lambda x:x[13]['componentwise_parent_inclusion_records'].pop())
 reject('malformed_parent_inclusion_boolean',lambda x:x[13]['componentwise_parent_inclusion_records'][0]['channel_inclusion_rows'][0]['componentwise_inclusion'].__setitem__(0,None))
 reject('wrong_parent_inclusion_R',lambda x:x[13]['componentwise_parent_inclusion_records'][0]['channel_inclusion_rows'][0].__setitem__('R',7))
 reject('missing_provenance',lambda x:x[13].__setitem__('preregistration_commit','bad'))
 return tests
def main():
 p=argparse.ArgumentParser()
 for lane in ('a','b'):
  for k in ROOTS:p.add_argument(f'--{lane}-root{k}',required=True)
  p.add_argument(f'--{lane}-assembled',required=True)
 p.add_argument('--aggregate',required=True);p.add_argument('--out',required=True);a=p.parse_args();A={};B={};ha={};hb={};errs=[]
 for lane,roots,hs in (('a',A,ha),('b',B,hb)):
  for k in ROOTS:
   o,h=load(getattr(a,f'{lane}_root{k}'));roots[k]=o;hs[str(k)]=h;errs += [f'{lane}:{k}:{q}' for q in validate(o,k)]
 aa,aah=load(a.a_assembled);bb,bbh=load(a.b_assembled);agg,aggh=load(a.aggregate);ca=classify(A) if not [e for e in errs if e.startswith('a:')] else INVALID;cb=classify(B) if not [e for e in errs if e.startswith('b:')] else INVALID
 for tag,o,c in (('a',aa,ca),('b',bb,cb)):
  if o.get('classification')!=c:errs.append('assembled_'+tag)
  if o.get('r_cohort_binding_implemented') is not True:errs.append('assembled_'+tag+'_r_cohort_binding')
  if o.get('componentwise_parent_inclusion_control_implemented') is not True:errs.append('assembled_'+tag+'_parent_inclusion_binding')
 cross=projection(A)==projection(B)
 if not cross:errs.append('cross_environment_projection')
 if ca!=cb:errs.append('cross_environment_classification')
 if agg.get('classification')!=ca or agg.get('cross_environment_exact_decision_agreement') is not True:errs.append('aggregate_authority')
 if agg.get('r_cohort_binding_implemented') is not True or agg.get('componentwise_parent_inclusion_control_implemented') is not True:errs.append('aggregate_repair_binding')
 neg=negative_controls(A)
 if not all(neg.values()):errs.append('negative_controls')
 cls=ca if not errs else INVALID
 out={'gate':GATE,'preregistration_commit':PREREG,'repair_preregistration_commit':REPAIR_PREREG,'classification':cls,'critic_errors':errs,'cross_environment_exact_decision_agreement':cross,'lane_a_root_sha256':ha,'lane_b_root_sha256':hb,'lane_a_assembled_sha256':aah,'lane_b_assembled_sha256':bbh,'aggregate_sha256':aggh,'negative_controls':neg,'lane_a_parent_inclusion_stats':inclusion_stats(A),'lane_b_parent_inclusion_stats':inclusion_stats(B),'componentwise_parent_inclusion_control_implemented':not any('inclusion' in e for e in errs),'r_cohort_binding_implemented':not any('R_cohort' in e or 'r_cohort' in e for e in errs),'threshold_exact':'1/20','robust_floor_exact':'1','max_depth':MAX_DEPTH,'partition_identity_verified':'exact_rational_dyadic_cells','claim_ceiling':'Independent three-root bounded local-D Critic only'}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['critic_payload_sha256']=hashlib.sha256(payload).hexdigest();q=Path(a.out);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
