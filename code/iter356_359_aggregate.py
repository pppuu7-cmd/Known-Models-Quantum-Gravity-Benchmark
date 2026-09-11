#!/usr/bin/env python3
import json, pathlib
root=pathlib.Path("iter356-359-results")
files=list(root.rglob("*.json"))
docs=[json.load(open(p)) for p in files]
uv=[d for d in docs if d.get("iteration")==356]
dc=[d for d in docs if d.get("iteration")==357]
sp=[d for d in docs if d.get("iteration")==358]
gd=[d for d in docs if d.get("iteration")==359]
assert len(uv)==5, len(uv)
assert len(dc)==3, len(dc)
assert len(sp)==4, len(sp)
assert len(gd)==1, len(gd)
assert all(d["has_same_product_scaling_with_valid_time_extension"] and d["has_same_product_scaling_with_invalid_time_extension"] for d in dc)
central=next(d for d in uv if abs(d["delta"]-0.54)<1e-12)
r1e4=next(x for x in central["volume_ratio_stress"] if x["N4_ratio"]==1e4)
out={
 "iteration_bundle":"356-359",
 "classification":"PASS_SCOPED_CDT_IR_OBSERVABLE_AND_UV_PRODUCT_EXPONENT_CONSISTENCY__DELTA_0P54_PM_0P04_IS_ONE_SIGMA_COMPATIBLE_WITH_REQUIRED_HALF_POWER_BUT_PRODUCT_ONLY_SCALING_DOES_NOT_FIX_OMEGA_TIME_EXTENSION_AND_FULL_CONTINUUM_OBSERVABLE_ERROR_LEDGER_REMAINS_BLOCKED",
 "uv_target_delta":0.5,
 "uv_reported_delta_central":0.54,
 "uv_reported_delta_sigma":0.04,
 "uv_target_distance_in_sigma":abs((0.54-0.5)/0.04),
 "central_coupling_proxy_ratio_N4_1e4":r1e4["coupling_proxy_ratio"],
 "central_fractional_drift_N4_1e4":r1e4["fractional_drift"],
 "product_scaling_time_extension_identifiable":False,
 "spectral_dimension_fit_D0":sp[0]["D_S_at_zero"],
 "spectral_dimension_large_sigma_limit":4.02,
 "family_status":"PARTIAL_SUBFAMILY_ONLY",
 "family_terminal":False,
 "d7_promotion_authorized":False,
 "refined_blocker":"CDT_SEPARATE_OMEGA_GAMMA_CRITICAL_SCALING_PLUS_SOURCE_DEFINED_4D_CONTINUUM_TRAJECTORY_AND_LATTICE_SPACING_MAP_WITH_PROPAGATED_FINITE_SIZE_DISCRETIZATION_NUMERICAL_ERRORS_PLUS_INVARIANT_PHYSICAL_OBSERVABLE_AND_SAME_DOMAIN_COMPARATOR",
 "scope_guard":gd[0]["scope_guard"]
}
with open("iter356-359-summary.json","w") as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
