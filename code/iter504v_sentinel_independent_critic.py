#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json
from fractions import Fraction
from pathlib import Path

GATE='ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_FIRST'
PREREG='c162f23df45a58c567fa04fcdf99035497e482f2'
SENTINEL_SHA='b56a2a32cd96b28c14aaaa86f1062d1f2f2a167a2295ed99f904a99fd8371e82'
CAMPAIGN_DESIGN='6a789730833120a5e3037fdc11fe03b28ed5b9cb'
CAMPAIGN_MANIFEST_BLOB='d3b8821e08243016bd475f3faf9f2161deed13d8'
PARENT_TERMINAL='a31db0d6b9f98448977a6fcdde80a45e3e7195fe'
POSTCLOSURE_AUDIT='dd32ae2616f4cbe3826f73c7a1d2f51818b4954c'
PASS='ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED'
INC='ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_TO_UNIFORM_CERTIFICATION_SCOPED'
INVALID='ITER504V_SENTINEL_INVALID'
RGRID=(6,8,10,12); RHOS=(0.35,0.9,1.6,2.7); MAX_DEPTH=3
DIRECTIONS=[
 [1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,-1,-1,-1],[1,1,1,-1,-1,-1],
 [1,-1,-1,1,1,-1],[1,-1,-1,1,1,-1],[1,-1,1,-1,1,-1],[1,-1,1,-1,1,-1],
 [1,1,-1,1,-1,-1],[1,1,-1,1,-1,-1],[1,-1,1,1,-1,1],[1,-1,1,1,-1,1],
 [1,1,-1,-1,1,1],[1,1,-1,-1,1,1],[1,-1,-1,-1,-1,1],[1,-1,-1,-1,-1,1],
]
STATE_IDS=[
 '0to5|b0|p0|x00','1to4|b0|p1|x01','2to3|b0|p2|x02','0to5|b0|p3|x03',
 '1to4|b1|p0|x04','2to3|b1|p1|x05','0to5|b1|p2|x06','1to4|b1|p3|x07',
 '2to3|b2|p0|x08','0to5|b2|p1|x09','1to4|b2|p2|x10','2to3|b2|p3|x11',
 '0to5|b3|p0|x12','1to4|b3|p1|x13','2to3|b3|p2|x14','0to5|b3|p3|x15']
EXPECTED={}
for i,s in enumerate(STATE_IDS):
 causal=s.split('|')[0]; block=int(s.split('|')[1][1:]); path=int(s.split('|')[2][1:])
 EXPECTED[s]=(causal,block,path,i,DIRECTIONS[i],1 if i%2==0 else -1)

def sha_json(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p):
 raw=Path(p).read_bytes(); return json.loads(raw),hashlib.sha256(raw).hexdigest()
def box_interval(i): return Fraction(16+i,12800),Fraction(17+i,12800)
def dyadic_cell_valid(box,leaf):
 d=int(leaf.get('depth',-1)); a=Fraction(leaf['amp_lower_q']); b=Fraction(leaf['amp_upper_q']); lo,hi=box_interval(box)
 if d<0 or d>MAX_DEPTH: return False
 w=(hi-lo)/(2**d); q=(a-lo)/w
 return b-a==w and q.denominator==1 and 0<=q.numerator<2**d

def validate_case(o,sid):
 e=[]; causal,block,path,box,direction,sign=EXPECTED[sid]
 checks={'gate':GATE,'preregistration_commit':PREREG,'sentinel_sequence_sha256':SENTINEL_SHA,'campaign_design_commit':CAMPAIGN_DESIGN,
 'campaign_manifest_blob':CAMPAIGN_MANIFEST_BLOB,'parent_terminal_authority_commit':PARENT_TERMINAL,'postclosure_audit_commit':POSTCLOSURE_AUDIT,
 'state_id':sid,'case_id':sid,'causal':causal,'block':block,'path':path,'box':box,'direction':direction,'sign':sign,'precision_bits':384,
 'python_flint':'0.9.0','full_channel_count':243,'channel_pruning_used':False,'max_depth':3,'partition_rule':'deterministic_dyadic_midpoint',
 'local_derivative_recomputed_each_visited_node':True,'leaf_certification_binding':'all_per_rho_exact','threshold_exact':'1/20','robust_floor_exact':'1',
 'r_cohort_consumed':list(RGRID),'rho_cohort_consumed':list(RHOS),'cover_valid':True}
 for k,v in checks.items():
  if o.get(k)!=v: e.append(k)
 lo,hi=box_interval(box)
 if Fraction(o.get('parent_amp_lower_q','0'))!=lo or Fraction(o.get('parent_amp_upper_q','0'))!=hi: e.append('parent_interval')
 leaves=o.get('leaves',[])
 if len(leaves)!=o.get('terminal_leaf_count'): e.append('terminal_leaf_count')
 if sum(not bool(x.get('certified')) for x in leaves)!=o.get('unresolved_leaf_count'): e.append('unresolved_leaf_count')
 try:
  spans=sorted((Fraction(x['amp_lower_q']),Fraction(x['amp_upper_q'])) for x in leaves)
  if not spans or spans[0][0]!=lo or spans[-1][1]!=hi or any(spans[i][1]!=spans[i+1][0] for i in range(len(spans)-1)): e.append('cover')
 except Exception: e.append('cover_parse')
 expected_pm={(R,r) for R in RGRID for r in RHOS}
 for leaf in leaves:
  try:
   if not dyadic_cell_valid(box,leaf): e.append('dyadic_leaf')
   if Fraction(leaf['local_mid_q']) != (Fraction(leaf['amp_lower_q'])+Fraction(leaf['amp_upper_q']))/2: e.append('local_midpoint')
  except Exception: e.append('dyadic_parse')
  if leaf.get('validated_local_derivative') is not True or leaf.get('local_derivative_recomputed_here') is not True: e.append('local_derivative')
  if leaf.get('leaf_certification_binding')!='all_per_rho_exact': e.append('leaf_binding_tag')
  if leaf.get('scientific_decision_transport')!='exact_arb_booleans_float_bounds_display_only': e.append('decision_transport')
  prs=leaf.get('per_rho',[])
  if tuple(float(x.get('rho')) for x in prs)!=RHOS: e.append('rho_rows')
  for row in prs:
   if row.get('certified') is not bool(row.get('slope_floor_satisfied') and row.get('drift_within_tolerance')): e.append('per_rho_binding')
  if leaf.get('certified') is not all(row.get('certified') is True for row in prs): e.append('C4_leaf_binding')
  if not leaf.get('certified') and int(leaf.get('depth',-1))!=MAX_DEPTH: e.append('premature_unresolved_leaf_depth')
  pm=leaf.get('possible_max',[])
  if len(pm)!=16 or {(int(x.get('R')),float(x.get('rho'))) for x in pm}!=expected_pm: e.append('possible_max_grid')
  for row in pm:
   inds=row.get('indices',[])
   if len(inds)!=len(set(inds)) or any(not isinstance(i,int) or not 0<=i<243 for i in inds): e.append('possible_max_indices')
 incs=o.get('componentwise_parent_inclusion_records',[])
 if len(incs)!=o.get('componentwise_parent_inclusion_record_count') or len(incs)!=max(0,int(o.get('visited_node_count',0))-1): e.append('inclusion_count')
 for rec in incs:
  if set(rec.get('haar_log_inclusion_by_R',{}))!={str(R) for R in RGRID}: e.append('inclusion_haar')
  rows=rec.get('channel_inclusion_rows',[])
  if len(rows)!=16 or {(int(x.get('R')),float(x.get('rho'))) for x in rows}!=expected_pm: e.append('inclusion_grid')
  for row in rows:
   bits=row.get('componentwise_inclusion',[])
   if len(bits)!=243 or any(type(b) is not bool for b in bits): e.append('inclusion_bits')
 return e

def discover(root,py):
 cases={}; hashes={}; dup=[]
 for p in sorted(Path(root).glob(f'iter504v-sentinel-{py}-*/case.json')):
  o,h=load(p); sid=o.get('state_id')
  if sid in cases: dup.append(sid)
  else: cases[sid]=o; hashes[sid]=h
 return cases,hashes,dup

def validate_all(cases):
 e=[]
 if set(cases)!=set(EXPECTED): e.append('case_set')
 for sid in STATE_IDS:
  if sid in cases: e += [f'{sid}:{x}' for x in validate_case(cases[sid],sid)]
 return e

def projection(cases):
 out=[]
 for sid in STATE_IDS:
  o=cases[sid]
  out.append({'state_id':o['state_id'],'causal':o['causal'],'block':o['block'],'path':o['path'],'box':o['box'],'direction':o['direction'],'sign':o['sign'],
   'parent_amp_lower_q':o['parent_amp_lower_q'],'parent_amp_upper_q':o['parent_amp_upper_q'],'visited_node_count':o['visited_node_count'],'terminal_leaf_count':o['terminal_leaf_count'],'unresolved_leaf_count':o['unresolved_leaf_count'],
   'leaves':[{'depth':x['depth'],'amp_lower_q':x['amp_lower_q'],'amp_upper_q':x['amp_upper_q'],'local_mid_q':x['local_mid_q'],'certified':x['certified'],
    'per_rho':[(float(r['rho']),r['slope_floor_satisfied'],r['drift_within_tolerance'],r['certified']) for r in x['per_rho']],
    'possible_max':[(p['R'],float(p['rho']),tuple(p['indices'])) for p in x['possible_max']]} for x in o['leaves']]})
 return out

def classify(cases): return INC if any(cases[s]['unresolved_leaf_count']>0 for s in STATE_IDS) else PASS

def negative_controls(base):
 tests={}; sid=STATE_IDS[0]
 def reject(name,mut):
  x=copy.deepcopy(base); mut(x); tests[name]=bool(validate_all(x))
 reject('wrong_state_identity',lambda x:x[sid].__setitem__('state_id','BAD'))
 reject('changed_threshold',lambda x:x[sid].__setitem__('threshold_exact','1/19'))
 reject('changed_floor',lambda x:x[sid].__setitem__('robust_floor_exact','0.9'))
 reject('changed_depth',lambda x:x[sid].__setitem__('max_depth',4))
 reject('channel_pruning',lambda x:x[sid].__setitem__('full_channel_count',242))
 reject('wrong_R_cohort',lambda x:x[sid].__setitem__('r_cohort_consumed',[7,8,10,12]))
 reject('wrong_rho_cohort',lambda x:x[sid].__setitem__('rho_cohort_consumed',[0.36,0.9,1.6,2.7]))
 reject('root_derivative_reuse',lambda x:x[sid].__setitem__('local_derivative_recomputed_each_visited_node',False))
 reject('C4_true_leaf_false_rho',lambda x:x[sid]['leaves'][0]['per_rho'][0].__setitem__('certified',False))
 def premature(x):
  leaf=x[sid]['leaves'][0]; leaf['certified']=False; leaf['depth']=2; x[sid]['unresolved_leaf_count']=1
  for r in leaf['per_rho']: r['certified']=False; r['drift_within_tolerance']=False
 reject('premature_unresolved_leaf_depth',premature)
 def badmid(x):
  leaf=x[sid]['leaves'][0]; leaf['local_mid_q']=str(Fraction(leaf['local_mid_q'])+Fraction(1,10**9))
 reject('midpoint_binding',badmid)
 def badtree(x): x[sid]['leaves'][0].__setitem__('amp_upper_q',x[sid]['leaves'][1]['amp_upper_q'])
 reject('tree_partition_binding',badtree)
 return tests

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
 errors=[]; lanes={}; hashes={}; projections={}; classes={}; assembled={}
 for py in ('3.11','3.13'):
  cases,h,dup=discover(a.source_dir,py); lanes[py]=cases; hashes[py]=h
  if dup: errors.append(f'{py}:duplicate_cases')
  ve=validate_all(cases); errors += [f'{py}:{x}' for x in ve]
  if not ve and set(cases)==set(EXPECTED):
   classes[py]=classify(cases); projections[py]=projection(cases)
  else: classes[py]=INVALID; projections[py]=None
  apath=Path(a.source_dir)/f'iter504v-sentinel-assembled-{py}'/f'iter504v-{py}.json'
  if not apath.exists(): errors.append(f'{py}:missing_assembly'); continue
  assembled[py],_=load(apath)
  if assembled[py].get('classification')!=classes[py]: errors.append(f'{py}:assembled_classification')
  if projections[py] is not None and assembled[py].get('decision_projection_sha256')!=sha_json(projections[py]): errors.append(f'{py}:assembled_projection')
 agg_path=Path(a.source_dir)/'iter504v-sentinel-aggregate'/'iter504v-aggregate.json'
 agg,aggh=load(agg_path) if agg_path.exists() else ({},None)
 cross=projections.get('3.11')==projections.get('3.13') and classes.get('3.11')==classes.get('3.13') and classes.get('3.11')!=INVALID
 if not cross: errors.append('cross_environment_exact_projection')
 source_class=classes.get('3.11') if cross else INVALID
 if agg.get('classification')!=source_class or agg.get('cross_environment_exact_decision_agreement') is not True: errors.append('aggregate_authority')
 neg=negative_controls(lanes['3.11']) if set(lanes.get('3.11',{}))==set(EXPECTED) and not [e for e in errors if e.startswith('3.11:')] else {}
 if not neg or not all(neg.values()): errors.append('negative_controls')
 final=source_class if not errors else INVALID
 out={'gate':GATE,'critic_kind':'independent_artifact_reconstruction','preregistration_commit':PREREG,'sentinel_sequence_sha256':SENTINEL_SHA,
 'classification':final,'critic_errors':errors,'cross_environment_exact_decision_agreement':cross,'source_aggregate_sha256':aggh,
 'lane_3_11_case_sha256':hashes.get('3.11',{}),'lane_3_13_case_sha256':hashes.get('3.13',{}),'decision_projection_sha256':sha_json(projections['3.11']) if cross else None,
 'negative_controls':neg,'counterexample_state_ids':[s for s in STATE_IDS if lanes.get('3.11',{}).get(s,{}).get('unresolved_leaf_count',0)>0] if final!=INVALID else None,
 'total_cases':16 if final!=INVALID else None,'total_unresolved_leaves':sum(lanes['3.11'][s]['unresolved_leaf_count'] for s in STATE_IDS) if final!=INVALID else None,
 'channels':243,'r_cohort':list(RGRID),'rho_cohort':list(RHOS),'max_depth':3,'threshold_exact':'1/20','robust_floor_exact':'1',
 'claim_ceiling':'Independent Critic of frozen 16-state Iter504V sentinel only; no full q=1-domain claim'}
 out['critic_payload_sha256']=sha_json(out)
 p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps(out,indent=2,sort_keys=True)); return 2 if final==INVALID else 0
if __name__=='__main__': raise SystemExit(main())
