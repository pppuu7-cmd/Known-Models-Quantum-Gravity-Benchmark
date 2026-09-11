#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter313_source_cplus_unit_sum.json'))
c=p['prospectively_frozen_claims']
ok=(c['source_cplus_uses_unit_coefficients_on_causal_structures'] and
    not c['source_cplus_contains_signed_class_weights_minus5_minus1_plus1'] and
    c['cplus_distinct_support_triangle_leading_sum']==-16 and c['cplus_distinct_support_k4_leading_sum']==0 and c['cplus_distinct_support_k5_leading_sum']==16 and
    not c['source_defined_cplus_cancels_minspin_triangle_or_k5_leading_sign'] and
    not c['full_contracted_triangle_residue_nonzero_proven'] and
    not c['family_terminal'] and not c['d7_authorized'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':313,
     'source_closed':'published C+ uses an unweighted sum over causal structures; the signed (-5,-1,+1) class weighting is not part of that definition',
     'leading_sign_result':'C+ preserves K3 and K5 scalar leading signs and cancels K4 scalar leading sign under distinct-support counting',
     'open':['exact contracted K3 residue witness','global compatible extension on surviving strata','complete-stack cutoff control','family terminality','D7 authorization']}
pathlib.Path('build/lqg-iter313').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter313/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
