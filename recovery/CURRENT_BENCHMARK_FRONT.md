# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter285 LQG Lorentzian entropy observable audit
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
- D7-S0 = PASS; D7-S1 = PASS; D7-S2 = NOT_CLOSED; D7-S3 = NOT_CLOSED; D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED; D7-S5 = NOT_AUTHORIZED; D7-S6 = INACTIVE.
- `NEW_REQUIRED`, `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED` are not authorized.
- Candidate Gravity remains inactive at canonical R3 = 24%.

## Readiness metrics
- Operational polygon readiness = 100%.
- D7 protocol infrastructure readiness = 100%.
- 15-row decision-stack synchronization remains validated.
These are infrastructure/operational metrics, not scientific D7 closure.

## Recent material reopens
### Iter277 — RQCP multi-axis resource closure
Independent cutoff audit established a material Hilbert/domain axis. Methodological delta: `MULTI_AXIS_RESOURCE_CLOSURE`. RQCP remains nonterminal.

### Iter278–280 — Asymptotic Safety / NSF
AS fixed-point and Lorentzian spectral evidence strengthened but stable public contact-complete `s+t+u+A4` remains missing. NSF reduced to existing GR parent; census remains 15.

### Iter281 — LQG stack construction
Han, PRD 113, 084034 (2026): explicit Hessian/nondegeneracy/refinement-control machinery independently strengthened. Topological infinite-cutoff regime is not physical UV->IR/GR closure.
Scientific run `34554825500`: 4/4 + aggregate SUCCESS.

### Iter282 — physical continuum certificate
Bruno–Colafranceschi–Mele–Rovelli, PRD 114, 066005 (2026): strong inductive-Hilbert convergence can force TQFT; distributional/rigging-map continuum evidence is admissible. Added `PHYSICAL_CONTINUUM_CERTIFICATE_ADAPTER`. Model-specific physical objects still required.

### Iter283 — LQG UV-to-IR bridge identity
Strong endpoints exist inside the shared LQG parent:
- large-spin/refinement Einstein-equation endpoint;
- small-spin Lorentzian complete-stack UV fixed-point endpoint.
Run `34555702346`: 4/4 + aggregate SUCCESS.
State: `shared_parent_family=true`, `material_positive_endpoints=true`, `same_realization_terminal_bridge_ready=false`.
Interpretation: **missing bridge/transport, not missing endpoints**.

### Iter284 — canonical/covariant physical-state component
Yang–Zhang–Ma, PRD 104, 044025 (2021): genuine scoped rigging-map/weak-constraint component for generalized Euclidean EPRL, `beta=1`, certain states.
Run `34556068228`: 4/4 + aggregate SUCCESS. Methodology `34556068266`: SUCCESS. Reproducibility `34556405328`: SUCCESS.
Boundary: no generic-beta/full-state/Lorentzian transport into Iter283 chain.

### Iter285 — Lorentzian entropy observable anchor
Primary object: Muxin Han, *Lorentzian spinfoam gravity path integral and geometrical area-law entanglement entropy*, Phys. Rev. D 113, 084044 (2026), DOI `10.1103/kbw3-m49g`.

Parallel workflow `lqg-lorentzian-entropy-observable-audit`, run `34557034125`: 4/4 independent guards + aggregate SUCCESS with `fail-fast:false`, `max-parallel:4`.
Methodology CI `34557034108`: preflight + 4/4 independent shards + aggregate/bundle SUCCESS.
Aggregate digest: `sha256:f86b1ac47148f9918a9efd46c6ab7efcea85e73208ea6ace9a224326ba24f7da`.

Guard results:
- `PASS_SCOPED_BH_NORMALIZATION_IDENTITY_BETA_EQUALS_PI_GAMMA`;
- `PASS_SCOPED_BH_MATCH_REQUIRES_EXPLICIT_COUPLING_GAMMA_SELECTION`;
- `PASS_LEADING_AREA_COEFFICIENT_2COMPLEX_INDEPENDENT__SUBLEADING_GRAPH_DEPENDENCE_REMAINS`;
- `PASS_HIGH_VALUE_LORENTZIAN_GRAVITATIONAL_OBSERVABLE_ANCHOR__UV_IR_TRANSPORT_STILL_MISSING`.

Aggregate classification:
`HIGH_VALUE_LORENTZIAN_ENTROPY_OBSERVABLE_ANCHOR_WITH_BH_NORMALIZATION__COUPLING_SELECTION_AND_UV_IR_TRANSPORT_REMAIN_OPEN`

Meaning:
- a material Lorentzian dynamically generated gravitational observable anchor now exists in the spinfoam-stack sector;
- `A=4*pi*gamma*lP^2*a` and `S≈beta*a` imply exact BH normalization `beta=pi*gamma`; independent probe verified `S/(A/lP^2)=1/4` on four gamma values;
- leading area-law coefficient is positive and independent of selected 2-complexes in the source construction;
- BH matching requires a stack-coupling↔gamma relation, so it is not parameter-free;
- subleading log correction may retain boundary-graph dependence;
- no same-realization normalized observable transport through small-spin UV -> physical-state -> large-spin Einstein endpoint has been demonstrated with common comparator and propagated errors.

LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS.

Canonical blocker remains:
`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

Interpretive refinement: the family now has strong physical-state, UV, GR and Lorentzian-observable components; the decisive missing object is compatible same-realization transport among them.

## Publication handoff
`recovery/PUBLICATION_IMPACT_LEDGER.md` is authoritative.
- Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`.
- Paper III: Iter278–285 = `NOT_NEEDED` as additional rules.
- Paper IV: Iter277–285 = `READY` with stated scope boundaries.
- Paper IV LQG wording should present a four-component near-bridge: physical-state link + UV endpoint + Lorentzian observable anchor + GR endpoint, with missing compatible same-realization signature/parameter/observable transport.

## Current scientific decision state
- 15 Tier-1 families.
- 1/15 strict terminal in declared low-energy benchmark domain.
- 0/14 candidate-QG families strict terminal.
- Remaining rows are PARTIAL/BLOCKED/nonterminal; this is not refutation.
- D7-S2/S3/S4 remain open; no global new-theory/adaptation verdict is authorized.

## Anti-idle compute policy
Whenever scientifically meaningful, nonduplicating calculations are mutually independent, launch them immediately as parallel jobs/matrices with `fail-fast:false` and the highest safe practical runner parallelism. Keep only dependent classification/aggregate stages behind barriers. If runner capacity is saturated, queue the extra independent jobs instead of suppressing them. Never rerun saturated calculations merely to manufacture load.

## Exact next gate
`D7_S2_EXTERNAL_AUTHORITY_DRIVEN_TERMINALIZATION_WITH_MULTI_AXIS_RESOURCE_CLOSURE_EXPLICIT_REDUCTION_MAPS_PHYSICAL_CONTINUUM_CERTIFICATES_AND_SAME_REALIZATION_TRANSPORT`

Priority:
1. test whether published Euclidean↔Lorentzian EPRL analytic-continuation/Wick-rotation constructions can bridge any part of the Iter284 signature gap without silently changing the physical real-Immirzi realization;
2. search for explicit parameter/state/observable transport linking the Iter283 UV and GR endpoints and Iter285 Lorentzian entropy anchor;
3. retain immediate external watch for stable public AS contact-complete `s+t+u+A4`;
4. RQCP all-band/background-independent autonomy bridge with Hilbert-cutoff closure;
5. other Tier-1 families only on materially new primary authority.
