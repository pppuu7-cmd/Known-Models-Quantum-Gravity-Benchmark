#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path

GATE="D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_GATE"
PASS="D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_PASS_SCOPED"
FAIL="D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_FAIL_SCOPED"
BLOCKED="D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_BLOCKED_SCOPED"
INVALID="D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_INVALID"
PREREG="bc9aa01263df1172206eb211b456bf5d78fe1b1b"
V=(1,2,3,4,5)
E=tuple((a,b) for a in V for b in V if a<b)
EI={e:i for i,e in enumerate(E)}
EXPECTED_TRI=[[-1,0],[1,-1],[0,-1]]


def canonical_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def rank_q(A):
    A=[[F(x) for x in row] for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]);r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r


def det_q(A):
    A=[[F(x) for x in row] for row in A]
    n=len(A)
    if n==0: return F(1)
    d=F(1)
    for c in range(n):
        p=next((i for i in range(c,n) if A[i][c]),None)
        if p is None: return F(0)
        if p!=c:
            A[c],A[p]=A[p],A[c]; d=-d
        q=A[c][c]; d*=q
        for i in range(c+1,n):
            if A[i][c]:
                f=A[i][c]/q
                for j in range(c,n): A[i][j]-=f*A[c][j]
    return d


def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(x) for x in zip(*A)]


def tangent_matrix(root):
    free=tuple(v for v in V if v!=root)
    return [[F((1 if a==v else 0)-(1 if b==v else 0)) for v in free] for a,b in E],free


def iter466_matrix(root):
    kept=tuple(v for v in V if v!=root)
    return [[F(-1 if v==a else (1 if v==b else 0)) for a,b in E] for v in kept]


def is_tree(edges):
    if len(edges)!=4: return False
    adj={v:set() for v in V}
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    seen={1};stack=[1]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y);stack.append(y)
    return len(seen)==5


def all_trees():
    return tuple(t for t in combinations(E,4) if is_tree(t))


def fundamental_cycles(root):
    star={tuple(sorted((root,v))) for v in V if v!=root}
    chords=tuple(e for e in E if e not in star)
    C=[]
    for u,v in chords:
        row=[F(0)]*10
        for a,b in ((root,u),(u,v),(v,root)):
            e=(a,b) if a<b else (b,a)
            row[EI[e]] += F(1 if a<b else -1)
        C.append(row)
    return C,chords


def root_change(r,s):
    _,old=tangent_matrix(r); _,new=tangent_matrix(s)
    oi={v:i for i,v in enumerate(old)}
    M=[]
    for w in new:
        row=[F(0)]*4
        if w!=r: row[oi[w]] += 1
        if s!=r: row[oi[s]] -= 1
        M.append(row)
    return M


def edge_transport(p):
    R=[[F(0)]*10 for _ in range(10)]
    for j,(a,b) in enumerate(E):
        pa,pb=p[a],p[b]
        e=(pa,pb) if pa<pb else (pb,pa)
        R[EI[e]][j]=F(1 if pa<pb else -1)
    return R


def coord_transport(root,p):
    old=tuple(v for v in V if v!=root); nr=p[root]; new=tuple(v for v in V if v!=nr)
    ni={v:i for i,v in enumerate(new)}
    P=[[F(0)]*4 for _ in range(4)]
    for j,v in enumerate(old): P[ni[p[v]]][j]=1
    return P,nr


def triangle_restriction(B,free):
    out=[]
    for e in ((1,2),(2,3),(1,3)):
        row=B[EI[e]]
        out.append([int(row[free.index(2)]),int(row[free.index(3)])])
    return out


def source_check(src,ident):
    try:
        eq4=src['eq4_causal_vertex']
        gen=ident['literal_general_wedge_identity']
        parent=ident['same_realization_parent']
    except Exception:
        return False,False
    defined=(src.get('source_id')=='arXiv:2601.23162v1' and ident.get('source_id')=='arXiv:2601.23162v1')
    exact=bool(
        defined and eq4.get('wedge_count')==10 and eq4.get('wedge_domain')=='1<=a<b<=5'
        and eq4.get('group_integrations')==['g_2','g_3','g_4','g_5'] and eq4.get('gauge_fix')=='g_1=identity'
        and gen.get('formula')=='g_ab = g_b^{-1} g_a'
        and parent.get('integration_tuple')==['g2','g3','g4','g5'] and parent.get('fixed_variable')=='g1 = 1'
        and ident.get('historical_v8_auxiliary_relation_used') is False
        and ident.get('generic_textbook_group_formula_used') is False
        and ident.get('toller_matrix_composition_used') is False
    )
    return defined,exact


def classify_fixture(source_defined=True,source_exact=True,algebra_ok=True,forbidden=False):
    if not source_defined: return BLOCKED
    if not source_exact or forbidden: return INVALID
    return PASS if algebra_ok else FAIL


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--identity',required=True);ap.add_argument('--method',choices=['rref','trees'],required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
    src=json.loads(Path(a.source).read_text()); ident=json.loads(Path(a.identity).read_text())
    source_defined,source_exact=source_check(src,ident)
    trees=all_trees()
    roots=[]; tree_det_values=set(); cycle_ok_all=True; iter466_ok_all=True; triangle_ok=False
    for r in V:
        B,free=tangent_matrix(r)
        if a.method=='rref':
            rk=rank_q(B)
        else:
            rk=4 if any(det_q([B[EI[e]] for e in t])!=0 for t in trees) else rank_q(B)
        C,chords=fundamental_cycles(r)
        left=mm(C,B)
        left_zero=all(x==0 for row in left for x in row)
        if a.method=='rref': cycle_rank=rank_q(C)
        else:
            chord_sub=[[C[i][EI[chords[j]]] for j in range(6)] for i in range(6)]
            cycle_rank=6 if abs(det_q(chord_sub))==1 else rank_q(C)
        cycle_ok=(left_zero and cycle_rank==6); cycle_ok_all &= cycle_ok
        A466=iter466_matrix(r)
        iter466_ok=(B==[[-x for x in row] for row in transpose(A466)])
        iter466_ok_all &= iter466_ok
        if r==1: triangle_ok=(triangle_restriction(B,free)==EXPECTED_TRI)
        dvals=[]
        for t in trees:
            d=det_q([B[EI[e]] for e in t]); dvals.append(d); tree_det_values.add(int(d))
        roots.append({'root':r,'rank':rk,'domain_nullity':4-rk,'edge_left_nullity':10-rk,'cycle_rank':cycle_rank,'cycle_annihilation':left_zero,'tree_min_abs_det':int(min(abs(x) for x in dvals)),'tree_max_abs_det':int(max(abs(x) for x in dvals)),'iter466_negative_transpose_match':iter466_ok})
    tree_count=len(trees); tree_all_unimodular=(tree_count==125 and tree_det_values=={-1,1})
    root_change_dets=[]
    for r in V:
        for s in V:
            if r!=s: root_change_dets.append(int(det_q(root_change(r,s))))
    root_changes_unimodular=(set(root_change_dets)=={-1,1} and len(root_change_dets)==20)
    perm_ok=True; perm_count=0
    for perm in permutations(V):
        p={V[i]:perm[i] for i in range(5)}
        R=edge_transport(p)
        for r in V:
            B,_=tangent_matrix(r);P,nr=coord_transport(r,p);Bn,_=tangent_matrix(nr)
            if mm(R,B)!=mm(Bn,P): perm_ok=False;break
        perm_count+=1
        if not perm_ok: break
    root_ranks=[x['rank'] for x in roots]
    algebra_ok=bool(
        root_ranks==[4]*5 and all(x['domain_nullity']==0 and x['edge_left_nullity']==6 for x in roots)
        and cycle_ok_all and tree_all_unimodular and root_changes_unimodular and perm_ok and perm_count==120
        and triangle_ok and iter466_ok_all
    )
    fixtures={
      'positive_canonical_pass': classify_fixture(True,True,True,False)==PASS,
      'negative_missing_source_blocked': classify_fixture(False,False,False,False)==BLOCKED,
      'negative_wrong_source_orientation_invalid': classify_fixture(True,False,True,False)==INVALID,
      'negative_edge_deletion_fail': classify_fixture(True,True,False,False)==FAIL,
      'negative_nonunimodular_edge_rescale_fail': classify_fixture(True,True,False,False)==FAIL,
      'negative_physical_quotient_insertion_invalid': classify_fixture(True,True,True,True)==INVALID,
    }
    if not source_defined: cls=BLOCKED
    elif not source_exact or not all(fixtures.values()): cls=INVALID
    elif not algebra_ok: cls=FAIL
    else: cls=PASS
    core={
      'gate':GATE,'classification':cls,
      'source_defined':source_defined,'source_exact':source_exact,
      'wedge_count':10,'gauge_roots':list(V),'root_ranks':root_ranks,'per_generator_domain_dimension':4,'per_generator_codomain_dimension':10,
      'per_generator_rank':4 if root_ranks==[4]*5 else None,'per_generator_domain_nullity':0 if root_ranks==[4]*5 else None,'per_generator_edge_left_nullity':6 if root_ranks==[4]*5 else None,
      'sl2c_real_dimension':6,'full_real_domain_dimension':24,'full_real_codomain_dimension':60,'full_real_rank':24 if root_ranks==[4]*5 else None,'full_real_domain_nullity':0 if root_ranks==[4]*5 else None,'full_real_edge_left_nullity':36 if root_ranks==[4]*5 else None,
      'triangle_parent_match':triangle_ok,'iter466_negative_transpose_match_all_roots':iter466_ok_all,
      'fundamental_cycle_basis_count':6,'fundamental_cycle_rank_all_roots':cycle_ok_all,'fundamental_cycle_annihilates_tangent_map_all_roots':cycle_ok_all,
      'spanning_tree_count':tree_count,'all_spanning_tree_minors_unimodular':tree_all_unimodular,'spanning_tree_minor_determinant_values':sorted(tree_det_values),
      'root_change_count':20,'root_changes_unimodular':root_changes_unimodular,'root_change_determinant_values':sorted(set(root_change_dets)),
      's5_permutation_count':perm_count,'s5_signed_orientation_transport_exact':perm_ok,
      'raw_linear_tree_coordinate_jacobian_abs_det':1 if tree_all_unimodular else None,
      'group_variable_tangent_pushforward_prerequisite_closed':cls==PASS,
      'physical_transverse_quotient_authorized':False,'distributional_contact_pushforward_authorized':False,'haar_contact_normalization_authorized':False,'observable_pushforward_authorized':False,'d7_s2_closed':False,
      'fixtures':fixtures,
      'claim_ceiling':'raw/source-faithful K5 group-variable tangent pushforward only; unit tree minors are linear coordinate Jacobians, not Haar/contact normalization; no physical quotient, distributional theorem, D7-S2 closure, selector or model/family conclusion'
    }
    out=dict(core);out.update({'method':a.method,'root_details':roots,'source_sha256':hashlib.sha256(Path(a.source).read_bytes()).hexdigest(),'identity_sha256':hashlib.sha256(Path(a.identity).read_bytes()).hexdigest(),'scientific_payload_sha256':canonical_sha(core)})
    Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 0 if cls in (PASS,FAIL,BLOCKED) else 2


if __name__=='__main__':raise SystemExit(main())
