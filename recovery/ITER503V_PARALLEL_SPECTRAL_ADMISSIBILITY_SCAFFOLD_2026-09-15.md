# Iter503V parallel spectral admissibility scaffold — 2026-09-15

## Status

Outcome-blind analytical scaffold only. This document does **not** close D7-S2, D7-S3, or D7-S4, does not establish absolute convergence, and does not authorize a terminal D7 selector. It is independent of the still-active Iter503V endpoint-contract verifier and of the queued Iter461 K5 collision-partition computation.

## Purpose

Freeze the proof obligations needed before the already-constructed ten-fold one-wedge boundary-value tensor product may be applied to the correlated four-group kernel. The point is to prevent a later exchange of a distributional boundary-value limit with correlated group integrations from being treated as automatic.

## Frozen objects and notation

Let `E(K5)` be the ten edges of the complete graph on five vertices. Associate one independent spectral variable `lambda_e` to every `e in E(K5)`.

For every edge let `T_e` denote the fixed one-wedge boundary-value distribution in the corresponding variable. After the one-wedge limits are fixed, write

`T = tensor_{e in E(K5)} T_e`

for the separate-variable ten-fold tensor product.

Let `g=(g1,g2,g3,g4)` denote the four gauge-fixed group variables and let `K(lambda;g)` denote the correlated source/group kernel entering the K5 amplitude after gauge fixing. The unresolved object is the pairing obtained only after `K` has been shown to belong to a source-appropriate test/multiplier class for `T` after the required group integrations.

## What is already allowed

The separate-variable tensor product `T` may be formed once the ten one-wedge boundary values are fixed. Equality of common-regularizer and independent-regularizer approaches at that separate tensor-product level, when established, is an identity **before** the correlated group integration.

It must not be promoted to any of the following without an additional theorem:

1. interchange of the ten boundary-value limits with the four group integrations;
2. absolute convergence of the correlated amplitude;
3. Fubini/Tonelli interchange across singular collision regions;
4. existence of an ordinary function obtained by evaluating `T` on an unqualified correlated kernel;
5. a principal-value prescription unless that prescription is separately source-defined and proved compatible.

## Admissibility classes to be proved

### `A_abs` — absolute/Tonelli class

A correlated kernel belongs to `A_abs` on a region only if a nonnegative integrable majorant controls the source-required integrand there, uniformly in the boundary-value regulator(s), strongly enough to justify the required limit/integration and integration-order exchanges by dominated-convergence/Tonelli/Fubini arguments.

For every source-required spectral multi-index `beta`, the proof must explicitly state whether the corresponding `partial_lambda^beta K(lambda;g)` is also controlled. A zeroth-order bound does not automatically authorize derivative-dependent distribution pairings.

A valid `A_abs` proof is sufficient for the corresponding exchange; absence of such a proof is **not** evidence of divergence.

### `A_dist` — distribution-pairing class

If absolute control is unavailable, a kernel may instead enter `A_dist` only when the map

`lambda -> integral K(lambda;g) dg`

is proved to lie continuously in a test/multiplier space on which `T` acts. The topology and all seminorms needed by the orders of the one-wedge distributions must be stated explicitly. Continuity must be established after handling the correlated group singularities, not inferred solely from pointwise smoothness away from them.

A valid `A_dist` proof establishes a source-defined distributional pairing. It does not by itself imply absolute convergence, order-independent improper integration, or principal-value equivalence.

## Collision-stratum obligations

Let the future Iter461 result provide the exact K5 collision partition `Sigma = union_alpha Sigma_alpha` and the associated incidence/codimension data. Until that artifact is consumed, no particular collision-stratum theorem is frozen as satisfied.

For each returned stratum `Sigma_alpha`, at least one of the following routes must be discharged prospectively:

1. **Integrable-majorant route.** Prove an integrable local majorant for every source-required spectral derivative/seminorm, with enough uniformity to pass the boundary-value limit through the group integral.
2. **Microlocal route.** Compute the relevant wavefront/conormal sets and prove the required Hörmander-style noninteraction/transversality criterion for the pullback/product/pushforward actually used by the correlated kernel.
3. **Blocked route.** Record the stratum as `OPEN_BLOCKED` with the missing estimate/transversality statement named explicitly.

Failure of route 1 does not imply failure of route 2. Failure to prove either route does not authorize an ad hoc regularization.

## Away-from-collision obligation

On the complement of the collision set, establish smooth dependence on all ten independent spectral variables together with group-integrable bounds for every seminorm/derivative required by `T`. This regular-region proof must be separated from all collision-stratum arguments so that singular geometry is not hidden inside a global formal manipulation.

## Exchange ledger

Every later correlated-kernel argument must label each exchange with exactly one currently proved status:

- `ABSOLUTE_JUSTIFIED` — justified through `A_abs`;
- `DISTRIBUTIONAL_JUSTIFIED` — justified through a named `A_dist` continuity theorem;
- `PV_SOURCE_DEFINED` — only if an explicit source-defined principal-value prescription and compatibility proof exist;
- `CONDITIONAL_ONLY` — conditional/improper convergence demonstrated but no stronger exchange theorem proved;
- `OPEN_BLOCKED` — required exchange not yet justified.

The labels `ABSOLUTE_JUSTIFIED`, `DISTRIBUTIONAL_JUSTIFIED`, and `PV_SOURCE_DEFINED` are theorem labels, not numerical observations.

## Iter461 dependency

The queued authoritative collision computation remains run `34748503239`, branch `research/iter461-k5-collision-partitions`, head `05c7f87c8519349057332bf90021f1128e1eefc3c`. No duplicate collision run is authorized by this scaffold.

After Iter461 is terminal and its artifact is validated, the next analytical action is:

1. import the exact strata/incidence data without reinterpretation;
2. attach to each stratum the weakest sufficient route among the three collision obligations above;
3. preregister the first unresolved local theorem/estimate before attempting it;
4. keep all still-unproved exchanges `OPEN_BLOCKED`.

## Independence from Iter503V / D7-S2 numerical gate

Iter503V and this spectral-admissibility front are logically independent. A future `ITER503V_ENDPOINT_CONTRACT_CONFIRMED` result may authorize preregistration of the full centered/correlated 12-lane numerical science campaign, but it does not discharge any spectral collision or Fubini/wavefront obligation here. Conversely, progress on this scaffold cannot substitute for the frozen Iter503V endpoint contract.

## Global guards

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- No terminal D7 selector is authorized.
- Candidate Gravity remains inactive.
- No numerical threshold, amplitude box, channel set, or physical scope is changed by this document.
