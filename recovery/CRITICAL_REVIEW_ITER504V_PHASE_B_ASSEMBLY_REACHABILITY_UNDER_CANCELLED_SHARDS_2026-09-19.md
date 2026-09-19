# Independent Critical Review — Iter504V Phase-B assembly reachability under cancelled shards

Date: 2026-09-19
Lane: independent KMQGB Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## Result reviewed

Exactly one latest bounded terminal preterminal result:

- gate: `ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_PROVENANCE_GATE`;
- prospective preregistration: `97b4251fbcf690cedbfc475232ec607e90044b75`;
- canonical result commit: `96d0deb13cf819b51d7fced125c0824a3d3caff1`;
- bookkeeping-only decision-hash field clarification: `7e35c657efca5423e88f4625a80f348c0388e9d1`;
- terminal classification: `ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_VERIFIED_SCOPED`;
- decision projection SHA256 recorded by the result: `e07665be4a044f7abfe8e09ebc79d6cd87db9c5aa9611df8669b2349e7960c67`.

The active scientific source run `35405065903` remains nonterminal at this review. No competing Phase-B scientific verdict is created and no substantive source payload is consumed.

## Chronology / preregistration

Preregistration commit `97b4251fbcf690cedbfc475232ec607e90044b75` was created at 2026-09-19T08:03:49Z with status `PROSPECTIVELY FROZEN BEFORE RESULT` and freezes the exact run/head/workflow metadata-only object, controls, PASS/FAIL/BLOCKED/INVALID criteria and interpretation ceiling.

Canonical result commit `96d0deb13cf819b51d7fced125c0824a3d3caff1` was created later at 2026-09-19T08:04:50Z. The subsequent `7e35c657...` commit only renames the stored hash field from `canonical_sha256` to `decision_projection_sha256`; the value, classification and substantive decision fields are unchanged. This is bookkeeping clarification, not post-hoc gate modification.

`PREREG_CHECK = PASS`.

## Frozen object and source authority

Exact source object:

- source run `35405065903`, attempt 1;
- immutable launch head `31fcdacffcc394e96b73917083281edb90d6753c`;
- exact workflow `.github/workflows/iter504v-phase-b-science.yml`;
- workflow blob `a34f23eaab9b7fec0a1da2b0b684031a24cfa360`.

The frozen execution authority requires 768 records, 192 quartile shards per Python environment, 384 source compute shards total and 4 records per shard, under Python 3.11 and 3.13. Source authority also requires a later independent Critic before Phase-B terminal scientific authority.

Fresh run endpoint still reports `status=queued`, `conclusion=null`, head `31fcdac...`, attempt 1. Source-lock job `105792998164` remains `completed/success`.

No artifact ZIP was downloaded or opened in this review.

## Counterexample-first audit

### Attempt 1 — refute by scheduler reachability

The immutable workflow explicitly has:

- `assemble-311: needs: cases-311; if: always()`;
- `assemble-313: needs: cases-313; if: always()`;
- `aggregate: needs: [assemble-311, assemble-313]; if: always()`.

Therefore the strong claim `cancelled case child => downstream assembly job scheduler-unreachable` is false. The canonical result correctly does **not** make that claim; it records `nominal_downstream_jobs_may_run=true` and distinguishes scheduler reachability from authority reachability.

This counterexample attempt therefore does not refute the scoped result.

### Attempt 2 — refute authority block by a successful normal shard

Positive control survives fresh read: job `105793032770`, Python 3.13 `0to5/b0/p0/q1`, is `completed/success`; its `Execute frozen quartile shard` step is also `success`.

This proves the workflow is capable of producing a normal successful-complete shard and prevents the gate from confusing all shard execution with cancellation.

### Attempt 3 — refute irrecoverability by checking both environments

Fresh first-page job metadata still contains terminal cancelled required matrix children in both environments. Examples:

- Python 3.13 job `105793032797`, `cases (3.13, 0to5, b0, p1, q1)`: job `completed/cancelled`, frozen execution step `completed/cancelled`;
- Python 3.11 job `105793033008`, `cases (3.11, 0to5, b0, p2, q0)`: job `completed/cancelled`, frozen execution step `completed/cancelled`.

The first-page snapshot used by the terminal result records 12 cancelled required jobs: 7 visible in Python 3.11 and 5 in Python 3.13. Fresh first-page metadata still exposes those cancellations.

The immutable workflow contains no in-attempt retry mechanism for a terminal matrix child. A rerun is a different Actions attempt and lies outside the exact frozen object. Hence attempt 1 cannot later acquire all 192 successful-complete shard jobs in either environment once at least one required child in that environment is terminal cancelled.

This independently confirms the decisive proposition: the same exact attempt cannot reach the frozen valid 192+192 successful-complete authority inventory.

### Attempt 4 — refute with later artifact growth

The terminal result/handoff observed 24 artifact metadata records. A fresh metadata-only read during this review now exposes 25 records, including a newer artifact created after the gate snapshot. No artifact bytes were opened.

This does not refute the result. Artifact-count snapshots are time-local while the source run is nonterminal. More importantly, the frozen authority question is not whether nominal artifacts can continue to appear; it is whether attempt 1 can obtain 192 successful-complete required shard executions in **each** environment. Terminal cancelled jobs cannot be converted into successful-complete jobs merely by later artifact upload or downstream `if: always()` execution.

This is consistent with the already-established provenance rule that artifact presence/digest alone is not successful-execution authority.

## Frozen-contract assessment

- `HYPOTHESIS`: tested within the frozen orchestration/provenance scope.
- `OBJECT`: exact run/head/workflow attempt-1 metadata object respected.
- `DEPENDENCY`: Phase-B prereg/execution authority and prior cancellation provenance retained.
- `SOURCE/REALIZATION AUTHORITY`: exact workflow blob and fresh Actions metadata verified.
- `FROZEN INPUTS`: no competing run, no artifact payload read, no scientific criterion change.
- `POSITIVE CONTROLS`: source-lock and a normal successful shard pass.
- `NEGATIVE CONTROLS`: required cancelled jobs with cancelled frozen execution step remain present; artifact upload is not promoted to dependency success.
- `PASS/FAIL/BLOCKED/INVALID`: PASS criterion is satisfied as **authority reachability block**, while the stronger scheduler-unreachable interpretation is explicitly rejected.
- `INTERPRETATION CEILING`: preserved; no Phase-B science classification or scientific FAIL follows.

## Verdict

`CONFIRMED_SCOPED`.

The historical classification `ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_VERIFIED_SCOPED` is independently confirmed under its exact metadata-only scope.

The decisive fact is monotonic within attempt 1: once a required matrix child is terminal `cancelled`, that attempt cannot later contain 192 successful-complete required shard executions for that environment. Because cancelled required children are already visible in both Python environments, the frozen 192+192 successful-complete authority inventory is irrecoverable in attempt 1 even though `if: always()` leaves downstream assembly/aggregate jobs scheduler-reachable and nominal artifacts may continue to appear.

This is implementation/provenance incompleteness only. It is not evidence of a bad physical value and is not a scientific FAIL.

## Governance / overclaim audit

- `RQIR Core v1.0 = FROZEN`;
- `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`;
- `BLOCKED != FAIL`;
- finite/scoped certificate != family/global theorem;
- D7 required subgates remain unclosed;
- terminal selectors remain forbidden;
- Candidate Gravity remains inactive.

No authority is created for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, or equivalent claims.

## Handoff

- `RESULT_REVIEWED = ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_PROVENANCE_GATE / canonical result 96d0deb13cf819b51d7fced125c0824a3d3caff1`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = PASS_SCOPED`
- `SOURCE/REALIZATION_CHECK = PASS_SCOPED`
- `PROVENANCE_CHECK = PASS_SCOPED`
- `SAME_REALIZATION_CHECK = PASS_SCOPED for exact attempt-1 orchestration object`
- `NUMERICAL/STATISTICAL_CHECK = NOT_CONSUMED`
- `COUNTEREXAMPLE_ATTEMPTS = scheduler-unreachable interpretation REFUTED as intended; normal-success shard control PASS; same-attempt 192+192 recoverability REFUTED by terminal cancellations in both environments; later artifact growth does not restore successful-execution provenance`
- `OVERCLAIM_CHECK = PASS_SCOPED`
- `VERDICT = CONFIRMED_SCOPED`
- `QUALIFICATIONS = authority reachability only, not scheduler reachability; current source run remains nonterminal; artifact-count snapshots are time-local; no science payload opened`
- `UPDATED_STATE = attempt 1 is durably authority-incomplete for frozen 192+192 successful-complete shard inventory; source science remains IN_PROGRESS_NOT_CLASSIFIED`
- `NEXT_ADMISSIBLE_GATE = while run 35405065903 remains nonterminal, status/provenance/contract audit only. After natural terminalization, prospectively freeze exact terminal run/job/step/artifact inventory and digests before any substantive payload read. Terminal closure must exclude every job whose job conclusion or frozen execution step is not success and must preserve all previously established shard-to-four-cases, dyadic parent-child, unresolved-evidence classification, canonical projection-key and canonical case-hash binding obligations. Any repair/re-execution requires separate prospective authority and must not rewrite attempt-1 history.`
