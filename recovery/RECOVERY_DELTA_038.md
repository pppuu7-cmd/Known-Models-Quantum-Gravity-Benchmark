# RECOVERY_DELTA_038 — Wave 15 terminal / fail-closed machine-readable KG pipeline

**Date:** 2026-09-08  
**KMQGB iteration:** 038  
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`  
**External RQIR:** read-only

## Terminal coverage

- Wave 1: `9/9 = 100%`, immutable.
- Waves 2–15: each `5/5 = 100%`, immutable.
- Wave 15 rollup: `5 PASS_RQIR_GATE`.
- Globally authorized robust unique-QG residuals: `0`.
- KMQGB-promoted Candidate Gravity ansatz: none.
- External Candidate Gravity readiness at latest directly observed RQIR authority: `24%`.

## Wave-15 authority

Canonical machine-readable objects:

- `protocol/MACHINE_READABLE_KG_PIPELINE.md`;
- `schema/KG_CANDIDATE_RECORD_v1.json`;
- `schema/KG_CANDIDATE_RECORD_PREANSATZ_EXAMPLE.json`;
- `code/kg_candidate_record_validator.py`;
- `fifteenth_wave/README.md`;
- `fifteenth_wave/result.json`.

## Critical validator correction

The first validator draft incorrectly treated every observable block with `completeness != PASS` as a malformed record.

This was corrected in commit `e2882283cb59bd87cccc21fa305b84e36011dcf3`.

Frozen rule:

`scientifically BLOCKED != structurally invalid`.

A BLOCKED/FAIL scientific block is allowed in a valid record. The record becomes invalid when it claims a contradictory downstream state, for example

- `G1=PASS` with an incomplete response block;
- `G0=PASS` without parent object/provenance/domain;
- `G3/G5=PASS` with no comparator registry;
- `G6=PASS` with no covariance object;
- ansatz promotion while any mandatory gate is not PASS;
- Fisher/resources promotion without a robust global comparator-subtracted residual;
- shared-parameter retuning on a prospective holdout without parent-model authority.

Missing required physics is never interpreted as zero.

## Validator self-check logic

The reference validator now distinguishes at least four cases:

1. pre-ansatz all-BLOCKED record -> structurally valid, promotion forbidden;
2. incomplete observable with `G1=BLOCKED` -> structurally valid, scientifically blocked;
3. the same incomplete observable with `G1=PASS` -> invalid methodology state;
4. illegal ansatz/Fisher/resources promotion -> invalid.

## Recovery synchronization

Updated:

- `recovery/CURRENT_BENCHMARK_FRONT.md` -> Iteration 038;
- `recovery/state.json` -> schema 4.1 / Iteration 038;
- `recovery/CANDIDATE_GRAVITY_RESEARCH_HANDOFF.md`;
- `recovery/RESTORE_FROM_NEW_CHAT.md`.

## External RQIR retained state

Latest directly observed scientific authority before this delta: RQIR Iteration `590`, `MODEL_READINESS=24%`.

Iter590 authority:

`d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G)`.

The local `K3` and ordered `K1^3` families have nonzero same-action support and cannot be silently omitted. External next gate remains hard-channel origin of local K3 and linked-cut/origin classification of K1^3 before complete nonlinear source Ward closure and comparator subtraction.

The KMQGB K3 analyticity note is only a read-only external cross-check and is not RQIR authority.

## Exact next front

Freeze a **prospective minimal DeltaGamma screening wave**. It must remain pre-ansatz.

For every exploratory template:

1. create a fail-closed machine record;
2. define exact parent/CTP representation and validity domain;
3. identify the first response order/configuration where the template differs from full matched C5;
4. try to absorb it into field redefinition, C5 EFT/loops/state freedom, C4/C6 mediator sectors or classical-CQ/nonlocal nuisance families;
5. enforce Ward/spin-2/locality/relational attribution;
6. use `BLOCKED` for missing theorems/objects;
7. terminate comparator-contained directions before any parameter optimization;
8. do not promote Candidate Gravity until a concrete joint residual passes the full promotion gate.
