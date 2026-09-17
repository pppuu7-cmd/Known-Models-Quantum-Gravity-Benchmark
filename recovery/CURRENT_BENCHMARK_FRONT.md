# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal closure result

Gate:

`ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_GATE`

Terminal classification:

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

This is an **exact-run scoped closure/authority PASS**, not an all-1888, model, family, D7 or global result.

Authority / execution chain:

- starting validated main `e2776a252d95a2becc92fae21c018b4fd05ccf2c`;
- prospective preregistration `c6d67dec8617202b9c3584a159dd9f66ab749bd5`;
- frozen authority `107786de17159fdf4d16b9ee6cc71827fce7e45c`;
- canonical reviewer `05fdb2319f8375c3885cdb39ee99226b9b993005`;
- aggregate code `520a4ccdc081dabd50c2f2005a0a259fdf4b5a32`;
- workflow head `8b6c3ecf7d7a808a6978c78e1f28e7a30296e389`;
- authoritative Actions run `35245037403`, terminal `completed/success`;
- jobs: source-lock `105282951727`, boundary-control `105283224608`, Python 3.11 `105283224783`, Python 3.13 `105283224698`, aggregate `105283316320`;
- artifacts: boundary control `10506639126` / `sha256:0304ef867482f2cc1c95baa31f2bacefbc8f7670f62ec066487eb4c6fccc969d`; Python 3.11 `10506853511` / `sha256:4e4b3a2d24f22796482c98ab65ca3254bc4f11d5d0de45751136f25ea6fada2d`; Python 3.13 `10506853498` / `sha256:7265710f1aeac774e87f336c45d27a17ff5ff6845d71ec10ce84dfa6624f235d`; aggregate `10507146412` / `sha256:d460e12599ff349916e60e1148c207ce3cfe29ab589b87dfc8fa6fef56ad1ac9`;
- canonical result SHA256 `d034657fd0680167ca0b5c2382a2072ee76191e665784f42bb5dfbae7b5573e0`;
- aggregate JSON SHA256 `576131ecd0482908b5112a58fd97c0adade3ab280e265bb3c1bad52688805633`;
- aggregate log SHA256 `f7b25e8567321e357818ed428a6269acdafc51e09a26cd1ec773d0eed9ee8854`;
- canonical manifest SHA256 `1188f3cce3280035373074b68358a65cedf420616bfca76fe8d67ffe6e723766`;
- lane canonical decision SHA256 `8969d8746ca56f6999b02b3ff04055d91d72a19f404d8e125bae3d049ec00a9e`;
- aggregate decision SHA256 `233444879a2f052a8e6706800750e2a4940414eb61ee00eebe5cbf4f3be4f1ee`.

Green CI is provenance only.

## Exact result

The prior independently confirmed defect was environment-local path dependence in outer decision hashing. This gate repairs only that decision-canonicalization layer; no physics was rerun.

The two production lanes intentionally place the same immutable upstream artifacts under different prefixes (`terminal_311/...` versus `terminal_313/...`). Their raw execution records differ as expected:

- 3.11 raw SHA256 `41ef6238bf6e651ed33b23791d85aa620faf1665c47375ba22b4aaac43ff2ac5`;
- 3.13 raw SHA256 `16159732867f22fc92013a468639369ce0d9bdd8f9bcf658ebd968e61ca1a115`.

After excluding only execution-local `local_path` values and the prior manifest hash derived from those paths, both lanes have exact identical canonical identities:

- canonical manifest SHA256 `1188f3cce3280035373074b68358a65cedf420616bfca76fe8d67ffe6e723766`;
- canonical decision SHA256 `8969d8746ca56f6999b02b3ff04055d91d72a19f404d8e125bae3d049ec00a9e`;
- inherited substantive review JSON byte-identical SHA256 `448508a79f77980b969dc156222a8872a18fd0467247501225131e5b0c9ecaee`.

All frozen canonicalization controls pass. Local path changes preserve the canonical manifest/decision, while artifact ID, artifact digest, downloaded-content SHA256 and substantive inherited-review mutations all change the canonical decision. The real missing-artifact boundary control still observes a nonzero `gh run download` return code, continues execution and emits `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.

The inherited exact-run review remains coherent: `review_errors=[]`, semantics controls all pass, both lanes independently recompute 12 terminal leaves and zero unresolved leaves, C1 remains 18 records / 70,056 booleans / zero false per lane, and the bounded three-root science remains `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`.

Thus exact immutable repair run `35205054496` again has a prospectively frozen, path-invariant terminal authority-review chain for its original scoped three-root bounded local-D claim.

## Latest independent Critical Review

No independent Critic review of this new decision-canonicalization terminal result is recorded yet.

The latest independent Critic remains:

`recovery/CRITICAL_REVIEW_ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_2026-09-17.md`

Critic commit `77357d92050a9bec2c8daefd4d4babf7ff032ed0`, verdict `CONFIRMED_SCOPED`, which independently confirmed the historical prior artifact-boundary gate's `INVALID_IMPLEMENTATION` and localized its remaining defect to path-sensitive decision hashing. This new gate was designed prospectively against that defect.

## Historical qualifications retained

- prior artifact-boundary run `35238357310` remains historically `INVALID_IMPLEMENTATION`, independently `CONFIRMED_SCOPED`;
- semantics-repair run `35232311780` remains historical and independently `INVALID_IMPLEMENTATION`;
- authority-review run `35225818354` remains independently `INVALID_IMPLEMENTATION`;
- C4 `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED` remains independently `CONFIRMED_SCOPED` for the reusable scientific-validator path;
- original Iter504T run `35181094204` remains `INVALID_IMPLEMENTATION`, not scientific FAIL;
- C1 VERIFIED, C2 REFUTED, C3 VERIFIED remain immutable history;
- exact repair run `35205054496` is now restored only as exact-run scoped authority through the new canonicalized review chain;
- this does not authorize future executions of the unrepaired reusable C4 validator;
- no Iter504T result is promoted to all 1888 states.

## Parallel D7-S2 retained state

- raw K5 group-variable tangent pushforward = `CLOSED_SCOPED`;
- group-only simultaneous contact-covector restriction/conditioning = `BLOCKED_SCOPED`;
- physical transverse quotient/projection = `BLOCKED_SCOPED`;
- measure/Haar/contact normalization = open;
- observable/distributional final pushforward = open.

Do not repeat blocked K5 source audits without genuinely new authorized primary material.

## Next admissible work

Before using this newly restored exact-run authority as a high-DAG downstream premise, the highest-value closure step is an independent Critical Review of the decision-canonicalization gate. It should independently verify prospective chronology, path-free canonical projection, path-invariance, id/digest/content-SHA/substantive mutation sensitivity, real missing-artifact BLOCKED semantics, artifact digests and exact inherited-science replay.

If that review confirms the terminal PASS, fresh DAG selection may move to a higher-information scientific/D7 frontier without repairing the reusable C4 validator unless a future Iter504T execution actually requires that reusable path. If Iter504T must be rerun, C4 reusable-validator repair remains mandatory before that new execution can carry automatic authority.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden until required subgates close.
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
- missing object/rank/certificate != zero; scoped child result != family closure; green CI != science.
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
