#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter348-results')
files=list(root.rglob('iter348-*.json'))
rows=[json.loads(p.read_text()) for p in files]
lanes={r['lane']:r for r in rows}
required={'algebra_identity','decoupling_scaling','independent_grid','source_scope'}
assert set(lanes)==required,(set(lanes),required)
assert lanes['algebra_identity']['max_identity_residual'] < 1e-12
assert lanes['source_scope']['parent_family_terminal'] is False
assert lanes['source_scope']['d7_authorized'] is False
out={'iteration':348,'source':'Dondarini, Phys. Rev. D 108, 083526 (2023)','lanes':sorted(lanes),
     'classification':'PASS_SCOPED_SOURCE_DEFINED_QUADRATIC_INFLATION_PHYSICAL_TENSOR_POWER_SPECTRUM_HAS_SINGULAR_FAKEON_DECOUPLING_RELATIVE_TO_IDENTICAL_MODEL_HEAVY_FAKEON_GR_COMPARATOR',
     'scientific_interpretation':'The published normalized physical tensor observable supplies a stronger branch-level certificate than response-kernel proxies: at leading common order P_T^F/P_T^GR=(9/2) alpha_k^2/xi^2, hence no finite xi->0 decoupling at fixed alpha_k. This is specific to quadratic inflation and is not a family theorem.',
     'paper_iii_impact':'NOT_NEEDED','paper_iv_impact':'READY',
     'parent_family_terminal':False,'d7_authorized':False,'candidate_gravity_activation':False,
     'remaining_blocker':'Other material higher-derivative/fakeon branches remain independently unresolved; family-scope proof or exhaustive material-subfamily resolution is still required.',
     'scope_guard':['PHYSICAL_NORMALIZED_TENSOR_POWER_SPECTRUM','QUADRATIC_INFLATION_SUBMODEL_ONLY','STAROBINSKY_REGULAR_CASE_PREVENTS_GENERICIZATION','NO_PARENT_FAMILY_FAIL','NO_D7_PROMOTION']}
Path('iter348-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
