# Iteration 449 — preregistration: shared-scale multi-pair coherent Toller collision geometry

Status: **FROZEN BEFORE IMPLEMENTATION / BEFORE RESULT**.

## Motivation
Iter448 terminally established that the coherent source branch sum `S=T_+ + T_-` removes the isolated pair-collision local-power obstruction on the frozen `(gamma,j,m,beta)` panel. The next admissible information-gain step is to test whether this cancellation remains compatible with simultaneous shared-variable collision scaling when two or three pair factors approach the same collision scale. This is not yet the complete source-defined magnetic/intertwiner contraction.

## Frozen scientific question
For the same source-faithful equal-spin Toller branch formulas and the same repaired near-`z=1` Euler evaluation, does the no-fit product of coherent branch sums remain locally integrable under a common collision scale `beta` for simultaneous 2-pair and 3-pair sectors?

## Frozen matrix
Independent lanes:
- gamma in `{7,8}`
- j in `{2,5}`
- multiplicity `k in {2,3}`
- all integer `m=-j,...,+j`
- beta=`2^-n`, `n=4,...,10`
- 100 dps production, 130 dps worst-witness recheck

For each `m,beta` compute source branch values and coherent sum `S=T_+ + T_-`. The simultaneous common-scale object is `P_k(beta)=S(beta)^k`; no fitted coefficients, no branch rephasing, no external normalization and no post-result retuning are allowed. The absolute-envelope control is `E_k(beta)=(|T_+|+|T_-|)^k`.

An independent-scale factorization control recomputes the expected product exponent from the single-pair coherent power and verifies that direct common-scale numerical differentiation agrees within the frozen tolerance below. This control is diagnostic of implementation consistency, not a physical independence assumption.

## Frozen thresholds
For each lane:
- all values finite;
- common-scale effective local power for `|P_k|` has worst tail-median over `m` `< 2.90`;
- tail stability spread `<=0.20`;
- 130-dps worst-witness power recheck delta `<=0.02`;
- direct common-scale power agrees with `k * single_pair_power` within `0.02` at the worst witness;
- envelope controls finite.

Aggregate classifications:
- any numerical invalidity -> `MULTIPAIR_COHERENT_COLLISION_NUMERICAL_INVALID`;
- all 8 lanes PASS -> `SOURCE_TOLLER_COHERENT_SHARED_SCALE_TWO_THREE_PAIR_POWER_INTEGRABLE_ON_FROZEN_GRID`;
- otherwise -> `SOURCE_TOLLER_COHERENT_SHARED_SCALE_MULTI_PAIR_POWER_OBSTRUCTION_ON_FROZEN_GRID`.

## Interpretation lock
PASS is only a scoped shared-scale product-geometry result for the coherent Toller matrix-element recombination. It is not the complete source-defined invariant contraction, not a full causal-vertex theorem, not a proof of absolute integrability on all collision strata, and not a PV/distributional equivalence theorem. A FAIL is a scientific obstruction for this frozen no-fit product geometry and must not be repaired by changing thresholds or weights.

D7 terminal classification, `EXISTING_SUFFICIENT/ADAPT_EXISTING/HYBRID_REQUIRED/NEW_REQUIRED`, and Candidate Gravity remain unauthorized.

## Next gate rule
- PASS: next priority is a source-backed reconstruction/audit of the complete coupled magnetic/intertwiner invariant contraction before any D7-S2 closure claim; an independent held-out collision geometry may run only if it adds a genuinely new stratum.
- FAIL: localize the failing multiplicity/witness and move directly to the complete source-backed invariant contraction; do not densify or retune this product gate.
