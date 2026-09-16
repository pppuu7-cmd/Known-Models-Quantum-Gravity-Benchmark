# SOURCE_J1_K5_TRIANGLE_CONTACT_REGULARIZATION_V6 — prospective preregistration

Date: 2026-09-16
Parent authority: Critic-qualified V5 front `e79e63cc1796fd63600a20327c988d30806160f4`.

## Question

At the already frozen coherent-contact K5 triangle witness with exact conormal relation
`dB12 + dB23 - dB13 = 0`, does a concrete approximate-identity regularization of the three nonzero contact factors produce a regulator-independent local product coefficient, or does the coefficient depend on the allowed mollifier widths?

This gate is deliberately narrower than existence/nonexistence of the full ten-factor contact product. It tests a local three-contact triangle subobject only.

## Frozen local object

Use normal-form coordinates `(x,y)` for the exact triangle relation:

- `B12=x`,
- `B23=y`,
- `B13=x+y`.

For positive rational `a`, define the normalized Gaussian approximate identity

`delta_eps^a(t)=sqrt(a)/(sqrt(pi)*eps)*exp(-a*t^2/eps^2)`.

For positive rational `(a,b,c)`, define

`I_eps(a,b,c)=Integral_R2 delta_eps^a(x) delta_eps^b(y) delta_eps^c(x+y) dx dy`.

Exact Gaussian integration gives

`I_eps = C(a,b,c)/(sqrt(pi)*eps)`,

with decision statistic

`S(a,b,c) := pi * (eps*I_eps)^2 = a*b*c/(a*b+a*c+b*c)`.

No floating-point threshold is allowed.

## Prospectively frozen schemes

Evaluate exactly:

- A = `(1,1,1)`;
- B = `(1,1,4)`;
- C = `(1,2,3)`.

Expected values are NOT hard-coded as pass conditions. The implementation must derive `S` from the quadratic-form determinant. Controls independently verify normalization algebra, determinant positivity, permutation symmetry, and a forest two-contact control whose integrated product is regulator-normalized and has no triangle overconstraint.

## Classifier

- `TRIANGLE_CONTACT_REGULARIZATION_DEPENDENT_SCOPED` iff all controls pass and at least two exact `S` values differ.
- `TRIANGLE_CONTACT_REGULARIZATION_INVARIANT_SCOPED` iff all controls pass and all exact `S` values are identical.
- `INVALID_IMPLEMENTATION` iff any frozen control fails.

A workflow/execution failure is infrastructure/numerical until the first causal failure is identified; it is not a scientific classification.

## Interpretation ceiling

`DEPENDENT_SCOPED` means only: within this explicitly frozen normalized Gaussian approximate-identity class, the leading `1/eps` coefficient of the local three-contact triangle product depends on regulator widths. Together with the already-established failure of the standard Hoermander sufficient criterion, this is evidence that the naive local product is not canonically regulator-independent under this class.

It is NOT a theorem that no distributional extension exists, NOT a proof of full K5 vertex divergence/nonuniqueness, NOT D7 closure, and NOT a family/model verdict. A renormalized extension could still require additional prescription/data.

`INVARIANT_SCOPED` is likewise restricted to these three schemes and does not prove full product existence.

## Governance

D7-S2/D7-S3/D7-S4 remain open regardless of this gate alone. Terminal selector labels remain forbidden. Candidate Gravity remains inactive. No scientific criterion may be weakened after observing results.
