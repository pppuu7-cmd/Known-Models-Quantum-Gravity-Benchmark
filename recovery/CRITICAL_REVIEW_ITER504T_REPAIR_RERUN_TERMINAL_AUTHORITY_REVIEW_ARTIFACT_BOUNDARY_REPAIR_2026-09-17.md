# KMQGB Critical Review — Iter504T terminal-review artifact-boundary repair

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Status: TERMINAL CRITIC REVIEW

## RESULT_REVIEWED

Exactly one latest substantive terminal closure result was reviewed:

- gate: `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE`;
- preregistration: `4a5f7d1c651527249b2831b6886cd502dc18e648`;
- frozen authority: `fbfca6f932dd540898de3d9d738e9f953de8ac84`;
- artifact collector: `bb99b03fe4ea5f6e5e3950ca32191ba55e87c6e1`;
- boundary reviewer: `8f0a72165479b870405bb51478a64e607777502b`;
- aggregate: `2f4207d0c69f280fbe63fec4c75b45aec0041562`;
- workflow head: `4e9a6ac95a10f89ba57eaa3aaa642a43e0236866`;
- authoritative Actions run: `35238357310`, terminal `completed/success`;
- historical terminal classification: `INVALID_IMPLEMENTATION`.

The historical result is not rewritten by this audit.

## PREREG_CHECK

PASS.

Chronology is prospective and clean:

`5d9ab076...` reconciled parent -> `4a5f7d1...` preregistration -> `fbfca6f...` authority -> `bb99b03...` collector -> `8f0a721...` reviewer -> `2f4207d...` aggregate -> `4e9a6ac...` workflow.

The frozen contract preserves the immutable Iter504T repair run `35205054496`, the prior semantics controls, the original scientific PASS/INCONCLUSIVE meanings and the interpretation ceiling. The new question is only the terminal-review artifact boundary.

The preregistration requires independent Python 3.11/3.13 lanes to reproduce the same terminal review decision. It does not make execution-local filesystem prefixes scientific or decision-critical objects. Therefore a cross-environment comparison must implement a canonical decision projection that is invariant to such local paths while remaining sensitive to immutable artifact/science/provenance identities.

## OBJECT_IDENTITY_CHECK

PASS_SCOPED.

No new physics object is introduced and no physics is recomputed by this gate. The production review consumes exactly the five frozen upstream terminal artifacts from immutable repair run `35205054496` at head `10ae6bcc8447d14cecc6e550065504b23f792953`.

The reviewed object is therefore the correctness of the terminal-review artifact boundary and its cross-environment decision projection, not an all-1888 result, D7 closure or a new physical model.

## SOURCE/REALIZATION_CHECK

PASS_SCOPED.

The authority ledger fixes the exact upstream run/head, required artifact names/IDs/digests, roots `[13,14,15]`, rhos `[0.35,0.9,1.6,2.7]`, R cohort `[6,8,10,12]`, 243 channels, 384-bit precision, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, scientific labels and claim ceiling.

No source/version substitution, threshold change, realization change or alternate run enters the terminal execution.

## PROVENANCE_CHECK

PASS.

Fresh Actions state confirms run `35238357310` is terminal `completed/success` at head `4e9a6ac95a10f89ba57eaa3aaa642a43e0236866`. All five jobs completed successfully:

- source-lock `105260048120`;
- boundary-control `105260104164`;
- Python 3.11 lane `105260104179`;
- Python 3.13 lane `105260104162`;
- aggregate `105260195631`.

Fresh Actions artifact identities:

- boundary control `10503972713`, ZIP digest `sha256:ea0edd702d8af7a525d88b3550753c805fa38cac78d9d1cdcede8bdae0fb2fb0`;
- Python 3.11 `10504281712`, ZIP digest `sha256:4103bd065f9351c021f2bf110088a9015cc1c0867f90877219badc1803a86c6c`;
- Python 3.13 `10504046837`, ZIP digest `sha256:61e8da2c5327bf225d127f5ba32898c9c85adb3daad32bfb358039fbc919e80a`;
- aggregate `10504616531`, ZIP digest `sha256:89619364918da0e663eaef9d882427a30392e11d441545d17585843596453987`.

All four ZIPs were independently downloaded and rehashed by this Critic; every local ZIP SHA256 matched the Actions digest. Aggregate internal JSON/log hashes also reproduce the recorded `823026fc00dcdddff765848f9513cdbf5a26ef7794288738662f4fcc7d4cb7f8` and `38790856fdec7d1e5751b3780b3260d8e4bfc36194e5c84e0caa765234a939d0`.

There is no `INVALID_PROVENANCE` basis.

## SAME_REALIZATION_CHECK

PASS_SCOPED.

Both production lanes consume the same immutable artifact IDs/digests and the same extracted file contents. The inherited exact-review JSON emitted in the two lane artifacts is byte-identical; independent SHA256 is `448508a79f77980b969dc156222a8872a18fd0467247501225131e5b0c9ecaee`.

Both inherited reviews classify `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`, report all inherited semantics controls true and independently recompute the same original science label `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED` with zero unresolved leaves across 12 terminal leaves.

## NUMERICAL/STATISTICAL_CHECK

PASS_EXACT_NONSTATISTICAL for the bounded object.

This gate does not introduce a statistical threshold or floating decision. The underlying exact-run supporting payload remains coherent: 12 terminal leaves, zero unresolved leaves, C1 `18` records / `70,056` component booleans / zero false, and no actual C4 contradiction. These facts remain supporting evidence only; this Critic does not promote them beyond the frozen exact-run scope.

## COUNTEREXAMPLE_ATTEMPTS

### 1. Prior workflow-boundary missing-artifact counterexample — REFUTED / CLOSED

The new workflow executes an actual `gh run download` request for deliberately nonexistent artifact `iter504t-boundary-control-definitely-missing`. The command returns exit code `1`, the job continues, the manifest records `MISSING_OR_UNAVAILABLE`, and the same frozen boundary classifier emits `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.

Thus the specific defect found by the preceding Critic is genuinely closed at the authoritative Actions boundary.

### 2. Cross-environment path-invariance counterexample — SUCCESS

The two production lanes use identical immutable upstream artifact identities and identical extracted file-content SHA256 values, and their inherited substantive review JSON is byte-identical. Nevertheless their outer `review_decision_sha256` values differ:

- Python 3.11: `4eec7f2966d9c0df79fdf381c73e88d5cc45acbb6a688f68f78616937e17ff96`;
- Python 3.13: `c12de65d9c2d0a065230198ecab78f09ecb43148ee0c45a130636a8f74144de5`.

Independent structural diff finds exactly seven differences in the two outer lane JSON payloads:

1. five `artifact_manifest.entries[*].local_path` strings (`terminal_311/...` versus `terminal_313/...`);
2. `artifact_manifest.manifest_sha256`, which hashes those local paths;
3. the final `review_decision_sha256`, which hashes the whole outer payload.

Removing only those environment-local path-derived fields makes the two canonical payloads exactly equal. Independent recomputation reproduces normalized SHA256 `a7eda65e7407e7188ae67763df01f40187fd7659531f5bb24f29187e8bac11d0` in both lanes.

This is an explicit counterexample to the implementation's decision projection: the same scientific/provenance decision transported through two harmless local directory prefixes is treated as two different decisions.

### 3. Artifact identity/content mutation sensitivity

No counterexample found in the terminal evidence. The repaired boundary continues to distinguish missing/unavailable artifacts from present identity mismatch, and the inherited exact reviewer retains the existing artifact-identity, C1/C3/C4, R/rho/root/channel/science checks.

## OVERCLAIM_CHECK

PASS.

The terminal result correctly states that the observed failure is not scientific FAIL or numerical disagreement and does not negate the three-root calculation. No all-1888 closure, D7 closure, family/model failure, selector, Candidate Gravity activation, Paper IV authorization or global quantum-gravity claim is made.

One wording qualification is important: the prospectively frozen requirement is equality of the terminal review **decision** across environments. Exact SHA equality of a payload containing execution-local paths was an implementation choice for enforcing that requirement, not a scientific identity requirement in its own right. The implementation choice is precisely what is defective.

## VERDICT

`CONFIRMED_SCOPED`

The historical terminal classification `INVALID_IMPLEMENTATION` is independently confirmed for this exact artifact-boundary-repair gate.

The reason is narrow and reproducible: the gate successfully repaired the missing-artifact BLOCKED boundary, but its cross-environment decision hash is not canonical because it includes execution-local filesystem paths and a manifest hash derived from those paths. Consequently a harmless environment-local path change produces false decision disagreement.

This Critic confirms implementation invalidity of the gate; it does not assert scientific falsification of the underlying Iter504T three-root result.

## QUALIFICATIONS

1. The previous workflow-boundary missing-artifact defect is genuinely closed.
2. Both production lanes substantively agree and their inherited review payloads are byte-identical.
3. The new defect is canonicalization/decision-projection invalidity, not numerical disagreement.
4. Historical run `35238357310` and its `INVALID_IMPLEMENTATION` classification remain immutable.
5. The exact repair run `35205054496` remains coherent scoped supporting evidence, not upgraded authority by this invalid gate.
6. Historical C4 remains independently `CONFIRMED_SCOPED` for the reusable scientific-validator path.
7. Governance remains unchanged: `RQIR Core v1.0 = FROZEN`; D7-S2/S3 are not closed; D7-S4 remains partial; terminal selectors remain forbidden; Candidate Gravity remains inactive; Paper IV remains not authorized.

## UPDATED_STATE

- `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE = INVALID_IMPLEMENTATION` historically, independently `CONFIRMED_SCOPED` by Critic.
- Missing-artifact download failure -> BLOCKED is now execution-verified and should be retained.
- Cross-environment outer decision hashing remains invalid because it is path-sensitive.
- No scientific/family/D7/global upgrade follows.

## NEXT_ADMISSIBLE_GATE

Prospectively freeze one same-object decision-canonicalization repair only; do not rerun physics.

The decision projection must exclude execution-local `local_path` strings and hashes derived solely from those path strings, while retaining and binding:

- immutable upstream run/head identity;
- artifact role/name/id/digest;
- downloaded artifact file-content SHA256;
- artifact boundary state;
- inherited substantive review decision and exact-run science recomputation;
- all C1/C3/C4/R/rho/root/channel/threshold/floor/MAX_DEPTH controls;
- the now-working real missing-artifact download-failure -> BLOCKED control;
- the same interpretation ceiling.

Mandatory positive control: identical frozen artifact bytes placed under at least two deliberately different local directory prefixes must produce the identical canonical decision SHA.

Mandatory negative controls: mutation of any artifact ID, digest, downloaded content SHA or substantive review field must change or invalidate the canonical decision.

Any change to the scientific object, immutable repair run, source realization, science classifier, thresholds or interpretation ceiling requires a new prospectively frozen scientific gate rather than a canonicalization repair.