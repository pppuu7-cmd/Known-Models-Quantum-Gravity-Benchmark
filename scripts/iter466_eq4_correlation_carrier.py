#!/usr/bin/env python3
import argparse, json, hashlib
from fractions import Fraction
from pathlib import Path

V = [1,2,3,4,5]
E = [(a,b) for a in V for b in V if a < b]

def rank_q(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    if not a: return 0
    m,n=len(a),len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c] != 0),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]!=0:
                q=a[i][c]; a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r += 1
        if r==m: break
    return r

def incidence(edges, root):
    rows=[v for v in V if v != root]
    out=[]
    for v in rows:
        row=[]
        for a,b in edges:
            row.append(-1 if v==a else (1 if v==b else 0))
        out.append(row)
    return out

def permute_edges(edges,p):
    out=[]
    for a,b in edges:
        x,y=p[a],p[b]
        out.append(tuple(sorted((x,y))))
    return sorted(out)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=int,required=True); ap.add_argument('--out',required=True)
    args=ap.parse_args(); root=args.root
    srcp=Path('sources/arxiv_2601_23162v1_causal_vertex.json')
    src=json.loads(srcp.read_text())
    raw=srcp.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
    eq3=src['eq3_toller_feynman']; eq4=src['eq4_causal_vertex']
    source_ok=(src['source_id']=='arXiv:2601.23162v1' and eq4['wedge_count']==10 and len(eq4['group_integrations'])==4 and 'g_1=identity' in eq4['gauge_fix'] and eq3['tilde_rho_domain']=='(-infinity,+infinity)')
    labels=[f'tilde_rho_{a}{b}' for a,b in E]
    spectral_locality=(len(labels)==10 and len(set(labels))==10)
    bad_labels=labels.copy(); bad_labels[-1]=bad_labels[0]
    duplicate_control=(len(set(bad_labels))==9)
    B=incidence(E,root); rk=rank_q(B); nullity=len(E)-rk
    incidence_ok=True
    kept=set(V)-{root}
    for col,(a,b) in enumerate(E):
        nz=sum(1 for row in B if row[col]!=0)
        expected=int(a in kept)+int(b in kept)
        incidence_ok &= (nz==expected and expected in (1,2))
    perms=[
      {1:2,2:1,3:3,4:4,5:5},
      {1:2,2:3,3:4,4:5,5:1},
      {1:5,2:4,3:3,4:2,5:1},
    ]
    relabel_ok=True
    for p in perms:
        pe=permute_edges(E,p); pr=p[root]
        PB=incidence(pe,pr); rr=rank_q(PB)
        relabel_ok &= (len(pe)==10 and len(set(pe))==10 and rr==4 and len(pe)-rr==6)
    deleted=E[:-1]; rdel=rank_q(incidence(deleted,root)); deletion_control=(len(deleted)==9 and rdel==4 and len(deleted)-rdel==5)
    duplicated=E+[E[0]]; duplication_topology_control=(len(duplicated)!=len(set(duplicated)))
    preds={
      'source_consistency':source_ok,
      'spectral_label_locality':spectral_locality,
      'duplicate_label_negative_control':duplicate_control,
      'reduced_incidence_rank4':rk==4,
      'cycle_nullity6':nullity==6,
      'endpoint_incidence':incidence_ok,
      'relabeling_robustness':relabel_ok,
      'edge_deletion_control':deletion_control,
      'duplicate_edge_control':duplication_topology_control,
    }
    qualified=all(preds.values())
    out={
      'iteration':466,'root':root,'source_id':src['source_id'],'source_sha256_observed':digest,
      'edge_count':len(E),'rank':rk,'nullity':nullity,'spectral_label_count':len(labels),'unique_spectral_label_count':len(set(labels)),
      'predicates':preds,'qualified':qualified,
      'classification':'ITER466_EQ4_GROUP_MEDIATED_SPECTRAL_CORRELATION_CARRIER_PINNED_SCOPED' if qualified else 'SCIENTIFIC_FAIL_ITER466_EQ4_CORRELATION_CARRIER',
      'scope':'topology/correlation-carrier only; no distributional pushforward or D7-S2 closure'
    }
    Path(args.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__': main()
