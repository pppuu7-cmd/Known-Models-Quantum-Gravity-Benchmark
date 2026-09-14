# Current Benchmark Front
Updated: 2026-09-14

## Authoritative frontier
Mainline has advanced through terminal Iter492. Iter461 remains independently queued on its research branch and must not be duplicated.

The consumed D7-S2 chain now includes: source Eq.(3)->Eq.(4) contraction pinning (Iter468), source Toller leading magnetic rank (Iter479), boundary-intertwiner noncancellation (Iter480B), full local angular/intertwiner network (Iter481), compact common-node correlation (Iter482), shared-node noncompact SL(2,C) geometry (Iter483), source one-edge Toller/KAK lift (Iter484), correlated ten-edge Toller magnetic network (Iter485), a valid one-dimensional shared-Haar NONDECAY witness after Iter487/489 revalidation, a valid negative fixed-radius sampled angular-thickening result (Iter491), and now a prospectively frozen shrinking tangent-boundary-layer bracket (Iter492).

Iter492 authority: prereg `6288e7543f52f714e0887e4cf120f2dd19c4fc7d`, evaluator `35b2a7c44b4c3bc9b6742513ef9fa375d189e2e1`, aggregate implementation `94730270d8b2b900aff270de9e9f0812c902db91`, production/workflow head `65e01fc8bf3b3e090da000501802d27a8d4aaca8`; run `34794279921`; source-lock job `103824262832`; aggregate job `103824804978`; aggregate artifact `10328863006`; digest `sha256:1821129dbbad0b8f9e4f435235b4d4f2695dbc7326cf899d40b196a989e197c8`. Terminal classification: `ITER492_TANGENT_BOUNDARY_LAYER_BRACKET_QUALIFIED_SCOPED`.

All 15 Iter492 raw matrix artifacts were consumed. There are no missing/invalid jobs. On the frozen `eps_q(R)=0.02 exp(-qR)` matrix, q=0.50 and q=0.75 fail FULL_NONDECAY (21/24 lanes fail for each), while q=1.00, q=1.25 and q=1.50 pass FULL_NONDECAY and robustness in all 24/24 lanes. Thus the smallest prospectively frozen passing q is 1.00 and the finite-grid critical bracket is `(0.75, 1.00]`. This is not an open-neighborhood or positive-measure theorem.

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

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Last authoritative status: queued; do not duplicate.
- A terminal PASS is collision-geometry evidence only and cannot close D7-S2 by itself.

### Iter493 — critical q=1 local first/second angular variation
- Prereg: `c372ae3b662349203aa39501696ea57aceeb77b5`.
- Evaluator: `bfed21574f3d5ea80f2695009561c22dc5efefea`.
- Aggregate implementation: `7a1759bb3baafd7f585fdb1178230069bdeab129`.
- Workflow launch: `724b8c0b3dfa9613b1ee9598ef4b1d37da25ed20`.
- Source-lock-only text repair: `38f67256aae6b778ad748baa2135340ad0968c1b`; no frozen scientific panel, equation, amplitude, threshold, or interpretation rule changed.
- Matrix: 3 causal classes × 4 fixed blocks covering all 20 standard angular basis coordinates, `fail-fast:false`, `max-parallel:12`.
- Critical scaling only: q=1; symmetric kappa amplitudes 0.005 and 0.010; all four rho witnesses; inherited source/HP controls.
- Purpose: measure finite-grid first/second variation tensor of the actual radial slope at the critical boundary layer. Even a valid result is not an analytic/uniform certificate.

### Ten-source-spectral object audit
Iter468 remains the source authority for ten independent spectral variables and shared group kernel. Exact published normalization, ordering and i-epsilon prescription remain mandatory before any production ten-spectral gate. No shared-spectral-variable shortcut or fitted contour is authorized.

## Current blockers
### D7-S2
Iter492 narrows the angular-Haar question from an unknown shrinking neighborhood to a finite-grid critical boundary layer: frozen perturbations shrinking as exp(-R) survive, while exp(-0.75R) do not on the tested matrix. Remaining blockers are:
1. local response and then analytic/uniform control of the critical angular boundary layer; Iter493 is the next finite-grid prerequisite, not the final certificate;
2. exact coupling to ten independent/source-defined spectral integrations with published normalization, order and i-epsilon;
3. K5 collision geometry and correlated boundary-value admissibility (Iter461 stream);
4. separation of absolute convergence from conditional/PV/source-defined distributional amplitudes.

No independent-edge surrogate, shared spectral-variable fiction, fitted cancellation, replacement of source KAK by polar factors, false Toller composition, artificial Haar-suppressing weight, post-hoc q refinement to manufacture a threshold, or post-hoc contour modification is allowed.

### D7-S3 / D7-S4
Remain open/partial. Preserve existing negative and blocked transport/closure evidence; do not invent missing closure maps.

## Exact next permitted decisions
1. Consume Iter493 matrix/aggregate when terminal. If any failure occurs, identify the first causal failure and distinguish source/numerical/infrastructure failure from science before classification.
2. If Iter493 is valid, use its measured spanning-basis first/second response to design a new prospectively frozen analytic/validated-uniform neighborhood certificate; do not simply add q points.
3. Consume Iter461 immediately if terminal; never duplicate its authoritative queued run.
4. Continue exact ten-spectral source audit independently; keep Haar, spectral, PV/conditional and distributional questions separate.
5. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 61%, integrated path 72%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. The +1 percentage-point D7 / +1 integrated update is credited only to terminal Iter492 because it materially narrows the angular-Haar blocker to a frozen critical boundary-layer bracket. Launching Iter493 carries no readiness credit until terminal evidence exists.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No positive-measure or absolute Haar convergence/divergence theorem. No universal causal-EPRL/contour no-go theorem. No terminal D7 label. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
