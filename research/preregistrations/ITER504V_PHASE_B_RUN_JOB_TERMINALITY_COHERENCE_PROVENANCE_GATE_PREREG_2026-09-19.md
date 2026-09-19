# ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_PROVENANCE_GATE — prospective preregistration

Date: 2026-09-19
Lane: KMQGB Research / Closure
Status: PROSPECTIVE / FROZEN BEFORE FULL JOB-INVENTORY READ

## HYPOTHESIS

For authoritative Phase-B source run `35405065903`, attempt 1, immutable head `31fcdacffcc394e96b73917083281edb90d6753c`, the GitHub workflow-run terminality state should be coherent with the complete exact-run job inventory: a nonterminal run must retain at least one nonterminal job, while a terminal run must have no queued/in-progress jobs.

## exact OBJECT

Metadata/provenance only:

- repository `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`;
- workflow run `35405065903`, attempt `1`;
- immutable launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- complete latest-attempt job inventory from the exact run, all pages, expected cardinality 385 = source-lock 1 + Phase-B matrix jobs 384;
- workflow-run status/conclusion from the exact run endpoint.

Artifact ZIP bytes and every case/leaf/slope/drift/certification/assembly/aggregate/counterexample scientific value are outside the object and MUST NOT be opened or consumed.

## DEPENDENCY

Inherited authorities:

- Phase-B prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- Phase-B execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- `ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_GATE` terminal result: exact instantiated inventory 385 jobs and successful-execution incompleteness already verified scoped;
- `ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_GATE` remains historical `BLOCKED_SCOPED` because the exact check-suite endpoint is unavailable through the connector. This gate does NOT reopen or substitute for that check-suite object.

## SOURCE / REALIZATION AUTHORITY

GitHub Actions metadata for exact run `35405065903` / attempt 1 / head `31fcdacffcc394e96b73917083281edb90d6753c` only. Current repository `main` at preregistration start was `d515fcf3d00d1e3290783c31ae88ec7bdc6ce6ce`; fresh GitHub state always outranks navigation snapshots.

## FROZEN INPUTS

1. Exact run endpoint for `35405065903`.
2. Complete exact-run latest-attempt jobs collection, paginated until exhausted.
3. Expected exact inventory cardinality 385.
4. Expected source-lock job id `105792998164` and required source-lock terminal success.
5. Terminal job statuses are `completed` regardless of conclusion; nonterminal job statuses include `queued`, `in_progress`, `waiting`, `pending`, or any status other than `completed`.
6. Run terminal iff `status == completed` and conclusion is non-null. Run nonterminal otherwise.

## POSITIVE CONTROLS

- exact run id/head/attempt must match the frozen object;
- source-lock `105792998164` must remain `completed/success`;
- complete inventory must contain exactly 385 unique job IDs;
- exactly one source-lock plus 384 Phase-B matrix jobs must be recoverable from the exact-run collection.

## NEGATIVE CONTROLS

- cancelled/timeout jobs count as terminal jobs for terminality coherence but NEVER as successful-complete science shards;
- artifact presence/digest is not evidence of successful execution and is not used here;
- no check-suite surrogate is allowed;
- no partial scientific payload may be consumed.

## PASS

`ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENT_SCOPED` iff all positive controls pass and exactly one of these coherent states holds:

1. run nonterminal AND at least one exact-run job nonterminal; or
2. run terminal AND all 385 exact-run jobs terminal.

PASS is metadata/provenance coherence only and is not a scientific PASS.

## FAIL

`ITER504V_PHASE_B_RUN_JOB_TERMINALITY_INCOHERENCE_VERIFIED_SCOPED` iff all positive controls pass and either:

1. run nonterminal while all 385 exact-run jobs are terminal; or
2. run terminal while at least one exact-run job remains nonterminal.

FAIL is a workflow-run/job provenance inconsistency only; it is not scientific falsification.

## BLOCKED / INVALID

`ITER504V_PHASE_B_RUN_JOB_TERMINALITY_PROVENANCE_BLOCKED_SCOPED` if complete exact-run pagination cannot be obtained while the run endpoint is readable.

`INVALID_IMPLEMENTATION` if the read is not the exact run/attempt/head object, inventory cardinality/identity cannot be reconciled to the frozen 385-job authority despite successful pagination, or scientific payload is consumed.

## INTERPRETATION CEILING

This gate may classify only run/job metadata coherence. It cannot classify Phase-B physics, cannot rehabilitate timeout/cancelled shards, cannot authorize a rerun, and cannot promote any all-domain/family/D7/Candidate-Gravity/Paper-IV/global quantum-gravity claim. `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`; green CI/status metadata != science.
