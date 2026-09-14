#!/usr/bin/env python3
"""Validated Arb/Acb core for prospectively frozen Iter499.

No classifier lives here.  This module implements only the frozen source geometry,
closed-form 2x2 KAK enclosure, exact j=1 Toller branches, exact-rational
intertwiners and the simultaneous 243-channel contraction.
"""
import math
import numpy as np
from flint import arb, acb, ctx

import iter482_common_node_su2_control as ctrl
import iter483_common_node_sl2c_polar as gb

ctx.prec = 384

COORDS=[0,1,3,5,6,11]
DIRS=[
 [1,1,1,1,1,1], [1,1,1,-1,-1,-1], [1,-1,-1,1,1,-1], [1,-1,1,-1,1,-1],
 [1,1,-1,1,-1,-1], [1,-1,1,1,-1,1], [1,1,-1,-1,1,1], [1,-1,-1,-1,-1,1]
]
BLOCKS=[DIRS[0:2],DIRS[2:4],DIRS[4:6],DIRS[6:8]]
EDGES=list(ctrl.EDGES)
RHOS=[0.35,0.9,1.6,2.7]
R_GRID=[6,8,10,12]
SIGMAS=ctrl.SIGMAS
I=acb(0,1)
ZERO=acb(0)
ONE=acb(1)


def A(x):
    if isinstance(x,arb): return x
    if isinstance(x,int): return arb(x)
    if isinstance(x,str): return arb(x)
    return arb(repr(float(x)))


def C(x=0):
    return x if isinstance(x,acb) else acb(x)


def conj(z): return C(z).conjugate()

def abs2(z):
    z=C(z)
    return z.real*z.real + z.imag*z.imag


def det2(M): return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def inv2(M):
    d=det2(M)
    return [[M[1][1]/d,-M[0][1]/d],[-M[1][0]/d,M[0][0]/d]]


def mm(A0,B0):
    n=len(A0); k=len(B0); m=len(B0[0])
    return [[sum((A0[i][q]*B0[q][j] for q in range(k)),acb(0)) for j in range(m)] for i in range(n)]


def madd(A0,B0,sgn=1):
    return [[A0[i][j]+sgn*B0[i][j] for j in range(len(A0[0]))] for i in range(len(A0))]


def dagger(M):
    return [[conj(M[j][i]) for j in range(len(M))] for i in range(len(M[0]))]


def eye2(): return [[acb(1),acb(0)],[acb(0),acb(1)]]

def diag2(a,b): return [[C(a),acb(0)],[acb(0),C(b)]]


def residual_contains_zero(M):
    return all(C(z).contains(0) for row in M for z in row)


def det_contains_one(M): return C(det2(M)).contains(1)


def unitary_contains(M):
    return residual_contains_zero(madd(mm(dagger(M),M),eye2(),-1))


def su2(a,t,g):
    a=A(a); t=A(t); g=A(g)
    c=(t/2).cos(); s=(t/2).sin()
    rz1=diag2(acb(0,-a/2).exp(),acb(0,a/2).exp())
    ry=[[C(c),C(-s)],[C(s),C(c)]]
    rz2=diag2(acb(0,-g/2).exp(),acb(0,g/2).exp())
    return mm(mm(rz1,ry),rz2)


def boost(x):
    x=A(x)
    return diag2((x/2).exp(),(-x/2).exp())


def rx(x):
    x=A(x); c=(x/2).cos(); s=(x/2).sin()
    return [[C(c),-I*s],[-I*s,C(c)]]


def ry(x):
    x=A(x); c=(x/2).cos(); s=(x/2).sin()
    return [[C(c),C(-s)],[C(s),C(c)]]


def rz(x):
    x=A(x)
    return diag2(acb(0,-x/2).exp(),acb(0,x/2).exp())


def geometry(R,vec6,sign,amp):
    """Whole amplitude-box geometry, matching Iter491/492 construction."""
    d20=[0]*20
    for k,c in enumerate(COORDS): d20[c]=int(sign)*int(vec6[k])
    B=boost(R)
    etas=gb.BOOSTS['strong']
    out=[eye2()]
    for i in range(1,5):
        a,t,g=gb.PANELS['C'][i]
        ur_a=float(-0.37*g); ur_t=float(0.73*t); ur_g=float(0.41*a)
        g0=mm(mm(su2(repr(float(a)),repr(float(t)),repr(float(g))),boost(repr(float(etas[i])))),
              su2(repr(ur_a),repr(ur_t),repr(ur_g)))
        out.append(mm(B,g0))
    eps=amp*((-A(R)).exp())
    for node in range(1,5):
        q=[eps*d20[(node-1)*5+j] for j in range(5)]
        L=mm(mm(rx(q[0]),ry(q[1])),rz(q[2]))
        RR=mm(rx(q[3]),ry(q[4]))
        out[node]=mm(mm(L,out[node]),RR)
    rs={(a,b):mm(inv2(out[b]),out[a]) for a,b in EDGES}
    return out,rs


def _norm2_pair(w): return abs2(w[0])+abs2(w[1])


def kak_ball(h):
    """Closed-form validated KAK enclosure for a 2x2 SL(2,C) ball matrix."""
    a=abs2(h[0][0])+abs2(h[1][0])
    d=abs2(h[0][1])+abs2(h[1][1])
    c=conj(h[0][0])*h[0][1]+conj(h[1][0])*h[1][1]
    t=(a+d)/2; delta=(a-d)/2
    rad=(delta*delta+abs2(c)).sqrt()
    lp=t+rad; lm=t-rad
    sep=lp-lm
    if not (lm.lower()>arb(0) and sep.lower()>arb(0)):
        raise ArithmeticError('KAK eigenvalue positivity/separation not certified')
    wA=[c,C(lp-a)]
    wB=[C(lp-d),conj(c)]
    nA2=_norm2_pair(wA); nB2=_norm2_pair(wB)
    loA=nA2.lower(); loB=nB2.lower()
    floor=arb('1e-60')  # norm^2 floor corresponding to preregistered norm >1e-30
    if not (loA>floor or loB>floor):
        raise ArithmeticError('KAK eigenvector chart norm not certified')
    w=wA if loA>=loB else wB
    chart='A' if loA>=loB else 'B'
    n=_norm2_pair(w).sqrt()
    v=[w[0]/n,w[1]/n]
    V=[[v[0],-conj(v[1])],[v[1],conj(v[0])]]
    U2=dagger(V)
    beta=(lp.log()-lm.log())/2
    if not beta.lower()>arb(0): raise ArithmeticError('positive beta not certified')
    AA=diag2((beta/2).exp(),(-beta/2).exp())
    Ainv=diag2((-beta/2).exp(),(beta/2).exp())
    U1=mm(mm(h,V),Ainv)
    H=[[C(a),c],[conj(c),C(d)]]
    DD=diag2(lp,lm)
    eigen_ok=residual_contains_zero(madd(mm(H,V),mm(V,DD),-1))
    recon_ok=residual_contains_zero(madd(mm(mm(U1,AA),U2),h,-1))
    u1_ok=unitary_contains(U1); u2_ok=unitary_contains(U2)
    d1_ok=det_contains_one(U1); d2_ok=det_contains_one(U2)
    valid=bool(eigen_ok and recon_ok and u1_ok and u2_ok and d1_ok and d2_ok)
    if not valid: raise ArithmeticError('KAK containment control failed')
    return {'U1':U1,'beta':beta,'U2':U2,'lambda_plus':lp,'lambda_minus':lm,
            'chart':chart,'chart_norm2_lower':loA if chart=='A' else loB,
            'valid':valid}


def spin1(U):
    """Canonical symmetric square in frozen (-1,0,+1) ordering."""
    a,b=U[0]; c,d=U[1]; q=arb(2).sqrt()
    return [
      [d*d, q*c*d, c*c],
      [q*b*d, a*d+b*c, q*a*c],
      [b*b, q*a*b, a*a],
    ]


def source_coeffs(m,rho,b):
    """Exact j=1 source formulas already locked by Iter456."""
    r=A(repr(float(rho))); den=r+r**3
    sh=b.sinh(); ch=b.cosh(); cs=1/sh; ct=ch/sh
    br=b*r; ep=acb(0,br).exp(); em=acb(0,-br).exp()
    co=br.cos(); si=br.sin(); sh2=(2*b).sinh(); ch2=(2*b).cosh()
    e2=(2*b).exp()
    if m==0:
        d=-12*e2*(((e2-1)*r*co-(e2+1)*si))/((e2-1)**3*den)
        tp=-3*ep*(C(r)+I*ct)*cs**2/(2*den)
        tm=-3*em*(C(r)-I*ct)*cs**2/(2*den)
    elif m==-1:
        d=12*(3*b).exp()*(-si+ep*r*sh*(C(ch)-I*r*sh))/((e2-1)**3*den)
        tp=3*ep*cs**3*(I*(1+r**2)+r*(C(sh2)-I*r*ch2))/(4*den)
        tm=-3*I*em*cs**3/(4*den)
    elif m==1:
        d=6*(b*(acb(3)-I*r)).exp()*(I*(ep**2-r**2-1)+r*(I*r*ch2+sh2))/((e2-1)**3*den)
        tp=3*I*ep*cs**3/(4*den)
        tm=3*cs**3*(I*co+si)*(-r**2+r**2*ch2-I*r*sh2-1)/(4*den)
    else:
        raise ValueError(m)
    return C(d),C(tp),C(tm)


def full_toller(kak,rho,branch):
    U1,U2,b=kak['U1'],kak['U2'],kak['beta']
    ds=[]; ps=[]; ms=[]; additive=True
    for m in (-1,0,1):
        d,p,n=source_coeffs(m,rho,b)
        additive=additive and (p+n-d).contains(0)
        ds.append(d); ps.append(p); ms.append(n)
    vals=ps if branch=='p' else ms
    L=spin1(U1); R=spin1(U2)
    out=[[sum((L[i][k]*vals[k]*R[k][j] for k in range(3)),acb(0)) for j in range(3)] for i in range(3)]
    return out,bool(additive)


# Exact-rational j=1 intertwiner tensors, support/signs generated from the same
# Wigner-3j definition used by iter482_common_node_su2_control.intertwiner.
_SUPPORTS={
0:{
 (-1,1,-1,1):'1/3',(-1,1,0,0):'-1/3',(-1,1,1,-1):'1/3',
 (0,0,-1,1):'-1/3',(0,0,0,0):'1/3',(0,0,1,-1):'-1/3',
 (1,-1,-1,1):'1/3',(1,-1,0,0):'-1/3',(1,-1,1,-1):'1/3'},
1:{
 (-1,0,0,1):'1/6',(-1,0,1,0):'-1/6',(-1,1,-1,1):'-1/6',(-1,1,1,-1):'1/6',
 (0,-1,0,1):'-1/6',(0,-1,1,0):'1/6',(0,1,-1,0):'1/6',(0,1,0,-1):'-1/6',
 (1,-1,-1,1):'1/6',(1,-1,1,-1):'-1/6',(1,0,-1,0):'-1/6',(1,0,0,-1):'1/6'},
2:{
 (-1,-1,1,1):'1/5',(-1,0,0,1):'-1/10',(-1,0,1,0):'-1/10',
 (-1,1,-1,1):'1/30',(-1,1,0,0):'1/15',(-1,1,1,-1):'1/30',
 (0,-1,0,1):'-1/10',(0,-1,1,0):'-1/10',(0,0,-1,1):'1/15',(0,0,0,0):'2/15',(0,0,1,-1):'1/15',
 (0,1,-1,0):'-1/10',(0,1,0,-1):'-1/10',(1,-1,-1,1):'1/30',(1,-1,0,0):'1/15',
 (1,-1,1,-1):'1/30',(1,0,-1,0):'-1/10',(1,0,0,-1):'-1/10',(1,1,-1,-1):'1/5'}
}


def exact_intertwiners():
    out=np.empty((3,3,3,3,3),dtype=object)
    for idx in np.ndindex(out.shape): out[idx]=arb(0)
    for channel,sup in _SUPPORTS.items():
        for ms,val in sup.items(): out[(channel,)+tuple(m+1 for m in ms)]=arb(val)
    return out

TSTACK=exact_intertwiners()


def intertwiner_regression():
    old=[ctrl.intertwiner(i) for i in range(3)]
    mx=0.0
    for i in range(3):
        for idx in np.ndindex((3,3,3,3)):
            mx=max(mx,abs(float(TSTACK[(i,)+idx].mid())-float(old[i][idx].real)))
    return mx


def _build_path():
    dummy=np.ones((3,3,3,3,3),dtype=np.float64)
    args=[]; outlabels=list(range(20,25))
    for node in range(5): args += [dummy,[20+node]+ctrl.NODE_LABELS[node]]
    for ei in range(10): args += [np.ones((3,3),dtype=np.float64),ctrl.EDGE_LABELS[ei]]
    args += [outlabels]
    return np.einsum_path(*args,optimize='greedy')[0]

BALL_PATH=_build_path()


def contract_all(mats):
    args=[]; outlabels=list(range(20,25))
    for node in range(5): args += [TSTACK,[20+node]+ctrl.NODE_LABELS[node]]
    for ei,M in enumerate(mats): args += [np.asarray(M,dtype=object),ctrl.EDGE_LABELS[ei]]
    args += [outlabels]
    return np.einsum(*args,optimize=BALL_PATH)


def envelope_bounds(vals):
    lows=[]; ups=[]
    for z in vals.flat:
        zz=C(z); lo=zz.abs_lower(); up=zz.abs_upper()
        if not (lo.is_finite() and up.is_finite()): raise ArithmeticError('nonfinite channel ball')
        lows.append(lo); ups.append(up)
    L=lows[0]; U=ups[0]
    for x in lows[1:]:
        if x>L: L=x
    for x in ups[1:]:
        if x>U: U=x
    if not L>arb(0): raise ArithmeticError('envelope lower bound not positive')
    possible=[i for i,u in enumerate(ups) if u>=L]
    return L,U,possible


def box_amp(k):
    if k not in range(16): raise ValueError(k)
    lo=arb(f'{16+k}/12800'); hi=arb(f'{17+k}/12800')
    return lo.union(hi),lo,hi


def arb_float(x):
    """Display-only conversion; never used for validated decisions."""
    return float(x.mid())


def bound_float(x,which):
    y=x.lower() if which=='lower' else x.upper()
    return float(y)
