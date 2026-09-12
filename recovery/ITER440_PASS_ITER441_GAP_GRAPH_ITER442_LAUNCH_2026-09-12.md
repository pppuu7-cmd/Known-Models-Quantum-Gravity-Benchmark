# KMQGB recovery delta — Iter440 PASS, Iter441 gap graph, Iter442 launch

Date: 2026-09-12

## Iter440 — repaired Toller recombination run consumed

- Workflow run: `34715459544`
- Head commit: `9dc61a1b6cf7cae6336b31b2e0d5068abadfec49`
- Conclusion: `success`
- Summary artifact: `lqg-iter440-summary`, artifact id `10305195265`
- Frozen lanes: `32/32` valid, `0` invalid.
- Classification: `SOURCE_TOLLER_RECOMBINATION_IDENTITY_REALIZED_ON_FROZEN_GRID`.
- Maximum scaled cross-precision difference: `1.7000150803904542e-77`.
- Maximum scaled recombination residual at 120 dps: `1.0208104944632994e-117`.
- Maximum scaled recombination residual at 80 dps: `1.700013070447523e-77`.

Interpretation: the first-run Iter440 failure was numerical-context-only. The repaired frozen Eq.(45)/(46) matrix validates the source-level finite-beta Toller/Wigner recombination on the preregistered gamma-simple grid. Scope remains source-level: this does **not** prove full K5 Haar/angular causal-vertex finiteness, cutoff removal, terminal family coverage, or D7 closure.

Frozen status remains:
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S2: `NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`
- Candidate Gravity: inactive / not authorized.

## Iter441 — parallel D7-S3/S4 gap-graph diagnostic

Research branch: `research/iter441-d7-s3-s4-gap-graph`
Workflow run: `34716237959`
Conclusion: all three prerequisite jobs plus aggregate `success`.
Summary artifact: `iter441-summary`, artifact id `10304848713`.

Observed nonterminal gap graph:
- S3 PRESENT: `0`
- S3 UNRESOLVED: `4`
- S4 PRESENT: `1`
- S4 UNRESOLVED: `3`
- terminal D7: `NOT_AUTHORIZED`
- Candidate Gravity activation: `false`

Exact K5 conditional-domain witness:
- vertices: `5`
- edges: `10`
- GF(2) incidence rank: `4`
- kernel dimension: `1`
- global-flip kernel size: `2`
- vertex assignments: `32`
- unique wedge signatures modulo global flip: `16`
- all single-edge removals connected: `true`
- all two-edge removals connected: `true`

Interpretation: do not rerun already-present conditional common-domain witnesses. The minimal useful S3/S4 targets are the unresolved transport / normalized-comparator / causal-stack realization / universal-domain-cutoff-normalization capability nodes. Absence of evidence remains `UNRESOLVED`, never scientific `FAIL`.

## Iter442 — source spectral Feynman-i-epsilon / Toller-pole gate launched

Research branch: `research/iter442-toller-spectral-projector`
Workflow run: `34716591952`
Frozen scientific contract: `benchmarks/lqg_iter442_toller_spectral_projector_contract.json`
Implementation: `code/lqg_iter442_toller_spectral_projector.py`

Purpose: extend the old j=1/2 spectral-epsilon special-case checks to the source-faithful gamma-simple matrix used by Iter439-440:
- gamma: `{7,8}`
- j: `{2,5}`
- all integer m in `[-j,j]`
- beta: `{0.5,2,8}`
- epsilon: `{1e-2,1e-4,1e-6,1e-8}`
- Toller-pole approach deltas: `{1e-8,1e-10,1e-12}`
- precision: `140 dps`

Source-backed convention: the Feynman epsilon acts in spectral `rho-tilde`, never as `beta+i*epsilon`. The gate checks Eq.(16) kernel normalization, exact Feynman/Toller pole separation, residue convergence to each Toller branch, and Cauchy-stable cancellation of all published Toller poles on every frozen lane.

Frozen pass thresholds:
- final residue scaled error <= `1e-6`
- residue error monotone over the epsilon grid
- last-pair projected-pole scaled difference <= `1e-6`
- minimum Feynman/Toller pole distance >= `10`

A PASS may strengthen D7-S2 but must leave it nonterminal. It cannot authorize D7-S5 or Candidate Gravity.

## Next gates

1. Consume Iter442 without changing frozen thresholds.
2. If Iter442 passes, stop spending cycles on source-level spectral pole cancellation and move to the genuinely harder full causal-vertex / Haar-angular integrability or source-backed normalized causal-vertex object.
3. In parallel attack the four S3 unresolved capability nodes and three remaining S4 unresolved nodes identified by Iter441.
4. Keep terminal D7 classifier and Candidate Gravity activation locked until D7-S2/S3/S4 are actually closed under the global decision contract.
