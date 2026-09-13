# Current Benchmark Front
Updated: 2026-09-14

## Authoritative frontier
Mainline has advanced through terminal Iter486. Iter461 remains independently queued on its research branch and must not be duplicated. Iter481 established that the full two-index local angular magnetic matrices plus genuine five-node four-valent SU(2) intertwiners do not force universal leading cancellation on frozen j=1 controls. Iter482 imposed the stronger compact common-node constraint. Iter483 qualified five-shared-node noncompact `SL(2,C)` geometry. Iter484 qualified the source-defined one-edge Toller/KAK lift while rejecting naive polar substitution and false Toller composition. Iter485 qualified the correlated ten-edge boost-dependent Toller magnetic network. Iter486 then tested that full network against the source radial Haar density along prospectively frozen shared-node escape profiles. All 24 raw lanes were produced, but all `s=2,3,4` lanes failed a frozen absolute nonrepresentation negative-control threshold because that absolute mismatch scales to zero with the escaping amplitudes. Therefore Iter486 is terminal `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486`: its raw slope pattern is diagnostic only and no Haar science label is promoted. The next permitted gate is a new prospective repeat of the same Haar science object with a dimensionless scale-normalized nonrepresentation control; the Haar object and science thresholds themselves must remain unchanged.

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
- Iter481 run `34775946391`, aggregate artifact `10323930725`, digest `sha256:25cae4be01215585362481ae6296729bfb0769093d8a8ac17d0913778a191475`: `ITER481_SOURCE_ANGULAR_INTERTWINER_NETWORK_NONZERO_WITNESS_SCOPED`.
- Iter482 run `34779214066`, aggregate artifact `10324334345`, digest `sha256:e80292603e898b730b7d7dce01e4bf239138b7637edf20a480e97891be233f81`: `ITER482_COMMON_NODE_SU2_CORRELATED_NETWORK_NONZERO_WITNESS_SCOPED`.
- Iter483 run `34782171609`, aggregate artifact `10325219145`, digest `sha256:4839a846ae235b3d5992e20739a94f35ed1d785e141a44c9432b1149483ed2b0`: `ITER483_COMMON_NODE_SL2C_POLAR_GEOMETRY_QUALIFIED_SCOPED`.
- Iter484 run `34787734912`, aggregate artifact `10326933008`, digest `sha256:1146847e79c50be7bf2c9213238990d877ba8c598f0d38dfc217385a0359aa1e`: `ITER484_SOURCE_TOLLER_KAK_ONE_EDGE_RECONSTRUCTION_QUALIFIED_SCOPED`.
- Iter485 prereg `1defff606f223a3fd91de970504686b5e2fa8318`, implementation `7b46b675d06bfaf6d4c28722bbff7bd9698049f7`, aggregate classifier `d5375c5c18fb3cd2f1a1021eea22714cb3f1f4ca`, workflow `507d339b6627a2e334a1bbee8916abd02a444718`, wording-only retry head `129a7587a6ba4074744b92c1e224c235e7edb018`; run `34788248941`; aggregate artifact `10327143297`; digest `sha256:4a4636eee315348a67b1a55fdec3aae6a5a500cd44971d8334970bceeb9c112f`: `ITER485_SHARED_NODE_TEN_EDGE_TOLLER_MAGNETIC_NETWORK_QUALIFIED_SCOPED`. All 24/24 expected lanes are present, valid and PASS.
- Iter486 source pin `2cbfa37aea635bd76e1fb0291191b6efb32699cc`, prereg `4e1098865dfdec5d4eebacb2d055c17a0a6f2b2c`, implementation `f3e8bfcbabddf5c2262eb2a98a04e76343aff3fe`, aggregate `4774e98c5dfa7ed1f7f6cdefd2e101c7aed99266`, workflow `1cc85b617c936917155af0fb36a4f529dc6a8ba5`, dependency-only retry head `3898fea010098b1ce3268669c72a0f9af2f01cc4`; authoritative run `34789259423`; source-lock job `103810316891`; aggregate job `103810617969`; summary artifact `10327790459`; digest `sha256:6c7269bac6124e1736d07ca5d642a552e4fcda0a34ff7528363dbd0a18dc7892`: `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486`. All 24 raw lanes are present, but 18 `s=2,3,4` lanes are invalid due the frozen scale-nonuniform absolute nonrepresentation control. Six `s=1` lanes are valid DECAY lanes. Raw non-promoted diagnostics contain 29 NONDECAY and 19 inconclusive points, with raw actual-envelope slopes ranging from about `-2.00086` to `+4.00143`; these are not an Iter486 science verdict.

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Status rechecked 2026-09-14: queued.
- Do not duplicate. A terminal PASS is collision-geometry evidence only and cannot close D7-S2 by itself.

## Current blockers
### D7-S2
The source spectral/group contraction object, one-wedge coefficients/rank, boundary intertwiners, compact/common-node correlation, noncompact shared-node geometry, source one-edge Toller/KAK lift, and correlated ten-edge boost-dependent magnetic network are qualified on frozen scopes. The Haar escape object has been implemented, but Iter486 produced no promotable science verdict because a scale-nonuniform validation control invalidated the multi-node escape lanes. Remaining blockers are: (i) a valid full-network shared-Haar escape classification with scale-robust controls; (ii) if nondecay survives, positive-measure angular-neighborhood thickening before any absolute Haar-divergence claim; (iii) coupling to ten source spectral integrations; (iv) K5 collision geometry and correlated boundary-value admissibility. No independent-edge surrogate, shared spectral-variable fiction, fitted cancellation, replacement of source KAK by polar factors, false Toller composition law, artificial Haar-suppressing weight, or post-hoc contour modification is allowed.

### D7-S3 / D7-S4
Remain open/partial. Existing negative and blocked transport/closure evidence must be preserved; do not invent missing closure maps.

## Exact next permitted decisions
1. Consume Iter461 immediately if/when terminal.
2. Prospectively repeat the exact Iter486 Haar-escape scientific object and frozen DECAY/NONDECAY slope thresholds, changing only the invalid scale-dependent validation control: use a dimensionless relative Toller nonrepresentation mismatch at the escaped scale and retain an undeformed-base absolute nonrepresentation regression.
3. If a valid stable NONDECAY escape survives, the next gate must thicken that escape into a positive-measure angular neighborhood before any absolute Haar-divergence conclusion. A one-dimensional path alone is insufficient.
4. Keep absolute convergence, conditional/PV finite parts, source-defined distributional amplitudes, and ten spectral integrations distinct.
5. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 59%, integrated path 70%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. Iter486 authorizes no readiness increment because it has no promotable scientific classification. The formal D7-S2 state remains NOT_CLOSED.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No universal causal-EPRL/contour no-go theorem. No terminal D7 label. No fitted completion or modified published spectral i-epsilon. Naive identification of polar factors with source Toller/KAK factors remains rejected. Iter486 raw slope patterns are diagnostic only until a prospectively valid scale-normalized control gate is completed. Candidate Gravity remains inactive.
