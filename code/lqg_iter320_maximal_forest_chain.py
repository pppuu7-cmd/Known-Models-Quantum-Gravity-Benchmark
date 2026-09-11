#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--chain', required=True, help='K3_K4, e.g. 012_0123')
a = p.parse_args()
try:
    k3s, k4s = a.chain.split('_')
except ValueError:
    raise SystemExit('chain must be K3_K4')
K3 = frozenset(map(int, k3s))
K4 = frozenset(map(int, k4s))
K5 = frozenset(range(5))
if len(K3) != 3 or len(K4) != 4 or not K3 < K4 or not K4 < K5:
    raise SystemExit('expected strict K3 subset K4 subset K5 chain on vertices 0..4')

# Sector decomposition for a nested collapse:
# 6 relative coordinates at scale lambda*mu*nu,
# 3 further coordinates at lambda*mu,
# 3 further coordinates at lambda.
# Three K3 edges contribute power 6, three K4\K3 edges power 6,
# four K5\K4 edges power 8. Hence shell densities:
# lambda^(11-20)=lambda^-9, mu^(8-12)=mu^-4, nu^(5-6)=nu^-1.
shell_exponents = {'lambda': -9, 'mu': -4, 'nu': -1}
cumulative_omega = {'K3': 0, 'K4': 3, 'K5': 8}

# Exact cutoff factors for lower cutoffs lambda=e^a, mu=e^b, nu=e^c.
def exact_factor(eps, powers):
    al, am, an = powers
    el, em, en = eps**al, eps**am, eps**an
    L = (el**-8 - 1.0) / 8.0
    M = (em**-3 - 1.0) / 3.0
    N = math.log(1.0/en)
    return L*M*N

paths = {
    'isotropic_111': (1,1,1),
    'deep_fast_113': (1,1,3),
    'middle_fast_121': (1,2,1),
    'outer_fast_211': (2,1,1),
    'ordered_123': (1,2,3),
}
eps_values = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
path_results = {}
for name, powers in paths.items():
    vals = [exact_factor(e, powers) for e in eps_values]
    # Remove the predicted log factor and fit the last 3 points.
    # F ~ const * eps^[-(8*a+3*b)] * log(1/eps).
    p_expected = 8*powers[0] + 3*powers[1]
    xs = [math.log(e) for e in eps_values[-3:]]
    ys = [math.log(v/math.log(1.0/e)) for e,v in zip(eps_values[-3:], vals[-3:])]
    mx, my = sum(xs)/3.0, sum(ys)/3.0
    slope = sum((x-mx)*(y-my) for x,y in zip(xs,ys)) / sum((x-mx)**2 for x in xs)
    assert abs(slope + p_expected) < 2e-3, (name, slope, p_expected)
    path_results[name] = {
        'cutoff_powers_lambda_mu_nu': list(powers),
        'values': vals,
        'expected_power_after_log_removal': -p_expected,
        'observed_power_after_log_removal': slope,
        'diverges': True,
    }

out = {
    'iteration': 320,
    'chain': a.chain,
    'K3': ''.join(map(str, sorted(K3))),
    'K4': ''.join(map(str, sorted(K4))),
    'K5': '01234',
    'relative_coordinate_groups': [6,3,3],
    'edge_singularity_groups': [6,6,8],
    'shell_exponents': shell_exponents,
    'cumulative_superficial_degrees': cumulative_omega,
    'path_results': path_results,
    'all_positive_joint_cutoff_paths_tested_diverge': True,
    'nonzero_residue_authority': {
        'K3_K4': 'Iter317 physical group-consistent witnesses',
        'K5': 'Iter307 exact total-identity witness'
    },
    'classification': 'maximal nested forest has simultaneous logarithmic K3, cubic K4 and eighth-power K5 extension burdens; an ordinary common cutoff limit is not finite',
    'scope_guard': 'This sector-decomposed nested-cutoff stress test establishes multiscale divergence for the witnessed homogeneous residues. It does not prove that the exact spectral i-epsilon boundary value lacks a canonical distributional extension, nor does it count independent physical counterterms.'
}
path = Path('build/lqg-iter320') / f'chain_{a.chain}.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps(out, sort_keys=True))
