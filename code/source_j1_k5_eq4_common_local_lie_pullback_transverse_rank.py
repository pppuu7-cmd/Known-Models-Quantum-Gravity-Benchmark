#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

GATE="SOURCE_J1_K5_EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_GATE"
PASS="EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_PASS_SCOPED"
FAIL="EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_FAIL_SCOPED"
BLOCKED="EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_BLOCKED_SCOPED"
INVALID="EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_INVALID"

RAW=[[F(-1),F(0)],[F(1),F(-1)],[F(0),F(-1)]]

def rank_rref(a):
    a=[row[:] for row in a]; m=len(a); n=len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def det2(a,r0,r1,c0,c1):
    return a[r0][c0]*a[r1][c1]-a[r0][c1]*a[r1][c0]

def rank_minors(a):
    m=len(a); n=len(a[0]);
    if all(x==0 for row in a for x in row): return 0
    if n>=2 and any(det2(a,i,j,c,d) for i in range(m) for j in range(i+1,m) for c in range(n) for d in range(c+1,n)):
        return 2 if n==2 else rank_rref(a)
    return 1

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    if not d: return None
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

def basis_controls(method):
    rk=rank_rref if method=='rref' else rank_minors
    base=rk(RAW)
    domain=[[[F(1),F(1)],[F(0),F(1)]],[[F(2),F(1)],[F(1),F(1)]]]
    codomain=[[[F(1),F(0),F(0)],[F(1),F(1),F(0)],[F(0),F(0),F(1)]],[[F(1),F(1),F(0)],[F(0),F(1),F(1)],[F(0),F(0),F(1)]]]
    vals=[]
    for D,C in zip(domain,codomain):
        Di=inv2(D); assert Di is not None
        vals.append(rk(mm(C,mm(RAW,Di))))
    return base,vals

def s3_raw_ranks(method):
    rk=rank_rref if method=='rref' else rank_minors
    vals=[]
    # All six vertex permutations act on an oriented triangle incidence map by
    # invertible row permutations/signs and a change of the two free vertex coordinates.
    # Construct each directly from Y_ab=X_a-X_b with the first permuted vertex fixed.
    for p in permutations((0,1,2)):
        fixed=p[0]; free=[p[1],p[2]]; edges=[tuple(sorted((p[0],p[1]))),tuple(sorted((p[1],p[2]))),tuple(sorted((p[0],p[2])))]
        rows=[]
        for a,b in edges:
            row=[]
            for v in free:
                row.append(F((1 if a==v else 0)-(1 if b==v else 0)))
            rows.append(row)
        vals.append(rk(rows))
    return vals

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--authority',required=True); ap.add_argument('--method',choices=['rref','minors'],required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    auth=json.loads(Path(a.authority).read_text())
    ass=auth['authority_assessment']; maps=auth['source_authorized_raw_object']['maps']
    expected={'G12':'g_2^{-1}','G23':'g_3^{-1} g_2','G13':'g_3^{-1}'}
    source_ok=(maps==expected and ass['raw_common_local_group_map_defined'] is True and ass['raw_local_lie_differential_mathematically_defined'] is True)
    rk=(rank_rref if a.method=='rref' else rank_minors)(RAW)
    base,basis=basis_controls(a.method); s3=s3_raw_ranks(a.method)
    raw_ok=(rk==base and all(x==rk for x in basis) and all(x==rk for x in s3))
    # SL(2,C) has real Lie-algebra dimension 6; the map is six identical generator blocks.
    total_raw_rank=6*rk
    raw_domain_dim=12; raw_codomain_dim=18
    left_relation=[F(1),F(1),F(-1)]
    left_ann=[sum(left_relation[i]*RAW[i][j] for i in range(3)) for j in range(2)]
    quotient_fields=['physical_transverse_quotient_defined','physical_quotient_projection_defined','simultaneous_contact_scalar_pullback_to_physical_quotient_defined','jacobian_haar_contact_normalization_transport_defined','s3_orientation_coordinate_transport_on_physical_quotient_defined']
    missing=[k for k in quotient_fields if ass.get(k) is not True]
    fixtures={
      'positive_full_rank_abstract': rank_rref([[F(1),F(0)],[F(0),F(1)]])==2,
      'negative_explicit_rank_deficient': rank_rref([[F(1),F(0)],[F(2),F(0)]])==1,
      'negative_noninvertible_basis_invalid': inv2([[F(1),F(1)],[F(2),F(2)]]) is None,
      'negative_undefined_quotient_blocked': len(missing)>0,
      'negative_raw_rank_not_physical_rank': len(missing)>0,
      'left_relation_exact': left_ann==[F(0),F(0)]
    }
    if not source_ok or not raw_ok or not all(fixtures.values()): cls=INVALID
    elif missing: cls=BLOCKED
    else:
        # This branch is unreachable for the frozen authority unless a future gate prospectively supplies the missing quotient fields.
        cls=PASS if total_raw_rank==raw_domain_dim else FAIL
    core={
      'gate':GATE,'classification':cls,'method':a.method,'source_provenance_ok':source_ok,
      'raw_generator_matrix':[[int(x) for x in row] for row in RAW],
      'raw_generator_rank':rk,'raw_group_real_dimension':6,'raw_domain_dimension':raw_domain_dim,'raw_codomain_dimension':raw_codomain_dim,'raw_total_rank':total_raw_rank,'raw_domain_nullity':raw_domain_dim-total_raw_rank,'raw_codomain_left_nullity':raw_codomain_dim-total_raw_rank,
      'generator_left_relation':[1,1,-1],'basis_replacement_ranks':basis,'s3_raw_ranks':s3,'raw_rank_controls_ok':raw_ok,
      'missing_physical_authority_fields':missing,'physical_transverse_rank':None if missing else total_raw_rank,
      'rank_status':'raw_exact__physical_undefined' if missing else 'physical_defined',
      'fixtures':fixtures,
      'scientific_boundary':'raw local Lie differential is exact; physical transverse rank remains undefined unless frozen quotient and normalization transport are source-authorized; BLOCKED != FAIL; raw rank != physical rank'
    }
    raw=json.dumps(core,sort_keys=True,separators=(',',':')).encode(); core['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest()
    Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(core,indent=2,sort_keys=True)+'\n')
    print(json.dumps(core,indent=2,sort_keys=True)); return 0 if cls in (PASS,FAIL,BLOCKED) else 2
if __name__=='__main__': raise SystemExit(main())
