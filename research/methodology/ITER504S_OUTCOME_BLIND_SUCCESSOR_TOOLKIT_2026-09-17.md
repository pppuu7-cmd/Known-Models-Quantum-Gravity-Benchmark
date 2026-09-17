# Iter504S outcome-blind successor mechanism toolkit

Date: 2026-09-17
Status: FROZEN GENERIC METHODOLOGY BEFORE REPAIRED ITER504S TERMINAL OUTCOME

This document does **not** choose an Iter504S outcome and is not a successor scientific preregistration. It freezes generic mathematical machinery that may be instantiated only after the repaired Iter504S terminal class is known. No witness, channel pair, partition depth, held-out case, or favorable parameter is selected here.

Scientific Iter504S authority remains `f6367456aa715fe6282ab70c1b2005971a4568c7`. The single repaired run is `35175533159`.

## A. Validated local derivative enclosure machinery

For a root interval `I` and deterministic child/subroot interval `J subset I`, construct the dual state directly with amplitude interval `J`, not with a point derivative substituted as truth.

For every retained channel `f_i`, require an interval derivative object `D_i(J)` satisfying

`forall a in J: f_i'(a) in D_i(J)`.

For the Haar/log term require the analogous validated derivative enclosure.

If `m_J` is the exact rational midpoint of `J`, the mean-value inclusion used downstream is

`f_i(J) subset f_i(m_J) + (J-m_J) D_i(J)`.

This is valid because each `a in J` has some segment between `m_J` and `a` wholly contained in `J`, and the derivative on that segment is contained in `D_i(J)`.

A local-D implementation must never replace `D_i(J)` by the midpoint of a derivative ball or by sampled derivatives.

### Optional contraction certificate

When mathematically expected, record exact Arb inclusion checks

`D_i(J) subseteq D_i(I)`

for every one of the 243 channels and the Haar/log derivative. Failure of such inclusion is not automatically invalid—the two validated constructions may have different dependency inflation—but any claimed contraction must be certified componentwise rather than inferred from nominal radii.

### Generic no-retuning controls

A future instantiated gate must freeze before output:

- deterministic child partition rule;
- exact maximum depth;
- whether derivatives are recomputed on every child or on fixed subroots;
- Arb precision;
- all 243 channels and no-pruning rule;
- rho/R grids;
- same drift and slope formulas;
- threshold `0.05` and floor `1.0` unless a completely new scientific question is prospectively preregistered;
- PASS/INCONCLUSIVE/INVALID conditions.

No post-outcome depth extension is permitted.

## B. Max-channel switching / dominance-cell machinery

For channels `i,j`, prefer the pre-log comparison quantity

`Q_ij(a;R,rho) = |f_i(a;R,rho)|^2 - |f_j(a;R,rho)|^2`

when this is numerically and analytically safer than subtracting logarithms. On domains where both magnitudes have positive lower bounds, `sign(Q_ij)` is equivalent to the ordering of `log|f_i|` and `log|f_j|`.

A future switching certificate must use validated interval evaluation/root isolation to classify a prospectively selected pair/domain as one of:

- strict `i>j` dominance;
- strict `j>i` dominance;
- one isolated crossing;
- multiple isolated crossings;
- unresolved crossing structure.

No fitted crossing location is admissible.

### Dominance cells

If all relevant pair relations can be certified on a subinterval, define a dominance cell there. A cell may have:

- one unique-max channel, certified by `L_i > max_{j!=i} U_j`; or
- a bounded active set when unique dominance is not certifiable.

Continuous drift may then be evaluated piecewise over cells without smoothing the max and without choosing a preferred channel for convenience.

The active set remains a subset only for the **cell proof**; the underlying full-envelope calculation must retain all 243 channels unless strict interval dominance has certified the excluded channels cannot maximize there.

## C. Direct fixed-channel local-function machinery

If a future Iter504S result implicates fixed-channel nonstationarity, the derivative-center control is insufficient evidence by itself.

For a prospectively frozen witness channel and exact amplitudes/subintervals, recompute that channel from the source-faithful KAK/Toller/intertwiner/contraction route using validated Arb values. Compute late and early slope enclosures directly from validated channel magnitudes.

A genuine fixed-channel mechanism requires direct validated `drift_upper > 0.05` under the frozen local-function construction, ideally reproduced by an independent route. If direct drift is within tolerance, the center-D affine sensitivity—not the physical/source channel—is localized as the cause.

## D. Mixed-mechanism factorial discriminator machinery

If repaired Iter504S returns MIXED, form a case matrix indexed exactly by

`root x location x rho`

with prospectively defined columns:

- full-D violation;
- center-D violation;
- derivative-radius sensitivity;
- competition completeness;
- competition necessary;
- fixed-channel nonstationarity;
- strict dominance presence;
- possible-max multiplicity.

Do not average these mechanisms into one score. Select the smallest deterministic next cohort by an outcome-independent rule frozen after the matrix exists but before successor computation—for example lexicographic first representatives of each distinct mechanism signature. The rule, not manual ease-of-PASS selection, must choose cases.

## E. Held-out generalization firewall

Any mechanism repair that succeeds on roots 13-15 must pass a prospectively chosen held-out representative cohort before a full Iter504-domain campaign is authorized.

The held-out selection rule must be frozen before the repair is applied to those cases and should cover different structural regimes where authority permits, such as non-crossing behavior, high possible-max multiplicity, a different rho regime, or another authorized causal/path family.

No three-root result may be promoted directly to all 1888 parent states.

## Claim ceiling

This toolkit provides generic validated constructions only. It does not select the Iter504S branch, does not claim any mechanism has been established, does not close D7, does not authorize Candidate Gravity or Paper IV, and does not establish quantum gravity or new physics.
