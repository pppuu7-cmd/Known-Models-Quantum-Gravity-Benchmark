# Current Benchmark Front
Updated: 2026-09-14

## Authoritative frontier
Mainline has advanced through terminal Iter499. Iter461 remains independently queued on its research branch and must not be duplicated.

The consumed D7-S2 chain includes Iter468 source contraction pinning; Iter479 source Toller leading magnetic rank; Iter480B boundary-intertwiner noncancellation; Iter481 full angular/intertwiner network; Iter482 compact common-node correlation; Iter483 shared-node noncompact SL(2,C) geometry; Iter484 source one-edge Toller/KAK lift; Iter485 correlated ten-edge Toller magnetic network; Iter487/489 one-dimensional shared-Haar NONDECAY witness; Iter491 negative fixed-radius sampled thickening; Iter492 shrinking tangent-boundary-layer bracket; Iter493 full-basis q=1 local first/second variation; Iter494 mixed q=1 curvature; Iter495 simultaneous multivariate Taylor stress; Iter496 coefficient-stencil/Richardson convergence; Iter497 independent Richardson-enclosure holdout validation; Iter498 sampled continuum-regularity diagnosis; and Iter499 the first direct Arb/Acb continuum-envelope attempt, which terminates as a validated-arithmetic method blocker before science classification.

Iter497 authority: prereg `3209cdadeed3dc7d5c1ceb12d72e8841fb688901`, evaluator `742199df295815841725820052aad6a468786ee9`, aggregate implementation `359492922a100582994dc6eb5e44845761b987d2`, production head `a7517b7fcd12e3a1a129a16881ee3e348a7b72e8`; run `34811898887`; aggregate artifact `10336250420`; digest `sha256:1804657dd14eb939da835c0c8f0eca84a5a93d76014f11016b0f642bcad19f0f`. Terminal classification: `ITER497_RICHARDSON_ENCLOSURE_HOLDOUT_QUALIFIED_SCOPED`.

All 12 Iter497 raw lanes are represented in the terminal aggregate: 192 frozen states and 768 independent holdouts. All 768/768 holdouts are covered by the prospectively frozen conservative Richardson enclosure; worst coverage ratio is `0.483944238351976`. All source/training/frozen predicates pass and there are no missing or invalid jobs. This materially validates finite holdout generalization, but it is not a continuum interval/uniform certificate.

Iter498 authority: prereg `0bedcbaf7b065b050585f2a3505c8bf0e2a14457`, evaluator `2148981be0a808094cd0b4b1b80d2e65fd586807`, aggregate implementation `432773c916872f6300a2c0e4d56872318eaa03bd`; control-only source-lock wording repair head `2bc6756dffdbf10b2d70bdf174657f7f2d478864`; authoritative retry run `34816799788`; aggregate job `103890003162`; aggregate artifact `10337025880`; digest `sha256:65851b593dfdc385969e4da67a9e9aa992f328f801521798d2a8c05e349ed814`. Terminal classification: `ITER498_MAX_ENVELOPE_NONSMOOTH_BLOCKER_IDENTIFIED_SCOPED`.

All 12 Iter498 jobs are valid. Aggregate diagnostics: two argmax switches, minimum relative top-two gap `0.0002002130966857187`, and minimum positive KAK beta `0.5017347792114244`. The only nonregular sampled lane is `0to5-b0`; both switches occur for direction `[1,1,1,-1,-1,-1]`, sign `+`, rho `2.7`, across amplitude `0.00234375 -> 0.00250`, at R=10 and R=12. The maximizing intertwiner channel changes `195 -> 222`, i.e. `(2,1,0,2,0) -> (2,2,0,2,0)`. The KAK margin is healthy; the blocker is genuine finite max-envelope branch switching. Result note: `results/ITER498_CONTINUUM_REGULARITY_RESULT_2026-09-14.md`.

Iter499 authority: prereg `5fd8124af8edb374d6b48c2a5e2e66cd7b322e54`; Arb core `f16f3106925f13e6e1d847f2d555b5d8fedc5b4d`; evaluator `bd935a81c2d2b1a1f4db78e1355054d92d36760f`; aggregate `cde7d15e03dd6d9a0ac6a78d61b07da4ff3ec517`; workflow/head `33d4dacc705247ab5966f1c01083cd92ee8ab2c1`; run `34818229950`; aggregate job `103895072732`; aggregate artifact `10337765174`; digest `sha256:70006ae095cebcb82dddbcfa4af72d40da7c8d3845747411a50a28eecd7b9513`. Terminal classification: `ITER499_NUMERICAL_METHOD_BLOCKER`.

All 12 expected Iter499 jobs are present exactly once and aggregate structure is valid, but all 12 lanes are method-blocked before any interval max-envelope/slope state becomes valid. No science slope or drift result is promotable from Iter499. Inspected raw lanes fail at the frozen interval-KAK positivity/separation predicate upstream of the 243-channel contraction; exact-rational intertwiner regression itself is exact on the inspected lanes.

A frozen diagnostic-only run (`34818721003`, artifact `10336829843`, digest `sha256:a1edf763095c80c512b5ef0776187124154fc17695e29a68715021742f71a85e`) is `ITER499_DEPENDENCY_DIAGNOSTIC_UNRESOLVED`, but it isolates the numerical mechanism: factorizing shared-node relatives cures all internal edges `1<=a<b<=4` on the representative box, while generic interval-KAK still loses certification for a boosted node and one `0b` edge at the largest R. Midpoint algebraic equivalence of naive and factorized relative matrices passes. Exact compact-sandwich covariance supplies the minimal next method: node and `0b` singular values/Cartan beta are invariant under the amplitude-dependent left/right SU(2) factors, so those factors should be stripped before KAK and restored afterward; internal edges should use dependency-preserving factorization. Result note: `results/ITER499_DIRECT_MAX_ENVELOPE_INTERVAL_RESULT_2026-09-14.md`.

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
- Last authoritative status: queued with no jobs; do not duplicate.

### Next D7-S2 dependent gate
Open only a **validated-arithmetic enabling gate**. Freeze and test the compact-sandwich/factorized KAK construction over the entire Iter499 16-box state space before repeating the direct max-envelope science classifier.

Required mathematical identities:
- node `g_a=L_a B G_a R_a` with `L_a,R_a in SU(2)`: singular values and beta equal those of fixed middle `B G_a`;
- `h_0b=R_b^{-1}(G_b^{-1}B^{-1})L_b^{-1}`: singular values and beta equal those of fixed middle `G_b^{-1}B^{-1}`, and if the middle has KAK `U1 A U2`, then the full KAK is `(R_b^{-1}U1) A (U2 L_b^{-1})`;
- internal `h_ab` must use the dependency-preserving factorization `R_b^{-1}G_b^{-1}B^{-1}L_b^{-1}L_a B G_a R_a`, with outer compact factors stripped/restored around its KAK.

The enabling gate is allowed to make only a validated-construction/covariance claim. It may not classify NONDECAY, max-envelope slopes or Haar convergence. A full enabling PASS is required before a fresh prospectively frozen continuum-envelope science gate.

### Ten-source-spectral object audit
Iter468 authority is recovered exactly. Source Eq.(3) assigns each wedge its own independent spectral variable with measure `d rhot/(2*pi*i)`, pole factor `±1/(rhot-rho∓i eps)` and gamma-function ratio; source Eq.(4) uses ten Toller factors and four unfixed SL(2,C) integrations after `g1=1`. Direct substitution gives ten independent spectral integrations coupled through one common four-group kernel. Iter468 run `34770144171`, aggregate artifact `10322025879`, digest `sha256:f45fe3012ed14fa4449554e9cd87edbedbe81a551a694d349adae2211a61a5ff`, terminal `ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED`.

The next source-only task is not to invent an integration order: the published object is a simultaneous ten-variable boundary-value expression under a single `eps->0+` prescription. Exact treatment of product boundary values/Fubini-Tonelli legitimacy remains open and must be separated from absolute convergence and from any iterated numerical quadrature. No shared-spectral-variable shortcut, artificial spectral delta, fitted contour or post-hoc ordering is authorized.

## Current blockers
### D7-S2
1. validated compact-sandwich/factorized KAK construction across the frozen Iter499 interval state space;
2. after (1), a fresh prospectively frozen direct continuous max-envelope certificate allowing channel crossings;
3. subsequent extension from frozen one-dimensional q=1 direction intervals to a genuine multidimensional angular neighborhood if the direct interval gate succeeds;
4. exact treatment of ten independent/source-defined spectral boundary values with the published common epsilon prescription and correlated group kernel;
5. K5 collision geometry and correlated boundary-value admissibility (Iter461 stream);
6. separation of absolute convergence from conditional/PV/source-defined distributional amplitudes.

No independent-edge surrogate, shared spectral-variable fiction, fitted cancellation, replacement of source KAK by polar factors, false Toller composition, artificial Haar-suppressing weight, post-hoc q/h refinement, post-hoc safety-factor enlargement, sampled-dominance relabelled as interval proof, determinant projection, midpoint substitution for an interval proof, or post-hoc contour modification is allowed.

### D7-S3 / D7-S4
Remain open/partial. Preserve existing negative and blocked transport/closure evidence; do not invent missing closure maps.

## Exact next permitted decisions
1. Prospectively freeze the full-state-space compact-sandwich/factorized KAK enabling gate; no NONDECAY or Haar classifier belongs in it.
2. Only if that enabling gate passes may a new prospectively frozen direct max-envelope interval science gate reuse the Iter499 16-box cover or adopt another cover fixed before new production.
3. Continue the exact ten-spectral source/boundary-value audit independently; keep the single published `eps->0+` prescription and ten independent variables explicit.
4. Consume Iter461 immediately if terminal; never duplicate its authoritative queued run.
5. Keep absolute convergence, iterated/conditional/PV finite parts and source-defined distributional amplitudes distinct.
6. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 65%, integrated path 76%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. Iter499 earns no closure point: it identifies a validated-arithmetic blocker before the scientific continuum-envelope predicate is reached.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No positive-measure or absolute Haar convergence/divergence theorem. No universal causal-EPRL/contour no-go theorem. No terminal D7 label. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
