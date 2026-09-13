# Current Benchmark Front
Updated: 2026-09-13

## Authoritative frontier
Mainline has advanced through terminal Iter481. Iter461 remains independently queued on its research branch and must not be duplicated. Iter479 qualified the source Eq.(7) one-wedge leading magnetic matrix as full rank on frozen panels; Iter480B showed genuine source-compatible four-valent SU(2) boundary-intertwiner contractions retain nonzero leading witnesses in the minimal diagonal control; Iter481 removed that diagonal/local-angular simplification and found nonzero witnesses in all 12 frozen full two-index angular/intertwiner lanes. Therefore universal leading cancellation is not produced solely by local Eq.(7) angular magnetic mixing plus the five boundary intertwiners on these j=1 controls. The next mandatory layer is common-node group compatibility: all ten edge matrices must be derived from one shared set of node group variables before any claim about full causal-vertex cancellation.

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
- Iter479 run `34772768304`, artifact `10322656348`: `ITER479_SOURCE_TOLLER_LEADING_MAGNETIC_MATRIX_FULL_RANK_QUALIFIED_SCOPED`.
- Iter480B authoritative retry run `34773320961`, aggregate artifact `10323081045`: `ITER480B_SOURCE_INTERTWINER_CONTRACTION_NONZERO_WITNESS_SCOPED`; all six panels contain `130/243` nonzero diagonal-control witnesses.
- Iter481 prereg `4609d55741e02db086dc42168d067ffb43dfe7f5`, implementation `11e358a2441aa1800b3ccbb5a923604d325ee242`. Initial run `34773608221` is NONAUTHORITATIVE infrastructure/output-serialization failure only; frozen science was unchanged. Minimal serialization-only repair / retry head `1d44bbf3c4fdd1a06e28beae498ebf0a680f927f`; authoritative retry run `34775946391`; aggregate job `103774033555`; aggregate artifact `10323930725`; digest `sha256:25cae4be01215585362481ae6296729bfb0769093d8a8ac17d0913778a191475`: `ITER481_SOURCE_ANGULAR_INTERTWINER_NETWORK_NONZERO_WITNESS_SCOPED`. All 12 raw lanes pass. Every lane has `243/243` nonzero witnesses; P0 `R_max≈1.07493e-4`, P1 `R_max≈4.07952e-4`; identity regression exactly reproduces Iter480B; Wigner/intertwiner/reindex/zero controls pass.

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Last known status: queued; recheck before any new batch.
- Do not duplicate. A terminal PASS is collision-geometry evidence only and cannot close D7-S2 by itself.

## Current blockers
### D7-S2
The source object, one-wedge coefficients/rank, boundary-intertwiner contractions and held-out local angular magnetic mixing are now explicit/qualified on their frozen scopes. The remaining cancellation blocker is genuinely common-group/global: whether the leading source object survives when all ten edge matrices are constrained by one common set of node `SL(2,C)` variables and then paired with the shared Haar/group integration, spectral integrations and collision geometry; separately, mathematical admissibility of the resulting ten-variable boundary value remains open. No shared spectral variable, fitted cancellation, arbitrary independent-edge angular surrogate or post-hoc contour change may be introduced.

### D7-S3 / D7-S4
Remain open/partial. Existing negative and blocked transport/closure evidence must be preserved; do not invent missing closure maps.

## Exact next permitted decisions
1. Consume Iter461 immediately if/when terminal.
2. Prospectively test common-node group compatibility before any further causal-vertex cancellation claim. First admissible control: a compact `SU(2)` node-group slice in which five node rotations generate all ten relative edge rotations, with exact cycle-consistency and gauge-covariance controls, then feed those source-compatible edge matrices through the already-qualified Iter481 intertwiner network.
3. If that compact common-group control passes, the next dependent gate must restore genuinely noncompact `SL(2,C)` boost/Haar structure; a compact-slice PASS cannot substitute for full Haar integration.
4. Keep absolute convergence, conditional/PV finite parts and source-defined distributional amplitudes distinct.
5. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 57%, integrated path 68%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. Relative to the preceding 56/67 frontier, +1 pp D7 and +1 pp integrated are credited to terminal Iter481 because it materially removes the independent local-angular plus boundary-intertwiner cancellation mechanism and narrows D7-S2 to common-group/Haar/spectral/collision validity. No D7-S2 closure is claimed.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No universal causal-EPRL/contour no-go theorem. No terminal D7 label. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
