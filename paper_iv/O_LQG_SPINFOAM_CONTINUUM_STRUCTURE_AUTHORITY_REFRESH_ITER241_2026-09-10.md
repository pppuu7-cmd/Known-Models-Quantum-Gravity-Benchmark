# LQG / spinfoam continuum-structure authority refresh — Iter241

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `LQG_SPINFOAM`  
**Gate:** `LQG_EPRL_SPINFOAM_UV_TO_SEMICLASSICAL_AREA_REGGE_GAMMA_ANCESTRY_AUTHORITY_REFRESH`

## Question

Do the 2026 covariant-LQG continuum-limit results close the old EPRL/spinfoam refinement gap, or do they instead sharpen the exact form that a non-topological continuum certificate must take before the existing EPRL->Regge and downstream gamma/area-metric objects can be composed?

## A. Previously frozen same-realization semiclassical bridge remains valid

Iter181 established a real, scoped same-realization result:

`Lorentzian EPRL microscopic amplitude -> large-spin critical/complex-critical effective dynamics -> Regge action + scoped corrections`.

That result is retained. It is asymptotic and local-in-complex/regime, not a nonperturbative refinement/coarse-graining theorem.

## B. Han 2026 — triangulation summation and candidate UV fixed point

Muxin Han, Phys. Rev. D 113, 084034 (2026), introduces spinfoam stacks and sums an infinite class of Lorentzian spinfoam complexes. In the stated cutoff limit the amplitude localizes on SU(2) flat connections; on topologically trivial manifolds the renormalized amplitude becomes independent of the bulk 2-complex up to boundary data.

Muxin Han, Phys. Rev. D 114, 044040 (2026), extends the programme to the complete covariant-LQG sum over 2-complexes and identifies a candidate small-spin UV fixed point/condensation regime. At leading order the fixed-point dynamics reduces to a topological theory and triangulation ambiguities contract to finitely many boundary coefficients.

These are genuine structural advances:

`PASS_SCOPED_COVARIANT_LQG_SUM_OVER_COMPLEXES_TRIANGULATION_INDEPENDENCE_CONTROL`

and

`PASS_SCOPED_CANDIDATE_UV_FIXED_POINT_WITH_SMALL_SPIN_CONDENSATION_AND_FINITE_BOUNDARY_DATA_CONTROL`.

They do **not** establish the required propagating-gravity crossover because the leading fixed-point theory is topological.

## C. Bruno–Colafranceschi–Mele–Rovelli 2026 — continuum convergence no-go and distributional route

Phys. Rev. D 114, 066005 (published 8 September 2026) gives a model-independent axiomatic analysis of spin-foam continuum limits.

Two results are directly material to KMQGB:

1. under sufficiently strong/natural convergence assumptions, the continuum limit necessarily becomes topological;
2. weakening convergence to a distributional notion, inspired by Refined Algebraic Quantisation, allows the cylinder amplitude to define a rigging map and therefore a canonical physical-Hilbert-space construction, with continuum amplitudes acting as distributions on physical states.

KMQGB classification:

`PASS_STRUCTURAL_GATE__SPINFOAM_CONTINUUM_LIMIT_REQUIRES_NON_STRONG_DISTRIBUTIONAL_OR_EQUIVALENT_CONVERGENCE_TO_AVOID_TQFT_COLLAPSE`.

and conditionally:

`PASS_STRUCTURAL_GATE__UNDER_DISTRIBUTIONAL_CONVERGENCE_ASSUMPTION_CYLINDER_AMPLITUDE_DEFINES_RIGGING_MAP_PHYSICAL_HILBERT_STRUCTURE`.

The second statement is conditional on the required convergence actually holding for the selected dynamics; it is not an EPRL-specific proof that the convergence exists.

## D. Important methodology correction

A naive RQIR requirement of ordinary strong/norm convergence for every spin-foam amplitude sequence would be scientifically overrestrictive: the 2026 no-go result shows that sufficiently strong convergence can force topological dynamics and thereby erase propagating gravitational content.

Therefore the LQG continuum certificate must test **physical convergence**, not merely strongest mathematical convergence. Acceptable routes can include a controlled distributional/rigging-map limit, provided the resulting physical state space and observables are well-defined and the semiclassical propagating sector is recovered.

This is a clarification of the Paper-IV adapter/closure criterion, not a change to frozen RQIR Core v1.0 and not a Paper-III failure mode.

## E. Topological-UV to propagating-GR crossover becomes the decisive missing object

The Han candidate UV fixed point and the Bruno et al. no-go point in the same direction: topological behavior at/under the strongest UV/continuum limit is not by itself a failure. What must be shown is how the physically relevant trajectory/refinement leaves or is corrected beyond that topological leading sector and reaches the known EPRL/Regge semiclassical propagating regime without changing realization by hand.

The required same-realization chain is now sharpened to:

`covariant-LQG/spinfoam UV/refinement object -> declared distributional/physical continuum limit -> controlled non-topological correction/crossover -> EPRL large-spin Regge sector -> area-Regge/area-metric parity couplings -> gamma_EFT/observable -> comparator + propagated errors`.

No audited 2026 source closes this complete chain.

## F. Relation to canonical-LQG coarse-graining

Assanioussi and Zeiß, arXiv:2608.31152, construct coarse Hilbert spaces and effective Hamiltonians for canonical LQG and explicitly write nonperturbative renormalization flow equations. This is a strong structural control for canonical coarse-graining, but it is not automatically the same realization as the Lorentzian EPRL/spinfoam stack dynamics used above.

Classification:

`PASS_STRUCTURAL_CANONICAL_LQG_COARSE_GRAINED_HILBERT_AND_RG_FLOW_EQUATIONS__CROSS_FORMULATION_MAP_TO_EPRL_SPINFOAM_NOT_CLOSED`.

D6 forbids importing these beta functions into the EPRL branch without an explicit equivalence/ancestry map.

## LQG family status after Iter241

The branch is stronger but remains nonterminal:

`BLOCKED_MISSING_REQUIRED_OBJECT__UV_CONTINUUM_STRUCTURE_AND_CANDIDATE_FIXED_POINT_EXIST__TOPOLOGICAL_TO_PROPAGATING_EPRL_REGGE_CROSSOVER_PLUS_AREA_METRIC_GAMMA_ANCESTRY_NOT_CLOSED`.

Updated exact missing certificate:

`EPRL_SPINFOAM_DISTRIBUTIONAL_CONTINUUM_UV_FIXED_POINT_TO_NONTOPOLOGICAL_SEMICLASSICAL_REGGE_CROSSOVER_WITH_AREA_METRIC_GAMMA_ANCESTRY_AND_ERROR_CERTIFICATE`.

This is **not** a scientific FAIL of LQG/spinfoam.

## Paper-III impact

The new no-go is theory-space/refinement specific. It does not create a new transferable experiment/resource-closure failure mode beyond Paper III's frozen provenance/model-transfer/resource rules.

`PAPER_III_REOPEN = NO`.

## Heavy compute

`IDLE_FOR_TERMINAL_DECISION`.

Numerical refinement may become valuable only after a specific EPRL/spinfoam-stack trajectory and a non-topological physical observable are frozen. Brute-force refinement without a declared convergence topology/rigging-map observable would not answer the gate.

## Next gate

Test whether the 2026 gamma-duality/parity EFT result supplies the missing same-realization parameter ancestry or only a phenomenological EFT realization inspired by EPRL:

`LQG_GAMMA_DUALITY_EPRL_TO_PARITY_EFT_PARAMETER_ANCESTRY_AUDIT`
