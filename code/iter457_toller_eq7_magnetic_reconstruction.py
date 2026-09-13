import argparse, json, os, sys
import mpmath as mp

sys.path.insert(0, os.path.dirname(__file__))
from iter456_reduced_toller_appendixb import source

mp.mp.dps = 80
MS=[1,0,-1]
RHOS=[mp.mpf(x) for x in ['-2.3','-1.7','-0.6','0.35','0.9','1.6','2.7']]
BETAS=[mp.mpf('0.35'),mp.mpf('0.8'),mp.mpf('1.2'),mp.pi/2,mp.mpf('2.1')]
CHIS=[mp.mpf('0.23'),mp.mpf('-0.71'),mp.mpf('1.19')]
LANES={
'L0': ((mp.mpf('.17'),mp.mpf('.43'),mp.mpf('-.29')),(mp.mpf('-.38'),mp.mpf('.71'),mp.mpf('.52')),(mp.mpf('.31'),mp.mpf('-.23'),mp.mpf('.41')),(mp.mpf('-.27'),mp.mpf('.36'),mp.mpf('-.19'))),
'L1': ((mp.mpf('-.61'),mp.mpf('.84'),mp.mpf('.33')),(mp.mpf('.47'),mp.mpf('.58'),mp.mpf('-.76')),(mp.mpf('.22'),mp.mpf('.39'),mp.mpf('-.51')),(mp.mpf('.56'),mp.mpf('-.28'),mp.mpf('.37'))),
'L2': ((mp.mpf('.93'),mp.mpf('.52'),mp.mpf('-.41')),(mp.mpf('-.74'),mp.mpf('1.03'),mp.mpf('.26')),(mp.mpf('-.35'),mp.mpf('.48'),mp.mpf('.63')),(mp.mpf('.44'),mp.mpf('.31'),mp.mpf('-.57'))),
'L3': ((mp.mpf('-1.11'),mp.mpf('.67'),mp.mpf('.89')),(mp.mpf('.68'),mp.mpf('.92'),mp.mpf('-1.02')),(mp.mpf('.53'),mp.mpf('-.44'),mp.mpf('.29')),(mp.mpf('-.62'),mp.mpf('.27'),mp.mpf('.46'))),
}

JZ=mp.matrix([[1,0,0],[0,0,0],[0,0,-1]])
JY=mp.matrix([[0,-1j/mp.sqrt(2),0],[1j/mp.sqrt(2),0,-1j/mp.sqrt(2)],[0,1j/mp.sqrt(2),0]])
I3=mp.eye(3)

def dag(A): return A.transpose_conj()
def fnorm(A): return mp.sqrt(sum(abs(A[i,j])**2 for i in range(A.rows) for j in range(A.cols)))
def maxentry(A): return max(abs(A[i,j]) for i in range(A.rows) for j in range(A.cols))

def wigner_closed(a,t,g):
    c=mp.cos(t); s=mp.sin(t); q=mp.sqrt(2)
    d=mp.matrix([[(1+c)/2,-s/q,(1-c)/2],[s/q,c,-s/q],[(1-c)/2,s/q,(1+c)/2]])
    D=mp.matrix(3)
    for i,m in enumerate(MS):
        for j,n in enumerate(MS): D[i,j]=mp.e**(-1j*m*a)*d[i,j]*mp.e**(-1j*n*g)
    return D

def wigner_exp(a,t,g):
    return mp.expm(-1j*a*JZ)*mp.expm(-1j*t*JY)*mp.expm(-1j*g*JZ)

def rz(x): return mp.diag([mp.e**(-1j*x),1,mp.e**(1j*x)])

def vals(r,b):
    # source() uses magnetic m=-1,0,+1; return in Eq.(7) matrix order p=+1,0,-1.
    d={};tp={};tm={}
    for p in (-1,0,1):
        q=source(p,r,b); d[p],tp[p],tm[p]=q
    return [d[p] for p in MS],[tp[p] for p in MS],[tm[p] for p in MS]

def diag(v): return mp.diag(v)

def recon_prod(A,v,B): return A*diag(v)*B

def recon_sum(A,v,B):
    R=mp.matrix(3)
    for i in range(3):
        for j in range(3): R[i,j]=sum(A[i,p]*v[p]*B[p,j] for p in range(3))
    return R

def tol_ok(res,ref): return res <= mp.mpf('1e-38') + mp.mpf('1e-35')*abs(ref)

def audit(lane):
    u1ang,u2ang,vlang,vrang=LANES[lane]
    U1=wigner_closed(*u1ang); U2=wigner_closed(*u2ang)
    U1b=wigner_exp(*u1ang); U2b=wigner_exp(*u2ang)
    VL=wigner_closed(*vlang); VR=wigner_closed(*vrang)
    route=max(maxentry(U1-U1b),maxentry(U2-U2b))
    unit=max(fnorm(dag(U1)*U1-I3),fnorm(dag(U2)*U2-I3),fnorm(dag(VL)*VL-I3),fnorm(dag(VR)*VR-I3))
    conv_ok=(route<=mp.mpf('1e-38') and unit<=mp.mpf('1e-38'))
    prod_sum_max=mp.mpf('0'); additive_max=mp.mpf('0'); redundancy_max=mp.mpf('0'); covariance_max=mp.mpf('0')
    wrong_p_hits=0; wrong_c_hits=0; total=0
    point_fail=[]
    for r in RHOS:
      for b in BETAS:
        dv,pv,mv=vals(r,b)
        D=recon_prod(U1,dv,U2); TP=recon_prod(U1,pv,U2); TM=recon_prod(U1,mv,U2)
        # Explicit Eq.(7) sum vs matrix product.
        for M,v in ((D,dv),(TP,pv),(TM,mv)):
            S=recon_sum(U1,v,U2); e=maxentry(M-S); prod_sum_max=max(prod_sum_max,e)
            for i in range(3):
                for j in range(3):
                    if not tol_ok(abs(M[i,j]-S[i,j]),M[i,j]): point_fail.append('prod_sum')
        A=TP+TM-D; additive_max=max(additive_max,maxentry(A))
        for i in range(3):
            for j in range(3):
                if not tol_ok(abs(A[i,j]),D[i,j]): point_fail.append('additive')
        # Exact Cartan U(1) redundancy at fixed beta.
        for chi in CHIS:
            U1c=U1*rz(chi); U2c=rz(-chi)*U2
            for v,M in ((dv,D),(pv,TP),(mv,TM)):
                Mc=recon_prod(U1c,v,U2c); q=fnorm(Mc-M)/max(mp.mpf('1'),fnorm(M)); redundancy_max=max(redundancy_max,q)
        # Left/right covariance of the reconstruction map.
        for v,M in ((dv,D),(pv,TP),(mv,TM)):
            lhs=recon_prod(VL*U1,v,U2*VR); rhs=VL*M*VR
            q=fnorm(lhs-rhs)/max(mp.mpf('1'),fnorm(rhs)); covariance_max=max(covariance_max,q)
        # Negative 1: reverse p association in BOTH reduced branches but compare to correct D target.
        badp=recon_prod(U1,list(reversed(pv)),U2)+recon_prod(U1,list(reversed(mv)),U2)
        rp=fnorm(badp-D)/max(mp.mpf('1'),fnorm(D)); wrong_p_hits += int(rp>mp.mpf('1e-8'))
        # Negative 2: conjugate right source factor in + branch only.
        U2c=U2.apply(lambda x: mp.conj(x))
        badc=recon_prod(U1,pv,U2c)+TM
        rc=fnorm(badc-D)/max(mp.mpf('1'),fnorm(D)); wrong_c_hits += int(rc>mp.mpf('1e-8'))
        total+=1
    tests={
      'su2_convention_control':conv_ok,
      'eq7_sum_product_agreement':(not any(x=='prod_sum' for x in point_fail)),
      'full_magnetic_additive_recovery':(not any(x=='additive' for x in point_fail)),
      'cartan_u1_redundancy':redundancy_max<=mp.mpf('1e-35'),
      'left_right_covariance':covariance_max<=mp.mpf('1e-35'),
      'wrong_p_index_negative':mp.mpf(wrong_p_hits)/total>=mp.mpf('.8'),
      'wrong_right_conjugation_negative':mp.mpf(wrong_c_hits)/total>=mp.mpf('.8')}
    return {'lane':lane,'tests':tests,'route_agreement_max':route,'unitarity_max':unit,'sum_product_max':prod_sum_max,'additive_max':additive_max,'cartan_redundancy_max':redundancy_max,'covariance_max':covariance_max,'wrong_p_hit_fraction':mp.mpf(wrong_p_hits)/total,'wrong_conjugation_hit_fraction':mp.mpf(wrong_c_hits)/total,'n_points':total,'valid':True,'pass':all(tests.values())}

def enc(z):
    if isinstance(z,(bool,int,str)) or z is None:return z
    if isinstance(z,dict):return {k:enc(v) for k,v in z.items()}
    if isinstance(z,(list,tuple)):return [enc(v) for v in z]
    try:
        if isinstance(z,(complex,mp.mpc)):return {'re':mp.nstr(mp.re(z),40),'im':mp.nstr(mp.im(z),40)}
        return mp.nstr(z,40)
    except:return str(z)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
    try:
        p=audit(a.lane);p['classification']='ITER457_TOLLER_EQ7_FULL_MAGNETIC_RECONSTRUCTION_QUALIFIED_SCOPED' if p['pass'] else 'SCIENTIFIC_FAIL_ITER457_TOLLER_EQ7_MAGNETIC_RECONSTRUCTION'
    except Exception as e:p={'lane':a.lane,'valid':False,'pass':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True);json.dump(enc(p),open(a.out,'w'),indent=2);print(json.dumps(enc(p),indent=2))
if __name__=='__main__':main()
