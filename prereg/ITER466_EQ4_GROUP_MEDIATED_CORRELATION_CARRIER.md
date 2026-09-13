# Iter466 — Eq.(4) group-mediated spectral-correlation carrier pin

Date: 2026-09-13
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION

## Purpose
Pin, from the already immutable `arXiv:2601.23162v1` Eq.(3)/(4) source snapshot only, the exact correlation carrier that a later D7-S2 multivariable distributional gate is allowed to use. This gate exists because the source gives one Toller spectral integral per wedge, while Eq.(4) couples wedge factors through shared group integrations. It must not manufacture a shared spectral variable that the source does not contain.

## Frozen source
- `sources/arxiv_2601_23162v1_causal_vertex.json`
- source id: `arXiv:2601.23162v1`
- frozen source digest already qualified by Iter452: `a78e72b972a288357b03138d9795299730d3069a4859fe4020a54d2c06607cb0`
- inherited qualified structures: Iter453 Eq.(4)/(5)/(6) contraction topology and Iter457 Eq.(7) magnetic reconstruction.

## Frozen exact object
For vertices `V={1,2,3,4,5}` and wedges `E={(a,b):1<=a<b<=5}`:
1. There are exactly 10 wedge factors and therefore 10 wedge-local Eq.(3) spectral integration labels `tilde_rho_ab`; before group integration these labels are distinct.
2. Eq.(4) integrates four independent group variables after gauge fixing one node (`g_r=1`); each wedge factor depends on its endpoint group variables through `g_b^{-1} g_a`.
3. The reduced oriented incidence matrix `B_r` of K5 (delete the gauge-root row) has shape 4x10, exact rank 4, and kernel dimension 6.
4. The six-dimensional kernel is the graph cycle space that carries group-mediated correlations among wedge factors. This is a topology/correlation-carrier statement only; it is not yet a distributional pushforward or spectral-collision theorem.
5. The exact rank/kernel dimension must be invariant for all five possible gauge roots and under deterministic vertex relabelings.

## Frozen predicates
A. Source consistency: wedge_count=10, group integrations=4, gauge fix present, Eq.(3) real spectral integral present.
B. Spectral-label locality: construct ten unique labels `tilde_rho_ab`; duplicate-label count must be zero. A deliberately duplicated-label negative control must be detected.
C. Reduced K5 incidence: for every gauge root r=1..5, `rank(B_r)=4`, `nullity(B_r)=6` exactly over rationals/integers.
D. Endpoint incidence: every wedge has exactly two graph endpoints before gauge-row deletion; after deletion, root-incident wedges have one retained endpoint and all others two.
E. Relabeling robustness: a frozen deterministic set of S5 permutations preserves wedge count, rank, nullity, and cycle-space dimension.
F. Broken-topology controls: deleting one K5 edge must change edge count to 9 and cycle dimension to 5 while retaining rank 4; duplicating one edge must be detected as a non-simple source topology.

## Frozen interpretation
PASS classification: `ITER466_EQ4_GROUP_MEDIATED_SPECTRAL_CORRELATION_CARRIER_PINNED_SCOPED`.

A PASS permits only the statement that the source-faithful next D7-S2 object must be a group-mediated correlated contraction/pushforward built from the ten wedge-local spectral factors and the K5 group-incidence/cycle structure. It does NOT prove a shared spectral pole, non-transversality, convergence, finiteness, divergence, a distributional limit, D7-S2 closure, terminal D7, or any family-level classifier.

FAIL means the proposed K5/group-mediated correlation-carrier reading is inconsistent with the frozen source snapshot or exact controls and must not be used.

Infrastructure/numerical errors are not scientific FAIL.

## Claim locks
D7-S2/S3/S4 remain open. D7 terminal classifier and `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` remain unauthorized. Candidate Gravity remains inactive. No modified i-epsilon, fitted cancellation, or post-hoc threshold/model changes are allowed.
