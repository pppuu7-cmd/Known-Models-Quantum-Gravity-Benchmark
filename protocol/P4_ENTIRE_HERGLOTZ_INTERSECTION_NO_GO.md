# P4 Entire–Herglotz Intersection No-Go

**Status:** exact scoped complex-analysis gate.  
**KMQGB iteration:** 101.  
**Purpose:** test a common O3 shortcut in which the same one-variable function is claimed to be simultaneously an entire nonlocal kernel and a passive causal retarded response.

## 1. Scope

This theorem applies when a proposed scalar response function `F(z)` itself is required to satisfy both

1. `F` is a Herglotz/Pick/Nevanlinna function: it is analytic in the upper half-plane and `Im F(z) >= 0` there (up to an overall sign convention for the retarded response);
2. `F` extends to an **entire** function on the whole complex plane.

It is **not** a theorem that every four-point amplitude is Herglotz, nor that every matrix/tensor response reduces to one scalar Pick function. Those stronger claims require separate justification.

## 2. Herglotz representation

A scalar Herglotz function has the representation

`F(z) = a + b z + integral_R [1/(t-z) - t/(1+t^2)] dmu(t)`

with `a` real, `b >= 0`, and `mu` a positive measure obeying the usual integrability condition.

The measure term carries the nontrivial poles/cuts/spectral support on the real axis.

## 3. Entire extension kills the spectral measure

If `F` is entire, it has no real-axis poles, branch discontinuity or other singular support. In the Herglotz representation this forces

`mu = 0`.

Therefore

`F(z) = a + b z`, with `b >= 0`.

Equivalently:

> an entire scalar Herglotz function is affine.

This is a standard consequence of the Herglotz representation and also admits a direct power-series proof.

## 4. KMQGB consequence

A candidate cannot obtain a genuinely nonlocal causal/passive scalar response merely by declaring the **same** function to be

- entire / ghost-free / pole-free;
- retarded-causal and Herglotz-positive;
- nontrivial at arbitrarily high order.

Under the scoped assumptions, the intersection collapses to the affine class.

Classification:

`ENTIRE_PLUS_HERGLOTZ_SAME_RESPONSE__AFFINE_COLLAPSE`.

An affine response is finite/local/rational from the KMQGB O3 perspective and does not supply a genuinely new hard nonlocal parent by itself.

## 5. Legitimate escape routes

A serious candidate can evade this gate only by changing at least one premise explicitly, for example:

1. the hard amplitude is not itself the passive Herglotz response; only a derived two-point/linear-response object has that property;
2. the function is analytic only in the causal half-plane and has physical cuts/poles on the boundary rather than being entire;
3. matrix/operator positivity replaces a scalar Herglotz condition and yields genuinely new structure;
4. the proposal is non-passive/non-Herglotz and independently proves probability/causality consistency;
5. the nonlocality lives at higher connected order rather than in the linear response.

These are reopen conditions, not loopholes to be assumed silently.

## 6. Relation to prior KMQGB gates

This result strengthens the previous pair of controls:

- general Herglotz causality leaves an arbitrary positive spectral measure;
- Schwarz–Pick extremality collapses the causal map to a rational Möbius form.

The new intersection theorem shows that demanding global entire analyticity does **not** create a rich middle ground: for the same scalar response it collapses even further to an affine function.

## 7. Search consequence

The surviving same-spectrum nonlocal P4 corridor should therefore place genuinely new structure in

- higher-point irreducible kernels;
- a derived physical cut/spectral sector with parent-fixed measure;
- a nonperturbative/transseries sector;
- or a controlled modification of factorization/quantum dynamics,

rather than in an entire passive scalar propagator/response alone.

## 8. Score consequence

This is a negative structural theorem. R4 remains 45%.