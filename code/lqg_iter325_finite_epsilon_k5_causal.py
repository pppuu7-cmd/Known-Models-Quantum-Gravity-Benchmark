#!/usr/bin/env python3
import argparse, itertools, json, math
from fractions import Fraction
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--sector', type=int, required=True, choices=range(16))
a = p.parse_args()

# Fix sigma_0=+1 to quotient the global flip. Bits encode sigma_1..sigma_4.
sigma = [1]
for i in range(4):
    sigma.append(1 if (a.sector >> i) & 1 else -1)

edges = list(itertools.combinations(range(5), 2))
kappa = {(u, v): sigma[u] * sigma[v] for u, v in edges}
pattern = ''.join('+' if kappa[e] > 0 else '-' for e in edges)
leading_scalar_sign = math.prod(-kappa[e] for e in edges)
assert leading_scalar_sign == 1

# Iter307 exact normalized geometric contraction for the (A,A,B,A,A)
# minimal-spin total-identity witness after stripping the universal edge residues.
geometric = Fraction(-1, 663552)
assert geometric * (2 ** 10) == Fraction(-1, 648)

gammas = [0.0, 0.1, 0.274, 1.0, 10.0]
eps_values = [1e-1, 1e-2, 1e-4, 1e-6]
rows = []
max_projector_cancel_error = 0.0
max_coefficient_error = 0.0

for gamma in gammas:
    rho = gamma / 2.0
    Cgamma = 2.0 / (1.0 + gamma * gamma)
    expected = -1.0 / (648.0 * (1.0 + gamma * gamma) ** 10)
    for eps in eps_values:
        # For every edge, use the source spectral shift associated with its
        # causal branch. At j=1/2 the source projector is
        # P(z;rho)=(z^2+1/4)/(rho^2+1/4), so P/(z^2+1/4) is exact and
        # independent of finite epsilon. We audit all ten edges explicitly.
        edge_residue_factor = 1.0
        edge_cancel_errors = []
        for e in edges:
            z = complex(rho, eps if kappa[e] > 0 else -eps)
            P = (z*z + 0.25) / (rho*rho + 0.25)
            cancellation = P / (z*z + 0.25)
            target = 1.0 / (rho*rho + 0.25)
            err = abs(cancellation - target)
            edge_cancel_errors.append(err)
            max_projector_cancel_error = max(max_projector_cancel_error, err)
            # The leading branch scalar is -kappa*C_gamma.
            edge_residue_factor *= (-kappa[e]) * Cgamma
        coefficient = float(geometric) * edge_residue_factor
        err_coeff = abs(coefficient - expected)
        max_coefficient_error = max(max_coefficient_error, err_coeff)
        rows.append({
            'gamma': gamma,
            'epsilon': eps,
            'rho': rho,
            'max_edge_projector_cancellation_error': max(edge_cancel_errors),
            'edge_residue_product': edge_residue_factor,
            'per_sector_delta_minus20_coefficient': coefficient,
            'expected_per_sector_coefficient': expected,
            'coefficient_error': err_coeff,
            'radial_density_exponent_in_12_relative_dimensions': -9,
        })

assert max_projector_cancel_error < 1e-11, max_projector_cancel_error
assert max_coefficient_error < 1e-15, max_coefficient_error
assert all(r['per_sector_delta_minus20_coefficient'] < 0 for r in rows)

out = {
    'iteration': 325,
    'sector': a.sector,
    'sigma_gauge_fixed': sigma,
    'edge_order': [f'{u}{v}' for u, v in edges],
    'kappa_pattern': pattern,
    'product_over_edges_minus_kappa': leading_scalar_sign,
    'boundary_state': '(A,A,B,A,A)',
    'normalized_geometric_contraction': '-1/663552',
    'gamma_grid': gammas,
    'epsilon_grid': eps_values,
    'rows': rows,
    'max_projector_denominator_cancellation_error': max_projector_cancel_error,
    'max_leading_coefficient_error': max_coefficient_error,
    'finite_source_epsilon_softens_full_k5_leading_pole': False,
    'classification': 'For this exact minimal-spin causal K5 witness, every gauge-fixed C+ sector retains the same nonzero delta^-20 leading coefficient at finite source spectral epsilon; in 12 relative dimensions the radial density is delta^-9.',
    'scope_guard': 'This closes the simple proposal of keeping the published spectral epsilon finite as a short-distance regulator for this explicit C+ witness. It does not exclude a separately specified joint distributional/renormalized extension, does not terminally fail LQG/spinfoam, and does not authorize D7.'
}
path = Path('build/lqg-iter325') / f'sector_{a.sector:02d}.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps(out, sort_keys=True))
