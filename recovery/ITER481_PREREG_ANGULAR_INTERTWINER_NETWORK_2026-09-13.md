# Iter481 preregistration — Eq.(7) angular magnetic matrices contracted with four-valent intertwiners

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent authority: terminal Iter479 + terminal Iter480B.

## Scientific question
After removing the Iter480B diagonal-collision simplification and restoring the full two-index source Eq.(7) leading magnetic matrix `L_e = U1_e diag(C_m) U2_e` on every K5 edge, do genuine four-valent SU(2) boundary-intertwiner contractions still admit nonzero leading-coefficient witnesses on held-out angular panels, or does angular magnetic mixing force universal cancellation?

## Source/convention lock
- Reuse exactly the j=1 Wigner `U` convention and the four frozen Euler-angle pairs already qualified in Iter479; do not introduce a new Wigner convention.
- Reuse the source-compatible four-valent Eq.(90) recoupling tensors qualified in Iter480B.
- This gate treats the per-edge angular pairs as held-out local Eq.(7) controls. It does **not** claim they arise from one common set of five SL(2,C) group variables. Common-group compatibility is a later mandatory gate.

## Frozen model
- K5, 10 edges, all face spins j=1.
- gamma in {7,8}.
- causal representatives: `0to5` sigma=(+,+,+,+,+), `1to4`=(-,+,+,+,+), `2to3`=(-,-,+,+,+), with branch kappa_ab=sigma_a sigma_b.
- Five four-valent boundary intertwiners, recoupling channel i in {0,1,2}; exhaust all 3^5=243 channel assignments.
- Every edge carries a full 3x3 leading magnetic matrix from Iter479's `U1 diag(C) U2` construction.
- Two prospectively frozen angular-pattern maps over the ten lexicographically ordered edges:
  - P0: Iter479 lane index `edge_index mod 4`.
  - P1: Iter479 lane index `(2*edge_index + 1) mod 4`.
- Total production panel: 2 gamma x 3 causal representatives x 2 angular patterns = 12 independent lanes, `fail-fast:false`.

## Dimensionless normalization
For each panel, define `S = product_e max_m |C_e(m)|`. Since all `U` matrices are unitary under the qualified convention, this is also the product of edge operator-norm leading scales. Require S finite and positive. For contraction A define `R=|A|/S`.
Frozen nonzero threshold: `R > 1e-12`.

## Frozen checks
A. Reconstruct all Eq.(90) j=1 intertwiners and require support/norm/orthogonality residual <1e-12.
B. Reconstruct every Iter479 Wigner matrix used in the lane and require unitarity residual <1e-12.
C. Evaluate the full two-index K5 tensor network for all 243 intertwiner-channel assignments. Require at least one finite `R>1e-12` witness in every frozen gamma x causal x angular-pattern lane. Individual channels may vanish.
D. Identity-angle regression: in every gamma x causal lane, replacing all U matrices by identity must reproduce the Iter480B diagonal-network support count `130/243` and `R_max=0.0046296296296296285` within relative 1e-10.
E. Pure basis-reindex control: simultaneously reverse every magnetic basis index on both indices of every edge matrix and every incident intertwiner tensor axis. The sorted multiset of 243 contraction magnitudes must agree at multiset-relative residual <1e-10.
F. Negative control: replace all ten edge matrices by zero matrices; all 243 contractions must have |A|<1e-14.
G. Report nonzero support count, R_max, maximizing channel tuple, Wigner unitarity maximum, regression residual and basis-reindex residual for every lane.

## PASS rule
PASS iff A-F pass in all 12 lanes. PASS label:
`ITER481_SOURCE_ANGULAR_INTERTWINER_NETWORK_NONZERO_WITNESS_SCOPED`.

A valid-control failure of C is a SCIENTIFIC FAIL for this frozen angular/intertwiner diagnostic. Dependency/runtime/control failure is infrastructure/numerical, not scientific evidence.

## Scope guards
PASS only excludes universal cancellation caused by local Eq.(7) angular magnetic mixing plus the five source-compatible four-valent boundary intertwiners on these held-out j=1 panels. It does not establish compatibility with a common set of SL(2,C) group variables; does not perform Haar/group integration, spectral integration, Jacobian analysis or full collision-stratum analysis; does not prove causal-vertex divergence/finiteness; does not close D7-S2/S3/S4; does not authorize terminal D7 labels or Candidate Gravity.
