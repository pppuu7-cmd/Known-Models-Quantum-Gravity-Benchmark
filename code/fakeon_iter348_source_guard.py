#!/usr/bin/env python3
import json
from pathlib import Path

def main():
    out={'iteration':348,'lane':'source_scope','source':'Dondarini, Phys. Rev. D 108, 083526 (2023), DOI 10.1103/PhysRevD.108.083526',
         'published_objects':{'eq_3_18':'heavy-fakeon / GR tensor power spectrum for quadratic inflation','eq_4_16':'full projected fakeon tensor power spectrum for quadratic inflation'},
         'source_reports_singular_decoupling':True,'source_contrasts_regular_starobinsky_case':True,
         'parent_family_terminal':False,'d7_authorized':False,'candidate_gravity_activation':False,
         'classification':'PASS_SOURCE_SCOPE_PHYSICAL_OBSERVABLE_OBJECT_EXISTS_FOR_QUADRATIC_INFLATION_SUBMODEL_ONLY',
         'scope_guard':['DO_NOT_GENERALIZE_TO_STAROBINSKY','DO_NOT_GENERALIZE_TO_ALL_FAKEON_MODELS','BLOCKED_PARTIAL_IS_NOT_FAIL','NO_D7_PROMOTION']}
    Path('iter348-source.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
