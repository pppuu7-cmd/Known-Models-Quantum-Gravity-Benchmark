# Current Benchmark Front
Updated: 2026-09-13

## Authoritative frontier
The repository has moved beyond Iter463. Iter459, Iter460, Iter462 and Iter463 are terminal and consumed; Iter461 and Iter464 are active/queued. Repository artifacts and frozen contracts remain authoritative; D7 stays fail-closed.

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
- Iter460 branch `research/iter460-source-spectral-tail`, run `34748501676`, artifact `10314837771`, digest `sha256:ce4f1a8a18c6c8282dad4a7f424f322e0e5133c926dfb327ce0c68f7f34163d0`: `ITER460_SOURCE_P11_D_TAIL_CHARACTERIZED_SCOPED`, 24/24 records. The source `P11*d_source` tail is non-Schwartz and shows growing oscillatory/polynomial envelope on the frozen panel (roughly slope +0.84 for m=0 and +1.67 for m=+/-1). No physical divergence theorem follows.
- Iter462 branch `research/iter462-d7-s3-s4-evidence-audit`, run `34748508906`, artifact `10315340931`, digest `sha256:97cc6c2e18df2467b2f4130b8cf2866b021c212d81fb9d9878a0448455adbc3a`: `ITER462_D7_S3_S4_EVIDENCE_LOCALIZATION_COMPLETE_SCOPED`. Six of seven unresolved S3/S4 gate names have no formal candidate artifact in the tracked snapshot; the sole normalized-comparator candidate is explicitly negative/not transport-ready. No positive S3/S4 closure artifact was found.
- Iter463 prereg `6c99b1593c14ed1fcd9b0469c64e745b903510a5`, authoritative retry head `97d2f39d20026e97b3268551dd595210dd3206b5`, run `34748737283`, aggregate job `103701422450`, artifact `10315131796`, digest `sha256:1fdd4f0258795fa23d9c2625035f31aca7bdd5634ddafa0a3a134330d34450da`: `ITER463_SOURCE_P11_D_LEADING_OSCILLATORY_ASYMPTOTICS_QUALIFIED_SCOPED`. All 6 lanes / 24 records pass after the separately recorded control-only repair. On the frozen panel m=0 has leading power 1 with +/-beta pair; m=-1 has leading power 2 with +beta; m=+1 has leading power 2 with -beta. This is an asymptotic-structure prerequisite only.

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Status at this update: queued.
- Do not duplicate. Terminal classification requires raw artifact consumption against its preregistered exact Bell(5)/local-pair-power gate.

### Iter464 — exact source exponential-polynomial / Feynman distributional pairing
- Preregistration commit: `599f49a76df6e745724cdc1fa06010e5442ca4af`.
- Implementation commit: `06774a643170161ba873721f4c93d597a55d7af7`.
- Workflow/head commit: `933da7cf5cfeac82b643b2ab457d744670a6dcc1`.
- Production run: `34750582787`.
- Status at this update: queued.
- Frozen identity uses the exact algebraic cancellation `P11/(x+x^3)=-i/[(i rho+1)(i rho)(i rho-1)]`, reducing the source factor to a finite sum of `x^n exp(i sigma beta x)` channels with n<=2. The frozen Feynman pairing uses the published denominator `x-rho-i*s*epsilon` and the standard tempered-distribution/Plemelj Fourier rule at nonzero beta; no damping, fitted subtraction, contour tuning or `beta+i*epsilon` replacement is allowed.
- Matrix: m=-1,0,+1; beta=0.8,2.1; rho=0.35,1.6; boundary sign s=+/-1; high-precision held-out source reconstruction, Plemelj-vs-selector equality, finite-epsilon approach and wrong-sign controls.
- PASS, if obtained, qualifies only the one-dimensional source-specific spectral pairing; it does not by itself close D7-S2 or prove a full causal-vertex theorem.

## Current blockers
### D7-S2
The universal Plemelj kernel and source leading phase/power structure are qualified. The key remaining question is whether the actual non-Schwartz source factor admits a source-faithful distributional pairing under the published spectral i-epsilon and, after that, whether the required multivariable/pullback structure is valid. Iter464 addresses only the one-dimensional source pairing prerequisite.

### D7-S3 / D7-S4
Iter462 found no positive closure artifact for the unresolved tracked gate names and one explicit negative comparator/transport candidate. Do not invent missing transport/closure maps.

## Exact next permitted decisions
1. Consume Iter461 and Iter464 immediately when terminal; distinguish scientific FAIL from numerical/infrastructure failure.
2. If Iter464 qualifies, preregister the next multivariable/pullback/order-independence D7-S2 gate using the source-defined distributional object; do not promote D7-S2 from the one-dimensional pairing alone.
3. If Iter461 passes its exact combinatorial audit, use it only as collision-geometry evidence; do not close D7-S2 from K5 local power counting alone.
4. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 57%, integrated path 68%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. The +1 pp D7 / +1 pp integrated update reflects the terminal qualification of the source-specific leading oscillatory structure in Iter463, which removes one prerequisite uncertainty but does not close D7-S2.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No universal causal-EPRL/contour no-go theorem. Keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
