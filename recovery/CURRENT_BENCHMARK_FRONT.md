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

Fresh run metadata remains `queued / conclusion=null`. Complete exact-run job pagination reports `total_count=385`; source-lock `105792998164 = completed/success`; nonterminal jobs remain present on later pages, including queued jobs `105793035543`, `105793039803`, and `105793044215`. Artifact metadata first page now contains 29 exact-run/head-bound non-expired SHA256-digested records; artifact ZIP bytes remain unopened. No scientific case/leaf/slope/drift/certification/assembly/aggregate/counterexample payload has been consumed. Phase-B science remains `IN_PROGRESS_NOT_CLASSIFIED`.

## Latest closure — run/job terminality coherence

`ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_PROVENANCE_GATE` -> `ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENT_SCOPED`.

- prospective prereg `5e67991ca4c09a9098ad3ae3a1d91601d2bbc7c7`;
- raw result commit `c9dacc08c9152900bfcb393d28aaa8f245c03956`, SHA256 `4b9c3727630f7631f5ae8d5c5f61b6f4ab842caac933c89d8ed10ae9b299e8e1`;
- canonical result commit `50bac01a4068d21f5a3e9d4d497e5b618424c0e7`, SHA256 `4fb7f7709ccc0ed62af5b402d9e04cfac356626fc5681d378255e6f3cc6ff10b`;
- terminal record `2f00b7af91e5e9249e7f01b4eb561b4cdeb5169e`;
- state delta `2807c7f051a5577482ede24abcb15c639fe0b640`.

The apparently stale-looking workflow-run endpoint is not currently contradicted by the complete job inventory: the run is nonterminal and the exact 385-job collection still contains nonterminal jobs. This is metadata/provenance coherence only. It does not validate successful-execution completeness and does not classify Phase-B science.

## Full job-inventory authority

`ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_FULL_JOB_INVENTORY_AUTHORITY_INCOMPLETE_VERIFIED_SCOPED`.

- prereg `cb69a9057a0b74cf8680e57f2d810d72ccdc6f93`;
- terminal record `4f2ee5a7f6312733ec782ec3a6ee461fc6527a3b`;
- state delta `aaff29bb277f012b4327f4e19a57397253fd324b`;
- exact instantiated inventory: 385 jobs = source-lock 1 + matrix jobs 384.

The defect is successful-execution completeness, not matrix instantiation. Terminal cancelled required shards exist in both Python environments, so attempt 1 can no longer satisfy exactly 192 successful-complete shards in Python 3.11 and exactly 192 in Python 3.13.

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

While run `35405065903` remains nonterminal: status/provenance work only; no partial science, no adaptive rerun, no competing same-object scientific gate. Do not reopen the blocked check-suite gate unless exact check-suite metadata becomes available under the same frozen object.

After natural terminalization, prospectively freeze the exact terminal run/job/step/artifact inventory and digests before substantive payload access, then execute one separately frozen terminal closure/Critic. Attempt 1 is already unable to satisfy 192+192 successful-complete shards; terminal closure must preserve implementation/provenance incompleteness and never reinterpret cancellation/timeout as scientific FAIL. Any repair/re-execution requires separate prospective authority.

Durable current recovery override: `recovery/ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_STATE_DELTA_2026-09-19.json` plus the earlier full-job-inventory and check-suite terminality state deltas and fresh GitHub state. `recovery/state.json` contains older Phase-B counters.

## Governance

`RQIR Core v1.0 = FROZEN`. `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden. Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`.

`INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`; green CI/artifact upload != science; scoped child result != family closure.

No authority exists for `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, `D7_FULLY_CLOSED`, `CANDIDATE_GRAVITY_ESTABLISHED`, or `NEW_PHYSICS_FOUND`.
