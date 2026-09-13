# Iter485 preregistration — shared-node ten-edge Toller magnetic network

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION
Parent authorities: terminal Iter482 boundary-intertwiner/common-node SU(2) network, terminal Iter483 shared-node SL(2,C) geometry, terminal Iter484 source-faithful one-edge Toller/KAK reconstruction.
Source locks: `sources/arxiv_2601_23162v1_causal_vertex.json`, `sources/arxiv_2604_24945v1_toller_cartan.json`.

## Scientific question
When all ten K5 edge elements are generated from the same five qualified SL(2,C) node variables, do the source-defined boost-dependent Toller magnetic matrices, with causal branch signs assigned from the five-node sigma pattern and genuine four-valent j=1 boundary intertwiners, form a finite convention-consistent ten-edge magnetic contraction object on the frozen witness panels? Does this correlated object retain nonzero contraction witnesses, or does the source branch/network structure force a universal cancellation on this scoped sector?

This gate qualifies only the pre-Haar magnetic network object. It does not integrate shared group variables or spectral variables.

## Frozen realization
- j=k=l=1, magnetic order (-1,0,+1), exactly as Iter484.
- Five shared SL(2,C) nodes and ten relative edges use `code/iter483_common_node_sl2c_polar.py` unchanged.
- Each edge is decomposed with the Iter484 source-faithful KAK convention and full magnetic matrices.
- rho witnesses per lane: [0.35, 0.9, 1.6, 2.7], unchanged from Iter484.
- Genuine five-node four-valent j=1 intertwiners and all 3^5=243 recoupling channels use the already-qualified Iter482 tensor construction unchanged.
- Source causal patterns are the three frozen five-node sign classes already used in the benchmark: `0to5=(+,+,+,+,+)`, `1to4=(-,+,+,+,+)`, `2to3=(-,-,+,+,+)`. For edge (a,b), use T+ when sigma_a sigma_b > 0 and T- when sigma_a sigma_b < 0.
- Frozen independent lanes: panel in {A,B,C,D} x regime in {mild,strong} x causal in {0to5,1to4,2to3}: 24 lanes, `fail-fast:false`. Each lane evaluates all four rho witnesses.

## Frozen predicates
A lane is valid only if all source evaluations are finite and all ten edge rapidities are finite.

1. **Shared-node geometry control**: ten relative edge elements reconstruct from one common five-node set and K5 triangle-cycle residual is <1e-10.
2. **Per-edge Iter484 inheritance**: every one of the ten KAK reconstructions has max residual <1e-10 and SU(2) factors have unitarity/determinant-one residuals <1e-10.
3. **Per-edge source additive control**: for every edge and rho, full matrices obey ||T+ + T- - D||_max <=1e-11.
4. **Causal-branch determinism**: branch choice is exactly the frozen sigma_a sigma_b rule; counts must equal 10/0 for 0to5, 6/4 for 1to4, and 4/6 for 2to3 (same-sign/opposite-sign edges).
5. **Intertwiner controls**: the frozen Iter482 j=1 tensors retain magnetic support and Gram residual <1e-12.
6. **Finite normalized contraction**: all 243 contractions are finite for every rho. Normalize each rho by the product of the ten max matrix norms; the scale must be finite and >0.
7. **Nonzero-witness test**: for every rho there must be at least one recoupling channel with normalized magnitude >1e-14. If valid but this fails, classify scientific cancellation on the frozen sector; do not weaken threshold.
8. **Magnetic-basis reindex covariance**: simultaneous reversal of every magnetic index in all edge matrices and intertwiners preserves the sorted contraction-magnitude spectrum with relative residual <1e-10.
9. **Zero-edge negative control**: replacing one frozen edge matrix by zero makes all 243 contractions exactly/numerically zero, max normalized magnitude <1e-14.
10. **Independent-edge surrogate negative control**: replace geometric edge (0,1) by an independently generated nontrivial relative element while keeping the other nine fixed; underlying K5 triangle-cycle residual must exceed 1e-5. This control is geometric only and must not be interpreted as a Toller composition law.
11. **False Toller-composition negative control**: in every lane at least one rho must retain the Iter484 nonrepresentation mismatch >1e-5 for a frozen two-edge product. No group-representation property of T is assumed.

## PASS / FAIL / BLOCKED contract
PASS iff all 24 lanes are valid and predicates 1–11 pass:
`ITER485_SHARED_NODE_TEN_EDGE_TOLLER_MAGNETIC_NETWORK_QUALIFIED_SCOPED`.

A valid lane that violates a positive predicate, fails a frozen negative control, or has no nonzero witness is:
`SCIENTIFIC_FAIL_ITER485_TEN_EDGE_TOLLER_NETWORK`.

Import/runtime/source-lock failure before a meaningful frozen verdict is:
`BLOCKED_OR_INFRASTRUCTURE_ITER485`.

Thresholds, panels, rho witnesses, causal patterns and interpretation rule may not be changed after production output is seen.

## Interpretation ceiling
PASS qualifies only this finite j=1, pre-Haar, pre-spectral ten-edge magnetic contraction object. It does not prove arbitrary-spin behavior, Haar/group convergence, spectral convergence, boundary-value admissibility, a finite physical causal vertex, D7-S2 closure, any terminal D7 classifier, or Candidate Gravity authorization. A FAIL is likewise scoped and is not a no-go theorem for the full model.

## Next if PASS
Only after terminal classification and durable recording may a prospectively frozen shared Haar/group-integration or controlled quadrature gate be opened, keeping absolute convergence, conditional/PV behavior and distributional interpretation distinct.