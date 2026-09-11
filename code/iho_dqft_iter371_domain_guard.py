#!/usr/bin/env python3
import argparse, json, math, pathlib

p = argparse.ArgumentParser()
p.add_argument('--x', type=float, required=True, help='x=beta/(12 alpha)')
p.add_argument('--output', required=True)
a = p.parse_args()

finite_positive = 0.0 <= a.x < 1.0
branch_sign_compatible = a.x >= 0.0
starobinsky_limit = (a.x == 0.0)
if finite_positive:
    amplification = 1.0 / (1.0 - a.x)
    assert math.isfinite(amplification) and amplification >= 1.0
else:
    amplification = None

out = {
    'iteration': 371,
    'x_beta_over_12alpha': a.x,
    'branch_sign_compatible_with_beta_nonnegative_scan': branch_sign_compatible,
    'finite_positive_r_domain': finite_positive,
    'starobinsky_limit': starobinsky_limit,
    'normalized_amplification_if_valid': amplification,
    'classification': 'PASS_SCOPED_DOMAIN_GUARD' if finite_positive else 'OUTSIDE_SCOPED_FINITE_POSITIVE_DOMAIN',
    'source_fit_claimed': False,
    'guard': 'Audit grid only; no observationally inferred alpha or beta is claimed.'
}
pathlib.Path(a.output).parent.mkdir(parents=True, exist_ok=True)
with open(a.output, 'w') as f:
    json.dump(out, f, indent=2, sort_keys=True)
print(json.dumps(out, sort_keys=True))
