# KMQGB Critical Review — V7 derivative-contact triangle regularization

Date: 2026-09-16
Lane: independent Critical Review / Verification
Status: TERMINAL CRITIC REVIEW

## RESULT_REVIEWED

Exactly one latest substantive terminal Research execution was reviewed:

- gate `SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7`;
- frozen preregistration commit `764cd9f915cef15b6294f5f72329f12cb145c08e`;
- implementation commit `44da1edd39debce755f9ae7d48c4e7abd375604c`;
- workflow head `e5021974d02f7cd52c540e80f5b3a14fcf0e5cdf`;
- authoritative Actions run `35054748495`, terminal `completed/success`;
- source-lock job `104662442178`, success;
- exact Python 3.13 job `104667121284`, success;
- exact Python 3.11 job `104667121315`, success;
- aggregate job `104671916886`, success.

Research aggregate classification:

`TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED`

The run terminalized after the earlier preterminal Critic audit. No historical Research output is rewritten by this review.

## PREREG_CHECK

PASS for chronology and frozen scientific contract.

The preregistration prospectively froze before implementation:

- local conormal map `B12=x`, `B23=y`, `B13=x+y`;
- normalized Gaussian second derivative `D2_eps^a = delta''_eps`;
- exact integral `I_eps(a,b,c)` and leading power `eps^-7`;
- scale-free exact statistic `K = pi*C^2/(a+b+c)^7`;
- exact schemes A `(1,1,1)`, B `(1,1,4)`, C `(1,2,3)`, A4 `(4,4,4)`;
- mandatory positive controls including an exact derivative-identity control and an **independent transverse two-contact normalization through the same Gaussian-moment machinery**;
- negative controls for wrong derivative sign, wrong conormal map and plain-delta substitution;
- PASS / FAIL / BLOCKED / INVALID semantics and interpretation ceiling.

No post-hoc threshold, width scheme or decision criterion was found.

## OBJECT_IDENTITY_CHECK

PASS for the production object itself; FAIL for mandatory control binding.

The decision-producing `gaussian_data()` path does use the frozen derivative-contact object: it evaluates the exact covariance matrix for `x,y,x+y`, the Wick moments and the polynomial expectation corresponding to `(2aX^2-1)(2bY^2-1)(2cZ^2-1)`. The plain-delta V6 quantity is stored only as a distinct adversarial fixture.

However, the implementation does not genuinely implement two mandatory frozen controls that were part of the object/implementation contract. This is decisive under the preregistered `INVALID_IMPLEMENTATION` branch.

## SOURCE/REALIZATION_CHECK

PASS_SCOPED for the source chain.

The execution source-locks the repaired V4 highest-`delta''` authority, V5 channel-`00000` context, the V6 local triangle geometry and the V6 Critic requirement for a derivative-contact bridge. The local object is therefore the intended same-derivative-order triangle bridge, not the earlier plain-delta surrogate.

No source/version mismatch was found in the frozen dependency chain.

## PROVENANCE_CHECK

PASS.

Run `35054748495` is terminal `completed/success` at workflow head `e5021974d02f7cd52c540e80f5b3a14fcf0e5cdf`.

Actions artifacts:

- source lock `10430711890`, digest `sha256:fb97f0f48802026f0cc8fcc38bd8749e307f9f091cb3e74af1bca11cc660a1d3`;
- Python 3.11 `10431855371`, digest `sha256:952d9f95aaddf363d82444c5c8cfc0cc2d52e47376a988cee734a3ad689d7348`;
- Python 3.13 `10431023217`, digest `sha256:ae345963ee9733711f95cb619864c9ecb031cdb42ec0edd0e46187df7e67edc0`;
- aggregate `10431741758`, digest `sha256:4933e65ca18f316be51508d0481449f2debc546126d9cac6ee791ddda4217f2c`.

The aggregate records lane agreement and exact rational output. Green CI is used only as execution provenance and cannot repair a frozen-contract implementation defect.

## SAME_REALIZATION_CHECK

QUALIFIED.

The production calculation is on the intended V7 `delta''` triangle realization. The failure is not a plain-delta transfer problem and not a source-authority problem.

The decisive issue is that the frozen controls do not exercise the same executable realization as the production path in the way preregistered.

## NUMERICAL/STATISTICAL_CHECK

Exact/non-statistical result; no floating threshold is involved.

The terminal aggregate reports:

- `K(A)=1600/531441`;
- `K(B)=204800/1162261467`;
- `K(C)=14400/19487171`;
- `K(A4)=K(A)` exactly;
- both exact lanes report the same Research classification.

These values are useful diagnostic evidence for the underlying algebra, but because mandatory frozen implementation controls are not genuinely implemented, they are not accepted here as a validated scientific PASS classification.

## COUNTEREXAMPLE_ATTEMPTS

### 1. Mandatory derivative-identity control — explicit binding counterexample succeeds

Frozen positive control 1 requires the exact derivative identity for the production `D2_eps^a(t)`.

Implementation instead sets

`derivative_identity = all((4*a^2,-2*a) == (4*a^2,-2*a) for a in (1,4))`.

This comparison is true by construction and never derives, evaluates or reuses the production derivative representation in `gaussian_data()`.

Explicit counterexample to control binding: change the production derivative polynomial/coefficient in `gaussian_data()` while leaving this comparison and `one_factor_controls()` untouched. The frozen `derivative_identity` and wrong-plus-sign fixture can remain `true` although the decision path no longer uses the frozen derivative object.

Therefore the mandatory derivative-identity control is tautological/disconnected from production.

### 2. Mandatory independent transverse two-contact replay — explicit machinery counterexample succeeds

Frozen positive control 5 requires an **independent transverse two-contact normalization through the same Gaussian-moment machinery**:

`integral D2^1(x) D2^4(y) x^2 y^2 dxdy = 4` at `eps=1`.

Implementation computes

`transverse = x21 * x24`,

where `x21` and `x24` are already-computed one-factor controls. This is algebraically 4, but it never exercises the multivariate covariance/Wick path used by `gaussian_data()`.

Explicit counterexample to control binding: introduce an error in the production multivariate covariance or Wick-moment implementation while leaving `one_factor_controls()` unchanged. The transverse control still reports 4. Hence this control cannot detect the exact class of two-dimensional Gaussian-moment implementation error that the preregistration prospectively required it to guard against.

### 3. Wrong conormal map

Refutation attempt failed: the implementation distinguishes target determinant `ab+ac+bc` from the `x+2y` fixture determinant and does not accept the wrong conormal map.

### 4. Plain-delta substitution

Refutation attempt failed: production `K` and the plain-delta fixture are separate, and the V6 statistic is not substituted as the V7 decision variable.

### 5. Common-rescaling / permutation / lane dependence

No counterexample found in the terminal artifact: exact common-rescaling invariance, permutation records and lane agreement are reported. These controls do not cure the two mandatory control-binding failures above.

### 6. Green CI promoted to science

Rejected. All jobs succeeded, but the frozen gate requires controls that were not actually implemented as frozen.

## OVERCLAIM_CHECK

The historical Actions aggregate may be recorded as having output `TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED`, but that label is not independently validated for downstream scientific consumption because the implementation fails the frozen mandatory-control contract.

This Critic does **not** assert the opposite scientific result. In particular it does not establish regulator invariance, scientific FAIL, distributional extension existence/nonexistence, all-mollifier behavior, full ten-contact K5 behavior, model/family failure, D7 closure, a terminal selector or Candidate Gravity activation.

The exact A/B/C rational values may be retained as diagnostic outputs of the historical run, not promoted to validated V7 scientific authority until a same-contract implementation repair passes the frozen controls genuinely.

## VERDICT

`INVALID_IMPLEMENTATION`

The terminal Research execution does not satisfy the prospectively frozen implementation contract because two mandatory positive controls are not genuinely implemented:

1. derivative identity is tautological and not bound to the production derivative representation;
2. transverse two-contact normalization is not independently replayed through the same multivariate Gaussian-moment machinery.

This is implementation invalidity, not scientific FAIL.

## QUALIFICATIONS

1. Prospective chronology and source authority are sound.
2. The production object itself appears to be the intended local `delta''` triangle object.
3. Exact terminal A/B/C outputs and lane agreement are diagnostic only under this Critic verdict.
4. Historical run `35054748495` remains immutable; its Actions aggregate is not rewritten.
5. A contract-preserving control-wiring repair may retain the same preregistration, object, schemes, statistic and decision semantics.
6. Any change to scientific object, conormal map, width schemes, statistic, thresholds, PASS/FAIL/BLOCKED semantics or interpretation ceiling requires a new prospective gate.
7. Iter504 run `34907349374` is freshly `in_progress / conclusion=null`; Iter461 run `34748503239` remains `queued / conclusion=null`; no partial substantive values were consumed.
8. Governance remains unchanged: `RQIR Core v1.0 = FROZEN`; `BLOCKED != FAIL`; D7-S2/S3 not closed; D7-S4 partial; terminal selectors forbidden; Candidate Gravity inactive.

## UPDATED_STATE

- `SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7 = INVALID_IMPLEMENTATION` by independent Critic for run `35054748495`.
- Research aggregate historical output = `TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED`, not validated downstream.
- production same-realization object = statically coherent but not scientifically closed under the frozen gate.
- exact A/B/C rational outputs = diagnostic only pending same-contract repair.
- V6 remains the latest prior terminal Research result with Critic verdict `QUALIFIED`; V7 does not upgrade D7 or family state.
- governance locks unchanged.

## NEXT_ADMISSIBLE_GATE

Perform only a same-contract implementation repair of V7:

1. define one executable derivative-factor representation/function and use that exact representation in production, derivative identity positive controls and wrong-sign adversarial replay;
2. independently compute the frozen transverse two-contact integral through the same Gaussian covariance/moment engine used for production, rather than multiplying two one-factor outputs;
3. retain all frozen source locks, local conormal map, width schemes A/B/C/A4, exact statistic `K`, PASS/FAIL/BLOCKED/INVALID semantics and interpretation ceiling;
4. rerun two independent exact Python lanes and terminal aggregate with fresh artifacts/digests.

If repair changes any scientific-contract field rather than only control wiring, require `REQUIRES_NEW_PREREGISTERED_GATE` instead of rewriting this history.
