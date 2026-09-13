#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import numpy as np

VERTICES = tuple(range(5))
EDGES = tuple((a,b) for a in VERTICES for b in VERTICES if a < b)
LETTERS = list("abcdefghijklmnopqrst")


def relerr(a,b):
    return float(abs(a-b) / max(1.0, abs(a), abs(b)))


def make_labels():
    labels = {}
    k = 0
    for a,b in EDGES:
        labels[(a,b,a)] = LETTERS[k]; k += 1
        labels[(a,b,b)] = LETTERS[k]; k += 1
    return labels

LABELS = make_labels()


def edge_label_pair(e):
    a,b = e
    return LABELS[(a,b,a)] + LABELS[(a,b,b)]


def vertex_neighbors(v):
    return tuple(n for n in VERTICES if n != v)


def vertex_label(v,n):
    a,b = sorted((v,n))
    return LABELS[(a,b,v)]


def contract(edge_tensors, vertex_tensors, vertex_orders=None, optimize='greedy'):
    operands = []
    subs = []
    for e in EDGES:
        operands.append(edge_tensors[e]); subs.append(edge_label_pair(e))
    for v in VERTICES:
        order = vertex_neighbors(v) if vertex_orders is None else tuple(vertex_orders[v])
        operands.append(vertex_tensors[v]); subs.append(''.join(vertex_label(v,n) for n in order))
    expr = ','.join(subs) + '->'
    return np.einsum(expr, *operands, optimize=optimize)


def normalized_complex(rng, shape):
    x = rng.normal(size=shape) + 1j*rng.normal(size=shape)
    n = np.linalg.norm(x)
    return x/n if n else x


def relabel_network(edge_tensors, vertex_tensors, perm):
    new_e = {}
    for a,b in EDGES:
        pa,pb = perm[a],perm[b]
        ne = tuple(sorted((pa,pb)))
        m = edge_tensors[(a,b)]
        new_e[ne] = m if pa < pb else m.T
    new_v = {}
    for v in VERTICES:
        mapped_v = perm[v]
        old_order = list(vertex_neighbors(v))
        target_new_order = list(vertex_neighbors(mapped_v))
        wanted_old_neighbors = [next(n for n in old_order if perm[n] == nn) for nn in target_new_order]
        axes = [old_order.index(n) for n in wanted_old_neighbors]
        new_v[mapped_v] = np.transpose(vertex_tensors[v], axes)
    return new_e, new_v


def lane(seed):
    rng = np.random.default_rng(seed)
    tplus, tminus, dmat = {}, {}, {}
    for e in EDGES:
        tplus[e] = normalized_complex(rng,(2,2))
        tminus[e] = normalized_complex(rng,(2,2))
        dmat[e] = tplus[e] + tminus[e]
    verts = {v: normalized_complex(rng,(2,2,2,2)) for v in VERTICES}

    counts = {c:0 for c in LETTERS}
    for e in EDGES:
        for c in edge_label_pair(e): counts[c]+=1
    for v in VERTICES:
        for n in vertex_neighbors(v): counts[vertex_label(v,n)]+=1
    incidence_exact = all(counts[c] == 2 for c in LETTERS)

    aD = complex(contract(dmat, verts, optimize='greedy'))
    scalar_valid = incidence_exact and np.isfinite(aD.real) and np.isfinite(aD.imag) and np.asarray(aD).shape == ()
    eq5_res = max(float(np.max(np.abs(dmat[e]-(tplus[e]+tminus[e])))) for e in EDGES)

    branch_sum = 0j
    for mask in range(1<<len(EDGES)):
        chosen = {}
        for i,e in enumerate(EDGES): chosen[e] = tplus[e] if ((mask>>i)&1) else tminus[e]
        branch_sum += complex(contract(chosen, verts, optimize='greedy'))
    eq6_rel = relerr(branch_sum,aD)
    eq6_abs = float(abs(branch_sum-aD))
    eq6_abs_lim = 5e-11*(1.0+abs(aD))

    # Frozen nontrivial S5 relabeling derived from seed, with rejection of identity.
    p = np.arange(5); rng.shuffle(p)
    if np.all(p == np.arange(5)): p = np.array([1,2,3,4,0])
    perm = {i:int(p[i]) for i in VERTICES}
    pe,pv = relabel_network(dmat,verts,perm)
    aperm = complex(contract(pe,pv,optimize='greedy'))
    perm_rel = relerr(aperm,aD)

    # Reorder each intertwiner's legs while supplying the matching leg-order metadata.
    rv, orders = {}, {}
    for v in VERTICES:
        canon = list(vertex_neighbors(v))
        ax = np.arange(4); rng.shuffle(ax)
        rv[v] = np.transpose(verts[v], list(ax))
        orders[v] = tuple(canon[int(i)] for i in ax)
    areorder = complex(contract(dmat,rv,vertex_orders=orders,optimize='greedy'))
    reorder_rel = relerr(areorder,aD)

    # Negative incidence control: transpose one non-symmetric wedge without compensating at vertices.
    bad_edges = {e:x.copy() for e,x in dmat.items()}
    bad_edge = EDGES[0]
    bad_edges[bad_edge] = bad_edges[bad_edge].T.copy()
    abad = complex(contract(bad_edges,verts,optimize='greedy'))
    bad_incidence_delta = relerr(abad,aD)

    # Negative Eq.(5) control: perturb one D entry, leaving branch tensors untouched.
    bad_d = {e:x.copy() for e,x in dmat.items()}
    bad_d[EDGES[1]][0,0] += 1e-3*(1+0.5j)
    abadD = complex(contract(bad_d,verts,optimize='greedy'))
    bad_eq5_delta = relerr(abadD,branch_sum)

    # Independently assembled contraction path: reverse operand ordering and use optimal path search.
    # Reversal leaves labels attached to tensors, so the scalar must be unchanged.
    operands=[]; subs=[]
    for v in reversed(VERTICES):
        operands.append(verts[v]); subs.append(''.join(vertex_label(v,n) for n in vertex_neighbors(v)))
    for e in reversed(EDGES):
        operands.append(dmat[e]); subs.append(edge_label_pair(e))
    a2 = complex(np.einsum(','.join(subs)+'->',*operands,optimize='optimal'))
    repeat_rel = relerr(a2,aD)

    checks = {
      'scalar_contraction_valid': bool(scalar_valid),
      'eq5_local_exact': eq5_res <= 1e-13,
      'eq6_full_branch_sum': eq6_rel <= 5e-11 and eq6_abs <= eq6_abs_lim,
      'permutation_covariance': perm_rel <= 5e-11,
      'intertwiner_leg_order_invariance': reorder_rel <= 5e-11,
      'negative_incidence_control': bad_incidence_delta >= 1e-6,
      'negative_eq5_control': bad_eq5_delta >= 1e-8,
      'precision_repeatability': repeat_rel <= 5e-11,
    }
    return {
      'iteration':453,'seed':seed,'source_id':'arXiv:2601.23162v1',
      'checks':checks,'qualified':all(checks.values()),
      'metrics':{
        'eq5_max_abs_residual':eq5_res,'eq6_relative_residual':eq6_rel,'eq6_absolute_residual':eq6_abs,
        'eq6_absolute_limit':eq6_abs_lim,'permutation_relative_residual':perm_rel,
        'leg_order_relative_residual':reorder_rel,'negative_incidence_relative_delta':bad_incidence_delta,
        'negative_eq5_relative_delta':bad_eq5_delta,'repeat_relative_residual':repeat_rel,
        'A_D_abs':float(abs(aD)),'branch_sum_abs':float(abs(branch_sum))
      },
      'scope_guard':'Finite deterministic Eq.(4) contraction-topology qualification only; no physical Toller-integral finiteness or D7-S2 closure.'
    }


def aggregate(paths):
    lanes=[json.loads(Path(p).read_text()) for p in paths]
    valid = len(lanes)==4 and sorted(x['seed'] for x in lanes)==[17,29,43,71]
    q = sum(bool(x.get('qualified')) for x in lanes)
    passed = valid and q==4 and all(x.get('source_id')=='arXiv:2601.23162v1' for x in lanes)
    return {
      'iteration':453,'lane_count':len(lanes),'qualified_lanes':q,'structurally_valid':valid,
      'classification':'ITER453_EQ4_MAGNETIC_INTERTWINER_CONTRACTION_TOPOLOGY_QUALIFIED' if passed else 'ITER453_EQ4_CONTRACTION_TOPOLOGY_QUALIFICATION_FAIL',
      'lanes':sorted(lanes,key=lambda x:x['seed']),
      'scope_guard':'PASS is executable finite-panel topology/algebra qualification only; no convergence/finiteness/D7 terminal claim.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seed',type=int); ap.add_argument('--out',required=True); ap.add_argument('--aggregate',nargs='*')
    args=ap.parse_args()
    result=aggregate(args.aggregate) if args.aggregate else lane(args.seed)
    Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")

if __name__=='__main__': main()
