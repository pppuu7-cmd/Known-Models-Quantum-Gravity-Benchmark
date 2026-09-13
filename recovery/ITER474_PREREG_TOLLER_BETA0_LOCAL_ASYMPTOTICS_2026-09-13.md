# Iter474 preregistration — source Toller beta->0 local asymptotics

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION

## Question
What local small-beta powers are actually exhibited by the published-source Toller branches `t_+`, `t_-` and by their recombined sum on the frozen EPRL source panel? This is a one-wedge/local diagnostic needed before comparing any contracted collision power to Iter471.

## Frozen source panel
- gamma: 7, 8
- j: 2, 5
- every integer m in [-j,j]
- beta grid: 0.4, 0.2, 0.1, 0.05, 0.025, 0.0125
- rho = gamma*j
- source hypergeometric/Gamma formulas inherited unchanged from Iter443
- independent precision routes: 80 dps and 120 dps.

For each branch and the recombined sum, report nested-window log-log slopes of absolute magnitude versus beta. Define the descriptive local power as `p=-slope`; do not preassign its value.

## Frozen qualification checks
1. all values on both precision routes are finite;
2. 80/120-dps relative disagreement <= 1e-18 wherever the reference magnitude exceeds 1e-40, otherwise absolute disagreement <=1e-40;
3. nested last-3 versus last-4 point power estimates differ by <=0.35 for every non-negligible branch/sum channel;
4. the recombined `t_+ + t_-` route is evaluated directly from the two published branches, with `t_+ - t_-` retained as a wrong-recombination negative control and required to differ in at least one frozen record.

PASS label: `ITER474_SOURCE_TOLLER_BETA0_LOCAL_ASYMPTOTICS_CHARACTERIZED_SCOPED`.

A failed stabilization check is scientific `UNRESOLVED_ON_FROZEN_GRID`, not divergence.

## Scope guards
No promotion of a one-wedge branch power to a K5 contracted collision exponent. No statement that p>=pcrit proves divergence. No full causal-vertex convergence/finiteness claim. Iter471 thresholds remain comparison geometry only until contractions, magnetic sums, angular structure and noncancellation are source-backed.