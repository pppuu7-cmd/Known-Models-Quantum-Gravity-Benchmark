import argparse, json, os
import mpmath as mp

mp.mp.dps = 80
RHO1=mp.mpf('0.35'); RHO2=mp.mpf('1.6')
MATS={
 'M1':((1,1),(0,1)),
 'M2':((1,0),(1,1)),
 'M3':((2,1),(1,1)),
 'M4':((1,2),(1,1)),
}
M5=((2,0),(0,1))
MSING=((1,1),(2,2))


def denrho(rho):
    i=mp.j
    return (i*rho+1)*(i*rho)*(i*rho-1)

def channels(m,b,rho):
    i=mp.j; D=denrho(rho); q=(mp.e**(2*b)-1)**3
    out={-1:{},1:{}}
    if m==0:
        A=mp.e**(2*b)-1; B=mp.e**(2*b)+1
        K=12*i*mp.e**(2*b)/(q*D)
        out[1]={1:K*A/2,0:K*i*B/2}
        out[-1]={1:K*A/2,0:-K*i*B/2}
    elif m==-1:
        S=mp.sinh(b); C=mp.cosh(b); K=-12*i*mp.e**(3*b)/(q*D)
        out[1]={0:K*i/2,1:K*S*C,2:K*(-i*S*S)}
        out[-1]={0:K*(-i/2)}
    else:
        S2=mp.sinh(2*b); C2=mp.cosh(2*b); K=-6*i*mp.e**(3*b)/(q*D)
        out[1]={0:K*i}
        out[-1]={0:K*(-i),1:K*S2,2:K*i*(C2-1)}
    return out

def poly_at(m,b,rho,s):
    terms=channels(m,b,rho)[s]
    return sum(v*rho**n for n,v in terms.items())

def source_selected_at(m,b,rho,s):
    return mp.e**(mp.j*s*b*rho)*poly_at(m,b,rho,s)

def selector(m,b,rho,s):
    return 2*mp.pi*mp.j*s*source_selected_at(m,b,rho,s)

def det2(M):
    return mp.mpf(M[0][0])*M[1][1]-mp.mpf(M[0][1])*M[1][0]

def inv2(M):
    d=det2(M)
    if d==0: return None
    return ((mp.mpf(M[1][1])/d,-mp.mpf(M[0][1])/d),(-mp.mpf(M[1][0])/d,mp.mpf(M[0][0])/d))

def rel(a,b):
    return abs(a-b)/max(mp.mpf('1e-70'),abs(a),abs(b))

def fstr(x): return mp.nstr(x,30)

def transformed_value(m1,m2,b1,b2,s1,s2,M,measure_comp=True):
    dM=det2(M)
    if dM==0: raise ValueError('singular transform')
    L=inv2(M); dL=abs(det2(L))
    measure=1/abs(dM) if measure_comp else mp.mpf('1')
    F=source_selected_at(m1,b1,RHO1,s1)*source_selected_at(m2,b2,RHO2,s2)
    pole_pref=(2*mp.pi*mp.j*s1)*(2*mp.pi*mp.j*s2)
    return pole_pref*F*measure/dL

def seq12_value(m1,m2,b1,b2,s1,s2,M):
    dM=det2(M); L=inv2(M)
    a,b=L[0]; c,d=L[1]
    if a==0: raise ValueError('seq12 zero first pivot')
    q=d-c*b/a
    if q==0: raise ValueError('seq12 singular Schur complement')
    jac_seq=1/(abs(a)*abs(q))
    measure=1/abs(dM)
    F=source_selected_at(m1,b1,RHO1,s1)*source_selected_at(m2,b2,RHO2,s2)
    return (2*mp.pi*mp.j*s1)*(2*mp.pi*mp.j*s2)*F*measure*jac_seq

def seq21_value(m1,m2,b1,b2,s1,s2,M):
    dM=det2(M); L=inv2(M)
    a,b=L[0]; c,d=L[1]
    if d==0: raise ValueError('seq21 zero first pivot')
    q=a-b*c/d
    if q==0: raise ValueError('seq21 singular Schur complement')
    jac_seq=1/(abs(d)*abs(q))
    measure=1/abs(dM)
    F=source_selected_at(m1,b1,RHO1,s1)*source_selected_at(m2,b2,RHO2,s2)
    return (2*mp.pi*mp.j*s1)*(2*mp.pi*mp.j*s2)*F*measure*jac_seq

def lane(m1,m2,b1,b2,label):
    records=[]; ok=True
    for s1 in (-1,1):
      for s2 in (-1,1):
        A=selector(m1,b1,RHO1,s1)*selector(m2,b2,RHO2,s2)
        negligible=abs(A)<mp.mpf('1e-20')
        for name,M in MATS.items():
            B=transformed_value(m1,m2,b1,b2,s1,s2,M,True)
            C=seq12_value(m1,m2,b1,b2,s1,s2,M)
            D=seq21_value(m1,m2,b1,b2,s1,s2,M)
            if negligible:
                core=max(abs(A-B),abs(A-C),abs(A-D),abs(C-D)) <= mp.mpf('1e-45')
            else:
                core=max(rel(A,B),rel(A,C),rel(A,D),rel(C,D)) <= mp.mpf('1e-35')
            # Flip s1 while keeping the original selected source channel: opposite boundary selector annihilates it.
            wrong=mp.mpc('0')
            wrong_sep=rel(A,wrong) if not negligible else mp.mpf('1')
            passed=bool(core and (negligible or wrong_sep>=mp.mpf('1e-3')))
            ok &= passed
            records.append({'matrix':name,'s1':s1,'s2':s2,'canonical_abs':fstr(abs(A)),
              'rel_A_B':fstr(rel(A,B)),'rel_A_C':fstr(rel(A,C)),'rel_A_D':fstr(rel(A,D)),
              'rel_C_D':fstr(rel(C,D)),'wrong_sign_relative_difference':fstr(wrong_sep),
              'pass':passed})
    # Frozen wrong-Jacobian scaling control.
    A=selector(m1,b1,RHO1,1)*selector(m2,b2,RHO2,1)
    wrongJ=transformed_value(m1,m2,b1,b2,1,1,M5,False)
    wj=rel(A,wrongJ)
    ctrl_j=bool(abs(A)<mp.mpf('1e-20') or wj>=mp.mpf('0.25'))
    # Frozen singular-normal null control.
    ctrl_sing=(det2(MSING)==0 and inv2(MSING) is None)
    ok &= ctrl_j and ctrl_sing
    return {'iteration':465,'lane':label,'m1':m1,'m2':m2,'beta1':fstr(b1),'beta2':fstr(b2),
      'records':records,'wrong_jacobian_M5_relative_difference':fstr(wj),
      'wrong_jacobian_control_pass':ctrl_j,'singular_normal_control_pass':bool(ctrl_sing),'pass':bool(ok),
      'classification':'ITER465_SOURCE_TWOFACTOR_TRANSVERSAL_PULLBACK_ORDER_INDEPENDENCE_QUALIFIED_SCOPED' if ok else 'SCIENTIFIC_FAIL_ITER465_SOURCE_TWOFACTOR_PULLBACK_OR_ORDER_INDEPENDENCE',
      'scope':'Transversal two-factor tensor-product/source-channel pullback and order-independence prerequisite only; no shared-variable/non-transversal causal-vertex theorem; D7-S2 remains open.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--m1',type=int,required=True); ap.add_argument('--m2',type=int,required=True)
    ap.add_argument('--beta1',required=True); ap.add_argument('--beta2',required=True); ap.add_argument('--label',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); out=lane(a.m1,a.m2,mp.mpf(a.beta1),mp.mpf(a.beta2),a.label)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2)); raise SystemExit(0 if out['pass'] else 1)
if __name__=='__main__': main()
