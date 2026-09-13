# Iter477 preregistration — exact source Toller beta->0 singular order

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent: main through Iter473–476 recovery.

## Question
Can the unstable individual-branch fitted powers seen in Iter474 be replaced by an exact source-backed local asymptotic order, using the published Toller hypergeometric parameters and the standard Gauss hypergeometric z->1 formula rather than a fitted exponent?

## Source formulas
For the published source branches with `z=exp(-2 beta)`:
- plus: `a=j+m+1`, `b=j+1-i rho`, `c=1+m-i rho`;
- minus: `a=j-m+1`, `b=j+1+i rho`, `c=1-m+i rho`.

Therefore the audit must verify algebraically, independently for both branches,
`a+b-c = 2j+1` and hence `c-a-b = -(2j+1)`.

External mathematical authority: NIST DLMF 15.4.23. For `Re(c-a-b)<0`,
`F(a,b;c;z)/(1-z)^(c-a-b) -> Gamma(c) Gamma(a+b-c)/(Gamma(a) Gamma(b))` as `z->1-`.

On the EPRL panel `rho=gamma*j>0`, the audit must verify the total leading coefficient obtained after multiplying by the source Toller Gamma prefactor is finite and nonzero. Gamma-function nonvanishing and the nonzero imaginary parts of the potentially problematic complex arguments are part of the exact certificate.

## Frozen panel
- gamma = {7,8}
- j = {2,5}
- all integer m in [-j,j]
- rho=gamma*j
- numeric cross-check beta = {0.05,0.025,0.0125}
- direct convergent 2F1 power series, no alternate regulator.

## Frozen PASS rule
PASS iff for every frozen record and both branches:
1. exact parameter identity `a+b-c=2j+1` holds;
2. the DLMF leading coefficient, including the source Toller prefactor, is finite and nonzero;
3. the numerical correct-order scaled ratio `R_N=t_branch*(1-z)^N/C_N` approaches 1 monotonically over the frozen beta panel;
4. at the smallest beta, the correct exponent `N=2j+1` is closer to unit scaling than both wrong-exponent controls `N-1` and `N+1`.

PASS label: `ITER477_SOURCE_TOLLER_EXACT_BETA0_BRANCH_ORDER_2JPLUS1_QUALIFIED_SCOPED`.

If the exact algebra succeeds but the frozen numerical confirmation does not, classify `ANALYTIC_ORDER_SUPPORTED_NUMERIC_CONFIRMATION_UNRESOLVED_SCOPED`; do not retune thresholds.

## Scope guards
This is a **one-wedge individual Toller-branch** singular-order result. It is not a K5 contracted collision exponent, not a proof that magnetic/intertwiner/group contractions fail to cancel the leading coefficient, and not a causal-vertex divergence theorem. Never compare `2j+1` directly to Iter471 pcrit as if they were the same physical exponent. The recombined identity `t_+ + t_- = D` may cancel singular pieces, but a causal amplitude selecting one branch cannot silently be replaced by the recombined noncausal object. D7-S2 remains fail-closed.