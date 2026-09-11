#!/usr/bin/env python3
import argparse, json, math, pathlib

p = argparse.ArgumentParser()
p.add_argument('--N', type=float, required=True)
p.add_argument('--x', type=float, required=True, help='x=beta/(12 alpha)')
p.add_argument('--output', required=True)
a = p.parse_args()

assert a.N > 0.0
assert 0.0 <= a.x < 1.0
r_star = 12.0 / (a.N * a.N)
ratio = 1.0 / (1.0 - a.x)
r_iho = r_star * ratio
assert math.isfinite(r_iho) and r_iho > 0.0
assert abs((r_iho / r_star) - ratio) < 1e-12
if a.x == 0.0:
    assert abs(r_iho - r_star) < 1e-15
else:
    assert r_iho > r_star

out = {
    'iteration': 370,
    'observable': 'tensor_to_scalar_ratio',
    'N': a.N,
    'x_beta_over_12alpha': a.x,
    'r_starobinsky_beta0': r_star,
    'r_iho_quadratic': r_iho,
    'normalized_ratio_r_over_rstar': ratio,
    'source_relation': 'r=(12/N^2)*(12alpha)/(12alpha-beta)',
    'classification': 'PASS_SCOPED_SOURCE_FORMULA_REPRODUCED',
    'fit_claimed': False
}
pathlib.Path(a.output).parent.mkdir(parents=True, exist_ok=True)
with open(a.output, 'w') as f:
    json.dump(out, f, indent=2, sort_keys=True)
print(json.dumps(out, sort_keys=True))
