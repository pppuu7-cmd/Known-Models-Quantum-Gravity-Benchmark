# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter256
Authoritative commit: Iter256 head once exact-head validation is green

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census remains 14 families: terminal 1/14, nonterminal 13/14 under the strict coverage contract.
- Tier-2 unresolved = 0.
- D2 = NOT_CLOSED.
- D4 = PARTIAL / globally NOT_CLOSED.
- D7 = NOT_CLOSED; decision = NOT_YET_AUTHORIZED.
- Candidate Gravity remains inactive at canonical R3 = 24%.
- Papers I–III remain FROZEN/CLOSED.

## Exact-head validation
- Iter255 methodology/reproducibility validation completed green on head `47f1677b72199ebe6312c70619ff91415ee763f5`; reproducibility-release run `34534245994` completed SUCCESS.
- Iter256 requires exact-head methodology/reproducibility validation after commit.

## Iter256 scientific result — CFS
Fresh 2026 authority materially strengthens the same-realization gravity ancestry for Causal Fermion Systems. The causal action principle yields Einstein equations with an energy-momentum tensor organized as a power expansion in the regularization length; the gravitational coupling is the square of that length; and the construction provides a systematic procedure for higher-order corrections.

Scoped PASS:
`PASS_STRUCTURAL_GATE__CFS_CAUSAL_ACTION_TO_EINSTEIN_EQUATION_POWER_EXPANSION_WITH_REGULARIZATION_LENGTH_ANCESTRY_EXISTS`.

This does not yet provide the frozen beyond-GR object required by RQIR: one explicit first non-Einstein correction tensor with coefficients fixed by a declared microscopic regularization/state, plus normalized observable, identical-domain GR/EFT comparator and propagated uncertainty.

Remaining blocker:
`BLOCKED_MISSING_REQUIRED_OBJECT__CFS_EXPLICIT_NORMALIZED_FIRST_NON_EINSTEIN_CORRECTION_TENSOR_WITH_FIXED_MICROSCOPIC_REGULARIZATION_STATE_COMPARATOR_AND_PROPAGATED_ERROR`.

CFS remains `BLOCKED_MISSING_REQUIRED_OBJECT`; family residual remains `UNDEFINED`. No family FAIL and no NEW_REQUIRED authorization.

## Operational progress
- NONLOCAL_QG remains parked pending new object authority from Iter255.
- CFS blocker has been narrowed from generic beyond-continuum gravity observable absence to a specific correction-tensor/normalization/provenance/error capsule.
- Heavy compute remains IDLE because the active blocker is analytic/provenance limited.

## Exact provenance
- Finster & Krpoun, `A Geometric Derivation of the Einstein Equations from the Causal Action Principle`, arXiv:2607.13871, submitted 2026-07-15.
- `post_freeze_paper_iv_wave_01/PF1_01_CFS/result.json`.

## Exact next gate
`CFS_FIRST_NON_EINSTEIN_GRAVITY_CORRECTION_TENSOR_COEFFICIENT_EXTRACTION_AND_NORMALIZED_OBSERVABLE_CERTIFICATE`
