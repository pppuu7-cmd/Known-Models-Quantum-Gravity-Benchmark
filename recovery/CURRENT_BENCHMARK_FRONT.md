# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal closure result

Gate:

`ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE`

Terminal classification:

`INVALID_IMPLEMENTATION`

This is **not scientific FAIL**.

Authority / execution chain:

- reconciled starting main `5d9ab0763d9ad64073e13b6ff9415a830483041b`;
- prospective preregistration `4a5f7d1c651527249b2831b6886cd502dc18e648`;
- frozen authority `fbfca6f932dd540898de3d9d738e9f953de8ac84`;
- artifact collector `bb99b03fe4ea5f6e5e3950ca32191ba55e87c6e1`;
- repaired boundary reviewer `8f0a72165479b870405bb51478a64e607777502b`;
- aggregate code `2f4207d0c69f280fbe63fec4c75b45aec0041562`;
- workflow head `4e9a6ac95a10f89ba57eaa3aaa642a43e0236866`;
- authoritative Actions run `35238357310`, terminal `completed/success`;
- jobs: source-lock `105260048120`, boundary-control `105260104164`, Python 3.11 `105260104179`, Python 3.13 `105260104162`, aggregate `105260195631`;
- artifacts: boundary control `10503972713` / `sha256:ea0edd702d8af7a525d88b3550753c805fa38cac78d9d1cdcede8bdae0fb2fb0`; Python 3.11 `10504281712` / `sha256:4103bd065f9351c021f2bf110088a9015cc1c0867f90877219badc1803a86c6c`; Python 3.13 `10504046837` / `sha256:61e8da2c5327bf225d127f5ba32898c9c85adb3daad32bfb358039fbc919e80a`; aggregate `10504616531` / `sha256:89619364918da0e663eaef9d882427a30392e11d441545d17585843596453987`;
- aggregate JSON SHA256 `823026fc00dcdddff765848f9513cdbf5a26ef7794288738662f4fcc7d4cb7f8`;
- aggregate log SHA256 `38790856fdec7d1e5751b3780b3260d8e4bfc36194e5c84e0caa765234a939d0`;
- aggregate decision SHA256 `09306cd3fc13b599d000f2e937ccdcf1c1bbf219d339a0396c06ac6a2d8624bb`.

Green CI is provenance only.

## Exact result

The gate genuinely closes the workflow-boundary counterexample identified by independent Critic `7263accb799829fddef81c1b4759822261f8b8d4`:

- a deliberately nonexistent upstream artifact was requested through a real `gh run download` call;
- the download returned exit code `1`;
- CI continued rather than aborting;
- the state was recorded as `MISSING_OR_UNAVAILABLE`;
- the same frozen reviewer was reached and emitted `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`;
- aggregate records `workflow_boundary_actual_download_failure_observed=true` and `workflow_boundary_missing_artifact_control_blocked=true`.

Both production lanes independently replayed immutable repair run `35205054496` and each classified it `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`. All five required artifacts matched exact frozen IDs/digests, all inherited semantics controls passed, both lanes recomputed `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`, unresolved leaves were zero across 12 leaves, and C1 remained 18 records / 70,056 booleans / zero false with no actual C4 contradiction.

The gate is terminally `INVALID_IMPLEMENTATION` because its cross-environment decision projection hashes execution-local path strings. The two lane classifications and substantive inherited review payloads agree, but outer decision hashes differ:

- lane 3.11 decision SHA256 `4eec7f2966d9c0df79fdf381c73e88d5cc45acbb6a688f68f78616937e17ff96`;
- lane 3.13 decision SHA256 `c12de65d9c2d0a065230198ecab78f09ecb43148ee0c45a130636a8f74144de5`.

Independent Critic reconstruction finds exactly seven differences: five environment-specific `local_path` strings (`terminal_311/...` versus `terminal_313/...`), their path-derived manifest SHA, and the final outer review-decision SHA. Removing only those environment-local path-derived fields makes the lane payloads identical with normalized SHA256 `a7eda65e7407e7188ae67763df01f40187fd7659531f5bb24f29187e8bac11d0`.

The prospectively frozen requirement is equality of the terminal review decision across environments. Environment-local filesystem prefixes are not decision-critical scientific/provenance identity. Including them in the decision hash is therefore an implementation/canonicalization defect. This is not science, numerical disagreement, or physical falsification.

## Latest independent Critical Review

Audit:

`recovery/CRITICAL_REVIEW_ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_2026-09-17.md`

Critic commit:

`77357d92050a9bec2c8daefd4d4babf7ff032ed0`

Verdict:

`CONFIRMED_SCOPED`

The historical terminal classification `INVALID_IMPLEMENTATION` is independently confirmed for this exact gate. The preceding missing-artifact workflow-boundary defect is genuinely closed; the remaining defect is specifically noncanonical outer decision hashing. Both production lanes use identical immutable upstream artifacts and their inherited exact-review JSON is byte-identical (Critic SHA256 `448508a79f77980b969dc156222a8872a18fd0467247501225131e5b0c9ecaee`).

The Critic independently downloaded and rehashed all four current run artifacts; every ZIP SHA256 matched fresh Actions metadata. There is no `INVALID_PROVENANCE` basis.

## Historical qualifications retained

- Historical semantics-repair run `35232311780` remains immutable with independent Critic verdict `INVALID_IMPLEMENTATION`.
- Historical authority-review run `35225818354` remains immutable with independent `INVALID_IMPLEMENTATION` verdict.
- C4 `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED` remains independently `CONFIRMED_SCOPED` for the reusable scientific-validator path.
- Original Iter504T run `35181094204` remains historically `INVALID_IMPLEMENTATION`, not scientific FAIL.
- C1 VERIFIED, C2 REFUTED, C3 VERIFIED remain immutable history.
- Exact repair run `35205054496` remains coherent supporting evidence for the three-root scientific PASS, but this latest invalid gate does not issue validated authority.
- No Iter504T result is promoted to all 1888 states.

## Parallel D7-S2 retained state

- raw K5 group-variable tangent pushforward = `CLOSED_SCOPED`;
- group-only simultaneous contact-covector restriction/conditioning = `BLOCKED_SCOPED`;
- physical transverse quotient/projection = `BLOCKED_SCOPED`;
- measure/Haar/contact normalization = open;
- observable/distributional final pushforward = open.

Do not repeat blocked K5 source audits without genuinely new authorized primary material.

## Next admissible work

Highest-information same-object closure step: prospectively freeze a decision-canonicalization implementation repair only. The canonical cross-environment decision projection must exclude execution-local `local_path` strings and hashes derived solely from those paths while retaining immutable artifact IDs/digests, downloaded content SHA256 values, run/head identity, boundary states, inherited substantive review decision, workflow-level missing-artifact BLOCKED control, present-identity-mismatch INVALID control, C1/C3/C4/R/rho/root/channel/science checks, and the same interpretation ceiling.

A mandatory positive control must place the same immutable artifact bytes under at least two deliberately different directory prefixes and require identical canonical decision SHA. Mandatory negative controls must mutate artifact ID, digest, content SHA or substantive review field and require a changed/invalid decision. Do not rerun physics.

A distinct scientific frontier may proceed only if it does not consume this `INVALID_IMPLEMENTATION` gate as validated authority.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden until required subgates close.
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
- missing object/rank/certificate != zero; scoped child result != family closure; green CI != science.
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
