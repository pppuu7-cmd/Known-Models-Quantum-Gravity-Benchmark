# Iter458 — Toller Feynman i-epsilon noncompact pilot

Date: 2026-09-13

## Frozen gate
Prospectively preregistered source-faithful finite-`i epsilon` / noncompact pilot using the published spectral prescription `+/- /(rhot-rho \mp i epsilon)` and the already-qualified reduced `k=j=l=1` Toller sector. No `beta+i epsilon`, no damping replacement, no fitted subtraction, and no threshold retuning were allowed.

## Authoritative production
- head: `4f105e5af640208532799cc6556727e592beed6b`
- run: `34744070219`
- raw lane jobs: `103688591312`, `103688591384`, `103688591409`, `103688591439`
- aggregate job: `103688630826`
- raw artifacts:
  - L0 `10312889609`, `sha256:692456f9b2d815484b070c205b48e6e288b7d7d7ec7c232449220f37c277b2c8`
  - L1 `10313209133`, `sha256:5df66aa2c7035ced078e344b383c7dd79b35199da00b1be901ee76a5052f9760`
  - L2 `10313214102`, `sha256:93f2e7470ced6bf03e2f677189ca4372ce1e171dbe4c31564417bb056b0076a5`
  - L3 `10313690943`, `sha256:0e350530e9fb4e2ec5a1b97c20ba0a6ec2c6075ace69541b4ed02aafc0030101`
- aggregate artifact: `10313389047`
- aggregate digest: `sha256:e0ed79ee20c142f4bd67f46495c3b24fd0f6977a07eda6507b086981c438e68a`

## Terminal classification
`SCIENTIFIC_FAIL_ITER458_TOLLER_FEYNMAN_IEPSILON_ORDINARY_TRUNCATION`

All 4 raw lanes were structurally valid, but 0/4 passed the prospectively frozen scientific gate. The aggregate independently reproduced the same classification.

The failure is not explainable as a summation/overflow failure: every lane was finite and direct-vs-compensated accumulation agreement was excellent (`~1e-14` or better). The ordinary symmetric real-line truncation failed the frozen Cauchy/window and closed-branch target tests broadly; representative branch errors remained O(1) to O(10^2) in the m=+/-1 lanes at the smallest frozen epsilon, while final-window Cauchy discrepancies remained O(2) in those lanes. The m=0 lane showed some locally smaller errors but did not rescue the frozen all-lane gate.

The polynomial-route control also exceeded its very tight floating-point tolerance (`~1.19e-7` versus `1e-12`). That control exposes numerical conditioning in the two algebraically identical polynomial evaluation routes, but it does not account for the many-orders-larger branch-target/window failures. Therefore the appropriate terminal interpretation is a scientific failure of this *ordinary symmetric-truncation realization*, not an infrastructure failure and not a theorem against the published distributional prescription.

## Scientific scope
This result does **not** establish divergence of the physical causal vertex, does **not** reject the source-defined Feynman/distributional amplitude, and does **not** close D7-S2. It rejects only the preregistered ordinary symmetric truncation as an adequate realization on this finite panel.

The next admissible route must keep the source `i epsilon` prescription and move to a mathematically justified oscillatory/distributional/contour realization. Threshold weakening or denser repeats of the same ordinary truncation are forbidden.
