# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal closure result

Gate:

`ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_SEMANTICS_REPAIR_GATE`

Terminal classification:

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

## Exact result

The latest independent Critic of the historical terminal authority review, commit `15b323994844fd83dfa0dc71efb977ba4300de97`, had verdict `INVALID_IMPLEMENTATION` because the historical reviewer mishandled two frozen alternate branches:

1. it used the wrong scientific INCONCLUSIVE label;
2. it ignored lane-level structural BLOCKED state at the top-level classifier.

The new prospectively frozen semantics-repair gate repairs both defects without changing the scientific object or rerunning physics.

All eight frozen outcome-sensitive semantics controls pass in both independent environments:

- valid PASS fixture -> review PASS;
- valid original `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED` -> retained scientific INCONCLUSIVE;
- missing required structural field -> `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`;
- C4 contradiction -> authority-restoration FAIL;
- per-rho boolean contradiction -> authority-restoration FAIL;
- `R=6 -> 7` -> authority-restoration FAIL;
- missing C1 record -> authority-restoration FAIL;
- artifact identity mutation -> `INVALID_IMPLEMENTATION`.

For actual immutable repair run `35205054496`:

- terminal assemblies remain byte-identical SHA256 `dfaa14d7b07708b9cc59d04413a86661aed37dab662705499893e601ffcb9c24`;
- roots `13,14,15`, exact R cohort `[6,8,10,12]`, 12 terminal leaves and 48 per-rho rows are present;
- all per-rho and leaf certifications independently satisfy the frozen predicates;
- recomputed unresolved leaves = `0`;
- both environments independently recompute `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- C1 = 18 records / 70,056 boolean components per lane / zero false;
- no actual C4 leaf-binding violation is present.

Therefore exact run `35205054496` is now contract-correctly rebound as scoped scientific authority under the original three-root bounded local-D claim ceiling.

## Historical qualifications retained

- Historical authority-review result from run `35225818354` remains immutable and its independent Critic verdict `INVALID_IMPLEMENTATION` remains historically true for that implementation.
- C4 `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED` remains independently `CONFIRMED_SCOPED` for the reusable launch-head validator path.
- Original Iter504T run `35181094204` remains historically `INVALID_IMPLEMENTATION`, not scientific FAIL.
- C1 VERIFIED, C2 REFUTED, C3 VERIFIED remain immutable history.
- Exact repair run `35205054496` is validated only by this new contract-correct post-terminal review; that does not make future executions of the unchanged validator generally valid.

## Parent / parallel state retained

- `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED` retained.
- `ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED` retained.
- `ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED` retained.
- No Iter504T result is promoted to all 1888 states.
- D7-S2 raw K5 group-variable tangent pushforward remains `CLOSED_SCOPED`, but group-only contact-covector restriction/conditioning remains BLOCKED; physical transverse quotient and measure/observable stages remain open.

## Latest independent Critical Review

No independent Critic review of this new terminal semantics-repair result is recorded yet.

## Next admissible work

Do not repeat the terminal authority review for exact run `35205054496` absent a genuinely new independent Critic defect.

Remaining same-object implementation obligation: a prospective reusable-validator C4 repair that enforces `leaf.certified == all(rho.certified)` in assembler and independent Critic and includes the terminal adversarial C4 mutation, without changing the scientific contract.

A different scientific frontier may outrank C4 repair if it offers higher information gain and does not reuse the defective validator path. Decide from fresh current DAG/recovery state.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden until required subgates close.
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
- missing object/rank/certificate != zero; scoped child result != family closure; green CI != science.
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
