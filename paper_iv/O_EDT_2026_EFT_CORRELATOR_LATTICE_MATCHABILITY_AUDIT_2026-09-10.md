# EDT 2026 GR/EFT correlator -> lattice-operator matchability audit (Iter226)

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `CDT_EDT`  
**Branch:** four-dimensional EDT  
**Gate:** `EDT_2026_EFT_CORRELATOR_TO_LATTICE_OPERATOR_MATCHABILITY_AUDIT`

## Question

Can the new universal one-loop GR/EFT curvature or volume correlator already be paired with an existing modern four-dimensional EDT lattice observable to produce an RQIR-ready same-domain comparator residual, or is a new lattice measurement still required?

## A. Analytic comparator side is now closed at scoped level

Laiho and Ratliff, Phys. Rev. D 113, 106032 (2026), derive gauge-invariant Euclidean curvature-curvature and volume-volume correlators through the stated low-energy order. Away from contact terms the final expressions are universal at this order and depend only on Newton's constant and the source-sink separation.

The paper explicitly identifies nonperturbative lattice gravity, and EDT in particular, as a target for comparison.

Classification:

`PASS_SCOPED_ANALYTIC_GR_EFT_CORRELATOR_COMPARATOR_READY_FOR_LATTICE_TEST`.

This removes the old analytic-comparator blocker.

## B. Historical EDT curvature-correlator evidence is not enough for immediate terminal matching

The 2018 conference analysis and Bassler's 2019 dissertation contain nontrivial EDT curvature-correlator evidence: connected correlators display positive-norm / power-law behavior, and the dissertation reports a continuum/infinite-volume scaling analysis with a power near the expected gravitational value under its chosen discretizations.

However this evidence predates the 2026 relational gauge-invariant continuum calculation and does not provide a prospectively frozen one-to-one operator dictionary to the final 2026 invariantized scalar-curvature observable.

In addition, later nonperturbative curvature literature emphasizes that the traditional Regge/deficit-angle local curvature used in early four-dimensional Euclidean DT correlators has an uncontrolled infinite-volume divergence and is not by itself a clean continuum local-curvature observable.

Therefore KMQGB must not retroactively splice the historical correlator to the 2026 EFT formula and call the comparison closed.

Classification:

`PASS_SCOPED_HISTORICAL_EDT_POWER_LAW_CORRELATOR_CONTROL__BLOCKED_OPERATOR_DICTIONARY_AND_CONTINUUM_SAFE_CURVATURE_DEFINITION`.

## C. Volume correlator is promising but is not automatically the same object

EDT has long used normalized volume-volume / shell-volume correlators for finite-size scaling and extraction of the Hausdorff dimension. These are valuable geometric observables.

The 2026 EFT calculation instead constructs a two-point function of an invariantized local volume factor using relational coordinates and quantum-coordinate corrections.

The shared word `volume` does not establish operator identity. Before comparison, one needs an explicit continuum map from the discrete shell/geodesic-distance observable to the invariantized EFT volume operator and matching distance convention.

Classification:

`BLOCKED_VOLUME_OPERATOR_DICTIONARY_FOR_IDENTICAL_DOMAIN_COMPARISON`.

## D. Newton's constant input is unusually favorable

A major advantage of EDT is that the required EFT input, Newton's constant in lattice units, is already constrained by two independent EDT sectors: scalar-particle binding and the de Sitter / Hawking-Moss analysis.

Thus the future correlator comparison need not introduce a freely fitted normalization if the same realization / scale-setting lineage is respected.

This makes the EDT correlator gate unusually high-information compared with many other KMQGB families.

## E. What is now concretely required

The missing object has become operational rather than conceptual:

1. choose one fixed modern EDT action/measure/triangulation realization;
2. define a lattice curvature or volume operator with a declared continuum dictionary to the 2026 invariantized EFT operator;
3. measure its connected two-point function at physical geodesic separation on several lattice spacings / volumes along the same scaling trajectory;
4. use independently determined `G_N` rather than refitting the correlator normalization;
5. extrapolate finite volume and lattice spacing with covariance;
6. compare directly to the universal EFT distance dependence, including EFT truncation/contact-term window restrictions;
7. freeze residual and uncertainty.

## F. Iter226 result

`EDT_EFT_COMPARATOR_READY__LATTICE_MATCH_NOT_YET_EXECUTED_WITH_CONTINUUM_SAFE_SAME_OPERATOR`.

Parent EDT status remains:

`PARTIAL_SUBFAMILY_ONLY__STRONG_SEMICLASSICAL_SCALE_AND_PHENOMENOLOGY_CONTROLS__DIRECT_UNIVERSAL_EFT_COMPARATOR_AVAILABLE__CONTINUUM_SAFE_SAME_OBSERVABLE_LATTICE_TEST_PENDING`.

This is **not** a scientific FAIL and produces zero exclusion evidence toward `NEW_REQUIRED`.

## G. Compute authorization

`PROSPECTIVE_HEAVY_COMPUTE_HIGH_VALUE__CURRENT_PUBLIC_OBJECT_INSUFFICIENT_FOR_TERMINAL_RUN`.

A heavy run becomes strongly justified once raw modern EDT ensembles / correlator measurement code are available for a prospectively declared continuum-safe operator. Re-fitting historical deficit-angle correlators alone is not sufficient because the main uncertainty is operator validity / matching, not numerical precision.

## H. Paper-III impact

No new transferable failure mode appears. Operator identity, calibration/normalization ancestry, same-realization provenance and covariance/error transport are already represented in the frozen Paper-III methodology.

`PAPER_III_REOPEN = NO`.

## Next proving-ground gate

Park the CDT/EDT parent on explicit, high-information missing certificates and move to the remaining nonterminal family with the highest chance of a terminal physical statement rather than another pure authority gap:

`PERTURBATIVE_HIGHER_DERIVATIVE_POLE_PRESCRIPTION_CAUSALITY_OBSERVABLE_FAMILY_CLOSURE_REAUDIT`
