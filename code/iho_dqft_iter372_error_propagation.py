#!/usr/bin/env python3
import argparse, json, math, pathlib

p = argparse.ArgumentParser()
p.add_argument('--N', type=float, required=True)
p.add_argument('--x', type=float, required=True, help='x=beta/(12 alpha)')
p.add_argument('--sigma-N', type=float, required=True)
p.add_argument('--sigma-x', type=float, required=True)
p.add_argument('--output', required=True)
a = p.parse_args()

assert a.N > 0.0
assert 0.0 <= a.x < 1.0
assert a.sigma_N >= 0.0 and a.sigma_x >= 0.0
r_star = 12.0/(a.N*a.N)
r = r_star/(1.0-a.x)
term_N = 2.0*a.sigma_N/a.N
term_x = a.sigma_x/(1.0-a.x)
relative_sigma = math.sqrt(term_N*term_N + term_x*term_x)
sigma_r = r*relative_sigma
assert math.isfinite(sigma_r) and sigma_r >= 0.0

out = {
    'iteration': 372,
    'N': a.N,
    'x_beta_over_12alpha': a.x,
    'sigma_N': a.sigma_N,
    'sigma_x': a.sigma_x,
    'r_iho_quadratic': r,
    'relative_sigma_r': relative_sigma,
    'sigma_r': sigma_r,
    'propagation_formula': 'sigma_r/r=sqrt((2 sigma_N/N)^2+(sigma_x/(1-x))^2)',
    'classification': 'PASS_SCOPED_ANALYTIC_ERROR_PROPAGATION',
    'covariance_dataset_claimed': False,
    'guard': 'Independent-error propagation validates sensitivity of the source formula only; it is not a source-supplied observational covariance matrix.'
}
pathlib.Path(a.output).parent.mkdir(parents=True, exist_ok=True)
with open(a.output, 'w') as f:
    json.dump(out, f, indent=2, sort_keys=True)
print(json.dumps(out, sort_keys=True))
