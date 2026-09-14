# Iter503 preregistration — centered multilinear max-envelope method diagnostic

**Prospectively frozen before Iter503 implementation or production evidence.**

## Authority and motivation

Parent authority is `main` at `df500a32eccf1d8ca9f952e795599c9d2b2f6fcc`.

Iter501 is terminal `ITER501_NUMERICAL_METHOD_BLOCKER`: the direct Arb/Acb natural-interval contraction loses enough dependency that the max-envelope lower bound reaches zero and point-slope containment is not certified. Iter502 is an already-frozen 8-way dyadic repair of the same natural interval expression. At the time of this preregistration, Iter502 is still running; several completed lanes already exhibit the same nonpositive-envelope-lower-bound method blocker. Iter503 is therefore a **method diagnostic only**. It must not consume, replace, predict, or compete with the eventual Iter502 aggregate verdict.

The exact point/network object is unchanged. The point evaluator normalizes each of the ten edge matrices and restores the ten scalar log norms. Because every channel contraction is multilinear and uses every edge matrix exactly once, this is exactly equivalent to contracting the ten unnormalized edge matrices and taking the logarithm of their max envelope. Iter503 keeps the unnormalized formulation used by Iter501/502.

## Frozen representative domain

This is an enabling diagnostic, not the next full science gate.

- q = 1 exactly.
- Causal classes exactly `0to5`, `1to4`, `2to3`.
- Direction block exactly block 0 from Iter495–502, i.e. both frozen directions in that block and both signs.
- Original 16 frozen amplitude boxes exactly; **no further subdivision**.
- Same nine frozen point amplitudes.
- Same rho witnesses `{0.35,0.9,1.6,2.7}`.
- Same R grid `{6,8,10,12}`.
- Same 243 intertwiner channels.
- Same Iter500 compact-sandwich/factorized KAK construction and same source Toller branches.
- 384-bit Arb/Acb arithmetic; no float fallback in validated decisions.

This gives three independent jobs, one per causal class, each covering the complete frozen block-0 signed paths.

## Frozen centered enclosure

For one amplitude box A=[a_lo,a_hi], define its exact midpoint a0=(a_lo+a_hi)/2. For every edge e:

1. `M_e(A)` is the existing Iter500/501 validated Acb enclosure of the **unnormalized** source-faithful Toller edge matrix on A.
2. `M_e^0 = M_e({a0})` is the same validated construction on the degenerate midpoint ball.
3. Entrywise variation radius is
   `R_e,ij = abs_upper(M_e,ij(A) - M_e,ij^0)`.
4. Entrywise center magnitude bound is
   `B_e,ij = abs_upper(M_e,ij^0)`.

For channel I, let `C_I(M_1,...,M_10)` be the existing exact-rational intertwiner contraction. Define the nonnegative absolute network `A_I(X_1,...,X_10)` by replacing every fixed intertwiner coefficient by its absolute value and every edge entry by the corresponding nonnegative X entry, while retaining the identical contraction incidence.

Freeze the variation bound

`Delta_I = upper( A_I(B_1+R_1,...,B_10+R_10) - A_I(B_1,...,B_10) )`.

By multilinearity and the triangle inequality, for every actual amplitude a in A,

`|C_I(M(a)) - C_I(M^0)| <= Delta_I`.

Therefore the centered channel-magnitude enclosure is

- `L_I = max(0, abs_lower(C_I(M^0)) - Delta_I)`
- `U_I = abs_upper(C_I(M^0)) + Delta_I`.

The direct max-envelope enclosure is

- `L = max_I L_I`
- `U = max_I U_I`.

No unique maximizing channel is assumed. Channel crossings, including the Iter498 195→222 crossing, are allowed.

## Mandatory controls

For every frozen state/box:

- all Iter500 construction/KAK containment controls pass;
- source Toller additive identity passes;
- group/cycle consistency passes exactly as in Iter501;
- `Delta_I >= 0` for every channel;
- centered upper bounds are finite;
- midpoint channel contractions from the centered implementation contain the corresponding high-precision midpoint values;
- whenever the centered max-envelope lower bound is positive for every R needed by a slope, the resulting interval slope must contain the frozen high-precision point slope at each of the nine point amplitudes assigned to that box, using the same endpoint ownership convention as Iter501.

Point containment is a validation control, not a tunable target.

## Frozen classifications

`ITER503_CENTERED_MULTILINEAR_METHOD_QUALIFIED_SCOPED` iff all three causal jobs pass all controls, every frozen block-0 amplitude box has a strictly positive centered max-envelope lower bound at every required R/rho state, and all frozen point-slope containment checks pass.

`ITER503_CENTERED_MULTILINEAR_METHOD_INSUFFICIENT_SCOPED` iff arithmetic/source controls pass but at least one frozen state still has zero centered max-envelope lower bound. This is a valid negative result for this enclosure method, not a physics result.

`INFRASTRUCTURE_OR_VALIDATION_FAIL_ITER503` iff source/KAK/arithmetic controls fail, `Delta_I` is invalid, midpoint regression fails, or an eligible positive-envelope box fails frozen point containment.

No Iter503 outcome is a NONDECAY/DECAY science classification.

## Decision rule after Iter503

- If qualified: only then preregister a full 12-job science gate using the same centered formula and the already-frozen Iter501 science thresholds. Do not change thresholds, directions, amplitudes, rho, R, or channels.
- If insufficient: do not add post-hoc mesh refinement. The next admissible method is a genuinely dependency-preserving first-order affine/Taylor/mean-value model for the common scalar amplitude.
- If validation fails: repair only the identified implementation/containment defect before any science claim.

## Scope guards

D7-S2 remains `NOT_CLOSED`; D7-S3 remains `NOT_CLOSED`; D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`. No positive-Haar-measure theorem, Haar convergence/divergence theorem, source spectral certification, terminal D7 classifier, terminal four-way label, or physical causal-vertex finiteness/divergence theorem is authorized. Candidate Gravity remains inactive.

The ten-source spectral pairing problem and Iter461 K5 collision geometry remain independent blockers.