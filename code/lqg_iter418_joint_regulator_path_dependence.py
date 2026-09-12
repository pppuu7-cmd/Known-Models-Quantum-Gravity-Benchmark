#!/usr/bin/env python3
import argparse, itertools, json, math
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--sector', required=True, help='four bits for sigma_1..sigma_4 with sigma_0 fixed +1')
a = p.parse_args()
if len(a.sector) != 4 or any(c not in '01' for c in a.sector):
    raise SystemExit('sector must be four bits')

vertices = list(range(5))
edges = list(itertools.combinations(vertices, 2))

sigma = [1] + [1 if c == '1' else -1 for c in a.sector]

def incidence_row(edge):
    i, j = edge
    r = [0.0] * 4
    if i != 0:
        r[i-1] += 1.0
    if j != 0:
        r[j-1] -= 1.0
    kappa = sigma[i] * sigma[j]
    return [kappa*x for x in r]

B = [incidence_row(e) for e in edges]

def det4(m):
    a = [row[:] for row in m]
    det = 1.0
    for i in range(4):
        pivot = max(range(i,4), key=lambda r: abs(a[r][i]))
        if abs(a[pivot][i]) < 1e-300:
            return 0.0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            det *= -1.0
        piv = a[i][i]
        det *= piv
        for r in range(i+1,4):
            f = a[r][i] / piv
            for c in range(i+1,4):
                a[r][c] -= f * a[i][c]
    return det

def connected_tree(edge_subset):
    if len(edge_subset) != 4:
        return False
    parent = list(range(5))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i,j in edge_subset:
        ri,rj = find(i),find(j)
        if ri == rj:
            return False
        parent[ri] = rj
    root = find(0)
    return all(find(v) == root for v in vertices)

trees = [comb for comb in itertools.combinations(edges,4) if connected_tree(comb)]
assert len(trees) == 125

cycle = {(0,1),(1,2),(2,3),(3,4),(0,4)}
patterns = {
    'isotropic': [1.0]*10,
    'star0_heavy': [2.0 if 0 in e else 1.0 for e in edges],
    'cycle_heavy': [2.0 if e in cycle else 1.0 for e in edges],
    'single_edge_heavy': [2.0 if e == (0,1) else 1.0 for e in edges],
    'mixed': [1.0,2.0,1.5,1.0,2.0,1.0,1.5,2.0,1.0,1.5]
}

def predicted_exponent(exponents):
    amap = dict(zip(edges, exponents))
    total = sum(exponents)
    max_tree = max(sum(amap[e] for e in T) for T in trees)
    return total - max_tree, max_tree

def log_integral_without_constant(t, exponents):
    eps = [t**x for x in exponents]
    M = [[0.0]*4 for _ in range(4)]
    for r, ep in zip(B, eps):
        w = ep**-2
        for i in range(4):
            for j in range(4):
                M[i][j] += w*r[i]*r[j]
    d = det4(M)
    if d <= 0:
        raise RuntimeError('non-positive determinant')
    return -sum(math.log(ep) for ep in eps) - 0.5*math.log(d)

def fit_slope(xs, ys):
    xm = sum(xs)/len(xs); ym = sum(ys)/len(ys)
    num = sum((x-xm)*(y-ym) for x,y in zip(xs,ys))
    den = sum((x-xm)**2 for x in xs)
    return num/den

results = {}
for name, exps in patterns.items():
    pred, max_tree = predicted_exponent(exps)
    ts = [10.0**(-k/2.0) for k in range(4,13)]
    xs = [math.log(t) for t in ts[-5:]]
    ys = [log_integral_without_constant(t, exps) for t in ts[-5:]]
    slope = fit_slope(xs, ys)
    numeric_div = -slope
    results[name] = {
        'sum_exponents': sum(exps),
        'max_tree_exponent_sum': max_tree,
        'predicted_divergence_exponent': pred,
        'numeric_tail_divergence_exponent': numeric_div,
        'abs_error': abs(numeric_div-pred)
    }

unique = sorted({round(v['predicted_divergence_exponent'], 9) for v in results.values()})
path_dependent = len(unique) > 1
assert abs(results['isotropic']['predicted_divergence_exponent'] - 6.0) < 1e-12
assert all(v['abs_error'] < 2e-3 for v in results.values())
assert path_dependent

out = {
    'iteration': 418,
    'sector': a.sector,
    'sigma': sigma,
    'kappa_signs': {f'{i}{j}': sigma[i]*sigma[j] for i,j in edges},
    'spanning_tree_count': len(trees),
    'rank_expected': 4,
    'cycle_nullity_expected': 6,
    'paths': results,
    'unique_predicted_exponents': unique,
    'path_dependent': path_dependent,
    'classification': 'PASS_SCOPED_K5_LINEARIZED_DELTA_LIKE_PRODUCT_HAS_REGULATOR_PATH_DEPENDENT_SINGULAR_SCALING',
    'scope_guard': 'linearized Gaussian delta-like surrogate only; not a proof against correlated spectral i-epsilon or renormalized Toller distributional extension'
}
path = Path('build/lqg-iter418') / f'sector_{a.sector}.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
print(json.dumps(out, sort_keys=True))
