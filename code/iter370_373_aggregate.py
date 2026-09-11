#!/usr/bin/env python3
import json, pathlib

root = pathlib.Path('iter370-373-results')
docs = [json.load(open(p)) for p in root.rglob('*.json')]
r370 = [d for d in docs if d.get('iteration') == 370]
r371 = [d for d in docs if d.get('iteration') == 371]
r372 = [d for d in docs if d.get('iteration') == 372]
r373 = [d for d in docs if d.get('iteration') == 373]

assert len(r370) == 18, len(r370)
assert len(r371) == 9, len(r371)
assert len(r372) == 5, len(r372)
assert len(r373) == 1, len(r373)
assert all(d['classification'] == 'PASS_SCOPED_SOURCE_FORMULA_REPRODUCED' for d in r370)
assert all(abs(d['normalized_ratio_r_over_rstar'] - 1.0) < 1e-12 for d in r370 if d['x_beta_over_12alpha'] == 0.0)
assert all(d['normalized_ratio_r_over_rstar'] > 1.0 for d in r370 if d['x_beta_over_12alpha'] > 0.0)
assert sum(1 for d in r371 if d['finite_positive_r_domain']) == 6
assert sum(1 for d in r371 if not d['finite_positive_r_domain']) == 3
assert all(d['classification'] == 'PASS_SCOPED_ANALYTIC_ERROR_PROPAGATION' for d in r372)
by_x = sorted(r372, key=lambda d: d['x_beta_over_12alpha'])
assert all(by_x[i+1]['relative_sigma_r'] > by_x[i]['relative_sigma_r'] for i in range(len(by_x)-1))
sg = r373[0]
assert sg['source_defined_normalized_observable_candidate_present'] is True
assert sg['same_formula_starobinsky_comparator_present'] is True
assert sg['source_supplied_observational_covariance_present'] is False
assert sg['family_terminal'] is False
assert sg['d7_promotion_authorized'] is False

out = {
    'iteration_bundle': '370-373',
    'classification': 'PASS_SCOPED_IHO_DQFT_SOURCE_DEFINED_COSMOLOGICAL_TENSOR_RATIO_WITH_SAME_FORMULA_STAROBINSKY_COMPARATOR_AND_ANALYTIC_ERROR_SENSITIVITY__SOURCE_SUPPLIED_COVARIANCE_AND_FULL_DOMAIN_TRANSPORT_REMAIN_OPEN',
    'observable_grid_jobs': len(r370),
    'domain_guard_jobs': len(r371),
    'error_propagation_jobs': len(r372),
    'scope_guard_jobs': len(r373),
    'source_defined_normalized_observable_candidate_present': True,
    'same_domain_starobinsky_comparator_present': True,
    'analytic_error_propagation_present': True,
    'source_supplied_observational_covariance_present': False,
    'family_status': 'PARTIAL_SUBFAMILY_ONLY',
    'family_terminal': False,
    'd7_promotion_authorized': False,
    'refined_blocker': sg['refined_blocker'],
    'scientific_boundary': 'This bundle audits a source-defined cosmological prediction of the IHO/DQFT quadratic-gravity construction. It does not establish a source likelihood/covariance object, full non-cosmological domain transport, or family-level D7 closure.'
}
with open('iter370-373-summary.json', 'w') as f:
    json.dump(out, f, indent=2, sort_keys=True)
print(json.dumps(out, sort_keys=True))
