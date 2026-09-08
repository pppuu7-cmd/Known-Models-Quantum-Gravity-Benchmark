# KMQGB Fifteenth Wave — Machine-Readable Candidate Gravity Pipeline

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–14:** terminal and immutable.  
**Purpose:** make future Candidate Gravity construction/restoration executable and fail-closed rather than dependent on prose or chat memory.

## Terminal matrix

1. **T15-01 — candidate-record contract** — `PASS_RQIR_GATE`.
   - Canonical contract: `schema/KG_CANDIDATE_RECORD_v1.json`.
   - Binds parent authority, parameter sharing, observable blocks, comparator registry, covariance, attribution, rigidity and G0–G10 promotion state.

2. **T15-02 — fail-closed validator** — `PASS_RQIR_GATE`.
   - Reference: `code/kg_candidate_record_validator.py`.
   - Missing mandatory evidence blocks promotion.
   - A scientifically `BLOCKED` record remains structurally valid.
   - Internal contradictions, such as `G1=PASS` with incomplete response, are invalid.

3. **T15-03 — valid-blocked versus invalid-state distinction** — `PASS_RQIR_GATE`.
   - `BLOCKED` is a legitimate scientific state, not zero and not malformed data.
   - `FAIL` is reserved for a computed failed criterion.
   - Illegal promotion/Fisher/resource states are rejected.

4. **T15-04 — prospective role/version/provenance contract** — `PASS_RQIR_GATE`.
   - Parent/comparator/test-suite/split changes that can alter the quotient require a new version/iteration.
   - Training/holdout/null/anchor roles are prospective and may not be silently rewritten after residual inspection.

5. **T15-05 — automation boundary / downstream authorization** — `PASS_RQIR_GATE`.
   - Automation may check completeness, shapes, sharing consistency, COR/rigidity calculations and gate consistency.
   - It may not infer missing physical theorems or convert unknown terms to zero.
   - Fisher/resources remain forbidden without an independently recorded robust global comparator-subtracted residual.

**Wave-15 terminal coverage: 5/5 = 100%.**

## Canonical files

- `protocol/MACHINE_READABLE_KG_PIPELINE.md`
- `schema/KG_CANDIDATE_RECORD_v1.json`
- `schema/KG_CANDIDATE_RECORD_PREANSATZ_EXAMPLE.json`
- `code/kg_candidate_record_validator.py`

## Critical validator correction

The executable layer was corrected so that

`scientifically BLOCKED != structurally invalid`.

An incomplete observable block is allowed as a valid record when `G1` is also non-PASS.  The record becomes invalid only if it simultaneously claims a contradictory PASS/promotion state.

## Candidate Gravity consequence

A future candidate must be reconstructible from its machine record plus referenced artifacts.  The record is not a theory and does not promote an ansatz; it is the reproducibility and fail-closed control layer through which every prospective ansatz must pass.
