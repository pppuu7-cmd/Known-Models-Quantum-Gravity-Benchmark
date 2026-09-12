# Iteration 448 — preregistration: Toller branch-sum pair-collision cancellation diagnostic

Status: **FROZEN BEFORE IMPLEMENTATION / BEFORE RESULT**.

## Motivation
Iter447 authoritative repaired production (run 34721563256, head `2b4b70ad3aacb19c4cfc4376077aacf0da9e46c2`) was numerically valid in all 4 lanes but classified `SOURCE_TOLLER_PAIR_COLLISION_LOCAL_POWER_OBSTRUCTION_ON_FROZEN_GRID`: 0/4 lanes passed, worst isolated-branch local power was about 11.00003, with small stability spread. Therefore the next permitted diagnostic is a non-retuned branch-sum cancellation audit, not a denser re-run of Iter447.

## Frozen scientific question
For the same equal-spin Toller source object, same `(gamma,j)` matrix and same beta grid used in Iter447, does the coherent source branch sum `T_plus + T_minus` soften the pair-collision singularity relative to the isolated branches strongly enough to satisfy the same local radial support criterion?

This is a scoped cancellation diagnostic. `T_plus + T_minus` is audited because the source spectral decomposition recombines the two branches at the matrix-element level. This gate does **not** assert that this scalar sum is the full causal-vertex invariant contraction.

## Frozen matrix and numerics
- gamma: `{7,8}`
- j: `{2,5}`
- rho = gamma*j
- m: every integer `-j,...,+j`
- beta = `2^-n`, `n=4,...,10`
- precision: 100 decimal digits
- exact same Toller formulas and exact Euler-transformed near-z=1 hypergeometric evaluation as repaired Iter447
- no fitted coefficients, no relative phase rotation, no reweighting of branches, no altered beta grid

For each `(gamma,j,m,beta)` compute:
1. `T_plus`, `T_minus`;
2. coherent source sum `S = T_plus + T_minus`;
3. absolute-envelope control `A = |T_plus| + |T_minus|`;
4. cancellation ratio `R = |S|/A` when `A>0`.

Estimate effective local powers from adjacent beta points exactly as in Iter447. The lane witness is the largest tail-median coherent-sum power over m. Tail uses the last three adjacent-grid powers. Stability spread is max-min over those three values.

## Frozen gates
A lane is scientifically PASS only if all of the following hold:
- all complex values are finite;
- coherent-sum worst local power `< 2.90` (same Iter447 radial threshold; no weakening);
- coherent-sum worst-witness stability spread `<= 0.20`;
- no hidden numerical cancellation pathology: for the worst witness, recomputation at 130 dps changes the final coherent-sum local-power estimate by `<= 0.02`;
- branch/envelope controls remain finite.

Aggregate classifications are frozen as:
- invalid numerics -> `BRANCH_SUM_COLLISION_CANCELLATION_NUMERICAL_INVALID`;
- all 4 lanes pass -> `SOURCE_TOLLER_BRANCH_SUM_PAIR_COLLISION_POWER_INTEGRABLE_ON_FROZEN_GRID`;
- at least one valid lane fails threshold -> `SOURCE_TOLLER_BRANCH_SUM_PAIR_COLLISION_OBSTRUCTION_ON_FROZEN_GRID`.

Secondary diagnostic fields (non-gating): minimum cancellation ratio on the frozen grid, isolated-branch worst power, absolute-envelope worst power, and coherent-vs-envelope power reduction.

## Interpretation lock
Even aggregate PASS means only that the **coherent two-branch source sum** is locally supported on this frozen pair-collision grid. It is not a theorem for the full causal K5 vertex, not a simultaneous multi-pair result, not a proof of absolute integrability, and not equivalence to PV/finite-part/distributional prescriptions. Aggregate FAIL leaves open cancellation from the actual source-defined invariant contraction or from other coupled factors.

D7 terminal classifier and `EXISTING_SUFFICIENT/ADAPT_EXISTING/HYBRID_REQUIRED/NEW_REQUIRED` remain unauthorized. Candidate Gravity remains inactive.

## Next gate rule
- PASS: preregister explicit shared-variable simultaneous two-/three-pair collision geometry with source-defined invariant contraction structure.
- FAIL: do not retune this gate. Next admissible work is a source-backed invariant-contraction construction/audit that includes the remaining coupled magnetic/intertwiner structure; if that object is unavailable, D7-S2 stays blocked.
