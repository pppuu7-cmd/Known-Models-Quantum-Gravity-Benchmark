# KMQGB Critical Review — Iter504T implementation-control repair rerun preterminal audit

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Review-start main: `b6b6f308670c780e11d7acea223a3ade0b7bde32`
Latest static-audit refresh main: `7c66ad020ae96f5b02b86947f06784a1da42aacc`

## RESULT_REVIEWED

No terminal scientific/repair result is reviewed in this document.

Active authoritative gate:

`ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE`

Authoritative run:

`35205054496`

Latest observed state during this refresh:

`in_progress / conclusion=null`.

Source-lock is terminal success. One substantive root job (`Python 3.13`, root 13) is also terminal success, while the other substantive root jobs remain nonterminal. No substantive root, assembly, aggregate, Critic, repair-verdict, or scientific decision values from the active run were consumed.

## PREREG_CHECK

PASS for prospective repair chronology.

Frozen order is:

- original Iter504T terminal Critic front `51b8a95ed009761e542f8c50efaeca3a98bc2891`;
- repair preregistration `adc7bfb9df77a90455cac1b0f0cb7255d80c44d5`;
- immutable repair authority `a47a9140cf10f2f0f912943133a01238ff1b5653`;
- producer repair `ec619bbe2212fe2affaddbd251d75408d534df88`;
- assembler repair `f9c180abd56e06521f177df06d34651f3f4a28fb`;
- aggregate repair `81e15e0d1586b7ad7d17c616eb0d2fd0f179670b`;
- independent Critic repair `f41e82a97e527c44e60c24d218015661b71e342a`;
- repair-verdict code `e96979b650a67cc960b6f4be6ce37400da5bd88b`;
- repair workflow `9239db6a9b1637dc10889afae289dc6e0908df61`;
- launch head `10ae6bcc8447d14cecc6e550065504b23f792953`.

No repair criterion was found to have been introduced after launch output.

The original scientific preregistration `aa2b0256ce60d605574a18ec86c0bad5b5df1512` remains controlling for the scientific predicate. It freezes `rho_certified := slope_floor_satisfied AND drift_within_tolerance`, then states that a node is certified iff all four rhos are certified, and PASS requires every terminal leaf to be scientifically certified.

## OBJECT_IDENTITY_CHECK

Static PASS for the scientific object; one new decision-binding defect candidate is recorded below.

The repair keeps the original scientific gate `ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION`, original scientific preregistration, roots 13/14/15, rhos 0.35/0.9/1.6/2.7, R grid 6/8/10/12, 243 channels, precision 384, python-flint 0.9.0, threshold 1/20, floor 1, MAX_DEPTH 3, direct local derivative recomputation, original classifier and original interpretation ceiling.

Compare from original launch head `d23f34cba57b220dd29474c0651bc727d6d85eae` to the pre-repair Critic front `51b8a95ed009761e542f8c50efaeca3a98bc2891` changes only Critic/verification/recovery/result files; imported scientific source modules were not changed. Compare from `51b8a95...` to repair launch `10ae6bc...` changes only the prospectively frozen repair files, validator wiring, repair authority/workflow and launch record.

## SOURCE / REALIZATION CHECK

Static PASS, terminal source/artifact provenance pending.

The source-lock job `105148662991` completed successfully before substantive work. The repair workflow source-locks both pre-repair blobs and repaired blobs and verifies the original scientific preregistration blob unchanged.

No change of scientific source route, local-D construction, imported scientific modules, classifier, threshold/floor, cohort values or claim ceiling was found in the repair diff.

## PROVENANCE_CHECK

PRETERMINAL PASS only.

Run `35205054496` is still nonterminal. Only chronology, source-lock success, source code, frozen contracts and job topology were consumed. No active substantive artifact was opened and no scientific value from the one completed root job was consumed.

## SAME_REALIZATION_CHECK

Static PASS.

The repair is implementation-only. Producer changes add two records/controls while leaving the decision-producing local-D calculation intact:

1. `r_cohort_consumed` is derived from the same `core.R_GRID` that is actually iterated, with an exact runtime assertion `(6,8,10,12)`;
2. every visited non-root child receives a componentwise inclusion record comparing its directly recomputed derivative snapshot to the directly recomputed parent snapshot.

The new snapshot path is observational: it reads derivative balls and does not feed back into the scientific `certified` predicate.

## COUNTEREXAMPLE-FIRST STATIC AUDIT

### C1 missing parent-inclusion record

The old counterexample is statically closed.

Producer now emits exactly one record for every visited non-root node. Assembler and Critic require record count `visited_node_count - 1`, unique child identities, a complete parent/child tree, exact midpoint parent-child relation, exact frozen R/rho identities, 4 Haar/log booleans, and 16 x 243 channel inclusion booleans per record.

The Critic explicitly mutates a valid payload by removing a record and requires rejection.

### C1 malformed/incomplete component records

Static rejection path present.

Malformed non-boolean channel entries, wrong R identity, wrong row count, wrong 243-component cardinality, malformed Haar map, duplicate child identity and broken parent relation all produce validator errors.

False inclusion booleans themselves are deliberately retained as diagnostic-only, matching the frozen repair contract.

### C3 exact R cohort

The old counterexample is statically closed.

Producer derives `R_COHORT` from the actually iterated `core.R_GRID` and fails unless it is exactly `(6,8,10,12)`. Top-level `r_cohort_consumed`, leaf `possible_max` R/rho pairs and every inclusion row are independently checked by assembler and Critic.

The repaired Critic includes explicit wrong-top-level-R, missing-R, extra-R and `R=6 -> 7` possible-max mutations and requires rejection.

### Dyadic partition

No repair defect found. The earlier C2 suspicion remains REFUTED. Exact rational dyadic-cell validation and parent-child midpoint validation are retained.

### NEW C4 — terminal-leaf certification is not independently bound to the four rho predicates

Outcome-independent counterexample succeeds against the repaired assembler/Critic wiring.

The original frozen scientific predicate requires:

- for each rho, `rho_certified = slope_floor_satisfied AND drift_within_tolerance`;
- a node is certified iff all four rhos are certified;
- scientific PASS requires every terminal leaf to be scientifically certified.

The repaired assembler and repaired Critic do verify the first relation inside each `per_rho` row. However, neither validates the second relation

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`.

Instead, both trust the producer's top-level `leaf.certified`, check only that `unresolved_leaf_count` equals the number of leaves whose top-level flag is false, and derive PASS/INCONCLUSIVE from that unresolved count. The aggregate and cross-environment projection also carry both the leaf flag and the rho flags but only compare the two environments to each other; they do not enforce the frozen implication between them.

Explicit mutation counterexample: start from any structurally valid depth-3 terminal leaf with one rho row scientifically uncertified. In both environment payloads, leave all four per-rho exact booleans unchanged, change only the top-level `leaf.certified` to `true`, and update `unresolved_leaf_count` consistently. All current assembler validation checks can remain green; the repaired Critic can remain error-free if both lanes receive the same mutation; cross-environment projection remains equal; and the classifier can be promoted from INCONCLUSIVE to PASS despite the frozen scientific predicate still containing an uncertified rho.

The current negative-control suite does not include this mutation. Therefore the repair gate has a new decision-relevant implementation-binding defect candidate independent of the already repaired C1/C3 controls.

This finding does not assert that the active producer actually emitted an inconsistent leaf. No partial active output was inspected. It establishes that the frozen validator/independent-Critic contract would not reject such an inconsistency if it occurred.

## NUMERICAL / STATISTICAL CHECK

Not performed on active outputs because the authoritative workflow is nonterminal.

## OVERCLAIM_CHECK

PASS.

No scientific PASS, repair PASS, FAIL, BLOCKED, INVALID, D7 closure, model/family statement, selector, Candidate Gravity activation or global quantum-gravity claim is issued by this preterminal audit.

## VERDICT

None while run `35205054496` remains nonterminal.

If the launch-head code remains unchanged, any eventual repair PASS must be tested against C4 at terminal review; green CI, cross-environment agreement and a PASS repair-verdict cannot by themselves cure this frozen scientific-predicate binding gap.

## QUALIFICATIONS

- Source-lock success is provenance only.
- C1 and C3 remain statically repaired.
- C2 remains REFUTED and must not be resurrected.
- C4 concerns validator binding of the frozen leaf predicate, not evidence that the current producer result is scientifically wrong.
- No partial substantive values were consumed.
- Historical run `35181094204` and its independent `INVALID_IMPLEMENTATION` review remain immutable.

## UPDATED_STATE

`ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE = ACTIVE / NOT CLASSIFIED`.

The two previously verified implementation defects appear statically repaired, but one new outcome-independent decision-binding counterexample now survives: top-level terminal-leaf certification is not independently constrained to equal conjunction of the four frozen rho-certified predicates.

Governance remains unchanged: RQIR Core v1.0 FROZEN; BLOCKED != FAIL; INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL; finite certificate != universal theorem; scoped child result != family closure; D7 required subgates remain unclosed; terminal selectors remain forbidden; Candidate Gravity remains inactive.

## NEXT_ADMISSIBLE_GATE

Do not launch a competing same-object gate while run `35205054496` is nonterminal.

After the run fully terminalizes, consume only the terminal aggregate, repaired independent Critic, repair-verdict, job chronology and artifact digests. Test any terminal repair/scientific classification against C4 in addition to the frozen repair contract. If the launch-head code is unchanged and the terminal repair verdict is PASS, the independent terminal Critic must determine whether the missing leaf-to-rho binding constitutes `INVALID_IMPLEMENTATION` under the original preregistered scientific predicate.

A same-contract implementation repair can close C4 by requiring in assembler and Critic that every leaf's top-level `certified` boolean equals exact conjunction of its four `per_rho[*].certified` booleans, and by adding an adversarial mutation that flips only the top-level leaf flag. This does not require changing the scientific object or threshold. Any change to the scientific predicate itself, source/domain/classifier/threshold/floor/cohort values or interpretation ceiling requires a new prospectively frozen gate.