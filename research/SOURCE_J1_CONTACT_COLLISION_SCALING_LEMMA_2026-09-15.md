# Source j=1 coherent-contact collision scaling lemma

Date: 2026-09-15
Status: `DERIVED_KMQGB_ANALYTIC_LEMMA`
Role: outcome-independent support for the prospectively frozen V4 transfer gate; no V4 classification is assumed.

## Source object

Use Bianchi–Chen–Gamonal, arXiv:2601.23162v1:

- Appendix C Eq. (C6)–Eq. (C9), especially `B(z,g)` in Eq. (C7);
- Appendix D Eq. (D1)–Eq. (D4), especially
  `Theta_(sigma,rho,j)(B)=theta(sigma B)+sigma delta^(rho,j)(B)` and the finite sum of delta derivatives.

Freeze `j=1`, so the contact sum contains exactly `delta(B)`, `delta'(B)`, and `delta''(B)`.

This lemma concerns one wedge and one positive pure-boost radial collision. It does not multiply contact distributions across K5.

## Exact pure-boost coordinate

Let

`g_beta = exp[(beta/2) n.sigma]`, `beta>0`, `|n|=1`.

For a projective spinor `z`, define its Bloch component along the boost direction

`u = <z|n.sigma|z>/<z|z>`, so `u in [-1,1]`.

Because `g_beta` is Hermitian and

`g_beta g_beta^dagger = exp(beta n.sigma) = cosh(beta) I + sinh(beta) n.sigma`,

source Eq. (C7) gives exactly

`B_beta(u) = log(cosh(beta) + u sinh(beta))`.

Hence

`B_beta(u) = beta u + (beta^2/2)(1-u^2) + O(beta^3)`

and the source collision variable has the required nontrivial linear part.

More importantly, the map is exactly invertible for fixed `beta>0`:

`u(B) = [exp(B)-cosh(beta)]/sinh(beta)`.

The contact support `B=0` occurs at

`u0(beta) = [1-cosh(beta)]/sinh(beta) = -tanh(beta/2)`,

which lies strictly inside `(-1,1)` for every finite `beta>0` and approaches `0` as `beta->0+`.

Exact derivatives of the inverse map at contact are

`u^(q)(0) = 1/sinh(beta)`

for every integer `q>=1`.

## Pullback of contact derivatives

Let `f(u,beta)` denote a smooth local test weight obtained after the source coherent-Wigner integrand is kept in its recombined polynomial/integral form. Change variables from `u` to `B`:

`du = exp(B)/sinh(beta) dB`.

For the zeroth contact,

`Integral du f(u,beta) delta(B_beta(u))`

is proportional to `csch(beta)` and therefore can have leading order `beta^-1`.

For `delta'(B)`, the distribution differentiates once with respect to `B` the transformed test weight

`f(u(B),beta) exp(B)/sinh(beta)`.

Since both `u'(0)` and the Jacobian factor are proportional to `csch(beta)`, the strongest term is proportional to `csch(beta)^2`, hence at most `beta^-2`.

For `delta''(B)`, two `B` derivatives of the transformed test weight produce a strongest term proportional to `u'(0)^2` times the Jacobian, i.e. `csch(beta)^3`, hence order `beta^-3`. All other terms contain fewer powers of `csch(beta)` and are lower order.

Thus the exact hierarchy is

- `delta(B)` -> no stronger than `beta^-1`;
- `delta'(B)` -> no stronger than `beta^-2`;
- `delta''(B)` -> may produce `beta^-3` and is the **only** Appendix-D contact term capable of doing so at `j=1`.

## Step part

For `beta>0`,

`theta(sigma B_beta(u))`

restricts the compact projective-spinor domain by a boundary at `u=u0(beta)`. As `beta->0+`, `u0(beta)->0`. The recombined source coherent-Wigner integrand is smooth in the group variable at the identity before the Feynman projector split; restricting a compact integral by a moving half-domain can change its finite limit but does not introduce a `beta^-3` radial pole.

Therefore the regular step contribution cannot be the source of a nonzero cubic Laurent coefficient.

## Consequence for V4

For the complete source `j=1` D1–D4 split, a nonzero magnetic `beta^-3` Laurent coefficient of the same Toller branch, once the V3/V3K coherent↔magnetic projector bridge is fixed, has a unique source origin: the highest `delta''(B)` contact component.

This lemma does not assume that the cubic coefficient is nonzero. V4 independently recomputes that magnetic Laurent coefficient from the exact source formulas and then performs the fixed K5 channel contraction.

## Claim ceiling

The lemma proves only the source-component **order identification** for one-wedge pure-boost collision scaling. It does not prove:

- existence of a product of multiple contact distributions;
- K5 survival/cancellation;
- absolute or ordinary divergence;
- regulator-path independence/dependence;
- D7 closure or any terminal selector.

Governance remains unchanged.
