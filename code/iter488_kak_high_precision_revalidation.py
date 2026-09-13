#!/usr/bin/env python3
import argparse, json, math, os
import mpmath as mp
import numpy as np
import iter486_shared_node_haar_escape as base

mp.mp.dps = 100
KAK_TOL = mp.mpf('1e-8')
UNIT_TOL = mp.mpf('1e-30')
BETA_TOL = mp.mpf('1e-10')


def mpc_exact(z):
    return mp.mpc(mp.mpf(repr(float(np.real(z)))), mp.mpf(repr(float(np.imag(z)))))


def mp_matrix_from_np(a):
    return mp.matrix([[mpc_exact(a[i,j]) for j in range(a.shape[1])] for i in range(a.shape[0])])


def det2(a):
    return a[0,0]*a[1,1]-a[0,1]*a[1,0]


def maxabs_mp(a):
    return max(abs(a[i,j]) for i in range(a.rows) for j in range(a.cols))


def eye2():
    return mp.eye(2)


def mp_kak(h_np):
    h=mp_matrix_from_np(h_np)
    U,S,Vh=mp.svd_c(h)
    detu=det2(U)
    alpha=mp.sqrt(detu)
    U1=U/alpha
    U2=Vh*alpha
    beta=mp.log(S[0]/S[1])
    A=mp.matrix([[mp.e**(beta/2),0],[0,mp.e**(-beta/2)]])
    recon=maxabs_mp(U1*A*U2-h)
    u1u=maxabs_mp(U1.H*U1-eye2())
    u2u=maxabs_mp(U2.H*U2-eye2())
    u1d=abs(det2(U1)-1)
    u2d=abs(det2(U2)-1)
    return recon,u1u,u2u,u1d,u2d,beta


def beta_agrees(beta_mp,beta_double):
    bd=mp.mpf(repr(float(beta_double)))
    err=abs(beta_mp-bd)
    scale=max(abs(beta_mp),abs(bd),mp.mpf('1'))
    return err < BETA_TOL or err/scale < BETA_TOL, err, err/scale


def evaluate(cluster):
    panel='C'
    rows=[]
    recon_max=mp.mpf('0'); unit_max=mp.mpf('0'); det_max=mp.mpf('0')
    beta_abs_max=mp.mpf('0'); beta_rel_max=mp.mpf('0')
    finite=True; beta_ok=True
    for R in base.R_GRID:
        rs=base.relatives(base.escaped_nodes(panel,cluster,float(R)))
        for e,h in rs.items():
            recon,u1u,u2u,u1d,u2d,beta=mp_kak(h)
            _,beta_double,_,_=base.kak(h)
            bok,berr,brel=beta_agrees(beta,beta_double)
            vals=[recon,u1u,u2u,u1d,u2d,beta,berr,brel]
            finite=finite and all(bool(mp.isfinite(v)) for v in vals)
            beta_ok=beta_ok and bool(bok)
            recon_max=max(recon_max,recon); unit_max=max(unit_max,u1u,u2u); det_max=max(det_max,u1d,u2d)
            beta_abs_max=max(beta_abs_max,berr); beta_rel_max=max(beta_rel_max,brel)
            rows.append({'R':float(R),'edge':list(e),'reconstruction_residual':float(recon),'u_unitarity_max':float(max(u1u,u2u)),'u_det_max':float(max(u1d,u2d)),'beta_high_precision':float(beta),'beta_double':float(beta_double),'beta_abs_error':float(berr),'beta_relative_error':float(brel),'beta_agrees':bool(bok)})
    checks={
      'finite_all_40':bool(finite and len(rows)==40),
      'same_frozen_absolute_kak_threshold':bool(recon_max < KAK_TOL),
      'su2_unitarity_high_precision':bool(unit_max < UNIT_TOL),
      'su2_determinant_high_precision':bool(det_max < UNIT_TOL),
      'double_beta_agreement':bool(beta_ok),
    }
    passed=bool(all(checks.values()))
    return {
      'iteration':488,'panel':'C','cluster_size':cluster,'geometry_key':f'C-s{cluster}',
      'revalidates_lanes':([f'C-s{cluster}-0to5',f'C-s{cluster}-2to3'] if cluster==2 else [f'C-s{cluster}-0to5',f'C-s{cluster}-1to4',f'C-s{cluster}-2to3']),
      'checks':checks,'pass':passed,
      'classification':'ITER488_KAK_HIGH_PRECISION_REVALIDATED_SCOPED' if passed else 'NUMERICAL_OR_SOURCE_FAIL_ITER488_KAK_REVALIDATION',
      'high_precision_kak_reconstruction_max':float(recon_max),'high_precision_unitarity_max':float(unit_max),'high_precision_det_max':float(det_max),
      'beta_abs_error_max':float(beta_abs_max),'beta_relative_error_max':float(beta_rel_max),'objects_checked':len(rows),
      'rows':rows,
      'scope':'validation-only recheck of the unchanged Iter487 KAK reconstruction predicate; no slope recomputation or threshold change'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--cluster',type=int,required=True,choices=[2,3]); ap.add_argument('--out',required=True); args=ap.parse_args()
    try: payload=evaluate(args.cluster)
    except Exception as e: payload={'iteration':488,'cluster_size':args.cluster,'pass':False,'classification':'NUMERICAL_OR_SOURCE_FAIL_ITER488_KAK_REVALIDATION','error':repr(e)}
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(payload,f,indent=2,sort_keys=True)
    print(json.dumps(payload,indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__': main()
