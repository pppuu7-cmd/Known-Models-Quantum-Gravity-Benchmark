# Recovery Delta — Iter273

Date: 2026-09-11
Research lane: Paper IV / ecological D7 campaign
Active stage: `D7-S2 STRICT_TIER1_TERMINAL_COVERAGE`

## Trigger

A material peer-reviewed LQG authority omitted from the Iter258 freshness audit was identified during the D7 external-authority reopen watch:

Muxin Han, *Ultraviolet fixed point in covariant loop quantum gravity*, Physical Review D 114, 044040 (2026), published 2026-08-12, DOI `10.1103/d8s7-jqfl`, arXiv:`2602.18665`.

## New scientific result

The authority provides a four-dimensional Lorentzian covariant LQG construction in which EPRL/KKL spinfoam amplitudes are summed over families of 2-complexes and a candidate small-spin UV fixed point / fundamental continuum limit is identified.

Scoped result:

`PASS_SCOPED_CONTINUUM_CONSTRUCTION__LORENTZIAN_EPRL_KKL_SUM_OVER_2_COMPLEXES_HAS_A_CANDIDATE_UV_FIXED_POINT_AND_FUNDAMENTAL_CONTINUUM_LIMIT`

The result is important positive LQG evidence but is not promoted to family sufficiency. At the identified UV fixed point the leading bulk theory is topological, while a terminal Paper-IV realization still requires a same-realization physical UV-to-IR/GR bridge, parameter/refinement identity, normalized gravity observable, common comparator and propagated error certificate.

Refined family blocker:

`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

## Governance state after Iter273

- RQIR Core v1.0: `FROZEN`.
- Operational polygon readiness: `100%`.
- D7 protocol infrastructure readiness: `100%`.
- D7-S0: `PASS`.
- D7-S1: `PASS`.
- D7-S2: `NOT_CLOSED`.
- Tier-1 strict terminal: `1/14`.
- Tier-1 strict nonterminal: `13/14`.
- D7-S3: `NOT_CLOSED`.
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5: `NOT_AUTHORIZED`.
- D7-S6: `INACTIVE`.
- Candidate Gravity R3: `24%`.
- Heavy compute: `IDLE`.
- `NEW_REQUIRED`: not authorized.

## Authorities / repository objects

- `paper_iv/P_LQG_COMPLETE_SPINFOAM_UV_FIXED_POINT_REOPEN_AUDIT_ITER273_2026-09-11.md`
- audit commit: `bdd17c68644226a46aa2c8ac3c41a75edba078d5`
- `paper_iv/PAPER_IV_D7_READINESS_STATE.json` updated for Iter273 without terminal-count promotion.
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_273.json`

## Recovery rule

Do not rerun the Iter273 LQG literature branch unless new authority satisfies the explicit reopen condition. Do not splice the new small-spin summed-complex UV fixed-point object to prior large-spin EPRL->Regge/GR ancestry as one terminal same-realization trajectory without an explicit parameter/refinement/observable bridge.

## Exact next gate

`D7_S2_NEXT_EXTERNAL_AUTHORITY_REOPEN__SEARCH_FOR_A_NEW_OBJECT_CAPABLE_OF_FAMILY_LEVEL_TERMINALIZATION_OR_VALID_REDUCTION`

Prefer a different parked Tier-1 family with a finite blocker. Asymptotic Safety remains a high-information watch target because a September 2026 ERG conference report describes Lorentzian contact-term progress, but it must not be promoted until a public reproducible contact-complete authority exists.
