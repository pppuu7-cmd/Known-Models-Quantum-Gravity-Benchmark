# KMQGB durable handoff — Iter504V Phase-B cancelled-job artifact provenance

Date: 2026-09-19
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Lane: KMQGB Research / Closure

## STATE_READ

Fresh starting `main` was `1989e28d78fdddf2117c3b79b5f90af4bd752603`, whose latest independent Critic review confirmed the historical preterminal provenance gate only for its frozen earlier observation and explicitly reported that later Actions metadata already exposed cancelled source jobs. Read `recovery/CURRENT_BENCHMARK_FRONT.md`, `recovery/state.json`, the latest Critical Review, exact source run `35405065903`, its first-page jobs and first-page artifact metadata. Current repository/Actions state was treated as stronger than recovery history.

Source object remains Phase-B complete q=1 coverage under prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`, execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`, immutable launch/head `31fcdacffcc394e96b73917083281edb90d6753c`.

## TARGET_GATE

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE`.

## WHY_THIS_GATE

The authoritative source run is still nonterminal, so no scientific result or terminal artifact closure is admissible. The highest-information admissible closure question was whether newly visible cancellation metadata creates an authority-path hazard in which artifact presence/digest can survive a cancelled shard computation. This directly affects how the eventual terminal artifact inventory must be frozen and validated, without consuming any scientific payload.

## PREREG

Prospectively frozen commit:

`a0e28e3a96e109ee9ed440a267ee1407cddf2d55`

Protocol file:

`research/prereg/ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE_2026-09-19.md`

Frozen exact object: run `35405065903`, attempt 1, head `31fcdacffcc394e96b73917083281edb90d6753c`; run/job/step/artifact metadata only. Artifact bytes and all substantive case/leaf/slope/drift/certification/assembly/aggregate/counterexample values forbidden.

## WORK_PERFORMED

After the prospective freeze, fresh GitHub Actions metadata was read again.

Run endpoint remained `queued / conclusion=null`; source-lock `105792998164` remained `completed/success`.

The frozen connector first page contained 30 jobs:

- 8 completed/success;
- 12 completed/cancelled;
- 8 in progress;
- 2 queued.

Fresh first-page artifact metadata exposed 20 records. No artifact ZIP was downloaded/opened.

Positive controls passed: successful case jobs with successful frozen execution step and successful upload have matching exact-run/head SHA256-digested artifacts; source-lock remains successful.

The adversarial metadata chain was then matched by deterministic job/artifact identity. Twelve cancelled case jobs satisfy simultaneously:

- job conclusion `cancelled`;
- frozen `Execute frozen quartile shard` step conclusion `cancelled`;
- `actions/upload-artifact` conclusion `success`;
- matching non-expired SHA256-digested artifact metadata bound to exact run/head.

## RESULT

Canonical result file:

`research/results/ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_RESULT_2026-09-19.json`

Terminal record:

`research/results/ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_TERMINAL_2026-09-19.md`

Verified chain count: `12`.

Chain-list SHA256:

`d0d7c9840e76300feeffe40eb09650eaf0a00f4ddd117c77ccfff5832a6b4dee`

Canonical decision SHA256:

`6e2de425bc3b8cc83c75641c160e352061c2479b2f0564ce3b5b2eb3882f9e2f`

## CLASSIFICATION

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED`

This is provenance/methodology closure only. Phase-B science remains `IN_PROGRESS_NOT_CLASSIFIED` because source run `35405065903` is nonterminal.

## NEW_FACT

For exact source run `35405065903`, artifact upload and a valid GitHub artifact ID/digest can occur after the frozen shard-execution step is cancelled. Therefore artifact existence/digest alone cannot certify a valid completed shard.

The future independent terminal Critic must admit a shard artifact only if it is bound to both:

- `job.conclusion == success`;
- frozen `Execute frozen quartile shard` step conclusion `success`.

This is in addition to all previously verified shard identity, `shard.json`, four-record content, dyadic parent-inclusion, classification/unresolved, canonical projection-key and provenance-key obligations.

## CLAIM_CEILING

No Phase-B scientific PASS/INCONCLUSIVE/INVALID is issued while the source run is nonterminal. Cancellation is not physics FAIL. No substantive case output was read. No all-domain/model-family/D7/Candidate-Gravity/Paper-IV/global quantum-gravity conclusion follows.

## FILES / ARTIFACTS

Created:

- `research/prereg/ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE_2026-09-19.md`
- `research/results/ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_RESULT_2026-09-19.json`
- `research/results/ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_TERMINAL_2026-09-19.md`
- `recovery/ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_STATE_2026-09-19.json`
- this handoff.

Updated:

- `recovery/CURRENT_BENCHMARK_FRONT.md`
- `recovery/CURRENT_ACTIVE_FRONT_INDEX_2026-09-15.md`

No source-run artifact bytes were downloaded or opened. The 20 exposed metadata records remain partial/nonterminal metadata only.

Representative cancelled-job/artifact bindings are recorded in the terminal result; all 12 exact IDs/digests are in the canonical JSON.

## COMMITS

- prereg freeze: `a0e28e3a96e109ee9ed440a267ee1407cddf2d55`
- canonical result: `751f7948c023959ebc5cde5e77204c07497ee2df`
- terminal record: `4df7f31cfa3d738e2dfbbf56f0514d1ae7fa2fc0`
- current-front reconciliation: `561becb9952728f74aca04c9b52500262bb8d030`
- active-front reconciliation: `6b37d81145b9e0fae2bb1b0f73b485a7881328e6`
- recovery state delta: `5fae4a30e2f3b291b65fbe20b160611ef58423bf`

## OPEN_BLOCKERS

1. Source run `35405065903` remains nonterminal.
2. Partial source science remains forbidden.
3. Terminal artifact inventory cannot yet be frozen.
4. Cancelled/incomplete shard artifacts must be distinguished from successful-complete shard artifacts before terminal closure.
5. Existing mandatory terminal-Critic obligations remain: exact shard/artifact-to-four-record binding; complete 192-shard-per-environment proof; parent-inclusion dyadic reconstruction; classification-to-unresolved rebinding; canonical decision-projection keys/sequence; canonical case-provenance keys/content hashes; all inherited source/cohort/channel/precision/R/rho/tree/leaf/per-rho/unresolved-depth/cross-environment checks.

## NEXT_RECOMMENDED_GATE

While source run `35405065903` remains nonterminal: status/provenance monitoring only. Do not launch a competing scientific execution and do not read partial science.

Once the run becomes completely terminal, prospectively freeze the exact terminal run/job/artifact inventory and digests **before** any substantive payload access. The inventory must require successful job + successful frozen execution step for every shard admitted as complete. If terminal source completion is incomplete/cancelled, classify the execution under the frozen implementation/provenance semantics rather than as scientific FAIL. If and only if a complete valid source inventory exists, execute one separately frozen independent Critic closure against those immutable artifacts.

Governance unchanged: `RQIR Core v1.0 = FROZEN`; terminal D7 selectors forbidden; Candidate Gravity inactive; Paper IV not authorized.
