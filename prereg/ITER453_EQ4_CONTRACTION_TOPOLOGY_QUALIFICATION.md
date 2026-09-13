# Iter453 preregistration — Eq.(4) coupled magnetic/intertwiner contraction topology qualification

Prospective freeze date: 2026-09-13.

This document is committed before implementation/production results are observed.

## Source lock
Immutable source object: `sources/arxiv_2601_23162v1_causal_vertex.json`, source id `arXiv:2601.23162v1`, source SHA-256 `a78e72b972a288357b03138d9795299730d3069a4859fe4020a54d2c06607cb0`, qualified by terminal Iter452.

## Scientific target
Validate the executable **index/contraction topology** implied by Eq.(4) and the boundary-state contraction before attempting a direct causal-vertex convergence/finiteness calculation. This is an algebraic/computational qualification gate, not an amplitude-finiteness gate.

For K5 vertices `a=0..4`, use the ten unordered wedges `(a,b), a<b`, with one magnetic half-edge index at each endpoint. Five rank-4 boundary intertwiner tensors contract the four half-edge indices incident on each vertex. Each wedge contributes a two-index branch tensor `T^+_{m_ba,m_ab}` or `T^-_{m_ba,m_ab}`. Define `D=T^+ + T^-` wedgewise exactly as Eq.(5).

## Frozen deterministic panel
Four independent lanes, `seed in {17,29,43,71}`, each with:
- magnetic dimension `d=2`;
- deterministic complex branch tensors for all ten wedges;
- deterministic complex rank-4 intertwiner tensors for all five vertices;
- tensors normalized to finite Frobenius norm but otherwise unconstrained; no fitted coefficients;
- one fixed canonical K5 edge ordering and one independently generated nontrivial S5 vertex permutation per lane.

## Frozen checks per lane
1. `scalar_contraction_valid`: direct full network contraction returns one finite complex scalar and every one of the 20 half-edge magnetic indices occurs exactly twice (one wedge, one intertwiner).
2. `eq5_local_exact`: for every wedge, stored `D` equals `T+ + T-` to max absolute residual `<=1e-13`.
3. `eq6_full_branch_sum`: explicit sum of all `2^10=1024` independent wedge-branch contractions equals the single all-`D` contraction, relative residual `<=5e-11` and absolute residual `<=5e-11*(1+|A_D|)`.
4. `permutation_covariance`: simultaneous relabeling of vertices, wedge tensors and intertwiner legs gives the same scalar, relative residual `<=5e-11`.
5. `intertwiner_leg_order_invariance`: canonical reordering of the four legs at each vertex together with the corresponding tensor-axis permutation leaves the scalar unchanged, relative residual `<=5e-11`.
6. `negative_incidence_control`: deliberately break exactly one wedge-to-vertex incidence mapping without applying the compensating intertwiner-axis relabeling; the scalar must differ from the valid scalar by relative amount `>=1e-6` for the frozen deterministic panel.
7. `negative_eq5_control`: perturb one wedge `D` tensor by frozen complex offset `1e-3*(1+0.5i)`; the all-D contraction must then fail the Eq.(6) branch-sum equality by relative amount `>=1e-8`.
8. `precision_repeatability`: recompute the network in two independently assembled contraction orders; relative discrepancy `<=5e-11`.

## Aggregate frozen rule
PASS label only if all four lanes are structurally valid and all eight checks pass in every lane:
`ITER453_EQ4_MAGNETIC_INTERTWINER_CONTRACTION_TOPOLOGY_QUALIFIED`.

Any genuine frozen-predicate miss is scientific/computational qualification FAIL and must not be weakened post hoc. An exception/import/runner failure before predicates are evaluated is infrastructure/implementation failure and may receive only minimal repair without changing this preregistration.

## Interpretation lock
PASS establishes only that the Eq.(4)/boundary magnetic-index wiring and Eq.(5)/(6) additive-control algebra are implemented consistently on the frozen finite deterministic panel. It does **not** establish that the deterministic tensors are physical Toller matrix elements, nor convergence/absolute integrability/finite normalization of the noncompact group/spectral integrals, nor D7-S2 closure, nor a family-level classifier result.

After PASS, the next allowed dependent gate is a separately preregistered source-faithful finite-`i epsilon` Toller-matrix insertion/convergence pilot using actual Eq.(3)/(7) objects. After FAIL, diagnose the first causal implementation or topology defect without weakening frozen criteria.
