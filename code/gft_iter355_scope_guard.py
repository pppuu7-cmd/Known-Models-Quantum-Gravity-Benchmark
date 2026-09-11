#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

a=json.loads(Path('paper_iv/GFT_SOURCE_AUTHORITY_ITER353_355.json').read_text())
f=a['frozen_interpretation']
assert a['family']=='GFT_TENSOR_MODELS'
assert f['new_concrete_child_authority'] is True
assert f['full_gravity_observable_comparator'] is False
assert f['intensive_sector_closed'] is False
assert f['observable_spectrum_bridge_closed'] is False
assert f['explicit_spinfoam_reduction_map'] is False
text=' '.join(a['source_open_boundaries']).lower()
assert 'intensive' in text and 'observable cosmological perturbation spectra' in text and 'negligible gft interactions' in text
out={
 'iteration':355,
 'classification':'BLOCKED_SCOPED_GFT_CONDENSATE_COSMOLOGY_CHILD__SOURCE_DEFINES_A_CONCRETE_EMERGENT_MATTER_DISPERSION_OBJECT_BUT_INTENSIVE_SECTOR_SELECTION_SOURCE_TERM_CLOSURE_OBSERVABLE_SPECTRUM_BRIDGE_AND_FULL_GRAVITY_COMPARATOR_REMAIN_OPEN',
 'source':a['source'],
 'new_child_object_available':True,
 'full_gravity_observable_comparator':False,
 'intensive_sector_selection_closed':False,
 'observable_spectrum_bridge_closed':False,
 'explicit_spinfoam_reduction_equivalence_map':False,
 'family_terminalization_authorized':False,
 'scope_guard':['BLOCKED_IS_NOT_FAIL','CONDENSATE_COSMOLOGY_CHILD_NOT_PARENT_EXHAUSTION','MATTER_PROPAGATION_NOT_FULL_GRAVITY_OBSERVABLE','NO_IMPLICIT_MERGE_WITH_LQG_SPINFOAM','NO_D7_PROMOTION']
}
Path('iter355-gft-scope-guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
