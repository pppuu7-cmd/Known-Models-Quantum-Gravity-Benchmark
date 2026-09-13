# Current Benchmark Front
Updated: 2026-09-13

## Authoritative frontier
Mainline has advanced through Iter479 and terminal Iter480B. Iter461 remains independently queued on its research branch and must not be duplicated. Iter479 proved that the source Eq.(7) one-wedge leading magnetic matrix is full rank on the frozen panels. Iter480B then inserted genuine source-compatible four-valent SU(2) boundary-intertwiner contractions and found nonzero leading-coefficient witnesses in every frozen gamma/causal panel. Therefore universal leading cancellation is not produced solely by the five boundary intertwiner contractions in the minimal equal-spin j=1 diagonal-collision control. Remaining D7-S2 cancellation/validity questions must involve structure absent from that gate: angular U1/U2 dependence tied to group elements, shared group/Haar integration, non-diagonal magnetic mixing, spectral integration, Jacobians, and/or full K5 collision geometry.

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
- Iter479 prereg `19d8d6d88ee542e43f721dadc7e9bee3900e1944`, implementation `ad29c9cd2c8460fe86ef7c5b59090b1265dbc2d5`, workflow run `34772768304`, job `103765265032`, artifact `10322656348`, digest `sha256:849ecf0db0438e36904664016fcdcf1589f621c2186658648de56d8f84e46f91`: `ITER479_SOURCE_TOLLER_LEADING_MAGNETIC_MATRIX_FULL_RANK_QUALIFIED_SCOPED`. The individual one-wedge leading Eq.(7) magnetic matrix is full rank on all frozen panels; cancellation cannot occur solely inside the one-wedge magnetic reconstruction.
- Iter480 initial prereg `9e1eb674e4c05e1cb3dcea1d01104d29e7cf29fa` was invalidated transparently before implementation/production because its nonzero threshold contained an inappropriate absolute `max(1,...)` scale floor. It has no scientific classification.
- Iter480B prereg `da49c5b97494992e62045355579645698da91821`; initial run `34773180686` was a NONAUTHORITATIVE numerical/control-evaluator failure only. The frozen science was unchanged. Minimal evaluator repair head `fb7395328f2e1c12a8a49fc6b89b150de92cd4f1`; authoritative retry run `34773320961`, aggregate job `103766837720`, artifact `10323081045`, digest `sha256:ef44f8a32e7641f86bcef01376eb6e7a10b26584c6ffb0ff1c23c1e45de9e3aa`: `ITER480B_SOURCE_INTERTWINER_CONTRACTION_NONZERO_WITNESS_SCOPED`. All 6 gamma/causal lanes pass. Every panel has `130/243` nonzero recoupling-channel witnesses; `R_max=0.0046296296296296285`; reindex controls are `0` to `2.10e-89`; zero-vector controls vanish exactly.

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Status at this update: queued.
- Do not duplicate. A terminal PASS is collision-geometry evidence only and cannot close D7-S2 by itself.

## Current blockers
### D7-S2
The source object, one-wedge leading coefficients, one-wedge magnetic rank and minimal source-backed boundary-intertwiner contraction are now explicit/qualified on their frozen scopes. The remaining blocker is genuinely correlated: whether the leading source object survives or cancels once the actual angular matrices and common SL(2,C) group variables/Haar integrations are restored, and whether the resulting ten-variable boundary value is mathematically admissible. No shared spectral variable, fitted cancellation, or independent-wedge surrogate may be introduced.

### D7-S3 / D7-S4
Remain open/partial. Existing negative and blocked transport/closure evidence must be preserved; do not invent missing closure maps.

## Exact next permitted decisions
1. Consume Iter461 immediately if/when terminal.
2. Prospectively test the already-qualified Iter479 source Eq.(7) angular magnetic mixing together with the qualified Iter480B boundary-intertwiner contraction, initially as an explicitly scoped angular/intertwiner diagnostic.
3. After that, restore common group-variable dependence before any claim about full causal-vertex cancellation or D7-S2 closure.
4. Keep absolute convergence, conditional/PV finite parts, and source-defined distributional amplitudes distinct.
5. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 56%, integrated path 67%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. Iter480B gets no percentage increase: it materially narrows a source-backed cancellation mechanism but does not close a frozen D7 prerequisite. The lower 56/67 frontier supersedes the stale pre-Iter479 62/73 entry because the later source-specific chain exposed additional mandatory magnetic/boundary/group-contraction work.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No universal causal-EPRL/contour no-go theorem. No terminal D7 label. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
