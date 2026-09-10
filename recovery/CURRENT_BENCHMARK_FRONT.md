# Current Benchmark Front
Updated: 2026-09-10
Iteration: Iter250
Authoritative commit: this Iter250 commit once exact-head validation is green

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census remains 14 families: terminal 1/14, nonterminal 13/14.
- Tier-2 unresolved = 0.
- D2 = NOT_CLOSED.
- D4 = PARTIAL / globally NOT_CLOSED.
- D7 = NOT_CLOSED; decision = NOT_YET_AUTHORIZED.
- Candidate Gravity remains inactive at R3 = 24%.

## Exact-head validation
- Iter249 methodology CI is SUCCESS: workflow run 34517986952.
- Iter249 reproducibility release is SUCCESS: workflow run 34518055179; artifact `kmqgb-reproducibility-bundle` / 10167744246; SHA-256 `4c9c6b8a49f1539e9beca60b597841fab66685df991627065d198947e82dea20`.
- Iter250 requires its own exact-head methodology and reproducibility validation after this commit.

## Iter250 scientific result
- Re-audited the materially distinct Riemann/Weyl weakly-nonlocal causality branch.
- Zhao, Modesto & Bambi (EPJC 86, 713, 2026; arXiv:2605.01413) prove that a special but large class of nonlocal form factors admits an exact vacuum subclass of Gödel-type solutions with closed timelike curves.
- Scoped disposition: `FAIL_SCOPED_CAUSALITY_GATE__WEAKLY_NONLOCAL_RIEMANN_RICCI_WEYL_FORM_FACTOR_SUBCLASS_ADMITS_EXACT_GODEL_TYPE_VACUA_WITH_CLOSED_TIMELIKE_CURVES`.
- This is not promoted to family-level FAIL: the paper itself limits the result to a special though large class of form factors.
- Renormalizability/unitarity-motivated UV structure cannot be used as a surrogate for global causality in that subclass.
- A surviving branch must now demonstrate a fixed-action causality-safe restriction or matter/deformation mechanism that lifts the vacuum degeneracy, plus full-momentum physical observable, comparator and propagated error in the same realization.

## Family consequence
`NONLOCAL_QG` remains `PARTIAL_SUBFAMILY_ONLY` with family residual `UNDEFINED`. No family terminal promotion and no `NEW_REQUIRED` authorization.

## Running / compute
Heavy compute remains IDLE; blocker is structural/provenance/realization matching.

## Exact next gate
`NONLOCAL_QG_RIEMANN_WEYL_RICCI_FLAT_OR_GODEL_DEGENERACY_EVASION_AND_MATTER_COUPLED_CAUSAL_COMPLETION_CERTIFICATE`
