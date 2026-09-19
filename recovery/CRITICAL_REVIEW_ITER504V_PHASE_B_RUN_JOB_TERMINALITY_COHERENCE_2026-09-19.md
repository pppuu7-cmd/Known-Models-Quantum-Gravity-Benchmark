# Independent Critical Review — Iter504V Phase-B run/job terminality coherence

Date: 2026-09-19
Lane: independent KMQGB Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## Result reviewed

Exactly one latest bounded terminal provenance result:

- gate: `ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_PROVENANCE_GATE`;
- prospective preregistration: `5e67991ca4c09a9098ad3ae3a1d91601d2bbc7c7`;
- raw result: `c9dacc08c9152900bfcb393d28aaa8f245c03956`;
- canonical result: `50bac01a4068d21f5a3e9d4d497e5b618424c0e7`;
- terminal record: `2f00b7af91e5e9249e7f01b4eb561b4cdeb5169e`;
- historical classification: `ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENT_SCOPED`.

The active scientific source run `35405065903` remains nonterminal. This review does not classify Phase-B science and does not consume any partial scientific payload.

## Preregistration chronology

The gate was frozen before the result read:

- prereg commit time: 2026-09-19T10:06:39Z;
- raw result commit time: 2026-09-19T10:07:33Z;
- canonical result commit time: 2026-09-19T10:07:39Z;
- terminal record commit time: 2026-09-19T10:08:00Z.

No post-hoc criterion change was found.

## Frozen contract review

### HYPOTHESIS / OBJECT

The frozen object is metadata/provenance only: exact workflow run `35405065903`, attempt 1, immutable head `31fcdacffcc394e96b73917083281edb90d6753c`, exact run status/conclusion, and the complete latest-attempt job collection with frozen cardinality 385 = one source-lock plus 384 matrix jobs.

Artifact ZIP bytes and case/leaf/slope/drift/certification/assembly/aggregate/counterexample scientific values are explicitly outside the object.

### SOURCE / REALIZATION AUTHORITY

Fresh GitHub Actions read reproduces the exact run/head/attempt object:

- run id `35405065903`;
- attempt `1`;
- head `31fcdacffcc394e96b73917083281edb90d6753c`;
- run `status=queued`, `conclusion=null`;
- jobs collection `total_count=385`;
- source-lock job `105792998164 = completed/success`.

Fresh page-4 pagination still contains nonterminal jobs. In particular job `105793044215`, `cases (3.11, 2to3, b1, p1, q1)`, remains `queued / conclusion=null`; adjacent page-4 jobs are also queued. Thus the terminality relation used by the frozen gate is independently reproduced now: run nonterminal AND exact-run job inventory contains nonterminal jobs.

### POSITIVE / NEGATIVE CONTROLS

Positive controls surviving independent replay:

- exact run/head/attempt matches;
- exact collection reports frozen total count 385;
- source-lock remains terminal success;
- a nonterminal exact-run job is directly witnessed on the later pagination page.

Negative-control / interpretation checks:

- terminal cancelled/timeout jobs are not treated as successful-complete science shards;
- artifact presence/digest is not used as successful-execution evidence;
- inaccessible check-suite state is not replaced by a surrogate;
- no partial scientific payload was opened or consumed.

Fresh artifact metadata continues to grow after the historical gate snapshot, including artifacts created after the terminal-record time. This does not alter the bounded terminality result because artifact inventory is outside this gate's decision rule and the fresh run/job relation itself remains reproduced.

## Counterexample-first attempts

1. **Nonterminal run with all jobs terminal** — not supported: fresh page 4 contains queued jobs, including `105793044215`.
2. **Terminal run with a nonterminal job** — not supported: fresh exact run endpoint remains nonterminal (`queued`, `conclusion=null`).
3. **Wrong run/head/attempt realization** — not supported: fresh run and job metadata remain bound to run `35405065903`, attempt 1, head `31fcdacffcc394e96b73917083281edb90d6753c`.
4. **Source-lock failure hidden by later jobs** — not supported: job `105792998164` remains `completed/success`.
5. **Overreading `queued` as exact lifecycle coherence** — rejected as outside the frozen claim. The gate tests only terminal-vs-nonterminal coherence. `COHERENT_SCOPED` must not be promoted to a claim that every finer workflow lifecycle status is semantically synchronized with every job state.

No explicit counterexample to the frozen terminality relation was found.

## Verdict

`CONFIRMED_SCOPED`.

The historical classification `ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENT_SCOPED` is independently reproduced for its exact bounded meaning: the workflow run is nonterminal and the complete exact-run job authority contains nonterminal jobs. This is metadata/provenance coherence only.

It does not repair or supersede the separately verified successful-execution incompleteness caused by cancelled/timeout required shards, does not rehabilitate uploaded artifacts from cancelled executions, and does not classify Phase-B science.

## Governance / claim ceiling

- `RQIR Core v1.0 = FROZEN`;
- `BLOCKED != FAIL`;
- `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`;
- `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`;
- finite certificate != universal theorem;
- scoped child result != family closure;
- D7 required subgates remain unclosed;
- terminal selectors remain forbidden;
- Candidate Gravity remains inactive.

No all-domain/family/D7/Candidate-Gravity/Paper-IV/global quantum-gravity conclusion is authorized.

## Handoff

- `RESULT_REVIEWED = ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_PROVENANCE_GATE / canonical result 50bac01a4068d21f5a3e9d4d497e5b618424c0e7`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = PASS_SCOPED`
- `SOURCE/REALIZATION_CHECK = PASS_SCOPED`
- `PROVENANCE_CHECK = PASS_SCOPED`
- `SAME_REALIZATION_CHECK = PASS_SCOPED; fresh run/head/attempt and queued-job witness reproduce the frozen relation`
- `NUMERICAL/STATISTICAL_CHECK = NOT_CONSUMED`
- `COUNTEREXAMPLE_ATTEMPTS = nonterminal-run/all-terminal-jobs REFUTED by queued page-4 jobs; terminal-run/nonterminal-job not present; wrong realization not present; source-lock mismatch not present; finer lifecycle-status interpretation excluded by claim ceiling`
- `OVERCLAIM_CHECK = PASS_SCOPED`
- `VERDICT = CONFIRMED_SCOPED`
- `QUALIFICATIONS = confirms terminality coherence only; does not establish successful shard completeness, exact check-suite coherence, or Phase-B science`
- `UPDATED_STATE = latest terminal run/job coherence closure independently confirmed; active source run remains nonterminal and scientifically unclassified`
- `NEXT_ADMISSIBLE_GATE = while run 35405065903 remains nonterminal, status/provenance/contract audit only. After natural terminalization, prospectively freeze exact terminal run/job/step/artifact inventory and digests before substantive access, then execute one separately frozen terminal Critic under all accumulated Phase-B binding obligations; cancelled/timeout required shards remain implementation/provenance incompleteness, never scientific FAIL.`
