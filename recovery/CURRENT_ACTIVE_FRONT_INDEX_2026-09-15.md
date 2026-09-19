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

- prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- static Critic `eaa2d1ef84fe8370f33cec360233f60571f9bcd0 = PASS_SCOPED`;
- execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- source run `35405065903`, attempt 1;
- fresh run endpoint `queued / conclusion=null`;
- source-lock `105792998164 = success`;
- fresh first-page matrix status: 8 success, 12 cancelled, 9 in progress, 0 queued;
- artifact ZIP bytes opened: false;
- partial scientific values consumed: false;
- science classification: `IN_PROGRESS_NOT_CLASSIFIED`.

## Full job inventory closure

`ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_FULL_JOB_INVENTORY_AUTHORITY_INCOMPLETE_VERIFIED_SCOPED`.

Exact instantiated inventory is 385 jobs = 1 source-lock + 384 matrix jobs. Terminal cancelled required shards exist in both environments. Therefore attempt 1 cannot satisfy the frozen 192 successful-complete shards in Python 3.11 plus 192 in Python 3.13, independent of scientific values.

Authority: prereg `cb69a9057a0b74cf8680e57f2d810d72ccdc6f93`; terminal `4f2ee5a7f6312733ec782ec3a6ee461fc6527a3b`; state delta `aaff29bb277f012b4327f4e19a57397253fd324b`.

## Latest closure

`ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_GATE` -> `ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_BLOCKED_SCOPED`.

- prereg `27e2176d488770ef425916d2fd6da1836724017e`;
- exact check suite `95888147622`;
- raw commit `fdef83468c59645f37fed8598d9ce8bb7226bdb2`;
- canonical commit `90da05534b53a7eda107abc22096310cd765a390`;
- terminal commit `b092611ae361abca4d89316d69ce2298841caaae`;
- recovery delta `1ec8049170a2dfbc5a22d76cec7c294ff4f5814b`.

Fresh exact-run jobs are readable and include nine in-progress matrix jobs, but the current GitHub connector does not expose the exact check-suite endpoint required by the frozen gate. No surrogate endpoint was substituted after the result. This is a local metadata/provenance BLOCKED, not a scientific FAIL and not a Phase-B source classification.

## Retained provenance / verifier obligations

1. bind exact shard/artifact identity + `shard.json` to frozen four-record cohort;
2. require exactly 192 unique successful-complete shards per environment;
3. reconstruct every parent-inclusion dyadic edge;
4. recompute unresolved evidence and bind classification;
5. exact canonical 768-state decision-projection key set/sequence;
6. exact canonical 768-state provenance key set/content hashes;
7. require job success and frozen execution-step success for each admitted shard;
8. exclude timeout/cancelled/incomplete artifacts regardless of ID/digest;
9. distinguish scheduler reachability from semantic authority validity.

The earlier assembler-binding, aggregate-binding, cancelled-artifact, timeout-causality, and assembly-reachability closures remain in force; historical FAIL/BLOCKED/INVALID labels are unchanged.

## Next admissible action

While run `35405065903` remains nonterminal: status/provenance checks only. No partial science, no adaptive rerun, no competing same-object scientific gate. Do not reopen the blocked check-suite gate unless exact check-suite metadata becomes available under the same frozen object.

After natural terminalization: prospectively freeze exact terminal run/job/step/artifact inventory and digests before substantive payload access, then perform one separately frozen terminal closure/Critic. Attempt 1 is already authority-incomplete; cancellation/timeout must never be converted into scientific FAIL. Any repair/re-execution requires separate prospective authority.

Durable recovery override: `recovery/ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_STATE_DELTA_2026-09-19.json` plus `recovery/ITER504V_PHASE_B_FULL_JOB_INVENTORY_STATE_DELTA_2026-09-19.json` and fresh GitHub state.
