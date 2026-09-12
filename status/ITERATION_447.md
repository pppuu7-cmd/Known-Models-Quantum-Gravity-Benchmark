# Iteration 447 — preregistered local collision-strata power audit

Status: PREREGISTERED BEFORE IMPLEMENTATION / PRODUCTION.

## Scientific object
Attack the remaining D7-S2 blocker after Iter446: the local relative-rapidity collision strata of the fixed source-backed Toller branches. This gate is a local-power diagnostic only. It does **not** assert full causal-vertex finiteness, a distributional extension theorem, spin/refinement-sum control, terminal D7, or Candidate Gravity authorization.

## Frozen matrix
- gamma in {7.0, 8.0}
- j in {2, 5}
- all integer magnetic labels m=-j,...,+j
- both source Toller branches t^(+), t^(-)
- beta collision sequence beta_n = 2^(-n), n=4,...,10
- mpmath precision: 100 decimal digits
- local radial measure benchmark: beta^2 d beta (3-dimensional relative rapidity coordinate)

## Frozen observables
For every (gamma,j,m,branch):
1. finite source amplitude values on all beta_n;
2. pairwise effective local power p_n = -[log|t(beta_{n+1})|-log|t(beta_n)|]/[log beta_{n+1}-log beta_n];
3. finest-window p_local = median of the last three p_n;
4. stability spread = max(last three p_n)-min(last three p_n).

The lane records the worst p_local over m and branch. This is deliberately a source-branch local singularity audit rather than a fitted global vertex model.

## Frozen controls / thresholds
A lane is numerically valid only if all sampled complex amplitudes are finite and every effective power is finite.

Local single-pair radial absolute-integrability support requires BOTH:
- worst p_local < 3.0 - 0.10 (fixed safety margin 0.10), and
- stability spread <= 0.20 for the worst witness.

If any lane violates either threshold with valid numerics, classification is a scientific local-power obstruction for this frozen source-branch object, not an infrastructure failure.

## Frozen aggregate classifier
- `SOURCE_TOLLER_PAIR_COLLISION_LOCAL_POWER_INTEGRABLE_ON_FROZEN_GRID` iff all 4 gamma/j lanes are valid and pass both thresholds.
- `SOURCE_TOLLER_PAIR_COLLISION_LOCAL_POWER_OBSTRUCTION_ON_FROZEN_GRID` iff all 4 lanes are numerically valid but >=1 lane fails the frozen scientific threshold.
- `COLLISION_LOCAL_POWER_NUMERICAL_INVALID` otherwise.

## Interpretation locks
- PASS is scoped to isolated pair-collision local powers on the frozen source branches. It does not establish simultaneous multi-pair collision integrability because shared group variables and invariant contractions can correlate strata.
- FAIL is a scoped obstruction, not a theorem that the physical causal vertex diverges; cancellations, invariant contractions, PV/finite-part or distributional objects remain logically distinct.
- Ordinary absolute integrability, PV/finite part and distributional amplitudes must remain separate.
- Do not replace the published real beta collision variable by beta+i*epsilon.
- No threshold/model retuning after production.
- D7-S3, D7-S4, terminal D7 classifier and EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED remain unauthorized.

## Prospectively permitted next step
If pair-collision PASS: preregister an independent simultaneous two-/three-pair collision audit using explicit shared-variable geometry/invariant contraction before granting further D7-S2 credit.
If pair-collision obstruction: preregister exact branch-sum/invariant-contraction cancellation diagnostics; do not densify the same beta grid merely to seek PASS.
