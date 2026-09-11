#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter310_scaling_degree_extension.json'))
c=p['prospectively_frozen_claims']
ok=(c['same_scaling_degree_extension_exists'] and not c['same_scaling_degree_extension_unique'] and
    c['max_local_delta_derivative_order']==8 and c['physical_symmetry_or_normalization_conditions_may_reduce_ambiguity'] and
    not c['source_eq4_alone_fixes_all_extension_coefficients'] and
    not c['global_causal_vertex_distribution_constructed'] and not c['complete_stack_control_proven'] and
    not c['family_terminal'] and not c['d7_authorized'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':310,
     'proven_scope':'the explicit total-identity witness admits same-scaling-degree distributional extensions, but scaling degree alone leaves local delta-derivative ambiguity through order 8',
     'not_proven':['all raw counterterm coefficients survive physical symmetries','a globally compatible extension exists across all partial diagonals','the source fixes a renormalization scheme','complete-stack finiteness','family terminality','D7 authorization'],
     'required_next':'derive symmetry/gluing/normalization constraints and test whether they uniquely fix the local extension coefficients'}
pathlib.Path('build/lqg-iter310').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter310/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
