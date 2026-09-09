# P4 Retarded Herglotz Spectral-Freedom Gate

**Status:** permanent real-time/causal P4 prefilter.  
**KMQGB iteration:** 089.  
**Purpose:** prevent causality/passivity/retarded analyticity from being mistaken for a unique dynamical selector when they only characterize a positive spectral family.

## 1. Linear causal-passive response class

For a one-variable passive causal transfer/response function with the appropriate reality property, analyticity in the upper half-plane and nonnegative imaginary part place the response in the Herglotz-Nevanlinna class.

A standard representation has the schematic form

`F(z)=a+b z + integral_R [1/(t-z)-t/(1+t^2)] dmu(t)`,

with

- `a` real;
- `b>=0`;
- `dmu(t)` a positive measure satisfying the usual growth condition.

The exact subtraction convention is not the point. The structural fact is that the admissible class is parameterized by a positive measure.

## 2. Functional-freedom consequence

Causality, passivity and positivity constrain `dmu` but do not generically derive it from finite data.

As spectral resolution/cutoff is increased, independent admissible measure directions remain. Therefore

`retarded analyticity + positivity/passivity`

by itself does not satisfy the KMQGB finite-parent requirement.

Classification:

`A2 FAIL_IF_ONLY_HERGLOTZ_CLASS_IS_SPECIFIED__POSITIVE_SPECTRAL_MEASURE_REMAINS_FREE`.

This is the real-time analogue of the Källén-Lehmann/dispersive spectral-freedom gate.

## 3. Relation to O3 and O4

### O3

A nonlocal retarded kernel is not novel merely because its support is causal and its spectral density is positive. The parent must derive the measure/kernel and linked non-Gaussian higher-point data.

### O4

A reduced dissipative/decohering response can satisfy causal/passive constraints while still admitting an ordinary environment realization. The Stinespring attribution gate remains mandatory.

Thus real-time consistency is necessary representation completeness, not sufficient origin physics.

## 4. Gravity-specific requirement

A future gravity parent must go beyond a one-response Herglotz certificate and derive, from the same finite data,

- physical spin-2 tensor/helicity structure;
- an irreducible hard four-point or higher relation;
- retarded/advanced/Keldysh relations;
- and the spectral/absorptive data entering those relations.

If only the class of allowed spectral measures is specified, P4 remains blocked.

## 5. Extremal loophole to test next

One possible attempt to remove the measure freedom is to impose an extremal causal condition, such as saturation of a Schwarz-Pick/Herglotz contraction bound.

That route must be checked separately: equality cases of Schwarz-Pick are highly rigid and may collapse to Möbius/rational response functions, which would trigger the O3 rational-localization / ordinary-mediator gate.

## 6. Score consequence

No P4 credit. R4 remains 45%.