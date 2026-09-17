# KMQGB Critical Review — Iter504T terminal-authority-review semantics repair

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Status: TERMINAL CRITIC REVIEW
Review-start main: `52002982a8a8fd55bc2221f0133f8907ebc44f6e`

## RESULT_REVIEWED

Exactly one latest terminal substantive closure result was reviewed:

- gate: `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_SEMANTICS_REPAIR_GATE`;
- prospective preregistration: `5b18ffbe46b967ef64c54d6181924aa8acf6f43e`;
- frozen authority: `39bd24ff03cba8858dca39ceb2935509352f295a`;
- repaired reviewer: `b0f9fa5f2efe1e1f09d72d33e78bbee904ad5eb5`;
- aggregate code: `311ac4169bd3fd8e0ce8b8ded1f8bc566db3cdeb`;
- workflow head: `71b1e197192c17d0c74e06fe7eb12b9b4b332f60`;
- authoritative Actions run: `35232311780`, terminal `completed/success`;
- historical Research/closure classification: `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`.

Historical emitted results remain immutable.

## PREREG_CHECK

PASS.

Chronology is prospective and clean: the semantics-repair preregistration and authority precede the repaired reviewer, aggregate implementation, workflow launch, and terminal result. The frozen repair is explicitly same-object: it does not change the underlying Iter504T scientific object, roots/rhos/R cohort, 243 channels, 384-bit precision, threshold `1/20`, robust floor `1`, `MAX_DEPTH=3`, original scientific PASS/INCONCLUSIVE labels, source realization, or claim ceiling.

The repaired gate prospectively requires all alternate semantics to remain distinct:

- complete valid zero-unresolved exact run -> exact-run authority PASS;
- complete valid nonzero-unresolved exact run -> original `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`;
- structurally insufficient or unavailable required terminal review object -> `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`;
- complete exact-run binding contradiction -> authority-restoration FAIL;
- authority/provenance/control implementation failure -> `INVALID_IMPLEMENTATION`.

In particular, the frozen BLOCKED clause explicitly includes any required terminal artifact that is unavailable, expired, missing, corrupted, or otherwise insufficient for independent recomputation without guessing.

## OBJECT_IDENTITY_CHECK

PASS_SCOPED for the actual exact-run replay.

The reviewer independently recomputes each per-rho predicate, recomputes each leaf certification as the conjunction of the four recomputed rho predicates, recomputes unresolved counts, preserves the exact original scientific INCONCLUSIVE label, verifies C1/C3/C4-relevant bindings, and checks the fixed roots/rhos/R/channel/threshold/floor/MAX_DEPTH identity.

The actual immutable run `35205054496` remains on the intended three-root local-D object. No all-1888, D7, family, selector, or Candidate Gravity promotion is present.

## SOURCE / REALIZATION CHECK

PASS_SCOPED for the actual successful execution.

The source-lock job verifies the exact underlying run id/head/status, required artifact ids/digests, latest independent Critic blob, prior review objects, and prospective chronology before substantive review lanes run. No source/version substitution was found in run `35232311780`.

However, the workflow-level treatment of a *missing required artifact* does not implement the frozen BLOCKED semantics; this is the decisive implementation defect below.

## PROVENANCE_CHECK

PASS for the observed terminal run.

Run `35232311780` is terminal `completed/success` at head `71b1e197192c17d0c74e06fe7eb12b9b4b332f60`. Jobs all succeeded:

- source-lock `105239292923`;
- Python 3.11 `105239369708`;
- Python 3.13 `105239369636`;
- aggregate `105239442328`.

Actions artifacts and independently rechecked ZIP SHA256 values:

- Python 3.11 artifact `10501567806`: `sha256:70f4a0b7b4e2e7ab60c42c5e83abeaa28dd2b55bc45bbace7d448e2ccbbe888e`;
- Python 3.13 artifact `10501033269`: `sha256:7ae9953cfc780230007eb326ab8fc5c13532a30bde12b7c41e08d1ed156093ec`;
- aggregate artifact `10501338087`: `sha256:cec9f4eaa6192d0a2defc57d117ae5de89cc7e9b5f9c77a2ec9403ea1d545fe4`.

Independent internal hashes also reproduce the recorded values: lane JSON `2f769095dfca88b00b02fd20d18dce726eb8b435f7d1af6bf7aa9728afa547cf` in both environments; lane log `da3eb8a08dc6dd87779c4ebb28e2789363f0d10c2bb74a5ba1ece9ac629c5e9d`; aggregate JSON `345642be3ad316d2c2cd704dce67670b41a364d78129411a1d8475b5a146ba23`; aggregate log `af7dcc5e9c4badae68b09479af9cd7da10ad837c40ecd68f0160e51a9a06c1c3`.

There is no basis for `INVALID_PROVENANCE` on the observed execution.

## SAME_REALIZATION_CHECK

PASS_SCOPED for the actual exact-run payload.

The semantics repair re-reviews the same immutable terminal repair run `35205054496` at head `10ae6bcc8447d14cecc6e550065504b23f792953`; no new physics execution or realization substitution occurs.

## NUMERICAL / STATISTICAL CHECK

PASS_EXACT_NONSTATISTICAL for the actual payload, subject to the implementation verdict below.

Both review lanes are byte-decision-identical and report:

- exact-run review classification `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`;
- underlying science `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- `12` terminal leaves;
- independently recomputed unresolved leaves `0`;
- C1 `18` records / `70,056` boolean components / `0` false;
- no C4 actual leaf-binding error;
- all eight implemented semantics controls true;
- no review errors.

Lane review decision SHA256 is `ab197395b971d3dc3c78574d4ae8176df839394ce902b72b126307b2674f604c`; aggregate decision SHA256 is `627836dc469c726c280d7b00c3ac46413724683fd05cc8759fbb185735230d61`.

These facts support the exact actual PASS path but do not cure a frozen alternate-branch implementation mismatch.

## COUNTEREXAMPLE_ATTEMPTS

### 1. Original scientific INCONCLUSIVE branch

REFUTED as a defect. The repaired reviewer now uses the exact original label `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`, and its frozen internally consistent unresolved fixture maps to that label rather than authority-restoration FAIL.

### 2. Missing structural field inside a successfully downloaded lane object

REFUTED as a defect. Removing `roots` from a parseable production-shaped lane object yields `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED` as frozen.

### 3. C4 / per-rho / R / C1 mutations

REFUTED as bypasses. The implemented fixtures correctly reject a true-leaf/false-rho contradiction, a serialized per-rho boolean contradiction, `R=6 -> 7`, and removal of a required C1 record. Artifact-identity mutation is routed to `INVALID_IMPLEMENTATION` in the classifier-level fixture.

### 4. Required terminal artifact unavailable or missing — explicit workflow counterexample SUCCEEDS

Frozen contract: if any required terminal artifact is unavailable, expired, missing, corrupted, or otherwise insufficient for independent recomputation without guessing, classification must be `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.

The Python reviewer contains a local-path missing-object BLOCKED handler. But the authoritative Actions workflow makes that branch unreachable for an actually missing upstream artifact:

1. `source-lock` queries run `35205054496` artifacts and executes shell `test` assertions for the exact id and digest of every required artifact under `set -euo pipefail`.
2. If, for example, required artifact `iter504t-repair-verdict` is absent/expired/unavailable in the upstream run, `got_id`/`got_digest` do not equal the frozen values and `source-lock` exits nonzero.
3. Both substantive lanes have `needs: source-lock` with no failure-path invocation of the repaired reviewer, so they are skipped rather than emitting the frozen BLOCKED result.
4. Even if metadata survived source-lock but `gh run download ... --name <required artifact>` failed, the lane step is under `set -euo pipefail`; execution aborts before Python receives a missing path and before its BLOCKED handler can run.
5. Aggregate requires successful lanes, so no terminal semantic classification is produced.

Thus the authoritative workflow converts a prospectively frozen **missing required terminal artifact => BLOCKED** branch into CI failure / no gate verdict. The implemented synthetic `missing_required_field_maps_to_blocked` control exercises a different case — deleting `roots` from an already downloaded parseable object — and cannot detect this workflow-level counterexample.

This is an outcome-independent frozen-contract mismatch. It does not claim that any artifact was actually missing in successful run `35232311780`.

### 5. Green CI promoted to science

Rejected. The observed run is green and provenance is sound, but successful CI does not repair the missing-artifact branch mismatch.

## OVERCLAIM_CHECK

PASS after qualification.

The historical terminal semantics-repair PASS is exact-run scoped and does not overclaim all-1888/D7/family/global closure. Historical C4 remains retained for the reusable launch-head validator. This Critic does not assert the underlying three-root scientific PASS is false.

## VERDICT

`INVALID_IMPLEMENTATION`

The semantics-repair implementation still does not satisfy its prospectively frozen BLOCKED contract at the authoritative workflow boundary. A required upstream terminal artifact being unavailable/missing cannot produce the required BLOCKED label because source-lock/download fail before the reviewer executes.

This is implementation invalidity of the review gate, not scientific FAIL and not observed-run provenance failure.

## QUALIFICATIONS

1. The two defects from the prior independent Critic — wrong INCONCLUSIVE label and structural-field BLOCKED misrouting — are genuinely repaired.
2. Actual run `35232311780` has complete provenance and all required upstream artifacts were present; the decisive counterexample concerns required alternate-branch semantics, not observed artifact absence.
3. The actual exact-run replay remains internally coherent: both lanes independently recover zero unresolved leaves and the frozen three-root scientific PASS.
4. Historical result `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED` is not rewritten; it remains immutable Actions/repository history but is not independently confirmed as a fully contract-valid semantics-repair gate.
5. Underlying exact-run scientific PASS may still be correct; this verdict does not establish its negation.
6. C4 remains `CONFIRMED_SCOPED` for the reusable launch-head validator path.

## UPDATED_STATE

- latest terminal semantics-repair gate run `35232311780`: historical closure classification `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`; independent Critic `INVALID_IMPLEMENTATION`;
- observed execution provenance: PASS;
- exact actual three-root replay: coherent diagnostic/supporting evidence, not a fully contract-validated authority-restoration result under this gate;
- prior historical reviews/results remain immutable;
- `RQIR Core v1.0 = FROZEN`;
- D7 required subgates remain unclosed; terminal selectors remain forbidden;
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`.

## NEXT_ADMISSIBLE_GATE

A same-object implementation repair is admissible without rerunning physics or changing the scientific contract:

1. make upstream artifact absence/expiration/download failure reach a classifier path that emits `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED` rather than failing the workflow before classification;
2. add a prospectively frozen outcome-sensitive control that exercises a genuinely missing required terminal artifact at the workflow/reviewer boundary, not only a missing field inside a downloaded JSON payload;
3. retain the now-correct original INCONCLUSIVE branch, structural-field BLOCKED branch, C4/per-rho/R/C1 controls, exact source/artifact locks, and interpretation ceiling;
4. preserve historical run `35232311780` unchanged.

Any change to underlying science object, thresholds, roots/rhos/R cohort, classifier meaning, source realization, or interpretation ceiling requires a new prospectively frozen gate.