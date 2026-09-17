# KMQGB Research / Closure handoff — Iter504T terminal-review artifact-boundary repair

Date: 2026-09-17
Status: TERMINAL_HANDOFF

## STATE_READ

- Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark` only.
- Starting `main`: `170813fee572e87d59b3f0fa29444249dfb1a4c6`.
- `CURRENT_BENCHMARK_FRONT` already carried the newest independent Critic qualification; `CURRENT_ACTIVE_FRONT_INDEX_2026-09-15.md` was stale and was reconciled first at commit `5d9ab0763d9ad64073e13b6ff9415a830483041b`.
- Latest prior terminal closure gate: `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_SEMANTICS_REPAIR_GATE`, historical emitted classification `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`.
- Latest independent Critic: `recovery/CRITICAL_REVIEW_ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_SEMANTICS_REPAIR_2026-09-17.md`, commit `7263accb799829fddef81c1b4759822261f8b8d4`, verdict `INVALID_IMPLEMENTATION`.
- Critic defect: required upstream terminal artifact absence/expiration/download failure could terminate Actions before the prospectively frozen BLOCKED classifier was reached.
- No same-object workflow was in progress before this gate was launched.
- Governance retained: `RQIR Core v1.0 = FROZEN`; D7-S2/D7-S3 NOT_CLOSED; D7-S4 PARTIAL_GLOBAL_NOT_CLOSED; terminal selectors forbidden; Candidate Gravity inactive; Paper IV not authorized.

## TARGET_GATE

`ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE`

## WHY_THIS_GATE

The preceding Critic exposed a high-information implementation blocker directly upstream of any authority restoration: the frozen missing-artifact BLOCKED branch existed in Python but was unreachable through the authoritative Actions boundary. Repairing that branch without rerunning physics had high downstream unlock value and strong falsifiability at very low computational cost.

## PREREG

- Protocol: `research/prereg/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE_2026-09-17.md`.
- Prospective preregistration commit: `4a5f7d1c651527249b2831b6886cd502dc18e648`.
- Frozen authority ledger: `inputs/iter504t_repair_rerun_terminal_authority_review_artifact_boundary_repair_authority.json`.
- Authority commit: `fbfca6f932dd540898de3d9d738e9f953de8ac84`.
- Frozen PASS: `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`.
- Frozen FAIL: `ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED`.
- Frozen BLOCKED: `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.
- Frozen INVALID: `INVALID_IMPLEMENTATION`.
- The underlying scientific roots/rhos/R/channels/precision/threshold/floor/MAX_DEPTH, science labels and interpretation ceiling were unchanged.
- Frozen workflow-boundary positive control required a real download attempt for nonexistent artifact `iter504t-boundary-control-definitely-missing` to fail nonzero yet reach the BLOCKED classifier rather than abort CI.

## WORK_PERFORMED

- Reconciled stale active-front recovery before substantive work.
- Prospectively froze full gate and authority before implementation/result.
- Added `code/iter504t_artifact_boundary_collect.py` to query exact-run/artifact metadata and perform downloads without process abort on missing artifacts.
- Added a repaired boundary reviewer that maps missing/unavailable/download-failed required artifact to BLOCKED and present frozen identity mismatch to INVALID before invoking the inherited exact reviewer.
- Added independent Python 3.11/3.13 lanes with `fail-fast:false` and an independent real workflow-boundary missing-artifact control job.
- Added an aggregate requiring lane classification/decision agreement plus successful boundary-control evidence.
- Launched only this gate at workflow head `4e9a6ac95a10f89ba57eaa3aaa642a43e0236866`.
- Consumed no substantive lane result before run `35238357310` terminalized.
- After terminalization, downloaded only the aggregate artifact, independently rehashed its ZIP and internal JSON/log, and recorded the terminal outcome without changing frozen criteria.
- Performed one post-terminal diagnostic diff to localize the lane decision-SHA disagreement; this diagnostic did not alter classification.

## RESULT

Authoritative Actions run `35238357310` terminalized `completed/success`.

Jobs:

- source-lock `105260048120` — success;
- boundary-control `105260104164` — success;
- Python 3.11 `105260104179` — success;
- Python 3.13 `105260104162` — success;
- aggregate `105260195631` — success.

Artifacts:

- boundary control `10503972713`, digest `sha256:ea0edd702d8af7a525d88b3550753c805fa38cac78d9d1cdcede8bdae0fb2fb0`;
- Python 3.11 `10504281712`, digest `sha256:4103bd065f9351c021f2bf110088a9015cc1c0867f90877219badc1803a86c6c`;
- Python 3.13 `10504046837`, digest `sha256:61e8da2c5327bf225d127f5ba32898c9c85adb3daad32bfb358039fbc919e80a`;
- aggregate `10504616531`, digest and independently rehashed ZIP SHA256 `sha256:89619364918da0e663eaef9d882427a30392e11d441545d17585843596453987`.

Raw aggregate hashes:

- JSON SHA256 `823026fc00dcdddff765848f9513cdbf5a26ef7794288738662f4fcc7d4cb7f8`;
- log SHA256 `38790856fdec7d1e5751b3780b3260d8e4bfc36194e5c84e0caa765234a939d0`;
- aggregate decision SHA256 `09306cd3fc13b599d000f2e937ccdcf1c1bbf219d339a0396c06ac6a2d8624bb`.

Workflow-boundary control:

- actual `gh run download` attempted against nonexistent artifact;
- return code `1`;
- recorded state `MISSING_OR_UNAVAILABLE`;
- classifier reached successfully;
- classification `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`;
- aggregate confirms both `workflow_boundary_actual_download_failure_observed=true` and `workflow_boundary_missing_artifact_control_blocked=true`.

Production lanes:

- both independently classify `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`;
- all five required upstream artifacts are present and exact frozen identities match;
- inherited semantics/boundary controls all pass;
- both independently recompute `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- unresolved leaves = `0`; terminal leaves = `12`;
- C1 = `18` records / `70,056` booleans / zero false;
- no actual C4 violation.

Frozen aggregate failure:

- lane classifications agree = `true`;
- lane 3.11 review decision SHA256 `4eec7f2966d9c0df79fdf381c73e88d5cc45acbb6a688f68f78616937e17ff96`;
- lane 3.13 review decision SHA256 `c12de65d9c2d0a065230198ecab78f09ecb43148ee0c45a130636a8f74144de5`;
- exact lane decision SHA agreement = `false`;
- aggregate therefore emits `INVALID_IMPLEMENTATION`.

Terminal diagnostic localization: exactly seven lane-payload fields differ — five local filesystem paths (`terminal_311/...` versus `terminal_313/...`), the resulting manifest SHA, and the resulting review-decision SHA. After removing only those environment-local path-derived fields, lane payloads are identical and share normalized SHA256 `a7eda65e7407e7188ae67763df01f40187fd7659531f5bb24f29187e8bac11d0`.

## CLASSIFICATION

`INVALID_IMPLEMENTATION`

This is not scientific FAIL, not numerical disagreement, and not evidence against the underlying three-root result.

## NEW_FACT

The prior independent Critic's artifact-boundary counterexample has been genuinely closed at the authoritative execution boundary: an actual missing-artifact download failure now reaches the frozen BLOCKED classifier instead of terminating CI. The new gate exposes a narrower defect in the repaired review implementation: cross-environment decision hashing includes environment-specific local download paths, causing artificial SHA disagreement despite substantive lane equality.

Thus the remaining same-object blocker is decision canonicalization, not artifact availability semantics and not physics.

## CLAIM_CEILING

This gate does not issue authority-restoration PASS because its own prospectively frozen aggregate control failed. Exact repair run `35205054496` remains coherent supporting evidence only. No all-1888 closure, D7 closure, model/family failure, terminal selector, Candidate Gravity activation, Paper IV authorization, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.

Historical C4 remains `CONFIRMED_SCOPED` for the reusable scientific-validator path; all historical FAIL/BLOCKED/INCONCLUSIVE/INVALID results remain immutable.

## FILES/ARTIFACTS

- `research/prereg/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE_2026-09-17.md`;
- `inputs/iter504t_repair_rerun_terminal_authority_review_artifact_boundary_repair_authority.json`;
- `code/iter504t_artifact_boundary_collect.py`;
- `code/iter504t_repair_rerun_terminal_authority_review_artifact_boundary_repair.py`;
- `code/iter504t_repair_rerun_terminal_authority_review_artifact_boundary_repair_aggregate.py`;
- `.github/workflows/iter504t-repair-rerun-terminal-authority-review-artifact-boundary-repair.yml`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_CANONICAL_2026-09-17.json`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_ACTIONS_AGGREGATE_RAW_2026-09-17.log`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_HASHES_2026-09-17.json`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_TERMINAL_2026-09-17.md`;
- Actions run `35238357310` and artifact IDs/digests listed above.

## COMMITS

- active-front reconciliation before gate: `5d9ab0763d9ad64073e13b6ff9415a830483041b`;
- preregistration: `4a5f7d1c651527249b2831b6886cd502dc18e648`;
- authority: `fbfca6f932dd540898de3d9d738e9f953de8ac84`;
- artifact collector: `bb99b03fe4ea5f6e5e3950ca32191ba55e87c6e1`;
- boundary reviewer: `8f0a72165479b870405bb51478a64e607777502b`;
- aggregate code: `2f4207d0c69f280fbe63fec4c75b45aec0041562`;
- workflow head: `4e9a6ac95a10f89ba57eaa3aaa642a43e0236866`;
- canonical result: `559778f5d80f28429c495ce54a28b0f9ecdfa468`;
- exact aggregate raw log: `ccd681adeedd83bf6fad0b929efa701e8846215f`;
- hashes/provenance: `d99fe2a3fec6816c0e8f07196ec476bda23d6118`;
- terminal result: `4b14a017ff792fa6ec199b137f3fe15b586844a4`;
- current-front reconciliation: `fb2e5205cd098589d6a6dc137d67058257cf150b`;
- active-front reconciliation after result: `39a467202ab66a3c6fbf5efc1383898d2312edaf`.

## OPEN_BLOCKERS

1. The latest gate is `INVALID_IMPLEMENTATION` because environment-local paths enter the review-decision hash and break frozen cross-environment exact-SHA agreement.
2. No independent Critic review of this new terminal gate is yet recorded.
3. C4 remains confirmed for the reusable scientific-validator path.
4. Exact run `35205054496` remains only coherent supporting evidence until a contract-valid authority-restoration path closes.
5. No Iter504T result is all-1888 closure.
6. D7-S2/S3/S4 obligations remain open as recorded in current fronts.

## NEXT_RECOMMENDED_GATE

Prospectively freeze one same-object decision-canonicalization repair only.

Its exact object should be the cross-environment decision projection. Environment-local path strings and hashes derived solely from those local paths must be excluded from the decision SHA, while immutable run/head, artifact name/id/digest, downloaded file-content SHA256, artifact boundary state, inherited substantive review decision and all C1/C3/C4/R/rho/root/channel/science controls remain bound.

Mandatory positive control: place identical frozen artifact bytes under two deliberately different local directory prefixes and require identical decision SHA. Mandatory negative controls: mutate artifact id, digest, content SHA or substantive review field and require changed/invalid decision. Preserve the now-working real missing-artifact `gh run download` failure → BLOCKED control. Do not rerun physics.
