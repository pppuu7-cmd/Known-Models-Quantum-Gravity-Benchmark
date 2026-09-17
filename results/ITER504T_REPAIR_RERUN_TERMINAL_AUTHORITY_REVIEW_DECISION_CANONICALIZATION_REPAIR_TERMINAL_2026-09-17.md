# ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_GATE — terminal result

Date: 2026-09-17
Status: TERMINAL

## Authority / chronology

- Starting validated main: `e2776a252d95a2becc92fae21c018b4fd05ccf2c`.
- Latest pre-gate independent Critic: commit `77357d92050a9bec2c8daefd4d4babf7ff032ed0`, verdict `CONFIRMED_SCOPED` for the prior artifact-boundary gate's historical `INVALID_IMPLEMENTATION`.
- Prospective preregistration: `c6d67dec8617202b9c3584a159dd9f66ab749bd5`.
- Frozen authority: `107786de17159fdf4d16b9ee6cc71827fce7e45c`.
- Canonical reviewer: `05fdb2319f8375c3885cdb39ee99226b9b993005`.
- Aggregate code: `520a4ccdc081dabd50c2f2005a0a259fdf4b5a32`.
- Workflow head: `8b6c3ecf7d7a808a6978c78e1f28e7a30296e389`.
- Authoritative Actions run: `35245037403`, terminal `completed/success`.

The frozen criteria were not changed after result. No new physics execution was performed.

## Actions provenance

Jobs:

- source-lock `105282951727` — success;
- boundary-control `105283224608` — success;
- Python 3.11 lane `105283224783` — success;
- Python 3.13 lane `105283224698` — success;
- aggregate `105283316320` — success.

Artifacts and GitHub digests, independently rehashed after download:

- missing-artifact control `10506639126` / `sha256:0304ef867482f2cc1c95baa31f2bacefbc8f7670f62ec066487eb4c6fccc969d`;
- Python 3.11 `10506853511` / `sha256:4e4b3a2d24f22796482c98ab65ca3254bc4f11d5d0de45751136f25ea6fada2d`;
- Python 3.13 `10506853498` / `sha256:7265710f1aeac774e87f336c45d27a17ff5ff6845d71ec10ce84dfa6624f235d`;
- aggregate `10507146412` / `sha256:d460e12599ff349916e60e1148c207ce3cfe29ab589b87dfc8fa6fef56ad1ac9`.

Green CI is provenance/execution evidence only.

## Classification

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

This is a scoped closure/authority PASS for exact immutable repair run `35205054496`. It is not an all-1888, model, family, D7, Candidate Gravity or global quantum-gravity result.

## Exact terminal result

All frozen aggregate controls passed:

- lane classification agreement = true;
- lane canonical-decision SHA agreement = true;
- lane canonical-manifest SHA agreement = true;
- inherited substantive review agreement = true;
- both lane boundary-control suites pass;
- both lane canonicalization-control suites pass;
- real missing-artifact workflow control reaches BLOCKED;
- actual nonzero `gh run download` failure is observed without aborting classification.

The two production lanes deliberately use different local prefixes:

- Python 3.11: `terminal_311/...`;
- Python 3.13: `terminal_313/...`.

Their raw execution records therefore differ as expected:

- 3.11 raw execution SHA256 `41ef6238bf6e651ed33b23791d85aa620faf1665c47375ba22b4aaac43ff2ac5`;
- 3.13 raw execution SHA256 `16159732867f22fc92013a468639369ce0d9bdd8f9bcf658ebd968e61ca1a115`.

Their raw lane JSON files also differ (`a835087f...` versus `628268b6...`). Nevertheless the path-free canonical projection is exactly identical:

- canonical manifest SHA256 `1188f3cce3280035373074b68358a65cedf420616bfca76fe8d67ffe6e723766` in both lanes;
- canonical decision SHA256 `8969d8746ca56f6999b02b3ff04055d91d72a19f404d8e125bae3d049ec00a9e` in both lanes;
- inherited substantive review JSON is byte-identical, SHA256 `448508a79f77980b969dc156222a8872a18fd0467247501225131e5b0c9ecaee`.

All six frozen canonicalization controls passed:

1. different local prefixes preserve canonical-manifest identity;
2. different local prefixes preserve canonical-decision identity;
3. artifact-id mutation changes the canonical decision;
4. artifact-digest mutation changes the canonical decision;
5. downloaded-content-SHA mutation changes the canonical decision;
6. substantive inherited-review mutation changes the canonical decision.

Thus the repair removes only execution-local filesystem path dependence while retaining outcome sensitivity to immutable artifact and substantive-review identities.

The inherited exact-run review remains coherent:

- classification `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`;
- recomputed science `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- `review_errors=[]`;
- inherited semantics controls all pass;
- assemblies byte-identical;
- both lanes independently recompute 12 terminal leaves and 0 unresolved leaves;
- C1 in each lane: 18 records, 70,056 component booleans, 0 false.

The real missing-artifact boundary control remains correctly BLOCKED with canonical decision SHA256 `9aff1125345baa7713ce6e60dcdb053f5901a9139d8a19636bd9d81c298c21f7`.

Aggregate decision SHA256: `233444879a2f052a8e6706800750e2a4940414eb61ee00eebe5cbf4f3be4f1ee`.

## New fact

The independently confirmed path-sensitivity defect of the prior artifact-boundary closure has been closed for this exact review path: environment-local paths may change the raw execution record, but they no longer change the canonical scientific/closure decision. At the same time, artifact ID, artifact digest, downloaded content SHA256 and substantive inherited-review mutations remain decision-sensitive.

Therefore exact repair run `35205054496` is again supported by a prospectively frozen, path-invariant terminal authority-review chain for its original three-root bounded local-D claim.

Historical facts are preserved:

- prior artifact-boundary run `35238357310` remains historically `INVALID_IMPLEMENTATION` and Critic-confirmed;
- historical C4 remains `CONFIRMED_SCOPED` for the reusable scientific-validator path;
- original Iter504T run `35181094204` remains `INVALID_IMPLEMENTATION`, not scientific FAIL;
- this exact-run closure does not automatically authorize future executions of the unrepaired reusable validator.

## Hashes

- canonical result SHA256 `d034657fd0680167ca0b5c2382a2072ee76191e665784f42bb5dfbae7b5573e0`;
- aggregate JSON SHA256 `576131ecd0482908b5112a58fd97c0adade3ab280e265bb3c1bad52688805633`;
- aggregate log SHA256 `f7b25e8567321e357818ed428a6269acdafc51e09a26cd1ec773d0eed9ee8854`;
- canonical manifest SHA256 `1188f3cce3280035373074b68358a65cedf420616bfca76fe8d67ffe6e723766`;
- lane canonical decision SHA256 `8969d8746ca56f6999b02b3ff04055d91d72a19f404d8e125bae3d049ec00a9e`;
- aggregate decision SHA256 `233444879a2f052a8e6706800750e2a4940414eb61ee00eebe5cbf4f3be4f1ee`.

## Claim ceiling

Exact completed repair run `35205054496` and correctness of this terminal-review decision canonicalization only. No all-1888 closure, D7 closure, model/family failure, terminal selector, Candidate Gravity, Paper IV authorization, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.

## Independent Critic status

No independent Critic review of this new decision-canonicalization terminal result is recorded yet. The latest independent Critic remains the pre-gate audit that confirmed the prior path-sensitivity defect.
