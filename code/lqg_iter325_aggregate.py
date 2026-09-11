#!/usr/bin/env python3
import json
from pathlib import Path

root = Path('build/lqg-iter325-results')
files = sorted(root.glob('sector_*.json'))
if len(files) != 16:
    raise SystemExit(f'expected 16 sector artifacts, got {len(files)}')
rows = [json.loads(p.read_text()) for p in files]
assert sorted(r['sector'] for r in rows) == list(range(16))
patterns = {r['kappa_pattern'] for r in rows}
assert len(patterns) == 16
assert all(r['product_over_edges_minus_kappa'] == 1 for r in rows)
assert all(r['finite_source_epsilon_softens_full_k5_leading_pole'] is False for r in rows)
assert all(r['rows'][0]['radial_density_exponent_in_12_relative_dimensions'] == -9 for r in rows)

max_cancel = max(r['max_projector_denominator_cancellation_error'] for r in rows)
max_coeff = max(r['max_leading_coefficient_error'] for r in rows)
assert max_cancel < 1e-11
assert max_coeff < 1e-15

gammas = rows[0]['gamma_grid']
eps_values = rows[0]['epsilon_grid']
cplus = []
for gamma in gammas:
    expected_per = -1.0 / (648.0 * (1.0 + gamma*gamma)**10)
    expected_sum = -2.0 / (81.0 * (1.0 + gamma*gamma)**10)
    for eps in eps_values:
        coeffs = []
        for r in rows:
            hit = [x for x in r['rows'] if x['gamma'] == gamma and x['epsilon'] == eps]
            assert len(hit) == 1
            coeffs.append(hit[0]['per_sector_delta_minus20_coefficient'])
        assert max(abs(x-expected_per) for x in coeffs) < 1e-15
        total = sum(coeffs)
        assert abs(total-expected_sum) < max(1e-15, abs(expected_sum)*1e-13)
        assert total < 0
        cplus.append({
            'gamma': gamma,
            'epsilon': eps,
            'per_sector_coefficient': expected_per,
            'cplus_unit_sum_coefficient': total,
            'expected_cplus_coefficient': expected_sum,
            'nonzero': True,
        })

summary = {
    'iteration': 325,
    'gauge_fixed_causal_sectors': 16,
    'distinct_kappa_patterns': len(patterns),
    'gamma_grid': gammas,
    'epsilon_grid': eps_values,
    'all_16_sectors_have_same_nonzero_leading_sign': True,
    'per_sector_leading_coefficient': '-1/[648*(1+gamma^2)^10] * delta^-20',
    'source_Cplus_unit_sum_leading_coefficient': '-2/[81*(1+gamma^2)^10] * delta^-20',
    'radial_density_in_12_relative_dimensions': 'delta^-9 d(delta)',
    'all_tested_finite_source_epsilons_retain_divergence': True,
    'max_projector_denominator_cancellation_error': max_cancel,
    'max_leading_coefficient_error': max_coeff,
    'cplus_grid_results': cplus,
    'classification': 'The explicit Iter307 minimal-spin C+ K5 witness remains nonzero and locally non-integrable for every one of the 16 causal sectors and for every tested finite value of the published spectral epsilon. The C+ unit sum reinforces rather than cancels the leading pole.',
    'implication': 'Finite source spectral epsilon is not a sufficient local UV regulator for the full causal K5 witness; any finite definition must invoke additional joint distributional/extension or subtraction data beyond this simple finite-epsilon prescription.',
    'scope_guard': 'This is an explicit witness-level obstruction, not a proof that no mathematically consistent joint extension exists, not a terminal family FAIL, and not D7 authorization.'
}
out = Path('build/lqg-iter325-summary.json')
out.write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
