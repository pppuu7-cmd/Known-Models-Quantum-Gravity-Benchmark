# KMQGB Research / Closure handoff — Iter504T decision-canonicalization repair

Date: 2026-09-17
Status: TERMINAL_HANDOFF

## STATE_READ

- Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark` only.
- Starting validated main: `e2776a252d95a2becc92fae21c018b4fd05ccf2c`.
- Starting latest terminal closure gate: `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE`.
- Starting terminal classification: `INVALID_IMPLEMENTATION`, not scientific FAIL.
- Latest independent Critic before this gate: `recovery/CRITICAL_REVIEW_ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_2026-09-17.md`, commit `77357d92050a9bec2c8daefd4d4babf7ff032ed0`, verdict `CONFIRMED_SCOPED`.
- That Critic independently localized the remaining prior defect to environment-local `local_path` strings and the manifest/review hashes derived from those paths; it also independently confirmed that the real missing-artifact boundary repair works and found no provenance defect.
- Immutable physics repair run retained: `35205054496`, head `10ae6bcc8447d14cecc6e550065504b23f792953`.
- Historical C4 remains independently `CONFIRMED_SCOPED` for the reusable scientific-validator path.
- `CURRENT_BENCHMARK_FRONT` and active-front index were current at start; no pre-gate recovery reconciliation was needed.
- Governance retained: `RQIR Core v1.0 = FROZEN`; D7-S2/D7-S3 not closed; D7-S4 partial; terminal selectors forbidden; Candidate Gravity inactive; Paper IV not authorized.

## TARGET_GATE

`ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_GATE`

## WHY_THIS_GATE

The prior gate had already repaired the real Actions missing-artifact boundary and independently replayed coherent exact-run science, but its terminal cross-environment decision equality was invalid solely because execution-local download-directory paths were included in the hashed decision projection. This narrow defect blocked use of the exact repair run as validated high-DAG authority even though the substantive review was byte-identical. A prospective canonicalization repair therefore offered maximal downstream unlock at low cost without rerunning physics or altering any scientific threshold/object.

## PREREG

- Protocol: `research/prereg/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_GATE_2026-09-17.md`.
- Prospective freeze commit: `c6d67dec8617202b9c3584a159dd9f66ab749bd5`.
- Frozen authority: `inputs/iter504t_repair_rerun_terminal_authority_review_decision_canonicalization_repair_authority.json`.
- Authority commit: `107786de17159fdf4d16b9ee6cc71827fce7e45c`.
- Frozen PASS: `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`.
- Frozen FAIL: `ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED`.
- Frozen BLOCKED: `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.
- Frozen INVALID: `INVALID_IMPLEMENTATION`.
- Frozen interpretation ceiling was unchanged after result.

## WORK_PERFORMED

- Froze the canonical decision contract before implementation.
- Locked exact run/head, all five required upstream artifact identities/digests, latest Critic identity, prior collector/reviewer identities, science constants and claim ceiling.
- Reused the already repaired nonaborting artifact collector unchanged.
- Reused the inherited substantive exact-run semantics reviewer unchanged.
- Implemented a path-free canonical manifest projection excluding only `entries[*].local_path` and the old raw manifest SHA derived from those paths.
- Retained terminal run identity, artifact roles/names/IDs/digests/states/download outcomes/content SHA256 values, inherited substantive review, boundary controls and claim ceiling in the canonical decision.
- Added explicit path-invariance controls using two deliberately different synthetic local prefixes.
- Added negative mutation controls for artifact ID, artifact digest, downloaded-content SHA256 and substantive inherited-review content.
- Preserved the real workflow-boundary missing-artifact `gh run download` control.
- Ran independent Python 3.11/3.13 lanes with `fail-fast:false`; substantive output was consumed only after aggregate and run terminalized.
- Downloaded and independently rehashed all four current-run artifacts; each ZIP SHA256 matched GitHub Actions digest.
- Persisted canonical result, exact aggregate log, hashes/provenance, terminal result and reconciled both front documents.

## RESULT

Authoritative Actions run `35245037403` at workflow head `8b6c3ecf7d7a808a6978c78e1f28e7a30296e389` terminalized `completed/success`.

Jobs:

- source-lock `105282951727` — success;
- boundary-control `105283224608` — success;
- Python 3.11 `105283224783` — success;
- Python 3.13 `105283224698` — success;
- aggregate `105283316320` — success.

Artifacts:

- boundary-control `10506639126`, digest `sha256:0304ef867482f2cc1c95baa31f2bacefbc8f7670f62ec066487eb4c6fccc969d`;
- Python 3.11 `10506853511`, digest `sha256:4e4b3a2d24f22796482c98ab65ca3254bc4f11d5d0de45751136f25ea6fada2d`;
- Python 3.13 `10506853498`, digest `sha256:7265710f1aeac774e87f336c45d27a17ff5ff6845d71ec10ce84dfa6624f235d`;
- aggregate `10507146412`, digest `sha256:d460e12599ff349916e60e1148c207ce3cfe29ab589b87dfc8fa6fef56ad1ac9`.

Independent local ZIP rehashes matched all four Actions digests exactly.

All aggregate controls pass. The production lanes have deliberately different raw execution identities because their local paths differ:

- 3.11 raw execution SHA256 `41ef6238bf6e651ed33b23791d85aa620faf1665c47375ba22b4aaac43ff2ac5`;
- 3.13 raw execution SHA256 `16159732867f22fc92013a468639369ce0d9bdd8f9bcf658ebd968e61ca1a115`.

But the canonical identities are identical:

- canonical manifest SHA256 `1188f3cce3280035373074b68358a65cedf420616bfca76fe8d67ffe6e723766`;
- canonical decision SHA256 `8969d8746ca56f6999b02b3ff04055d91d72a19f404d8e125bae3d049ec00a9e`;
- inherited substantive review JSON SHA256 `448508a79f77980b969dc156222a8872a18fd0467247501225131e5b0c9ecaee` in both lanes.

All canonicalization controls pass: local-prefix changes are invariant; artifact ID, digest, content SHA and substantive review mutations remain decision-sensitive.

Real missing-artifact boundary control still observes download return code `1`, reaches the reviewer and yields `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED` without aborting.

Inherited exact-run review remains coherent:

- `review_errors=[]`;
- all inherited semantics controls pass;
- assemblies byte-identical;
- both environments recompute 12 terminal leaves and 0 unresolved leaves;
- C1 per lane: 18 records, 70,056 component booleans, 0 false;
- recomputed bounded three-root science: `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`.

Aggregate decision SHA256 `233444879a2f052a8e6706800750e2a4940414eb61ee00eebe5cbf4f3be4f1ee`.

## CLASSIFICATION

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

Scoped closure/authority PASS for exact immutable repair run `35205054496` only.

## NEW_FACT

The independently confirmed decision-path canonicalization defect is closed for this exact authority-review chain. Raw execution records may legitimately differ due solely to environment-local download paths, while the scientific/closure canonical decision is now exactly path-invariant. Crucially, the repair does not over-normalize: artifact ID, artifact digest, downloaded artifact content SHA256 and substantive inherited-review mutations all remain visible to the decision.

Therefore the exact repair run `35205054496` is again backed by a prospectively frozen terminal authority-review chain for its original three-root bounded local-D claim. This does not erase historical invalid implementations and does not repair or authorize the reusable C4 validator for future runs.

## CLAIM_CEILING

Exact completed run `35205054496` and correctness of the terminal-review decision canonicalization only. No all-1888 closure; no D7 closure; no model/family failure; no terminal selector; no Candidate Gravity activation; no Paper IV authorization; no global quantum-gravity/new-physics claim.

## FILES/ARTIFACTS

- `research/prereg/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_GATE_2026-09-17.md`;
- `inputs/iter504t_repair_rerun_terminal_authority_review_decision_canonicalization_repair_authority.json`;
- `code/iter504t_repair_rerun_terminal_authority_review_decision_canonicalization_repair.py`;
- `code/iter504t_repair_rerun_terminal_authority_review_decision_canonicalization_repair_aggregate.py`;
- `.github/workflows/iter504t-repair-rerun-terminal-authority-review-decision-canonicalization-repair.yml`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_CANONICAL_2026-09-17.json`, SHA256 `d034657fd0680167ca0b5c2382a2072ee76191e665784f42bb5dfbae7b5573e0`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_ACTIONS_AGGREGATE_RAW_2026-09-17.log`, SHA256 `f7b25e8567321e357818ed428a6269acdafc51e09a26cd1ec773d0eed9ee8854`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_HASHES_2026-09-17.json`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_TERMINAL_2026-09-17.md`;
- Actions run `35245037403` and four artifacts listed above.

## COMMITS

- starting validated main `e2776a252d95a2becc92fae21c018b4fd05ccf2c`;
- preregistration `c6d67dec8617202b9c3584a159dd9f66ab749bd5`;
- authority `107786de17159fdf4d16b9ee6cc71827fce7e45c`;
- reviewer `05fdb2319f8375c3885cdb39ee99226b9b993005`;
- aggregate code `520a4ccdc081dabd50c2f2005a0a259fdf4b5a32`;
- workflow head `8b6c3ecf7d7a808a6978c78e1f28e7a30296e389`;
- canonical result `c2deb5357eb33b75e9081ac3044a3654a1ef89f6`;
- exact aggregate log `65f35eff39fd7362461cad4cbcdc4b4b278886bb`;
- hashes/provenance `fb330527d7c76407290be562b6b4ca3343d9f66f`;
- terminal result `c572afa719e783619a981da5eb8de11acd2b5d54`;
- current-front reconciliation `05d8660227199f9e306bc14f77661a6528feb07b`;
- active-front reconciliation `4edcf6a238518e96f76b6aa3d6e6f29b6ed76f41`.

## OPEN_BLOCKERS

1. No independent Critic review of this new canonicalization terminal PASS is yet recorded.
2. Historical C4 remains independently confirmed for the reusable scientific-validator path; any future Iter504T execution relying on that validator requires its own prospective repair first.
3. The exact three-root result is not an all-1888-state certificate.
4. D7-S2/D7-S3/D7-S4 obligations remain open as recorded in current front.
5. Candidate Gravity and Paper IV remain inactive/not authorized.

## NEXT_RECOMMENDED_GATE

Perform an independent Critical Review of `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_DECISION_CANONICALIZATION_REPAIR_GATE` before consuming the restored exact-run authority as a high-DAG downstream premise.

That review should independently verify prospective chronology, immutable source/run/artifact identities, downloaded ZIP rehashes, path-free canonical projection, deliberately distinct local-prefix invariance, artifact-ID/digest/content-SHA/substantive-review mutation sensitivity, real missing-artifact BLOCKED semantics, and inherited exact-run science replay. If confirmed, fresh DAG selection may proceed to a higher-information scientific/D7 frontier. Do not rerun Iter504T physics merely to repeat this exact result.
