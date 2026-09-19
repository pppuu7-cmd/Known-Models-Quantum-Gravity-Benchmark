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

Fresh post-gate state remains nonterminal: run endpoint `queued / conclusion=null`; source-lock `105792998164 = completed/success`. Frozen first-page snapshot for the latest closure contains 30 jobs = 8 completed/success, 12 completed/cancelled, 8 in progress, 2 queued. Latest metadata-only artifact read shows 24 artifacts. No artifact ZIP bytes were opened/downloaded and no case/leaf/slope/drift/certification/assembly/aggregate/counterexample scientific value was consumed.

Current science status remains `IN_PROGRESS_NOT_CLASSIFIED`.

`recovery/state.json` contains older Phase-B counters. Durable current override is `recovery/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_STATE_DELTA_2026-09-19.json` plus fresh GitHub state.

## Latest terminal preterminal closure — assembly authority reachability

Gate: `ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_PROVENANCE_GATE`.

Prospective preregistration: `97b4251fbcf690cedbfc475232ec607e90044b75`.

Terminal classification:

`ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_VERIFIED_SCOPED`.

Decision projection SHA256:
`e07665be4a044f7abfe8e09ebc79d6cd87db9c5aa9611df8669b2349e7960c67`.

Exact immutable workflow blob: `a34f23eaab9b7fec0a1da2b0b684031a24cfa360`.

The workflow uses:
- `assemble-311: needs: cases-311; if: always()`;
- `assemble-313: needs: cases-313; if: always()`;
- `aggregate: needs: [assemble-311, assemble-313]; if: always()`.

Therefore cancelled case jobs do not make the downstream GitHub jobs scheduler-unreachable. Assembly/aggregate jobs may still run nominally.

The verified block is **valid authority reachability**: Phase-B requires exactly 192 successful-complete shards per Python environment. The frozen snapshot already contains terminal cancelled required case jobs in both environments (7 visible in Python 3.11 and 5 in Python 3.13). Attempt 1 has no in-attempt retry path that can turn those terminal cancelled matrix children into successful-complete shards. Consequently this same attempt can no longer satisfy the frozen 192+192 successful-complete authority inventory, even if downstream `if: always()` jobs later execute and emit nominal artifacts.

Raw/canonical/terminal records:
- `research/results/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_RAW_2026-09-19.json`;
- `research/results/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_RESULT_2026-09-19.json`;
- `research/results/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_TERMINAL_2026-09-19.md`.

No source science was classified.

## Prior independently confirmed execution-provenance closures

### Timeout causality

`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED`.

Prospective prereg `2fc02a80c7d4db6f05813cbb571eb01cb4fb7c53`; independent Critical Review commit `08e60368119cc3c06dd8d493eb3fdf955300d88e = CONFIRMED_SCOPED`.

The prospectively selected first six cancelled case jobs all terminate their frozen numerical step within four seconds of the exact workflow `timeout-minutes: 360` boundary across Python 3.13 and 3.11, with runner marker `The operation was canceled.` and successful post-cancellation upload. Successful control `105793032770` completes normally at `272.992696` minutes. These cancellations are execution-timeout/provenance events, not science verdicts.

### Cancelled-job artifact provenance

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE` -> `ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED`, independently reviewed at `171d8ee9b0945de095ed9f5cbc1f9296aa2007fc = CONFIRMED_SCOPED`.

Cancelled case jobs can have frozen execution step `cancelled`, upload step `success`, and a matching non-expired SHA256-digested artifact. Therefore artifact presence/ID/digest alone is insufficient evidence of a completed valid shard.

## Existing verifier-binding closures

Source assembler binding gate is independently confirmed scoped. Mandatory obligations:
1. bind every expected shard/artifact identity and `shard.json` to exactly its frozen four physical case records and prove exactly 192 unique complete shards per environment;
2. reconstruct every parent-inclusion child/parent dyadic edge and reject malformed/duplicate/orphan records.

Source aggregate binding gate is confirmed scoped. Mandatory obligations:
3. rebind PASS/INCONCLUSIVE classification to independently recomputed unresolved evidence;
4. rebind `decision_projection_sha256_by_state` keys and projection sequence to the exact canonical 768-state identity;
5. rebind `case_file_sha256` keys/content hashes to the exact canonical 768-state identity.

Execution-provenance obligations now also require:
6. bind every shard admitted to authority to `job.conclusion == success` and frozen `Execute frozen quartile shard == success`;
7. exclude timeout-cancelled/incomplete artifacts regardless of artifact ID/digest;
8. distinguish scheduler reachability of `if: always()` assembly/aggregate jobs from semantic validity of their input inventory;
9. require exactly 192 successful-complete shards in Python 3.11 and exactly 192 in Python 3.13 before any assembly/aggregate artifact can enter terminal scientific authority.

All inherited source/cohort/channel/precision/R/rho/tree/leaf/per-rho/unresolved-depth/cross-environment controls remain mandatory.

## Frozen Phase-B object

Complete q=1 domain: causals `0to5,1to4,2to3` x blocks `0..3` x signed paths `0..3` x amplitude boxes `0..15` = 768 canonical records.

Frozen contract retains rho `0.35,0.9,1.6,2.7`; R `6,8,10,12`; all 243 channels; 384-bit precision; deterministic dyadic midpoint partition; `MAX_DEPTH=3`; local validated `D(J)` recomputed at every visited node; exact leaf/per-rho and unresolved-depth binding.

Execution topology: 192 deterministic quartile shards per Python environment, 384 total source compute shards, Python 3.11/3.13, `fail-fast:false`, `max-parallel:12`, case-job timeout 360 minutes.

Frozen source taxonomy remains:
- PASS `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`;
- INCONCLUSIVE `ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED`;
- INVALID `ITER504V_BROADER_DOMAIN_INVALID` for implementation/provenance/cohort/channel/depth/partition/source/artifact/cross-environment invalidity.

There is no scientific FAIL label for this bounded source gate.

## Firewall and next admissible action

While source run `35405065903` remains nonterminal: status/provenance checking only. Do not consume partial source science, adaptively stop, rerun producer science based on observed values, or launch a competing same-object scientific gate.

After natural terminalization, prospectively freeze the exact terminal run/job/step/artifact inventory and digests **before** opening substantive payload. Because attempt 1 is already proven unable to satisfy the required 192+192 successful-complete inventory, terminal closure must preserve implementation/provenance incompleteness and must never reinterpret cancellation/timeout as scientific FAIL. A repair/re-execution would require a separate prospective authority; none is created here.

## Retained lower authority and governance

Iter504U remains terminal scoped `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED` for its frozen six-case object. Iter504V Phase-A remains sentinel-only. No child result is promoted to family/all-domain/D7/global closure.

`RQIR Core v1.0 = FROZEN`. `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden. Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`.

`INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`; green CI/artifact upload != science; missing object/certificate != zero residual; scoped child result != family closure.

No authority exists for `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, `D7_FULLY_CLOSED`, `CANDIDATE_GRAVITY_ESTABLISHED`, or `NEW_PHYSICS_FOUND`.
