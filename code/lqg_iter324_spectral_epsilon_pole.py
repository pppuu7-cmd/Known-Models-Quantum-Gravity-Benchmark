#!/usr/bin/env python3
import argparse, cmath, json, math
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--sector', required=True, choices=('plus_mp','plus_mm','minus_mp','minus_mm'))
p.add_argument('--gamma', required=True, type=float)
a = p.parse_args()

gamma = a.gamma
rho = gamma / 2.0
Cgamma = 2.0 / (1.0 + gamma*gamma)
expected_sign = {
    'plus_mp': -1.0,
    'plus_mm': +1.0,
    'minus_mp': +1.0,
    'minus_mm': -1.0,
}[a.sector]
expected = expected_sign * Cgamma
branch = 'plus' if a.sector.startswith('plus_') else 'minus'
mag = 'mp' if a.sector.endswith('_mp') else 'mm'

def projector(z):
    return (z*z + 0.25) / (rho*rho + 0.25)

def toller(z, beta):
    den = 2.0 * (math.sinh(beta)**2) * (z*z + 0.25)
    if branch == 'plus' and mag == 'mp':
        return -cmath.exp(1j*z*beta) / den
    if branch == 'plus' and mag == 'mm':
        return cmath.exp(1j*z*beta) * (math.cosh(beta) - 2j*z*math.sinh(beta)) / den
    if branch == 'minus' and mag == 'mp':
        return cmath.exp(-1j*z*beta) * (math.cosh(beta) + 2j*z*math.sinh(beta)) / den
    return -cmath.exp(-1j*z*beta) / den

eps_values = [1e-1, 1e-2, 1e-4, 1e-6]
beta_values = [1e-2, 1e-3, 1e-4, 1e-5]
rows = []
max_cancel_error = 0.0
max_small_beta_error = 0.0
for eps in eps_values:
    z = rho + (1j*eps if branch == 'plus' else -1j*eps)
    P = projector(z)
    cancellation = P / (z*z + 0.25)
    exact_cancel = 1.0 / (rho*rho + 0.25)
    cancel_error = abs(cancellation - exact_cancel)
    max_cancel_error = max(max_cancel_error, cancel_error)
    coeffs = []
    for beta in beta_values:
        projected = P * toller(z, beta)
        coeff = beta*beta*projected
        coeffs.append({'beta': beta, 'real': coeff.real, 'imag': coeff.imag, 'abs_error_vs_expected': abs(coeff-expected)})
    small_error = abs(complex(coeffs[-1]['real'], coeffs[-1]['imag']) - expected)
    max_small_beta_error = max(max_small_beta_error, small_error)
    rows.append({
        'epsilon': eps,
        'z_real': z.real,
        'z_imag': z.imag,
        'projector_denominator_cancellation_error': cancel_error,
        'beta2_projected_coefficients': coeffs,
        'smallest_beta_error_vs_expected': small_error,
    })

# The algebraic cancellation should be at machine precision; the beta->0
# coefficient converges linearly/quadratically depending on the magnetic sector.
assert max_cancel_error < 1e-11, max_cancel_error
assert max_small_beta_error < 5e-5, (a.sector, gamma, max_small_beta_error, expected)
assert abs(expected) > 0.0

out = {
    'iteration': 324,
    'sector': a.sector,
    'branch': branch,
    'magnetic_sector': mag,
    'gamma': gamma,
    'rho_gamma_simple_j_half': rho,
    'epsilon_values': eps_values,
    'beta_values': beta_values,
    'expected_beta_minus2_coefficient': expected,
    'expected_coefficient_magnitude_Cgamma': Cgamma,
    'max_projector_denominator_cancellation_error': max_cancel_error,
    'max_smallest_beta_error_vs_expected': max_small_beta_error,
    'finite_epsilon_softens_beta_pole': False,
    'rows': rows,
    'classification': 'For the published j=1/2 Toller formula, the finite spectral i-epsilon projector exactly cancels the shifted spectral denominator and leaves the leading beta^-2 residue epsilon-independent.',
    'scope_guard': 'This establishes that the source spectral i-epsilon is not a short-distance beta regulator for this minimal-spin branch. It does not rule out a separately defined joint distributional boundary value or renormalized product, and it is not a family-level FAIL or D7 authorization.'
}
slug = str(gamma).replace('.','p')
path = Path('build/lqg-iter324') / f'{a.sector}_g{slug}.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps(out, sort_keys=True))
