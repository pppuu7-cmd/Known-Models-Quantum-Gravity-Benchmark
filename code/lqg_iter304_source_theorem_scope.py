#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter304_toller_finiteness_transfer.json'))
c=p['prospectively_frozen_claims']
ok=(c['standard_eprl_three_edge_connected_integrability_theorem_exists'] and
    c['standard_theorem_is_stated_for_sl2c_spin_network_invariants_of_specified_class'] and
    c['toller_branches_are_polynomially_bounded'] and
    c['fixed_toller_branch_is_not_sl2c_representation'] and
    (not c['published_source_explicitly_extends_kaminski_integrability_theorem_to_toller_causal_vertex']))
out={'probe':'source_theorem_scope','pass':bool(ok),'iteration':304,
     'standard_eprl_finiteness_theorem':True,
     'explicit_toller_extension_found_in_frozen_contract':False,
     'tested_claim':'source-grounded theorem-scope mismatch requires an explicit transfer argument'}
pathlib.Path('build/lqg-iter304').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter304/source_theorem_scope.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
