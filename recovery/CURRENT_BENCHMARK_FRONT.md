# Current Benchmark Front
Updated: 2026-09-13

## Authoritative frontier
The repository has moved beyond Iter464. Iter459, Iter460, Iter462, Iter463 and Iter464 are terminal and consumed. Iter461 remains independently queued on its research branch; Iter465 is the active mainline D7-S2 prerequisite. Repository artifacts and frozen contracts remain authoritative; D7 stays fail-closed.

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

## Consumed causal-Toller / distributional chain
- Iter457 run `34741925566`, artifact `10313410848`: `ITER457_TOLLER_EQ7_FULL_MAGNETIC_RECONSTRUCTION_QUALIFIED_SCOPED`.
- Iter458 run `34744070219`, artifact `10313389047`: `SCIENTIFIC_FAIL_ITER458_TOLLER_FEYNMAN_IEPSILON_ORDINARY_TRUNCATION`. This rejects only the frozen ordinary symmetric truncation realization.
- Iter459 run `34746472976`, artifact `10313863332`, digest `sha256:f54e6e4ee1b787f17b7bab924409611297ce06ac73a005e308be3d1613a9aa8d`: `ITER459_TOLLER_PLEMELJ_DISTRIBUTIONAL_KERNEL_QUALIFIED_SCOPED`, 6/6 Schwartz lanes. This qualifies the universal Sokhotski-Plemelj denominator boundary identity only.
- Iter460 run `34748501676`, artifact `10314837771`, digest `sha256:ce4f1a8a18c6c8282dad4a7f424f322e0e5133c926dfb327ce0c68f7f34163d0`: `ITER460_SOURCE_P11_D_TAIL_CHARACTERIZED_SCOPED`, 24/24 records. The source `P11*d_source` tail is non-Schwartz and shows a growing oscillatory/polynomial envelope on the frozen panel. No physical divergence theorem follows.
- Iter462 run `34748508906`, artifact `10315340931`, digest `sha256:97cc6c2e18df2467b2f4130b8cf2866b021c212d81fb9d9878a0448455adbc3a`: `ITER462_D7_S3_S4_EVIDENCE_LOCALIZATION_COMPLETE_SCOPED`. Six of seven unresolved S3/S4 gate names have no formal candidate artifact in the tracked snapshot; the sole normalized-comparator candidate is explicitly negative/not transport-ready.
- Iter463 prereg `6c99b1593c14ed1fcd9b0469c64e745b903510a5`, retry head `97d2f39d20026e97b3268551dd595210dd3206b5`, run `34748737283`, aggregate job `103701422450`, artifact `10315131796`, digest `sha256:1fdd4f0258795fa23d9c2625035f31aca7bdd5634ddafa0a3a134330d34450da`: `ITER463_SOURCE_P11_D_LEADING_OSCILLATORY_ASYMPTOTICS_QUALIFIED_SCOPED`.
- Iter464 prereg `599f49a76df6e745724cdc1fa06010e5442ca4af`, head `933da7cf5cfeac82b643b2ab457d744670a6dcc1`, run `34750582787`, aggregate job `103706358448`, artifact `10316110295`, digest `sha256:d628fbf9cf259cb6522d6d73d12d5e7a3ab3fd2c2d5c242be9cb35f2f559585d`: `ITER464_SOURCE_P11_D_DISTRIBUTIONAL_PAIRING_QUALIFIED_SCOPED`. All 6 lanes / 24 frozen records pass. Exact denominator cancellation and source-channel reconstruction hold at high precision; Plemelj and Fourier-selector boundary values agree; finite-epsilon errors approach the boundary monotonically under the frozen rule. This qualifies only the one-dimensional source-specific spectral pairing and does not close D7-S2.

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Status at this update: queued.
- Do not duplicate. Terminal classification requires raw artifact consumption against its preregistered exact Bell(5)/local-pair-power gate.

### Iter465 — source two-factor transversal pullback / order independence
- Preregistration commit: `9b968ec425b857cc94fb320eb2ebe6cf2f89ffbe`.
- Implementation commit: `bf37d728a4f2e140b3aa0425ac937d6e0d36d2f9`.
- Workflow/head commit: `bbdeeb86a9ffb228eed2c1e536734264ee32512c`.
- Production run: `34753163940`.
- Status at this update: queued.
- Six independent source-pair lanes, all four boundary-sign pairs and four invertible nontrivial integer reparameterizations are frozen. The gate compares the canonical tensor-product selector, direct transformed common-pole residue/Jacobian evaluation, and both Schur-complement sequential resolution orders. Wrong-sign, wrong-Jacobian and singular-normal controls are frozen.
- PASS, if obtained, qualifies only a transversal two-factor source-defined pullback/order-independence prerequisite. Shared-variable/non-transversal collision structure from the actual causal vertex remains outside this gate.

## Current blockers
### D7-S2
The universal Plemelj kernel, source leading phase/power structure and exact one-dimensional source-specific distributional pairing are qualified. The next unresolved layer is multivariable pullback/order independence and then correlated/shared-variable or non-transversal causal-vertex structure. Iter465 addresses only the transversal two-factor layer.

### D7-S3 / D7-S4
Iter462 found no positive closure artifact for the unresolved tracked gate names and one explicit negative comparator/transport candidate. Do not invent missing transport/closure maps.

## Exact next permitted decisions
1. Consume Iter465 immediately when terminal; distinguish scientific FAIL from numerical/infrastructure failure.
2. Consume Iter461 when it starts/terminates; use a PASS only as collision-geometry evidence.
3. If Iter465 qualifies, prospectively preregister a correlated/shared-variable or non-transversal source-distribution gate grounded in an actual causal-vertex contraction object. Do not infer that layer from tensor-product transversality.
4. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 58%, integrated path 69%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. The +1 pp D7 / +1 pp integrated update reflects terminal Iter464 qualification of the actual one-dimensional non-Schwartz source pairing under the published spectral i-epsilon. D7-S2 remains open.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No universal causal-EPRL/contour no-go theorem. Keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
