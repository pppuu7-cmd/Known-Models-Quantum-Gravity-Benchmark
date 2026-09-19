# ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_PROVENANCE_GATE

Date: 2026-09-19
Lane: KMQGB Research / Closure
Status: PROSPECTIVELY FROZEN BEFORE RESULT

## HYPOTHESIS

Given the immutable Phase-B source workflow and already-established presence of required case-matrix jobs whose numerical step terminated `cancelled`, determine whether the workflow dependency/condition graph can still produce the two complete environment assemblies and final aggregate for the same run without accepting cancelled/incomplete shards. The primary hypothesis is that at least one required cancelled matrix child makes the normal assembly/aggregate authority path unreachable or skipped in this attempt.

## EXACT OBJECT

Only orchestration/provenance structure of authoritative source run `35405065903`, attempt 1, immutable launch head `31fcdacffcc394e96b73917083281edb90d6753c`, plus the exact immutable workflow `.github/workflows/iter504v-phase-b-science.yml` at that launch head and GitHub job/step status metadata. No artifact ZIP bytes and no substantive case/leaf/slope/drift/certification/assembly/aggregate/counterexample values may be opened or consumed.

## DEPENDENCY

Depends on Phase-B prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`, execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`, immutable launch head `31fcdacffcc394e96b73917083281edb90d6753c`, and terminal provenance facts that some required case jobs are `completed/cancelled` with `Execute frozen quartile shard = cancelled` while upload may still succeed. This gate does not alter any scientific criterion.

## SOURCE / REALIZATION AUTHORITY

GitHub `main`, immutable launch-head workflow source, Actions run/job/step metadata for exact run `35405065903`, and existing terminal provenance records only. Fresh GitHub state outranks recovery snapshots.

## FROZEN INPUTS

- run `35405065903`, attempt 1;
- launch head `31fcdacffcc394e96b73917083281edb90d6753c`;
- workflow path `.github/workflows/iter504v-phase-b-science.yml` at that head;
- no artifact downloads;
- no substantive source-science payload reads;
- no rerun/restart/competing same-object science execution;
- inspect only dependency expressions, job conditions, job/step statuses, and artifact metadata if needed.

## POSITIVE CONTROLS

1. `source-lock` must remain `completed/success`.
2. At least one case shard must show `job.conclusion=success` and `Execute frozen quartile shard=success`, proving the workflow can complete a shard normally.
3. The workflow must contain explicit assembly/aggregate jobs or equivalent downstream authority path whose dependency/condition semantics can be inspected.

## NEGATIVE CONTROLS

1. At least one required case-matrix job must be `completed/cancelled` with its frozen numerical execution step `cancelled`.
2. An uploaded artifact from such a cancelled job must not be treated as evidence that the dependency itself succeeded.
3. No conclusion may be drawn from substantive artifact contents.

## PASS

Classify `ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_VERIFIED_SCOPED` iff the immutable workflow semantics plus exact run metadata show that one or more required cancelled matrix children prevent the same attempt from reaching a valid complete two-environment assembly/final aggregate authority path, while successful-shard positive controls remain intact.

## FAIL

Classify `ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_REFUTED_SCOPED` iff the immutable workflow explicitly permits downstream assembly/aggregate execution despite cancelled required shard jobs *and* independently requires/reconstructs exactly 192 successful-complete shards per environment so that cancelled artifacts cannot satisfy completeness.

## BLOCKED / INVALID

BLOCKED if exact launch-head workflow or necessary job dependency metadata cannot be read unambiguously. INVALID if this gate consumes substantive science payload, changes the frozen Phase-B scientific object/criteria, relies on a competing run, or cannot distinguish cancelled execution from successful completion.

## INTERPRETATION CEILING

This gate may classify only workflow orchestration/provenance reachability for this exact source attempt. It cannot classify Phase-B physics, cannot convert cancellation/timeout/incomplete execution into scientific FAIL, cannot assert any case value is wrong, cannot authorize a producer rerun, and cannot promote to all-Iter504, family, D7, Candidate Gravity, Paper IV, or global quantum-gravity claims.
