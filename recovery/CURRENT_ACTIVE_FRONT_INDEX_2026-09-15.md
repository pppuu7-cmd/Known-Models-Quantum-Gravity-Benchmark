# Current active front index — 2026-09-19

Fresh repository `main` and fresh Actions state always outrank this index if they diverge.

## Frozen global state

- repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark` only;
- `RQIR Core v1.0 = FROZEN`;
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 selectors unauthorized;
- Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`;
- `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `INCONCLUSIVE != FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`; green CI/artifact upload != science; scoped result != family/global closure.

## Active scientific execution

`ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE` / `ITER504V_PHASE_B_SOURCE_EXECUTION`.

- prereg: `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- static implementation Critic: `eaa2d1ef84fe8370f33cec360233f60571f9bcd0 = PASS_SCOPED`;
- execution authority: `caf67585a9fad990dd90948df51839e6ed7cf891`;
- launch/head: `31fcdacffcc394e96b73917083281edb90d6753c`;
- source run: `35405065903`, attempt 1;
- latest run endpoint: `queued / conclusion=null`;
- source-lock `105792998164 = success`;
- latest frozen first-page job snapshot: 30 = 8 success, 12 cancelled, 8 in progress, 2 queued;
- latest metadata-only artifact count: 24;
- artifact ZIP bytes opened: false;
- partial scientific values consumed: false;
- operational science classification: `IN_PROGRESS_NOT_CLASSIFIED`.

Durable recovery override: `recovery/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_STATE_DELTA_2026-09-19.json`.

## Latest terminal preterminal closure

`ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_PROVENANCE_GATE` -> `ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_VERIFIED_SCOPED`.

- prospective prereg: `97b4251fbcf690cedbfc475232ec607e90044b75`;
- workflow blob: `a34f23eaab9b7fec0a1da2b0b684031a24cfa360`;
- decision projection SHA256: `e07665be4a044f7abfe8e09ebc79d6cd87db9c5aa9611df8669b2349e7960c67`;
- cancelled visible required shards: 7 in Python 3.11 and 5 in Python 3.13;
- positive control shard `105793032770`: success / execution-step success;
- source-lock: success;
- source science consumed: false.

Workflow orchestration uses `if: always()` for both environment assemblies and final aggregate. Thus scheduler reachability survives cancelled matrix children, but **valid authority reachability does not**: the frozen source authority requires exactly 192 successful-complete shards per environment, and attempt 1 already contains terminal cancelled required shards in both environments with no in-attempt retry path. Nominal downstream artifacts cannot repair missing successful-execution provenance.

## Prior independently confirmed provenance closures

- timeout-causality gate -> `ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED`; independent review `08e60368119cc3c06dd8d493eb3fdf955300d88e = CONFIRMED_SCOPED`;
- cancelled-job artifact provenance gate -> `ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED`; independent review `171d8ee9b0945de095ed9f5cbc1f9296aa2007fc = CONFIRMED_SCOPED`;
- source assembler binding adversarial gate -> defects verified scoped, independently confirmed;
- source aggregate binding adversarial gate -> defects verified scoped.

## Mandatory terminal-Critic obligations

1. exact shard/artifact identity + `shard.json` -> frozen four-record cohort;
2. exact 192 unique successful-complete shards per environment;
3. reconstruct every parent-inclusion dyadic edge;
4. recompute unresolved evidence and bind PASS/INCONCLUSIVE classification;
5. exact canonical 768-state decision-projection key set/sequence;
6. exact canonical 768-state provenance key set/content hashes;
7. require `job.conclusion == success` and frozen execution-step success for every admitted shard;
8. exclude all timeout/cancelled/incomplete shard artifacts regardless of ID/digest;
9. distinguish scheduler reachability from semantic authority validity; `if: always()` downstream execution is not authority completion.

All inherited source/cohort/channel/precision/R/rho/tree/leaf/per-rho/unresolved-depth/cross-environment controls remain mandatory.

## Next admissible action

While run `35405065903` remains nonterminal: status/provenance checks only. No partial science, no adaptive rerun, no competing same-object scientific gate.

After natural terminalization: prospectively freeze the exact terminal run/job/step/artifact inventory and digests before substantive payload access. Because attempt 1 is already unable to satisfy 192+192 successful-complete shards, classify exact execution completeness under frozen implementation/provenance semantics and never convert incomplete execution into scientific FAIL. Any repair/re-execution requires a separate future prospective authority.
