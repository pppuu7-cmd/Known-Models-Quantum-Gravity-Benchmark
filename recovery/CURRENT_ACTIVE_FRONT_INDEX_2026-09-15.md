# Current active front index — 2026-09-19

Fresh repository `main` and fresh Actions state always outrank this index if they diverge.

## Frozen global state

- Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark` only.
- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain unauthorized.
- Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`.
- `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `INCONCLUSIVE != FAIL`; green CI/artifact upload != science; scoped result != family/global closure.

## Active scientific gate

`ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE` / execution `ITER504V_PHASE_B_SOURCE_EXECUTION`.

Prospective authority: prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`; static implementation Critic `eaa2d1ef84fe8370f33cec360233f60571f9bcd0 = PASS_SCOPED`; execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`; source launch/head `31fcdacffcc394e96b73917083281edb90d6753c`; source run `35405065903` attempt 1.

Latest fresh state remains nonterminal: run endpoint `queued / conclusion=null`; source-lock `105792998164 = success`. Latest validated first-page job snapshot: 30 = 8 completed/success, 12 completed/cancelled, 8 in progress, 2 queued. Latest validated artifact metadata count `20`. Artifact bytes were not opened/downloaded. No partial scientific values were consumed and no duplicate source execution was launched.

Operational classification: `IN_PROGRESS_NOT_CLASSIFIED`.

Recovery delta `recovery/ITER504V_PHASE_B_TIMEOUT_CAUSALITY_STATE_DELTA_2026-09-19.json` overrides stale selected Phase-B fields in `recovery/state.json` until the consolidated state file is next rewritten.

## Latest terminal preterminal provenance closure — timeout causality

`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED`.

- preregistration `2fc02a80c7d4db6f05813cbb571eb01cb4fb7c53`;
- canonical result commit `558c02abd710812437f8616397d27cef7091af44`;
- terminal record commit `a1ca2288e774895ab6f77dedc2065299df8f2b89`;
- canonical result SHA256 `471a8369cbfdb763ef5193984fe0f60d058d183e6f5bd5fb19e61bcb1e822504`;
- frozen workflow blob `a34f23eaab9b7fec0a1da2b0b684031a24cfa360` sets `timeout-minutes: 360` for both Python case matrices and artifact upload `if: always()`;
- first six visible cancelled case jobs selected by ascending job id before log inspection all cancelled the frozen execution step within four seconds of the 360-minute boundary, across Python 3.13 and 3.11;
- each showed runner marker `The operation was canceled.` and a successful post-cancellation artifact upload;
- successful control job `105793032770` completed the execution step successfully at `272.992696` minutes;
- artifact bytes opened: false;
- production science consumed: false;
- source science classified: false.

New fact: the prospectively sampled Phase-B cancellations are execution-timeout/provenance events caused by the frozen six-hour case-job limit. Timeout-cancelled artifacts are incomplete shards and cannot enter terminal scientific authority even if upload succeeds and a SHA256 digest exists.

## Independently confirmed cancelled-job artifact provenance

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE` -> `ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED`, independently reviewed at `171d8ee9b0945de095ed9f5cbc1f9296aa2007fc = CONFIRMED_SCOPED`.

- preregistration `a0e28e3a96e109ee9ed440a267ee1407cddf2d55`;
- 12 visible cancelled case jobs had cancelled frozen execution step, successful artifact upload, and matching non-expired SHA256-digested artifact metadata;
- chain-list SHA256 `d0d7c9840e76300feeffe40eb09650eaf0a00f4ddd117c77ccfff5832a6b4dee`;
- canonical decision SHA256 `6e2de425bc3b8cc83c75641c160e352061c2479b2f0564ce3b5b2eb3882f9e2f`;
- artifact bytes opened: false;
- production science consumed: false;
- source science classified: false.

Mandatory rule: artifact presence/ID/digest is insufficient. Every required shard artifact must be bound to both `job.conclusion == success` and `Execute frozen quartile shard` step conclusion `success`; timeout/cancelled execution artifacts cannot count as complete source shards.

## Historical time-local metadata closure

`ITER504V_PHASE_B_PRETERMINAL_SOURCE_STATUS_PROVENANCE_GATE` remains historically valid only for its earlier frozen observation and was independently reviewed at `1989e28d78fdddf2117c3b79b5f90af4bd752603 = CONFIRMED_SCOPED`. It is superseded as a current-status statement by later Actions cancellations and artifact growth.

## Existing terminal preterminal verifier closures

### Source assembler binding

`ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_ADVERSARIAL_GATE` -> `ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECTS_VERIFIED_SCOPED`, independently confirmed at `c641e1083473000307c3399c4c1e51e8194cb43c`.

Mandatory obligations:
- reconstruct and bind every parent-inclusion child/parent dyadic edge;
- bind every exact artifact/shard identity plus `shard.json` to its frozen four physically contained records.

### Source aggregate binding

`ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_ADVERSARIAL_GATE` -> `ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_DEFECTS_VERIFIED_SCOPED`.

Mandatory additional obligations:
- rebind PASS/INCONCLUSIVE classification to independently recomputed unresolved evidence;
- require exact canonical 768-state key set/sequence for `decision_projection_sha256_by_state`;
- require exact canonical 768-state key set and independently bound content hashes for `case_file_sha256`.

## Frozen Phase-B object

Complete canonical q=1 cover: 768 records = 3 causals x 4 blocks x 4 signed paths x 16 amplitude boxes. Frozen no-refit contract retains 384-bit precision, all 243 channels, R `6,8,10,12`, rho `0.35,0.9,1.6,2.7`, threshold `1/20`, robust floor `1`, deterministic dyadic midpoint partition, `MAX_DEPTH=3`, local `D(J)` recomputation on every visited node, exact leaf/per-rho binding and unresolved-only-at-depth-3 semantics.

Execution topology: 192 deterministic quartile shards per Python environment, 384 source compute shards total, Python 3.11/3.13, `fail-fast:false`, `max-parallel:12`, frozen case-job timeout 360 minutes.

## Next admissible action

While source run `35405065903` is nonterminal: status/provenance checks only. Do not consume partial science, rerun based on observed values, or launch a competing same-object scientific gate.

After complete terminalization: prospectively freeze the exact terminal run/job/step/artifact inventory and digests before substantive payload access. Exclude cancelled/time-limited/incomplete shard artifacts from valid-completion inventory. Then execute exactly one separately frozen independent Critic closure satisfying all assembler, aggregate, job/step completion, timeout-completeness and inherited scientific-contract controls.

Nominal complete inventory remains 384 **successful-complete** shard artifacts + 2 assemblies + 1 aggregate. If the source execution terminalizes incomplete/cancelled, classify the execution only under frozen implementation/provenance semantics, never as scientific FAIL.
