# Iter452 — immutable primary-source causal-vertex pin

Date: 2026-09-13

## Frozen gate
Qualify, from one immutable source snapshot only, the source objects required before any Eq.(4)-level direct causal-vertex computation: Toller Feynman definition Eq.(3), causal vertex Eq.(4), boundary spin/intertwiner domains, additive/EPRL controls Eq.(5)/(6), and Cartan magnetic decomposition Eq.(7).

## Provenance
- Preregistration: `eedfb67e6744e18cdd146fa7a739e7d2a5e72ebc`
- Immutable source snapshot commit: `9a9583e312254f2aae96ab637ac849cd80f99faf`
- Implementation: `0250941a29ffbd82b12a0aff258b2800e73d1f52`
- CI/science-separation correction: `c83a8f4dd6d6c74af488c2a9282a716fe543831d`
- Authoritative production head: `32118a2d13a990f32ec3f41352066fb6e63c63d6`
- Authoritative run: `34732114506`
- Aggregate job: `103656784221`
- Summary artifact: `10309392395`
- Downloaded summary ZIP SHA-256: `b537966559056b8ed10bd1d5ec897c70d0f4affb9e5ffd8a04c9e9ec4464e691`
- Frozen source: `arXiv:2601.23162v1`
- Frozen source SHA-256: `a78e72b972a288357b03138d9795299730d3069a4859fe4020a54d2c06607cb0`

## Raw-lane consumption
All five raw lane artifacts were consumed, not inferred from green CI:
- `toller_feynman_eq3`: qualified; Eq.(3), Feynman spectral definition, full real spectral domain, branch kernel, gamma factor and Wigner integrand all present.
- `causal_vertex_eq4`: qualified; Eq.(4), four group integrations, `g_1=identity`, ten ordered wedges, gamma simplicity, magnetic indices and ordered group argument all present.
- `boundary_domains`: qualified; ten spins, five intertwiners, magnetic labels, basis sum and contraction relation present.
- `eprl_controls_eq5_eq6`: qualified; additive identity, unconstrained independent wedge-sign EPRL control and unchanged published `i epsilon` present.
- `cartan_magnetic_eq7`: qualified; Cartan/SU(2) decomposition, finite magnetic-p domain, two Wigner factors and reduced Toller object present.

All five lanes use exactly the same immutable source id and source digest. Aggregate: `5/5 qualified`, `structurally_valid=true`, `same_source_id=true`, `same_source_digest=true`.

## Scientific classification
`PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_PINNED_COMPLETE`

This is a source/object qualification PASS only. It closes the Iter450/451 source ambiguity/incompleteness blocker. It does **not** establish direct causal-vertex convergence, finite normalization, absolute integrability, a distributional finite part, D7-S2 closure, a family-level LQG/spinfoam PASS, or terminal D7.

## Scope locks retained
- D7-S2 remains `NOT_CLOSED`.
- D7-S3 remains `NOT_CLOSED`.
- D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`.
- Terminal D7 remains `NOT_AUTHORIZED`.
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain unauthorized while S2-S4 are open.
- Candidate Gravity remains inactive.
- No universal causal-EPRL/contour no-go and no causal-vertex finiteness/divergence theorem follows.

## Next permitted gate
Prospectively preregister an Eq.(4)-level executable contraction qualification using the pinned source object. The first gate must verify a complete scalar magnetic/intertwiner contraction and exact pointwise Eq.(5)/(6) EPRL control on a deterministic small admissible panel, with basis/permutation/null controls. It is a qualification gate, not a finiteness theorem.
