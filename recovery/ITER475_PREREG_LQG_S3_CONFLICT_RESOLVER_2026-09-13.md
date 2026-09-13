# Iter475 preregistration — targeted LQG/EPRL D7-S3 conflict resolver

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION

## Question
Among the explicit LQG/EPRL causal-stack files flagged by Iter472, which positive/negative declarations actually refer to the same named realization and same required S3 map, and which apparent conflicts are merely cross-realization or cross-family lexical overlap?

## Frozen target set
Only tracked files whose paths/names explicitly identify LQG/EPRL causal-stack, UV/IR bridge, Wick bridge, physical-state link, stack UV entropy, gamma-duality observable/parameter bridge, or the corresponding Paper-IV decision-ledger deltas 283–303 are eligible. TGFT, DSI, IHO/DQFT and unrelated-family files are excluded.

## Frozen fields
Extract explicit boolean/key-value declarations containing: `same_realization`, `transport`, `normalized`, `comparator`, `error_certificate`, `missing_`, `causal_stack`, `physical_state`, `uv_ir`, `wick`, `gamma_duality`. Preserve file path, key, value and nearby text. Group only when both the realization tag and requirement class match explicitly; do not infer identity from similar vocabulary.

## Outcomes
For each S3 class: `CONSISTENT_POSITIVE_CANDIDATE`, `EXPLICIT_NEGATIVE`, `SAME_REALIZATION_CONFLICT`, or `INSUFFICIENT_IDENTITY_EVIDENCE`. D7-S3 may close no class from mention-only evidence. Any unresolved identity keeps that class open.

PASS label means the conflict-resolution audit completed reproducibly, not that S3 closed: `ITER475_LQG_S3_TARGETED_CONFLICT_MATRIX_COMPLETE_SCOPED`.

## Scope lock
No cross-family mixing. No absence-as-impossibility inference. No automatic override of newer negative authority by older positive local certificates. D7-S3 and D7-S5 remain fail-closed unless the exact required same-realization object/map/comparator/error bundle is positively certified.