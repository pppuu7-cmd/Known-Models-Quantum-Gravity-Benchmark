# Iter463 terminal result — source P11*d leading oscillatory asymptotics

Date: 2026-09-13

## Scientific classification
`ITER463_SOURCE_P11_D_LEADING_OSCILLATORY_ASYMPTOTICS_QUALIFIED_SCOPED`

## Authority
- Preregistration commit: `6c99b1593c14ed1fcd9b0469c64e745b903510a5`
- Implementation commit: `c8a2c9d708795a2152002a75b41ef13d21a197f1`
- Control-authority record: `46d91caa9d2a4922fb69b9f45b52fa4a16633dda`
- Authoritative retry head: `97d2f39d20026e97b3268551dd595210dd3206b5`
- Authoritative run: `34748737283`
- Aggregate job: `103701422450`
- Aggregate artifact: `10315131796`
- Aggregate digest: `sha256:1fdd4f0258795fa23d9c2625035f31aca7bdd5634ddafa0a3a134330d34450da`

Raw jobs: `103701399787`, `103701399902`, `103701399937`, `103701399976`, `103701399977`, `103701400304`.

Raw artifacts: `10315610338`, `10315510913`, `10315480992`, `10315022223`, `10314977247`, `10314703204`.

## Frozen result
All 6 lanes and all 24 frozen `(m,beta,rho,side)` records pass the preregistered asymptotic-structure gate after the control-only repair recorded separately. The source `P11*d_source` leading tail is consistent on the frozen panel with:
- `m=0`: leading power 1 with the `+beta/-beta` phase pair;
- `m=-1`: leading power 2 with dominant `+beta` phase;
- `m=+1`: leading power 2 with dominant `-beta` phase.

The two independent degree-3 `P11` routes agree at machine precision; scaled leading envelopes stabilize strongly, expected phase recurrences are accurate, and the frozen wrong-power/wrong-frequency controls separate.

## Scope guards
This qualifies only the tested source-tail leading powers/phases. It does **not** establish ordinary convergence, absolute integrability, a source-defined distributional amplitude, causal-vertex finiteness/divergence, D7-S2 closure, or any terminal D7 label. Candidate Gravity remains inactive.
