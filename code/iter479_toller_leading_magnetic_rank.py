#!/usr/bin/env python3
import json,pathlib
import mpmath as mp
mp.mp.dps=90
GAMMAS=[7,8]; JS=[1,2,5]; MS1=[1,0,-1]
LANES={
'L0': ((mp.mpf('.17'),mp.mpf('.43'),mp.mpf('-.29')),(mp.mpf('-.38'),mp.mpf('.71'),mp.mpf('.52'))),
'L1': ((mp.mpf('-.61'),mp.mpf('.84'),mp.mpf('.33')),(mp.mpf('.47'),mp.mpf('.58'),mp.mpf('-.76'))),
'L2': ((mp.mpf('.93'),mp.mpf('.52'),mp.mpf('-.41')),(mp.mpf('-.74'),mp.mpf('1.03'),mp.mpf('.26'))),
'L3': ((mp.mpf('-1.11'),mp.mpf('.67'),mp.mpf('.89')),(mp.mpf('.68'),mp.mpf('.92'),mp.mpf('-1.02'))),
}

def coeff(j,m,rho,plus=True):
    jx=mp.mpf(j); mx=mp.mpf(m); rx=mp.mpf(rho); ii=mp.j; N=2*j+1
    if plus:
        a=jx+mx+1; b=jx+1-ii*rx; c=1+mx-ii*rx
        pref=mp.gamma(2*jx+2)*mp.gamma(ii*rx-mx)/(mp.gamma(jx-mx+1)*mp.gamma(jx+1+ii*rx))
    else:
        a=jx-mx+1; b=jx+1+ii*rx; c=1-mx+ii*rx
        pref=mp.gamma(2*jx+2)*mp.gamma(-ii*rx+mx)/(mp.gamma(jx+mx+1)*mp.gamma(jx+1-ii*rx))
    return pref*mp.gamma(c)*mp.gamma(N)/(mp.gamma(a)*mp.gamma(b))

def wigner1(a,t,g):
    c=mp.cos(t); s=mp.sin(t); q=mp.sqrt(2)
    d=mp.matrix([[(1+c)/2,-s/q,(1-c)/2],[s/q,c,-s/q],[(1-c)/2,s/q,(1+c)/2]])
    D=mp.matrix(3)
    for i,m in enumerate(MS1):
        for k,n in enumerate(MS1): D[i,k]=mp.e**(-mp.j*m*a)*d[i,k]*mp.e**(-mp.j*n*g)
    return D

def dag(A): return A.transpose_conj()
def fnorm(A): return mp.sqrt(sum(abs(A[i,j])**2 for i in range(A.rows) for j in range(A.cols)))

def rel(a,b): return abs(a-b)/max(mp.mpf('1e-100'),abs(b))

coef_records=[]; coeff_ok=True
for gamma in GAMMAS:
  for j in JS:
    rho=gamma*j
    for m in range(-j,j+1):
      for name,plus in [('plus',True),('minus',False)]:
        C=coeff(j,m,rho,plus)
        finite=bool(mp.isfinite(C.real) and mp.isfinite(C.imag)); nonzero=abs(C)>mp.mpf('1e-70')
        coeff_ok &= finite and nonzero
        coef_records.append({'gamma':gamma,'j':j,'m':m,'branch':name,'coefficient_abs':float(abs(C)),'finite':finite,'nonzero':nonzero})

lane_records=[]; unit_ok=True; det_id_ok=True; full_rank_ok=True; neg_ok=True
for gamma in GAMMAS:
  rho=gamma
  for branch,plus in [('plus',True),('minus',False)]:
    cv=[coeff(1,m,rho,plus) for m in MS1]
    D=mp.diag(cv); prodC=mp.det(D)
    for lane,(a1,a2) in LANES.items():
      U1=wigner1(*a1); U2=wigner1(*a2); I=mp.eye(3)
      unit=max(fnorm(dag(U1)*U1-I),fnorm(dag(U2)*U2-I)); unit_pass=unit<mp.mpf('1e-60'); unit_ok &= unit_pass
      L=U1*D*U2; detL=mp.det(L); rhs=mp.det(U1)*prodC*mp.det(U2); detres=rel(detL,rhs); did=detres<mp.mpf('1e-60'); det_id_ok &= did
      nonsing=abs(detL)>mp.mpf('1e-70'); full_rank_ok &= nonsing
      negs=[]
      for idx in range(3):
        bad=list(cv); bad[idx]=mp.mpc(0); B=U1*mp.diag(bad)*U2; db=abs(mp.det(B)); passed=db<mp.mpf('1e-60'); neg_ok &= passed; negs.append({'zero_index':idx,'det_abs':float(db),'singular_detected':passed})
      lane_records.append({'gamma':gamma,'branch':branch,'lane':lane,'unitarity_residual':float(unit),'determinant_identity_relative_residual':float(detres),'det_abs':float(abs(detL)),'full_rank':nonsing,'negative_controls':negs})
checks={'all_source_leading_coefficients_finite_nonzero':coeff_ok,'j1_eq7_wigner_unitarity':unit_ok,'determinant_identity':det_id_ok,'correct_leading_matrices_full_rank':full_rank_ok,'forced_zero_negative_controls_singular':neg_ok}
ok=all(checks.values())
out={'iteration':479,'classification':'ITER479_SOURCE_TOLLER_LEADING_MAGNETIC_MATRIX_FULL_RANK_QUALIFIED_SCOPED' if ok else 'FAIL_ITER479_LEADING_MAGNETIC_RANK','scientific_pass':ok,'checks':checks,'coefficient_panel':coef_records,'j1_eq7_lanes':lane_records,'algebraic_certificate':'For any j in the source Eq.(7) reconstruction, nonzero diagonal leading coefficients C_m and invertible U1,U2 imply rank(U1 diag(C_m) U2)=2j+1. Explicit j=1 lanes provide a numerical convention/control certificate.','scope':'single-wedge internal magnetic reconstruction only; no intertwiner, multi-edge, group-integration, angular-integration or K5 contracted-collision conclusion','d7_s2':'NOT_CLOSED'}
pathlib.Path('artifacts').mkdir(exist_ok=True); pathlib.Path('artifacts/iter479-summary.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(0 if ok else 2)
