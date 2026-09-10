# O-NONLOCAL Riemann/Weyl amplitude — fixed-order EFT quotient

**Date:** 2026-09-10  
**Iteration:** 186  
**RQIR Core:** v1.0 FROZEN  
**Gate:** `PF2_01B3_RIEMANN_WEYL_AMPLITUDE_RESIDUAL`

## Question

A nonlocal Riemann/Weyl form factor can change on-shell graviton amplitudes relative to Einstein gravity. Does that fact alone provide a comparator-orthogonal nonlocal-QG residual?

## Published starting point

Donà, Giaccari, Modesto, Rachwał and Zhu, arXiv:1506.04589, explicitly show that Ricci/scalar-curvature weakly-nonlocal quadratic theories have Einstein tree amplitudes in the stated class, while addition of an independent Riemann-tensor operator changes the amplitudes and makes them form-factor dependent.

This establishes `A_nonlocal != A_GR` for the Riemann branch, but RQIR requires comparison against the full same-order local higher-curvature EFT span, not GR alone.

## Structural quotient

For an analytic/entire form factor around the comparison point,

`F(Box) = sum_{n=0}^infinity f_n Box^n`.

At any fixed derivative cutoff/order N,

`F_N(Box) = sum_{n=0}^N f_n Box^n`

is a polynomial differential operator. Consequently a term such as

`Riemann F_N(Box) Riemann`

is a finite linear combination of local higher-derivative curvature operators

`sum_{n=0}^N f_n Riemann Box^n Riemann`.

If the same-order comparator basis is complete and its Wilson coefficients are free over exactly these local operator directions, the truncated nonlocal amplitude vector is contained in that comparator span.

Let `J_EFT,N` be the complete local-EFT response matrix through order N and `r_N` the nonlocal-minus-GR amplitude vector at that same truncation. Then structurally

`r_N in Col(J_EFT,N)`

and therefore the RQIR comparator-orthogonal projection obeys

`Pi_perp,N r_N = 0`.

This is an exact basis-containment statement, not a numerical smallness claim.

## What this does and does not prove

It proves that **a single fixed finite EFT order cannot establish uniquely nonlocal ancestry** merely because the Riemann/Weyl amplitude differs from Einstein gravity. The deviation can be represented by the complete local higher-curvature EFT comparator at the same order.

It does **not** prove that a finite-parameter nonlocal parent is globally equivalent to an arbitrary local EFT. A fixed nonlocal form factor can impose cross-order relations among the infinite Taylor coefficients `{f_n}`. Those relations can carry rigidity that is absent when each local-EFT Wilson coefficient is independently free.

Likewise, a finite-energy amplitude evaluated over a domain that resolves the full non-polynomial/entire momentum dependence need not be reproduced by a finite local truncation.

## RQIR result

**`PASS_RQIR_GATE__FIXED_ORDER_LOCAL_EFT_COMPARATOR_ABSORPTION`**

with residual status

**`EXACT_ZERO_COMPARATOR_ORTHOGONAL_RESIDUAL_AT_EACH_COMPLETE_FIXED_LOCAL_EFT_ORDER`**.

This is a negative uniqueness control, not a theory FAIL and not a family sufficiency result.

## Next nonlocal discriminator

The correct next object is no longer a one-order Riemann/Weyl amplitude. It is

**`NONLOCAL_CROSS_ORDER_FUNCTIONAL_RIGIDITY_OR_FULL_MOMENTUM_SHAPE_CERTIFICATE`**.

Required payload:

`{finite-parameter form-factor family, coefficient sequence f_n or full momentum function, same-realization unitarity/causality prescription, multiple prospectively fixed orders/kinematic windows, complete local-EFT comparator at each order, shared-parameter incidence across orders, holdout prediction, cross-order comparator-orthogonal rigidity}`.

A nonzero result must come from the shared functional law / non-polynomial momentum dependence, not from omitting allowed local EFT coefficients.

## Family consequence

`NONLOCAL_QG` remains `PARTIAL_SUBFAMILY_ONLY`.

The fixed-order Riemann/Weyl gate is closed as comparator-absorbed. Remaining family-level work is cross-order/full-shape rigidity plus disposition of materially distinct non-scattering/loop/form-factor branches. Existing causality PASS/FAIL controls remain realization-local.
