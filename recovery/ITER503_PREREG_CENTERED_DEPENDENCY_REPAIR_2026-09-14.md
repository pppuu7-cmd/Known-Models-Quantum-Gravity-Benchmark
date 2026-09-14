# Iter503 — prospectively frozen centered dependency-repair enabling gate

**Frozen before implementation / production.** This is a numerical-method enabling gate for D7-S2. It is not a scientific DECAY/NONDECAY classifier and it does not close any D7 subgate.

## Trigger
Iter501 and Iter502 both terminated as numerical-method blockers. Iter502's fixed 8-way exact subdivision left all 8 completed lanes with failed source point containment; four `2to3` lanes were cancelled before artifact upload. The completed failures are sufficient to reject modest dyadic subdivision as the repair mechanism. The next admissible family, already named in the Iter502 preregistration, is a genuinely dependency-preserving centered/mean-value or direct correlated-factor enclosure.

## Question
Can a centered first-order enclosure of the amplitude dependence recover the unchanged source point-regression values on representative frozen states without shrinking the physical domain or relaxing any scientific threshold?

## Frozen method
For each selected source quantity `F(a)` on a closed amplitude interval `[a0-h,a0+h]`, construct

`F_centered(a) = F(a0) + (a-a0) * D([a0-h,a0+h])`,

where `D` is a validated interval enclosure of the derivative with respect to the **single common amplitude parameter**. The same amplitude variable must be shared through the complete source-faithful geometry/evaluator path; replacing it independently in repeated factors is not permitted.

The gate is diagnostic/enabling: it tests containment quality on a preregistered representative subset before any new 12-lane science campaign. It must preserve the source-faithful Iter500 compact-sandwich/factorized KAK construction and compare against the unchanged Iter491/492 point evaluator.

## Frozen representative subset
- causal classes: `0to5`, `1to4`, `2to3`;
- direction: `[1,1,1,-1,-1,-1]` (the previously observed nonregular/max-switch lane);
- sign: `+1`;
- rho witnesses: `0.35, 0.9, 1.6, 2.7`;
- `R = {6,8,10,12}`;
- amplitude parent boxes: `k = {0,7,15}` from the original Iter501 16-box cover;
- unchanged source-regression amplitudes lying in or on those boxes are used as point controls.

This subset is fixed before implementation because it includes the hardest known channel-switch direction, both boundary and interior amplitude regions, all causal classes, all rho witnesses and all four R values while remaining small enough to discriminate the method before a full production campaign.

## Positive controls
1. Center evaluation at `a0` must reproduce the existing high-precision point evaluator within Iter500 regression tolerances.
2. The centered enclosure must contain both endpoint point evaluations for every frozen test interval and observable tested by this enabling gate.
3. All Iter500 construction/KAK/source-additivity controls used by the selected observable path must pass.

## Negative controls
1. Re-run the direct natural interval enclosure on the identical frozen subset and require reproduction of at least one known containment failure; otherwise this gate has not demonstrated that it is testing the prior blocker.
2. Artificially independent amplitude copies across repeated factors are forbidden as a repair and may be used only as a negative-control demonstration of dependency widening.

## PASS / FAIL
`ITER503_CENTERED_DEPENDENCY_REPAIR_ENABLED_SCOPED` only if all positive controls pass and the centered enclosure contains every frozen endpoint/point control on the representative subset while the direct-natural negative control reproduces the prior widening/failure on at least one case.

`ITER503_CENTERED_DEPENDENCY_REPAIR_INCONCLUSIVE` if centered containment succeeds but the negative control does not reproduce the old blocker, or if only part of the representative subset is resolved without a source/covariance failure.

`ITER503_NUMERICAL_METHOD_BLOCKER` if centered containment fails on any frozen endpoint/point control, derivative enclosure cannot be certified, or any inherited construction/KAK/source-additivity control fails.

## Consequence ceiling
A PASS authorizes a separately preregistered full 12-lane centered/correlated science gate with the unchanged Iter501 scientific thresholds. It is **not** itself evidence for DECAY, NONDECAY, positive-Haar-measure behavior, absolute convergence, spectral-integral convergence, or a terminal D7 label.

## Governance
- no post-hoc amplitude refinement inside Iter503;
- no threshold changes;
- no domain point removal;
- no replacement of source KAK/Toller objects;
- D7-S2 remains `NOT_CLOSED`;
- D7-S3 remains `NOT_CLOSED`;
- D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`;
- `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden;
- Candidate Gravity remains inactive.
