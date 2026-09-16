# KMQGB Critical Preterminal Audit — V7 derivative-contact triangle regularization

Date: 2026-09-16
Lane: independent Critical Review / Verification
Status: PRETERMINAL_ONLY — NO SCIENTIFIC VERDICT

## RESULT_REVIEWED

No terminal substantive Research result exists for the active V7 gate at this audit point.

Active gate:

`SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7`

Authoritative workflow run:

`35054748495`

Fresh repository `main` at audit start:

`b69f75ab2ae733c0fdda6d673acca130b830d55e`

Fresh Actions state: workflow nonterminal; the source-lock job `104662442178` had completed its chronology/source-evaluation steps but remained in progress during artifact upload. No exact-lane or aggregate substantive values were consumed.

## PREREG_CHECK

PASS for prospective chronology.

Frozen preregistration commit:

`764cd9f915cef15b6294f5f72329f12cb145c08e`

Implementation commit:

`44da1edd39debce755f9ae7d48c4e7abd375604c`

Workflow head:

`e5021974d02f7cd52c540e80f5b3a14fcf0e5cdf`

Direct comparison shows the implementation commit is exactly one commit after the preregistration and adds only `code/source_j1_k5_triangle_derivative_contact_regularization_v7.py`. The workflow was added afterward. No post-hoc scientific threshold or scheme change was found in the static chronology.

The frozen contract is outcome-discriminating and clearly separates:

- PASS: `TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED`;
- FAIL: `TRIANGLE_DELTA2_CONTACT_REGULARIZATION_INVARIANT_SCOPED`;
- BLOCKED: `TRIANGLE_DELTA2_CONTACT_REGULARIZATION_SOURCE_BLOCKED`;
- INVALID: `INVALID_IMPLEMENTATION`.

## OBJECT_IDENTITY_CHECK

Static object identity is consistent with the intended derivative-contact bridge:

- local conormal map `B12=x`, `B23=y`, `B13=x+y`;
- normalized Gaussian approximate identity;
- second derivative contact order `D2 = delta''`;
- frozen scale-free statistic `K = pi*C^2/(a+b+c)^7`;
- exact width schemes A/B/C and common-rescaling A4.

The production `gaussian_data()` algebra uses the frozen covariance matrix and the polynomial expectation corresponding to `(2aX^2-1)(2bY^2-1)(2cZ^2-1)`. No plain-delta V6 statistic is substituted into the production `K` formula by inspection.

However, two mandatory frozen controls are not independently bound to the production implementation; these are recorded below as explicit code-audit defect candidates to be applied after terminalization.

## SOURCE/REALIZATION_CHECK

Static source/realization chain is coherent with the preregistration:

- repaired V4 supplies the parent highest `delta''` derivative order;
- V6 supplies the local triangle conormal geometry;
- V5 channel `00000=11/24` is only contextual and is not multiplied into the local integral.

`source_authority()` checks the V4/V5/V6 front records and the V6 Critic requirement for the derivative bridge. Runtime source authority remains an Actions provenance question until the workflow is terminal.

## PROVENANCE_CHECK

Current authoritative run `35054748495` is nonterminal. Therefore:

- no PASS / FAIL / BLOCKED / INVALID classification is consumed;
- no `K(A/B/C)` values are consumed;
- no exact-lane artifacts or aggregate digest are consumed;
- green/pending CI is not used as scientific evidence.

Fresh independent workflow state also shows Iter504 run `34907349374` has advanced from queued to `in_progress / conclusion=null`; no partial values are consumed. Iter461 run `34748503239` remains `queued / conclusion=null`.

## SAME_REALIZATION_CHECK

The intended same-realization repair is structurally correct at the object-definition level: V7 restores `delta''` while retaining the V6 triangle map. No terminal same-realization scientific conclusion is assigned before the Actions aggregate exists.

## NUMERICAL/STATISTICAL_CHECK

No terminal numerical/statistical result is available or used. The gate is exact-rational by design; no floating threshold is part of the frozen decision.

Outcome-independent analytic inspection confirms that the preregistered scaling construction is dimensionally coherent: each normalized Gaussian second derivative contributes `eps^-3`, the two-dimensional integration contributes `eps^2`, so the frozen leading power is `eps^-7`; common width scaling sends `C -> lambda^(7/2) C`, making the frozen `K` scale-free.

This dimensional consistency is not a scientific verdict on A/B/C.

## COUNTEREXAMPLE_ATTEMPTS

### 1. Frozen derivative-identity control is tautological and disconnected from production

The preregistration requires a positive control for the exact second-derivative identity. The implementation defines:

`derivative_identity = all((4*a^2,-2*a) == (4*a^2,-2*a) for a in (1,4))`

which is true by construction and does not evaluate, derive, or bind the production derivative factor used by `gaussian_data()`.

The adversarial plus-sign derivative test is also computed in the separate `one_factor_controls()` path rather than by mutating/replaying the production derivative representation.

Explicit outcome-independent counterexample to the control binding: if the production derivative polynomial inside `gaussian_data()` were changed while leaving `one_factor_controls()` unchanged, both `derivative_identity` and `wrong_derivative_plus_sign_rejected` could retain their current truth values. Thus these controls do not establish that the decision-producing path uses the frozen derivative identity.

This is a frozen-contract implementation defect candidate, not a V7 scientific outcome.

### 2. Frozen independent transverse two-contact control is not independently replayed through the production Gaussian machinery

The preregistration requires an **independent transverse two-contact normalization through the same Gaussian-moment machinery**. The implementation instead computes

`transverse = x21 * x24`

where `x21` and `x24` are the one-factor normalization values from `one_factor_controls()`.

That product is mathematically equal to 4 for the transverse factorized object, but it is not an independent two-dimensional replay of the multivariate Gaussian/Wick machinery used by `gaussian_data()`.

Explicit outcome-independent counterexample to the control binding: an error introduced in the multivariate covariance/Wick path of `gaussian_data()` would leave `transverse = x21*x24` unchanged. Therefore this frozen control cannot detect precisely the class of multivariate-integration implementation errors it was prospectively intended to guard against.

This repeats, in derivative-contact form, the control weakness identified by the preceding V6 Critic and is stronger here because V7 explicitly froze an independent replay as a required positive control.

### 3. Wrong-conormal negative fixture

The wrong map `B13=x+2y` is structurally distinguished by the determinant formula `ab+4ac+bc` at scheme A versus target `ab+ac+bc`. No defect was found in this static fixture.

### 4. Plain-delta substitution

Production `K` and the plain-delta `abc/D` fixture are separate fields. No static substitution of the V6 plain-delta statistic into the V7 decision path was found.

## OVERCLAIM_CHECK

No V7 scientific claim is admissible while run `35054748495` is nonterminal.

Even if the eventual exact lanes agree, lane agreement and green CI cannot by themselves repair a mandatory frozen control that is tautological or not connected to the production path.

No distributional extension nonexistence, all-mollifier statement, full ten-contact K5 result, model/family failure, D7 closure, terminal selector, or Candidate Gravity activation is authorized.

## VERDICT

NO TERMINAL VERDICT — AUTHORITATIVE WORKFLOW NONTERMINAL.

The two implementation-control defects above are prepared counterexamples for the terminal review. If the source remains unchanged, any eventual Research PASS/FAIL must be audited against the frozen requirement that these controls be genuinely implemented; CI color cannot override that contract question.

## QUALIFICATIONS

1. Prospective chronology is clean.
2. Static production object appears to be the intended local `delta''` triangle realization.
3. Mandatory derivative-identity control is tautological/disconnected from production.
4. Mandatory independent transverse two-contact replay is not actually independent and does not exercise the production multivariate Gaussian machinery.
5. No partial substantive Actions values are consumed.
6. Governance remains unchanged: RQIR Core v1.0 FROZEN; BLOCKED != FAIL; D7-S2/D7-S3 not closed; D7-S4 partial; terminal selectors forbidden; Candidate Gravity inactive.

## UPDATED_STATE

- V7 = ACTIVE / NONTERMINAL / NOT CLASSIFIED by Critic.
- run `35054748495` remains the only authoritative V7 execution to consume after terminalization.
- derivative-control and transverse-control implementation defects are durably preregistered for counterexample-first terminal review.
- Iter504 is now `in_progress / conclusion=null`; Iter461 remains `queued / conclusion=null`; no partial values consumed.

## NEXT_ADMISSIBLE_GATE

Do not launch a competing V7 scientific gate while run `35054748495` is nonterminal.

First consume only the terminal V7 aggregate/artifacts/digests. Then audit the historical Research classification against the two frozen-control defects above.

A contract-preserving implementation repair, if required, should:

1. represent the production derivative polynomial/prefactor in one executable object/function and derive both production and derivative positive/negative controls from that same representation;
2. independently evaluate the frozen transverse two-contact integral with the same Gaussian moment/integration engine used by the target calculation, not as a product of already-validated one-factor outputs;
3. preserve the frozen object, width schemes, `K`, conormal map, PASS/FAIL/BLOCKED/INVALID semantics and interpretation ceiling.

Changing those scientific fields requires a new prospectively frozen gate; fixing only the control wiring does not.
