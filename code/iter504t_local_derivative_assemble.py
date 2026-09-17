#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
GATE='ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION';PREREG='aa2b0256ce60d605574a18ec86c0bad5b5df1512';ROOTS=(13,14,15);MAX_DEPTH=3
PASS='ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED';INC='ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED';INVALID='ITER504T_INVALID'
def load(p):raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyadic_cell_valid(k,x):
 d=int(x.get('depth',-1));a=Fraction(x['amp_lower_q']);b=Fraction(x['amp_upper_q']);lo=Fraction(16+k,12800);hi=Fraction(17+k,12800)
 if d<0 or d>MAX_DEPTH:return False
 w=(hi-lo)/(2**d)
 if b-a!=w:return False
 q=(a-lo)/w
 return q.denominator==1 and 0<=q.numerator<2**d
def validate(o,k):
 e=[]
 for key,val in [('gate',GATE),('preregistration_commit',PREREG),('root_box',k),('precision_bits',384),('python_flint','0.9.0'),('full_channel_count',243),('channel_pruning_used',False),('max_depth',MAX_DEPTH),('partition_rule','deterministic_dyadic_midpoint'),('local_derivative_recomputed_each_visited_node',True),('threshold_exact','1/20'),('robust_floor_exact','1'),('cover_valid',True)]:
  if o.get(key)!=val:e.append(key)
 if o.get('invalid'):e.append('producer_invalid')
 leaves=o.get('leaves',[])
 if len(leaves)!=o.get('terminal_leaf_count'):e.append('leaf_count')
 if sum(not x.get('certified',False) for x in leaves)!=o.get('unresolved_leaf_count'):e.append('unresolved_count')
 for x in leaves:
  if x.get('scientific_decision_transport')!='exact_arb_booleans_float_bounds_display_only':e.append('transport')
  if not x.get('validated_local_derivative'):e.append('local_derivative')
  try:
   if not dyadic_cell_valid(k,x):e.append('non_dyadic_cell')
  except Exception:e.append('dyadic_parse')
  if len(x.get('per_rho',[]))!=4:e.append('rhos')
  for r in x.get('per_rho',[]):
   if r.get('certified') is not bool(r.get('slope_floor_satisfied') and r.get('drift_within_tolerance')):e.append('boolean_consistency')
 try:
  spans=sorted((Fraction(x['amp_lower_q']),Fraction(x['amp_upper_q'])) for x in leaves);lo=Fraction(16+k,12800);hi=Fraction(17+k,12800)
  if not spans or spans[0][0]!=lo or spans[-1][1]!=hi or any(spans[i][1]!=spans[i+1][0] for i in range(len(spans)-1)):e.append('cover')
 except Exception:e.append('cover_parse')
 return e
def main():
 p=argparse.ArgumentParser();[p.add_argument(f'--root{k}',required=True) for k in ROOTS];p.add_argument('--out',required=True);a=p.parse_args();errs=[];roots=[];hs={}
 for k in ROOTS:
  o,h=load(getattr(a,f'root{k}'));errs += [f'{k}:{x}' for x in validate(o,k)];roots.append(o);hs[str(k)]=h
 unresolved=sum(o.get('unresolved_leaf_count',0) for o in roots);cls=INVALID if errs else (PASS if unresolved==0 else INC)
 out={'gate':GATE,'preregistration_commit':PREREG,'classification':cls,'errors':errs,'root_sha256':hs,'root_count':len(roots),'total_terminal_leaves':sum(o.get('terminal_leaf_count',0) for o in roots),'total_unresolved_leaves':unresolved,'total_visited_nodes':sum(o.get('visited_node_count',0) for o in roots),'threshold_exact':'1/20','robust_floor_exact':'1','max_depth':MAX_DEPTH,'partition_identity_verified':'exact_rational_dyadic_cells','scientific_decision_transport':'producer_exact_arb_booleans','roots':roots,'claim_ceiling':'Three-root bounded local-D mechanism test only'}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['payload_sha256']=hashlib.sha256(payload).hexdigest();q=Path(a.out);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='roots'},indent=2,sort_keys=True));return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
