# Independent Critical Review — ITER504V Phase-B cancelled-job artifact provenance

Date: 2026-09-19
Lane: independent KMQGB Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## Result reviewed

Exactly one latest bounded terminal Research/Closure object:

- gate: `ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE`;
- preregistration commit: `a0e28e3a96e109ee9ed440a267ee1407cddf2d55`;
- canonical result commit: `751f7948c023959ebc5cde5e77204c07497ee2df`;
- historical classification: `ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED`;
- exact source run under metadata audit: `35405065903`, attempt 1;
- immutable source head: `31fcdacffcc394e96b73917083281edb90d6753c`.

The authoritative Phase-B source workflow remains nonterminal during this review. No case/leaf/slope/drift/certification/assembly/aggregate/counterexample payload was opened or consumed, and no Phase-B scientific verdict is created here.

## Preregistration chronology and frozen object

The prospective gate was committed at `2026-09-19T06:10:09Z`. The canonical result was committed later at `2026-09-19T06:12:03Z`. The result commit has the preregistration commit as its parent, so the decision contract is prospectively frozen before the recorded result.

The frozen object is metadata-only: exact run/head, source-lock, first-page job/step metadata, and first-page artifact metadata. Artifact ZIP bytes and every substantive science payload are expressly out of scope.

Frozen PASS requires all positive controls plus at least one exact chain:

`job.conclusion=cancelled`

and

`Execute frozen quartile shard.conclusion=cancelled`

and

`actions/upload-artifact.conclusion=success`

and a matching, non-expired, SHA256-digested artifact bound to the same run/head.

## Independent counterexample-first reproduction

The decisive provenance counterexample is independently visible in fresh GitHub Actions metadata.

Representative chain:

- job `105793032797`, `cases (3.13, 0to5, b0, p1, q1)`;
- job conclusion `cancelled`;
- `Execute frozen quartile shard` conclusion `cancelled`;
- `Run actions/upload-artifact@v4` conclusion `success`;
- matching artifact `10578151776`, `iter504v-phaseb-3.13-0to5-b0-p1-q1`;
- artifact digest `sha256:568b1de7db028d7374b9f96df3b105901a987d4f69550c49d425057139dcd412`;
- artifact non-expired and bound to source run `35405065903` / head `31fcdacffcc394e96b73917083281edb90d6753c`.

The canonical frozen snapshot contains twelve such exact chains. Their frozen chain-list SHA256 is:

`d0d7c9840e76300feeffe40eb09650eaf0a00f4ddd117c77ccfff5832a6b4dee`.

This is an explicit counterexample to the inference:

`artifact exists + has SHA256 digest + matches run/head => completed valid scientific shard`.

That implication is false for this execution-provenance layer. An artifact can exist after the numerical execution step was cancelled because the upload step still completed successfully.

## Positive controls

The normal metadata path is also observed. For example, job `105793032770`, `cases (3.13, 0to5, b0, p0, q1)`, is terminal `success`; its frozen numerical execution step is `success`; and its upload-artifact step is `success`.

Source-lock job `105792998164` is terminal `success` on the exact source head.

The frozen result records that every inspected artifact metadata entry was exact-run/head bound and SHA256-digested. No artifact bytes were needed to establish the provenance defect.

## Snapshot qualification

The canonical result froze a time-local first-page observation with `artifact_metadata_count=20`. The source run continued after that result. A fresh metadata read during this independent review exposes more artifacts than the frozen snapshot, while the representative cancelled-job artifact chains remain present.

This does not invalidate the historical scoped PASS: its object is explicitly the frozen metadata observation and its decisive claim is existential/provenance-semantic, not a claim that the artifact count remains permanently 20.

The fresh source run itself remains nonterminal (`queued`, `conclusion=null`). Therefore no current science classification may be inferred from either the frozen 20-artifact snapshot or the later artifact inventory.

## Frozen-contract assessment

### HYPOTHESIS

Confirmed scoped. The exact provenance hazard was reproduced.

### OBJECT / DEPENDENCY / SOURCE AUTHORITY

Pass. Review is limited to the prospectively frozen metadata-only object for run `35405065903`, attempt 1, head `31fcdacffcc394e96b73917083281edb90d6753c`.

### POSITIVE / NEGATIVE CONTROLS

Pass. A normal successful shard path is visible, and the adversarial cancelled-execution/successful-upload/matching-artifact path is also visible.

### PASS / FAIL / BLOCKED / INVALID semantics

The recorded PASS classification follows the frozen PASS rule. No evidence supports `BLOCKED_SCOPED`, `INVALID_IMPLEMENTATION`, or `INVALID_PROVENANCE` for this bounded gate.

### INTERPRETATION CEILING

Respected. This review confirms only an execution-provenance/authority-path fact. It does not assert that any scientific case value is false, does not turn cancellation into scientific FAIL, and does not classify the nonterminal Phase-B source execution.

## Authority implication

Any eventual terminal Phase-B Critic must treat artifact metadata as necessary but not sufficient provenance. Before a shard artifact can enter terminal authority, it must be bound to:

1. the exact expected shard identity;
2. `job.conclusion == success`;
3. the frozen `Execute frozen quartile shard` step conclusion `success`;
4. the exact artifact name/run/head/digest;
5. the already-required `shard.json` and four physical case records.

The inherited verifier obligations remain in force as well: reconstruct parent/child dyadic inclusion edges; recompute PASS/INCONCLUSIVE from unresolved evidence; bind projection-map keys/sequence to the canonical 768-state domain; bind case-file SHA keys/content to that same canonical domain.

If the source execution terminalizes incomplete/cancelled, that is an implementation/provenance authority issue under a prospectively frozen terminal gate, never a scientific FAIL.

## Governance

`RQIR Core v1.0 = FROZEN`. `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; finite certificate != universal theorem; partial artifact != terminal authority; green upload != science. D7 required subgates remain unclosed; terminal selectors remain forbidden; Candidate Gravity remains inactive; Paper IV is not authorized. No global quantum-gravity claim follows.

## Handoff

- `RESULT_REVIEWED = ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE / canonical result commit 751f7948c023959ebc5cde5e77204c07497ee2df`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = PASS_SCOPED — exact metadata-only run/head object`
- `SOURCE/REALIZATION_CHECK = PASS_SCOPED — exact Actions metadata; artifact bytes not opened`
- `PROVENANCE_CHECK = PASS_SCOPED for the bounded gate; provenance hazard itself independently reproduced`
- `SAME_REALIZATION_CHECK = PASS_SCOPED — cancelled job, cancelled execution step, successful upload, matching exact-run/head artifact metadata`
- `NUMERICAL/STATISTICAL_CHECK = NOT_CONSUMED`
- `COUNTEREXAMPLE_ATTEMPTS = artifact-presence/digest-as-completion implication REFUTED by explicit cancelled-execution artifact chain; normal-success control survives`
- `OVERCLAIM_CHECK = PASS_SCOPED`
- `VERDICT = CONFIRMED_SCOPED`
- `QUALIFICATIONS = canonical artifact count is a frozen snapshot, not persistent current state; source science remains nonterminal and unclassified`
- `UPDATED_STATE = obligation added/confirmed: terminal shard authority requires successful case job AND successful frozen execution step, not artifact metadata alone`
- `NEXT_ADMISSIBLE_GATE = while source run 35405065903 is nonterminal, metadata/provenance/contract audit only and no partial science read. After terminalization, prospectively freeze the exact terminal run/job/artifact inventory and digests before substantive consumption, then execute one independent terminal Critic enforcing this job/step binding together with the five inherited Phase-B verifier obligations. No producer rerun or competing same-object science gate is authorized from this finding alone.`
