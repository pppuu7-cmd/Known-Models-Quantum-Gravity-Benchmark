# Iter440 numerical-repair front/ledger delta — 2026-09-12

## Scope locks retained

RQIR Core v1.0 remains frozen. Candidate Gravity remains inactive. D7 remains `NOT_CLOSED / NOT_YET_AUTHORIZED`; no `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED` label is authorized while D7-S2/S3/S4 remain open.

Canonical statuses are unchanged:
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S2: `NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`

## Iter440 first production run — NUMERICAL/IMPLEMENTATION FAIL only

Frozen scientific contract remains the preregistration in `recovery/ITER439_RESULT_AND_ITER440_PREREG_TOLLER_RECOMBINATION_2026-09-12.md`: source-faithful Eq. (45)/(46), `t^(+)+t^(-)=d`, gamma `{7,8}`, j `{2,5}`, all integer m, beta `{0.5,1,2,4,8}`, 80/120 dps, cross-precision threshold `1e-35`, recombination residual threshold `1e-30`, and no artificial `beta+i*epsilon`.

Original launch commit: `e7b675c21c39589bea6ba8c61312e52980980e88`.
Original run: `34712981480`.
Run conclusion: workflow failure.
Summary artifact: `lqg-iter440-summary`, artifact id `10304338541`, digest `sha256:76014ab8eda12c19272f1c5edbb825fea753915e73f5c44eff22f05730229eb7`.
Representative failed matrix job inspected: `103605003936`.

The terminal evidence is NOT a scientific recombination failure. The first causal failure is numerical implementation precision context:

1. `eval_source(..., dps)` evaluated `d`, `t_plus`, and `t_minus` inside `mp.workdps(80/120)` and returned high-precision values.
2. After return, `mpmath` restored ambient/default precision.
3. `identity_residual()` and cross-precision arithmetic were then evaluated outside a high-precision context.
4. This rounded the recombination operation itself to roughly machine/default-mpmath precision and produced a spurious residual of order `3.9e-18`, despite stable 80/120-digit branch evaluations.
5. Re-evaluating the same frozen source expressions and the residual arithmetic inside the high-precision context gives residuals of order `1e-81` on the inspected lane, consistent with the exact source identity rather than a physical/source-formula contradiction.

Scientific classification of run `34712981480`:

`NUMERICAL_IMPLEMENTATION_PRECISION_CONTEXT_FAIL__NO_SCIENTIFIC_ITER440_CLASSIFICATION`

No threshold, source equation, matrix point, physical object, or interpretation rule was changed.

## Minimal repair and authoritative rerun

Repair commit: `9dc61a1b6cf7cae6336b31b2e0d5068abadfec49`.

Repair: only the finite/cross-precision/recombination-residual arithmetic is now executed inside an explicit high-precision context (`TIGHT_DPS + 20`). The frozen 80/120-digit source evaluations and every preregistered threshold remain unchanged.

Authoritative repaired Iter440 run: `34715459544` (`lqg-iter440-toller-recombination`, run number 2), head `9dc61a1b6cf7cae6336b31b2e0d5068abadfec49`.
At this delta write the 32-lane scientific matrix is queued; scientific classification remains OPEN until the full repaired aggregate is terminal and consumed.

## Readiness effect

No readiness increase is credited for repairing a numerical implementation defect. Working research metric remains:

`D2 82% -> D4 68% -> D7 52% -> overall 65%`.

## Next permitted gate

First consume and classify repaired run `34715459544` against the unchanged preregistered Iter440 contract.

- If repaired Iter440 terminally passes: preregister, before implementation, the source-faithful projected Feynman-i-epsilon / collision-integrability diagnostic using validated `t^(+)`, `t^(-)`, and `d`, preserving exact invariant-projector controls and never replacing the published spectral prescription by an artificial `beta+i*epsilon` shift.
- If repaired Iter440 remains invalid: diagnose the first remaining source-formula/numerical-convention failure. Do not infer causal-vertex divergence/finiteness and do not proceed to the dependent collision gate.
