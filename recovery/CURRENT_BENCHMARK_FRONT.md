# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter288 LQG hierarchy-overlap + Iter289 CFS correction-pathway results ready for archival
Authoritative operational-saturation milestone: Iter270
Authoritative D7 infrastructure milestone: Iter272
Authoritative 15-row census synchronization milestone: Iter276

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census = 15 families.
- Strict terminal coverage = 1/15.
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
These are infrastructure metrics, not scientific D7 closure.

## LQG/spinfoam front
Iter281–287 established a progressively stronger four-component near-bridge:
1. complete-stack/topological/refinement machinery;
2. physical-continuum certificate adapter and scoped canonical/covariant physical-state component;
3. small-spin Lorentzian complete-stack UV endpoint plus large-spin/refinement Einstein endpoint;
4. Lorentzian entropy observable anchor inside the same stack architecture, with exact BH normalization after stated coupling selection.

Important scoped refinements:
- explicit Euclidean↔Lorentzian EPRL vertex analytic continuation exists, but not same-real-`gamma` full state/stack transport;
- UV fixed point and entropy observable are aligned inside the same Lorentzian spinfoam-stack architecture;
- the remaining decisive object is controlled compatible same-realization transport to the large-spin/Einstein regime with parameter identity, normalized observable, comparator and propagated uncertainty.

### Iter288 — semiclassical hierarchy / entropy-domain overlap
Scientific run `34557797109`: 4/4 sensitivity jobs + aggregate SUCCESS.
Methodology `34557797084`: SUCCESS. Reproducibility `34557875010`: SUCCESS.
Digest: `sha256:57986e696cfb7e139bcb75a9cdf9c3f48b65e0f4120b567b624aa4a6b5945f6a`.

Prospective sensitivity convention for published `1 << gamma^-1 << lambda << gamma^-2`:
`lambda >= R/gamma`, `lambda <= 1/(R gamma^2)`, yielding a nonempty window iff `gamma < 1/R^2`.
Results:
- R=2 -> gamma<0.25
- R=3 -> gamma<1/9
- R=5 -> gamma<0.04
- R=10 -> gamma<0.01

Classification:
`QUANTIFIED_SEMICLASSICAL_HIERARCHY_OVERLAP__BH_RANGE_CONTAINS_SMALL_GAMMA_SUBDOMAIN_WITH_REGGE_WINDOW_BUT_NO_UNIQUE_NUMERICAL_DOUBLE_LESS_THAN_THRESHOLD`

Boundary: these are sensitivity thresholds under chosen operational meanings of `<<`, not physical gamma bounds. They establish domain overlap, not a running law or UV→IR trajectory.

LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS.
Canonical blocker remains:
`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

## CFS front
The existing PF1 authority already includes Fischer–Finster arXiv:2605.30199 as exact curved-spacetime Einstein–Dirac comparator evidence and rejects obsolete blockers about absence of curved-spacetime GR/Fock/relational controls. The frozen blocker is a gravity-specific beyond-continuum observable / normalized non-Einstein correction tensor plus same-domain comparator residual.

### Iter289 — systematic current / correction-tensor pathway
Primary object: Finster–Fischer, *Construction of Currents in Causal Fermion Systems*, arXiv:2507.09633 (2025).
Scientific run `34558237027`: 4/4 guards + aggregate SUCCESS.
Methodology `34558237116`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
Digest: `sha256:b27830783f0fa7a90e75689e38584eb21263296c78bdd97d5226e5ac8e4dc9e3`.

Aggregate:
- explicit rank-one CFS current/Maxwell control = true;
- systematic pathway extends in scope to gravity and higher-order quantum/discreteness corrections = true;
- explicit rank-two gravity tensor = false;
- explicit higher-rank gravity correction tensor = false;
- frozen CFS blocker closed = false.

Classification:
`HIGH_VALUE_CFS_SYSTEMATIC_CURRENT_AND_HIGHER_RANK_PATHWAY__GRAVITY_CORRECTION_TENSOR_REMAINS_PROSPECTIVE_AND_BLOCKER_STAYS_OPEN`

CFS therefore remains `BLOCKED_MISSING_REQUIRED_OBJECT`, not FAIL. Iter289 makes the route to the missing object more concrete but does not supply it.

## Other priority fronts
- Asymptotic Safety: stable public contact-complete Lorentzian `s+t+u+A4` package remains decisive external object.
- RQCP: all-band/background-independent autonomy plus Hilbert-cutoff/resource closure remains open.
- Other Tier-1 families reopen only on genuinely new status-changing authority/computation/reduction objects.

## Publication handoff
`recovery/PUBLICATION_IMPACT_LEDGER.md` is authoritative.
- Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`; Iter278–289 = `NOT_NEEDED` as additional rules.
- Paper IV: Iter277–289 = `READY` with stated claim boundaries.

## Anti-idle compute policy
Whenever scientifically meaningful, nonduplicating tasks are independent, launch them immediately in parallel (`fail-fast:false`, highest safe practical runner parallelism). Dependent classification/aggregate stages wait behind explicit barriers. When runners are saturated, queue additional useful independent jobs rather than suppress them. Never repeat saturated or duplicate calculations merely to manufacture activity. The active KMQGB auto-research automation is configured with the same mandatory rule.

## Exact next gate
`D7_S2_EXTERNAL_AUTHORITY_DRIVEN_TERMINALIZATION_WITH_MULTI_AXIS_RESOURCE_CLOSURE_EXPLICIT_REDUCTION_MAPS_PHYSICAL_CONTINUUM_CERTIFICATES_AND_SAME_REALIZATION_TRANSPORT`

Priority:
1. seek/compute an explicit LQG stack-coupling/`gamma`/spin-scale flow connecting the Iter287 same-stack UV/entropy sector to the large-spin Einstein endpoint;
2. seek an explicit CFS rank-two/higher-rank gravity tensor evaluation that produces a normalized beyond-Einstein residual/comparator object rather than a prospective pathway;
3. stable public AS contact-complete `s+t+u+A4`;
4. RQCP all-band/background-independent autonomy bridge;
5. other Tier-1 authority only when materially status-changing.
