# Current Benchmark Front
Updated: 2026-09-14

## Authoritative frontier
Mainline has advanced through terminal Iter500. Iter461 remains independently queued on its research branch and must not be duplicated.

The consumed D7-S2 chain includes Iter468 source contraction pinning; Iter479 source Toller leading magnetic rank; Iter480B boundary-intertwiner noncancellation; Iter481 full angular/intertwiner network; Iter482 compact common-node correlation; Iter483 shared-node noncompact SL(2,C) geometry; Iter484 source one-edge Toller/KAK lift; Iter485 correlated ten-edge Toller magnetic network; Iter487/489 one-dimensional shared-Haar NONDECAY witness; Iter491 negative fixed-radius sampled thickening; Iter492 shrinking tangent-boundary-layer bracket; Iter493 full-basis q=1 local first/second variation; Iter494 mixed q=1 curvature; Iter495 simultaneous multivariate Taylor stress; Iter496 coefficient-stencil/Richardson convergence; Iter497 independent Richardson-enclosure holdout validation; Iter498 sampled continuum-regularity diagnosis; Iter499 first direct Arb/Acb continuum-envelope attempt and numerical-method blocker; and Iter500 the prospectively frozen compact-sandwich/dependency-preserving KAK enabling qualification that removes that numerical blocker on the full frozen state space.

### Iter497
Authority: prereg `3209cdadeed3dc7d5c1ceb12d72e8841fb688901`, evaluator `742199df295815841725820052aad6a468786ee9`, aggregate implementation `359492922a100582994dc6eb5e44845761b987d2`, production head `a7517b7fcd12e3a1a129a16881ee3e348a7b72e8`; run `34811898887`; aggregate artifact `10336250420`; digest `sha256:1804657dd14eb939da835c0c8f0eca84a5a93d76014f11016b0f642bcad19f0f`. Terminal `ITER497_RICHARDSON_ENCLOSURE_HOLDOUT_QUALIFIED_SCOPED`. All 768/768 independent holdouts are covered; worst coverage ratio `0.483944238351976`. This validates finite holdout generalization, not a continuum theorem.

### Iter498
Authority: prereg `0bedcbaf7b065b050585f2a3505c8bf0e2a14457`, evaluator `2148981be0a808094cd0b4b1b80d2e65fd586807`, aggregate `432773c916872f6300a2c0e4d56872318eaa03bd`, source-lock repair `2bc6756dffdbf10b2d70bdf174657f7f2d478864`; run `34816799788`; aggregate job `103890003162`; artifact `10337025880`; digest `sha256:65851b593dfdc385969e4da67a9e9aa992f328f801521798d2a8c05e349ed814`. Terminal `ITER498_MAX_ENVELOPE_NONSMOOTH_BLOCKER_IDENTIFIED_SCOPED`.

All 12 jobs are valid. Two argmax switches occur on the only sampled nonregular lane `0to5-b0`, direction `[1,1,1,-1,-1,-1]`, sign `+`, rho `2.7`, across amplitude `0.00234375 -> 0.00250` at R=10 and R=12; channel `195 -> 222`. Minimum relative top-two gap is `0.0002002130966857187`; minimum positive KAK beta is `0.5017347792114244`. The blocker is genuine finite max-envelope branch switching, not KAK degeneracy.

### Iter499
Authority: prereg `5fd8124af8edb374d6b48c2a5e2e66cd7b322e54`; Arb core `f16f3106925f13e6e1d847f2d555b5d8fedc5b4d`; evaluator `bd935a81c2d2b1a1f4db78e1355054d92d36760f`; aggregate `cde7d15e03dd6d9a0ac6a78d61b07da4ff3ec517`; workflow/head `33d4dacc705247ab5966f1c01083cd92ee8ab2c1`; run `34818229950`; aggregate job `103895072732`; artifact `10337765174`; digest `sha256:70006ae095cebcb82dddbcfa4af72d40da7c8d3845747411a50a28eecd7b9513`. Terminal `ITER499_NUMERICAL_METHOD_BLOCKER`.

All 12 expected jobs are structurally present, but generic interval-KAK loses certification upstream of the 243-channel contraction. Diagnostic run `34818721003` isolates the dependency problem and motivates compact-sandwich stripping/restoration of outer SU(2) factors plus dependency-preserving internal-edge factorization. No Iter499 slope or drift science result is promotable.

### Iter500
Authority: prereg `04b6f01f603e7b37ed4b0e380eedbdff6b44fe50`; evaluator `5e4054b105cdfc646b85f4e52926dc4dd87c6d50`; regression-semantics repair `4964bb8a882ee840e30c45b71e90bd9edebedf21`; aggregate `0e95a580645aeca467139bcdb2b43e3131ab889b`; production head `aeda66ac6d80a1ac85f43f21fe300194042313bb`; run `34819282062`; source-lock job `103896861477`; aggregate job `103897145400`; aggregate artifact `10338155232`; digest `sha256:f687ee7bcd1cb4afc8404171c3834a321c061b74c56cce8d475d6b60b018f950`. Terminal classification: `ITER500_COMPACT_SANDWICH_FACTORIZED_KAK_QUALIFIED_SCOPED`.

All 4/4 frozen blocks qualify and all 1024/1024 frozen states evaluate with no method blocker, covariance failure or source-regression failure. Aggregate maxima are matrix relative error `1.506093027251261e-16`, beta absolute error `2.220446049250313e-16`, Toller relative error `1.2412085474744689e-15`; minimum certified beta lower bound is `0.5011445004474808`. The old generic interval-KAK limitation is reproduced as a negative control. Iter500 closes the validated-arithmetic enabling prerequisite only; it makes no NONDECAY/Haar/spectral claim.

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census = 15 families.
- D1 = PASS.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3 = PARTIAL.
- D4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D5 = PASS.
- D6 = PASS_RULE_TARGETS_OPEN.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- D7-S0 = PASS; D7-S1 = PASS; D7-S2 = NOT_CLOSED; D7-S3 = NOT_CLOSED; D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED; D7-S5 = NOT_AUTHORIZED; D7-S6 = INACTIVE.
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain forbidden while S2-S4 remain open.
- Candidate Gravity remains inactive.

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Last authoritative status: queued with no jobs; do not duplicate.

### Next D7-S2 dependent gate
Prospectively freeze and run a **fresh direct continuous 243-channel max-envelope interval science gate** using the Iter500 compact-sandwich/factorized KAK construction. It may reuse the already-frozen Iter499 16-box amplitude cover and source point-regression mesh, but production must postdate a new preregistration and the classifier must explicitly allow max-channel crossings rather than assuming a smooth single branch.

Required rules:
- retain the source-faithful Iter500 compact-sandwich node and `0b` KAK construction;
- retain dependency-preserving factorization on internal edges;
- evaluate the direct max over all 243 intertwiner channels with validated interval bounds;
- keep the Iter499 frozen causal classes, q=1 directions/signs, rho witnesses, R grid, slope/drift thresholds and point-containment regression unless prospectively changed for an explicit source-backed reason;
- `fail-fast:false` and independent causal×block lanes;
- valid interval uniform-decay evidence is a scientific failure of the NONDECAY hypothesis, not a CI criterion to be weakened;
- method failure and scientific failure remain distinct.

A full direct interval PASS remains only a one-dimensional signed-direction continuum result; extension to a genuine multidimensional angular neighborhood remains a subsequent gate.

### Ten-source-spectral object audit
Iter468 authority remains exact: run `34770144171`, aggregate artifact `10322025879`, digest `sha256:f45fe3012ed14fa4449554e9cd87edbedbe81a551a694d349adae2211a61a5ff`, terminal `ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED`.

The 2026-09-14 source/mathematical audit removes a false subproblem. The ten source one-wedge boundary-value distributions live in ten independent spectral variables and possess a canonical tensor product once the one-wedge distributional limits are fixed; no arbitrary iterated order is required merely because there are ten variables, and common versus independent epsilon paths agree at this separate-variable tensor-product level. This does **not** justify exchange with group integrations.

The actual unresolved object is the action of that ten-fold boundary-value tensor product on the correlated four-group kernel. Remaining questions include admissible multiplier/test-function class or source-defined extension, spectral growth/decay, Fubini/Tonelli conditions, wavefront/transversality across K5 collision strata, and separation of absolute convergence from conditional/PV/source-defined distributional amplitudes. Iter461 must be consumed before choosing a collision-stratum theorem; do not duplicate it.

## Current blockers
### D7-S2
1. fresh direct continuous 243-channel max-envelope interval science gate using the Iter500 construction and allowing channel crossings;
2. if (1) succeeds, extension from the frozen one-dimensional q=1 direction intervals to a genuine multidimensional angular neighborhood;
3. exact admissibility/pairing of the ten independent source boundary-value distributions with the correlated four-group kernel;
4. K5 collision geometry and correlated boundary-value admissibility (Iter461 stream);
5. separation of absolute convergence from conditional/PV/source-defined distributional amplitudes.

No independent-edge surrogate, shared spectral-variable fiction, fitted cancellation, replacement of source KAK by polar factors, false Toller composition, artificial Haar-suppressing weight, post-hoc q/h refinement, post-hoc safety-factor enlargement, sampled dominance relabelled as interval proof, determinant projection, midpoint substitution for an interval proof, arbitrary iterated spectral ordering, or post-hoc contour modification is allowed.

### D7-S3 / D7-S4
Remain open/partial. Preserve existing negative and blocked transport/closure evidence; do not invent missing closure maps.

## Exact next permitted decisions
1. Prospectively freeze the fresh direct max-envelope interval science gate using Iter500 before production.
2. Only if that gate qualifies may a multidimensional validated angular-neighborhood gate be opened.
3. Continue the correlated-kernel / ten-fold boundary-value admissibility audit independently; do not waste a gate choosing an arbitrary order among the ten separate spectral variables.
4. Consume Iter461 immediately if terminal; never duplicate its authoritative queued run.
5. Keep absolute convergence, iterated/conditional/PV finite parts and source-defined distributional amplitudes distinct.
6. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 66%, integrated path 77%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. Iter500 earns one readiness point because it closes the validated-arithmetic enabling blocker across all 1024 frozen states. The ten-spectral audit materially narrows the spectral subproblem but is not counted as an additional closure point in this update.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No positive-measure or absolute Haar convergence/divergence theorem. No universal causal-EPRL/contour no-go theorem. No terminal D7 label. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
