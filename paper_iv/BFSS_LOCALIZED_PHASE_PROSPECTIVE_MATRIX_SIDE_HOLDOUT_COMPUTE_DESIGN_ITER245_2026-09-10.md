# BFSS localized/non-uniform phase — prospective matrix-side holdout compute design (Iter245)

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Parent family:** `STRING_MTHEORY_HOLOGRAPHY`  
**Branch:** `BFSS_BMN_MATRIX_MTHEORY`  
**Gate:** `BFSS_LOCALIZED_PHASE_PROSPECTIVE_MATRIX_SIDE_HOLDOUT_COMPUTE_DESIGN`

## Purpose

Design a genuinely independent BFSS-side test of the Dias–Santos 2025–2026 gravity-side localized/non-uniform phase predictions without importing the gravity solution into the matrix calculation and without pretending that an existing generic BFSS observable is already a phase classifier.

This is a **prospective compute-design certificate**, not a completed numerical validation.

## 1. Frozen target theory

The target theory is the **full supersymmetric BFSS matrix quantum mechanics**, not a bosonic or Gaussian surrogate.

The final production result must be reported in the BFSS limit. A BMN mass/flux deformation may be used only as a numerical stabilizer if an explicit `mu -> 0` extrapolation is performed and included in the uncertainty ledger. A finite-`mu` result alone must be labelled BMN, not BFSS.

## 2. Gravity-side holdout frozen before matrix-side high-statistics analysis

Primary canonical target from Dias & Santos, *Localized states of BFSS super quantum mechanics*:

`tau_c * N^(5/9) = 0.61196576`

with

`f_c * N^(-4/9) = -1.04043637`.

The same paper gives the Gregory-Laflamme onset

`tau_GL * N^(5/9) = 0.59280163`

and

`epsilon_GL * N^(-4/9) = 1.71316176`.

The final discussion states that the localized phase dominates the canonical ensemble at sufficiently low temperatures and identifies the first-order localized/uniform transition near the quoted `0.6118` scaling variable. The experimental HTML text immediately around Eq. (92) contains an internal wording inconsistency about which branch dominates on either side; KMQGB therefore freezes the **numerical crossing coordinate and the final-discussion phase ordering**, not the contradictory local prose sentence.

The matrix-side analysis may not retune the target after observing the data.

## 3. Derived finite-N temperature targets

Using

`tau_c(N) = 0.61196576 / N^(5/9)`

and

`tau_GL(N) = 0.59280163 / N^(5/9)`, 

the prospective canonical grid is:

| N | tau_c target | tau_GL target |
|---:|---:|---:|
| 8 | 0.192757 | 0.186721 |
| 12 | 0.153880 | 0.149061 |
| 16 | 0.131151 | 0.127044 |
| 24 | 0.104699 | 0.101420 |
| 32 | 0.089234 | 0.086440 |
| 48 | 0.071237 | 0.069006 |
| 64 | 0.060715 | 0.058813 |

These numbers are KMQGB-derived from the published large-N scaling relation; they are not independent literature measurements.

## 4. Existing public simulation engine — candidate, not validator

The public `gbergner/SYM1DMMMT` repository is a candidate numerical engine. Its repository description states that it contains BFSS and BMN implementations, including serial, GPU/OpenACC/CUDA and MPI variants. Its README explicitly calls the current code a development version.

Code inspection confirms existing measurement routines for, among other quantities:

- internal energy (`Calc_energy.f90`, documented as `E/N^2`);
- temporal Polyakov-loop magnitude (`Calc_Polyakov.f90`);
- matrix extent / `Tr X^2`;
- eigenvalue-type matrix observables;
- RHMC dynamics and fermionic machinery.

This is sufficient to justify an **engine reproducibility pilot**.

It is not sufficient to certify the code as the RQIR production engine without a pinned revision, build/environment manifest, known-result regression, seed control and autocorrelation/error audit.

## 5. Direct phase-identifier problem

Dias–Santos explicitly state that a first BFSS-side task is to understand the non-uniform/localized phases using BFSS degrees of freedom. They point to the D1/SYM(1+1)-on-a-circle system, where spatial Wilson-loop eigenvalue distributions provide clean uniform/non-uniform/localized classifiers.

That D1 classifier does **not** transfer automatically to BFSS quantum mechanics: BFSS has only Euclidean time as a gauge-theory coordinate and no explicit spatial gauge circle whose Wilson loop is the D1 order parameter. The M-theory circle is emergent/dual rather than a bare BFSS spatial lattice direction.

Therefore the current direct-classifier status is:

`BLOCKED_PHASE_IDENTIFIER__BFSS_NATIVE_M_THEORY_CIRCLE_LOCALIZATION_OBSERVABLE_NOT_YET_FROZEN`.

Temporal Polyakov loop, energy, `Tr X^2` and scalar eigenvalue diagnostics are useful but must not be relabelled as direct proof of localization along the M-theory circle without an explicit operator/dictionary.

## 6. Phase 1 — thermodynamic holdout

Before attempting a microscopic localization classifier, the first independent target should be a thermodynamic test.

### Required observables

At each `(N, L, tau, mu)` point record at minimum:

- internal energy `E/N^2`;
- temporal Polyakov loop and holonomy-eigenvalue diagnostics;
- `Tr X^2` / scalar extent and tails/runaway diagnostics;
- bosonic action components;
- fermionic/RHMC acceptance and solver diagnostics;
- any available matrix-eigenvalue summaries useful for metastability detection.

### Canonical transition strategy

A first-order transition must be inferred from equilibrium thermodynamics, not hysteresis alone.

Allowed evidence stack:

1. hot- and cold-start runs to reveal metastable branches;
2. branch-conditioned measurements where statistically defensible;
3. energy/action curves across the prospectively frozen window around `tau_c(N)`;
4. free-energy difference obtained by a declared thermodynamic-integration scheme with a controlled reference normalization;
5. finite-`L`, finite-`N`, finite-`mu` and sampling extrapolations;
6. crossing analysis performed with frozen fit/interpolation rules.

Hysteresis, long dwell times or bimodality may diagnose a first-order region but do not by themselves establish the equilibrium free-energy crossing.

## 7. Phase 2 — microcanonical / non-uniform holdout

The stronger second-stage target is the predicted non-uniform window and Gregory-Laflamme endpoint.

Frozen gravity-side targets include:

- `epsilon_GL * N^(-4/9) = 1.71316176`;
- the localized/non-uniform topology-change region begins near scaled energy `~1.51` (the paper quotes a narrow numerical transition/cusp region from the gravity-side branch construction).

A direct BFSS microcanonical test is substantially harder because BFSS lattice simulations are naturally canonical and because no BFSS-native microscopic localization classifier has yet been frozen.

Phase 2 therefore remains:

`DESIGN_TARGET_ONLY__MICROCANONICAL_NONUNIFORM_WINDOW_REQUIRES_ENSEMBLE_RECONSTRUCTION_OR_DENSITY_OF_STATES_METHOD_PLUS_NATIVE_PHASE_IDENTIFIER`.

## 8. Continuum, large-N and deformation ladder

A scientific production campaign must not test the large-N prediction at one finite lattice point.

Required hierarchy:

1. **engine regression** at established temperatures where published BFSS/BMN energies exist;
2. **continuum ladder** in temporal lattice size `L` at fixed `(N, tau, mu)`;
3. **deformation ladder** in BMN regulator/flux `mu` where used, with explicit `mu -> 0` extrapolation;
4. **finite-N ladder** with multiple `N` values;
5. **temperature scan** centered prospectively on the derived `tau_c(N)` window;
6. joint extrapolation to the BFSS continuum/large-N target with covariance propagation.

The order of limits must be declared and stability under reasonable alternative orderings tested where feasible.

## 9. Resource reality check

Recent precision BFSS/BMN simulations reported efficient access down to about

`tau = 0.25`

using a small BMN deformation to stabilize flat directions while performing continuum/large-N extrapolation.

The Dias–Santos transition scales far lower at useful N:

- `N=16 -> tau_c ~= 0.131`;
- `N=32 -> tau_c ~= 0.089`;
- `N=64 -> tau_c ~= 0.061`.

Thus a decisive large-N test is a **frontier low-temperature HPC campaign**, not a routine current-runner calculation. Flat-direction runaways become increasingly serious in precisely this regime.

## 10. Mandatory uncertainty / failure ledger

Production evidence must include at least:

- thermalization burn-in and independent-chain agreement;
- integrated autocorrelation/effective sample size;
- RHMC approximation/solver residual controls;
- fermion/Pfaffian phase or sign treatment and reweighting policy where relevant;
- flat-direction/runaway rejection policy defined prospectively, not tuned after seeing the target;
- finite temporal lattice-spacing extrapolation;
- finite-N extrapolation;
- BMN `mu -> 0` extrapolation if deformation is used;
- temperature calibration and scan interpolation uncertainty;
- metastability/tunnelling and branch-sampling uncertainty;
- thermodynamic-integration reference and path dependence checks;
- analysis-code version and random-seed provenance.

## 11. Pre-registration / anti-tuning rule

The gravity-side target coordinates, temperature windows, primary observables, continuum/N/mu ladders, exclusion rules, fit family and acceptance thresholds must be frozen before the high-statistics holdout run.

Forbidden:

- choosing the temperature window after seeing where a feature appears;
- changing the phase classifier to improve agreement;
- dropping unstable chains without a predeclared diagnostic rule;
- treating gravity-side output as a prior in the matrix simulation;
- reporting only the N or L values closest to the predicted crossing.

## 12. Iter245 classification

`COMPUTE_DESIGN_PASS__BFSS_THERMODYNAMIC_HOLDOUT_AND_LIMIT_ERROR_LADDER_SPECIFIED__DIRECT_LOCALIZED_NONUNIFORM_PHASE_IDENTIFIER_AND_FRONTIER_LOW_T_LARGE_N_RESOURCE_CLOSURE_OPEN`.

This is a real advance from `interesting gravity-side prediction` to a falsifiable prospective matrix-side protocol, but it is not a BFSS validation and not a String/M-theory family PASS.

## 13. Compute authorization

`PRODUCTION_HEAVY_COMPUTE = NOT_YET_AUTHORIZED`.

Reason: the available public engine is a development code requiring independent reproducibility qualification; the direct BFSS-native localized/non-uniform phase identifier is not frozen; and the required `tau` range is below the recent efficient precision regime for scientifically useful N.

A **small engine-reproducibility pilot** is scientifically permissible after a pinned code revision/build manifest is frozen. Such a pilot is validation infrastructure only and must not be scored as testing the Dias–Santos holdout.

## 14. Paper-III impact

No new transferable Paper-III failure class appears. The issues encountered — apparatus/observable identity, extrapolation ancestry, hidden conditioning, resource limits and independent holdout discipline — are already covered by Paper III's frozen methodology.

`PAPER_III_REOPEN = NO`.

## Next gate

Because full BFSS production is not yet action-ready, the immediate route is:

`BFSS_NATIVE_PHASE_IDENTIFIER_AUTHORITY_AND_OPERATOR_DICTIONARY_AUDIT`

If no defensible BFSS-native localization observable is located/derived from published authority, park BFSS production planning and reselect the next compute-actionable branch, with 4D CDT as the leading candidate.
