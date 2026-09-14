#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np
import mpmath as mp

import iter482_common_node_su2_control as ctrl
import iter484_source_toller_kak_one_edge as src

mp.mp.dps = 90

PANELS = {
    'T0': [(0,0,0),(1,2,3),(-2,1,4),(3,-1,2),(2,4,-1)],
    'T1': [(0,0,0),(2,-1,1),(1,3,-2),(-3,2,2),(4,1,3)],
    'T2': [(0,0,0),(1,-2,4),(-1,3,2),(4,2,-3),(-3,-1,1)],
}
RHOS = (7, 8)
MS = (-1,0,1)
CHANNELS = list(itertools.product(range(3), repeat=5))
WITNESS_TOL = 1e-12
AXIAL_THETA = 0.371
T_COARSE = 1e-3
T_FINE = 5e-4
FINE_ERR_TOL = 5e-3
REFINE_FACTOR = 0.75


def coeff_src(j,m,rho,plus=True):
    """Exact Iter477/479 hypergeometric coefficient C_m^(src)."""
    jx=mp.mpf(j); mx=mp.mpf(m); rx=mp.mpf(rho); ii=mp.j; N=2*j+1
    if plus:
        a=jx+mx+1; b=jx+1-ii*rx; c=1+mx-ii*rx
        pref=mp.gamma(2*jx+2)*mp.gamma(ii*rx-mx)/(mp.gamma(jx-mx+1)*mp.gamma(jx+1+ii*rx))
    else:
        a=jx-mx+1; b=jx+1+ii*rx; c=1-mx+ii*rx
        pref=mp.gamma(2*jx+2)*mp.gamma(-ii*rx+mx)/(mp.gamma(jx+mx+1)*mp.gamma(jx+1-ii*rx))
    return pref*mp.gamma(c)*mp.gamma(N)/(mp.gamma(a)*mp.gamma(b))


def beta_coeff(m,rho,plus):
    # Iter477: t_m(beta)*(1-exp(-2 beta))^3/C_m -> 1.
    # Therefore t_m(beta) ~ (C_m/8)*beta^-3 for j=1.
    return complex(coeff_src(1,m,rho,plus) / mp.mpf(8))


def ry(theta):
    c=math.cos(theta/2.0); s=math.sin(theta/2.0)
    return np.array([[c,-s],[s,c]],dtype=np.complex128)


def section_from_vec(v):
    v=np.asarray(v,dtype=float); r=float(np.linalg.norm(v))
    if r==0.0:
        return np.eye(2,dtype=np.complex128)
    n=v/r
    theta=math.acos(max(-1.0,min(1.0,float(n[2]))))
    phi=math.atan2(float(n[1]),float(n[0]))
    return src.rz(phi) @ ry(theta)


def relmax(A,B):
    den=max(src.maxabs(B),1e-300)
    return src.maxabs(A-B)/den


def fro_rel(A,B):
    den=max(float(np.linalg.norm(B)),1e-300)
    return float(np.linalg.norm(A-B))/den


def geometry(panel,scale=1.0,translation=None):
    trans=np.zeros(3,dtype=float) if translation is None else np.asarray(translation,dtype=float)
    vs=[scale*np.asarray(v,dtype=float)+trans for v in PANELS[panel]]
    data=[]; cycle=0.0; min_r=float('inf')
    for e in ctrl.EDGES:
        a,b=e; w=vs[a]-vs[b]; r=float(np.linalg.norm(w)); min_r=min(min_r,r)
        data.append((e,w,r,w/r if r>0 else np.zeros(3)))
    for a,b,c in itertools.combinations(range(5),3):
        wab=vs[a]-vs[b]; wbc=vs[b]-vs[c]; wac=vs[a]-vs[c]
        cycle=max(cycle,float(np.max(np.abs(wab+wbc-wac))))
    return vs,data,min_r,cycle


def leading_mats(panel,causal,rho,scale=1.0,translation=None,axial=0.0):
    sig=ctrl.SIGMAS[causal]
    vs,data,min_r,cycle=geometry(panel,scale=scale,translation=translation)
    mats=[]; coeff_abs=[]; su2_res=0.0; su2_det=0.0; spin1_unit=0.0; spin1_det=0.0
    coeff_ok=True
    for (a,b),w,r,n in data:
        plus=bool(sig[a]*sig[b]>0)
        cs=[]
        for m in MS:
            csrc=coeff_src(1,m,rho,plus); B=csrc/mp.mpf(8)
            finite=bool(mp.isfinite(mp.re(csrc)) and mp.isfinite(mp.im(csrc)) and mp.isfinite(mp.re(B)) and mp.isfinite(mp.im(B)))
            nz=bool(abs(csrc)>mp.mpf('1e-70') and abs(B)>mp.mpf('1e-70'))
            coeff_ok=coeff_ok and finite and nz
            coeff_abs.append(float(abs(B))); cs.append(complex(B))
        U=section_from_vec(w)
        if axial:
            U=U@src.rz(axial)
        uu,dd=src.su2_metrics(U); su2_res=max(su2_res,uu); su2_det=max(su2_det,dd)
        D=src.spin1(U); I3=np.eye(3,dtype=np.complex128)
        spin1_unit=max(spin1_unit,src.maxabs(D.conj().T@D-I3)); spin1_det=max(spin1_det,float(abs(np.linalg.det(D)-1)))
        L=(r**-3)*(D@np.diag(cs)@D.conj().T)
        mats.append(L)
    return {
        'vs':vs,'data':data,'mats':mats,'min_r':min_r,'cycle':cycle,
        'coeff_ok':bool(coeff_ok),'min_coeff_abs':min(coeff_abs) if coeff_abs else 0.0,
        'su2_unitarity':su2_res,'su2_det':su2_det,'spin1_unitarity':spin1_unit,'spin1_det':spin1_det,
    }


def finite_nodes(panel,t):
    gs=[]
    for v0 in PANELS[panel]:
        v=np.asarray(v0,dtype=float); r=float(np.linalg.norm(v))
        if r==0.0:
            gs.append(np.eye(2,dtype=np.complex128)); continue
        U=section_from_vec(v)
        gs.append(U@src.boost(t*r)@U.conj().T)
    return gs


def finite_t_errors(panel,causal,rho,leading,t):
    sig=ctrl.SIGMAS[causal]; gs=finite_nodes(panel,t); errs=[]; beta_ratio=[]; recmax=0.0
    for ei,(a,b) in enumerate(ctrl.EDGES):
        h=np.linalg.inv(gs[b])@gs[a]
        U1,beta,U2,A=src.kak(h)
        recmax=max(recmax,src.maxabs(U1@A@U2-h))
        _,Tp,Tm=src.full_from_kak(U1,beta,U2,mp.mpf(rho))
        M=Tp if sig[a]*sig[b]>0 else Tm
        target=leading[ei]
        errs.append(fro_rel((t**3)*M,target))
        r=float(np.linalg.norm(np.asarray(PANELS[panel][a],dtype=float)-np.asarray(PANELS[panel][b],dtype=float)))
        beta_ratio.append(beta/(t*r))
    return {'errors':errs,'max_error':max(errs),'min_beta_ratio':min(beta_ratio),'max_beta_ratio':max(beta_ratio),'kak_reconstruction_max':recmax}


def contraction_values(ts,path,mats):
    return np.asarray([ctrl.contract(ch,ts,mats,path) for ch in CHANNELS],dtype=np.complex128)


def normalized_ratios(vals,mats):
    scale=float(np.prod([src.maxabs(M) for M in mats]))
    if not np.isfinite(scale) or scale<=0:
        raise FloatingPointError('invalid leading edge scale')
    return np.abs(vals)/scale,scale


def evaluate(panel,causal,rho):
    rho=int(rho); ts=[ctrl.intertwiner(i) for i in range(3)]; int_ok,gram=ctrl.tensor_controls(ts); path=ctrl.contraction_path(ts)
    base=leading_mats(panel,causal,rho)
    mats=base['mats']; vals=contraction_values(ts,path,mats); ratios,scale=normalized_ratios(vals,mats)
    finite=bool(np.all(np.isfinite(ratios)))
    imax=int(np.argmax(ratios)); max_ratio=float(ratios[imax]); nonzero=int(np.count_nonzero(ratios>WITNESS_TOL))

    axial=leading_mats(panel,causal,rho,axial=AXIAL_THETA)
    axial_res=max(relmax(A,B) for A,B in zip(axial['mats'],mats))

    translated=leading_mats(panel,causal,rho,translation=(2,-3,5))
    translation_res=max(relmax(A,B) for A,B in zip(translated['mats'],mats))

    doubled=leading_mats(panel,causal,rho,scale=2.0)
    edge_scale_res=max(relmax(A,B/8.0) for A,B in zip(doubled['mats'],mats))
    vals2=contraction_values(ts,path,doubled['mats']); ratios2,scale2=normalized_ratios(vals2,doubled['mats'])
    expected_vals=vals*(2.0**-30)
    contraction_scale_res=float(np.max(np.abs(vals2-expected_vals))/max(float(np.max(np.abs(expected_vals))),1e-300))
    ratio_scale_res=float(np.max(np.abs(ratios2-ratios))/max(float(np.max(ratios)),1e-300))

    coarse=finite_t_errors(panel,causal,rho,mats,T_COARSE)
    fine=finite_t_errors(panel,causal,rho,mats,T_FINE)
    refinement=all(f<=REFINE_FACTOR*c+1e-10 for c,f in zip(coarse['errors'],fine['errors']))

    rts=[T[::-1,::-1,::-1,::-1].copy() for T in ts]
    rmats=[M[::-1,::-1].copy() for M in mats]
    rvals=contraction_values(rts,path,rmats)
    s0=np.sort(np.abs(vals)); s1=np.sort(np.abs(rvals)); reindex=float(np.max(np.abs(s0-s1))/max(float(np.max(s0)),float(np.max(s1)),1e-300))

    zmats=[M.copy() for M in mats]; zmats[0]=np.zeros((3,3),dtype=np.complex128)
    zvals=contraction_values(ts,path,zmats); zero_norm=float(np.max(np.abs(zvals))/max(scale,1e-300))

    checks={
      'source_coefficients_finite_nonzero': bool(base['coeff_ok']),
      'tangent_geometry': bool(base['min_r']>0 and base['cycle']<1e-14),
      'su2_section_and_spin1': bool(base['su2_unitarity']<1e-12 and base['su2_det']<1e-12 and base['spin1_unitarity']<1e-12 and base['spin1_det']<1e-12),
      'axial_section_invariance': bool(axial_res<1e-11),
      'common_translation_invariance': bool(translation_res<1e-12),
      'scale_homogeneity': bool(edge_scale_res<1e-12 and contraction_scale_res<1e-10 and ratio_scale_res<1e-10),
      'finite_t_source_regression': bool(fine['max_error']<FINE_ERR_TOL and refinement and coarse['kak_reconstruction_max']<1e-10 and fine['kak_reconstruction_max']<1e-10),
      'intertwiner_controls': bool(int_ok and gram<1e-12),
      'magnetic_reindex_control': bool(reindex<1e-10),
      'zero_edge_negative_control': bool(zero_norm<1e-14),
      'finite_normalized_contraction': finite,
    }
    valid=bool(all(checks.values()))
    if not valid:
        cls='BLOCKED_OR_INFRASTRUCTURE_ITER504'; passed=False
    elif max_ratio>WITNESS_TOL:
        cls='ITER504_FIXED_CAUSAL_K5_FULL_COLLISION_LEADING_CONTRACTION_SURVIVES_QUALIFIED_SCOPED'; passed=True
    else:
        cls='SCIENTIFIC_FAIL_ITER504_UNIFORM_FROZEN_FULL_COLLISION_LEADING_SURVIVAL'; passed=False
    return {
      'iteration':504,'lane':f'{panel}-{causal}-rho{rho}','panel':panel,'causal':causal,'rho':rho,
      'valid':valid,'pass':passed,'classification':cls,'checks':checks,
      'max_ratio':max_ratio,'max_channel':list(CHANNELS[imax]),'channel_00000_ratio':float(ratios[0]),
      'nonzero_witnesses_gt_1e-12':nonzero,'total_channels':243,'edge_scale_product':scale,
      'min_edge_distance':base['min_r'],'tangent_cycle_residual':base['cycle'],'min_beta_leading_coefficient_abs':base['min_coeff_abs'],
      'su2_unitarity_residual':base['su2_unitarity'],'su2_det_residual':base['su2_det'],'spin1_unitarity_residual':base['spin1_unitarity'],'spin1_det_residual':base['spin1_det'],
      'axial_section_relative_residual':axial_res,'translation_relative_residual':translation_res,
      'edge_scale_homogeneity_relative_residual':edge_scale_res,'contraction_scale_homogeneity_relative_residual':contraction_scale_res,'ratio_scale_invariance_relative_residual':ratio_scale_res,
      'finite_t_coarse_max_relative_error':coarse['max_error'],'finite_t_fine_max_relative_error':fine['max_error'],'finite_t_refinement_all':bool(refinement),
      'finite_t_coarse_beta_ratio_range':[coarse['min_beta_ratio'],coarse['max_beta_ratio']],
      'finite_t_fine_beta_ratio_range':[fine['min_beta_ratio'],fine['max_beta_ratio']],
      'finite_t_kak_reconstruction_max':max(coarse['kak_reconstruction_max'],fine['kak_reconstruction_max']),
      'magnetic_reindex_relative_residual':reindex,'zero_edge_normalized_max':zero_norm,
      'intertwiner_gram_residual':float(gram),'threshold':WITNESS_TOL,
      'scope':'fixed-causal j=1 full-K5 common-node full-collision leading coefficient on frozen tangent panels only; no remainder, positive-measure, local-integrability, Haar, spectral-pairing or physical-vertex theorem'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--panel',required=True,choices=sorted(PANELS)); ap.add_argument('--causal',required=True,choices=sorted(ctrl.SIGMAS)); ap.add_argument('--rho',required=True,type=int,choices=RHOS); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.panel,a.causal,a.rho)
    except Exception as e:
        out={'iteration':504,'lane':f'{a.panel}-{a.causal}-rho{a.rho}','panel':a.panel,'causal':a.causal,'rho':a.rho,'valid':False,'pass':False,'classification':'BLOCKED_OR_INFRASTRUCTURE_ITER504','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__': main()
