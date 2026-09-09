# SYNTHESIS-003 — Subtraction-Free Dispersive Hard Selector

**Status:** REJECTED as P4 origin law / retained dispersive control.  
**KMQGB iteration:** 086.  
**Purpose:** test whether analyticity, crossing, unitarity and sufficiently soft UV behavior can determine the channel-irreducible four-graviton hard datum without inserting a new kernel by hand.

## 1. Proposed selector

Start from a physical helicity four-graviton amplitude with the Einstein massless pole separated explicitly. Assume a UV falloff strong enough that the regular hard part admits an unsubtracted or effectively subtraction-free dispersion relation.

Schematically for a crossing-adapted hard coordinate,

`K4(z) = integral ds' rho4(s')/(s'-z) + crossed channels`,

where `rho4` denotes the appropriate physical discontinuity/partial-wave data.

The proposed principle was:

> choose the unique crossing-symmetric, unitary, causal hard amplitude reconstructed from its own physical discontinuities with no subtraction constants.

This would be attractive because eliminating subtraction polynomials appears to remove the ordinary contact/Wilson ambiguity exposed by Iter083.

## 2. A1 — reconstruction map is explicit, origin data are not

A dispersion relation is a concrete reconstruction rule once the discontinuity is known. But the rule does not by itself derive the discontinuity.

Modern primal dispersive bootstrap methods make this distinction explicit: the imaginary parts of partial waves are parameterized as the dynamical data, while dispersion relations, crossing and unitarity map/constrain those data into amplitudes.

Thus the missing hard datum has moved from a subtraction polynomial into the spectral/partial-wave functions.

Classification:

`A1 BLOCKED__DISCONTINUITY_DATA_NOT_SELECTED_BY_DISPERSION_RELATION`.

## 3. A2 — functional freedom survives without subtractions

Let `Im a_l(s)` be the absorptive part of a physical partial wave. Unitarity constrains it, for example through inequalities or nonlinear relations involving `|a_l|^2`, but generic unitary solutions still contain functions of `s` for each allowed `l` and channel.

Removing subtraction constants does not collapse

`{ Im a_l(s) }`

to finite parent data.

In KMQGB language, the structural-null space is no longer an arbitrary polynomial tower but a spectral/partial-wave functional space. Without an independent finite microscopic rule for these functions, `FF_D` grows as spectral/partial-wave resolution is increased.

Classification:

`A2 FAIL__SPECTRAL_PARTIAL_WAVE_FUNCTIONAL_FREEDOM_REMAINS`.

## 4. Crossing/unitarity are constraints, not a unique origin law

Crossing couples the channel data and full unitarity strongly shrinks the admissible set. Regge boundedness can reduce the number of subtractions and sharpen positivity/null constraints.

However contemporary bootstrap results produce allowed regions/bounds unless further special structure is imposed. In the Virasoro-Shapiro case, additional Virasoro/string-inspired nonlinear relations or level-truncation/high-energy assumptions are what drive the solution toward the string trajectory.

Therefore

`analyticity + crossing + unitarity + UV falloff`

is a consistency architecture, not a general unique gravitational parent selector.

## 5. A3 — registered S-matrix/bootstrap comparator

The proposed construction is exactly within modern analytic/primal/dispersive S-matrix bootstrap architecture, already registered as a comparator in KMQGB.

Classification:

`A3 FAIL__STANDARD_DISPERSIVE_S_MATRIX_BOOTSTRAP_ARCHITECTURE`.

## 6. What would reopen this route

A dispersive parent could become interesting only if an independent finite gravity-specific microscopic rule prospectively derives the complete discontinuity data, for example

`finite parent -> rho4(s,t; helicities) -> dispersion -> K4`,

with

- no arbitrary spectral density;
- fixed normalization before candidate comparison;
- same-parent CTP/retarded continuation;
- comparator-orthogonal higher-point relations.

In that case the parent is the rule generating `rho4`, not the dispersion relation itself.

## 7. Score consequence

No P4 credit. R4 remains 45%.