# 4D CDT line-of-constant-physics prospective compute/data-capsule design — Iter247

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `CDT_EDT`  
**Branch:** `4D_CDT`  
**Gate:** `CDT_4D_LINE_OF_CONSTANT_PHYSICS_PROSPECTIVE_COMPUTE_AND_DATA_CAPSULE_DESIGN`

## Purpose

Convert the Iter224 continuum blocker into a prospectively testable multi-coupling simulation/data capsule while checking whether the currently public 4D CDT data/software are sufficient to execute it without inventing a new implementation.

## 1. Frozen positive controls

The following remain valid and are not re-scored:

- four-dimensional de-Sitter-like semiclassical phase;
- finite-size scaling structure inside the `C_dS` phase;
- fixed-realization normalized curvature-correlator/geon observable at `Delta=0.6`, `kappa_0=2.2`;
- operator, volume, smearing and fit-window controls for that observable;
- public stochastic measurement samples for the one-point geon study.

The current missing object is not `some observable`; it is **continuum transport of a normalized observable along a controlled multi-coupling trajectory**.

## 2. UV/line-of-constant-physics logic from current authority

Ambjorn–Gizbert-Studnicki–Görlich–Németh (2024) formulate a concrete CDT↔FRG matching strategy.

The relevant bare parameter space is `(k_0, Delta, N_4)` with `k_4` tuned/removed by fixed-volume simulations. Only the de-Sitter phase exhibits the finite-size-scaling behavior used for the continuum analysis.

A putative UV trajectory must approach the `A-C_dS` boundary as `N_4 -> infinity` while a renormalized quantity corresponding to the FRG combination is held fixed. Their scaling analysis gives a prospective bare-coupling path of the form

`k_0(N_4) = k_0^UV - c / N_4^[1/2(alpha-2 beta)]`

under the declared critical-exponent assumptions, with lattice spacings scaling schematically as

`a ~ k^(-1) N_4^[-(1+beta/(3 nu_UV))/4]`,

and a distinct temporal spacing `a_t` because the geometries contract anisotropically near the relevant boundary.

The paper's own conclusion is that present numerical accuracy allows a UV fixed point but is not strong evidence for it and is insufficient to decide whether it exists.

## 3. Prospectively frozen simulation capsule

A decision-relevant new 4D CDT campaign must contain, for each selected trajectory:

### Bare/finite-size grid

- at least 4 distinct `N_4` values spanning a useful finite-size lever arm;
- at least 3 coupling points near each pseudo-critical location in `(k_0, Delta)` to estimate local gradients/systematics;
- at least 2 candidate trajectories holding the chosen renormalized matching quantity approximately fixed, so path dependence is testable rather than assumed away;
- explicit `k_4`/volume-fixing procedure and width of the volume constraint.

The exact grid is not frozen numerically here because a production-compatible 4D simulator and its feasible volume range have not yet been qualified. Freezing unattainable volumes before an engine audit would create false precision.

## 4. Required observables at every point

The same ensemble set must measure both **continuum-control observables** and the **physical normalized gravity observable**.

Minimum payload:

1. volume profile and effective-action parameters, including the `Gamma`/shape quantities used in the CDT↔FRG scaling analysis;
2. pseudo-critical location and finite-size scaling variables;
3. spatial/temporal anisotropy diagnostics needed for `a` versus `a_t` scaling;
4. normalized curvature-correlator observable in the same definition as Iter200;
5. operator variants (`Delta Q`, `Delta Q^2`, reconstructed curvature proxy where technically valid);
6. multiple smearing radii with the same stabilization criterion used in the geon study;
7. geodesic-distance/volume normalization object entering the correlator denominator;
8. autocorrelation and independent-chain diagnostics.

A campaign that measures only `Gamma, omega` or only the geon correlator cannot close the RQIR object. They must be measured on the **same multi-coupling continuum trajectory**.

## 5. Continuum transport test

For each candidate line of constant physics:

- infer/fit the critical exponents with finite-size covariance;
- test whether the required inequalities for `a,a_t -> 0` are satisfied;
- derive relative lattice-spacing ratios along the trajectory without assuming the one-point `a ~= 2.1 l_P` conversion is exact;
- express the normalized curvature-correlator distance and extracted mass/shape parameters in units of the prospectively chosen physical scale;
- test convergence under removal of the coarsest one or two lattice points;
- propagate uncertainty from critical scaling, anisotropy, finite volume, operator definition, smearing and fit window.

Only after this may a physical `a -> 0` observable be compared with GR/EFT.

## 6. Comparator requirement

The continuum object must be compared in the **same observable domain**.

Minimum comparator hierarchy:

1. GR/minisuperspace control for the long-distance semiclassical sector;
2. gravitational EFT expectation for curvature-correlation structure where a controlled prediction exists;
3. if no closed analytic GR/EFT prediction for the exact normalized lattice correlator exists, freeze an explicit continuum proxy/matching map and treat its mapping uncertainty as part of the comparator rather than forcing a zero residual.

The word `geon` remains interpretation-level until continuum transport and comparator closure are established.

## 7. Current public-data sufficiency audit

The public Zenodo record associated with the 2026 geon paper contains stochastic measurement samples for the fixed geon ensembles, including the volume and smearing controls. It is valuable for independent reanalysis of the one-point observable.

It does **not** contain a multi-`(k_0,Delta)` line-of-constant-physics ensemble approaching the `A-C_dS` boundary. Therefore it cannot close the continuum trajectory by reanalysis alone.

Classification:

`PASS_SCOPED_PUBLIC_ONE_POINT_OBSERVABLE_REANALYSIS_CAPSULE__INSUFFICIENT_FOR_MULTI_COUPLING_CONTINUUM_TRANSPORT`.

## 8. Current public-engine sufficiency audit

Open CDT implementations exist, including educational/reference 2D/3D and older 3+1 code. The recent geon work, however, describes its triangulation ensembles as generated using a 4D simulation code written by Andrzej Görlich and provided by Dániel Németh, rather than identifying a public versioned production repository that can be pinned by KMQGB.

A different public 3+1 implementation must not be silently substituted for the production realization. It would require a cross-implementation validation showing the same action, move set/detailed balance, topology, volume-fixing, coupling conventions, phase structure and observable normalization.

Current engine status:

`BLOCKED_PRODUCTION_ENGINE__NO_PINNED_PUBLIC_SAME_REALIZATION_4D_CDT_SIMULATOR_IDENTIFIED_FOR_MODERN_GEON_PLUS_UV_SCALING_CAMPAIGN`.

This is a bounded accessibility statement, not a claim that the collaboration code is unavailable to researchers by request.

## 9. Heavy-compute authorization

`PRODUCTION_HEAVY_COMPUTE = NOT_YET_AUTHORIZED`.

Reason: KMQGB currently lacks a pinned/qualified same-realization 4D production engine and a published multi-coupling raw-ensemble capsule. Reanalyzing the one-point Zenodo data cannot produce the missing UV trajectory.

A **one-point replication** of the published geon observable is allowed as validation infrastructure, but it has low D2/D4 information gain because Iter200 already established the observable side.

## 10. Iter247 classification

`COMPUTE_DESIGN_PASS__CDT_MULTI_COUPLING_UV_LINE_OF_CONSTANT_PHYSICS_PLUS_SAME_TRAJECTORY_CURVATURE_CORRELATOR_PROTOCOL_SPECIFIED__CURRENT_PUBLIC_ONE_POINT_DATA_AND_UNQUALIFIED_4D_ENGINE_INSUFFICIENT_FOR_PRODUCTION`.

The physical question is now precise enough to execute once an appropriate 4D engine/data campaign is available.

## 11. Paper-III impact

`PAPER_III_REOPEN = NO`.

The distinction between finite-volume robustness and true continuum-resource closure remains an application of already-frozen Paper-III scaling/calibration/provenance rules.

## 12. Route consequence

BFSS and CDT are both high-scientific-value compute targets but are not immediately production-actionable with the presently audited public resources.

The closure campaign should therefore reselect a branch where the theory-side observable is already analytic and the next step can be performed without external HPC code. `NONLOCAL_QG` is the leading candidate because Iter232–234 already established a finite-parameter full-shape residual direction and a reproducible holdout test; the remaining actionable layer is projection into a real weak-field observational domain with an explicit local-EFT nuisance quotient.

## Next gate

`NONLOCAL_QG_WEAK_FIELD_FULL_SHAPE_REAL_DATA_DOMAIN_AND_EFT_NUISANCE_PROJECTION_AUDIT`
