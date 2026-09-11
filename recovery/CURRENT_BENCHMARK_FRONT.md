# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter273 scoped LQG external-authority reopen
Authoritative prior validated D7 infrastructure milestone: Iter272
Authoritative operational-saturation milestone: Iter270

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census remains 14 families: strict terminal 1/14, nonterminal 13/14.
- Tier-2 unresolved = 0.
- D1 = PASS.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3 = PARTIAL.
- D4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D5 = PASS.
- D6 = PASS_RULE_TARGETS_OPEN.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- D7-S0 = PASS.
- D7-S1 = PASS.
- D7-S2 = NOT_CLOSED.
- D7-S3 = NOT_CLOSED.
- D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D7-S5 = NOT_AUTHORIZED.
- D7-S6 = INACTIVE.
- Paper IV global decision = NOT_YET_AUTHORIZED.
- NEW_REQUIRED is not authorized.
- Candidate Gravity remains inactive at canonical R3 = 24%.
- Heavy compute = IDLE.

## Operational polygon status
Iter270 established:
- `OPERATIONAL_POLYGON_READINESS = 100%`
- `INTERNALLY_ACTIONABLE_UNRESOLVED_FRONTS = 0`

Iter272 established and validated D7 protocol infrastructure at 100%. Neither metric is scientific D7 closure.

## Iter273 external-authority reopen — LQG/spinfoam

A peer-reviewed authority omitted from the Iter258 freshness ledger was identified:

Muxin Han, *Ultraviolet fixed point in covariant loop quantum gravity*, Physical Review D 114, 044040 (2026), published 2026-08-12, DOI `10.1103/d8s7-jqfl`, arXiv:`2602.18665`.

The work supplies a materially new scoped object: a complete Lorentzian EPRL/KKL spinfoam amplitude organized as a sum over 2-complex families with a candidate small-spin UV fixed point and fundamental continuum-limit construction.

Scoped result:

`PASS_SCOPED_CONTINUUM_CONSTRUCTION__LORENTZIAN_EPRL_KKL_SUM_OVER_2_COMPLEXES_HAS_A_CANDIDATE_UV_FIXED_POINT_AND_FUNDAMENTAL_CONTINUUM_LIMIT`

This does **not** terminalize `LQG_SPINFOAM`. At the identified fixed point the leading bulk dynamics is topological, and the frozen Paper-IV target still lacks one explicit same-realization physical UV-to-IR/GR trajectory with parameter/refinement identity, normalized gravity observable, common comparator and propagated error certificate.

Refined blocker:

`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

Therefore strict Tier-1 coverage remains `1/14`, not `2/14`. BLOCKED is not FAIL and no NEW_REQUIRED inference is authorized.

## Iter273 provenance
- `paper_iv/P_LQG_COMPLETE_SPINFOAM_UV_FIXED_POINT_REOPEN_AUDIT_ITER273_2026-09-11.md`
- initial audit commit: `bdd17c68644226a46aa2c8ac3c41a75edba078d5`
- `paper_iv/PAPER_IV_D7_READINESS_STATE.json` — Iter273 state, terminal count unchanged.
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_273.json`
- `recovery/RECOVERY_DELTA_273.md`

## Validation
Prior D7 infrastructure is validated by Iter272 methodology-ci run `34545563636` = success.
Iter273 validation must be read from the methodology-ci run attached to the final Iter273 synchronization head; do not treat a queued/in-progress run as success.

## Exact next gate
`D7_S2_NEXT_EXTERNAL_AUTHORITY_REOPEN__SEARCH_FOR_A_NEW_OBJECT_CAPABLE_OF_FAMILY_LEVEL_TERMINALIZATION_OR_VALID_REDUCTION`

Priority rule: use genuinely new external authority with potential to change a strict family classification. Do not repeat saturated family scans merely to create activity. Asymptotic Safety remains a high-information watch target because September-2026 conference material reports Lorentzian contact-term progress, but conference-only progress cannot be promoted to terminal authority without a public reproducible contact-complete package.
