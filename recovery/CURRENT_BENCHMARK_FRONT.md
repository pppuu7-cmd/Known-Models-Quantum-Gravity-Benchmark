# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter284 LQG canonical/covariant physical-state link compatibility audit
Authoritative operational-saturation milestone: Iter270
Authoritative D7 infrastructure milestone: Iter272
Authoritative 15-row census synchronization milestone: Iter276

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census = 15 families.
- Strict terminal coverage = 1/15.
- Strict nonterminal coverage = 14/15.
- Candidate-family terminal coverage = 0/14.
- Tier-2 unresolved = 0.
- D1 = PASS.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3 = PARTIAL.
- D4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D5 = PASS.
- D6 = PASS_RULE_TARGETS_OPEN.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- D7-S0 = PASS.
- D7-S1 = PASS.
- D7-S2 = NOT_CLOSED.
- D7-S3 = NOT_CLOSED.
- D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D7-S5 = NOT_AUTHORIZED.
- D7-S6 = INACTIVE.
- `NEW_REQUIRED`, `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED` are not authorized.
- Candidate Gravity remains inactive at canonical R3 = 24%.

## Readiness metrics
- Operational polygon readiness = 100%.
- D7 protocol infrastructure readiness = 100%.
- 15-row decision-stack synchronization remains validated.
These are infrastructure/operational metrics, not scientific D7 closure.

## Recent material reopens
### Iter277 — RQCP multi-axis resource closure
RQCP remains a distinct nonterminal Tier-1 parent. Independent cutoff audit established a material Hilbert/domain axis: cutoff 8 -> 28 shifts `G` ~7.32%, gap ~3.07%, `G*gap^2` ~1.36%; high-cutoff 24 -> 28 is extremely stable. Methodological delta: `MULTI_AXIS_RESOURCE_CLOSURE`.

### Iter278 — Asymptotic Safety PIRG
Diffeomorphism-invariant/background-independent PIRG fixed-point evidence strengthened. Six published variants retain two positive relevant directions, but scheme/procedure dependence remains and the public contact-complete `s+t+u+A4` object is still missing.

### Iter279 — NSF classification
NSF was reduced to the existing GR parent rather than promoted as a new Tier-1 family. Tree-level normalization/t-u symmetry checks pass; fixed-angle growth is ~`s^1`; forward behavior remains pole-like. Census remains 15.

### Iter280 — Asymptotic Safety Lorentzian spectral function
Positive normalisable Lorentzian TT-graviton spectral evidence was cross-checked, but the source states those fluctuation states are not physical diffeomorphism-invariant Hilbert-space states, the full numerical curve was not independently reproduced from a public dataset, and the contact-complete scattering blocker remains active.

### Iter281 — LQG spinfoam-stack explicit audit
Han, Phys. Rev. D 113, 084034 (2026). Run `34554825500`: 4/4 independent jobs + aggregate SUCCESS. Methodology CI `34554825514`, reproducibility release `34554911718`, archival methodology `34555185332`: SUCCESS.

Scoped result:
`PASS_SCOPED_EXPLICIT_TRIVIAL_TOPOLOGY_SPINFOAM_STACK_HESSIAN_NONDEGENERACY_INCIDENCE_FACTORIZATION_AND_COEFFICIENT_CONVERGENCE__TOPOLOGICAL_LARGE_CUTOFF_NOT_PHYSICAL_UV_IR_GR_CLOSURE`

### Iter282 — spin-foam physical continuum certificate
Bruno, Colafranceschi, Mele, Rovelli, Phys. Rev. D 114, 066005 (2026). Run `34555287209`: 4/4 guards + aggregate SUCCESS. Methodology `34555287201`, reproducibility `34555302796`, archival methodology `34555562285`: SUCCESS.

Additive Paper-IV adapter:
`PHYSICAL_CONTINUUM_CERTIFICATE_ADAPTER`

Strong inductive-Hilbert convergence that forces a TQFT is not the unique acceptable continuum certificate for physical 4D gravity. Distributional/rigging-map continuum evidence is admissible, but model-specific state/constraint structure, normalized physical observables, UV->IR/GR transport, comparator and errors remain mandatory.

### Iter283 — LQG UV-to-IR bridge identity
Endpoint authorities:
- Han 2017, Phys. Rev. D 96, 024047: large-spin/refinement semiclassical continuum endpoint yielding the Einstein equation;
- Han 2026, Phys. Rev. D 114, 044040: small-spin complete-amplitude UV fixed point with topological leading regime;
- Han 2026, Phys. Rev. D 113, 084034: stack/cutoff topological localization structure.

Run `34555702346`: 4/4 independent guards + aggregate SUCCESS. Methodology CI `34555702337`, archival methodology `34555959626`, reproducibility release `34556045719`: SUCCESS.

Aggregate state:
- `shared_parent_family = true`;
- `material_positive_endpoints = true`;
- `same_realization_terminal_bridge_ready = false`.

Canonical interpretation:
`HIGH_VALUE_UV_AND_GR_ENDPOINTS_IN_SHARED_LQG_PARENT__NO_EXPLICIT_SAME_REALIZATION_PARAMETER_AND_OBSERVABLE_TRANSPORT_BRIDGE`

Interpretive refinement: **missing bridge/transport, not missing endpoints**.

### Iter284 — LQG canonical/covariant physical-state link
Primary object: Yang, Zhang, Ma, *Relating spin-foam to canonical loop quantum gravity by graphical calculus*, Phys. Rev. D 104, 044025 (2021), DOI `10.1103/PhysRevD.104.044025`.

Parallel workflow `lqg-physical-state-link-compatibility-audit`, run `34556068228`: 4/4 independent guards + aggregate SUCCESS. Methodology CI `34556068266`: preflight + 4/4 shards + aggregate/bundle SUCCESS. Aggregate digest: `sha256:61a71ea3aab1fa23b58ad2760b27500c84f34ac62aca5d020526516125cb7d47`.

Aggregate state:
- `physical_state_component = HIGH_VALUE_SCOPED_POSITIVE`;
- `same_realization_chain_ready = false`.

Guard results:
- `PASS_SCOPED_EPRL_RIGGING_MAP_WITH_WEAK_CONSTRAINT_SATISFACTION_ON_CERTAIN_STATES`;
- `PASS_EUCLIDEAN_PHYSICAL_STATE_LINK__LORENTZIAN_SAME_REALIZATION_MAP_MISSING`;
- `PASS_SCOPED_BETA1_CERTAIN_STATES__NO_GENERIC_BETA_OR_FULL_STATE_SPACE_CERTIFICATE`;
- `PASS_HIGH_VALUE_PHYSICAL_STATE_COMPONENT__NOT_YET_COMPATIBLE_SAME_REALIZATION_UV_IR_CHAIN`.

Canonical result:
`HIGH_VALUE_EUCLIDEAN_BETA1_RIGGING_MAP_COMPONENT__NO_EXPLICIT_COMPATIBLE_TRANSPORT_INTO_LORENTZIAN_UV_IR_CHAIN`

Interpretation: LQG now has three strong but incompletely stitched components:
1. a scoped canonical/covariant physical-state/rigging-map link;
2. a large-spin/refinement Einstein-equation endpoint;
3. a small-spin Lorentzian complete-amplitude UV fixed-point endpoint.

The 2021 physical-state component is genuinely positive but scoped to generalized Euclidean EPRL, `beta=1`, certain states, and weak Euclidean Hamiltonian-constraint satisfaction. No explicit state/signature/parameter transport maps it into the Lorentzian 2017/2026 UV-to-IR chain, and no normalized gravity observable is transported through all three components.

LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS.

Canonical blocker remains:
`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

Interpretive refinement: physical-state evidence exists, but the compatible Lorentzian same-realization transport remains missing.

## Publication handoff
`recovery/PUBLICATION_IMPACT_LEDGER.md` is authoritative.
- Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`.
- Paper III: Iter278–284 = `NOT_NEEDED` as additional rules; optional corroboration only.
- Paper IV: Iter277–284 = `READY` for inclusion with stated scope boundaries.
- Paper IV LQG wording should now present a **three-component near-bridge** (physical-state link + GR endpoint + UV endpoint) whose missing object is compatible same-realization signature/parameter/observable transport.

## Current scientific decision state
- 15 Tier-1 families.
- 1/15 strict terminal in its declared low-energy benchmark domain (GR + controlled low-energy EFT baseline).
- 0/14 candidate-QG families strict terminal.
- Remaining rows are PARTIAL/BLOCKED/nonterminal; this is not refutation.
- D7-S2/S3/S4 remain open; no global new-theory/adaptation verdict is authorized.

## Current compute policy
Shard every scientifically independent calculation immediately with `fail-fast: false`; dependent scoring/classification begins only after an explicit aggregate barrier. Do not rerun saturated grids merely to occupy runners.

## Exact next gate
`D7_S2_EXTERNAL_AUTHORITY_DRIVEN_TERMINALIZATION_WITH_MULTI_AXIS_RESOURCE_CLOSURE_EXPLICIT_REDUCTION_MAPS_PHYSICAL_CONTINUUM_CERTIFICATES_AND_SAME_REALIZATION_TRANSPORT`

Priority:
1. search for a Lorentzian or generic-Immirzi canonical/covariant physical-state construction compatible with the Han 2017/2026 chain;
2. search for an explicit state/signature/parameter map connecting Yang–Zhang–Ma-type rigging-map evidence into the Lorentzian complete-stack realization;
3. search for a normalized physical gravity observable transported across the whole UV -> physical-state -> semiclassical GR chain;
4. retain immediate external watch for a stable public contact-complete Asymptotic-Safety `s+t+u+A4` package;
5. RQCP all-band/background-independent autonomy bridge with Hilbert-cutoff closure;
6. other Tier-1 families only on materially new primary authority;
7. any apparently new QG parent must first pass explicit reduction/equivalence audit before census promotion.
