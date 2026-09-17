#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,hashlib,json
from fractions import Fraction
from pathlib import Path
GATE='ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION';PREREG='aa2b0256ce60d605574a18ec86c0bad5b5df1512';ROOTS=(13,14,15);MAX_DEPTH=3
PASS='ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED';INC='ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED';INVALID='ITER504T_INVALID'
def load(p):raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def validate(o,k):
 e=[]
 expected={'gate':GATE,'preregistration_commit':PREREG,'root_box':k,'precision_bits':384,'python_flint':'0.9.0','full_channel_count':243,'channel_pruning_used':False,'max_depth':MAX_DEPTH,'partition_rule':'deterministic_dyadic_midpoint','local_derivative_recomputed_each_visited_node':True,'threshold_exact':'1/20','robust_floor_exact':'1','cover_valid':True}
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
 for x in leaves:
  if x.get('scientific_decision_transport')!='exact_arb_booleans_float_bounds_display_only':e.append('transport')
  if x.get('validated_local_derivative') is not True:e.append('validated_local_derivative')
  if int(x.get('depth',99))>MAX_DEPTH:e.append('depth')
  prs=x.get('per_rho',[])
  if tuple(float(r.get('rho')) for r in prs)!=(0.35,0.9,1.6,2.7):e.append('rhos')
  for r in prs:
   if r.get('certified') is not bool(r.get('slope_floor_satisfied') and r.get('drift_within_tolerance')):e.append('exact_boolean_consistency')
  for pm in x.get('possible_max',[]):
   inds=pm.get('indices',[])
   if len(inds)!=len(set(inds)) or any(not isinstance(i,int) or i<0 or i>=243 for i in inds):e.append('possible_max')
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
 reject('missing_child_cover',lambda x:x[13]['leaves'].pop())
 reject('derivative_midpoint_truth',lambda x:x[13]['leaves'][0].__setitem__('validated_local_derivative',False))
 reject('reuse_root_derivative',lambda x:x[13].__setitem__('local_derivative_recomputed_each_visited_node',False))
 reject('channel_pruning',lambda x:x[13].__setitem__('channel_pruning_used',True))
 reject('wrong_cohort',lambda x:x[13]['leaves'][0]['per_rho'][0].__setitem__('rho',0.36))
 reject('missing_provenance',lambda x:x[13].__setitem__('preregistration_commit','bad'))
 return tests
def main():
 p=argparse.ArgumentParser()
 for lane in ('a','b'):
  for k in ROOTS:p.add_argument(f'--{lane}-root{k}',required=True)
  p.add_argument(f'--{lane}-assembled',required=True)
 p.add_argument('--out',required=True);a=p.parse_args();A={};B={};ha={};hb={};errs=[]
 for lane,roots,hs in (('a',A,ha),('b',B,hb)):
  for k in ROOTS:
   o,h=load(getattr(a,f'{lane}_root{k}'));roots[k]=o;hs[str(k)]=h;errs += [f'{lane}:{k}:{q}' for q in validate(o,k)]
 aa,aah=load(a.a_assembled);bb,bbh=load(a.b_assembled);ca=classify(A) if not [e for e in errs if e.startswith('a:')] else INVALID;cb=classify(B) if not [e for e in errs if e.startswith('b:')] else INVALID
 if aa.get('classification')!=ca:errs.append('assembled_a')
 if bb.get('classification')!=cb:errs.append('assembled_b')
 cross=projection(A)==projection(B)
 if not cross:errs.append('cross_environment_projection')
 if ca!=cb:errs.append('cross_environment_classification')
 neg=negative_controls(A)
 if not all(neg.values()):errs.append('negative_controls')
 cls=ca if not errs else INVALID
 out={'gate':GATE,'preregistration_commit':PREREG,'classification':cls,'critic_errors':errs,'cross_environment_exact_decision_agreement':cross,'lane_a_root_sha256':ha,'lane_b_root_sha256':hb,'lane_a_assembled_sha256':aah,'lane_b_assembled_sha256':bbh,'negative_controls':neg,'threshold_exact':'1/20','robust_floor_exact':'1','max_depth':MAX_DEPTH,'claim_ceiling':'Independent three-root bounded local-D Critic only'}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['critic_payload_sha256']=hashlib.sha256(payload).hexdigest();q=Path(a.out);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
