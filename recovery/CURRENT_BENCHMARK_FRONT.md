# Current Benchmark Front
Updated: 2026-09-14

## Authoritative frontier
Mainline has advanced through terminal Iter495. Iter461 remains independently queued on its research branch and must not be duplicated.

The consumed D7-S2 chain includes Iter468 source Eq.(3)->Eq.(4) contraction pinning; Iter479 source Toller leading magnetic rank; Iter480B boundary-intertwiner noncancellation; Iter481 full angular/intertwiner network; Iter482 compact common-node correlation; Iter483 shared-node noncompact SL(2,C) geometry; Iter484 source one-edge Toller/KAK lift; Iter485 correlated ten-edge Toller magnetic network; Iter487/489 one-dimensional shared-Haar NONDECAY witness; Iter491 negative fixed-radius sampled thickening; Iter492 shrinking tangent-boundary-layer bracket; Iter493 full-basis q=1 local first/second variation; Iter494 mixed q=1 curvature; and Iter495 simultaneous multivariate Taylor stress.

Iter495 authority: prereg `1b73918e53663186eb4811a62922cd4402220958`, evaluator `7ab222baf9fede2e5ff39a07d770c0f5544c1f61`, aggregate implementation `1a2f6974156dc4e6a1eaae7f4b95e3258f5c5ebe`, production head `49a4695e2ecc43391d3477d0ff9554b910e425ee`; run `34804409129`; aggregate job `103854581566`; aggregate artifact `10333052075`; digest `sha256:6d0cf4c19a3735d4509772ab43e246ab58da3d408534cbd09578348e3ed44a77`. Terminal classification: `ITER495_MULTIVARIATE_TAYLOR_STRESS_QUALIFIED_SCOPED`.

All 12 Iter495 scientific jobs are terminal success and aggregate is valid with no missing/invalid jobs. However the quadratic remainder is not uniformly cubic on the frozen simultaneous perturbations: max absolute remainder `2.1820206151890176e-4`, max `|r|/a^3=4069.3407635785657`, observed small/large remainder ratio median `0.22654674656585128` and max `9.533261802575108` versus cubic expectation `0.125`. Therefore a direct validated quadratic Taylor-envelope certificate is not authorized.

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

### Iter496 — coefficient-stencil convergence / Richardson diagnostic
- Prereg: `fb9b2a5f8ed3dc24beba31e6e55fdf3f60692898`.
- Evaluator: `4351165495050e533bd812b30dbcd31276c15634`.
- Aggregate implementation: `c277968c65ddd2587250ce8b859cad6409cbd579`.
- Workflow/production head: `1098eb1f8a8ceac78013e8c85194bad61d43cf6a`.
- Run: `34807803061`.
- Frozen coefficient stencils `{0.0050,0.0025,0.00125}`, second-order Richardson from the two finest stencils, target amplitudes `{0.00125,0.0025}`, same Iter495 chart/directions/q=1/rho witnesses.
- Matrix: 3 causal classes × 4 direction blocks = 12 independent jobs; `fail-fast:false`, `max-parallel:12`.
- Purpose: distinguish finite-difference coefficient truncation from genuine higher-order/nonlocal angular structure before choosing an interval certificate or higher-order model.

### Ten-source-spectral object audit
Iter468 remains the source authority for ten independent spectral variables and the shared group kernel. Exact published normalization, ordering and i-epsilon prescription remain mandatory before a production ten-spectral gate. No shared-spectral-variable shortcut or fitted contour is authorized.

## Current blockers
### D7-S2
Iter492 established finite-grid critical bracket `(0.75,1.00]`; Iter493/494 measured anisotropic first/second/mixed local response; Iter495 shows the resulting finite-difference quadratic model has a non-uniformly-cubic remainder on simultaneous perturbations. Remaining blockers:
1. separate coefficient-stencil truncation from genuine higher-order angular structure (Iter496); then choose either validated coefficient/remainder enclosure or a prospectively frozen higher-order/direct interval treatment;
2. exact coupling to ten independent/source-defined spectral integrations with published normalization, order and i-epsilon;
3. K5 collision geometry and correlated boundary-value admissibility (Iter461 stream);
4. separation of absolute convergence from conditional/PV/source-defined distributional amplitudes.

No independent-edge surrogate, shared spectral-variable fiction, fitted cancellation, replacement of source KAK by polar factors, false Toller composition, artificial Haar-suppressing weight, post-hoc q/h refinement, or post-hoc contour modification is allowed.

### D7-S3 / D7-S4
Remain open/partial. Preserve existing negative and blocked transport/closure evidence; do not invent missing closure maps.

## Exact next permitted decisions
1. Consume Iter496 matrix/aggregate when terminal. Any failure must first be separated into infrastructure/numerical versus scientific failure.
2. If coefficient refinement/Richardson materially suppresses the remainder across the frozen states, prospectively design a validated coefficient/remainder enclosure. If not, prospectively design a third-order-or-direct interval treatment; do not tune h or directions post hoc.
3. Consume Iter461 immediately if terminal; never duplicate its authoritative queued run.
4. Continue exact ten-spectral source audit independently; keep Haar, spectral, PV/conditional and distributional questions separate.
5. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 63%, integrated path 74%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. Iter495 materially identifies a new remainder-scaling blocker but does not close or sufficiently narrow D7-S2 to earn readiness credit; therefore the stable rubric is unchanged. Launching Iter496 carries no readiness credit until terminal evidence exists.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No positive-measure or absolute Haar convergence/divergence theorem. No universal causal-EPRL/contour no-go theorem. No terminal D7 label. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
