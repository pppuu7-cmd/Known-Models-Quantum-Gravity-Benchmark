# Iter506 preregistration — uniform full-K5 neighborhood certificate

**Prospectively frozen after consuming terminal Iter505 and before any Iter506 production evidence.**

## Purpose
Iter505 qualified all 18 frozen fixed-causal full-K5 leading-survival lanes at the unchanged finite-t source-regression threshold. Iter506 addresses the next dependent blocker only: turn the nonzero leading witness at each frozen tangent panel into an explicit, conservative open coordinate-neighborhood certificate using an analytic Lipschitz/telescoping bound for the full ten-edge contraction.

This gate does not claim Haar divergence, absolute/conditional integrability, a spectral pairing theorem, D7-S2 closure, or a terminal D7 label.

## Frozen physical scope
Reuse Iter505/504 without changing the physical object:
- panels `T0,T1,T2`;
- causal classes `0to5,1to4,2to3`;
- rho `7,8`;
- j=1 source coefficients `B_m=C_m^(src)/8`;
- all ten K5 edges;
- all 243 intertwiner channels;
- fixed-causal no-branch-sum contraction;
- witness threshold `1e-12`;
- finite-t control values `t_coarse=1.25e-4`, `t_fine=6.25e-5` and unchanged `5e-3` fine source-regression criterion.

## Frozen neighborhood family
Anchor node 0 is fixed. Each of nodes 1..4 may move independently in R^3 by Euclidean norm at most eta. Freeze the candidate radii before production:
`eta in {1e-12, 1e-10, 1e-8, 1e-6}`.
No post-hoc radius insertion or refinement is allowed.

For an edge with center separation `w`, radius `r=|w|`, endpoint perturbations imply `|delta w| <= 2 eta`. A radius is admissible only when `2 eta < r` on every edge.

## Analytic edge bound
For j=1, write the rotated magnetic coefficient matrix as
`M(n)=a I + b J_n + c J_n^2`, where `a=B_0`, `b=(B_1-B_-1)/2`, `c=(B_1+B_-1)/2-B_0`, and `||J_n||_2=1`, `||J_n-J_n'||_F <= sqrt(2)||n-n'||`.
For `d=2 eta` and `r_-=r-d`, use the deterministic normalization bound
`||n'-n|| <= 2 d / r_-`.
The evaluator must bound each edge variation by the sum of the radial `r^-3` change and the representation-theoretic directional variation. No sampled angular dominance may substitute for this bound.

For a fixed center channel I, the closed tensor-network contraction obeys the Hilbert-Schmidt product bound. The ten-edge perturbation is therefore bounded by a telescoping product using the Frobenius norms of the five frozen intertwiner tensors and the center edge matrices plus their certified edge variations.

For each lane choose the center channel with maximal normalized witness *before* evaluating any eta. A radius is certified only if
`abs(F_I(center)) - certified_variation_bound > 0`.
Channel crossings elsewhere are irrelevant because the certificate follows one already nonzero continuous channel; no unique max-channel assumption is made.

## Required controls
- full Iter505 lane controls must remain valid;
- all center contraction values and norms finite;
- all ten edge radii positive and every frozen eta geometrically admissible;
- analytic coefficient decomposition finite;
- network tensor Frobenius prefactor finite/positive;
- certified variation bound finite/nonnegative;
- center witness channel fixed before eta scan;
- no sampled point may be used to shrink a bound or choose a radius.

## Frozen classifications
`ITER506_UNIFORM_FULL_K5_NEIGHBORHOOD_CERTIFIED_SCOPED` iff all 18 lanes are valid and every lane certifies at least the smallest frozen eta with a strictly positive lower margin.

`SCIENTIFIC_FAIL_ITER506_NO_CERTIFIED_OPEN_NEIGHBORHOOD_AT_FROZEN_RADII` iff all source/mathematical controls are valid but at least one lane has no positive certified margin even at eta=1e-12.

`BLOCKED_OR_INFRASTRUCTURE_ITER506` iff an upstream Iter505 control or analytic-bound validity/control fails.

The aggregate must report the minimum certified radius across lanes, the minimum positive margin at that common radius, and the count of lanes certified at every frozen radius.

## Claim locks
Even a PASS proves only a scoped explicit open coordinate neighborhood of nonzero fixed-causal full-K5 leading contraction around the frozen panels. It does not by itself prove Haar divergence/convergence, spectral admissibility, physical-vertex finiteness, D7-S2 closure, or any terminal classifier. D7-S2/S3/S4 remain open. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain forbidden. Candidate Gravity remains inactive.

## Post-gate decision
After PASS, the next collision step may combine this explicit open-neighborhood leading witness with a separately preregistered uniform finite-t remainder/blow-up domination test before any positive-measure/Haar claim. After scientific FAIL, do not enlarge or insert radii post hoc; inspect whether the conservative analytic bound is too coarse and preregister a stronger dependency-preserving bound if justified. After BLOCKED, repair only the first causal mathematical/infrastructure defect.