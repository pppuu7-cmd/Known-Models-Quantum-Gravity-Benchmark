#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,hashlib,json
from fractions import Fraction
from pathlib import Path
GATE='ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR';PREREG='f6367456aa715fe6282ab70c1b2005971a4568c7'
REPAIRS=['88c92f86a765e9d8b441152674fc2c303f3f1ff3','4ef41c0f4ceed3082fd4d80930ef5d848f18802b','77d42eb58c03eef2356aed7a25795562760de4e3']
ROOTS=(13,14,15);RHOS=(0.35,0.9,1.6,2.7);LOCS=('LOW','MID','HIGH')
D='ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED';C='ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED';F='ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED';M='ITER504S_MIXED_MECHANISM_SCOPED';INVALID='ITER504S_INVALID'
def load(p):raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def one(rows,r):
 h=[x for x in rows if float(x.get('rho'))==r]
 if len(h)!=1:raise ValueError('rho');return h[0]
def fixed_all(rr):
 cand=rr.get('candidate_union',[]);inc=rr.get('ineligible_candidates',[]);viol=rr.get('violating_channel_indices',[])
 return bool(not inc and rr.get('eligible_count')==len(cand) and rr.get('competition_test_complete') is True and len(cand)>0 and not viol and rr.get('all_candidate_fixed_channel_drifts_within_tolerance') is True)
def validate_root(o,k):
 e=[]
 if o.get('gate')!=GATE:e.append('gate')
 if o.get('preregistration_commit')!=PREREG:e.append('prereg')
 if o.get('repair_preregistrations')!=REPAIRS:e.append('repairs')
 if o.get('root_box')!=k:e.append('root')
 if o.get('scientific_decision_transport')!='exact_arb_booleans_float_bounds_display_only':e.append('transport')
 if o.get('precision_bits')!=384 or o.get('full_channel_count')!=243 or o.get('channel_pruning_used') is not False:e.append('frozen_source')
 cs=o.get('cases',[])
 if tuple(x.get('location') for x in cs)!=LOCS:e.append('locations')
 lo=Fraction(16+k,12800);hi=Fraction(17+k,12800);mid=(lo+hi)/2;pts={'LOW':lo,'MID':mid,'HIGH':hi}
 for c in cs:
  loc=c.get('location')
  try:
   if Fraction(c['amp_q'])!=pts[loc] or Fraction(c['delta_q'])!=pts[loc]-mid:e.append(loc+':point')
  except Exception:e.append(str(loc)+':point_parse')
  for tag in ('full_D','center_D_sensitivity'):
   t=c.get(tag,{})
   if tuple(float(x.get('rho')) for x in t.get('per_rho',[]))!=RHOS:e.append(loc+':'+tag+':rhos')
   for rr in t.get('per_rho',[]):
    if rr.get('within_tolerance') is not bool(rr.get('slope_floor_satisfied') and rr.get('drift_within_tolerance')):e.append(loc+':'+tag+':composite')
   for rr in t.get('fixed_channel',[]):
    cand=rr.get('candidate_union',[]);inc=rr.get('ineligible_candidates',[]);viol=rr.get('violating_channel_indices',[])
    complete=bool(not inc and rr.get('eligible_count')==len(cand))
    if rr.get('competition_test_complete') is not complete:e.append(loc+':'+tag+':complete')
    if rr.get('all_candidate_fixed_channel_drifts_within_tolerance') is not bool(complete and len(cand)>0 and not viol):e.append(loc+':'+tag+':allwithin')
 return e
def classify(roots):
 mids=[];ends=[];cv=[]
 for k in ROOTS:
  for c in roots[k]['cases']:
   for rho in RHOS:
    f=one(c['full_D']['per_rho'],rho);z=one(c['center_D_sensitivity']['per_rho'],rho);cf=one(c['center_D_sensitivity']['fixed_channel'],rho)
    rec={'mid':c['location']=='MID','full_within':f['within_tolerance'],'fv':not f['drift_within_tolerance'],'cv':not z['drift_within_tolerance'],
         'deriv':bool((not f['drift_within_tolerance']) and z['drift_within_tolerance']),'complete':cf['competition_test_complete'],'fall':fixed_all(cf)}
    (mids if rec['mid'] else ends).append(rec)
    if rec['cv']:cv.append(rec)
 ep=[x for x in ends if x['fv']]
 if mids and all(x['full_within'] for x in mids) and ep and all(x['deriv'] for x in ep) and not cv:return D
 if cv and all(x['complete'] and x['fall'] for x in cv):return C
 if cv and all(x['complete'] for x in cv) and any(not x['fall'] for x in cv):return F
 return M
def projection(roots):
 p=[]
 for k in ROOTS:
  for c in roots[k]['cases']:
   z=[k,c['location'],c['amp_q']]
   for rho in RHOS:
    f=one(c['full_D']['per_rho'],rho);cc=one(c['center_D_sensitivity']['per_rho'],rho);ff=one(c['full_D']['fixed_channel'],rho);cf=one(c['center_D_sensitivity']['fixed_channel'],rho)
    z.append((rho,f['slope_floor_satisfied'],f['drift_within_tolerance'],cc['slope_floor_satisfied'],cc['drift_within_tolerance'],tuple(ff['candidate_union']),tuple(ff['violating_channel_indices']),tuple(cf['candidate_union']),tuple(cf['violating_channel_indices'])))
   p.append(z)
 return p
def negative_controls(base):
 tests={}
 def reject(name,mut):
  x=copy.deepcopy(base);mut(x);err=[]
  for k in ROOTS:err += [f'{k}:{q}' for q in validate_root(x[k],k)] if k in x else ['missing_root']
  tests[name]=bool(err)
 reject('missing_root',lambda x:x.pop(13))
 reject('wrong_exact_amplitude',lambda x:x[13]['cases'][0].__setitem__('amp_q','1/2'))
 reject('active_channel_pruning',lambda x:x[13].__setitem__('channel_pruning_used',True))
 reject('float_transport_reintroduced',lambda x:x[13].__setitem__('scientific_decision_transport','float'))
 reject('corrupt_composite_boolean',lambda x:x[13]['cases'][0]['full_D']['per_rho'][0].__setitem__('within_tolerance',not x[13]['cases'][0]['full_D']['per_rho'][0]['within_tolerance']))
 reject('corrupt_fixed_exact_boolean',lambda x:x[13]['cases'][0]['full_D']['fixed_channel'][0].__setitem__('all_candidate_fixed_channel_drifts_within_tolerance',not x[13]['cases'][0]['full_D']['fixed_channel'][0]['all_candidate_fixed_channel_drifts_within_tolerance']))
 return tests
def main():
 ap=argparse.ArgumentParser()
 for lane in ('a','b'):
  for k in ROOTS:ap.add_argument(f'--{lane}-root{k}',required=True)
  ap.add_argument(f'--{lane}-assembled',required=True)
 ap.add_argument('--aggregate',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
 rootsA={};rootsB={};hashA={};hashB={};errs=[]
 for lane,roots,hs in (('a',rootsA,hashA),('b',rootsB,hashB)):
  for k in ROOTS:
   o,h=load(getattr(a,f'{lane}_root{k}'));roots[k]=o;hs[str(k)]=h;errs += [f'{lane}:{k}:{x}' for x in validate_root(o,k)]
 A,Ah=load(a.a_assembled);B,Bh=load(a.b_assembled);agg,_=load(a.aggregate)
 clsA=classify(rootsA) if not [x for x in errs if x.startswith('a:')] else INVALID;clsB=classify(rootsB) if not [x for x in errs if x.startswith('b:')] else INVALID
 if A.get('classification')!=clsA:errs.append('assembled_a_class')
 if B.get('classification')!=clsB:errs.append('assembled_b_class')
 if clsA!=clsB:errs.append('cross_environment_class')
 cross=projection(rootsA)==projection(rootsB)
 if not cross:errs.append('cross_environment_exact_projection')
 if agg.get('classification')!=clsA:errs.append('aggregate_class')
 neg=negative_controls(rootsA)
 if not all(neg.values()):errs.append('negative_control_failure')
 cls=clsA if not errs and clsA!=INVALID else INVALID
 out={'gate':GATE,'preregistration_commit':PREREG,'repair_preregistrations':REPAIRS,'classification':cls,'critic_errors':errs,
      'cross_environment_exact_decision_agreement':cross,'lane_a_root_sha256':hashA,'lane_b_root_sha256':hashB,'lane_a_assembled_sha256':Ah,'lane_b_assembled_sha256':Bh,
      'negative_controls':neg,'scientific_decision_transport':'exact_arb_booleans_float_bounds_display_only','claim_ceiling':'Independent exact-decision Iter504S verification only; no full-domain theorem'}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['critic_payload_sha256']=hashlib.sha256(payload).hexdigest()
 p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
