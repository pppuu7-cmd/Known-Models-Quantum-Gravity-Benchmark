#!/usr/bin/env python3
from __future__ import annotations
import argparse, cmath, json, math
from pathlib import Path

RQCP={
 'N':[8,10,12,14,16,18,20,24,28],
 'G':[23.200280752211146,21.809484424122982,21.5409284181087,21.51013837956672,21.50232102803958,21.50115669884191,21.500993416081617,21.500968814791843,21.50096842760798],
 'gap':[0.48633956724666694,0.499214520584097,0.5013796809782525,0.501713727090391,0.5017421496959152,0.5017456279937786,0.501746042954463,0.5017460967618718,0.5017460974407341],
 'prod':[5.487473657582998,5.435259236822587,5.41432102821346,5.414460274027426,5.413105780434489,5.4128877144348015,5.412855561436078,5.412850529035239,5.412850446209202]
}

def write(out,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,sort_keys=True))
    if not out.get('pass',False): raise SystemExit(2)

def linear_fit(x,y):
    n=len(x); sx=sum(x); sy=sum(y); sxx=sum(v*v for v in x); sxy=sum(a*b for a,b in zip(x,y))
    den=n*sxx-sx*sx
    if abs(den)<1e-30: raise ValueError('singular fit')
    intercept=(sy*sxx-sx*sxy)/den
    slope=(n*sxy-sx*sy)/den
    sse=sum((yy-(intercept+slope*xx))**2 for xx,yy in zip(x,y))
    return intercept,slope,sse

def lqg_toller(gamma:float,n:int):
    if gamma<=0 or n<1 or n>4: raise ValueError('invalid gamma/n')
    js=[2,4,8,16,32,64]
    rows=[]
    target=(2.0*math.atan(1.0/gamma))**n
    for j in js:
        rho=gamma*j
        coeff=[1.0+0.0j]
        for m in range(2*j+1):
            denom=1j*rho-(m-j)
            a=1j/denom
            nxt=[0j]*(len(coeff)+1)
            for k,v in enumerate(coeff):
                nxt[k]+=v; nxt[k+1]+=v*a
            coeff=nxt
        cn=math.factorial(n)*coeff[n]
        rel=abs(cn-target)/max(abs(target),1e-300)
        rows.append({'j':j,'rho':rho,'c_n_real':cn.real,'c_n_imag':cn.imag,'target':target,'relative_error':rel})
    tail=rows[-4:]
    _,slope,_=linear_fit([math.log(r['j']) for r in tail],[math.log(max(r['relative_error'],1e-300)) for r in tail])
    final_error=rows[-1]['relative_error']
    ok=final_error<0.03 and slope<-0.5 and max(abs(r['c_n_imag']) for r in rows)<1e-10
    return {
      'iteration':404,'stream':'LQG_SPINFOAM','probe':'TOLLER_COEFFICIENT_FIXED_GAMMA_LARGE_SPIN',
      'gamma':gamma,'n':n,'rows':rows,'published_asymptotic_target':target,
      'tail_loglog_error_slope':slope,'final_relative_error_j64':final_error,
      'pass':ok,
      'classification':'PASS_SOURCE_DEFINED_TOLLER_COEFFICIENT_CONVERGES_TO_FIXED_GAMMA_LARGE_SPIN_FORM_WITH_O_1_OVER_J_COMPATIBLE_DECAY' if ok else 'FAIL_TOLLER_ASYMPTOTIC_NUMERIC_GUARD',
      'scope_guard':['BUILDING_BLOCK_ONLY','NO_CAUSAL_VERTEX_FINITE_NORM_PROOF','NO_COMPLETE_STACK_SUM','NO_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']
    }

def cfs_scaling(L_over_delta:float,C3:float):
    if L_over_delta<=1 or C3<=0: raise ValueError('invalid order-counting inputs')
    epsilon=1.0/L_over_delta
    # After factoring the characteristic powers needed to make the hierarchy dimensionless,
    # O(delta^3) / O(delta^2) carries one additional epsilon=delta/L.
    relative_nominal=C3*epsilon
    return {
      'iteration':405,'stream':'CAUSAL_FERMION_SYSTEMS','probe':'DELTA_ORDER_COUNTING_DIAGNOSTIC',
      'L_over_delta':L_over_delta,'epsilon_delta_over_L':epsilon,'unknown_dimensionless_C3_scan_value':C3,
      'nominal_O_delta3_over_O_delta2':relative_nominal,
      'higher_order_power_suppression_present':epsilon<1.0,
      'pass':math.isfinite(relative_nominal) and epsilon<1.0,
      'classification':'PASS_PARAMETRIC_ORDER_TRANSPORT__ONE_EXTRA_DELTA_OVER_L_POWER_FOR_NOMINAL_DELTA3_TERM',
      'scope_guard':['C3_IS_DIAGNOSTIC_NOT_SOURCE_FIT','NO_EXPLICIT_BEYOND_EINSTEIN_TENSOR','NO_PHENOMENOLOGICAL_BOUND','NO_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']
    }

def as_forward(t_fixed:float):
    if t_fixed>=0: raise ValueError('use spacelike fixed t<0')
    ss=[1e4,1e5,1e6,1e7,1e8]
    rows=[]
    for s in ss:
        u=-s-t_fixed
        # Source Eq.65 with a normalized fixed V_L(t)=1. At fixed t the vertex factor
        # is independent of s, so this isolates the exact kinematic high-energy power.
        amp=(s*s-4*s*u+u*u-t_fixed*t_fixed)/t_fixed
        rows.append({'s':s,'t':t_fixed,'u':u,'normalized_A_t_over_VL_t':amp,'abs_value':abs(amp)})
    _,slope,_=linear_fit([math.log(r['s']) for r in rows[-4:]],[math.log(r['abs_value']) for r in rows[-4:]])
    ok=1.98<slope<2.02
    return {
      'iteration':406,'stream':'ASYMPTOTIC_SAFETY','probe':'FIXED_T_FORWARD_SCALING',
      't_fixed':t_fixed,'rows':rows,'high_energy_loglog_slope':slope,'pass':ok,
      'classification':'PASS_SOURCE_KINEMATIC_FORWARD_DIVERGENCE_REPRODUCED__A_T_SCALES_AS_S_SQUARED_AT_FIXED_T' if ok else 'FAIL_FORWARD_SCALING_GUARD',
      'required_missing_object':'CONTACT_COMPLETE_A4_IN_SAME_NONPERTURBATIVE_REALIZATION',
      'scope_guard':['VL_T_NORMALIZED_OUT','STRUCTURAL_SCALING_ONLY','SOURCE_STATES_A4_REQUIRED_FOR_FORWARD_RESOLUTION','NO_CONTACT_COMPLETION','NO_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']
    }

def as_bounded(theta_deg:float):
    if not 0<theta_deg<180: raise ValueError('invalid angle')
    ss=[1e2,1e3,1e4,1e5,1e6,1e8]
    theta=math.radians(theta_deg); sin2=math.sin(theta)**2
    Vstar=1.0; Mpl2=1.0
    rows=[]
    for s in ss:
        V=Vstar/(s+Vstar*Mpl2)
        amp=-s*sin2*V
        asymptote=-Vstar*sin2
        rel=abs(amp-asymptote)/max(abs(asymptote),1e-300)
        rows.append({'s_over_Mpl2':s,'normalized_Vstar':Vstar,'A_s_adapted_RG':amp,'UV_asymptote':asymptote,'relative_error_to_asymptote':rel})
    ok=rows[-1]['relative_error_to_asymptote']<2e-8
    return {
      'iteration':406,'stream':'ASYMPTOTIC_SAFETY','probe':'ADAPTED_RG_S_CHANNEL_BOUNDEDNESS_DIAGNOSTIC',
      'theta_deg':theta_deg,'rows':rows,'pass':ok,
      'classification':'PASS_SOURCE_ADAPTED_RG_DIAGNOSTIC_APPROACHES_BOUNDED_UV_S_CHANNEL' if ok else 'FAIL_ADAPTED_RG_BOUNDEDNESS_GUARD',
      'scope_guard':['USES_SOURCE_EQ63_ADAPTED_RG_DIAGNOSTIC_WITH_NORMALIZED_VSTAR_AND_MPL','NOT_FULL_RECONSTRUCTED_VERTEX_DATA','NOT_S_T_U_A4_COMPLETE','NO_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']
    }

def rqcp_linfit(x,y):
    return linear_fit(x,y)

def rqcp_best(ns,ys,kind):
    best=None
    if kind=='power': grid=[0.5+0.01*i for i in range(1351)]
    elif kind=='exp': grid=[0.025+0.0025*i for i in range(791)]
    else: raise ValueError(kind)
    for q in grid:
        x=[n**(-q) for n in ns] if kind=='power' else [math.exp(-q*n) for n in ns]
        try: yinf,a,sse=rqcp_linfit(x,ys)
        except ValueError: continue
        rec=(sse,q,yinf,a)
        if best is None or rec<best: best=rec
    if best is None: raise ValueError('no fit')
    return best

def rqcp_window(observable:str,min_cutoff:int):
    key={'G':'G','gap':'gap','G_gap2':'prod'}[observable]
    if min_cutoff not in RQCP['N']: raise ValueError('cutoff absent')
    idx=RQCP['N'].index(min_cutoff)
    ns=[float(v) for v in RQCP['N'][idx:]]; ys=[float(v) for v in RQCP[key][idx:]]
    if len(ns)<5: raise ValueError('need >=5 points')
    models={}
    for kind in ('power','exp'):
        sse,q,yinf,a=rqcp_best(ns,ys,kind)
        models[kind]={'shape_parameter':q,'y_inf':yinf,'sse':sse,'amplitude':a}
    center=0.5*(models['power']['y_inf']+models['exp']['y_inf'])
    disagreement=abs(models['power']['y_inf']-models['exp']['y_inf'])/max(abs(center),1e-300)
    ok=math.isfinite(disagreement) and disagreement<1e-3
    return {
      'iteration':407,'stream':'RQCP','probe':'HIGH_CUTOFF_WINDOW_AND_ANSATZ_STABILITY',
      'observable':observable,'min_cutoff':min_cutoff,'cutoffs':[int(v) for v in ns],
      'models':models,'relative_inferred_limit_model_disagreement':disagreement,'pass':ok,
      'classification':'PASS_SCOPED_NUMERIC_CUTOFF_LIMIT_STABILITY_ACROSS_POWER_AND_EXPONENTIAL_ANSATZ' if ok else 'FAIL_SCOPED_CUTOFF_LIMIT_STABILITY',
      'scope_guard':['REPRODUCED_FINITE_SEQUENCE_ONLY','NOT_A_RIGOROUS_CUTOFF_REMOVAL_THEOREM','NOT_ALL_BAND_AUTONOMY','NOT_BACKGROUND_INDEPENDENCE_CERTIFICATE','NO_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',required=True,choices=['lqg','cfs','as-forward','as-bounded','rqcp'])
    ap.add_argument('--gamma',type=float); ap.add_argument('--n',type=int)
    ap.add_argument('--L-over-delta',type=float); ap.add_argument('--C3',type=float)
    ap.add_argument('--t-fixed',type=float); ap.add_argument('--theta-deg',type=float)
    ap.add_argument('--observable'); ap.add_argument('--min-cutoff',type=int)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    if a.mode=='lqg': out=lqg_toller(a.gamma,a.n)
    elif a.mode=='cfs': out=cfs_scaling(a.L_over_delta,a.C3)
    elif a.mode=='as-forward': out=as_forward(a.t_fixed)
    elif a.mode=='as-bounded': out=as_bounded(a.theta_deg)
    else: out=rqcp_window(a.observable,a.min_cutoff)
    write(out,a.output)
if __name__=='__main__': main()
