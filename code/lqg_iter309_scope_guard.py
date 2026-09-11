#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter309_distribution_transversality.json'))
c=p['prospectively_frozen_claims']
ok=(not c['full_row_rank_transversality_holds_everywhere_on_common_identity_support'] and
    not c['standard_sufficient_delta_product_transversality_criterion_closes_vertex_distribution_product'] and
    not c['joint_multiwedge_epsilon_limit_explicitly_defined_by_eq4'] and
    not c['distributional_extension_or_renormalized_product_nonexistence_proven'] and
    not c['unregularized_absolute_integrability_restored'] and
    not c['family_terminal'] and not c['d7_authorized'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':309,
     'closed':['wedge-level source distribution identified','generic and rank-deficient common-support strata exhibited','standard sufficient transversality criterion shown not global'],
     'open':['existence/uniqueness of a microlocal extension','joint common-epsilon vertex limit','renormalized product compatible with gluing and normalization','complete-stack cutoff control','same-realization UV-to-Regge/GR transport'],
     'family_terminal':False,'d7_authorized':False}
pathlib.Path('build/lqg-iter309').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter309/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
