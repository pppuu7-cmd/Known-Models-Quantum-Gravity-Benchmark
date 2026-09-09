# SYNTHESIS-005 — Schwarz–Pick Causal Extremality

**Status:** REJECTED as P4 gravity parent / retained exact causal-extremality control.  
**KMQGB iteration:** 090.  
**Purpose:** test whether the functional freedom of a causal/passive Herglotz response can be removed by an extremal principle rather than by supplying an arbitrary spectral measure.

## 1. Proposed selector

Let the parent retarded response `F` be a nonconstant Herglotz map from the upper half-plane `H` to itself.

Schwarz-Pick implies contraction of the hyperbolic metric:

`d_H(F(z1),F(z2)) <= d_H(z1,z2)`.

The attempted physical selector is maximal causal transport:

> the fundamental gravitational response saturates the causal analytic contraction bound for at least one nontrivial pair of points.

This is a genuine extremal condition, not a fitted form factor.

## 2. Exact rigidity theorem

The equality case of Schwarz-Pick states that if a nonconstant holomorphic self-map of the upper half-plane attains equality for one pair of distinct points, it is an automorphism of the upper half-plane.

Therefore

`F(z) = (a z + b)/(c z + d)`

with real `a,b,c,d` and `ad-bc>0`.

Thus the extremal principle collapses the infinite Herglotz measure freedom to finite Möbius data.

Classification:

`A2 PASS__EXTREMALITY_COLLAPSES_LINEAR_RESPONSE_TO_FINITE_DATA`.

## 3. O3 rational-localization consequence

A Möbius transfer function is rational. It has at most one finite simple pole after trivial affine pieces are separated.

By the Iter074 rational-kernel localization gate, such a response admits a finite-dimensional auxiliary/mediator realization. It is therefore not a genuinely new D-nonlocal spectral object.

Classification:

`A3/E2 FAIL__SCHWARZ_PICK_EXTREMAL_RESPONSE_IS_RATIONAL_FINITE_MEDIATOR_CLASS`.

## 4. Gravity-attribution problem

The Schwarz-Pick theorem is universal complex analysis. Nothing in the equality condition selects spin-2 tensor structure or gravitational Ward data.

Even before the rational-localization failure, a gravity parent would have to explain why this extremality applies to a specific gravitational process rather than to an arbitrary passive linear system.

## 5. Higher-point lesson

The result closes an important loophole:

- generic causal/passive linear response -> arbitrary positive spectral measure;
- maximal Schwarz-Pick extremality -> finite Möbius/rational mediator response.

Neither endpoint yields the required irreducible non-Gaussian four-graviton datum.

Therefore the remaining novelty must reside in a genuinely higher-point nonlinear gravitational process law, not in extremizing a one-response transfer function.

## 6. Score consequence

No P4 credit. R4 remains 45%.