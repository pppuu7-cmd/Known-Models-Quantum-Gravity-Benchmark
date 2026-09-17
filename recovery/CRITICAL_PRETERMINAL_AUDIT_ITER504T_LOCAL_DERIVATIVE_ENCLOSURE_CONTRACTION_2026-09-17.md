# KMQGB Critical Preterminal Audit — Iter504T local-D derivative enclosure contraction

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Status: PRETERMINAL — NO SCIENTIFIC VERDICT

## RESULT_REVIEWED

No terminal Iter504T scientific result is reviewed in this audit.

Fresh scientific execution head:

`d23f34cba57b220dd29474c0651bc727d6d85eae`

Active authoritative scientific workflow:

- gate: `ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION`;
- workflow: `KMQGB Iter504T local-D bounded science`;
- Actions run: `35181094204`;
- head: `d23f34cba57b220dd29474c0651bc727d6d85eae`;
- state at latest Critic refresh: `in_progress / conclusion=null`.

Latest job-state refresh, with no substantive payload values consumed:

- source-lock `105073194770`: `completed/success`;
- Python 3.11 root 13 `105073218689`: `completed/success`;
- Python 3.11 root 14 `105073218688`: `completed/success`;
- Python 3.11 root 15 `105073218687`: still `in_progress`;
- all Python 3.13 roots 13/14/15 remain `in_progress`;
- assembly, aggregate and Critic are not terminal/available as authoritative terminal output.

Completed root artifacts are partial substantive outputs and were deliberately not opened or consumed.

The latest terminal parent remains Iter504S:

`ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`

with terminal record commit `1b0004064575f046210383dc7b1ee22d4f25e66b` and authoritative run `35178186905`.

## PREREG_CHECK

PASS for prospective chronology.

Frozen Iter504T preregistration:

`aa2b0256ce60d605574a18ec86c0bad5b5df1512`

The preregistration precedes implementation, methodology hardening, pre-execution audit, single-execution authority and launch. The single-execution authority `3a485d34efaa500bbd0276b397c1a2078d18905e` pins:

- preregistration `aa2b0256...`;
- parent terminal commit `1b000406...`;
- outcome-blind toolkit `81e0e946...`;
- pre-execution audit `e2c9ed47...`;
- successful methodology CI run `35180986268`;
- exact evaluator/assembler/aggregate/Critic/workflow blob SHAs;
- Python 3.11/3.13, `python-flint==0.9.0`, 384 bits;
- roots 13/14/15, all 243 channels, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, deterministic dyadic partition and no post-outcome depth extension.

No chronology defect or post-hoc scientific parameter change was found.

## FROZEN CONTRACT AUDIT

The preregistration freezes the local derivative construction on every visited interval `J`, exact midpoint mean-value enclosure, exact Arb scientific predicates, deterministic dyadic subdivision and three terminal classes PASS / INCONCLUSIVE / INVALID.

It freezes three implementation/verification requirements material to this audit:

1. at depth 0 construct `D(I)` and, for every child `J`, record componentwise Arb containment checks `D_i(J) subseteq D_i(parent(J))` for all 243 channel derivatives at every R/rho and for Haar/log where meaningful;
2. the Critic must reject an outcome-dependent/non-dyadic split location;
3. the Critic must reject a changed root/rho/R cohort.

Containment truth is explicitly diagnostic rather than a PASS condition: a recorded false inclusion does not by itself invalidate the local construction. What is frozen is that the check is actually performed/recorded, and that claimed contraction is not inferred from widths alone.

## OBJECT_IDENTITY_CHECK

Static PASS for the intended local-D object, with frozen-control implementation defect candidates.

The evaluator constructs each visited `J` directly as an Arb interval amplitude with derivative seed 1 and recomputes the source realization. Midpoint ordinary values are separately recomputed at the exact rational midpoint. Channel and Haar/log mean-value enclosures use derivative components from the local dual construction. The code does not substitute sampled derivatives, finite differences, or the Iter504S center derivative as scientific truth.

However, the evaluator never computes or serializes the preregistered child-to-parent componentwise inclusion certificate. Returned leaf records contain `validated_local_derivative=true`, exact interval/depth identity, scientific booleans and possible-max information, but no `componentwise_parent_inclusion` field, no per-channel/R/rho inclusion map and no Haar/log inclusion record.

## SOURCE / REALIZATION CHECK

Static PASS for source identity and frozen execution authority.

The active source-lock job passed against the exact frozen blob authority. The current evaluator source preserves the fixed roots, path, direction/sign, rho/R cohort, 243-channel cube, precision and exact decision constants.

No wrong-source or wrong-realization counterexample has been established. The additional counterexamples below target verification binding: payloads that violate frozen partition/cohort contracts but are accepted by the current assembler/Critic.

## PROVENANCE_CHECK

PRETERMINAL PASS for chronology/source lock only.

Run `35181094204` remains `in_progress / conclusion=null`. Some root jobs have now completed successfully, but their root payloads remain partial substantive outputs and were not read. Since the cross-environment assembly, aggregate and independent Critic are non-terminal/not authoritative, no terminal provenance or science verdict is issued.

## SAME_REALIZATION_CHECK

Static PASS for the intended child construction; pending terminal artifact audit.

Every visited child interval is intended to recompute its own dual/source object rather than reuse the root derivative enclosure. This is materially different from Iter504R and is consistent with the Iter504T scientific object.

The unresolved issues are verification binding: the current scientific record can assert correct construction/partition/cohort metadata without the assembler/Critic independently establishing several frozen properties from the serialized object.

## NUMERICAL / STATISTICAL CHECK

No terminal or partial substantive numbers were consumed.

Static inspection confirms that threshold/floor decisions are made as Arb comparisons before binary64 display serialization. Any numerical conclusion awaits terminal Actions authority.

## COUNTEREXAMPLE_ATTEMPTS

### 1. Frozen parent-inclusion control binding — explicit counterexample succeeds

Construct two otherwise identical root payloads:

A. one implementation actually computes and records every preregistered `D_i(J) subseteq D_i(parent(J))` and Haar/log inclusion result;

B. one implementation omits every such check and record while preserving the same leaves, exact scientific booleans, dyadic cover, metadata and possible-max fields.

The current producer is of type B. The current assembler and adversarial Critic accept payload B because neither requires any parent-inclusion field or checks any componentwise derivative containment.

Thus the mandatory frozen record/control requirement is non-binding: omission is observationally invisible to the current gate machinery.

### 2. Frozen deterministic-dyadic split control — explicit payload counterexample succeeds

The preregistration requires every unresolved node to split exactly at its rational midpoint and explicitly requires the Critic to reject an outcome-dependent split location.

The current assembler/Critic do not reconstruct the dyadic tree. They check only:

- the top-level string `partition_rule == "deterministic_dyadic_midpoint"`;
- each leaf depth is at most 3;
- terminal leaf intervals form an exact contiguous cover of the root.

For root 13 the frozen root is

`I = [29/12800, 30/12800]`.

A depth-1 payload with two otherwise valid leaves

- `[29/12800, 11/4800]`,
- `[11/4800, 30/12800]`,

covers the root exactly but splits at one third of the interval rather than the midpoint. If its metadata string remains `deterministic_dyadic_midpoint` and its scientific booleans are internally consistent, the current `validate()` cover/depth checks do not reject it.

Therefore the frozen negative control "outcome-dependent split location" is not independently enforced by the serialized-record Critic. A non-dyadic/adaptive partition can be relabeled with the expected metadata string and pass this part of verification.

### 3. Frozen R-cohort control — explicit payload counterexample succeeds

The preregistration freezes `R=[6,8,10,12]` and requires the Critic to reject a changed root/rho/R cohort.

The Critic explicitly validates the rho tuple in `per_rho`, but it never validates the expected R set in `possible_max`. Its `wrong_cohort` negative fixture mutates a rho to `0.36`; there is no R-cohort mutation fixture.

Consequently, take an otherwise valid payload and replace every `possible_max` record with `R=6` by `R=7`, applying the same mutation in both Python-lane payloads. The current validator checks only that the channel indices are unique integers in `[0,242]`; it does not reject `R=7`, does not require exactly the set `{6,8,10,12}`, and cross-environment projection still agrees if both lanes carry the same wrong R labels.

Hence the mandatory changed-R-cohort adversarial control is non-binding in the current implementation.

### 4. Pre-execution audit cannot weaken preregistration

The later outcome-blind pre-execution note states that componentwise nesting is an "optional diagnostic/certificate" and correctly notes that failure of nesting is not evidence of invalidity.

The second statement is consistent with the preregistration. The first cannot remove the preregistered requirement to record the checks for every child where meaningful. A later source audit cannot silently relax a prospectively frozen control after preregistration.

### 5. Green CI promoted to science

Rejected. Methodology CI, source lock and individual successful root jobs establish execution/provenance properties only. They cannot repair missing/non-binding frozen controls.

## OVERCLAIM_CHECK

No Iter504T PASS, INCONCLUSIVE, INVALID or independent terminal Critic verdict is issued while the authoritative workflow is non-terminal.

No conclusion is drawn about all 1888 states, D7 closure, model/family closure, terminal selectors, Candidate Gravity, quantum gravity, new theory or new physics.

## VERDICT

None — authoritative Iter504T workflow is non-terminal.

Prepared terminal-review implementation-defect candidates:

- `FROZEN_COMPONENTWISE_PARENT_INCLUSION_CONTROL_NOT_IMPLEMENTED_OR_RECORDED`;
- `FROZEN_DYADIC_SPLIT_LOCATION_NOT_INDEPENDENTLY_VERIFIED`;
- `FROZEN_R_COHORT_NOT_INDEPENDENTLY_VERIFIED`.

If execution source remains unchanged through terminalization, any Research PASS or INCONCLUSIVE classification must be audited against these frozen-contract mismatches before downstream scientific consumption. `INVALID_IMPLEMENTATION` is the appropriate terminal Critic branch if these omissions remain and no stronger fresh authority changes implementation status.

## QUALIFICATIONS

1. This audit does not claim that any child derivative enclosure fails inclusion; no substantive child derivative output was read.
2. Inclusion false is allowed diagnostically; missing/unperformed inclusion checking is the defect.
3. The partition/R counterexamples are verification counterexamples: they show malformed payloads that current assembler/Critic would accept. They do not allege that the active producer actually changed the frozen partition or R grid.
4. A contract-preserving repair can add these checks without changing scientific PASS/INCONCLUSIVE semantics.
5. Making `componentwise_parent_inclusion=true` a mandatory PASS predicate, changing depth/partition, changing the R cohort, or changing any scientific threshold/object would require new prospective authority rather than a historical rewrite.

## UPDATED_STATE

- Fresh repository main at this audit refresh was `cd3fbfe2783399c6fdf0893d2efe7a29a28de705` before this Critic update.
- Iter504S remains the latest terminal parent authority.
- Iter504T run `35181094204` remains active/non-terminal.
- No competing scientific classification has been created and no partial substantive root values were consumed.
- Three outcome-independent frozen-control/verification implementation defect candidates are now durably recorded for terminal review.
- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal selectors remain unauthorized; Candidate Gravity remains inactive.

## NEXT_ADMISSIBLE_GATE

First consume only the terminal authoritative Iter504T run, assemblies, aggregate, Critic and artifact/digest provenance when run `35181094204` becomes terminal. Then audit its historical classifier against all three preregistered-control mismatches before accepting PASS or INCONCLUSIVE downstream.

If repair is needed, it is implementation-only under the same frozen science provided it merely:

1. computes/records child-to-parent componentwise inclusion for all frozen channel derivative objects and Haar/log where meaningful, while treating recorded true/false as diagnostic;
2. reconstructs and validates the exact dyadic parent/child midpoint tree from serialized rational interval identities instead of trusting the `partition_rule` label;
3. validates exactly the frozen R cohort `{6,8,10,12}` at every leaf/rho and includes a changed-R adversarial fixture;
4. binds assembler/Critic to these records and preserves roots, depth, local-D construction, threshold/floor, rho/R values, channel set, scientific classifier and interpretation ceiling.

Any change to those scientific fields, or promotion of inclusion truth into a new PASS condition, requires a new prospectively frozen gate.