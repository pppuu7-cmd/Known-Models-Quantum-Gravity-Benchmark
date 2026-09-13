# Current Benchmark Front
Updated: 2026-09-14

## Authoritative frontier
Mainline has advanced through terminal Iter483. Iter461 remains independently queued on its research branch and must not be duplicated. Iter481 established that the full two-index local angular magnetic matrices plus genuine five-node four-valent SU(2) intertwiners do not force universal leading cancellation on frozen j=1 controls. Iter482 imposed the stronger compact common-node constraint: all ten K5 edge rotations were generated from only five shared SU(2) node rotations with exact triangle-cycle and common-left-gauge consistency, with all frozen lanes remaining nonzero. Iter483 now qualifies the next noncompact prerequisite: five shared SL(2,C) node elements generate all ten relative edge elements with determinant-one, exact K5 cycle consistency, common-left-gauge invariance, numerically stable positive-polar reconstruction, finite nonnegative edge rapidities, inversion consistency and deliberately corrupted controls. This does not identify the source Toller/KAK factors. Therefore the current D7-S2 frontier is source-faithful Toller/KAK mapping on these qualified common-node noncompact elements, followed only then by the boost-dependent Toller network, shared Haar/group integration, ten spectral integrations and collision/boundary-value admissibility.

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census = 15 families.
- D1 = PASS.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3 = PARTIAL.
- D4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D5 = PASS.
- D6 = PASS_RULE_TARGETS_OPEN.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- D7-S0 = PASS; D7-S1 = PASS; D7-S2 = NOT_CLOSED; D7-S3 = NOT_CLOSED; D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED; D7-S5 = NOT_AUTHORIZED; D7-S6 = INACTIVE.
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain forbidden while S2-S4 remain open.
- Candidate Gravity remains inactive.

## Latest consumed D7-S2 chain
- Iter468 run `34770144171`, aggregate artifact `10322025879`: explicit source Eq.(3)->Eq.(4) spectral/group contraction object pinned scoped.
- Iter479 run `34772768304`, artifact `10322656348`: source Toller leading magnetic matrix full-rank qualified scoped.
- Iter480B authoritative retry run `34773320961`, aggregate artifact `10323081045`: source-compatible boundary-intertwiner contractions retain nonzero leading witnesses.
- Iter481 authoritative retry run `34775946391`, aggregate job `103774033555`, aggregate artifact `10323930725`, digest `sha256:25cae4be01215585362481ae6296729bfb0769093d8a8ac17d0913778a191475`: `ITER481_SOURCE_ANGULAR_INTERTWINER_NETWORK_NONZERO_WITNESS_SCOPED`; 12/12 raw lanes pass, every lane `243/243` nonzero.
- Iter482 prereg `c23770098211125f25fb29d57c02db579febf2bf`, implementation `db87a3144b92aca8e0b1fce125c8ce20bc81ece7`, production head `07ff8d9b6d15279b73296b26767d0af260bf33a0`; run `34779214066`; aggregate job `103783117185`; aggregate artifact `10324334345`; digest `sha256:e80292603e898b730b7d7dce01e4bf239138b7637edf20a480e97891be233f81`: `ITER482_COMMON_NODE_SU2_CORRELATED_NETWORK_NONZERO_WITNESS_SCOPED`. All 18 raw artifacts consumed; all lanes pass all frozen controls and retain `243/243` nonzero witnesses.
- Iter483 prereg `a745b14adc9e554e77c51eb5572fb34879990747`, implementation `9a2eb176f87124f0f87481b25f03202da522d89f`, workflow `cc1ffe237953728aa61d953c0a928cac3efaa09e`, authoritative serialization-only repair head `9eb185779ab316591bb6383923182c0b4472883d`; run `34782171609`; aggregate job `103791079718`; aggregate artifact `10325219145`; digest `sha256:4839a846ae235b3d5992e20739a94f35ed1d785e141a44c9432b1149483ed2b0`: `ITER483_COMMON_NODE_SL2C_POLAR_GEOMETRY_QUALIFIED_SCOPED`. All 8 raw artifacts consumed and all 8 frozen lanes pass. The aggregate scope is explicitly common-node SL2C kinematic/polar qualification only; no source Toller KAK identification, Haar/spectral or full-vertex claim.

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Status rechecked 2026-09-14: queued.
- Do not duplicate. A terminal PASS is collision-geometry evidence only and cannot close D7-S2 by itself.

## Current blockers
### D7-S2
The source spectral/group contraction object, one-wedge coefficients/rank, boundary intertwiners, held-out local angular mixing, compact common-node correlation and common-node noncompact SL2C kinematic/polar geometry are qualified on frozen scopes. Remaining blockers are source/global: (i) source-faithful Toller/KAK mapping and branch/order convention for all ten edges from five node variables; (ii) source-faithful boost-dependent Toller magnetic kernel; (iii) shared Haar/group integration and its convergence/distributional interpretation; (iv) coupling to ten spectral integrations and K5 collision geometry. No independent-edge surrogate, shared spectral-variable fiction, fitted cancellation, replacement of source KAK by polar factors, or post-hoc contour modification is allowed.

### D7-S3 / D7-S4
Remain open/partial. Existing negative and blocked transport/closure evidence must be preserved; do not invent missing closure maps.

## Exact next permitted decisions
1. Consume Iter461 immediately if/when terminal.
2. Prospectively pin the source-defined one-edge Toller/KAK convention on the already qualified common-node SL2C panels, including reconstruction, ordering, inversion/reversal, branch/degeneracy handling and negative controls against naive polar substitution.
3. Only after that source mapping qualifies may a ten-edge boost-dependent Toller network or controlled Haar/quadrature gate be opened.
4. Keep absolute convergence, conditional/PV finite parts and source-defined distributional amplitudes distinct.
5. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 59%, integrated path 70%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. Relative to the Iter482 frontier, +1 pp D7 and +1 pp integrated are credited to terminal Iter483 because it materially closes the common-node noncompact kinematic/polar prerequisite. No D7-S2 closure is claimed.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No universal causal-EPRL/contour no-go theorem. No terminal D7 label. No fitted completion or modified published spectral i-epsilon. No identification of source Toller/KAK factors with the qualified polar factors. Candidate Gravity remains inactive.
