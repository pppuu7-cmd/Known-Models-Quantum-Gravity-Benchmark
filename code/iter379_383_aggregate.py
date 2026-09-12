#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('iter379-383-results')
records=[]
for p in root.rglob('*.json'):
    try:
        records.append(json.loads(p.read_text()))
    except Exception:
        pass
ratios=[r for r in records if r.get('record_type')=='published_ratio']
mc=[r for r in records if r.get('record_type')=='mc_precision']
sem=[r for r in records if r.get('record_type')=='semantics_guard']
cov=[r for r in records if r.get('record_type')=='covariance_scope']
assert len(ratios)==14, len(ratios)
assert len(mc)==8, len(mc)
assert len(sem)==1, len(sem)
assert len(cov)==1, len(cov)
assert all(r['raw_ratio']>1 for r in ratios)
assert all(r['reported_ratio_inside_rounding_interval'] for r in ratios)
assert all(r['relative_error_to_reported_ratio']<0.05 for r in ratios)
key=next(r for r in ratios if r['table']=='1' and r['metric']=='C2_RTT')
assert key['raw_ratio']>600
assert abs(key['reported_ratio']-653)<1e-12
assert key['published_rounding_ratio_interval'][0]>500
keymc=next(r for r in mc if r['metric']=='C2_RTT')
assert keymc['conservative_ratio_interval95'][0]>1
s=sem[0]; c=cov[0]
assert s['empirical_tail_ratio_reproducible'] is True
assert s['bayes_factor_reproduced'] is False
assert s['posterior_odds_reproduced'] is False
assert s['d7_promotion_authorized'] is False
assert c['raw_covariance_matrix_present'] is False
assert c['raw_mc_realizations_present'] is False
assert c['d7_promotion_authorized'] is False
out={
 'iteration_bundle':'379-383',
 'classification':'PASS_SCOPED_PUBLISHED_DSI_TAIL_PROBABILITY_RATIO_REPRODUCTION_WITH_FINITE_MC_ROBUSTNESS__FORMAL_BAYES_FACTOR_AND_RAW_COVARIANCE_REPRODUCTION_REMAIN_OPEN',
 'family_status':'PARTIAL_SUBFAMILY_ONLY','family_terminal':False,'d7_promotion_authorized':False,
 'published_ratio_jobs':len(ratios),'mc_precision_jobs':len(mc),'semantics_guard_jobs':len(sem),'covariance_scope_jobs':len(cov),
 'key_c2_rtt_raw_ratio':key['raw_ratio'],'key_c2_rtt_reported_ratio':key['reported_ratio'],
 'key_c2_rtt_rounding_ratio_interval':key['published_rounding_ratio_interval'],
 'key_c2_rtt_mc_proxy_ratio_interval95':keymc['conservative_ratio_interval95'],
 'formal_bayes_factor_reproduced':False,'raw_covariance_matrix_reproduced':False,'raw_monte_carlo_realizations_reproduced':False,
 'refined_blocker':'RAW_PLANCK_OR_AUTHOR_MONTE_CARLO_REALIZATIONS_PLUS_EXPLICIT_MODEL_EVIDENCE_OR_MARGINAL_LIKELIHOOD_DEFINITION_AND_PRIORS_PLUS_RAW_COVARIANCE_MATRIX_PLUS_FULL_FAMILY_DOMAIN_TRANSPORT',
 'scientific_boundary':'The published DSI/SI empirical-tail probability ratios, including the 653 C2+RTT ratio, are arithmetically reproducible and remain strongly above unity under a finite-one-million-simulation precision proxy. This is not a reproduction of formal Bayesian model evidence, posterior odds, the raw Planck/author Monte-Carlo ensemble, or the raw covariance matrix; D7 remains closed to promotion.'
}
Path('iter379-383-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
