#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter311-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'subset_degree_census','non_safe_subset_count','overlap_pair_census','forest_count','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter311_partial_diagonal_subdivergence_census.json'))
out={
  'iteration':311,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),
  'subset_degree_formula':'omega(s)=(s-1)(s-3)',
  'collapse_census':{'K2':{'count':10,'omega':-1},'K3':{'count':10,'omega':0},'K4':{'count':5,'omega':3},'K5':{'count':1,'omega':8}},
  'proper_non_safe_partial_diagonals':15,'all_non_safe_including_total':16,
  'nested_pairs':35,'overlapping_incomparable_pairs':85,'compatible_forests_including_empty':72,
  'single_total_identity_extension_sufficient':False,
  'all_partial_diagonal_leading_coefficients_nonzero_proven':False,
  'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
  'next_required_object':'causal-sector and boundary-contraction residue audit on K3/K4/K5 strata, followed by a compatible forest extension/normalization prescription on all surviving divergent diagonals'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter311-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter311-summary.sha256').write_text(digest+'  lqg-iter311-summary.json\n')
