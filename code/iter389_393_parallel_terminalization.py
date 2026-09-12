#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

RQCP={
    'N':[8,10,12,14,16,18,20,24,28],
    'G':[23.200280752211146,21.809484424122982,21.5409284181087,21.51013837956672,21.50232102803958,21.50115669884191,21.500993416081617,21.500968814791843,21.50096842760798],
    'gap':[0.48633956724666694,0.499214520584097,0.5013796809782525,0.501713727090391,0.5017421496959152,0.5017456279937786,0.501746042954463,0.5017460967618718,0.5017460974407341],
    'prod':[5.487473657582998,5.435259236822587,5.41432102821346,5.414460274027426,5.413105780434489,5.4128877144348015,5.412855561436078,5.412850529035239,5.412850446209202],
}

TERMINAL={
    'BENCHMARKED_COMPLETE_REALIZATION','EQUIVALENCE_CLASS_CLOSED_BY_THEOREM',
    'MERGED_INTO_OTHER_ROW_WITH_EXPLICIT_REDUCTION_MAP','OUTSIDE_PAPER_IV_TARGET_WITH_SCOPE_PROOF'
}

def linfit(x,y):
    n=len(x); sx=sum(x); sy=sum(y); sxx=sum(v*v for v in x); sxy=sum(a*b for a,b in zip(x,y))
    den=n*sxx-sx*sx
    scale=max(abs(n*sxx),abs(sx*sx),1e-300)
    if abs(den) < 1e-14*scale: return None
    a=(sy*sxx-sx*sxy)/den
    b=(n*sxy-sx*sy)/den
    sse=sum((yy-(a+b*xx))**2 for xx,yy in zip(x,y))
    return a,b,sse

def rqcp_fit(observable,nmin):
    ns=[float(n) for n in RQCP['N'] if n>=nmin]
    ys=[float(v) for n,v in zip(RQCP['N'],RQCP[observable]) if n>=nmin]
    if len(ns)<4: raise ValueError('need >=4 points')
    bestp=None; skipped_power=0
    p=0.50
    while p<=14.0000001:
        x=[n**(-p) for n in ns]
        fit=linfit(x,ys)
        if fit is None:
            skipped_power+=1
        else:
            yinf,a,sse=fit
            rec=(sse,p,yinf,a)
            if bestp is None or rec<bestp: bestp=rec
        p+=0.01
    beste=None; skipped_exp=0
    b=0.05
    while b<=2.0000001:
        x=[math.exp(-b*n) for n in ns]
        fit=linfit(x,ys)
        if fit is None:
            skipped_exp+=1
        else:
            yinf,a,sse=fit
            rec=(sse,b,yinf,a)
            if beste is None or rec<beste: beste=rec
        b+=0.005
    if bestp is None or beste is None: raise ValueError('no non-singular extrapolation model')
    sse_p,p,yip,ap=bestp; sse_e,b,yie,ae=beste
    model_spread=abs(yip-yie)/max(abs(yie),1e-30)
    tail_rel=abs(ys[-1]-ys[-2])/max(abs(ys[-1]),1e-30)
    return {
        'mode':'rqcp_fit','iteration':389,'observable':observable,'nmin':nmin,'npoints':len(ns),
        'last_cutoff':int(ns[-1]),'last_value':ys[-1],'last_step_relative_change':tail_rel,
        'power_model':{'form':'y_inf+a/N^p','p':p,'y_inf':yip,'a':ap,'sse':sse_p,'skipped_singular_grid_points':skipped_power},
        'exponential_model':{'form':'y_inf+a*exp(-b*N)','b':b,'y_inf':yie,'a':ae,'sse':sse_e,'skipped_singular_grid_points':skipped_exp},
        'relative_asymptote_model_spread':model_spread,
        'pass':all(math.isfinite(v) for v in [yip,yie,sse_p,sse_e]) and model_spread<0.01,
        'classification':'SCOPED_FINITE_SEQUENCE_EXTRAPOLATION_DIAGNOSTIC',
        'scope_guard':'Finite-cutoff extrapolation is not an infinite-cutoff theorem and does not establish the all-band autonomous RQCP gravity parent.'
    }

def taylor_exp_minus(z,degree):
    s=0.0; term=1.0
    for k in range(degree+1):
        if k==0: term=1.0
        else: term*=(-z)/k
        s+=term
    return s

def nonlocal_domain(degree,zmax):
    ngrid=4001
    max_abs=0.0; max_rel=0.0; first_1e3=None; first_1e2=None
    for i in range(ngrid):
        z=zmax*i/(ngrid-1)
        exact=math.exp(-z); approx=taylor_exp_minus(z,degree)
        ae=abs(approx-exact); re=ae/max(abs(exact),1e-300)
        max_abs=max(max_abs,ae); max_rel=max(max_rel,re)
        if first_1e3 is None and re>1e-3: first_1e3=z
        if first_1e2 is None and re>1e-2: first_1e2=z
    endpoint_exact=math.exp(-zmax); endpoint_approx=taylor_exp_minus(zmax,degree)
    return {
        'mode':'nonlocal_domain','iteration':390,'degree':degree,'zmax':zmax,'grid_points':ngrid,
        'comparator':'finite-local Taylor polynomial to exp(-z) about z=0',
        'max_abs_error':max_abs,'max_relative_error':max_rel,
        'endpoint_exact':endpoint_exact,'endpoint_approx':endpoint_approx,
        'first_z_relative_error_gt_1e-3':first_1e3,
        'first_z_relative_error_gt_1e-2':first_1e2,
        'pass':math.isfinite(max_rel),
        'classification':'PASS_SCOPED_FINITE_DOMAIN_LOCAL_APPROXIMATION_MAP',
        'scope_guard':'Approximation quality on a finite z-domain is not exact functional equivalence and is not a source-normalized physical graviton amplitude comparison.'
    }

def higher_derivative_branch():
    bm=json.loads((ROOT/'paper_iv/HIGHER_DERIVATIVE_QUANTIZATION_BRANCH_MAP_2026-09-10.json').read_text())
    iho=json.loads((ROOT/'paper_iv/IHO_DQFT_COSMOLOGY_SOURCE_AUTHORITY_ITER370_373.json').read_text())
    ids=[b['id'] for b in bm['material_branches']]
    explicit=any(('IHO' in x or 'DQFT' in x or 'DIRECT_SUM' in x) for x in ids)
    required=list(bm['minimum_payload'])
    present={
        'branch_identifier_and_fixed_action': bool(iho.get('branch')),
        'normalized_physical_observable': bool(iho.get('source_defined_observable')),
        'IR_GR_map': bool(iho.get('source_defined_observable',{}).get('same_domain_baseline')),
        'same_domain_comparators': bool(iho.get('source_defined_observable',{}).get('same_domain_baseline')),
        'error_remainder_scheme_ledger': bool(iho.get('error_object')),
    }
    missing=[x for x in required if not present.get(x,False)]
    return {
        'mode':'higher_derivative_branch','iteration':391,
        'iter187_material_branch_count':len(ids),'iter187_branch_ids':ids,
        'source_defined_new_realization_label':iho.get('branch'),
        'iho_dqft_explicitly_represented_in_iter187_branch_ids':explicit,
        'minimum_payload_total':len(required),'repo_authority_payload_items_present':sum(1 for x in required if present.get(x,False)),
        'present_payload_items':[x for x in required if present.get(x,False)],
        'missing_payload_items':missing,
        'classification':'BRANCH_MAP_REOPEN_REQUIRED_FOR_MATERIAL_CLASSIFICATION' if not explicit else 'BRANCH_ALREADY_EXPLICITLY_MAPPED',
        'family_terminal':False,'d7_promotion_authorized':False,'pass':True,
        'scope_guard':'The post-Iter187 IHO/DQFT realization is source-defined in the repository. Absence from the old five branch identifiers requires classification review; it does not by itself prove material independence or terminality.'
    }

def coverage():
    cov=json.loads((ROOT/'protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json').read_text())
    rows=cov['tier1_required_rows']
    terminal=[r['id'] for r in rows if r['coverage_status'] in TERMINAL]
    nonterminal=[r['id'] for r in rows if r['coverage_status'] not in TERMINAL]
    return {
        'mode':'coverage','iteration':392,'tier1_total':len(rows),'terminal_count':len(terminal),'nonterminal_count':len(nonterminal),
        'terminal_rows':terminal,'nonterminal_rows':nonterminal,'tier2_unresolved':len([x for x in cov.get('tier2_resolution_watchlist',[]) if x.get('status')=='UNRESOLVED_CLASSIFICATION']),
        'D2_closed':len(nonterminal)==0,'D4_closed':False,'D7_authorized':False,'pass':len(rows)==15 and len(terminal)==1,
        'classification':'PASS_CURRENT_15_ROW_DENOMINATOR_COHERENCE'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',required=True,choices=['rqcp','nonlocal','higher','coverage']); ap.add_argument('--observable',choices=['G','gap','prod']); ap.add_argument('--nmin',type=int); ap.add_argument('--degree',type=int); ap.add_argument('--zmax',type=float); ap.add_argument('--output',required=True)
    a=ap.parse_args()
    if a.mode=='rqcp': out=rqcp_fit(a.observable,a.nmin)
    elif a.mode=='nonlocal': out=nonlocal_domain(a.degree,a.zmax)
    elif a.mode=='higher': out=higher_derivative_branch()
    else: out=coverage()
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))
    if not out.get('pass',False): raise SystemExit(2)
if __name__=='__main__': main()
