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
- fresh post-freeze run endpoint `queued / conclusion=null`;
- complete job collection `total_count=385`;
- `completed=100`, `queued=285`, `in_progress=0`;
- source-lock `105792998164 = completed/success`;
- artifact/science payload bytes consumed: false;
- science classification: `IN_PROGRESS_NOT_CLASSIFIED`.

## Latest closure

`ITER504V_PHASE_B_ZERO_ACTIVE_RUNNER_QUEUE_STATE_PROVENANCE_GATE` -> `ITER504V_PHASE_B_QUEUE_ONLY_NONTERMINAL_STATE_VERIFIED_SCOPED`.

- prospective prereg `499ae185c2cd2f27cc0ca2191ff73fe07b2aa50c`;
- canonical result commit `05c71ac24fc9323b8f1c5830fdee4387e73aa0e9`;
- canonical result SHA256 `5c4c021e4a645bd2e3acca7f22bc763a5f3d562af5cafd91434f4d5a96a06021`;
- terminal record commit `9b87fd73a71903aae363efe614c5fbca350ee6bb`;
- state delta commit `7107a438436411f166cda70b8a7b1e2022d6225a`;
- durable handoff commit `753a89e22980b0d900f7968be9163a93a9f3e009`.

The exact post-preregistration snapshot contains zero `in_progress` jobs and 285 queued jobs. This is execution-topology provenance only. It does not identify a queue cause and it does not classify Phase-B science.

## Retained authority incompleteness

`ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_GATE` remains `ITER504V_PHASE_B_FULL_JOB_INVENTORY_AUTHORITY_INCOMPLETE_VERIFIED_SCOPED`.

Exact instantiated inventory is 385 jobs = one source-lock + 384 matrix jobs. Required cancelled/timeout shards exist in both Python environments, so attempt 1 cannot satisfy exactly 192 successful-complete shards per environment. The current queue-only state does not repair that terminal fact.

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

Earlier assembler-binding, aggregate-binding, cancelled-artifact, timeout-causality, assembly-reachability, full-job-inventory, and run/job-coherence closures remain in force. Historical FAIL/BLOCKED/INVALID labels are unchanged.

## Next admissible action

While run `35405065903` remains nonterminal: status/provenance only, and only for a material state change. No partial science, no causal queue inference, no adaptive rerun, no competing same-object scientific gate.

After natural terminalization: prospectively freeze exact terminal run/job/step/artifact inventory and digests before substantive payload access, then perform one separately frozen terminal closure/Critic. Attempt 1 remains authority-incomplete because of cancelled/timeout required shards; this must not be reinterpreted as scientific FAIL. Any repair/re-execution requires separate prospective authority.

Durable recovery override: `recovery/ITER504V_PHASE_B_ZERO_ACTIVE_RUNNER_QUEUE_STATE_PROVENANCE_STATE_DELTA_2026-09-19.json` plus prior Phase-B state deltas and fresh GitHub state. `recovery/state.json` contains older Phase-B counters.
