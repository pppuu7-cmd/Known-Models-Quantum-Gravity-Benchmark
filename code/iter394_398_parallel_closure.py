#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

RQCP={
 'N':[8,10,12,14,16,18,20,24,28],
 'G':[23.200280752211146,21.809484424122982,21.5409284181087,21.51013837956672,21.50232102803958,21.50115669884191,21.500993416081617,21.500968814791843,21.50096842760798],
 'gap':[0.48633956724666694,0.499214520584097,0.5013796809782525,0.501713727090391,0.5017421496959152,0.5017456279937786,0.501746042954463,0.5017460967618718,0.5017460974407341],
 'prod':[5.487473657582998,5.435259236822587,5.41432102821346,5.414460274027426,5.413105780434489,5.4128877144348015,5.412855561436078,5.412850529035239,5.412850446209202]
}

IHO_FIELDS={
 'branch_identifier_and_fixed_action':('PRESENT_SOURCE_DEFINED','The source fixes the positive-Weyl-squared quadratic-gravity realization and the IHO/DQFT branch identifier.'),
 'dressed_pole_locations_and_residues':('PARTIAL_OPEN','Spacelike pole location and PV distribution are source-defined/recomputed, but a dressed pole-and-residue ledger over the terminal domain is not frozen.'),
 'physical_Hilbert_space_and_asymptotic_state_rule':('PRESENT_SOURCE_DEFINED','DQFT split Hilbert space and no-asymptotic-IHO-state rule are explicit in current source authority.'),
 'same_prescription_unitarity_certificate':('PRESENT_SOURCE_THEOREM','Current source gives a Cutkosky/optical-theorem unitarity analysis for the same PV/DQFT realization; KMQGB does not claim an independent all-loop reproof.'),
 'declared_causality_or_controlled_nonlocal_replacement':('PARTIAL_OPEN','No physical timelike pinch and local UV counterterms are source-controlled, but a full causal observable/domain certificate is not frozen.'),
 'normalized_physical_observable':('PRESENT_SCOPED','Tensor-to-scalar ratio and parity-asymmetry observable layers are source-defined and machine audited.'),
 'IR_GR_map':('PARTIAL_OPEN','The beta=0 Starobinsky same-formula limit is explicit for inflation, but it is not a complete IR GR transport certificate for the full branch.'),
 'same_domain_comparators':('PRESENT_SCOPED','Starobinsky beta=0 and parity-symmetric zero-asymmetry baselines are present on their declared domains.'),
 'error_remainder_scheme_ledger':('PARTIAL_OPEN','Analytic propagated error object exists, but source-grounded covariance/likelihood and full remainder ledger are incomplete.'),
 'remaining_material_branch_disposition_map':('PARTIAL_REOPEN_REQUIRED','IHO/DQFT is explicitly distinct from fakeon, Lee-Wick, PT and Euclidean-OS source classes, but the historical five-branch map must be versioned and the bare/indefinite-metric relation plus exhaustion guard frozen.')
}

def dump(out,path):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True));
 if not out.get('pass',False): raise SystemExit(2)

def iho_field(field):
 if field not in IHO_FIELDS: raise ValueError(field)
 status,note=IHO_FIELDS[field]
 full=status.startswith('PRESENT_')
 return {'mode':'iho_payload','iteration':394,'field':field,'status':status,'full_slot_satisfied':full,'note':note,'family_terminal':False,'d7_promotion_authorized':False,'pass':True}

def nonlocal_case(case):
 auth=json.loads((ROOT/'paper_iv/NONLOCAL_TREE_EQUIVALENCE_SOURCE_AUTHORITY_ITER395.json').read_text())
 theorem=auth['theorem_domain']
 if case=='analytic_eom_tree':
  applies=True; residual='EXACT_ZERO_BY_THEOREM'; reason='Declared analytic E_i F_ij E_j action class, on-shell tree S-matrix, no material Riemann^2 branch.'
 elif case=='riemann2_branch':
  applies=False; residual='UNDEFINED'; reason='Source explicitly warns Riemann^2-form-factor branch does not automatically inherit the theorem.'
 elif case=='loop_level':
  applies=False; residual='UNDEFINED'; reason='Tree theorem cannot be promoted to generic loop amplitudes.'
 elif case=='off_shell_shape':
  applies=False; residual='NOT_A_TREE_S_MATRIX_RESIDUAL'; reason='Bare/off-shell form-factor shape is not the on-shell theorem observable.'
 else: raise ValueError(case)
 return {'mode':'nonlocal_theorem_scope','iteration':395,'case':case,'theorem_applies':applies,'comparator_residual':residual,'reason':reason,'subfamily_terminal_candidate':case=='analytic_eom_tree','family_terminal':False,'pass':True}

def linfit(x,y):
 n=len(x); sx=sum(x); sy=sum(y); sxx=sum(v*v for v in x); sxy=sum(a*b for a,b in zip(x,y)); den=n*sxx-sx*sx
 scale=max(abs(n*sxx),abs(sx*sx),1e-300)
 if abs(den)<1e-14*scale: return None
 a=(sy*sxx-sx*sxy)/den; b=(n*sxy-sx*sy)/den
 sse=sum((yy-(a+b*xx))**2 for xx,yy in zip(x,y))
 return a,b,sse

def best_fit(ns,ys,kind):
 best=None
 if kind=='power':
  grid=[0.5+0.01*i for i in range(1351)]
  for q in grid:
   fit=linfit([n**(-q) for n in ns],ys)
   if fit:
    yinf,a,sse=fit; rec=(sse,q,yinf,a)
    if best is None or rec<best: best=rec
 elif kind=='exp':
  grid=[0.025+0.0025*i for i in range(791)]
  for q in grid:
   fit=linfit([math.exp(-q*n) for n in ns],ys)
   if fit:
    yinf,a,sse=fit; rec=(sse,q,yinf,a)
    if best is None or rec<best: best=rec
 else: raise ValueError(kind)
 if best is None: raise ValueError('no fit')
 return best

def rqcp_holdout(obs,train_max):
 Ns=RQCP['N']; Ys=RQCP[obs]; idx=Ns.index(train_max)
 if idx+1>=len(Ns): raise ValueError('no holdout')
 targetN=Ns[idx+1]; target=Ys[idx+1]
 # Use the high-cutoff tail but retain at least five training points.
 start=max(0,idx-5)
 ns=[float(x) for x in Ns[start:idx+1]]; ys=[float(x) for x in Ys[start:idx+1]]
 preds={}
 for kind in ('power','exp'):
  sse,q,yinf,a=best_fit(ns,ys,kind)
  x=targetN**(-q) if kind=='power' else math.exp(-q*targetN)
  pred=yinf+a*x
  preds[kind]={'shape_parameter':q,'y_inf':yinf,'train_sse':sse,'prediction':pred,'relative_holdout_error':abs(pred-target)/max(abs(target),1e-300)}
 disagreement=abs(preds['power']['prediction']-preds['exp']['prediction'])/max(abs(target),1e-300)
 worst=max(v['relative_holdout_error'] for v in preds.values())
 return {'mode':'rqcp_holdout','iteration':396,'observable':obs,'train_max':train_max,'train_cutoffs':[int(x) for x in ns],'target_cutoff':targetN,'target_value':target,'models':preds,'relative_model_prediction_disagreement':disagreement,'worst_relative_holdout_error':worst,'pass':math.isfinite(worst) and worst<0.02,'classification':'PASS_SCOPED_CUTOFF_HOLDOUT_PREDICTION' if worst<0.02 else 'FAIL_SCOPED_CUTOFF_HOLDOUT_PREDICTION','scope_guard':'Finite holdout predictivity is evidence of numerical convergence only; it is not a proof of controlled cutoff removal or all-band parent autonomy.'}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--mode',required=True,choices=['iho','nonlocal','rqcp']); ap.add_argument('--field'); ap.add_argument('--case'); ap.add_argument('--observable'); ap.add_argument('--train-max',type=int); ap.add_argument('--output',required=True); a=ap.parse_args()
 if a.mode=='iho': out=iho_field(a.field)
 elif a.mode=='nonlocal': out=nonlocal_case(a.case)
 else: out=rqcp_holdout(a.observable,a.train_max)
 dump(out,a.output)
if __name__=='__main__': main()
