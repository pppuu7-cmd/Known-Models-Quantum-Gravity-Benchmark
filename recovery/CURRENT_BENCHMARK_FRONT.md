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
- execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- immutable launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- source run `35405065903`, attempt 1.

Fresh post-freeze run metadata remains `queued / conclusion=null`. Complete exact-run job pagination reports `total_count=385`: `completed=100`, `queued=285`, `in_progress=0`; source-lock `105792998164 = completed/success`. No source-run artifact ZIP bytes were opened and no scientific case/leaf/slope/drift/certification/assembly/aggregate/counterexample payload has been consumed. Phase-B science remains `IN_PROGRESS_NOT_CLASSIFIED`.

## Latest closure — queue-only nonterminal execution topology

`ITER504V_PHASE_B_ZERO_ACTIVE_RUNNER_QUEUE_STATE_PROVENANCE_GATE` -> `ITER504V_PHASE_B_QUEUE_ONLY_NONTERMINAL_STATE_VERIFIED_SCOPED`.

- prospective prereg `499ae185c2cd2f27cc0ca2191ff73fe07b2aa50c`;
- canonical result commit `05c71ac24fc9323b8f1c5830fdee4387e73aa0e9`;
- canonical result SHA256 `5c4c021e4a645bd2e3acca7f22bc763a5f3d562af5cafd91434f4d5a96a06021`;
- terminal record commit `9b87fd73a71903aae363efe614c5fbca350ee6bb`;
- state delta commit `7107a438436411f166cda70b8a7b1e2022d6225a`;
- durable handoff commit `753a89e22980b0d900f7968be9163a93a9f3e009`.

The exact post-preregistration snapshot has zero actively executing jobs and 285 queued jobs. This establishes an instantaneous queue-only nonterminal topology only. It does **not** identify the cause of queuing and does not classify Phase-B science. No claim is authorized about billing, account limits, GitHub capacity, runner scarcity, scheduler policy, or any other queue cause.

## Retained run/job terminality coherence

`ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_PROVENANCE_GATE` -> `ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENT_SCOPED`.

The earlier apparently stale-looking workflow-run endpoint was not contradicted by the complete inventory because nonterminal jobs existed. The newer queue-only gate sharpens the topology: the source run is still nonterminal, but all remaining nonterminal jobs are currently queued rather than active.

## Full job-inventory authority

`ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_FULL_JOB_INVENTORY_AUTHORITY_INCOMPLETE_VERIFIED_SCOPED`.

Exact instantiated inventory: 385 jobs = source-lock 1 + matrix jobs 384. Terminal cancelled required shards exist in both Python environments, so attempt 1 can no longer satisfy exactly 192 successful-complete shards in Python 3.11 and exactly 192 in Python 3.13. The new queue-only topology does not repair this already terminal provenance fact.

## Check-suite closure retained

`ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_BLOCKED_SCOPED`, independently `CONFIRMED_SCOPED` at `d515fcf3d00d1e3290783c31ae88ec7bdc6ce6ce`.

The exact check-suite endpoint remains unavailable through the current connector. No surrogate endpoint is authorized under that frozen object. `BLOCKED != FAIL`; this does not classify Phase-B science.

## Retained execution-provenance closures

- assembly reachability under cancelled shards -> `ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_VERIFIED_SCOPED`;
- timeout causality -> `ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED`, independently `CONFIRMED_SCOPED` at `08e60368119cc3c06dd8d493eb3fdf955300d88e`;
- cancelled-job artifact provenance -> `ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED`, independently `CONFIRMED_SCOPED` at `171d8ee9b0945de095ed9f5cbc1f9296aa2007fc`;
- source assembler binding defects -> verified scoped, independently confirmed;
- source aggregate binding defects -> verified scoped, independently confirmed.

Cancelled/timeout shards are implementation/provenance incompleteness, never scientific FAIL. `if: always()` may keep downstream jobs scheduler-reachable but cannot restore semantic authority completeness.

## Mandatory terminal-Critic obligations

1. exact shard/artifact identity + `shard.json` -> frozen four-record cohort;
2. exactly 192 unique successful-complete shards per environment;
3. reconstruct every parent-inclusion dyadic edge;
4. recompute unresolved evidence and bind PASS/INCONCLUSIVE classification;
5. exact canonical 768-state decision-projection key set/sequence;
6. exact canonical 768-state provenance key set/content hashes;
7. `job.conclusion == success` and frozen execution-step success for every admitted shard;
8. exclude timeout/cancelled/incomplete artifacts regardless of artifact ID/digest;
9. distinguish scheduler reachability from semantic authority validity;
10. preserve exact run/job terminality coherence and do not substitute inaccessible check-suite state with a surrogate surface.

All inherited source/cohort/channel/precision/R/rho/tree/leaf/per-rho/unresolved-depth/cross-environment controls remain mandatory.

## Frozen Phase-B object and taxonomy

Complete q=1 domain: causals `0to5,1to4,2to3` x blocks `0..3` x signed paths `0..3` x amplitude boxes `0..15` = 768 canonical records. Frozen contract retains rho `0.35,0.9,1.6,2.7`; R `6,8,10,12`; all 243 channels; 384-bit precision; deterministic dyadic midpoint partition; `MAX_DEPTH=3`; local validated `D(J)` at every visited node.

Frozen source taxonomy:
- PASS `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`;
- INCONCLUSIVE `ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED`;
- INVALID `ITER504V_BROADER_DOMAIN_INVALID` for implementation/provenance/cohort/channel/depth/partition/source/artifact/cross-environment invalidity.

There is no scientific FAIL label for this bounded source gate.

## Next admissible action

While run `35405065903` remains nonterminal: status/provenance work only and only on material state changes; no partial science, no adaptive rerun, no competing same-object scientific gate. Do not infer the queue cause from the queue-only topology. Do not reopen the blocked check-suite gate unless exact check-suite metadata becomes available under the same frozen object.

After natural terminalization, prospectively freeze the exact terminal run/job/step/artifact inventory and digests before substantive payload access, then execute one separately frozen terminal closure/Critic. Attempt 1 is already unable to satisfy 192+192 successful-complete shards; terminal closure must preserve implementation/provenance incompleteness and never reinterpret cancellation/timeout as scientific FAIL. Any repair/re-execution requires separate prospective authority.

Durable current recovery override: `recovery/ITER504V_PHASE_B_ZERO_ACTIVE_RUNNER_QUEUE_STATE_PROVENANCE_STATE_DELTA_2026-09-19.json` plus prior Phase-B state deltas and fresh GitHub state. `recovery/state.json` contains older Phase-B counters and is lower authority than this front plus the latest state delta.

## Governance

`RQIR Core v1.0 = FROZEN`. `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden. Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`.

`INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`; green CI/artifact upload != science; scoped child result != family closure.

No authority exists for `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, `D7_FULLY_CLOSED`, `CANDIDATE_GRAVITY_ESTABLISHED`, or `NEW_PHYSICS_FOUND`.
