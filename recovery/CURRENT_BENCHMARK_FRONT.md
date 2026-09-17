# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal closure result

Gate:

`ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_SEMANTICS_REPAIR_GATE`

Historical terminal classification:

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

Authority / execution chain:

- prospective preregistration `5b18ffbe46b967ef64c54d6181924aa8acf6f43e`;
- frozen authority `39bd24ff03cba8858dca39ceb2935509352f295a`;
- reviewer `b0f9fa5f2efe1e1f09d72d33e78bbee904ad5eb5`;
- aggregate code `311ac4169bd3fd8e0ce8b8ded1f8bc566db3cdeb`;
- workflow head `71b1e197192c17d0c74e06fe7eb12b9b4b332f60`;
- authoritative Actions run `35232311780`, terminal `completed/success`;
- jobs: source-lock `105239292923`, Python 3.11 `105239369708`, Python 3.13 `105239369636`, aggregate `105239442328`;
- artifacts: Python 3.11 `10501567806` / `sha256:70f4a0b7b4e2e7ab60c42c5e83abeaa28dd2b55bc45bbace7d448e2ccbbe888e`; Python 3.13 `10501033269` / `sha256:7ae9953cfc780230007eb326ab8fc5c13532a30bde12b7c41e08d1ed156093ec`; aggregate `10501338087` / `sha256:cec9f4eaa6192d0a2defc57d117ae5de89cc7e9b5f9c77a2ec9403ea1d545fe4`;
- lane review decision SHA256 `ab197395b971d3dc3c78574d4ae8176df839394ce902b72b126307b2674f604c`;
- aggregate decision SHA256 `627836dc469c726c280d7b00c3ac46413724683fd05cc8759fbb185735230d61`.

Green CI is provenance only.

## Exact observed result

The semantics-repair implementation genuinely fixes the two defects identified by the prior independent Critic `15b323994844fd83dfa0dc71efb977ba4300de97`:

1. valid original scientific INCONCLUSIVE is preserved exactly as `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`;
2. deleting a required structural field from an already downloaded parseable lane object yields `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.

The actual immutable repair run `35205054496` remains internally coherent under the exact replay:

- terminal assemblies are byte-identical SHA256 `dfaa14d7b07708b9cc59d04413a86661aed37dab662705499893e601ffcb9c24`;
- roots `13,14,15`, exact R cohort `[6,8,10,12]`, 12 terminal leaves and 48 per-rho rows are present;
- all per-rho and leaf certifications satisfy the frozen predicates;
- recomputed unresolved leaves = `0`;
- both environments independently recompute `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- C1 = 18 records / 70,056 boolean components per lane / zero false;
- no actual C4 leaf-binding violation is present.

These facts remain exact supporting evidence for the underlying three-root PASS path.

## Latest independent Critical Review

Audit:

`recovery/CRITICAL_REVIEW_ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_SEMANTICS_REPAIR_2026-09-17.md`

Critic commit:

`7263accb799829fddef81c1b4759822261f8b8d4`

Verdict:

`INVALID_IMPLEMENTATION`

The terminal semantics-repair gate still fails one frozen alternate branch at the authoritative workflow boundary.

The preregistration freezes `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED` when any required terminal artifact is unavailable, expired, missing, corrupted, or otherwise insufficient for independent recomputation without guessing. The Python reviewer has a local missing-path BLOCKED handler, but the Actions workflow checks exact upstream artifact ids/digests under `set -euo pipefail` in `source-lock` and later downloads all required artifacts under `set -euo pipefail` before invoking Python.

Explicit workflow counterexample: if required upstream artifact `iter504t-repair-verdict` is unavailable/missing, source-lock fails before lane execution; if metadata passes but download fails, the lane exits before Python receives a missing path. In either case no frozen BLOCKED classification is emitted and aggregate cannot run. The implemented `missing_required_field_maps_to_blocked` fixture only deletes `roots` inside an already downloaded JSON object and therefore does not cover this workflow-level branch.

This is implementation invalidity, not scientific FAIL and not observed-run provenance failure. Historical terminal classification is not rewritten. The actual exact-run replay may still be scientifically correct, but this gate is not independently confirmed as a fully contract-valid semantics repair.

## Historical qualifications retained

- Historical terminal classification from run `35232311780` remains immutable Actions/repository history; independent Critic verdict is now `INVALID_IMPLEMENTATION`.
- Historical authority-review result from run `35225818354` remains immutable and its independent Critic verdict `INVALID_IMPLEMENTATION` remains historically true for that implementation.
- C4 `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED` remains independently `CONFIRMED_SCOPED` for the reusable launch-head validator path.
- Original Iter504T run `35181094204` remains historically `INVALID_IMPLEMENTATION`, not scientific FAIL.
- C1 VERIFIED, C2 REFUTED, C3 VERIFIED remain immutable history.
- Actual exact repair run `35205054496` remains coherent supporting evidence for the three-root scientific PASS, but authority restoration is not fully contract-validated by run `35232311780`.

## Parent / parallel state retained

- `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED` retained.
- `ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED` retained.
- `ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED` retained.
- No Iter504T result is promoted to all 1888 states.
- D7-S2 raw K5 group-variable tangent pushforward remains `CLOSED_SCOPED`, but group-only contact-covector restriction/conditioning remains BLOCKED; physical transverse quotient and measure/observable stages remain open.

## Next admissible work

A same-object implementation repair may preserve the existing scientific object and exact physics run while repairing review execution semantics:

1. make required upstream artifact absence/expiration/download failure reach a classifier path that emits `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED` rather than failing the workflow before classification;
2. add an outcome-sensitive missing-artifact fixture at the workflow/reviewer boundary, not only a missing field inside downloaded JSON;
3. retain the now-correct original INCONCLUSIVE branch, structural-field BLOCKED branch, C4/per-rho/R/C1 controls, source/artifact identity locks and claim ceiling;
4. do not rewrite run `35232311780`.

Changing underlying science object, thresholds, roots/rhos/R cohort, classifier meaning, source realization, or interpretation ceiling requires a new prospectively frozen gate.

A distinct scientific frontier may proceed only if it does not consume this terminal semantics-repair PASS as independently confirmed authority.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden until required subgates close.
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
- missing object/rank/certificate != zero; scoped child result != family closure; green CI != science.
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
