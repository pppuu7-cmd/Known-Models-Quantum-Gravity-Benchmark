#!/usr/bin/env python3
import json
from pathlib import Path

root = Path('build/lqg-iter324-results')
files = sorted(root.glob('*.json'))
if len(files) != 20:
    raise SystemExit(f'expected 20 artifacts, got {len(files)}')
rows = [json.loads(p.read_text()) for p in files]
sectors = sorted({r['sector'] for r in rows})
gammas = sorted({r['gamma'] for r in rows})
assert sectors == ['minus_mm','minus_mp','plus_mm','plus_mp']
assert gammas == [0.0,0.1,0.274,1.0,10.0]
assert all(r['finite_epsilon_softens_beta_pole'] is False for r in rows)
max_cancel = max(r['max_projector_denominator_cancellation_error'] for r in rows)
max_coeff = max(r['max_smallest_beta_error_vs_expected'] for r in rows)
assert max_cancel < 1e-11
assert max_coeff < 5e-5

# Sign pattern and gamma-simple magnitude must hold in every job.
expected_sign = {'plus_mp':-1,'plus_mm':1,'minus_mp':1,'minus_mm':-1}
for r in rows:
    cg = 2.0/(1.0+r['gamma']**2)
    assert abs(r['expected_coefficient_magnitude_Cgamma']-cg) < 1e-14
    assert abs(r['expected_beta_minus2_coefficient']-expected_sign[r['sector']]*cg) < 1e-14

summary = {
    'iteration': 324,
    'jobs': len(rows),
    'sectors': sectors,
    'gamma_grid': gammas,
    'epsilon_grid_per_job': rows[0]['epsilon_values'],
    'beta_grid_per_job': rows[0]['beta_values'],
    'all_finite_epsilon_jobs_retain_beta_minus2_pole': True,
    'max_exact_projector_denominator_cancellation_error': max_cancel,
    'max_small_beta_coefficient_error': max_coeff,
    'leading_residue_magnitude': '2/(1+gamma^2), independent of finite spectral epsilon',
    'classification': 'The published finite spectral i-epsilon prescription does not regularize the j=1/2 beta->0 Toller pole: after the exact projector/denominator cancellation, every tested branch and magnetic sector retains an epsilon-independent beta^-2 leading residue.',
    'implication': 'Keeping the source spectral epsilon finite cannot by itself supply the missing local short-distance regulator for products on common partial diagonals.',
    'scope_guard': 'This does not exclude a separately specified joint distributional extension/renormalized product, does not count physical counterterms, and does not terminally fail LQG/spinfoam or authorize D7.'
}
out = Path('build/lqg-iter324-summary.json')
out.write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
