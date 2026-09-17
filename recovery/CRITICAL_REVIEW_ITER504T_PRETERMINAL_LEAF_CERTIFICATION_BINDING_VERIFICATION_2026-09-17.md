# KMQGB Critical Review — Iter504T C4 leaf-certification binding verification

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Status: TERMINAL CRITIC REVIEW

## RESULT_REVIEWED

Exactly one clearly bounded terminal closure result was reviewed:

- gate: `ITER504T_PRETERMINAL_LEAF_CERTIFICATION_BINDING_VERIFICATION_GATE`;
- prospective preregistration: `aa421bd0b1aec1cbcc7a381fb00e947798d1b084`;
- frozen authority: `9aa9f77093bd34e058641bb141c8f95a4794d841`;
- verifier implementation: `72f952cb0ce6c3bc08f244fdde815337d3504b1e`;
- aggregate verifier: `c2527cb1966e6afe7fcdd8c9f1d0df435b35080a`;
- workflow head: `2a550a44cdf69b1b165ba65fec8f6a5d56bd0f40`;
- authoritative Actions run: `35220141450`, terminal `completed/success`;
- historical closure classification: `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED`.

Active repair run `35205054496` was still `in_progress / conclusion=null` at the review-start metadata check. No substantive artifact from that active repair run was consumed.

## PREREG_CHECK

PASS.

The defect-verification preregistration was committed before verifier implementation and before the terminal verification result. It prospectively froze one narrow question: whether the immutable repair launch-head downstream path independently enforces

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`

rather than trusting serialized top-level leaf certification. It explicitly excluded all active repair-run substantive artifacts and froze VERIFY / REFUTE / BLOCKED / INVALID semantics plus an implementation-only interpretation ceiling.

The original scientific preregistration `aa2b0256ce60d605574a18ec86c0bad5b5df1512` independently freezes:

- `rho_certified := slope_floor_satisfied AND drift_within_tolerance`;
- a node is certified iff all four rhos are certified;
- scientific PASS requires every terminal leaf to be scientifically certified.

No post-hoc threshold or scientific predicate was introduced by the C4 gate.

## OBJECT_IDENTITY_CHECK

PASS_SCOPED.

The reviewed object is exactly the decision-binding relation at immutable repair launch head `10ae6bcc8447d14cecc6e550065504b23f792953`, not the numerical truth of any active Iter504T leaf.

The synthetic target mutation preserves an internally consistent per-rho row with

- `slope_floor_satisfied=false`;
- `drift_within_tolerance=true`;
- `rho.certified=false`;

while setting only the enclosing top-level `leaf.certified=true` and keeping `unresolved_leaf_count=0` consistent with that top-level flag. This directly isolates the frozen implication under review.

## SOURCE/REALIZATION_CHECK

PASS_SCOPED.

The frozen authority ledger pins the original scientific preregistration blob and the exact launch-head blobs for:

- `code/iter504t_local_derivative_assemble.py`;
- `code/iter504t_local_derivative_critic.py`;
- `code/iter504t_local_derivative_aggregate.py`;
- the latest outcome-independent preterminal Critic record.

The workflow source-lock independently checks those blob identities before either Python lane runs.

Static launch-head inspection independently confirms the binding gap:

- assembler validates each `rho.certified == slope_floor_satisfied AND drift_within_tolerance`;
- assembler computes `unresolved_leaf_count` only from top-level `leaf.certified` flags;
- Critic likewise validates the per-rho identity, but does not require top-level `leaf.certified == all(per_rho.certified)`;
- Critic classification is derived from serialized `unresolved_leaf_count` after those checks;
- aggregate only compares lane decisions and therefore cannot repair an identical defect in both lanes.

This is the same immutable implementation realization exercised by the terminal synthetic replay.

## PROVENANCE_CHECK

PASS.

Run `35220141450` is terminal `completed/success` at exact head `2a550a44cdf69b1b165ba65fec8f6a5d56bd0f40`.

Jobs:

- source-lock `105197957392`, success;
- Python 3.11 `105197992013`, success;
- Python 3.13 `105197992075`, success;
- aggregate `105198050663`, success.

Actions artifact ZIP digests were independently downloaded and re-hashed during this review:

- Python 3.11 artifact `10496991098`: `sha256:011a0b8363dcf313d62bc9c2dd681afd1ecff0f91b2b3cee52a4f7492ca79562`;
- Python 3.13 artifact `10496836236`: `sha256:71c367aa409fa18b3bd04b423b377cbbbd90589543a06c94387d424f2010617d`;
- aggregate artifact `10496519019`: `sha256:7a932e0c36bdc09871ac114c9264c6997c4c352a84c2373e6323086ecbdb3daa`.

The independently extracted lane JSON files are byte-identical with SHA256 `ebfc6d514f2c013e6eeaae01b651fc612b39b2445934fc250fa3f6e1ba91b544`; lane decision SHA256 is `3eefcd29f0699da8c7bcae6639cabbffd04f0fa154f31862d6f716c216899c05`. Aggregate JSON SHA256 is `5ce6c4ebf5ece9919e460aed1216e0145e03b4a6339d6461624481824cf6ae4b`; aggregate decision SHA256 is `770ec74f672105a303c792586a8f644f12c1a54788021ff9856511d7c3fea6e5`.

No `INVALID_PROVENANCE` basis was found.

## SAME_REALIZATION_CHECK

PASS_SCOPED.

The verifier does not approximate or reimplement the launch-head validators. It invokes the exact blob-locked launch-head assembler, aggregate and independent Critic on synthetic root JSON fixtures. The workflow never downloads the active repair-run artifacts.

Thus the result establishes a validator-path property of the immutable active launch head without making any claim about hidden numerical outputs from the still-nonterminal repair execution.

## NUMERICAL/STATISTICAL_CHECK

PASS_EXACT_NONSTATISTICAL.

The closure is an exact synthetic decision-path replay, not a statistical estimate and not a floating-threshold calculation. Both Python 3.11 and 3.13 lanes produce byte-identical decision JSON and log hashes.

For the compliant positive fixture, assembler A/B, aggregate and Critic all return `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`.

For the target C4 fixture, both assemblers, aggregate and Critic also return the same PASS class with return code 0, `critic_errors=[]`, and `cross_environment_exact_decision_agreement=true` despite one internally consistent `rho.certified=false` inside a top-level `leaf.certified=true`.

## COUNTEREXAMPLE_ATTEMPTS

1. **Target top-level binding counterexample — succeeds.** The exact immutable launch-head path accepts the malformed leaf described above. This directly verifies C4.
2. **Broken per-rho relation — rejected.** Setting `rho.certified` inconsistent with `slope_floor_satisfied AND drift_within_tolerance` is rejected by assembler (`boolean_consistency`) and Critic (`exact_boolean_consistency`). This shows the target result is not caused by a generally inert validator.
3. **R-cohort mutation — rejected.** `R=6 -> 7` in the possible-max cohort is rejected by both assembler and Critic (`possible_max_R_rho_cohort`), confirming the previously repaired R binding is live in this fixture.
4. **Cross-environment rescue — fails.** Applying the same malformed C4 mutation to both lanes leaves exact lane agreement true, demonstrating that agreement alone cannot restore the missing predicate binding.
5. **Wrong launch-head/source identity — excluded by source-lock.** All frozen blob identities match.
6. **Active numerical artifacts as hidden input — no evidence.** Workflow structure and verifier inputs use repository authority plus generated synthetic fixtures only; no active repair artifact download occurs.

No counterexample to the scoped C4 VERIFIED interpretation was found.

## OVERCLAIM_CHECK

PASS.

The closure result establishes only an implementation/decision-binding defect in launch head `10ae6bcc8447d14cecc6e550065504b23f792953`.

It does not show that the active producer emitted an inconsistent leaf; does not classify repair run `35205054496` scientifically; does not establish Iter504T scientific FAIL; does not establish all-1888-state failure or closure; does not close D7; and does not authorize any terminal selector or Candidate Gravity activation.

Green CI is provenance, not science. `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.

## VERDICT

`CONFIRMED_SCOPED`

The terminal classification `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED` is independently confirmed for the exact immutable launch-head downstream validator path.

The decisive evidence is an explicit outcome-independent synthetic counterexample that passes all unrelated frozen positive controls and is accepted by assembler, aggregate and Critic in both Python environments while violating the original frozen node/leaf certification conjunction.

## QUALIFICATIONS

1. C4 is a verified implementation/decision-binding defect, not a numerical/scientific result about the active repair outputs.
2. The review does not assert that the producer actually generated an inconsistent leaf.
3. The active repair run remains outside this terminal review while nonterminal; its partial substantive values were not consumed.
4. The positive controls show that per-rho identity and R-cohort checks are live; the defect is specifically the missing top-level conjunction binding.
5. Historical Iter504T and repair-run execution records remain immutable.

## UPDATED_STATE

- `ITER504T_PRETERMINAL_LEAF_CERTIFICATION_BINDING_VERIFICATION_GATE = CONFIRMED_SCOPED` by independent Critic for run `35220141450`.
- Terminal historical closure classification `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED` is confirmed.
- Launch head `10ae6bcc8447d14cecc6e550065504b23f792953` has a verified C4 decision-binding defect.
- A future green/PASS result from that unchanged launch head cannot by itself be promoted as independently validated scientific authority under the original frozen predicate.
- `RQIR Core v1.0 = FROZEN`; D7 required subgates remain unclosed; terminal selectors remain forbidden; Candidate Gravity remains inactive.

## NEXT_ADMISSIBLE_GATE

While repair run `35205054496` is nonterminal, do not launch a competing same-object authoritative scientific execution and do not consume its partial substantive outputs.

After that run terminalizes, perform exactly one terminal review of its execution/provenance and apply this already-confirmed C4 defect to any historical repair classification. Preserve the run history; do not rewrite it.

A subsequent same-science implementation repair may prospectively add the explicit equality check

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`

in assembler and independent Critic, plus the exact adversarial C4 mutation used by this gate. Roots, rhos, R grid, channels, local-D science, threshold, floor, classifier and interpretation ceiling must remain unchanged for that to remain a same-contract repair. Any scientific-contract change requires a new prospectively frozen gate.