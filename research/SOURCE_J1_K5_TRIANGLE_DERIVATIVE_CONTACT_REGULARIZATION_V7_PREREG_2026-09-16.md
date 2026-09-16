# SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7 — prospective freeze

Date: 2026-09-16
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT
Lane: KMQGB Research / Closure

## HYPOTHESIS

For the same local three-edge K5 triangle conormal realization used in V6, but with the parent V4 highest-contact derivative order restored exactly, the leading coefficient of the Gaussian-regularized triple `delta''` contact product depends on **relative** regulator widths after quotienting out common-width rescaling.

This is a local same-derivative-order bridge only. It is not a full ten-factor K5 product theorem.

## EXACT OBJECT

Use local normal coordinates

- `B12 = x`,
- `B23 = y`,
- `B13 = x + y`,

and the normalized Gaussian approximate identity

`delta_eps^a(t) = sqrt(a)/(sqrt(pi) eps) * exp(-a t^2/eps^2)`, `a>0`.

The derivative-contact factor is the exact second derivative with respect to its argument:

`D2_eps^a(t) := d^2/dt^2 delta_eps^a(t)`

`= 2 a^(3/2)/(sqrt(pi) eps^3) * (2 a t^2/eps^2 - 1) * exp(-a t^2/eps^2)`.

The frozen triangle integral is

`I_eps(a,b,c) = integral_R2 D2_eps^a(x) D2_eps^b(y) D2_eps^c(x+y) dx dy`.

By dimensional scaling the leading power is `eps^-7`. Define

`C(a,b,c) := eps^7 I_eps(a,b,c)`

and the scale-free exact statistic

`K(a,b,c) := pi * C(a,b,c)^2 / (a+b+c)^7`.

`K` is frozen before outcomes because common width scaling `(a,b,c)->lambda(a,b,c)` sends `C->lambda^(7/2) C`, so `K` must remain invariant under common rescaling while retaining dependence on relative widths.

For exact evaluation, let `D=ab+ac+bc` and let `(X,Y,Z=X+Y)` be the centered Gaussian associated with `exp[-a x^2-b y^2-c(x+y)^2]`. Its exact covariances are

- `Var X=(b+c)/(2D)`,
- `Var Y=(a+c)/(2D)`,
- `Var Z=(a+b)/(2D)`,
- `Cov(X,Y)=-c/(2D)`,
- `Cov(X,Z)=b/(2D)`,
- `Cov(Y,Z)=a/(2D)`.

The exact dimensionless polynomial expectation is frozen as

`E = <(2aX^2-1)(2bY^2-1)(2cZ^2-1)>`,

with Wick moments

`<X^2Y^2>=Vx Vy + 2 Cxy^2`, etc., and

`<X^2Y^2Z^2> = Vx Vy Vz + 2 Cxy^2 Vz + 2 Cxz^2 Vy + 2 Cyz^2 Vx + 8 Cxy Cxz Cyz`.

Then

`C = 8 (abc)^(3/2)/(sqrt(pi) sqrt(D)) * E`

and the decision statistic is the exact rational

`K = 64 (abc)^3 E^2 / [ D (a+b+c)^7 ]`.

No floating threshold is used.

## DEPENDENCY / SOURCE-REALIZATION AUTHORITY

Frozen repository authority at preregistration:

- current main before this preregistration: `5a6790ae9d9e020a3a73338293446e0501b3c8c4`;
- repaired V4 run `35033194283`, recorded on current front as `CONFIRMED_SCOPED`, establishing survival of the highest `delta''` contact leading homogeneous tensor for frozen `j=1`, real nonzero `rho`, fixed full-K5 tangent witness and channel `00000`;
- V5 fixed-tangent channel census remains `QUALIFIED`, with exact channel `00000 = 11/24`; this is used only as nonzero angular-channel context, not multiplied into the local integral;
- V6 run `35050058294` and Critic commit `67c0895bf16074091abd9e2643e1629344414263`, which confirm the local triangle normal form but explicitly require restoring `delta''` before same-realization transfer.

The derivative order is taken from V4; the local conormal relation is the V6 triangle geometry. No plain-delta V6 coefficient is imported as a derivative-contact result.

## FROZEN INPUTS

Relative-width schemes:

- A = `(1,1,1)`;
- B = `(1,1,4)`;
- C = `(1,2,3)`.

Common-rescaling control:

- A4 = `(4,4,4)`.

All parameters are exact positive integers/rationals.

## POSITIVE CONTROLS

1. Exact derivative identity for `D2_eps^a(t)` above.
2. Exact Gaussian determinant `D=ab+ac+bc` for the target conormal map.
3. Exact symmetry of `K(a,b,c)` under all six permutations for each frozen scheme.
4. Exact common-rescaling invariance `K(4,4,4)=K(1,1,1)`.
5. Independent transverse two-contact normalization through the same Gaussian-moment machinery:
   `integral_R2 D2_eps^a(x) D2_eps^b(y) x^2 y^2 dxdy = 4` for frozen `(a,b)=(1,4)` and `eps=1`.
6. One-factor normalization checks `integral D2_eps^a(t) dt = 0` and `integral t^2 D2_eps^a(t) dt = 2` for positive frozen `a`.
7. Two independent exact Python lanes (3.11 and 3.13) must agree byte-for-byte on all decision-critical rational fields after canonical JSON serialization.

## NEGATIVE / ADVERSARIAL CONTROLS

1. Wrong derivative polynomial `2 a t^2/eps^2 + 1` must fail the frozen one-factor zero-mass control.
2. Wrong conormal map `B13=x+2y` must be distinguished structurally by its quadratic determinant and must not be accepted as the target map.
3. Plain-delta V6 statistic `abc/(ab+ac+bc)` is recorded only as an adversarial object-identity fixture and must never be substituted for `K`.
4. Any failure of permutation symmetry, common-rescaling invariance, transverse normalization, lane agreement, or exact rational canonicalization invalidates implementation.

## PASS

`TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED` iff all source/object/control locks pass and the exact frozen values `K(A), K(B), K(C)` are not all equal.

## FAIL

`TRIANGLE_DELTA2_CONTACT_REGULARIZATION_INVARIANT_SCOPED` iff all source/object/control locks pass and `K(A)=K(B)=K(C)` exactly.

This FAIL falsifies only the prospectively frozen relative-width-dependence hypothesis on this local Gaussian derivative-contact object. It is not a model/family failure.

## BLOCKED

`TRIANGLE_DELTA2_CONTACT_REGULARIZATION_SOURCE_BLOCKED` iff the repaired V4 derivative-contact authority, V5/V6 realization chain, or exact target conormal/derivative identity cannot be source-locked at execution head. Missing authority is not zero residual and is not scientific FAIL.

## INVALID

`INVALID_IMPLEMENTATION` iff any frozen algebraic/negative/control condition fails, lane decision fields disagree, wrong derivative order is used, the plain-delta V6 statistic is substituted for `K`, or criteria are changed after this preregistration.

## INTERPRETATION CEILING

A PASS would establish only that, for the frozen local triangle with the parent `delta''` derivative order and normalized Gaussian regularization class, the scale-free leading coefficient depends on relative regulator widths. A FAIL would establish only invariance across A/B/C for this exact local object.

Neither outcome proves distributional extension nonexistence, uniqueness/nonuniqueness for all mollifier classes, full ten-contact K5 failure, complete vertex divergence, model/family failure, D7 closure, any terminal selector, or Candidate Gravity activation.

RQIR Core v1.0 remains FROZEN. Historical FAIL/BLOCKED results remain immutable.