# KMQGB Recovery Delta 176

**Date:** 2026-09-10

CW2-02 / O-LQG now has a second independent gamma-sensitive observable candidate inside the area-metric Lorentzian route.

The 2026 area-metric GW/birefringence relation

`sinh(2 xi)=1/gamma`,

`psi=-(1/2) atan(tanh xi)`

is exactly invertible on the positive-gamma branch:

`gamma = -cot(4 psi)`, with `-pi/8 < psi < 0`.

Its derivative is

`d psi/d gamma = 1/[4(1+gamma^2)] > 0`

for every finite positive gamma. Thus the angle is structurally gamma-identifying, although sensitivity becomes poor at large gamma.

Combining this with the Iter173 generalized primordial relation

`q = 1/gamma - gamma - Delta_gamma`

gives the Jacobian

`J = [[-1-1/gamma^2,-1],[1/(4(1+gamma^2)),0]]`

with

`det J = 1/[4(1+gamma^2)] > 0`.

Therefore `{q,psi}` is structurally full rank for `{gamma,Delta_gamma}` if and only if the same-realization parameter map establishes that both observables use the same renormalized gamma after proper RG transport.

A compact direct consistency statistic follows:

`Delta_gamma = 2 cot(8 psi) - q`

when both quantities are referred to the same matched scale.

This supplies a new cross-representation falsifiability route:

`EPRL gamma -> area-metric RG -> birefringence psi`

versus

`EPRL gamma-dual EFT -> primordial q`.

The route remains conditional because the EPRL-to-area-metric parameter identity and multiscale transport are not yet derived. Primordial and low-energy detector observables cannot simply be compared at equal gamma without the RG trajectory.

Updated minimum object:

`SAME_REALIZATION_MULTISCALE_GAMMA_CLOSURE`.

Updated classification:

`PROMISING_ADAPT_EXISTING__AREA_METRIC_BIREFRINGENCE_SUPPLIES_INDEPENDENT_GAMMA_HOLDOUT__SAME_REALIZATION_MULTISCALE_MAP_MISSING`.

Executable authority:

`code/lqg_area_metric_birefringence_gamma_identifiability_reference.py`.

Audit authority:

`paper_iv/O_LQG_AREA_METRIC_BIREFRINGENCE_GAMMA_IDENTIFIABILITY_GATE_2026.md`.

CW2-02 remains OPEN; Closure Wave 02 remains `0/3`; Paper IV remains `NOT_YET_AUTHORIZED`.

No R1/R2/R3/R4 score change. Heavy compute remains idle; practical detector sensitivity is downstream of same-realization and scale matching.
