#!/usr/bin/env python3
import json

src_path = 'paper_iv/IHO_DQFT_COSMOLOGY_SOURCE_AUTHORITY_ITER370_373.json'
with open(src_path) as f:
    src = json.load(f)

assert src['family'] == 'PERTURBATIVE_HIGHER_DERIVATIVE'
assert src['branch'] == 'IHO_DQFT_SPACELIKE_PV'
assert src['source']['arxiv'] == '2603.07150v3'
assert src['protocol_guard']['no_family_terminalization_from_this_bundle'] is True
assert src['protocol_guard']['d7_promotion_authorized'] is False
assert src['error_object']['status'] == 'DERIVED_PROPAGATION_FROM_SOURCE_FORMULA_NOT_SOURCE_COVARIANCE_DATASET'

out = {
    'iteration': 373,
    'branch': src['branch'],
    'source_defined_normalized_observable_candidate_present': True,
    'same_formula_starobinsky_comparator_present': True,
    'analytic_error_propagation_object_present': True,
    'source_supplied_observational_covariance_present': False,
    'family_terminal': False,
    'd7_promotion_authorized': False,
    'classification': 'PASS_SCOPED_IHO_DQFT_COSMOLOGY_OBSERVABLE_CANDIDATE_WITH_STAROBINSKY_LIMIT__SOURCE_COVARIANCE_AND_FULL_DOMAIN_TRANSPORT_STILL_OPEN',
    'refined_blocker': 'KMQGB_ACCEPTANCE_OF_COSMOLOGICAL_R_AS_REQUIRED_NORMALIZED_GRAVITATIONAL_OBSERVABLE_PLUS_SOURCE_GROUNDED_UNCERTAINTY_OR_LIKELIHOOD_OBJECT_PLUS_FULL_DOMAIN_SCOPE_TRANSPORT'
}
with open('iter373-iho-cosmology-scope.json', 'w') as f:
    json.dump(out, f, indent=2, sort_keys=True)
print(json.dumps(out, sort_keys=True))
