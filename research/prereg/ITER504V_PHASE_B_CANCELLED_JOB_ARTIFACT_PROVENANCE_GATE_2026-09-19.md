# ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE — prospective preregistration

Date: 2026-09-19
Lane: KMQGB Research / Closure
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`

## HYPOTHESIS

The active immutable Iter504V Phase-B source execution may expose a provenance/authority-path hazard in which a case job whose frozen numerical execution step is cancelled nevertheless reaches `actions/upload-artifact` successfully and leaves an artifact metadata record. If reproduced after this preregistration, terminal closure must never accept artifact presence/digest alone as evidence of a completed valid shard; it must bind every shard artifact to a successful case job and successful frozen execution step.

## EXACT OBJECT

Metadata-only audit of the single authoritative source execution:

- workflow run `35405065903`, attempt 1;
- immutable source head `31fcdacffcc394e96b73917083281edb90d6753c`;
- workflow `.github/workflows/iter504v-phase-b-science.yml`;
- source-lock job `105792998164`;
- GitHub run metadata;
- GitHub first-page job metadata including step conclusions;
- GitHub first-page artifact metadata only.

Artifact ZIP bytes and every case/leaf/slope/drift/certification/assembly/aggregate/counterexample payload are explicitly outside this gate and MUST NOT be downloaded or opened.

## DEPENDENCY

Depends on Phase-B prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`, one-source execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`, launch head `31fcdacffcc394e96b73917083281edb90d6753c`, and the independent preterminal review `1989e28d78fdddf2117c3b79b5f90af4bd752603` only as motivation to perform an outcome-blind metadata audit. This gate does not inherit a verdict from that review.

## SOURCE / REALIZATION AUTHORITY

GitHub/Actions metadata for exact run `35405065903` is the only execution authority. Repository `main` at gate freeze is navigation/governance context only. No chat history is authority.

## FROZEN INPUTS

1. exact run ID/attempt/head above;
2. run status/conclusion and source-lock status;
3. first-page case-job IDs, names, status/conclusion and step status/conclusion;
4. first-page artifact IDs, names, sizes, digests, expiry state and exact run/head binding;
5. no artifact-byte access;
6. no scientific-value access;
7. no producer rerun and no competing same-object gate.

## POSITIVE CONTROLS

- source-lock must still be `completed/success`;
- at least one visible case job with job conclusion `success`, frozen execution step conclusion `success`, upload-artifact conclusion `success`, and matching artifact metadata name should exist, demonstrating the metadata path can represent a normal successful shard;
- every inspected artifact metadata record must remain bound to exact run `35405065903` and exact head `31fcdacffcc394e96b73917083281edb90d6753c` and carry a GitHub SHA256 digest.

## NEGATIVE / ADVERSARIAL CONTROL

Search only the frozen first-page metadata for a visible case job satisfying all of:

1. job conclusion = `cancelled`;
2. frozen numerical step `Execute frozen quartile shard` conclusion = `cancelled`;
3. `Run actions/upload-artifact@v4` conclusion = `success`;
4. an artifact metadata record exists whose deterministic name corresponds to that job's `(python, causal, block, path, quartile)` identity;
5. artifact is non-expired, SHA256-digested, and bound to the same run/head.

No artifact content is required.

## PASS

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED` iff all positive controls pass and at least one exact cancelled-job -> successful-upload -> matching-artifact metadata chain is reproduced after this preregistration.

Interpretation of PASS: artifact existence/digest is insufficient evidence of a valid completed shard. Future terminal Critic must bind every required shard artifact to both `job.conclusion == success` and frozen execution-step conclusion `success`, in addition to the already-frozen shard.json/four-record/content checks.

## FAIL

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_NOT_REPRODUCED_SCOPED` iff the audit is complete for the inspected first page, all positive controls pass, but no exact cancelled-job -> successful-upload -> matching-artifact chain exists.

FAIL here is a methodology/provenance negative finding, not a physics/scientific FAIL.

## BLOCKED / INVALID

`BLOCKED_SCOPED` if current GitHub metadata cannot establish exact run/head/job/artifact binding, first-page job/step data needed for the chain are unavailable, or the run identity changed.

`INVALID_IMPLEMENTATION` if artifact bytes or substantive scientific values are consumed, the wrong run/head is inspected, criteria are changed after observation, or a competing source execution is launched.

## INTERPRETATION CEILING

This gate may establish only a scoped execution-provenance/authority-path fact about metadata emitted by run `35405065903`. It cannot classify Phase-B scientific PASS/INCONCLUSIVE/INVALID while the source run is nonterminal, cannot assert that any scientific case value is wrong, cannot convert cancellation into physics FAIL, and cannot promote to all-domain/model-family/D7/Candidate-Gravity/global quantum-gravity conclusions.

## GOVERNANCE

`RQIR Core v1.0 = FROZEN`. D7 terminal selectors remain forbidden; Candidate Gravity inactive; Paper IV not authorized. `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; green CI/artifact upload != science; partial artifact != terminal authority.
