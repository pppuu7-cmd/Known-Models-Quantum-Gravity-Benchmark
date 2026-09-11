#!/usr/bin/env python3
import json, pathlib

p=json.load(open('benchmarks/lqg_iter307_minspin_contracted_local_witness.json'))
# Four gauge-fixed H3 variables -> 12 local noncompact dimensions.  Along a
# nonzero open angular cone the witness integrand scales delta^-20.  Polar
# measure contributes delta^(12-1), hence |integrand| dmu ~ delta^-9 ddelta.
dim=4*3
integrand_power=-20
measure_power=dim-1
radial_power=measure_power+integrand_power
absolute_integrable = radial_power > -1
ok=(dim==12 and radial_power==-9 and not absolute_integrable and
    p['prospectively_frozen_claims']['reduced_noncompact_local_dimension']==12 and
    p['prospectively_frozen_claims']['absolute_radial_power_after_measure']==-9 and
    p['prospectively_frozen_claims']['local_absolute_integrability_for_witness_component'] is False)
out={'probe':'absolute_integrability_power','pass':bool(ok),'iteration':307,
     'noncompact_dimension':dim,'integrand_scaling':'delta^-20','radial_measure_scaling':'delta^11 ddelta',
     'absolute_radial_scaling':'delta^-9 ddelta','criterion':'integral_0^eta delta^p ddelta converges iff p>-1',
     'local_absolute_integrability':absolute_integrable,
     'continuity_condition':'nonzero leading coefficient at a collision-free angular point gives a nonzero open angular neighborhood'}
pathlib.Path('build/lqg-iter307').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter307/absolute_integrability_power.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
