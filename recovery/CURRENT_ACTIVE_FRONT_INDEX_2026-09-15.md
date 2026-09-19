# Current active front index — 2026-09-19

Fresh repository `main` and fresh Actions state always outrank this index if they diverge.

## Frozen global state

- repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark` only;
- `RQIR Core v1.0 = FROZEN`;
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 selectors remain unauthorized;
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`;
- `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `INCONCLUSIVE != FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`; green CI/artifact upload != science; scoped result != family/global closure.

## Active scientific execution

`ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE` / `ITER504V_PHASE_B_SOURCE_EXECUTION`.

- prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- static Critic `eaa2d1ef84fe8370f33cec360233f60571f9bcd0 = PASS_SCOPED`;
- execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- source run `35405065903`, attempt 1;
- fresh run endpoint `queued / conclusion=null`;
- complete latest-attempt job collection `total_count=385` across pages 1..4;
- source-lock `105792998164 = completed/success`;
- nonterminal exact-run jobs remain present, including queued witnesses `105793035543`, `105793039803`, `105793044215`;
- artifact metadata first-page count: 29; artifact bytes unopened;
- partial scientific values consumed: false;
- science classification: `IN_PROGRESS_NOT_CLASSIFIED`.

## Latest closure

`ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_PROVENANCE_GATE` -> `ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENT_SCOPED`.

- prereg `5e67991ca4c09a9098ad3ae3a1d91601d2bbc7c7`;
- raw result `c9dacc08c9152900bfcb393d28aaa8f245c03956`, SHA256 `4b9c3727630f7631f5ae8d5c5f61b6f4ab842caac933c89d8ed10ae9b299e8e1`;
- canonical result `50bac01a4068d21f5a3e9d4d497e5b618424c0e7`, SHA256 `4fb7f7709ccc0ed62af5b402d9e04cfac356626fc5681d378255e6f3cc6ff10b`;
- terminal record `2f00b7af91e5e9249e7f01b4eb561b4cdeb5169e`;
- state delta `2807c7f051a5577482ede24abcb15c639fe0b640`.

The run/job terminality relation is currently coherent: the workflow run is nonterminal and the exact complete job inventory still contains nonterminal jobs. This is provenance coherence only, not science and not successful-execution completeness.

## Retained full-job authority incompleteness

`ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_FULL_JOB_INVENTORY_AUTHORITY_INCOMPLETE_VERIFIED_SCOPED`.

Exact instantiated inventory is 385 jobs = one source-lock + 384 matrix jobs. Required cancelled/timeout shards exist in both Python environments, so attempt 1 cannot satisfy exactly 192 successful-complete shards per environment.

## Retained check-suite closure

`ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_BLOCKED_SCOPED`, independently `CONFIRMED_SCOPED` by `d515fcf3d00d1e3290783c31ae88ec7bdc6ce6ce`.

The exact check-suite endpoint remains unavailable through the current connector; no surrogate may replace it under the frozen gate.

## Mandatory terminal-Critic obligations

1. exact shard/artifact identity + `shard.json` to frozen four-record cohort;
2. exactly 192 unique successful-complete shards per environment;
3. reconstruct every parent-inclusion dyadic edge;
4. recompute unresolved evidence and bind classification;
5. exact canonical 768-state decision-projection key set/sequence;
6. exact canonical 768-state provenance key set/content hashes;
7. require job success and frozen execution-step success for every admitted shard;
8. exclude timeout/cancelled/incomplete artifacts regardless of ID/digest;
9. distinguish scheduler reachability from semantic authority validity;
10. preserve run/job terminality coherence and do not substitute inaccessible check-suite state with a surrogate.

Earlier assembler-binding, aggregate-binding, cancelled-artifact, timeout-causality, assembly-reachability, and full-job-inventory closures remain in force. Historical FAIL/BLOCKED/INVALID labels are unchanged.

## Next admissible action

While run `35405065903` remains nonterminal: status/provenance only. No partial science, no adaptive rerun, no competing same-object scientific gate.

After natural terminalization: prospectively freeze exact terminal run/job/step/artifact inventory and digests before substantive payload access, then perform one separately frozen terminal closure/Critic. Attempt 1 remains authority-incomplete because of cancelled/timeout required shards; this must not be reinterpreted as scientific FAIL. Any repair/re-execution requires separate prospective authority.

Durable recovery override: `recovery/ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_STATE_DELTA_2026-09-19.json` plus earlier Phase-B state deltas and fresh GitHub state. `recovery/state.json` contains older Phase-B counters.
