# O3 Rational-Kernel Localization No-Go

**Status:** permanent O3 prefilter.  
**KMQGB iteration:** 074.  
**Purpose:** prevent a finite rational nonlocal form factor from being mislabeled as a genuinely new D-nonlocal gravity parent when it is equivalent to a finite local higher-derivative/auxiliary-field system.

## 1. Scope

Consider a quadratic or response-sector nonlocal structure of the schematic form

`S_nonlocal = 1/2 ∫ J P(Box)/Q(Box) J`,

where `P` and `Q` are finite-degree polynomials and `J` may be a curvature/source/tensor structure with all index projectors understood.

This is the natural output of many finite-state resolvent or finite-rank transfer constructions.

## 2. Polynomial division

Any rational kernel can be written

`P(z)/Q(z) = L(z) + R(z)/Q(z)`,

where `L` is a polynomial and `deg R < deg Q`.

The polynomial piece is a finite local derivative operator. In the gravitational low-energy domain it belongs to the ordinary local higher-derivative/EFT comparator space unless it carries some separately declared symmetry/DOF escape.

## 3. Partial-fraction localization

Over the complex numbers, factor

`Q(z) = C Π_a (z - mu_a)^{r_a}`.

The proper rational part admits a finite partial-fraction decomposition

`R(z)/Q(z) = Σ_a Σ_{p=1}^{r_a} c_{a,p}/(z-mu_a)^p`.

For a simple pole, a term

`(c/2) J (Box-mu)^(-1) J`

is reproduced by a local auxiliary field `chi` with a quadratic local action of the schematic form

`S_aux = ∫[-1/(2c) chi(Box-mu)chi + chi J]`.

Integrating out `chi` gives the original inverse-operator term, up to the standard choice of Green-function/boundary prescription.

Repeated poles can be represented by a finite chain of auxiliary fields or an equivalent finite higher-derivative local system. Complex poles likewise correspond to a finite local enlarged system, generally with additional reality/unitarity constraints and often ghost/instability taxes.

Therefore a finite rational kernel carries only a finite set of extra poles/local derivative data.

## 4. KMQGB classification

For O3 novelty purposes:

- polynomial kernel -> `FULL_C5_OR_LOCAL_HIGHER_DERIVATIVE_CONTAINED` in the ordinary GR-EFT domain;
- rational kernel with additional physical poles -> `C4_C6_FINITE_MEDIATOR_OR_HIGHER_DERIVATIVE_CONTAINED`;
- rational kernel with ghost/complex/unphysical poles -> same structural containment plus consistency failure/tax, not novelty;
- rational kernel whose auxiliary fields are merely hidden by integrating them out is not intrinsically D-nonlocal.

Thus

`finite rational kernel ≠ genuine O3 escape`

unless a separate observable relation survives the fully localized comparator description.

## 5. Finite-rank resolvent corollary

A finite-dimensional hidden transfer system produces a resolvent

`V†(z-H)^(-1)V`,

which is rational in `z` because

`(z-H)^(-1)=adj(z-H)/det(z-H)`.

Hence any O3 proposal based only on integrating out a **finite-dimensional linear hidden system** is automatically caught by this no-go. It is a finite mediator/auxiliary-field completion in disguise.

This is a useful boundary for O2/O3 crossover proposals.

## 6. What can still escape

A genuinely D-nonlocal O3 candidate must therefore contain a non-rational structure, for example

- an entire/transcendental kernel;
- a branch-cut/continuum spectral object;
- an infinite product or q-difference solution;
- another non-rational object not representable by finitely many local auxiliary poles.

But non-rationality alone is not enough. The kernel must still be **derived from finite parent data**, otherwise `P4_FUNCTIONAL_FREEDOM_NO_GO` applies.

This creates the central O3 tension:

`must be infinite/non-rational enough to avoid finite mediator localization`

while

`must be rigid enough to avoid arbitrary functional freedom`.

## 7. Causality / representation warning

Localization equivalence at the level of formal operators does not by itself identify a unique retarded/Feynman/CTP prescription. A candidate must use the same parent to fix that prescription before comparing observables.

Boundary-condition freedom cannot be used as a novelty loophole.

## 8. Score consequence

This is a necessary-condition prefilter, not a P4 survivor. R1/R2/R3/R4 remain unchanged.
