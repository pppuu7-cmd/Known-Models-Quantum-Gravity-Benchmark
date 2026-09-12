import json, pathlib
root=pathlib.Path('iter384-387-results')
objs=[]
for p in root.rglob('*.json'):
    try: objs.append(json.loads(p.read_text()))
    except Exception: pass
T=[o for o in objs if o.get('mode')=='transfer']
C=[o for o in objs if o.get('mode')=='convergence']
R=[o for o in objs if o.get('mode')=='rtt_proxy']
W=[o for o in objs if o.get('mode')=='window']
S=[o for o in objs if o.get('mode')=='scope']
coverage=(len(T)==3 and len(C)==3 and len(R)==6 and len(W)==6 and len(S)==1)
passes=all(o.get('pass') for o in T+C+R+W+S)
proxy_guard=all(o.get('is_planck_reproduction') is False for o in R)
scope_guard=(len(S)==1 and S[0].get('full_likelihood_reproduction_authorized') is False and S[0].get('d7_promotion_authorized') is False)
classification='PASS_SOURCE_DEFINED_LOW_ELL_DSI_TRANSFER_DOMAIN_AND_CUTOFF_TRANSPORT_REPRODUCED__RAW_PLANCK_MONTE_CARLO_COVARIANCE_AND_END_TO_END_LIKELIHOOD_REMAIN_OPEN' if coverage and passes and proxy_guard and scope_guard else 'INCOMPLETE_OR_FAILED_LOW_ELL_DSI_TRANSPORT_AUDIT'
out={
 'iteration_bundle':'384-387',
 'transfer_pattern_jobs':len(T),
 'cutoff_convergence_jobs':len(C),
 'diagnostic_RTT_proxy_jobs':len(R),
 'domain_window_jobs':len(W),
 'scope_guard_jobs':len(S),
 'classification':classification,
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'published_low_ell_transfer_domain_reproduced':coverage and passes,
 'diagnostic_RTT_proxies_explicitly_not_planck_reproduction':proxy_guard,
 'raw_planck_masked_map_present':False,
 'million_sky_realization_payload_present':False,
 'raw_covariance_present':False,
 'full_likelihood_reproduction_authorized':False,
 'refined_blocker':'RAW_PLANCK_MASKED_MAP_OR_EQUIVALENT_C_L_PAYLOAD_PLUS_REPRODUCIBLE_SKY_REALIZATION_PIPELINE_AND_COVARIANCE_FOR_END_TO_END_POSTERIOR_REPLICATION',
 'scientific_boundary':'Table-4 low-ell transfer factors, cutoff dependence and domain behavior are machine-audited. Equal-baseline C_l R_TT values are diagnostics only, not Planck likelihood reproduction.'
}
pathlib.Path('iter384-387-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if classification.startswith('INCOMPLETE'): raise SystemExit(2)
