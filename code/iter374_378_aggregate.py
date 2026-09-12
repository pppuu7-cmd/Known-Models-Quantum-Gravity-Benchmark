#!/usr/bin/env python3
import json, pathlib

root=pathlib.Path('iter374-378-results')
docs=[json.load(open(p)) for p in root.rglob('*.json')]
k=[d for d in docs if d.get('iteration')==374]
s=[d for d in docs if d.get('iteration')==375]
t=[d for d in docs if d.get('iteration')==376]
e=[d for d in docs if d.get('iteration')==377]
assert len(k)==8, len(k)
assert len(s)==3, len(s)
assert len(t)==12, len(t)
assert len(e)==1, len(e)
assert all(d['finite_difference_relative_change'] < 1e-6 for d in k)
assert all(d['kernel_K'] > 0 for d in k)
assert all(all(p['DeltaP_v'] > 0 for p in d['points']) for d in s)
assert all(all(p['DeltaP_u'] > 0 for p in d['points']) for d in t)
assert all(d['parity_symmetric_baseline_DeltaP_v']==0.0 for d in s)
assert all(d['parity_symmetric_baseline_DeltaP_u']==0.0 for d in t)
assert e[0]['reported_R_TT']==0.79
assert e[0]['likelihood_or_covariance_payload_present_in_current_source'] is False
assert e[0]['posterior_odds_recomputed_here'] is False

# Source formulas predict larger tensor parity amplitude when x=beta/(12 alpha) increases at fixed N,z.
for N in [50.0,55.0,60.0]:
    rows=sorted([d for d in t if abs(d['N']-N)<1e-12], key=lambda d:d['x_beta_over_12alpha'])
    assert len(rows)==4
    for j in range(len(rows)-1):
        a=rows[j]['points']; b=rows[j+1]['points']
        assert all(bi['DeltaP_u'] > ai['DeltaP_u'] for ai,bi in zip(a,b))

out={
 'iteration_bundle':'374-378',
 'classification':'PASS_SCOPED_INDEPENDENT_DSI_PARITY_OBSERVABLE_LAYER__SCALAR_AND_TENSOR_SOURCE_FORMULAS_NUMERICALLY_REPRODUCED__LIKELIHOOD_PAYLOAD_AND_FULL_DOMAIN_TRANSPORT_OPEN',
 'kernel_jobs':len(k),'scalar_jobs':len(s),'tensor_jobs':len(t),'evidence_guard_jobs':len(e),
 'source_defined_scalar_parity_observable_present':True,
 'source_defined_tensor_parity_observable_present':True,
 'same_domain_zero_asymmetry_baseline_present':True,
 'reported_R_TT_present':True,
 'reported_posterior_odds_pointer_present':True,
 'reproducible_source_likelihood_or_covariance_payload_present':False,
 'independent_from_r_only_scan':True,
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'refined_blocker':'REPRODUCIBLE_SOURCE_GROUNDED_PARITY_LIKELIHOOD_OR_COVARIANCE_OBJECT_PLUS_FULL_FAMILY_DOMAIN_TRANSPORT',
 'scientific_boundary':'The source-defined parity signal is a second observable layer of the same QQG/DSI realization. Numerical reproduction of its Hankel-order kernel and scalar/tensor fractional asymmetries does not reproduce the cited Planck posterior analysis and cannot by itself close D7.'
}
with open('iter374-378-summary.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
