# Current Benchmark Front

Updated: 2026-09-19

Fresh repository `main` and fresh GitHub Actions state always outrank this navigation snapshot.

## Active scientific front

Gate: `ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE`.
Execution gate: `ITER504V_PHASE_B_SOURCE_EXECUTION`.

Authority chain:
- Phase-A terminal `d03cae09c04638cb02412435a284cfd9acdf8406` -> `ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED` for the frozen 16-state sentinel only;
- Phase-B prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- static implementation Critic `eaa2d1ef84fe8370f33cec360233f60571f9bcd0 = PASS_SCOPED`;
- one-source execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- immutable source launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- authoritative source run `35405065903`, attempt 1.

Fresh post-gate state: source run remains nonterminal (`queued / conclusion=null`). Source-lock job `105792998164` remains `completed/success`. Latest validated first-page snapshot contains 30 jobs = 8 completed/success, 12 completed/cancelled, 8 in progress, 2 queued. Latest validated artifact metadata count is 20. Artifact ZIP bytes were not opened/downloaded and no case/leaf/slope/drift/certification/assembly/aggregate/counterexample scientific value was consumed.

Current scientific status remains `IN_PROGRESS_NOT_CLASSIFIED`.

Recovery reconciliation note: selected fields in `recovery/state.json` predate later cancellations/artifact growth. Durable override is `recovery/ITER504V_PHASE_B_TIMEOUT_CAUSALITY_STATE_DELTA_2026-09-19.json`; this front and fresh GitHub state outrank the older embedded snapshot until `state.json` is next consolidated.

## Latest terminal preterminal closure — case-job timeout causality

Gate: `ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_GATE`.

Prospective preregistration: `2fc02a80c7d4db6f05813cbb571eb01cb4fb7c53`.

Terminal classification:

`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED`.

Canonical result:
`research/results/ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_RESULT_2026-09-19.json`.

Terminal record:
`research/results/ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_TERMINAL_2026-09-19.md`.

Canonical result SHA256: `471a8369cbfdb763ef5193984fe0f60d058d183e6f5bd5fb19e61bcb1e822504`.

The immutable source workflow blob `a34f23eaab9b7fec0a1da2b0b684031a24cfa360` sets `timeout-minutes: 360` on both Python 3.11 and Python 3.13 case matrices and runs artifact upload under `if: always()`.

The first six visible cancelled case jobs selected by ascending job id before log inspection all terminated their frozen numerical step within four seconds of the exact 360-minute boundary, across both Python environments, with runner marker `The operation was canceled.` and successful post-cancellation artifact upload. A successful positive-control shard `105793032770` completed its numerical step in `272.992696` minutes, well before the same boundary.

Therefore the observed sampled cancellations are execution-timeout/provenance events, not scientific verdicts. Timeout-cancelled artifacts are incomplete implementation/provenance objects and cannot count as completed four-record shards even if GitHub assigned an artifact ID and SHA256 digest.

No artifact ZIP was opened and no source science was classified.

## Independently confirmed cancelled-job artifact provenance

Gate: `ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE`.

Prospective preregistration: `a0e28e3a96e109ee9ed440a267ee1407cddf2d55`.

Terminal classification:

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED`.

Independent Critical Review commit `171d8ee9b0945de095ed9f5cbc1f9296aa2007fc`: `CONFIRMED_SCOPED`.

Frozen decision SHA256: `6e2de425bc3b8cc83c75641c160e352061c2479b2f0564ce3b5b2eb3882f9e2f`.
Verified cancelled-job/artifact chain-list SHA256: `d0d7c9840e76300feeffe40eb09650eaf0a00f4ddd117c77ccfff5832a6b4dee`.

Outcome-independent metadata result: cancelled case jobs can have job conclusion `cancelled`, frozen `Execute frozen quartile shard` step conclusion `cancelled`, but `actions/upload-artifact` conclusion `success` and a matching non-expired SHA256-digested artifact metadata record bound to the exact source run/head. Therefore artifact presence/ID/digest alone is insufficient evidence of a completed valid shard.

This is a provenance/authority-path result only. It is not a scientific FAIL, does not classify Phase-B source science, and does not assert that any substantive case value is wrong.

## Superseded time-local metadata observation

Historical gate `ITER504V_PHASE_B_PRETERMINAL_SOURCE_STATUS_PROVENANCE_GATE` remains valid only for its frozen earlier observation and was independently reviewed by commit `1989e28d78fdddf2117c3b79b5f90af4bd752603 = CONFIRMED_SCOPED`. It must not be reused as current-source provenance authority because later Actions metadata contains cancelled source jobs and additional artifacts.

## Frozen Phase-B object

Complete q=1 domain: causals `0to5,1to4,2to3` x blocks `0..3` x signed paths `0..3` x amplitude boxes `0..15` = 768 canonical records.

Frozen contract retains rho `0.35,0.9,1.6,2.7`; R `6,8,10,12`; all 243 channels; 384-bit precision; deterministic dyadic midpoint partition; `MAX_DEPTH=3`; local validated `D(J)` recomputed at every visited node; exact leaf/per-rho and unresolved-depth binding.

Execution topology remains 192 deterministic quartile shards per Python environment, Python 3.11 and 3.13, 384 source compute shards total, `fail-fast:false`, `max-parallel:12`.

Frozen source taxonomy remains unchanged:
- PASS `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`;
- INCONCLUSIVE `ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED`;
- INVALID `ITER504V_BROADER_DOMAIN_INVALID` for implementation/provenance/cohort/channel/depth/partition/source/artifact/cross-environment invalidity.

There is no model-level/physics-level scientific FAIL label for this gate.

## Mandatory future terminal-Critic obligations

Existing independently verified source-assembler obligations:
1. bind every expected shard/artifact identity and `shard.json` to exactly its frozen four physical case records and prove exactly 192 unique complete shards per environment;
2. reconstruct every parent-inclusion child/parent dyadic edge and reject malformed/duplicate/orphan records.

Existing source-aggregate obligations:
3. rebind PASS/INCONCLUSIVE classification to independently recomputed unresolved evidence;
4. rebind `decision_projection_sha256_by_state` keys and projection sequence to the exact canonical 768-state identity;
5. rebind `case_file_sha256` keys/content hashes to the exact canonical 768-state identity.

Execution-provenance obligations:
6. before any shard artifact enters terminal authority, require exact binding to `job.conclusion == success` and frozen `Execute frozen quartile shard` step conclusion `success`; cancelled-execution artifacts must not count toward the required 192 complete shards per environment even if upload succeeded and GitHub supplies an artifact ID/digest;
7. explicitly exclude timeout-cancelled shards from the successful-complete inventory. The six prospectively selected sampled cancellations are bound to the workflow's frozen `timeout-minutes: 360` limit; timeout cancellation is implementation/provenance incompleteness, never scientific FAIL.

All inherited source/cohort/channel/precision/R/rho/tree/leaf/per-rho/unresolved-depth/cross-environment controls remain mandatory.

## Firewall and next admissible action

While source run `35405065903` remains nonterminal: status/provenance checking only. Do not consume partial source science, adaptively stop, rerun producer science based on observed values, or launch a competing same-object scientific gate.

After complete source terminalization, prospectively freeze the exact terminal run/job/step/artifact inventory and digests **before** opening substantive payload. The terminal inventory must distinguish successful-complete shard artifacts from artifacts emitted by cancelled/time-limited executions. Then execute exactly one separately frozen independent Critic closure against the immutable valid-completion inventory.

Expected nominal complete source inventory remains 384 successful shard artifacts + 2 assemblies + 1 aggregate. If terminal execution is incomplete/cancelled, classify only under the frozen implementation/provenance semantics; never convert that into scientific FAIL.

If a valid unresolved record exists only after fully valid independent closure, freeze the smallest exact unresolved record/cell as counterexample-first successor; do not increase `MAX_DEPTH` first.

## Retained lower authority

Iter504U remains terminal scoped `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED` for its frozen six-case object. Iter504V Phase-A remains sentinel-only. No Iter504U/Iter504V child result is promoted to family/all-domain/D7/global closure.

## Governance

`RQIR Core v1.0 = FROZEN`. `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden. Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`.

`INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; green CI/artifact upload != science; missing object/certificate != zero residual; scoped child result != family closure.

No authority exists for `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, `D7_FULLY_CLOSED`, `CANDIDATE_GRAVITY_ESTABLISHED`, or `NEW_PHYSICS_FOUND`.
