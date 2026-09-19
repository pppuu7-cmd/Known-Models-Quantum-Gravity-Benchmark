# Independent Critical Review — ITER504V Phase-B preterminal source status/provenance

Date: 2026-09-19
Lane: independent KMQGB Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## Result reviewed

Exactly one latest bounded terminal closure object:

- gate: `ITER504V_PHASE_B_PRETERMINAL_SOURCE_STATUS_PROVENANCE_GATE`;
- preregistration commit: `8737545156b2a64a514e28652bfe761a660cf575`;
- canonical result commit: `edcacbc400011063291a9cfbb879dadadfa91df9`;
- historical classification: `ITER504V_PHASE_B_PRETERMINAL_SOURCE_PROVENANCE_CONSISTENT_SCOPED`;
- exact source object: run `35405065903`, attempt 1, head `31fcdacffcc394e96b73917083281edb90d6753c`;
- canonical result SHA256 recorded by Research: `6f9cff143a11842f8c2bd349bc58fc4d7c2ec87944fdb0318ad9c0e03e81d4ad`.

This review does not consume any Phase-B source artifact bytes or substantive case/leaf/slope/drift/certification/assembly/aggregate/counterexample values.

## Preregistration chronology

The protocol was committed at `2026-09-19T05:11:26Z`. The canonical result was committed at `2026-09-19T05:12:08Z`. The frozen contract therefore predates the recorded metadata result.

The preregistration expressly bounds the object to one metadata observation and permits only run/job/artifact metadata. It forbids source artifact download/opening and scientific-value consumption. PASS is permitted only while the source run is nonterminal, source-lock is successful, every inspected artifact metadata record is exact-run/head-bound/non-expired/digested, no visible completed job in the inspected first page is failed/cancelled, and no science payload is consumed.

## Object / source / provenance check

The recorded source identity is exact and still matches GitHub Actions metadata:

- run `35405065903`;
- attempt `1`;
- head `31fcdacffcc394e96b73917083281edb90d6753c`;
- source-lock job `105792998164` is `completed/success`.

The six artifact IDs frozen in the historical result remain present in the authoritative run metadata with the same names, non-expired state, GitHub SHA256 digests, source run ID and source head. No artifact content was required or opened for this review.

The historical raw record explicitly limits its job statement to the connector first page and does not promote 30 visible jobs into a statement about the full 384-shard matrix. The terminal record likewise limits the result to one preterminal metadata observation. This scope discipline is essential to the verdict.

## Counterexample-first check and temporal scope

A decisive counterexample to any *persistent/current-state* interpretation now exists in fresh GitHub Actions metadata, but it does not invalidate the historically frozen one-observation claim.

At the historical canonical-result commit time (`05:12:08Z`), the first-page snapshot recorded 7 completed/success, 17 in-progress and 6 queued jobs, with zero visible failed/cancelled jobs. Fresh Actions metadata now shows first-page case jobs that later completed `cancelled`, including job `105793032797` (`cases (3.13, 0to5, b0, p1, q1)`, completed `2026-09-19T05:17:22Z`) and job `105793032807` (`cases (3.13, 0to5, b0, p0, q2)`, completed `2026-09-19T05:17:20Z`). These cancellations occurred roughly five minutes after the canonical result commit.

Therefore:

1. the historical one-observation statement is chronology-consistent and remains valid within its frozen instant/scope;
2. it must **not** be reused as authority that the source execution remains provenance-consistent at the current time;
3. current Actions state outranks recovery prose and now contains an outcome-independent infrastructure/provenance warning signal;
4. because the source run endpoint is still nonterminal (`queued / conclusion=null`) at the fresh read, no competing Phase-B scientific verdict is admissible.

Fresh run-artifact metadata has also advanced from the historical six records to 20 exposed metadata records. Several newly exposed artifacts were created after the cancellation transition. Their bytes were not opened. Their existence does not restore source completeness and must not be treated as terminal artifact authority.

## Frozen-contract verdict

`CONFIRMED_SCOPED`.

The terminal closure correctly represented the prospectively frozen metadata observation it actually made. Preregistration preceded observation; exact run/head/source-lock identity is bound; the six frozen artifact metadata records remain independently traceable to the exact run/head with the recorded digests; first-page limitation and claim ceiling are explicit; no scientific Phase-B classification was asserted.

The qualification is temporal: the historical PASS-class metadata observation has already been superseded by fresh Actions state containing visible cancelled source jobs. This is not a contradiction in the historical record because the cancellations postdate the result. It does mean the result cannot serve as current-source provenance authority.

## Governance / overclaim

No Phase-B source PASS/INCONCLUSIVE/INVALID scientific classification is created here. `cancelled` source jobs are not a physics FAIL. `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; green CI != science; partial artifacts != complete authority; scoped metadata closure != family/global closure.

`RQIR Core v1.0` remains FROZEN. D7 required subgates remain unclosed; terminal selectors remain forbidden; Candidate Gravity remains inactive; Paper IV remains unauthorized; no global quantum-gravity claim is authorized.

## Handoff

- `RESULT_REVIEWED = ITER504V_PHASE_B_PRETERMINAL_SOURCE_STATUS_PROVENANCE_GATE / historical result edcacbc400011063291a9cfbb879dadadfa91df9`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = PASS_SCOPED` — exact run 35405065903 / attempt 1 / head 31fcdacffcc394e96b73917083281edb90d6753c
- `SOURCE/REALIZATION_CHECK = PASS_SCOPED for the frozen observation; CURRENT_STATE_QUALIFIED by later cancellations`
- `PROVENANCE_CHECK = PASS_SCOPED for the six frozen metadata records; current execution now has visible cancelled jobs`
- `SAME_REALIZATION_CHECK = PASS_SCOPED` — all six frozen artifact metadata records still bind to the exact source run/head and recorded digest
- `NUMERICAL/STATISTICAL_CHECK = NOT_CONSUMED / NOT_APPLICABLE`
- `COUNTEREXAMPLE_ATTEMPTS = persistent/current-state interpretation REFUTED by later first-page cancelled jobs; historical one-observation interpretation survives because cancellations postdate result`
- `OVERCLAIM_CHECK = PASS_SCOPED`
- `VERDICT = CONFIRMED_SCOPED`
- `QUALIFICATIONS = historical metadata PASS is time-local only and is already superseded as a current-status statement; no source science payload consumed; no scientific FAIL`
- `UPDATED_STATE = historical preterminal provenance closure independently confirmed only for its frozen observation; fresh Actions metadata now exposes cancelled source jobs and 20 artifact metadata records while run endpoint remains nonterminal`
- `NEXT_ADMISSIBLE_GATE = while run 35405065903 remains nonterminal, provenance/status audit only. Do not reuse the old six-artifact PASS as current status, do not open partial artifact bytes, and do not launch a competing scientific gate. Once the source run becomes terminal, prospectively freeze exact terminal run/job/artifact identity before any substantive payload read; if terminal source completion is incomplete/cancelled, classify that execution only under the frozen implementation/provenance semantics, never as scientific FAIL.`
