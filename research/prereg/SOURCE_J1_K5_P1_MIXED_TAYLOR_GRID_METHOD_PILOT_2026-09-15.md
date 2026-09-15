# SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT — prospective freeze

Date: 2026-09-15
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT

## HYPOTHESIS

The mixed Taylor projector required by the exact P1 proper-forest operator can be evaluated stably without nested high-order `mp.diff` precision explosion by tensor-product forward interpolation on a prospectively frozen small grid near the common Taylor point. The method must converge under step refinement, agree across independent working precisions, be independent of tensor-reduction order, and retain enough measured cancellation margin for later 29-orbit production.

## OBJECT

Auxiliary scalar Gaussian K5 P1 only, with the already terminally validated numerical pairing and exact operator:

- `alpha=0.55`;
- `k=5` only in this method pilot;
- P1 exponents `(1,1,1,1,2,2,2,2,2,2)`;
- exact barycentric `Gamma_S(lambda)=C_S+lambda(I-C_S)`;
- scalar orders `r_2=2`, `r_3=7`, `r_4=15`;
- operator spec digest `sha256:c3e0ca0c5a5357887db79b7b0a1c5a0a1042c450ca13f7e2599c7e3801ef8a9c`.

For a laminar forest `F=(S_1,...,S_m)`, define

`G_F(lambda)=product_i Gamma_{S_i}(lambda_i)`

and

`H_F(lambda)=<T_epsilon, exp[-alpha ||G_F(lambda)x||^2]>`.

The target mixed Taylor value is the box-truncated Taylor polynomial evaluated at the physical point `(1,...,1)`:

`T_F = sum_{0<=n_i<=r(S_i)} [partial^n H_F(0) / product_i n_i!]`.

No sign/growth of `T_F` is scientific in this method gate.

## NUMERICAL METHOD — FROZEN BEFORE RESULT

For one variable with nodes `lambda_j=j h`, `j=0,...,r`, compute the unique degree-`r` Newton forward interpolation polynomial and evaluate it at `lambda=1`:

`P_r(1;h)=sum_{n=0}^r binom(1/h,n) Delta_h^n H(0)`.

For a forest, use the tensor product of these one-variable interpolation operators. Because the exact laminar `Gamma` families commute, tensor-axis reduction order is a numerical implementation choice only and must give the same result within the frozen tolerance.

This approximates the desired Taylor projector as `h -> 0`; step-refinement, precision-replay, exact polynomial fixtures, and cancellation budgets are mandatory. No post-hoc step/tolerance changes are allowed.

## FROZEN TEST FORESTS

All at `k=5`, `alpha=0.55`:

1. `SINGLE15 = [{0,1,2,3}]`, order `(15)`, grid boxes `16`.
2. `NESTED27 = [{0,1},{0,1,2}]`, orders `(2,7)`, grid boxes `24`.
3. `DISJOINT22 = [{0,1},{2,3}]`, orders `(2,2)`, grid boxes `9`.
4. `CHAIN2715 = [{0,1},{0,1,2},{0,1,2,3}]`, orders `(2,7,15)`, grid boxes `384`.

Total actual-Gaussian evaluations per step scale before cache reuse: `433`.

## FROZEN LANES / STEP SCALES

- lane LOW: `dps=1100`, `h=2^-100`;
- lane HIGH: `dps=1500`, evaluate both `h=2^-100` and refined `h=2^-140`.

The HIGH lane's `h=2^-100` values provide the same-step precision replay. Its `h=2^-140` values provide the frozen refinement check.

Pinned numerical dependency: `mpmath==1.3.0`.

## POSITIVE CONTROLS

1. Existing terminal numerical-kernel raw P1 lock is replayed once at `k=5`, `alpha=0.55` before grid work; normalized error <= `1e-65`.
2. Exact polynomial tensor fixture: for each frozen forest order box, use a deterministic polynomial with degree in each variable <= the corresponding frozen order. Tensor interpolation at both step scales must reproduce its exact value at all variables `=1` with normalized error <= `1e-200` in HIGH and <= `1e-120` in LOW.
3. Tensor reduction order: reducing grid axes forward vs reverse must agree with normalized error <= `1e-100` in LOW and <= `1e-180` in HIGH for every frozen forest/step calculation.
4. Same-step precision replay at `h=2^-100`: LOW vs HIGH must agree for all four actual-Gaussian forest targets within normalized error <= `1e-70`.
5. Step refinement in HIGH: `h=2^-100` vs `h=2^-140` must agree for all four actual-Gaussian forest targets within normalized error <= `1e-18`.
6. Exact forest/Gamma commutation and order locks from the terminal operator gate are rechecked structurally before numerical evaluation.
7. All actual-Gaussian grid samples and projected values must be finite.
8. Cancellation audit: for each actual-Gaussian projection compute
   `kappa = sum_grid |w_grid H_grid| / max(1,|P|)`
   using the direct tensor Lagrange weights for the same interpolation polynomial. Require measured remaining decimal safety margin
   `dps - log10(max(1,kappa)) >= 180`
   in every calculation.

## NEGATIVE / ADVERSARIAL CONTROLS

1. A degree `r+1` polynomial fixture in the first variable must not be claimed exact by the degree-`r` interpolator; the two step scales must differ measurably.
2. A deliberately nonlaminar overlapping pair `{0,1}` / `{1,2}` must be rejected before grid evaluation.
3. Replacing order 15 by historical three-normal-dimensional order 9 for `SINGLE15` must fail the scalar-order lock.
4. If the refinement or precision criteria fail, classification is BLOCKED; tolerances/steps/orders may not be relaxed in place.

## PASS

`P1_MIXED_TAYLOR_GRID_METHOD_CONFIRMED_SCOPED` iff all exact/object controls, polynomial fixtures, actual-Gaussian same-step precision replay, step refinement, tensor-order replay, finiteness, and cancellation-margin controls pass.

## BLOCKED / INVALID

`P1_MIXED_TAYLOR_GRID_METHOD_PRECISION_BLOCKED` iff object/source controls pass but precision/refinement/cancellation margin fails.

`INVALID_IMPLEMENTATION` for wrong P1 object, wrong forest/order box, nonlaminar acceptance, failed exact polynomial fixture, wrong interpolation formula, wrong operator digest, historical P3 use, or any post-hoc contract change.

## INTERPRETATION CEILING

PASS validates only the mixed Taylor numerical method for later P1 forest-orbit production. It does not establish forest-subtracted stabilization/divergence, Eq. (4) existence/nonexistence, model/family failure, D7 closure, any terminal selector, or Candidate Gravity.

Only a terminal PASS authorizes a separately prospectively frozen 29-orbit P1 proper-forest production diagnostic.