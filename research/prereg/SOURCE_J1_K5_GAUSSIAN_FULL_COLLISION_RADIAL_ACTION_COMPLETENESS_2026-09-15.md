# Prospective preregistration — full-collision radial action-space completeness

Date: 2026-09-15
Gate: `SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS_GATE`
Status: `PROSPECTIVELY_FROZEN`

## Parent authority

Consume only the terminal child:

- `results/SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_TERMINAL_2026-09-15.md`
- result commit `ae29ddbb41153e73d182173d6261e01f48a0bd00`
- classification `AUX_GAUSSIAN_LOCAL_COUNTERTERM_ANSATZ_INSUFFICIENT_SCOPED`
- production run `34958385950`.

That gate prospectively tested a degree-<=13 polynomial action in alpha, motivated there by the O(4)-invariant basis `{Delta^j delta_0}_{j=0..13}`, and found held-out divergence after subtraction on P1 and P3.

## HYPOTHESIS

The same degree-<=13 alpha-polynomial action is not merely the action of the O(4)-invariant Laplacian basis. It is the complete action, on the frozen radial Gaussian test family, of **every** distribution supported at the full K5 collision point and of derivative order <=26:

`C = sum_{|beta|<=26} c_beta partial^beta delta_0` on `R^4`.

For

`phi_alpha(x)=exp(-alpha |x|^2)`,

freeze the exact identity

`<partial^beta delta_0, phi_alpha> = (-1)^|beta| partial^beta phi_alpha(0)`.

Because the Gaussian factorizes by coordinate:

- if any beta_i is odd, the derivative at the origin is zero;
- if beta_i=2 m_i for all i, the result is a nonzero rational/integer coefficient times `alpha^(sum_i m_i)`;
- `sum_i m_i = |beta|/2 <=13`.

Conversely, for every j=0..13, `partial_1^(2j) delta_0` has nonzero action proportional to `alpha^j`.

Therefore the radial action space should be exactly `span{1,alpha,...,alpha^13}` with rank 14.

## Frozen object

This is an exact symbolic/combinatorial theorem gate. No regulator-path numerical values are refit and no scientific thresholds from the parent are changed.

Enumerate every multiindex

`beta=(b1,b2,b3,b4)`, `b_i>=0`, `|beta|<=26`.

For every beta derive its exact alpha monomial degree and exact integer coefficient from the one-dimensional identity

`d^(2m)/dx^(2m) exp(-alpha x^2)|_{x=0} = (-1)^m (2m)!/m! * alpha^m`.

Include the distributional pairing sign `(-1)^|beta|` exactly. Since every surviving beta is even, that outer sign is +1.

## Positive controls

1. Enumerated multiindex count must equal `C(30,4)=27405`.
2. Every multiindex with at least one odd component must map to zero.
3. Every all-even multiindex maps to exactly one degree j in `{0,...,13}`.
4. The set of nonzero degrees is exactly `{0,...,13}`.
5. Exact action-space rank is exactly 14.
6. Witness `beta=(2j,0,0,0)` is nonzero for every j=0..13.
7. Direct exact expansion of `(Delta^j phi_alpha)(0)` from multiindices reproduces `(-4 alpha)^j (j+1)!` for j=0..13.
8. The parent calibration/held-out alpha grids are source-locked but are not used to fit anything in this gate.

## Negative/adversarial controls

1. If the derivative-order cap is synthetically changed to 24, the computed radial degree ceiling must drop to 12 and rank to 13.
2. If a synthetic non-radial test monomial factor is introduced in the control harness, at least two even multiindices of the same total order must become distinguishable; otherwise the code is accidentally hard-wired to total order rather than radiality.
3. Any use of floating-point rank is forbidden; all decisions are exact integer/rational/combinatorial.

## PASS

`AUX_GAUSSIAN_FULL_COLLISION_ORDER26_RADIAL_ACTION_SPACE_EXHAUSTED_SCOPED`

iff every positive and adversarial control passes and the exact rank is 14 with degree set `{0,...,13}`.

## FAIL

`SCIENTIFIC_FAIL_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS`

iff the exact theorem claim is false under the frozen object and enumeration is valid.

## INVALID

`INVALID_IMPLEMENTATION`

for source-lock failure, enumeration/control failure, changed dimension/order cap, floating decision logic, or changed radial test family.

## Consequence if PASS

A PASS may be combined with the already-terminal parent result to strengthen only the following scoped statement:

> On the frozen radial Gaussian test family, **no** full-collision-supported local distribution of derivative order <=26 can remove the P1/P3 held-out divergence found by run `34958385950`, because the parent already tested the complete 14-dimensional radial action space of that entire class.

This does not rule out:

- counterterms supported on proper K5 collision strata;
- a rigorously justified derivative order >26 under a different/correlated scaling-degree analysis;
- nonlocal/source-defined extensions;
- source-authorized prescriptions outside the auxiliary surrogate.

## Interpretation ceiling / governance

No model/family failure, no Eq. (4) existence/nonexistence statement, no D7 closure, no final selector, and no Candidate Gravity activation.

`RQIR Core v1.0 = FROZEN`; D7-S2/S3 remain not closed; D7-S4 partial; KMQGB remains downstream of pinned DSIR authority.
