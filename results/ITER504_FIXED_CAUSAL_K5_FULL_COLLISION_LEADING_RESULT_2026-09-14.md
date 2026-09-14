# Iter504 terminal result — fixed-causal K5 full-collision leading contraction

Date: 2026-09-14
Status: **TERMINAL BLOCKED / CONTROL-LOCALIZED; NO SCIENTIFIC PASS OR FAIL**

## Authority

- initial prereg commit: `cb84832b1e7f1dc8fb1142958db91b45e3ab51c5`
- pre-implementation source-normalization correction: `56c9efe184074315296ba2e1c04507f8361208f5`
- evaluator: `038b8ad52671faa4cc1ccc9490b1c75644ec8c5d`
- aggregate: `73c20c4e12924f446834da9f0256bb46bf5842d7`
- workflow production head: `65a806736be9ec5cf08a95b856aaecbaff990aba`
- workflow run: `34872533574`
- source-lock job: `104071698526` — success
- aggregate job: `104073872029`
- aggregate artifact: `10358724329`
- aggregate digest: `sha256:129311244f18c104a9c73ceced3ad66073a27050fed56ee6fdbfc409d4a30708`

## Terminal classification

`BLOCKED_OR_INFRASTRUCTURE_ITER504`

The frozen matrix is structurally complete: all 18 prospectively declared `(panel, causal, rho)` jobs are present exactly once, with no missing or duplicate job ids. There are no `SCIENTIFIC_FAIL_ITER504_UNIFORM_FROZEN_FULL_COLLISION_LEADING_SURVIVAL` lanes.

All 18 lanes are blocked by the same preregistered validation predicate: the finite-`t` source regression fine-scale relative error exceeds the frozen `<5e-3` ceiling.

Aggregate worst fine error:

`0.019886942958436408`.

The refinement predicate itself passes: the finite-`t` error decreases when `t` is halved. KAK reconstruction, source coefficient nonzeroness, tangent cycles, SU(2)/spin-1 conventions, axial-section invariance, common-translation invariance, scale homogeneity, intertwiner controls, magnetic reindexing, zero-edge negative control, and finite normalized contractions pass in the inspected lane artifacts; the aggregate blocking cause is the finite-`t` tolerance.

Therefore Iter504 is a **method/control blocker**, not a scientific cancellation result.

## Diagnostic contraction evidence — explicitly non-promotable under Iter504

Although the frozen control prevents scientific promotion, the raw leading contractions are far from the frozen nonzero threshold:

- every one of the 18 lanes has all `243/243` boundary channels above `1e-12`;
- aggregate total: `4374/4374` nonzero witnesses;
- minimum lane maximum normalized ratio: `0.009121199671125558`;
- T0 maximum ratio: about `0.0091211996711`, max channel `[0,1,0,1,0]`;
- T1 maximum ratio: about `0.0786069961648`, max channel `[0,0,0,0,0]`;
- T2 maximum ratio: about `0.0845382791616`, max channel `[0,0,0,0,0]`.

These values are diagnostic only in Iter504 because `valid=false` follows from the frozen finite-`t` control. They must not be relabeled as the Iter504 PASS classification.

## Exact source explanation of the blocker

The separate exact audit `research/ITER504_J1_EXACT_LAURENT_SCALAR_REDUCTION_2026-09-14.md` derives from the already-qualified Appendix-B source formulas that for `j=1`

`B^+ = a(rho) (1,-2,1)`, `B^- = -B^+`,

with

`a(rho)=3 i / [4 rho(1+rho^2)]`.

It also reconciles the Iter477 hypergeometric normalization by `B_m=C_m^(src)/8`.

Thus the zero/nonzero leading-channel pattern is exactly independent of rho and the causal representative; those labels contribute only a common nonzero scalar/sign. This exact reduction explains why normalized ratios repeat across rho/causal lanes.

The failed finite-`t` control probes the rate of approach to the Laurent coefficient at the particular frozen `t_fine=5e-4`. Its failure does not contradict the exact Laurent coefficient and must not be repaired by retroactively relaxing the Iter504 threshold.

## Admissible repair

The frozen post-gate rule allows only repair of the identified validation defect.

The scientifically clean repair is **not** to tune the `<5e-3` ceiling or keep shrinking `t` until it passes. Instead, prospectively define a new gate whose source-leading normalization is validated analytically by the exact Appendix-B Laurent identity and which tests the same full-K5 leading contraction with the same panels/intertwiners/nonzero threshold.

Because the exact j=1 reduction makes rho and causal dependence a common nonzero scalar, that repaired gate may collapse the redundant 18-lane matrix to the three already frozen geometric panels, while retaining explicit algebraic controls proving the collapse.

## Scope ceiling

No local absolute divergence is established. No positive-measure collision cone, uniform blow-up remainder theorem, Haar divergence theorem, ten-spectral pairing theorem, or physical causal-vertex finiteness/divergence theorem follows. D7-S2/S3/S4 remain unchanged; terminal D7 labels remain forbidden; Candidate Gravity remains inactive.
