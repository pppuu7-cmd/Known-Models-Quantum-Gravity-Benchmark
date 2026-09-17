#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
import iter501_direct_max_envelope_interval as prev
import iter503_ad_core as ad
import iter504_centered_shard as parent
import iter504r_root_affine_reuse as rgate
ctx.prec=384
GATE='ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION'
PREREG='aa2b0256ce60d605574a18ec86c0bad5b5df1512'
PARENT='1b0004064575f046210383dc7b1ee22d4f25e66b'
REPAIR_PREREG='adc7bfb9df77a90455cac1b0f0cb7255d80c44d5'
ROOTS=(13,14,15);MAX_DEPTH=3;TOL=arb('0.05');FLOOR=arb('1.0')
R_COHORT=tuple(int(x) for x in core.R_GRID)
RHO_COHORT=tuple(float(x) for x in core.RHOS)
def af(q): return arb(q.numerator)/arb(q.denominator)
def qt(q): return f'{q.numerator}/{q.denominator}'
def bf(x,s): return core.bound_float(x,s)
def extract_derivatives(a):
 x=np.asarray(a,dtype=object);o=np.empty(x.shape,dtype=object)
 for i in np.ndindex(x.shape):o[i]=ad.as_c(x[i]).d
 return o
def _arb_subseteq(child,parent):
 return bool(child.lower()>=parent.lower() and child.upper()<=parent.upper())
def _acb_subseteq(child,parent):
 return _arb_subseteq(child.real,parent.real) and _arb_subseteq(child.imag,parent.imag)
def _derivative_snapshot(m):
 out={'haar':{},'channels':{}}
 for R in R_COHORT:
  q=m['model'][R]
  out['haar'][R]=q['dlogH'].d
  rows={}
  for rr in q['rho']:
   rho=float(rr['rho']);a=np.asarray(rr['dvals'],dtype=object)
   rows[rho]=[ad.as_c(a[idx]).d for idx in np.ndindex(a.shape)]
  out['channels'][R]=rows
 return out
def _inclusion_record(child,parent_snap,loq,hiq,depth,parent_loq,parent_hiq,parent_depth):
 if tuple(sorted(child['haar']))!=R_COHORT or tuple(sorted(parent_snap['haar']))!=R_COHORT: raise ArithmeticError('R cohort changed in inclusion snapshot')
 haar={};rows=[];all_ok=True
 for R in R_COHORT:
  hb=_arb_subseteq(child['haar'][R],parent_snap['haar'][R]);haar[str(R)]=hb;all_ok &= hb
  if tuple(sorted(child['channels'][R]))!=RHO_COHORT or tuple(sorted(parent_snap['channels'][R]))!=RHO_COHORT: raise ArithmeticError('rho cohort changed in inclusion snapshot')
  for rho in RHO_COHORT:
   cv=child['channels'][R][rho];pv=parent_snap['channels'][R][rho]
   if len(cv)!=243 or len(pv)!=243: raise ArithmeticError('channel count changed in inclusion snapshot')
   bits=[_acb_subseteq(c,p) for c,p in zip(cv,pv)];all_ok &= all(bits)
   rows.append({'R':R,'rho':rho,'componentwise_inclusion':bits})
 return {'depth':depth,'amp_lower_q':qt(loq),'amp_upper_q':qt(hiq),'parent_depth':parent_depth,'parent_amp_lower_q':qt(parent_loq),'parent_amp_upper_q':qt(parent_hiq),'haar_log_inclusion_by_R':haar,'channel_inclusion_rows':rows,'all_componentwise_parent_inclusion':bool(all_ok)}
def build_local(loq,hiq,direction,sign):
 lo,hi=af(loq),af(hiq);amp=lo.union(hi);midq=(loq+hiq)/2;mid=af(midq);dual=ad.RD(amp,1);sig=core.SIGMAS['0to5']
 controls={'construction':True,'cycle':True,'source_additive':True,'center_regression':True,'finite_local_envelope':True}
 model={}
 for R in R_COHORT:
  ds=ad.construct_dual_state(R,direction,sign,dual)
  controls['construction'] &= all(x[2] for x in ds['checks'])
  controls['cycle'] &= prev.cycle_contains({e:ad.value_matrix(M) for e,M in ds['edges'].items()})
  raw=enable.construct_state(R,direction,sign,mid);reg=enable.source_regression(R,direction,sign,mid,raw);controls['center_regression'] &= bool(reg['pass'])
  dlog=ad.RD(0,0);rawlog=arb(0)
  for k in ds['node_kak'].values(): dlog += 2*k['beta'].sinh().log()
  for k in raw['node_kak'].values(): rawlog += 2*k['beta'].sinh().log()
  rr=[]
  for rho in core.RHOS:
   dm=[];rm=[];add=True
   for e in core.EDGES:
    branch='p' if sig[e[0]]*sig[e[1]]>0 else 'm'
    dM,dok=ad.dfull_toller(ds['edge_kak'][e],rho,branch);rM,rok=core.full_toller(raw['edge_kak'][e],rho,branch)
    dm.append(dM);rm.append(rM);add &= dok and rok
   controls['source_additive'] &= add
   dv=ad.dcontract_all(dm);rv=core.contract_all(rm)
   delta=af(loq-midq).union(af(hiq-midq));vals=ad.centered_channels(rv,dv,delta);L,U,_=core.envelope_bounds(vals)
   controls['finite_local_envelope'] &= bool(L>arb(0) and U.is_finite())
   rr.append({'rho':rho,'dvals':dv,'rvals':rv})
  model[R]={'raw_logH':rawlog,'dlogH':dlog,'rho':rr}
 if not all(controls.values()): raise ArithmeticError(f'local controls failed {controls}')
 return {'loq':loq,'hiq':hiq,'midq':midq,'controls':controls,'model':model}
def evaluate(loq,hiq,depth,direction,sign):
 m=build_local(loq,hiq,direction,sign);snap=_derivative_snapshot(m);delta=af(loq-m['midq']).union(af(hiq-m['midq']));perR={};possible=[]
 for R in R_COHORT:
  q=m['model'][R];h=q['raw_logH']+delta*q['dlogH'].d;rows=[]
  for rr in q['rho']:
   vals=ad.centered_channels(rr['rvals'],rr['dvals'],delta);L,U,p=core.envelope_bounds(vals)
   rows.append({'rho':rr['rho'],'yl':h.lower()+L.log().lower(),'yu':h.upper()+U.log().upper(),'possible':list(p)})
   possible.append({'R':R,'rho':rr['rho'],'indices':list(p)})
  perR[R]=rows
 prs=[];cert=True;maxd=None;mins=None
 for i,rho in enumerate(core.RHOS):
  y6l,y6u=perR[6][i]['yl'],perR[6][i]['yu'];y8l,y8u=perR[8][i]['yl'],perR[8][i]['yu'];y10l,y10u=perR[10][i]['yl'],perR[10][i]['yu'];y12l,y12u=perR[12][i]['yl'],perR[12][i]['yu']
  sl=(y12l-y8u)/4;su=(y12u-y8l)/4;el=(y10l-y6u)/4;eu=(y10u-y6l)/4;du=max(abs(sl-eu),abs(su-el));sok=bool(sl>=FLOOR);dok=bool(du<=TOL);ok=sok and dok;cert &= ok
  maxd=du.upper() if maxd is None or du.upper()>maxd else maxd;mins=sl.lower() if mins is None or sl.lower()<mins else mins
  prs.append({'rho':rho,'slope_floor_satisfied':sok,'drift_within_tolerance':dok,'certified':ok,'S_lower':bf(sl,'lower'),'drift_upper':bf(du,'upper')})
 row={'depth':depth,'amp_lower_q':qt(loq),'amp_upper_q':qt(hiq),'local_mid_q':qt(m['midq']),'validated_local_derivative':True,'scientific_decision_transport':'exact_arb_booleans_float_bounds_display_only','certified':bool(cert),'per_rho':prs,'possible_max':possible,'max_drift_upper':bf(maxd,'upper'),'min_S_lower':bf(mins,'lower')}
 return row,snap
def root_run(k):
 direction,sign=parent.path_spec(0,2)
 if direction!=[1,1,1,-1,-1,-1] or sign!=1: raise RuntimeError('path')
 if R_COHORT!=(6,8,10,12): raise RuntimeError(f'R cohort {R_COHORT}')
 if RHO_COHORT!=(0.35,0.9,1.6,2.7): raise RuntimeError(f'rho cohort {RHO_COHORT}')
 lo,hi=rgate.root_interval(k);stack=[(lo,hi,0,None,None,None)];leaves=[];visited=0;inclusions=[]
 while stack:
  a,b,d,parent_snap,parent_bounds,parent_depth=stack.pop();row,snap=evaluate(a,b,d,direction,sign);visited+=1
  if parent_snap is not None:
   pa,pb=parent_bounds
   inclusions.append(_inclusion_record(snap,parent_snap,a,b,d,pa,pb,parent_depth))
  if row['certified'] or d==MAX_DEPTH: leaves.append(row)
  else:
   m=(a+b)/2;stack.append((m,b,d+1,snap,(a,b),d));stack.append((a,m,d+1,snap,(a,b),d))
 spans=sorted((Fraction(x['amp_lower_q']),Fraction(x['amp_upper_q'])) for x in leaves);cover=bool(spans and spans[0][0]==lo and spans[-1][1]==hi and all(spans[i][1]==spans[i+1][0] for i in range(len(spans)-1)))
 unresolved=[x for x in leaves if not x['certified']]
 return {'gate':GATE,'preregistration_commit':PREREG,'repair_preregistration_commit':REPAIR_PREREG,'parent_terminal_commit':PARENT,'root_box':k,'precision_bits':384,'python_flint':'0.9.0','full_channel_count':243,'channel_pruning_used':False,'max_depth':MAX_DEPTH,'partition_rule':'deterministic_dyadic_midpoint','local_derivative_recomputed_each_visited_node':True,'threshold_exact':'1/20','robust_floor_exact':'1','r_cohort_consumed':list(R_COHORT),'rho_cohort_consumed':list(RHO_COHORT),'componentwise_parent_inclusion_record_count':len(inclusions),'componentwise_parent_inclusion_records':inclusions,'cover_valid':cover,'visited_node_count':visited,'terminal_leaf_count':len(leaves),'unresolved_leaf_count':len(unresolved),'leaves':leaves}
def main():
 p=argparse.ArgumentParser();p.add_argument('--root-box',type=int,choices=ROOTS,required=True);p.add_argument('--out',required=True);a=p.parse_args()
 try:o=root_run(a.root_box)
 except Exception as e:o={'gate':GATE,'preregistration_commit':PREREG,'repair_preregistration_commit':REPAIR_PREREG,'root_box':a.root_box,'invalid':True,'error':repr(e)}
 q=Path(a.out);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in o.items() if k not in ('leaves','componentwise_parent_inclusion_records')},indent=2,sort_keys=True));return 2 if o.get('invalid') else 0
if __name__=='__main__':raise SystemExit(main())
