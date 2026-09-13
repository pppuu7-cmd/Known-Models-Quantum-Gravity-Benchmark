# Iter470 preregistration — global spectral decay budget for the Iter468/469 source object

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent authority: Iter463, Iter468, Iter469.

## Question
Given the source-faithful ten-variable spectral object and the qualified one-wedge leading powers, what decay must the common group-contraction kernel supply for a simple absolute-integrability proof at large simultaneous spectral radius?

## Frozen input
For each wedge, after the published Feynman denominator contributes one inverse power, use the Iter463 leading envelope power
- m=0 -> p_e=0;
- m=+/-1 -> p_e=1.
No statement is made about cancellations or conditional oscillatory convergence.

For a ten-dimensional isotropic shell, if the source-weight product grows as R^q and a candidate kernel bound is |C| <= const R^-c, the absolute radial comparison behaves as R^(9+q-c). The simple comparison proof closes only for c>q+10; equality is classified MARGINAL/UNRESOLVED, not divergent.

## Frozen streams
A. Enumerate all 3^10 magnetic patterns and exact multiplicities by q=sum p_e.
B. Verify multiplicities analytically as C(10,q) 2^q and total 59049.
C. Produce the isotropic strict-decay threshold c>q+10 for every q=0..10 and the coordinatewise sufficient condition c_e>p_e+1.
D. Negative controls: removing the source Feynman denominator must shift every one-wedge power and the isotropic threshold by exactly +10 in aggregate; equality at threshold must remain MARGINAL, never FAIL/divergence.

## PASS rule
PASS iff exact enumeration, analytic multiplicities, threshold algebra and controls all agree.

PASS label: `ITER470_TEN_SPECTRAL_ABSOLUTE_DECAY_REQUIREMENT_BUDGET_PINNED_SCOPED`.

## Scope guards
This gate does not measure the actual decay of the SL(2,C) group kernel and cannot prove convergence or divergence. It only pins the quantitative decay burden any later absolute-comparison theorem must meet. Conditional/distributional convergence remains a separate possibility. D7-S2 stays open unless an actual source-backed kernel bound closes it.