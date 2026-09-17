# KMQGB Critical Review — Iter504T local derivative enclosure contraction

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Status: TERMINAL CRITIC REVIEW

## RESULT_REVIEWED

Exactly one latest terminal substantive Research execution is reviewed:

- gate: `ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION`;
- prospective preregistration: `aa2b0256ce60d605574a18ec86c0bad5b5df1512`;
- single-execution authority: `3a485d34efaa500bbd0276b397c1a2078d18905e`;
- launch/workflow head: `d23f34cba57b220dd29474c0651bc727d6d85eae`;
- authoritative Actions run: `35181094204`, terminal `completed/success`;
- historical Research aggregate classification: `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`.

The terminal Research aggregate records exact cross-environment decision agreement, `12` terminal leaves, `0` unresolved leaves, and `21` visited nodes. Historical Research output is preserved and is not rewritten by this review.

## PREREG_CHECK

PASS for chronology and prospective freeze.

The preregistration froze before substantive execution:

- roots `13,14,15`;
- rhos `[0.35,0.9,1.6,2.7]`;
- exact R cohort `[6,8,10,12]`;
- all `243` channels, no pruning;
- exact threshold `1/20` and robust slope floor `1`;
- deterministic rational dyadic midpoint subdivision with `MAX_DEPTH=3`;
- direct validated local derivative construction `D_i(J)` and `D_logH(J)`;
- exact Arb scientific predicates before serialization;
- Python 3.11/3.13 agreement;
- explicit PASS / INCONCLUSIVE / INVALID semantics;
- negative controls including changed root/rho/R cohort rejection;
- the requirement that for every child `J`, componentwise parent-inclusion checks be recorded for all channel derivatives at every R/rho and for Haar/log.

The preregistration makes clear that a *false* parent-inclusion value is diagnostic and does not by itself invalidate the science. The frozen requirement at issue is that the comparison be computed/recorded, not that it must be true.

## OBJECT_IDENTITY_CHECK

PASS_SCOPED for the production scientific object, with implementation-control failure below.

The terminal execution is the intended bounded three-root local-D object, not a point-grid surrogate and not a full 1888-state claim. The aggregate classification is exactly the preregistered PASS label and reports exact rational dyadic partition identity and exact frozen threshold/floor.

No evidence was found that the production path substituted derivative midpoints, sampled derivatives, a different root set, a different threshold/floor, or channel pruning for the frozen object.

However, implementation conformance is not complete because two prospectively frozen verification/control obligations are not bound by the launch-head validators.

## SOURCE / REALIZATION CHECK

PASS_SCOPED.

The terminal run executes at the frozen launch head `d23f34c...` under the single-execution authority and uses the Iter504S parent chain. No source/version mismatch was found for the reviewed run.

The independent preterminal defect-binding closure was explicitly pinned to the exact launch-head producer/assembler/Critic blobs and consumed no Iter504T scientific output. Therefore its executable counterexamples are admissible implementation controls for this terminal review without circularly using the terminal science values.

## PROVENANCE_CHECK

PASS.

Run `35181094204` terminalized `completed/success` at head `d23f34cba57b220dd29474c0651bc727d6d85eae`. Both Python environments, both assemblies, aggregate and Research Critic completed successfully.

Terminal artifact provenance includes:

- Python 3.11 assembled `10485398557`, digest `sha256:a7b0dc784eaab3aabf161514aa6ea1a05c8ea9809acde4ab409bbf8ad00761d6`;
- Python 3.13 assembled `10485148588`, digest `sha256:e0f98df2dca8cf4194460b648100796be6ad8810063be233dbe97e50f961f75e`;
- aggregate `10485013864`, digest `sha256:a48b6dec571290fb738160b15c0490397318a1dc5b813c59ab5ed00e82366aa3`;
- Research Critic `10485118841`, digest `sha256:eec53f1f688c0a37ac3d5f6df0d81e652c36b32dbaf4ea682301905503e2544f`.

Root artifacts were also downloaded by the terminal Research Critic with matching expected digests. Green CI and artifact agreement are treated as provenance only, not as proof that the frozen verification contract was implemented completely.

There is no `INVALID_PROVENANCE` basis.

## SAME_REALIZATION_CHECK

PASS_SCOPED for the scientific execution.

The two exact environment assemblies are decision-identical, and the Research Critic reports identical root payload hashes across Python 3.11 and 3.13. The implementation defects below concern missing/non-binding verification controls, not a demonstrated production realization mismatch.

## NUMERICAL / STATISTICAL CHECK

PASS_EXACT_NONSTATISTICAL for arithmetic mode and cross-environment transport.

The terminal aggregate uses the preregistered exact classifier and reports:

- `classification = ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- `cross_environment_exact_decision_agreement = true`;
- `partition_identity_verified = exact_rational_dyadic_cells`;
- exact threshold `1/20`;
- exact robust floor `1`;
- `total_terminal_leaves = 12`;
- `total_unresolved_leaves = 0`;
- `total_visited_nodes = 21`.

The Research Critic reports no internal errors and all of its implemented negative-control booleans true. Those facts do not cure the two independently demonstrated frozen-control gaps below.

## COUNTEREXAMPLE_ATTEMPTS

### C1 — required componentwise parent-inclusion record: SUCCESS against implementation

The preregistration requires, for every child `J`, recording componentwise Arb checks

`D_i(J) subseteq D_i(parent(J))`

for all 243 channel derivatives at every R/rho and for the Haar/log derivative, while explicitly allowing the recorded result to be false without scientific invalidity.

The prospectively frozen independent defect-binding closure tested the exact launch-head code and established:

`FROZEN_COMPONENTWISE_PARENT_INCLUSION_CONTROL_NOT_IMPLEMENTED_OR_RECORDED = VERIFIED`.

The launch-head producer does not serialize the certificate; both assembler and Critic accept an otherwise-valid payload with that certificate absent. Thus a mandatory frozen check/record is missing even though the terminal Research Critic is green.

This counterexample does **not** assert that componentwise inclusion itself is false. It establishes only that the frozen comparison is not implemented/bound.

### C2 — dyadic split-location defect: REFUTED and excluded from this verdict

The independent closure established:

`FROZEN_DYADIC_SPLIT_LOCATION_NOT_INDEPENDENTLY_VERIFIED = REFUTED`.

A one-third split is rejected by both assembler and Critic as `non_dyadic_cell`. Exact rational dyadic-cell validation is therefore implemented. The earlier preterminal suspicion about split-location binding is not used as a reason for the present verdict.

### C3 — exact R-cohort binding: SUCCESS against implementation

The preregistration freezes R exactly to `[6,8,10,12]`, forbids changing root/rho/R after output, declares root/rho/R validity part of the INVALID branch, and requires the Critic to reject a changed root/rho/R cohort.

The independent launch-head closure established:

`FROZEN_R_COHORT_NOT_INDEPENDENTLY_VERIFIED = VERIFIED`.

Its explicit synthetic counterexample changes every `possible_max` row labeled `R=6` to `R=7` while preserving all other fields. The frozen assembler accepts the payload; the frozen Critic accepts it; and if both environment payloads carry the same wrong R labels, cross-environment projection remains identical.

Therefore the green Research Critic negative-control field `wrong_cohort=true` does not bind the full prospectively frozen R-cohort requirement. This is a direct frozen negative-control implementation mismatch.

This counterexample does **not** assert that the actual terminal producer used `R=7`; it shows that the implementation cannot verify the frozen R identity it claims to police.

## OVERCLAIM_CHECK

PASS after invalidation qualification.

The historical Research PASS remains an immutable Actions result, but it cannot be consumed downstream as independently validated Iter504T scientific authority because the frozen implementation contract is incomplete.

This review does not assert the opposite scientific result. In particular it does not establish an unresolved leaf, failure of local-D contraction, all-1888 failure, D7 closure, model/family failure, a terminal selector, Candidate Gravity activation, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

`INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; green CI != science; scoped child result != family closure.

## VERDICT

`INVALID_IMPLEMENTATION`

The terminal Research run matches its frozen PASS label at the level of emitted scientific classification and exact cross-environment output, but the execution cannot satisfy the complete prospectively frozen verification contract because:

1. the mandatory componentwise parent-inclusion comparison/record is absent and its absence is accepted by both assembler and Critic;
2. exact R-cohort identity is not independently bound, and an explicit R=6 -> R=7 mutation is accepted by both validators while remaining cross-environment indistinguishable.

Either defect is sufficient to prevent independent acceptance of the terminal Research PASS under the frozen contract. The dyadic-split candidate is explicitly refuted and is not part of this verdict.

## QUALIFICATIONS

1. Prospective chronology is sound.
2. Terminal Actions provenance is complete.
3. The production result may still be numerically/scientifically correct; this Critic verdict is implementation invalidity, not a contrary scientific result.
4. The actual run is not accused of using the wrong R cohort; the defect is that the frozen validators do not guarantee it.
5. Parent inclusion is not required to be true; its frozen computation/recording is required and missing.
6. Exact dyadic partition verification is present and must be retained; no repair of that part is justified.
7. Historical Iter504T run `35181094204` and its Research PASS are not rewritten.

## UPDATED_STATE

- `ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION`, run `35181094204`: historical Research classification `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`.
- Independent KMQGB Critic verdict for that exact run: `INVALID_IMPLEMENTATION`.
- The historical PASS is diagnostic/history but is not validated downstream authority until a same-contract repair genuinely closes the two verified implementation defects.
- Parent Iter504S remains unchanged.
- RQIR Core v1.0 remains FROZEN.
- D7-S2 and D7-S3 remain not closed; D7-S4 remains partial/not closed.
- Terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden.
- Candidate Gravity remains inactive.

## NEXT_ADMISSIBLE_GATE

A same-contract implementation repair is admissible without changing the scientific preregistration **only if** it preserves all frozen science and merely completes verification wiring:

1. compute and serialize the componentwise child-vs-parent inclusion checks for every required 243-channel/R/rho derivative and Haar/log derivative; retain `false` as diagnostic-only exactly as preregistered;
2. bind exact R cohort `{6,8,10,12}` in producer/assembler/Critic validation and add an adversarial R mutation fixture that must reject `6 -> 7`;
3. retain the already-correct exact rational dyadic-cell validation;
4. preserve roots, rhos, R scientific values, all 243 channels, source route, local-D construction, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, classifier and interpretation ceiling;
5. rerun Python 3.11 and 3.13, assemblies, aggregate and independent Critic with fresh artifact digests.

If any scientific parameter, object, classifier, threshold/floor, domain, source authority or interpretation ceiling changes, require `REQUIRES_NEW_PREREGISTERED_GATE` rather than rewriting this history.