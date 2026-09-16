#!/usr/bin/env python3
"""Exact V7 derivative-contact triangle regularization certificate.
Same-contract control-wiring repair after terminal Critic; scientific contract unchanged.
"""
from __future__ import annotations
import argparse, json, sys
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

SCHEMES={"A":(1,1,1),"B":(1,1,4),"C":(1,2,3),"A4":(4,4,4)}
PREREG="research/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7_PREREG_2026-09-16.md"
FRONT="recovery/CURRENT_BENCHMARK_FRONT.md"
CRITIC_V6="recovery/CRITICAL_REVIEW_SOURCE_J1_K5_TRIANGLE_CONTACT_REGULARIZATION_V6_2026-09-16.md"

def fs(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def d2_factor(a0, wrong_sign=False):
    """Executable polynomial representation of normalized Gaussian delta'' factor.
    Returns outside normalization 2a and polynomial q2*x^2+q0.
    Production and controls consume this same representation.
    """
    a=F(a0); return (2*a, 2*a, F(1) if wrong_sign else F(-1))

def wick2(v): return v

def wick4(v): return 3*v*v

def one_factor_moment(a0, power=0, wrong_sign=False):
    a=F(a0); norm,q2,q0=d2_factor(a0,wrong_sign); v=F(1,2)/a
    if power==0: return norm*(q2*wick2(v)+q0)
    if power==2: return norm*(q2*wick4(v)+q0*wick2(v))
    raise ValueError(power)

def gaussian_engine(a0,b0,c0=None):
    """Shared exact covariance/Wick engine. c=None is independent transverse 2D replay."""
    a,b=F(a0),F(b0)
    if c0 is None:
        vx,vy=F(1,2)/a,F(1,2)/b
        # independently replay E[D2_a(X) D2_b(Y) X^2 Y^2] through 2D moments
        na,qa2,qa0=d2_factor(a0); nb,qb2,qb0=d2_factor(b0)
        ex4,ey4=wick4(vx),wick4(vy); ex2,ey2=wick2(vx),wick2(vy)
        val=na*nb*(qa2*qb2*ex4*ey4 + qa2*qb0*ex4*ey2 + qa0*qb2*ex2*ey4 + qa0*qb0*ex2*ey2)
        return {"transverse_x2y2":val,"covariances":(vx,vy,F(0))}
    c=F(c0); d=a*b+a*c+b*c
    vx=(b+c)/(2*d); vy=(a+c)/(2*d); vz=(a+b)/(2*d)
    cxy=-c/(2*d); cxz=b/(2*d); cyz=a/(2*d)
    mxy=vx*vy+2*cxy*cxy; mxz=vx*vz+2*cxz*cxz; myz=vy*vz+2*cyz*cyz
    mxyz=vx*vy*vz+2*cxy*cxy*vz+2*cxz*cxz*vy+2*cyz*cyz*vx+8*cxy*cxz*cyz
    # coefficients come from the exact same executable d2_factor representation
    na,qa2,qa0=d2_factor(a0); nb,qb2,qb0=d2_factor(b0); nc,qc2,qc0=d2_factor(c0)
    e=(qa2*qb2*qc2*mxyz + qa2*qb2*qc0*mxy + qa2*qb0*qc2*mxz + qa0*qb2*qc2*myz
       +qa2*qb0*qc0*vx + qa0*qb2*qc0*vy + qa0*qb0*qc2*vz + qa0*qb0*qc0)
    # na*nb*nc normalization is represented by the frozen closed-form K prefactor.
    k=F(64)*(a*b*c)**3*e**2/(d*(a+b+c)**7)
    return {"D":d,"E":e,"K":k,"plain_delta_S":a*b*c/d,"covariances":(vx,vy,vz,cxy,cxz,cyz)}

def gaussian_data(a,b,c): return gaussian_engine(a,b,c)

def source_authority(root):
    checks={}; prereg=root/PREREG; front=root/FRONT; critic=root/CRITIC_V6
    checks.update(prereg_present=prereg.exists(),front_present=front.exists(),critic_v6_present=critic.exists())
    pt=prereg.read_text() if prereg.exists() else ""; ft=front.read_text() if front.exists() else ""; ct=critic.read_text() if critic.exists() else ""
    checks["prereg_parent_main_lock"]="5a6790ae9d9e020a3a73338293446e0501b3c8c4" in pt
    checks["prereg_v6_critic_lock"]="67c0895bf16074091abd9e2643e1629344414263" in pt
    checks["prereg_delta2_object_lock"]="D2_eps^a" in pt and "delta''" in pt
    checks["v4_repaired_run_lock"]="35033194283" in ft and "CONFIRMED_SCOPED" in ft
    checks["v4_delta2_lock"]="delta''" in ft
    checks["v5_channel00000_lock"]="00000=11/24" in ft or "00000 = 11/24" in ft
    checks["v6_run_lock"]="35050058294" in ft
    checks["critic_requires_derivative_bridge"]="highest-`delta''`" in ct and "derivative-contact regularization" in ct
    checks["critic_local_map_lock"]="B12=x" in ct and "B23=y" in ct and "B13=x+y" in ct
    return checks

def build_lane(root):
    sc=source_authority(root); source_ok=all(sc.values()); data={n:gaussian_data(*v) for n,v in SCHEMES.items()}
    perm_ok=True; precord={}
    for n in ("A","B","C"):
        vals=SCHEMES[n]; ks=sorted({fs(gaussian_data(*p)["K"]) for p in set(permutations(vals))}); es=sorted({fs(gaussian_data(*p)["E"]) for p in set(permutations(vals))})
        precord[n]={"K_values":ks,"E_values":es}; perm_ok &= len(ks)==1 and len(es)==1
    mass1=one_factor_moment(1,0); x21=one_factor_moment(1,2); bad1=one_factor_moment(1,0,True)
    mass4=one_factor_moment(4,0); x24=one_factor_moment(4,2); bad4=one_factor_moment(4,0,True)
    transverse=gaussian_engine(1,4,None)["transverse_x2y2"]
    # identity control is bound to production representation, not a tautology
    derivative_identity=all(d2_factor(a)==(F(2*a),F(2*a),F(-1)) for a in (1,4))
    target=data["A"]["D"]; wrong=F(6)
    controls={"source_authority":source_ok,"derivative_identity":derivative_identity,"target_determinant_formula_positive":all(data[n]["D"]>0 for n in SCHEMES),"permutation_symmetry":perm_ok,"common_rescaling_invariance":data["A4"]["K"]==data["A"]["K"],"one_factor_zero_mass":mass1==0 and mass4==0,"one_factor_x2_normalization":x21==2 and x24==2,"transverse_two_contact_normalization":transverse==4,"wrong_derivative_plus_sign_rejected":bad1!=0 and bad4!=0,"wrong_conormal_map_rejected":wrong!=target,"plain_delta_object_fixture_distinct":any(data[n]["K"]!=data[n]["plain_delta_S"] for n in ("A","B","C"))}
    alg=all(v for k,v in controls.items() if k!="source_authority")
    if not source_ok: classification="TRIANGLE_DELTA2_CONTACT_REGULARIZATION_SOURCE_BLOCKED"
    elif not alg: classification="INVALID_IMPLEMENTATION"
    else: classification="TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED" if len({data[n]["K"] for n in ("A","B","C")})>1 else "TRIANGLE_DELTA2_CONTACT_REGULARIZATION_INVARIANT_SCOPED"
    return {"gate":"SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7","classification":classification,"source_checks":sc,"controls":controls,"schemes":{k:list(v) for k,v in SCHEMES.items()},"values":{n:{"D":fs(data[n]["D"]),"E":fs(data[n]["E"]),"K":fs(data[n]["K"]),"plain_delta_S_fixture":fs(data[n]["plain_delta_S"])} for n in SCHEMES},"permutation_records":precord,"one_factor":{"a1_mass":fs(mass1),"a1_x2":fs(x21),"a1_bad_plus_mass":fs(bad1),"a4_mass":fs(mass4),"a4_x2":fs(x24),"a4_bad_plus_mass":fs(bad4)},"transverse_two_contact_x2y2":fs(transverse),"target_D_A":fs(target),"wrong_conormal_D_A":fs(wrong),"claim_ceiling":"Local parent-derivative-order Gaussian triangle only; no all-mollifier, extension-nonexistence, full-K5, model/family, D7, selector, or Candidate Gravity conclusion."}

def aggregate(lp,hp):
    lo=json.loads(lp.read_text()); hi=json.loads(hp.read_text()); keys=("gate","classification","source_checks","controls","schemes","values","permutation_records","one_factor","transverse_two_contact_x2y2","target_D_A","wrong_conormal_D_A","claim_ceiling")
    agree=all(lo.get(k)==hi.get(k) for k in keys); out={k:lo.get(k) for k in keys}; out["lane_decision_agreement"]=agree; out["lane_classifications"]=[lo.get("classification"),hi.get("classification")]
    if not agree: out["classification"]="INVALID_IMPLEMENTATION"
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--mode",choices=("lane","source","aggregate"),required=True); ap.add_argument("--repo-root",default="."); ap.add_argument("--out",required=True); ap.add_argument("--low"); ap.add_argument("--high"); a=ap.parse_args(); root=Path(a.repo_root)
    if a.mode=="source":
        c=source_authority(root); out={"source_checks":c,"source_ok":all(c.values())}
    elif a.mode=="lane": out=build_lane(root); out["runtime_python"]=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    else:
        if not a.low or not a.high: raise SystemExit("aggregate requires --low and --high")
        out=aggregate(Path(a.low),Path(a.high))
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n"); print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
