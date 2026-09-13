#!/usr/bin/env python3
import itertools, json, math, os, pathlib
import mpmath as mp
import numpy as np
from sympy.physics.wigner import wigner_3j

mp.mp.dps=70
MS=[-1,0,1]
MS_U=[1,0,-1]
EDGES=[(a,b) for a in range(5) for b in range(a+1,5)]
SIGMAS={'0to5':(1,1,1,1,1),'1to4':(-1,1,1,1,1),'2to3':(-1,-1,1,1,1)}
LANES={
'L0': ((.17,.43,-.29),(-.38,.71,.52)),
'L1': ((-.61,.84,.33),(.47,.58,-.76)),
'L2': ((.93,.52,-.41),(-.74,1.03,.26)),
'L3': ((-1.11,.67,.89),(.68,.92,-1.02)),
}
PATTERNS={
'P0':[f'L{i%4}' for i in range(10)],
'P1':[f'L{(2*i+1)%4}' for i in range(10)],
}
THRESH=1e-12
RTOL=1e-10

# Each node-edge incidence receives its own tensor index.
LABEL={}
k=0
for a in range(5):
    for ei,e in enumerate(EDGES):
        if a in e:
            LABEL[(a,ei)]=k; k+=1
NODE_LABELS={a:[LABEL[(a,ei)] for ei,e in enumerate(EDGES) if a in e] for a in range(5)}
EDGE_LABELS={ei:[LABEL[(a,ei)],LABEL[(b,ei)]] for ei,(a,b) in enumerate(EDGES)}


def coeff(m,rho,plus=True):
    jx=mp.mpf(1); mx=mp.mpf(m); rx=mp.mpf(rho); ii=mp.j; N=3
    if plus:
        a=jx+mx+1; b=jx+1-ii*rx; c=1+mx-ii*rx
        pref=mp.gamma(4)*mp.gamma(ii*rx-mx)/(mp.gamma(jx-mx+1)*mp.gamma(jx+1+ii*rx))
    else:
        a=jx-mx+1; b=jx+1+ii*rx; c=1-mx+ii*rx
        pref=mp.gamma(4)*mp.gamma(-ii*rx+mx)/(mp.gamma(jx+mx+1)*mp.gamma(jx+1-ii*rx))
    return complex(pref*mp.gamma(c)*mp.gamma(N)/(mp.gamma(a)*mp.gamma(b)))


def wigner1(a,t,g):
    c=math.cos(t); s=math.sin(t); q=math.sqrt(2.0)
    d=np.array([[(1+c)/2,-s/q,(1-c)/2],[s/q,c,-s/q],[(1-c)/2,s/q,(1+c)/2]],dtype=np.complex128)
    D=np.zeros((3,3),dtype=np.complex128)
    for i,m in enumerate(MS_U):
        for j,n in enumerate(MS_U):
            D[i,j]=np.exp(-1j*m*a)*d[i,j]*np.exp(-1j*n*g)
    return D


def intertwiner(i):
    T=np.zeros((3,3,3,3),dtype=np.complex128)
    for ms in itertools.product(MS,repeat=4):
        v=0j
        for m in range(-i,i+1):
            term=((-1)**(i-m))*wigner_3j(1,1,i,ms[0],ms[1],m)*wigner_3j(i,1,1,-m,ms[2],ms[3])
            v+=complex(term.evalf(40))
        T[tuple(x+1 for x in ms)]=v
    return T


def tensor_controls(ts):
    support=True
    for T in ts:
        for idx in np.ndindex(T.shape):
            if sum(i-1 for i in idx)!=0 and abs(T[idx])>1e-14: support=False
    gram=np.array([[np.vdot(ts[i],ts[j]) for j in range(3)] for i in range(3)])
    target=np.diag([1.0,1/3,1/5])
    res=float(np.max(np.abs(gram-target)))
    return bool(support and res<1e-12),res


def contract(ch,ts,mats,path):
    args=[]
    for a,c in enumerate(ch): args += [ts[c],NODE_LABELS[a]]
    for ei,M in enumerate(mats): args += [M,EDGE_LABELS[ei]]
    args += [[]]
    return np.einsum(*args,optimize=path)


def contraction_path(ts):
    args=[]
    for a in range(5): args += [ts[0],NODE_LABELS[a]]
    for ei in range(10): args += [np.ones((3,3),dtype=np.complex128),EDGE_LABELS[ei]]
    args += [[]]
    return np.einsum_path(*args,optimize='greedy')[0]


def edge_data(gamma,sig,pattern):
    mats=[]; diagmats=[]; coeff_scales=[]; unitmax=0.0
    # reorder Iter479 U basis [1,0,-1] into intertwiner basis [-1,0,1]
    perm=[2,1,0]
    for ei,(a,b) in enumerate(EDGES):
        plus=sig[a]*sig[b]>0
        cv_u=np.array([coeff(m,gamma,plus) for m in MS_U],dtype=np.complex128)
        coeff_scales.append(float(np.max(np.abs(cv_u))))
        lane=PATTERNS[pattern][ei]
        ang1,ang2=LANES[lane]
        U1=wigner1(*ang1); U2=wigner1(*ang2)
        I=np.eye(3)
        unitmax=max(unitmax,float(np.max(np.abs(U1.conj().T@U1-I))),float(np.max(np.abs(U2.conj().T@U2-I))))
        L_u=U1@np.diag(cv_u)@U2
        mats.append(L_u[np.ix_(perm,perm)])
        cv_i=np.array([coeff(m,gamma,plus) for m in MS],dtype=np.complex128)
        diagmats.append(np.diag(cv_i))
    scale=float(np.prod(coeff_scales))
    return mats,diagmats,scale,unitmax


def evaluate(gamma,cname,pattern):
    sig=SIGMAS[cname]
    ts=[intertwiner(i) for i in range(3)]
    int_ok,gramres=tensor_controls(ts)
    path=contraction_path(ts)
    mats,diag,scale,unitmax=edge_data(gamma,sig,pattern)
    channels=list(itertools.product(range(3),repeat=5))
    vals=np.array([contract(ch,ts,mats,path) for ch in channels])
    mags=np.abs(vals); ratios=mags/scale
    nz=ratios>THRESH; imax=int(np.argmax(ratios))

    # identity-angle regression to Iter480B.
    dvals=np.array([contract(ch,ts,diag,path) for ch in channels])
    drat=np.abs(dvals)/scale
    dcount=int(np.count_nonzero(drat>THRESH)); dmax=float(np.max(drat))
    target=0.0046296296296296285
    regrel=abs(dmax-target)/target
    regression=bool(dcount==130 and regrel<RTOL)

    # Pure basis reindex: m -> -m on every half-edge basis.
    rts=[T[::-1,::-1,::-1,::-1].copy() for T in ts]
    rmats=[M[::-1,::-1].copy() for M in mats]
    rvals=np.array([contract(ch,rts,rmats,path) for ch in channels])
    sm=np.sort(mags); srm=np.sort(np.abs(rvals)); denom=max(float(np.max(sm)),float(np.max(srm)),1e-300)
    reindex=float(np.max(np.abs(sm-srm))/denom)

    zero=[np.zeros((3,3),dtype=np.complex128) for _ in range(10)]
    zmax=max(abs(contract(ch,ts,zero,path)) for ch in channels)

    checks={
      'eq90_intertwiner_controls':int_ok,
      'iter479_wigner_unitarity':unitmax<1e-12,
      'scale_finite_positive':bool(np.isfinite(scale) and scale>0),
      'nonzero_witness':bool(np.any(nz)),
      'identity_angle_iter480b_regression':regression,
      'basis_reindex_control':reindex<RTOL,
      'zero_matrix_negative':bool(zmax<1e-14),
    }
    ok=all(checks.values())
    return {
      'iteration':'481','lane':f'g{gamma}-{cname}-{pattern}','scientific_pass':ok,
      'classification':'ITER481_SOURCE_ANGULAR_INTERTWINER_NETWORK_NONZERO_WITNESS_SCOPED' if ok else 'FAIL_ITER481_ANGULAR_INTERTWINER_NETWORK',
      'checks':checks,'gamma':gamma,'causal_representative':cname,'angular_pattern':pattern,
      'intertwiner_gram_residual':gramres,'wigner_unitarity_max':unitmax,'scale':scale,
      'total_channels':243,'nonzero_witnesses':int(np.count_nonzero(nz)),'max_ratio':float(ratios[imax]),'max_channel':list(channels[imax]),
      'identity_regression_count':dcount,'identity_regression_max_ratio':dmax,'identity_regression_relative_residual':regrel,
      'basis_reindex_relative_residual':reindex,'zero_matrix_negative_max_abs':float(zmax),
      'scope':'local Eq7 angular matrices + boundary intertwiners only; no common SL2C group compatibility/Haar/spectral/full-K5 conclusion',
      'd7_s2':'NOT_CLOSED','d7_s3':'NOT_CLOSED','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED'
    }


def main():
    gamma=int(os.environ['ITER481_GAMMA']); cname=os.environ['ITER481_CAUSAL']; pattern=os.environ['ITER481_PATTERN']
    out=evaluate(gamma,cname,pattern)
    pathlib.Path('artifacts').mkdir(exist_ok=True)
    p=pathlib.Path(f'artifacts/iter481-{out["lane"]}.json'); p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    raise SystemExit(0 if out['scientific_pass'] else 2)

if __name__=='__main__': main()
