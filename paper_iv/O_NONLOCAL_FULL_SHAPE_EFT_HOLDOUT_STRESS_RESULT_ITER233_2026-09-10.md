# Nonlocal full-shape vs finite-EFT holdout stress result — Iter233

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Input audit:** `O_NONLOCAL_EXPONENTIAL_FULL_SHAPE_HOLDOUT_COMPARATOR_AUDIT_ITER232_2026-09-10.md`  
**Executable:** `code/nonlocal_full_shape_eft_holdout_stress_test.py`  
**Frozen output:** `paper_iv/NONLOCAL_FULL_SHAPE_EFT_HOLDOUT_STRESS_ITER233.csv`

## Test object

Use the dimensionless entire-function transfer shape

`F_N(x) = exp[-(x^2)^N]`

as a synthetic proxy for the correlated form-factor shape. This is deliberately not called a detector observable or a full Newtonian-potential calculation. The purpose is to test the RQIR functional-rigidity logic under a finite local-EFT surrogate.

Calibration window: `x in [0,0.8]`.  
Holdout window: `x in [0.8,1.6]`.  
Comparator: free polynomial in `z=x^2` of finite degree `p`, fitted only on calibration data.  
Shapes: `N=1,2,3`; degrees `p=1,2,3,4,5,6,8,10`.

A Chebyshev numerical basis is used for conditioning, but it spans the same finite polynomial subspace in `z` as the corresponding local derivative expansion.

## Result 1 — calibration quality alone is misleading

For all three entire shapes, calibration RMSE falls extremely rapidly with polynomial degree. Examples:

- `N=1, p=6`: calibration RMSE `4.90e-10`;
- `N=2, p=6`: calibration RMSE `2.44e-7`;
- `N=3, p=8`: calibration RMSE `8.11e-9`.

Thus an apparently perfect finite-window EFT fit does not certify functional equivalence.

## Result 2 — disjoint holdout exposes the nonlocal shape

At the same parameter choices, holdout errors remain nonzero and can be very large:

- `N=1, p=6`: holdout relative RMSE `2.75e-2`;
- `N=2, p=6`: holdout relative RMSE `1.16e1`;
- `N=3, p=8`: holdout relative RMSE `1.69e2`.

For `N=2,3`, increasing polynomial degree can make the calibration error smaller while making extrapolative holdout behavior worse. This is not a claim that higher-order EFT is intrinsically pathological; it demonstrates that a calibration-only score is insufficient when the comparison asks whether an entire correlated shape is predicted outside the fit domain.

For `N=1`, sufficiently high polynomial degree approximates the shape very well even on the chosen holdout window (`p=10` relative RMSE about `1.96e-5`). This is equally important: the functional-rigidity advantage is **domain- and resource-dependent**, not absolute. If the local comparator is allowed enough orders over a bounded domain, the distinction can become arbitrarily small.

## RQIR interpretation

The test validates the following refined rule:

`finite-order coefficient absorption != global functional equivalence`.

But it also validates the converse guardrail:

`entire-function nonlocality != guaranteed observable distinguishability`.

Distinguishability depends on the declared domain, finite EFT order/resource budget, measurement precision, nuisance freedom and parameter ancestry.

Therefore the Iter232 scoped direction survives the synthetic stress test:

`PASS_SYNTHETIC_RIGIDITY_GATE__CALIBRATION_HOLDOUT_SEPARATION_CAN_EXPOSE_ENTIRE_FUNCTION_SHAPE_BEYOND_FINITE_EFT_SUBSPACE`.

This is a methodology/identifiability PASS only. It is not a scientific PASS of `NONLOCAL_QG` and not observational evidence for nonlocal gravity.

## New failure-mode check for Paper III

No new general failure class appears. The result maps directly to already frozen Paper-III principles:

- calibration and holdout data must be separated;
- comparator freedom/resource order must be declared;
- a fit inside the calibration domain cannot establish out-of-domain predictive closure;
- finite-resource approximability must be distinguished from exact structural identity.

`PAPER_III_REOPEN = NO`.

## Heavy-compute decision

Further synthetic brute-force scans have low immediate information gain. A heavier calculation becomes useful only after selecting a **physical** nonlocal observable/data domain and a frozen local-EFT truncation/error prior.

`HEAVY_COMPUTE = IDLE_PENDING_PHYSICAL_DATA_CAPSULE`.

## Family consequence

`NONLOCAL_QG` remains `PARTIAL_SUBFAMILY_ONLY`, but the old family blocker is narrowed. The open problem is no longer whether a correlated non-polynomial direction can exist in principle; it can. The remaining task is to bind one such direction to a same-realization physical observable, comparator/error budget and causality/unitarity disposition, then disposition the material form-factor branches.

Refined next gate:

`NONLOCAL_PHYSICAL_FULL_SHAPE_OBSERVABLE_PLUS_FINITE_EFT_COMPARATOR_ERROR_AND_SAME_REALIZATION_CAUSALITY_CERTIFICATE`

## Iteration status

- Iter233 task completion: **100%**.
- Paper III: **100% scientific/material, FROZEN**.
- Candidate Gravity R3: **24% inactive**.
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D4: `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D7: `NOT_CLOSED`.
