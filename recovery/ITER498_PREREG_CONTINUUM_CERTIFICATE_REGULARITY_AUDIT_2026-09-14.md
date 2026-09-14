# Iter498 preregistration — continuum-certificate regularity audit

**Prospectively frozen before implementation.**

## Authority and purpose
Iter497 terminal authority is `ITER497_RICHARDSON_ENCLOSURE_HOLDOUT_QUALIFIED_SCOPED`, production head `a7517b7fcd12e3a1a129a16881ee3e348a7b72e8`, run `34811898887`, aggregate artifact `10336250420`, digest `sha256:1804657dd14eb939da835c0c8f0eca84a5a93d76014f11016b0f642bcad19f0f`.

Iter497 covers all 768 frozen finite holdouts. It does **not** provide a continuum/interval certificate. Before implementing a rigorous interval proof, Iter498 diagnoses the two principal regularity obstacles in the actual source-faithful q=1 evaluator: (i) KAK branch/near-degeneracy and (ii) switching of the maximizing intertwiner channel inside the `max |contraction|` envelope. Dense sampling in Iter498 is explicitly diagnostic and may never be relabelled as an interval proof.

## Frozen geometry
- q = 1 exactly.
- Active coordinates exactly `[0,1,3,5,6,11]`.
- Same eight frozen 6-D directions and four direction blocks as Iter495-497.
- Causal classes exactly `0to5`, `1to4`, `2to3`.
- Both direction signs.
- Same four rho witnesses.
- Same R grid `{6,8,10,12}` and source-faithful high-precision shared-node/KAK machinery.

## Frozen amplitude audit mesh
Audit the closed amplitude interval `[0.00125,0.00250]` at exactly 9 predeclared points:
`{0.00125, 0.00140625, 0.0015625, 0.00171875, 0.001875, 0.00203125, 0.0021875, 0.00234375, 0.00250}`.
No mesh refinement is permitted after evidence is seen.

## Frozen diagnostics
For every causal × direction × sign × amplitude × R × rho state:
1. Reconstruct all ten source-faithful KAK edges and retain all existing determinant/cycle/reconstruction/additivity controls.
2. Compute all 243 normalized intertwiner contractions exactly as in the current j=1 envelope evaluator.
3. Record the maximizing channel index, largest magnitude `m1`, second-largest magnitude `m2`, relative top-two gap `(m1-m2)/max(m1,1e-300)`, and whether the argmax differs from the previous amplitude sample at fixed causal/direction/sign/R/rho.
4. Record the minimum edge KAK rapidity beta and node KAK rapidity beta over the state as a branch-distance diagnostic.

## Frozen interpretation
Define `REGULAR_SAMPLED_PATH` iff all source/numerical controls pass, there are zero argmax switches across adjacent amplitude samples for every fixed causal/direction/sign/R/rho path, minimum relative top-two gap is at least `1e-6`, and minimum positive KAK beta is at least `1e-6`.

If controls pass but either an argmax switch occurs or the top-two gap falls below `1e-6`, classify `ITER498_MAX_ENVELOPE_NONSMOOTH_BLOCKER_IDENTIFIED_SCOPED`.
If controls pass but KAK beta falls below `1e-6`, classify `ITER498_KAK_BRANCH_MARGIN_BLOCKER_IDENTIFIED_SCOPED` (or both blockers when both conditions occur).
If controls fail, classify `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER498` and do not draw scientific conclusions.

A `REGULAR_SAMPLED_PATH` result only authorizes construction of a prospectively frozen rigorous interval/validated derivative certificate on the same interval. It is not itself that certificate. A channel-switch blocker instead authorizes a direct interval bound on the max-envelope (bounding all competing channels) rather than differentiating a single active branch. A KAK-margin blocker requires a branch-safe KAK/analytic singular-value treatment before interval propagation.

## Matrix
`3 causal classes × 4 direction blocks = 12 independent Actions jobs`, `fail-fast:false`, `max-parallel:12`. Aggregate must consume all 12 raw artifacts.

## Scope guards
D7-S2 remains `NOT_CLOSED`; D7-S3 `NOT_CLOSED`; D7-S4 `PARTIAL_GLOBAL_NOT_CLOSED`. No positive-Haar-measure theorem, Haar convergence/divergence theorem, source spectral certification, terminal D7 classifier, terminal four-way label, or Candidate Gravity activation. Ten-source spectral normalization/order/i-epsilon, Iter461 K5 collision geometry, and PV/conditional/distributional admissibility remain independent blockers.
