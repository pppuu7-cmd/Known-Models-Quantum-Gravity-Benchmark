# BFSS native localized/non-uniform phase identifier and operator-dictionary audit — Iter246

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Parent family:** `STRING_MTHEORY_HOLOGRAPHY`  
**Branch:** `BFSS_BMN_MATRIX_MTHEORY`  
**Gate:** `BFSS_NATIVE_PHASE_IDENTIFIER_AUTHORITY_AND_OPERATOR_DICTIONARY_AUDIT`

## Question

Is there already a published BFSS-native observable whose value/eigenvalue distribution distinguishes the Dias–Santos uniform, non-uniform and localized phases along the emergent M-theory circle, so that the Iter245 production holdout can be launched without inventing a new operator dictionary?

## A. Temporal holonomy / partial deconfinement — real BFSS information

Bergner et al. (2022) use the temporal Polyakov loop and its phase distribution to characterize confinement/deconfinement in BFSS/BMN. They further discuss partial deconfinement as a way to estimate how many matrix/color degrees of freedom participate in a black-hole sector; the Polyakov-line phase distribution can encode that participation fraction.

Classification:

`PASS_SCOPED_BFSS_TEMPORAL_HOLONOMY_CONFINEMENT_AND_PARTIAL_DECONFINEMENT_DIAGNOSTIC`.

This is useful for thermodynamic branch/metastability diagnostics.

## B. Why temporal Polyakov is not yet the Dias–Santos localization operator

The Dias–Santos 2025/2026 localized/non-uniform phases are distinguished on the gravity side by the distribution of the black object along the **M-theory circle**.

BFSS is a 0+1 dimensional gauge quantum mechanics. Its temporal Polyakov loop is a holonomy around the Euclidean thermal circle. It is not automatically a Wilson loop around the emergent M-theory spatial circle.

A direct identification would require a published operator/dictionary showing that a BFSS observable reconstructs the M-theory-circle density/localization profile for the same strongly coupled state.

No such operator/dictionary was located in the bounded authority sweep through 2026-09-10.

## C. D1/SYM(1+1) analogy is not an equivalence map

Dias–Santos explicitly propose the D1-brane / SYM(1+1) theory on a spatial circle as an analogy. In that system, the **spatial Wilson-loop eigenvalue distribution** cleanly distinguishes:

- uniform phase: approximately uniform distribution;
- non-uniform phase: non-uniform but gapless distribution;
- localized phase: gapped/localized distribution.

They state that insights from this system may help understand analogous BFSS phases and that a first step is to understand the non-uniform/localized phases using BFSS degrees of freedom.

Therefore the D1 result establishes a promising design analogy, not a same-realization BFSS operator.

Classification:

`PASS_ANALOGY_CONTROL__D1_SPATIAL_WILSON_EIGENVALUE_PHASE_CLASSIFIER__NO_BFSS_NATIVE_OPERATOR_TRANSFER_AUTHORIZED`.

## D. Scalar matrices and D0-brane position information

The diagonal/eigenvalue structure of BFSS scalar matrices is often interpreted semiclassically as D0-brane position information, while off-diagonal modes represent strings between them. Scalar extent/eigenvalue observables are therefore physically informative.

However, the emergent M-theory circle in the relevant strongly coupled eleven-dimensional regime is not one of the nine bare transverse scalar directions. No audited authority gives a gauge-invariant map

`{X_i matrix data, temporal holonomy, color-sector information} -> M-theory-circle localization density`

with a controlled large-N/strong-coupling error.

Thus scalar eigenvalues cannot be promoted to the required phase identifier without additional theory.

## E. Bounded literature result

The 2021–2026 authority sweep located:

- temporal Polyakov/holonomy confinement and partial-deconfinement diagnostics;
- scalar extent/eigenvalue and black-hole-sector interpretations;
- the gravity-side prediction of the new uniform/non-uniform/localized BFSS phases;
- the D1 spatial-Wilson-loop analogy;

but **no published BFSS-native operator dictionary that directly resolves localization along the M-theory circle for the new Dias–Santos phases**.

This is a search-scope-bounded result, not a theorem of nonexistence.

## Iter246 disposition

`BLOCKED_PHASE_IDENTIFIER__TEMPORAL_HOLONOMY_AND_PARTIAL_DECONFINEMENT_DIAGNOSTICS_EXIST__NO_PUBLISHED_BFSS_NATIVE_M_THEORY_CIRCLE_LOCALIZATION_OPERATOR_DICTIONARY_LOCATED`.

Consequences:

- Iter245 thermodynamic holdout design remains valid;
- temporal Polyakov loop may be used as a thermodynamic/metastability diagnostic;
- it may **not** be claimed as direct uniform/non-uniform/localized M-circle classification;
- production heavy compute remains unauthorized because a run at frontier-low temperature would be expensive without a direct phase classifier and because the candidate engine still needs reproducibility qualification.

## Heavy compute

`PRODUCTION_HEAVY_COMPUTE = PARKED_PENDING_OPERATOR_DICTIONARY_OR_JUSTIFIED_THERMODYNAMIC_FREE_ENERGY_CAMPAIGN`.

A small code-regression pilot remains permissible but has lower Paper-IV information gain than moving to a branch whose physical observable already exists.

## Paper-III impact

`PAPER_III_REOPEN = NO`.

The obstruction is an application-specific observable-identity/dictionary problem already covered by frozen resource/provenance semantics.

## Route decision

Park BFSS production planning on the explicit operator-dictionary/resource blocker and reselect the next compute-actionable branch.

The leading target is 4D CDT because KMQGB already has:

- a fixed 4D normalized curvature-correlator observable;
- operator/volume/smearing controls;
- public stochastic samples;
- a semiclassical de-Sitter-like phase;
- a sharply defined missing line-of-constant-physics / `a -> 0` continuum transport problem.

## Next gate

`CDT_4D_LINE_OF_CONSTANT_PHYSICS_PROSPECTIVE_COMPUTE_AND_DATA_CAPSULE_DESIGN`
