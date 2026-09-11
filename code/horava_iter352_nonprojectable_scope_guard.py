#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

a=json.loads(Path('paper_iv/HORAVA_SOURCE_AUTHORITY_ITER349_352.json').read_text())
n=a['nonprojectable_2026_authority']; text=' '.join(n['facts']).lower()
assert '2+1' in text; assert 'additional questions' in text; assert 'not a 3+1' in text
assert a['frozen_interpretation']['nonprojectable_can_close_projectable_gap'] is False
out={'iteration':352,'classification':'PASS_PROCESS_SCOPE_GUARD__2026_NONPROJECTABLE_PATH_INTEGRAL_IS_REAL_PROGRESS_BUT_DOES_NOT_SUPPLY_3P1_ALL_SECTOR_RENORMALIZABILITY_OR_PHYSICAL_OBSERVABLE_CLOSURE_AND_CANNOT_BE_SUBSTITUTED_FOR_PROJECTABLE_UV_TO_IR_TRANSPORT','source':n['source'],'explicit_case_study_dimension':'2+1','three_plus_one_terminal_certificate':False,'can_replace_projectable_ir_resolution':False,'scope_guard':['NONPROJECTABLE_AND_PROJECTABLE_ARE_MATERIAL_SUBFAMILIES','NO_CROSS_SUBFAMILY_SUBSTITUTION','NO_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']}
Path('iter352-horava-nonprojectable-scope-guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
