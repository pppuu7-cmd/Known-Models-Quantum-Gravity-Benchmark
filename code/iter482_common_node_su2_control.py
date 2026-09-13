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
THRESH=1e-12
RTOL=1e-10
PANELS={
 'Q0':[(0.,0.,0.),(.17,.43,-.29),(-.38,.71,.52),(.61,.84,.33),(-.47,.58,-.76)],
 'Q1':[(0.,0.,0.),(.93,.52,-.41),(-.74,1.03,.26),(-1.11,.67,.89),(.68,.92,-1.02)],
 'Q2':[(0.,0.,0.),(.29,.36,.77),(-.83,.57,-.24),(.51,1.12,-.66),(-.42,.88,.95)],
}
OLD_LANES={
 'L0':((.17,.43,-.29),(-.38,.71,.52)),
 'L1':((-.61,.84,.33),(.47,.58,-.76)),
 'L2':((.93,.52,-.41),(-.74,1.03,.26)),
 'L3':((-1.11,.67,.89),(.68,.92,-1.02)),
}
OLD_PATTERNS={'P0':[f'L{i%4}' for i in range(10)],'P1':[f'L{(2*i+1)%4}' for i in range(10)]}

LABEL={}; k=0
for a in range(5):
    for ei,e in enumerate(EDGES):
        if a in e: LABEL[(a,ei)]=k; k+=1
NODE_LABELS={a:[LABEL[(a,ei)] for ei,e in enumerate(EDGES) if a in e] for a in range(5)}
EDGE_LABELS={ei:[LABEL[(a,ei)],LABEL[(b,ei)]] for ei,(a,b) in enumerate(EDGES)}

def coeff(m,rho,plus=True):
    jx=mp.mpf(1); mx=mp.mpf(m); rx=mp.mpf(rho); ii=mp.j; N=3
    if plus:
        aa=jx+mx+1; bb=jx+1-ii*rx; cc=1+mx-ii*rx
        pref=mp.gamma(4)*mp.gamma(ii*rx-mx)/(mp.gamma(jx-mx+1)*mp.gamma(jx+1+ii*rx))
    else:
        aa=jx-mx+1; bb=jx+1+ii*rx; cc=1-mx+ii*rx
        pref=mp.gamma(4)*mp.gamma(-ii*rx+mx)/(mp.gamma(jx+mx+1)*mp.gamma(jx+1-ii*rx))
    return complex(pref*mp.gamma(cc)*mp.gamma(N)/(mp.gamma(aa)*mp.gamma(bb)))

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

def relatives(qs):
    return {(a,b):qs[b].conj().T@qs[a] for a,b in EDGES}

def cycle_residual(rs):
    r=0.0
    for a,b,c in itertools.combinations(range(5),3):
        r=max(r,float(np.max(np.abs(rs[(b,c)]@rs[(a,b)]-rs[(a,c)]))))
    return r

def old_pattern_cycle(pattern):
    rs={}
    for ei,e in enumerate(EDGES):
        ang1,ang2=OLD_LANES[OLD_PATTERNS[pattern][ei]]
        rs[e]=wigner1(*ang1)@wigner1(*ang2)
    return cycle_residual(rs)

def evaluate(gamma,cname,panel):
    sig=SIGMAS[cname]
    ts=[intertwiner(i) for i in range(3)]
    int_ok,gramres=tensor_controls(ts)
    path=contraction_path(ts)
    qs=[wigner1(*ang) for ang in PANELS[panel]]
    I=np.eye(3,dtype=np.complex128)
    node_unit=max(float(np.max(np.abs(Q.conj().T@Q-I))) for Q in qs)
    rs=relatives(qs)
    edge_unit=max(float(np.max(np.abs(R.conj().T@R-I))) for R in rs.values())
    cyc=cycle_residual(rs)
    G=wigner1(.31,.49,-.27)
    rsg=relatives([G@Q for Q in qs])
    gauge=max(float(np.max(np.abs(rsg[e]-rs[e]))) for e in EDGES)
    corrupt=dict(rs); corrupt[(0,1)]=wigner1(.23,.37,.19)@corrupt[(0,1)]
    corrupt_cycle=cycle_residual(corrupt)
    olddiag={'P0':old_pattern_cycle('P0'),'P1':old_pattern_cycle('P1')}

    perm=[2,1,0]; mats=[]; scales=[]
    for e in EDGES:
        a,b=e; plus=sig[a]*sig[b]>0
        cv=np.array([coeff(m,gamma,plus) for m in MS_U],dtype=np.complex128)
        scales.append(float(np.max(np.abs(cv))))
        L=rs[e]@np.diag(cv)
        mats.append(L[np.ix_(perm,perm)])
    scale=float(np.prod(scales))
    channels=list(itertools.product(range(3),repeat=5))
    vals=np.array([contract(ch,ts,mats,path) for ch in channels])
    mags=np.abs(vals); ratios=mags/scale; nz=ratios>THRESH; imax=int(np.argmax(ratios))

    rts=[T[::-1,::-1,::-1,::-1].copy() for T in ts]
    rmats=[M[::-1,::-1].copy() for M in mats]
    rvals=np.array([contract(ch,rts,rmats,path) for ch in channels])
    sm=np.sort(mags); srm=np.sort(np.abs(rvals)); denom=max(float(np.max(sm)),float(np.max(srm)),1e-300)
    reindex=float(np.max(np.abs(sm-srm))/denom)
    zero=[np.zeros((3,3),dtype=np.complex128) for _ in EDGES]
    zmax=max(abs(contract(ch,ts,zero,path)) for ch in channels)

    checks={
      'node_unitarity':node_unit<1e-12,
      'edge_unitarity':edge_unit<1e-12,
      'triangle_cycle_consistency':cyc<1e-12,
      'common_left_gauge_control':gauge<1e-12,
      'corrupted_edge_negative':corrupt_cycle>1e-6,
      'eq90_intertwiner_controls':int_ok,
      'scale_finite_positive':bool(np.isfinite(scale) and scale>0),
      'nonzero_witness':bool(np.any(nz)),
      'basis_reindex_control':reindex<RTOL,
      'zero_matrix_negative':bool(zmax<1e-14),
    }
    ok=all(checks.values())
    return {
      'iteration':'482','lane':f'g{gamma}-{cname}-{panel}','gamma':gamma,'causal_representative':cname,'panel':panel,
      'scientific_pass':ok,
      'classification':'ITER482_COMMON_NODE_SU2_CORRELATED_NETWORK_NONZERO_WITNESS_SCOPED' if ok else 'FAIL_ITER482_COMMON_NODE_SU2_CORRELATED_CONTROL',
      'checks':checks,'node_unitarity_max':node_unit,'edge_unitarity_max':edge_unit,'triangle_cycle_residual':cyc,
      'common_left_gauge_residual':gauge,'corrupted_edge_cycle_residual':corrupt_cycle,'iter481_old_pattern_cycle_residuals':olddiag,
      'intertwiner_gram_residual':gramres,'scale':scale,'total_channels':243,'nonzero_witnesses':int(np.count_nonzero(nz)),
      'max_ratio':float(ratios[imax]),'max_channel':list(channels[imax]),'basis_reindex_relative_residual':reindex,
      'zero_matrix_negative_max_abs':float(zmax),
      'scope':'compact SU2 common-node correlated control only; no unique full SL2C KAK, boost/Haar/spectral/full-vertex conclusion',
      'd7_s2':'NOT_CLOSED','d7_s3':'NOT_CLOSED','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED'
    }

def main():
    gamma=int(os.environ['ITER482_GAMMA']); cname=os.environ['ITER482_CAUSAL']; panel=os.environ['ITER482_PANEL']
    out=evaluate(gamma,cname,panel)
    pathlib.Path('artifacts').mkdir(exist_ok=True)
    p=pathlib.Path(f'artifacts/iter482-{out["lane"]}.json'); p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    raise SystemExit(0 if out['scientific_pass'] else 2)

if __name__=='__main__': main()
