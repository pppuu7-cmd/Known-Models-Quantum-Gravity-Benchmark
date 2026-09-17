# Independent Critical Review — Iter504T decision-canonicalization repair

Date: 2026-09-17
Reviewer role: independent adversarial Critic
Reviewed gate: `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_GATE`
Reviewed terminal classification: `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`
Verdict: `CONFIRMED_SCOPED`

## Scope

This review tests only whether the terminal authority-review decision for immutable repair run `35205054496` was correctly repaired to be invariant to execution-local filesystem paths while remaining sensitive to immutable provenance, artifact-content and substantive scientific-review identity.

It does **not** rerun physics and does not promote the bounded three-root result to all Iter504 states, D7, a model/family conclusion, Candidate Gravity, Paper IV, or a global quantum-gravity claim.

## 1. Prospective chronology — confirmed

The repair preregistration is commit:

`c6d67dec8617202b9c3584a159dd9f66ab749bd5`

Its status is explicitly `PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT` and it freezes the exact defect, object, canonical projection, positive controls, negative controls, PASS/FAIL/BLOCKED/INVALID rules and interpretation ceiling before the repair implementation or terminal result.

The frozen authority is commit:

`107786de17159fdf4d16b9ee6cc71827fce7e45c`

The canonical reviewer and aggregate implementations are later commits:

- reviewer `05fdb2319f8375c3885cdb39ee99226b9b993005`;
- aggregate `520a4ccdc081dabd50c2f2005a0a259fdf4b5a32`.

The execution workflow head is:

`8b6c3ecf7d7a808a6978c78e1f28e7a30296e389`.

An independent repository compare gives the preregistration commit as the merge base of the workflow head, with the workflow head exactly four commits ahead and zero commits behind. The only additions in that interval are the frozen authority, reviewer, aggregate and workflow. The workflow source-lock also independently requires preregistration, authority, prior Critic, reviewer and aggregate ancestry and checks exact repository blob hashes before execution.

Result: no outcome-dependent chronology defect found.

## 2. Frozen object / no physics rerun — confirmed

The authority binds immutable physics repair run:

- run `35205054496`;
- head `10ae6bcc8447d14cecc6e550065504b23f792953`.

The canonicalization workflow does not execute the scientific evaluator. It downloads the already frozen five terminal artifacts, invokes the inherited exact-run semantics reviewer, canonicalizes only the outer terminal-review decision and aggregates the two review lanes plus the missing-artifact boundary control.

The underlying frozen science remains roots `[13,14,15]`, rhos `[0.35,0.9,1.6,2.7]`, R `[6,8,10,12]`, 243 channels, 384-bit Arb/Acb, threshold `1/20`, robust floor `1`, deterministic rational dyadic subdivision and `MAX_DEPTH=3`.

Result: no scientific-object retuning found.

## 3. Upstream artifact identity — independently confirmed

Fresh Actions metadata for run `35205054496` was independently queried during this review. All five required artifacts exactly match the frozen authority by artifact ID, digest and run head:

- assembly 3.11: id `10498265422`, digest `sha256:3e6739a93cd6e467ea4d1929c37bf68a830fabcd10e415bf2d08388ee4dc0075`;
- assembly 3.13: id `10497554745`, digest `sha256:fee046299dee740c4a85df00eb8e6c21628ad98b7bf812a0518f8a423e6df2ff`;
- aggregate: id `10497359984`, digest `sha256:dee8780bb093f8dfe35419a1e4749127cebf730972ed1a395bc894ebfb7d0d47`;
- Critic: id `10498490034`, digest `sha256:cbe6e8856f16850f5c4ecefe07a9c64aa6a7c2c0d035383f385da99c264078a1`;
- verdict: id `10498015467`, digest `sha256:888edcf687b1c6705d32cd2aae3f03637732376f2eb2eadd8818690fd00cad49`.

All are unexpired in the fresh metadata and all are tied to head `10ae6bcc8447d14cecc6e550065504b23f792953`.

Result: no `INVALID_PROVENANCE` basis found.

## 4. Current repair-run artifacts — independently downloaded and rehashed

All four terminal artifacts of canonicalization run `35245037403` were freshly downloaded during this independent review and their ZIP SHA256 values were recomputed outside the workflow:

- aggregate `10507146412` -> `d460e12599ff349916e60e1148c207ce3cfe29ab589b87dfc8fa6fef56ad1ac9`;
- Python 3.11 `10506853511` -> `4e4b3a2d24f22796482c98ab65ca3254bc4f11d5d0de45751136f25ea6fada2d`;
- Python 3.13 `10506853498` -> `7265710f1aeac774e87f336c45d27a17ff5ff6845d71ec10ce84dfa6624f235d`;
- missing-artifact control `10506639126` -> `0304ef867482f2cc1c95baa31f2bacefbc8f7670f62ec066487eb4c6fccc969d`.

These exactly match fresh Actions metadata and the durable result/hash records.

Fresh internal-file rehashes also reproduce:

- aggregate JSON `576131ecd0482908b5112a58fd97c0adade3ab280e265bb3c1bad52688805633`;
- aggregate log `f7b25e8567321e357818ed428a6269acdafc51e09a26cd1ec773d0eed9ee8854`;
- lane 3.11 JSON `a835087fcfdf0a2b1d2f82d5ab60d4717cad34026d01fbf11d588490a947d21e`;
- lane 3.13 JSON `628268b633f7c994d4e6b0bf167bc3fb69e92c6b99256d8025cb1e4f8a84aaf5`;
- boundary-control JSON `b704faeeb01e105ba4ecd1e3aee6430257c6651fb3a6b8bfa98cb0842075adfd`.

Result: durable artifact record matches independently downloaded bytes.

## 5. Path-free canonicalization — independently reconstructed

The reviewer implementation removes only each manifest entry's execution-local `local_path` from the canonical manifest. The old raw `manifest_sha256`, which is itself path-derived, is not part of the canonical manifest projection. Immutable run identity, artifact role/name/id/digest/state/download result/content SHA, inherited substantive review, boundary controls and claim ceiling remain decision-bound.

The two actual lane payloads intentionally differ in raw local paths:

- lane 3.11 uses `terminal_311/...`;
- lane 3.13 uses `terminal_313/...`.

Their raw manifest hashes differ:

- 3.11 `88459ee31ef8ca0ac1fa465daddb3b8b891e46eeddd83168b5c0589fcc0569c5`;
- 3.13 `6f8afccf131664587116dfa897cafd74ca47f8e3c661836c1a191bba46c644b8`.

During this review the canonical projection was reconstructed independently from the downloaded lane JSON, without invoking the repository reviewer. The independent reconstruction reproduces for **both** lanes:

- canonical manifest SHA256 `1188f3cce3280035373074b68358a65cedf420616bfca76fe8d67ffe6e723766`;
- canonical decision SHA256 `8969d8746ca56f6999b02b3ff04055d91d72a19f404d8e125bae3d049ec00a9e`.

The independently reconstructed canonical manifests are exactly equal and the independently reconstructed canonical decision projections are exactly equal. The raw execution-record hashes remain unequal, as expected and as required for the positive path-invariance test.

Result: the previously confirmed path-sensitivity defect is closed at the frozen decision layer.

## 6. Mutation sensitivity — confirmed

Both independently produced lane payloads report all preregistered canonicalization controls true:

- changing local prefixes preserves canonical manifest;
- changing local prefixes preserves canonical decision;
- artifact ID mutation changes canonical decision;
- artifact digest mutation changes canonical decision;
- downloaded content SHA mutation changes canonical decision;
- substantive inherited-review mutation changes canonical decision.

Code inspection confirms these controls compare the resulting canonical projection hash rather than merely testing a label. The aggregate requires canonical-decision equality, canonical-manifest equality, inherited substantive-review equality and all lane canonicalization controls before preserving the lane classification.

Result: the repair did not obtain path invariance by dropping immutable decision-critical identity.

## 7. Real missing-artifact boundary semantics — independently confirmed

The freshly downloaded boundary-control JSON records:

- `run_identity_ok = true`;
- simulated role `verdict`;
- lookup name `iter504t-boundary-control-definitely-missing`;
- `download_attempted = true`;
- actual download return code `1`;
- state `MISSING_OR_UNAVAILABLE`;
- classifier reached `true`;
- classification `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.

The aggregate independently requires both the BLOCKED classification and the observed nonzero download return code/state.

Result: missing evidence remains BLOCKED, not false, zero, PASS or implementation abort.

## 8. Inherited exact science replay — confirmed at the exact-run scope

The two lane `inherited_review` objects are byte-for-byte equal in parsed content and contain:

- `review_errors = []`;
- `semantics_controls_all_pass = true`;
- science `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- for Python 3.11: 12 terminal leaves, zero recomputed unresolved leaves, C1 = 18 records / 70,056 components / zero false;
- for Python 3.13: 12 terminal leaves, zero recomputed unresolved leaves, C1 = 18 records / 70,056 components / zero false;
- every serialized leaf certification shown in the replay agrees with the recomputed conjunction of its four per-rho certification booleans.

Inherited semantics negative controls all pass, including C4 true-leaf/false-rho contradiction -> failure, R `6 -> 7` -> failure, missing C1 -> failure, missing required field -> BLOCKED, per-rho inconsistency -> failure, artifact identity mutation -> INVALID and preservation of a valid INCONCLUSIVE fixture.

Result: the canonicalization repair preserves rather than substitutes the substantive exact-run review.

## 9. Aggregate terminal decision — confirmed

Run `35245037403` completed successfully with every job successful. The aggregate payload has:

- all eight aggregate controls true;
- `aggregate_controls_all_pass = true`;
- classification `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`;
- aggregate decision SHA256 `233444879a2f052a8e6706800750e2a4940414eb61ee00eebe5cbf4f3be4f1ee`.

The aggregate does not equate raw execution hashes; it requires equality only of the prospectively defined canonical decision/manifest and inherited substantive review while retaining the real boundary control.

## Verdict

`CONFIRMED_SCOPED`

The terminal classification

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

is independently confirmed for the exact immutable repair run `35205054496` and the prospectively frozen decision-canonicalization contract.

The prior `INVALID_IMPLEMENTATION` caused by environment-local path hashing is closed by a path-free canonical projection that still binds immutable artifact/provenance/content/science identities and preserves real missing-artifact BLOCKED semantics.

The inherited scientific statement is therefore authority-valid only at its original bounded scope:

`ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`.

## Claim ceiling / next admissible use

This review does not authorize direct promotion to all 1888 parent states. Under the already frozen outcome-blind successor toolkit, any use of this successful roots-13/14/15 mechanism repair as a broader scientific premise must first pass a prospectively selected held-out representative cohort with no refit.

If a future Iter504T-like execution uses the historical reusable scientific-validator path, the retained C4 reusable-validator defect must be repaired before that new execution can carry automatic authority. This requirement is separate from the exact completed-run authority confirmed here.
