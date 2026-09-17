# ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_GATE — prospective freeze

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT

## HYPOTHESIS

The independently confirmed `INVALID_IMPLEMENTATION` of `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE` can be repaired without changing the underlying Iter504T scientific object, immutable physics execution, artifact-boundary semantics, numerical thresholds, source realization, scientific classifier, or interpretation ceiling.

The remaining defect is exactly decision canonicalization: the prior outer review decision hash includes execution-local filesystem `local_path` strings and a manifest hash derived from those paths, so identical immutable artifacts transported through harmlessly different local prefixes yield different decision hashes. A contract-correct repair must make the cross-environment decision projection invariant to execution-local paths while remaining sensitive to every immutable artifact/science/provenance identity that matters.

## exact OBJECT

Exactly one implementation/closure repair of the terminal authority-review decision projection for immutable repair run `35205054496` at head `10ae6bcc8447d14cecc6e550065504b23f792953`.

No physics is rerun. The exact five upstream terminal artifacts, the now-working artifact-boundary collector semantics, the inherited exact-run reviewer, and the scientific payload are unchanged.

The repaired decision object must contain a canonical projection that:

1. excludes execution-local `artifact_manifest.entries[*].local_path` values;
2. excludes the prior `artifact_manifest.manifest_sha256` because that hash is derived from the noncanonical raw manifest including local paths;
3. retains immutable terminal run/head identity;
4. retains artifact role/name/id/digest, boundary state, observed identity/expiration state, download outcome, and downloaded file-content SHA256;
5. retains the inherited substantive exact-run review result, C1/C3/C4/R/rho/root/channel/threshold/floor/MAX_DEPTH checks, recomputed science classification, and claim ceiling;
6. emits a new `canonical_manifest_sha256` over the path-free manifest projection and a `canonical_decision_sha256` over the full path-free decision projection;
7. may separately record a raw execution-record SHA for provenance, but such environment-local raw hash may not be used for scientific/closure decision equality.

Historical runs remain immutable and are not rewritten.

## DEPENDENCY

- starting validated main `e2776a252d95a2becc92fae21c018b4fd05ccf2c`;
- latest independent Critic audit `recovery/CRITICAL_REVIEW_ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_2026-09-17.md`, commit `77357d92050a9bec2c8daefd4d4babf7ff032ed0`, verdict `CONFIRMED_SCOPED` for the prior gate's `INVALID_IMPLEMENTATION`;
- prior artifact-boundary preregistration `4a5f7d1c651527249b2831b6886cd502dc18e648`, authority `fbfca6f932dd540898de3d9d738e9f953de8ac84`, collector `bb99b03fe4ea5f6e5e3950ca32191ba55e87c6e1`, reviewer `8f0a72165479b870405bb51478a64e607777502b`, aggregate `2f4207d0c69f280fbe63fec4c75b45aec0041562`, workflow head `4e9a6ac95a10f89ba57eaa3aaa642a43e0236866`, terminal run `35238357310`;
- immutable physics repair run `35205054496`, head `10ae6bcc8447d14cecc6e550065504b23f792953`;
- inherited exact-run semantics reviewer `code/iter504t_repair_rerun_terminal_authority_review_semantics_repair.py` remains unchanged;
- terminal C4 authority/review and all C1/C2/C3 historical qualifications remain retained.

## SOURCE/REALIZATION AUTHORITY

Only the prospectively committed authority ledger `inputs/iter504t_repair_rerun_terminal_authority_review_decision_canonicalization_repair_authority.json`, the immutable repository objects it locks, the latest independent Critic audit, and GitHub Actions metadata/artifacts for exact run `35205054496` are authoritative.

No web source, alternate run, partial/nonterminal value, changed threshold, changed realization, changed scientific classifier, guessed artifact content, or synthetic production substitution may enter the production decision.

Synthetic controls are permitted only to test canonicalization and boundary semantics. They must not replace production scientific data.

## FROZEN INPUTS

Underlying science identity remains unchanged:

- roots `[13,14,15]`;
- rhos `[0.35,0.9,1.6,2.7]`;
- exact R cohort `[6,8,10,12]`;
- 243 channels;
- Arb/Acb precision 384 bits;
- exact threshold `1/20`;
- exact robust slope floor `1`;
- deterministic rational dyadic subdivision;
- `MAX_DEPTH=3`;
- direct local derivative recomputation on visited intervals.

Frozen scientific labels:

- PASS: `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- INCONCLUSIVE: `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`.

Frozen review labels:

- exact-run authority PASS: `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`;
- authority-restoration FAIL: `ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED`;
- artifact/structural BLOCKED: `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`;
- implementation/provenance invalidity: `INVALID_IMPLEMENTATION`.

Required upstream terminal artifacts remain exactly:

- `iter504t-repair-assembled-3.11`;
- `iter504t-repair-assembled-3.13`;
- `iter504t-repair-aggregate`;
- `iter504t-repair-critic`;
- `iter504t-repair-verdict`.

Frozen artifact-state semantics remain:

- absent/expired/unavailable/not downloadable required artifact => BLOCKED;
- present required artifact with wrong frozen id or digest => `INVALID_IMPLEMENTATION`;
- all present and identity-matching => continue to substantive exact-run reviewer.

## POSITIVE CONTROLS

1. The actual immutable run with all five required artifacts present and identity-matching must traverse the repaired reviewer in independent Python 3.11/3.13 lanes and produce identical `canonical_decision_sha256` even though the collector uses different local directory prefixes.
2. An explicit path-invariance fixture must take the same production manifest/substantive review, replace every local path with two deliberately different prefixes and alter only the path-derived raw manifest hash; both variants must produce identical canonical manifest and canonical decision SHA256 values.
3. The already repaired real workflow-boundary missing-artifact control must continue to request a deliberately nonexistent artifact, observe a nonzero real `gh run download` return code without aborting, and classify `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.
4. A structurally valid unresolved fixture must preserve `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`.
5. A missing required structural field inside an available downloaded lane object must remain BLOCKED.
6. Exact C1/C3/C4/R/rho/root/channel/threshold/floor/MAX_DEPTH controls must remain bound.

## NEGATIVE CONTROLS

1. Mutating any artifact id in the canonical production projection must change the canonical decision SHA or classify invalid.
2. Mutating any artifact digest must change the canonical decision SHA or classify invalid.
3. Mutating any downloaded artifact content SHA256 must change the canonical decision SHA or classify invalid.
4. Mutating a substantive inherited-review field, including recomputed scientific classification, must change the canonical decision SHA or classify FAIL/INVALID as appropriate.
5. A present artifact metadata fixture with correct required name but wrong frozen id/digest must remain `INVALID_IMPLEMENTATION`, not BLOCKED.
6. A top-level leaf certification contradicting recomputed per-rho certification must remain authority-restoration FAIL on a structurally complete object.
7. Serialized per-rho inconsistency, `R=6 -> 7`, missing required C1 record, cross-environment substantive science disagreement, or contradiction between transported aggregate/Critic/verdict and independently recomputed science must remain authority-restoration FAIL when complete.
8. Changing immutable run/head, source realization, scientific object, thresholds, labels, or claim ceiling is `INVALID_IMPLEMENTATION`.

## PASS

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED` iff:

- immutable run/head and repository authority identities match;
- the real missing-artifact boundary control still reaches the frozen BLOCKED label;
- artifact identity mismatch still reaches `INVALID_IMPLEMENTATION`;
- all actual required artifacts are present and identity-matching;
- both independent lanes reproduce the same substantive exact-run review decision;
- both independent lanes produce identical `canonical_decision_sha256` despite distinct local prefixes;
- the explicit path-invariance positive control passes;
- all id/digest/content-SHA/substantive-field mutation controls remain decision-sensitive;
- all inherited semantics controls pass;
- actual exact-run data independently recompute zero unresolved leaves and `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED` with C1/C3/C4 bindings intact;
- transported aggregate/Critic/verdict remain consistent with that independently recomputed decision.

PASS is exact-run scoped authority only. It does not erase historical invalid implementations or historical C4 and does not authorize future executions of an unrepaired reusable scientific validator.

If all required artifacts are present and complete but exact science independently recomputes nonzero unresolved leaves, preserve original `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`.

## FAIL

`ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED` iff authority/provenance/artifact availability and identity are valid and review objects are complete, but exact production data violate frozen per-rho/leaf/C1/C3/C4/science bindings or contradict transported terminal decisions. This is authority-restoration failure only, not scientific/model falsification.

## BLOCKED / INVALID

`ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED` iff any required terminal artifact is absent, expired, unavailable, not downloadable, corrupted beyond parsing, or any required structural field is insufficient for independent recomputation without guessing. Missing evidence remains missing, never false or zero.

`INVALID_IMPLEMENTATION` iff authority/provenance identity fails, a present artifact has wrong frozen id/digest, another run is substituted, the canonical decision remains path-sensitive, any frozen canonicalization or inherited semantics control fails, frozen criteria change after result, scientific object/source/threshold/classifier meaning changes, or synthetic data enter production.

## INTERPRETATION CEILING

Any outcome is limited to exact completed repair run `35205054496` and correctness of this terminal-review decision canonicalization. No outcome establishes all-1888 closure, D7 closure, model/family failure, selector status, Candidate Gravity, Paper IV authorization, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`. Historical FAIL/BLOCKED/INCONCLUSIVE/INVALID results remain immutable.
