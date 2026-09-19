# ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_GATE — preregistration

Date: 2026-09-19
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Lane: KMQGB Research / Closure

## HYPOTHESIS
The newly observed cancelled Iter504V Phase-B case jobs are caused by the frozen numerical shard step exceeding the GitHub Actions job execution-time limit (or an equivalent explicit timeout/cancellation condition visible in job logs), rather than by a scientific condition. If verified, this makes those jobs implementation/provenance-incomplete and their uploaded artifacts ineligible for scientific authority regardless of artifact presence/digest.

## exact OBJECT
Metadata/log provenance only for authoritative source run `35405065903`, attempt 1, immutable head `31fcdacffcc394e96b73917083281edb90d6753c`: source-lock; currently visible cancelled case jobs; their job timestamps/steps/logs; and one or more visible successful case-job positive controls. No artifact ZIP bytes and no case/leaf/slope/drift/certification/assembly/aggregate/counterexample values may be opened.

## DEPENDENCY
Depends on the independently confirmed cancelled-job artifact provenance result `171d8ee9b0945de095ed9f5cbc1f9296aa2007fc = CONFIRMED_SCOPED`, which established that cancelled numerical execution can still be followed by successful artifact upload.

## SOURCE / REALIZATION AUTHORITY
Exact source execution authority: Phase-B prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`; execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`; source launch/head `31fcdacffcc394e96b73917083281edb90d6753c`; run `35405065903`, attempt 1. Fresh GitHub Actions metadata/logs outrank recovery snapshots.

## FROZEN INPUTS
- run/head above;
- first-page jobs from fresh post-prereg read, plus direct logs/step metadata for cancelled jobs selected deterministically by ascending job id, up to the first 6 visible cancelled case jobs;
- first visible successful case job by ascending job id as positive control;
- source-lock job `105792998164`;
- no artifact bytes.

## POSITIVE CONTROLS
1. Source-lock remains `completed/success`.
2. At least one successful case job shows frozen numerical execution step `success` and job conclusion `success`.
3. Job/log retrieval is internally consistent with exact run/head.

## NEGATIVE / ADVERSARIAL CONTROL
At least one cancelled case job must show the frozen numerical execution step cancelled/terminated and job conclusion cancelled; causal classification requires an explicit timeout/maximum-runtime/cancellation message in logs or a job duration consistent with the platform timeout together with such an explicit runner message.

## PASS
`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED` iff all positive controls pass and at least one selected cancelled case job has explicit log evidence that the numerical shard step/job was terminated by execution-time limit (or explicit platform timeout), with no scientific payload consumed.

## FAIL
`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_REFUTED_SCOPED` iff selected cancelled jobs have readable logs proving a different non-timeout cause while positive controls pass.

## BLOCKED
`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_BLOCKED_SCOPED` if logs/step metadata are unavailable or insufficient to distinguish timeout from another cancellation cause.

## INVALID
`INVALID_IMPLEMENTATION` if wrong run/head/jobs are inspected, selection is changed after observing results, or artifact/scientific payload is consumed.

## INTERPRETATION CEILING
Metadata/log provenance only. PASS or FAIL cannot classify Phase-B science, cannot make cancellation a scientific FAIL, cannot assert any case value is wrong, cannot authorize producer rerun while the source run remains nonterminal, and cannot promote any result to family/D7/Candidate-Gravity/global quantum-gravity closure.
