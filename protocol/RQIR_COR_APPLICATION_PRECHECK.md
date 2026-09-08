# RQIR Comparator-Orthogonal Residual Application — Precheck

**Protocol ID:** `KMQGB-RQIR-COR-PRE-001`  
**Status:** PRE-REGISTERED / BLOCKED ON EXTERNAL RQIR SOURCE-WARD RESIDUAL

This file is read-only with respect to external RQIR authority. It defines how KMQGB residual-space geometry may be applied **after** RQIR itself closes the same-dynamics source/Ward object and fixed comparator residual.

## External coordinate currently available but not yet a residual

Latest read-only RQIR authority observed during this precheck: Iteration 587.

The operator coordinate from Iter582 has three distinct timelike buckets, with no Source/Born subtraction yet:

- candidate `q^2=-1.0`;
- candidate `q^2=-0.34`;
- candidate `q^2=-0.14`.

KMQGB must not feed the raw Iter582 operator values into COR as if they were comparator-subtracted observables.

The external RQIR next gate is to close the complete same-dynamics source Ward object from K1 exchange + K2 contact on the frozen off-shell routing.

## Future physical residual vector

Only after external RQIR authority defines matched physical residuals `R(q_i^2)` may KMQGB form the real vector

`y_RQIR = [ Im R(-1.0), Im R(-0.34), Im R(-0.14) ]^T`

if the final matched residual is indeed purely imaginary in the frozen convention. If real components survive, split them into independent physical real coordinates only after exact conjugation/symmetry relations are applied.

The three-bucket imaginary-only case has

`m_phys <= 3`.

## Immediate dimension-count warning

For any locally linearized union comparator tangent `A_union`,

`dim(comparator-orthogonal space) = m_phys - rank(A_union)`.

Therefore in the three-real-coordinate case:

- rank 0 -> at most 3 local residual directions;
- rank 1 -> at most 2;
- rank 2 -> at most 1;
- rank 3 -> **no local comparator-orthogonal direction remains**.

Increasing numerical precision of the same three coordinates cannot change this rank fact.

This is why cross-order/cross-attribution observables may be necessary even if all three q2 buckets are computed extremely accurately.

## Comparator Jacobian to freeze prospectively

After external RQIR supplies the matched observable for every comparator, construct

`J_union=[J_C3,J_C4,J_C5,J_nonlocal,J_AS,...]`

in the exact same three-bucket physical coordinate, adding only genuinely independent nuisance/state/calibration directions and removing representation-equivalent duplicates.

The comparator list must follow the external RQIR frozen comparator authority; KMQGB may diagnose rank but must not silently alter RQIR's comparator definition.

## Covariance / numerical metric

Use the matched residual covariance/numerical uncertainty matrix `Sigma_RQIR`, including cross-bucket correlations if present.

Do not assume diagonal covariance merely because the q2 buckets are stored separately. Shared integration, normalization, source, matching or subtraction uncertainties can create correlated directions.

Then

`A = Sigma_RQIR^(-1/2) J_union`,

`COR_RQIR = (I-AA^+) Sigma_RQIR^(-1/2) y_RQIR`.

## Cross-order augmentation rule

If the three-bucket comparator complement has dimension zero or is nearly singular, do not tune an ansatz to manufacture separation in the same coordinate.

Instead augment the physical observable vector with an independently derived quantity from the **same parent dynamics**, for example a Ward/contact-complete cross-order, channel or ordered-response observable already allowed by the frozen Candidate Gravity design priors.

An augmentation is useful only if it raises physical observable dimension more than it raises comparator/nuisance tangent rank.

Formally, for adding observable block `B`, require

`Delta d_perp = Delta m_phys - Delta rank(A_union) > 0`

or a substantial improvement in the smallest relevant projected singular value.

## Current classification

`BLOCKED_MISSING_REQUIRED_OBJECT` for actual COR evaluation.

Missing external object:

`RQIR_MATCHED_SOURCE_WARD_COMPARATOR_RESIDUAL_VECTOR`.

This is not a failure of Candidate Gravity. It is a prospective application guardrail preventing premature residual projection.
