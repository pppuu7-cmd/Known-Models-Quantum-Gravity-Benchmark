# Current Benchmark Front
Updated: 2026-09-13

## Authoritative frontier
The repository has moved beyond Iter458. Iter459, Iter460 and Iter462 are terminal and consumed; Iter461 and Iter463 are active/queued. Repository artifacts and frozen contracts remain authoritative; D7 stays fail-closed.

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

## Active independent work
### Iter461 — exact K5 collision partitions
- Branch: `research/iter461-k5-collision-partitions`
- Head: `05c7f87c8519349057332bf90021f1128e1eefc3`
- Run: `34748503239`
- Status at this update: queued.
- Do not duplicate. Terminal classification requires raw artifact consumption against its preregistered exact Bell(5)/local-pair-power gate.

### Iter463 — source P11*d leading oscillatory asymptotics
- Preregistration commit: `6c99b1593c14ed1fcd9b0469c64e745b903510a5`.
- Implementation commit: `c8a2c9d708795a2152002a75b41ef13d21a197f1`.
- Workflow/head commit: `4aa4f51e68cae30e6cec766e7359103218cb3b16`.
- Production run: `34748683091`.
- Frozen panel: m=-1,0,+1; beta=0.8,2.1; rho=0.35,1.6; both spectral tails; radii 80..1280.
- Frozen hypothesis: leading power 1 with +/-beta pair for m=0; leading power 2 with +beta for m=-1 and -beta for m=+1. Tests include P11 route agreement, scaled-envelope stabilization, phase recurrence/increment, wrong-power and wrong-phase controls. No damping, fitted subtraction, modified i-epsilon, contour change or coefficient fitting.
- Status at this update: queued. Scientific classification is absent until all raw lanes and aggregate are terminal and consumed.

## Current blockers
### D7-S2
The universal Plemelj kernel is qualified, but the actual source object is non-Schwartz. A source-specific oscillatory/distributional realization preserving the published spectral i-epsilon remains missing. Iter463 is a prerequisite asymptotic-structure audit, not the boundary-value reconstruction itself.

### D7-S3 / D7-S4
Iter462 found no positive closure artifact for the unresolved tracked gate names and one explicit negative comparator/transport candidate. Do not invent missing transport/closure maps.

## Exact next permitted decisions
1. Consume Iter461 and Iter463 immediately when terminal; distinguish scientific FAIL from numerical/infrastructure failure.
2. If Iter463 qualifies the frozen source asymptotics, preregister a mathematically justified source-specific oscillatory/distributional boundary-value gate that preserves the published i-epsilon; no ordinary denser truncation, arbitrary damping or beta+i*epsilon replacement.
3. If Iter461 passes its exact combinatorial audit, use it only as collision-geometry evidence; do not close D7-S2 from K5 local power counting alone.
4. D7 terminal classifier and all four terminal labels remain forbidden until S2-S4 are formally closed.

## Working progress rubric
D2 82%, D4 68%, D7 56%, integrated path 67%.
This is a research-readiness metric, not a formal gate status and not a probability of `NEW_REQUIRED`. The D7/integrated values are lower than the earlier provisional 69%/76% because Iter460 established a harder non-Schwartz source-tail blocker and Iter462 showed that the expected S3/S4 closure artifacts are largely absent rather than merely unconsumed.

## Claim guards
No complete-QG claim. No physical causal-vertex finiteness/divergence theorem. No universal causal-EPRL/contour no-go theorem. Keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct. No fitted completion or modified published spectral i-epsilon. Candidate Gravity remains inactive.
