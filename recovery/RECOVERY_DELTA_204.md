# KMQGB recovery delta — Iteration 204

**Date:** 2026-09-10  
**Base canonical main:** `d8cbaaacd8c5142ea4fe9b1afb949129334d02d8` (Iter203)  
**RQIR Core:** v1.0 FROZEN.

## Auto-research reconciliation

Before Iter204, KMQGB auto-research was checked again. Its last run was still 2026-09-10T11:21:11Z and had not created a competing post-Iter203 front. Canonical Iter203 passed post-merge methodology-ci run `34473933838` and reproducibility-release run `34473982268`, both `success`.

## New scientific result

The pure/random-tensor material branch is not globally terminal, but two explicitly solved continuum universality sectors receive scoped terminal FAILs under the frozen 3+1 semiclassical Lorentzian gravity requirement.

### Standard melonic sector

Gurau–Ryan prove that the melonic continuum is precisely branched-polymer universality, with `d_H=2` and `d_S=4/3`.

Frozen scoped result:

`FAIL_RQIR_GATE__PURE_RANDOM_TENSOR_STANDARD_MELONIC_CONTINUUM_IS_BRANCHED_POLYMER_NOT_3P1_LORENTZIAN_GRAVITY`.

### Solved enhanced nonmelonic sectors

Published enhanced tensor models contain branched-polymer and planar/two-dimensional quantum-gravity phases and transitions between them; the rank-3/rank-4 multicritical survey through order six finds this BP/planar structure broadly in the studied class.

Frozen scoped result:

`FAIL_RQIR_GATE__PURE_RANDOM_TENSOR_SOLVED_ENHANCED_BP_OR_PLANAR_CONTINUA_ARE_NOT_3P1_LORENTZIAN_GRAVITY`.

### Why the umbrella branch remains BLOCKED

The solved BP/planar sectors do not exhaust the space of pure tensor interactions. Background-independent rank-4 tensor-model RG literature contains candidate interacting fixed points, including a fixed point with two relevant directions, whose physical continuum interpretation remains unresolved. Higher-order/nonmelonic sectors also prevent extrapolation of the solved universality classes into a complete no-go.

Therefore:

`PARTIAL_BRANCH_DISPOSITION__PURE_RANDOM_TENSOR_STANDARD_MELONIC_AND_SOLVED_BP_PLANAR_ENHANCED_CONTINUA_FAIL_3P1_GRAVITY__UNRESOLVED_NONMELONIC_RG_SPACE_BLOCKED`.

The remaining pure-tensor gate is:

`PURE_RANDOM_TENSOR_NONMELONIC_RG_FIXED_POINT_TO_3P1_SEMICLASSICAL_GEOMETRY_AND_NORMALIZED_GRAVITY_OBSERVABLE_CERTIFICATE`.

## Global status

No family/global promotion:

- Tier-1: `1/14` terminal, `13/14` nonterminal;
- comparator-ready scoped gravity residual/control rows remain `10`;
- D2: NOT_CLOSED;
- D4: NOT_CLOSED;
- D7: NOT_CLOSED;
- Paper IV: `NOT_YET_AUTHORIZED`;
- Candidate Gravity R3: `24%`, inactive;
- heavy compute: IDLE.

The two new scoped FAILs are continuum-universality incompatibilities, not normalized comparator residual rows, so the comparator-ready residual count is not increased.

## Authorities added

- `paper_iv/O_PURE_RANDOM_TENSOR_CONTINUUM_UNIVERSALITY_AUDIT_2026-09-10.md`
- `paper_iv/PURE_RANDOM_TENSOR_BRANCH_LEDGER_ITER204.json`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_204.json`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_204.json`

## Next operation

1. synchronize `recovery/state.json` and `CURRENT_BENCHMARK_FRONT.md`;
2. exact-head CI validate Iter204;
3. recheck KMQGB auto-research before merge;
4. if integrated, decide whether the unresolved nonmelonic/RG candidate pure-tensor remainder is literature-terminal BLOCKED or whether a concrete same-realization RG->continuum-geometry observable certificate can be constructed from existing primary work;
5. if not, park pure tensors and move to the next GFT/TGFT material branch or another Tier-1 family.