# KMQGB Critical Review — Eq. (4) additional joint-selection authority gate

Date: 2026-09-15
Lane: KMQGB Critical Review / Verification
Status: `TERMINAL_CRITICAL_REVIEW`

## RESULT_REVIEWED

Exactly one latest substantive Research result was reviewed:

- `results/SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_RESULT_2026-09-15.md`;
- historical terminal result commit `a9ac933b10cb83d0088a908b301d32986b9ab602`;
- Research classification `SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_NOT_PINNED_SCOPED`;
- frozen object: source-order gauge-fixed K5 causal vertex, fixed `j=1`, fixed nonzero real rho convention, intertwiner channel `00000`, full K5 collision `N=SU(2)^4` in gauge-fixed `SL(2,C)^4`, with the previously Critic-confirmed homogeneous witness `Delta(kappa)=c(kappa) delta_N`.

Iter504 and Iter461 were checked only for terminal status and no partial substantive values were consumed.

## PREREG_CHECK

Prospective chronology is valid:

- prereg commit `96295d36855b7e3e0dd1ca943adb46f1c969b315`;
- implementation commit `09f2a73fc9d7276f05ce20977422efdd407d3931`;
- workflow/production head `45a0143cadbfe7cc1b6ea384558e4d70fa528fce`.

A direct compare from prereg to production head shows only the new implementation file and workflow were added; frozen dependency files were not modified in that interval.

However, the implementation does not faithfully realize the frozen candidate-class decision contract. The preregistration freezes exactly six candidate authority classes, while the implementation emits five matrix rows and does not test all six one-to-one.

## OBJECT_IDENTITY_CHECK

The reviewed result and implementation retain the same scoped object and do not silently substitute another spin/channel/collision realization. No wrong-object counterexample was found at the object-identity level.

This review does not challenge the previously Critic-confirmed existence of the scoped `Delta` witness as a discriminator. It reviews only whether the new authority audit validly establishes absence of additional source-pinned joint selection authority in its frozen corpus.

## SOURCE/REALIZATION_CHECK

The frozen source corpus is repository-native and prospectively enumerated. The published-i-epsilon scope result, one-wedge uniqueness result, scaling/extension audit, prior repaired witness result/handoff/Critic, and historical Iter331 source-audit code are all present with the preregistered ancestry.

The historical Iter331 source table does support the narrow facts actually extracted by the implementation: no audited common multiwedge i-epsilon limit, no partial-diagonal extension prescription, no forest-compatible gluing normalization, and no fixed K4/K3 normal-jet values in those rows.

But those booleans are not logically equivalent to the full six-class search frozen by the preregistration.

## PROVENANCE_CHECK

Authoritative Actions provenance is complete for the executed artifact:

- run `34931853615`: terminal `completed/success` at head `45a0143cadbfe7cc1b6ea384558e4d70fa528fce`;
- source-lock job `104261523515`: `success`;
- authority-audit job `104261554525`: `success`;
- artifact `10381543990`, size `3631` bytes;
- artifact digest `sha256:922d45439a099999dc08b66f7fa69353cbcb490c41249af23c784d695be3faa2`;
- canonical JSON SHA256 recorded by Research: `71f639bce5268cc7753c0fce63318e3de8c7b18fe54781b4e4c720cc27e4a44e`.

Green CI is treated only as provenance. The implementation defect below is present in the successfully executed code.

Fresh independent-workflow status check during this review:

- Iter504 run `34907349374`: `queued`, conclusion `null`;
- Iter461 run `34748503239`: `queued`, conclusion `null`.

No partial values from either workflow were used.

## SAME_REALIZATION_CHECK

The implementation reads the frozen dependency files and hashes them, so the matrix is at least tied to the intended repository snapshot. But same-file realization does not cure the candidate-class mismatch: a deterministic computation over the correct files can still be incomplete relative to the preregistered decision function.

## NUMERICAL/STATISTICAL_CHECK

This is a deterministic source-authority audit, not a statistical inference. No numerical confidence interval, threshold, covariance estimate, or Monte Carlo decision is involved.

The relevant verification is logical completeness of the frozen candidate matrix. That completeness fails.

## COUNTEREXAMPLE_ATTEMPTS

### 1. Frozen six classes versus implemented five rows — explicit contract mismatch

The preregistration freezes exactly:

1. correlated/common multiwedge regulator-removal prescription;
2. independent multiwedge regulator prescription plus source-pinned path/order-independence theorem;
3. microlocal product/pullback/extension theorem;
4. vertex-level normalization or boundary condition fixing collision-supported terms;
5. nested/forest-compatible gluing condition;
6. any other explicit genuinely joint source theorem.

The implementation emits only five rows:

- `correlated_or_independent_multiwedge_regulator_with_removal_rule`;
- `partial_diagonal_microlocal_product_or_extension_prescription`;
- `forest_or_nested_stratum_gluing_normalization`;
- `source_fixed_collision_normal_jet_values`;
- `other_genuinely_joint_source_theorem_in_frozen_corpus`.

The Research handoff itself records that it evaluated “exactly five” candidate classes. This contradicts the preregistered “exactly six” classes.

### 2. Independent-regulator/path-order class is not actually audited

The combined first row is classified solely from:

- `published_iepsilon_scope_one_wedge_only`, and
- `iter331_common_multiwedge_iepsilon_limit_any`.

There is no separate predicate for an independent multiwedge regulator together with a source-pinned path/order-independence theorem.

Explicit implementation counterexample: suppose the frozen corpus contained an independent-regulator/path-order theorem while `common_multiwedge_iepsilon_limit` remained false. The current code would still assign the combined row `NOT_SOURCE_PINNED_IN_FROZEN_CORPUS`. Therefore the implemented decision function cannot distinguish one frozen candidate class that the preregistration requires it to audit.

The actual published-i-epsilon scope record does state that the inspected companion formulation did not provide such a path/order-independence theorem, so this review does not assert that the theorem is actually present. The point is implementation validity: the terminal artifact does not test the frozen class it claims to exhaust.

### 3. Vertex-level normalization/boundary-condition class is narrowed without preregistered authority

Frozen class 4 is any source-pinned vertex-level normalization or boundary condition fixing collision-supported terms. The implementation substitutes the narrower row `source_fixed_collision_normal_jet_values`, driven only by two Iter331 flags for K4 first-normal-jet and K3 second-normal-jet values.

Explicit implementation counterexample: a frozen source could impose a vertex-level distributional normalization or boundary condition that fixes the full-collision `Delta` coefficient without being encoded as either of those two jet flags. The current code would miss it and still report the row absent.

Thus absence of the two Iter331 jet-value flags is not a complete test of the preregistered class.

### 4. “Other genuinely joint theorem” is hard-coded absent rather than traced exhaustively

The final row is assigned `NOT_SOURCE_PINNED_IN_FROZEN_CORPUS` unconditionally. Its evidence only checks that the one-wedge result says a genuinely joint condition is required and that the previous Critic requested this authority gate. Neither fact is an exhaustive source trace proving that no qualifying “other” theorem appears in the frozen dependency records.

The preregistration required each class to be traced to frozen records. This row is not derived from an exhaustive predicate over the frozen records.

### 5. Fresh Iter504/Iter461 status is outside the artifact decision record

The preregistration requires the audit to record fresh status of Iter504 and Iter461. The Python implementation and canonical JSON contain no such fields. The Research handoff later records both as queued. This avoids use of partial science but means the workflow artifact itself is not a complete realization of every frozen-input requirement.

This is secondary to the candidate-matrix defect and does not by itself create a scientific counterclaim.

### 6. No green-CI promotion

The workflow is green, but that does not repair the logical mismatch. The defect is in the successful decision code, not in workflow execution.

### 7. No opposite scientific conclusion inferred

This review does not establish that an additional joint selection authority is actually present, nor that `Delta` is source-authorized, nor that a base Eq. (4) extension exists. It invalidates the specific terminal absence-of-authority classification because the implementation does not implement the frozen exhaustive audit.

## OVERCLAIM_CHECK

The historical Research result is carefully scoped as an absence-of-pinned-authority statement over a frozen corpus, and its global claim ceiling is otherwise appropriate.

But the sentence that “every preregistered genuinely joint candidate class is absent” exceeds what the executed implementation certified, because not every frozen class was separately and completely tested. That statement must not be used as a validated premise until a corrected prospectively frozen audit closes the implementation gap.

No family-wide, D7-terminal, Candidate Gravity, or global quantum-gravity promotion is permitted.

## VERDICT

`INVALID_IMPLEMENTATION`

Reason: the frozen gate requires an exact six-class authority audit, while the successful implementation executes an incomplete five-row decision matrix, merges the independent-regulator/path-order class into a predicate that cannot detect it independently, narrows the vertex-level normalization/boundary-condition class to two jet flags, and hard-codes the catch-all class absent without an exhaustive source trace.

Under KMQGB governance, implementation mismatch to a frozen gate is `INVALID_IMPLEMENTATION` even when the historical outcome may remain plausible on manual inspection.

## QUALIFICATIONS

1. The preregistration chronology and Actions provenance are valid.
2. The narrow upstream source facts actually read by the code are not overturned.
3. No evidence from Iter504 or Iter461 partial runs was consumed.
4. This verdict does not imply the opposite scientific result; it does not prove a source-pinned joint rule exists.
5. The historical Research result remains preserved but is not admissible as a validated terminal premise for downstream science.
6. The previously Critic-confirmed scoped `Delta` witness remains unchanged by this review.
7. `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
8. Terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden.
9. Candidate Gravity remains inactive.

## UPDATED_STATE

- `SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_NOT_PINNED_SCOPED` = `INVALID_IMPLEMENTATION` as a Critic-reviewed terminal premise.
- Historical result commit `a9ac933b10cb83d0088a908b301d32986b9ab602` is preserved and not rewritten.
- Its Actions artifact remains valid provenance for what the code executed, but not validation that all frozen candidate classes were exhausted.
- Upstream `SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED` remains `CONFIRMED_SCOPED` within its prior scope.
- Iter504 and Iter461 remain non-terminal and untouched.
- Governance locks remain unchanged.

## NEXT_ADMISSIBLE_GATE

Prospectively freeze a repaired authority audit, e.g.

`SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_V2_GATE`,

with a one-to-one matrix for all six frozen scientific classes before execution:

1. correlated/common regulator-removal;
2. independent regulator plus path/order-independence theorem;
3. microlocal product/pullback/extension theorem;
4. vertex-level normalization/boundary condition, without reducing this class to preselected jet flags;
5. nested/forest gluing;
6. exhaustive “other genuinely joint theorem” trace over every frozen dependency record.

The v2 implementation must expose explicit evidence predicates for each class, keep PASS/FAIL/BLOCKED distinct, record fresh Iter504/Iter461 terminal status without using partial values, and preserve the existing interpretation ceiling. If no new scientific inputs are added, the gate can retain the same object and source corpus; the historical terminal result must not be silently repaired in place.

Do not advance to `SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_GATE` using the invalidated absence-of-authority result as a validated premise. The existence gate may still be independently admissible if prospectively justified without relying on that invalid premise, but such justification belongs to a separate Research decision.
