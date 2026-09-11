# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter295 Han-stack / generalized causal EPRL-KKL conditional domain overlap scoped; Iter294 CFS Einstein endpoint and earlier bridge refinements retained
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
- Iter290 adds an explicit causal Lorentzian EPRL-vertex large-spin Regge endpoint with a single causal Regge phase, strengthening the IR/semiclassical endpoint but not supplying complete-stack transport;
- Iter291 adds an independent EPRL semiclassical `gamma`-to-observable bridge: in the Bianchi–Rincon-Ramirez gamma-dual EFT construction, `gamma` fixes parity-even/parity-odd higher-curvature coupling relations and is in principle inferable from primordial tensor polarization plus tensor tilt and tensor-to-scalar ratio;
- the remaining decisive object is controlled compatible same-realization transport from the complete-stack UV sector to the causal large-spin Regge/Einstein regime with stack-coupling/`gamma`/spin-scale identity, normalized observable, comparator and propagated uncertainty.

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

### Iter290 — causal Lorentzian vertex / Regge endpoint
Primary object: Bianchi–Chen–Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162 (2026).
Scientific run `34561212081`: four independent guards in parallel + aggregate SUCCESS on head `a6cbecf7507adb9dc52dc0090d171905e1432b50`.
Summary artifact `10184373486`; artifact digest `sha256:ee0ba2168b4ea3113517fadc94abdac82dcfd9c1bfbafff94a686ef3a1e264ec`; raw aggregate digest `sha256:573a5590ffe7a4bfcd298f0a14c13e77c5a034a31bc8d69b280b17dd23493b02`.

Aggregate:
- causal Toller split at EPRL-vertex scope = PASS;
- large-spin causally compatible Lorentzian Regge endpoint / single `exp(+i S_Regge/hbar)` phase = PASS;
- complete-stack/refinement transport = false;
- continuous same-realization UV→IR transport = false;
- family terminal = false.

Classification:
`HIGH_VALUE_CAUSAL_LARGE_SPIN_LORENTZIAN_REGGE_ENDPOINT__NO_COMPLETE_STACK_SAME_REALIZATION_UV_TO_IR_TRANSPORT`

### Iter291 — gamma-duality semiclassical observable / parameter bridge
Primary object: Bianchi–Rincon-Ramirez, *Spinfoams, gamma-duality, and parity violation in primordial gravitational waves*, Physical Review D 113, 124013 (2026), DOI `10.1103/qz89-26hk`.
Scientific run `34568777275`: four independent guards in parallel + aggregate SUCCESS on head `4b2212fe21830964b43fa8c0f9fabef842c6e6aa`.
Summary artifact `10186981524`; artifact digest `sha256:3ef255ea6377cc487447b5ac62df01c43e870ca1f9913e2f7bedbba165b714ad`; raw aggregate digest `sha256:3b7f1797aa37d1722a3fce276520a7e7467c27f834823c6240764f1c32f727b0`.

Aggregate:
- peer-reviewed authority identity = PASS;
- EPRL `gamma`-duality/parity coupling scope = PASS;
- semiclassical EFT parameter-to-observable route = PASS;
- fail-closed complete-stack transport scope guard = PASS;
- complete-stack same-realization UV→IR transport = false;
- normalized observable with full propagated QG error = false;
- family terminal = false;
- D7 authorized = false.

Classification:
`HIGH_VALUE_LQG_GAMMA_DUALITY_SEMICLASSICAL_OBSERVABLE_PARAMETER_BRIDGE__NO_COMPLETE_STACK_SAME_REALIZATION_UV_TO_IR_TRANSPORT`

LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS. The new authority removes an obsolete sub-blocker (“no semiclassical gamma observable”) but does not supply the terminal bridge.
Canonical blocker remains, sharpened to:
`BLOCKED_MISSING_CAUSAL_VERTEX_LIFT_THROUGH_HAN_COMPLETE_STACK_SUM_FACE_MULTIPLICITIES_AND_LAMBDA_F_WEIGHTS_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`

### Iter292 — external refinement-flow authority
Primary object: Tamburini, *ER = EPR in Loop Quantum Gravity: the Immirzi Parameter and the Continuum Limit*, arXiv:2508.18324v2 (2025). Public preprint; no peer-reviewed journal version located in the Iter292 authority check.
Scientific run `34575046143`: four independent guards in parallel + aggregate SUCCESS on head `eb6ba509773ac50697b4c6c683b2f3638ea7ad71`.
Summary artifact `10189283134`; artifact digest `sha256:3dfa5deb1bab46bfcb7c32f199969dcc8a1588a69937d408483ff202a48002f5`.

Raw aggregate:
- public preprint identity = PASS;
- explicit refinement-renormalization / conditional regulator-independent continuum claim = PASS;
- explicit equivalence map to active Han complete-stack = false;
- continuous `gamma` / stack-coupling / spin-scale transport to Iter290 = false;
- normalized same-realization observable/comparator/error certificate = false;
- family terminal = false;
- D7 authorized = false.

Classification:
`HIGH_VALUE_EXTERNAL_REFINEMENT_FLOW_AUTHORITY__NO_EXPLICIT_EQUIVALENCE_TO_THE_ACTIVE_COMPLETE_STACK_OR_CAUSAL_REGGE_CHAIN`

This removes only the weak sub-blocker that no explicit LQG refinement-flow proposal exists. The decisive family-scope blocker remains the same-realization/equivalence transport into the active complete-stack + causal-Regge chain.

### Iter293 — generalized EPRL-KKL causal scope
Primary object: Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026), public preprint.
Scientific run `34584685590`: four independent guards in parallel + aggregate SUCCESS on head `3edcaf9feb3a308750fd6a84a25056f9f105c61d`.
Summary artifact `10193076711`; artifact digest `sha256:d14df68d7b1c98464bacd38644d75271ab5c75745e75bf69c6a6d048bc04cd42`; raw summary digest `sha256:a0521f16d90f393376d7899556a3c452123025baa172f1248f7bcbad6eb1b277`.

Aggregate:
- public-preprint authority identity = PASS;
- generalized EPRL-KKL arbitrary-2-complex causal structure / orientation consistency = PASS;
- causal vertex generalizing Bianchi–Chen–Gamonal plus semiclassical asymptotic analysis = PASS;
- explicit Han-stack equivalence = false;
- complete-stack same-realization UV→IR transport = false;
- normalized observable/comparator/error certificate = false;
- family terminal = false;
- D7 authorized = false.

Classification:
`HIGH_VALUE_GENERALIZED_EPRL_KKL_CAUSAL_SCOPE_EXTENSION__NO_COMPLETE_STACK_EQUIVALENCE_OR_UV_TO_IR_TRANSPORT`

Interpretation: the Iter290 causal endpoint is no longer confined to a single simplicial EPRL-vertex construction; a generalized EPRL-KKL causal framework on arbitrary 2-complexes exists. This is a meaningful scope extension, but it does not establish identity with the active Han stack or close the decisive UV→IR transport blocker.

### Iter295 — Han-stack / generalized causal EPRL-KKL conditional overlap
Authorities: Han, PRD 113, 084034 (2026), and Beltrán, arXiv:2603.22661v2 (2026).
Scientific run `34592425741`: 4/4 independent guards + aggregate SUCCESS on head `300159ee62c096aeaff766658169be5d5fea83fe`.
Methodology `34592425770`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
Summary artifact `10196164627`; artifact digest `sha256:5ac870b2e59d0717913042bc2a0eb809e650c24bcc4c0ca7ad0facf929eeef70`; raw summary digest `sha256:55b371ffda6542839d1cdfc92b07196e207e4b4b83253d00142ed35d7bf86eb6`.

Aggregate:
- shared generalized EPRL-KKL per-complex formalism = PASS;
- conditional common domain nonempty = PASS;
- exact K5 witness = PASS: 5 nodes, 10 links, GF(2) rank 4, kernel dimension 1, all one/two-link cuts connected;
- universal Han-stack inclusion in Beltrán working domain = false;
- causal-vertex lift through Han complete stack sum = false;
- `lambda_f` / face-multiplicity transport = false;
- complete-stack same-realization UV→IR transport = false;
- normalized observable/comparator/error = false;
- family terminal = false; D7 authorized = false.

Classification:
`PASS_SCOPED_CONDITIONAL_GENERALIZED_EPRL_KKL_DOMAIN_OVERLAP_WITH_EXPLICIT_K5_CAUSAL_WITNESS__NO_HAN_STACK_SUM_LIFT_OR_SAME_REALIZATION_UV_TO_IR_TRANSPORT`

Interpretation: the frameworks are no longer merely adjacent. A concrete admissible per-complex overlap exists. The decisive missing object is now the lift of the causal prescription through the complete Han stack sum and the subsequent physical same-realization transport to causal Regge/GR observables.

Refined blocker:
`BLOCKED_MISSING_CAUSAL_VERTEX_LIFT_THROUGH_HAN_COMPLETE_STACK_SUM_FACE_MULTIPLICITIES_AND_LAMBDA_F_WEIGHTS_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`

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

### Iter294 — geometric Lorentzian Einstein endpoint / correction hierarchy
Primary object: Finster–Krpoun, *A Geometric Derivation of the Einstein Equations from the Causal Action Principle*, arXiv:2607.13871v1 (2026), public preprint.
Scientific run `34585821754`: four independent guards in parallel + aggregate SUCCESS on head `9d821ea02aae8a85c093cec27ecffb120250d6b7`.
Methodology run `34585821764`: SUCCESS.
Summary artifact `10193537053`; artifact digest `sha256:996064f831648b6f2a5e788b3e8f63f20f7a0213a13422d65d085676cd61439b`; raw summary digest `sha256:89a2f8b287d637b7d2ae664bfe84d4abd0e27b254d99adf5c353c72677343902`.

Aggregate:
- explicit Lorentzian 4D Einstein endpoint from causal action = PASS;
- explicit symmetric/divergence-free energy-momentum tensor = PASS;
- leading `T_ij = O(delta^2)` and gravitational-coupling/regularization-length scaling contract = PASS;
- systematic correction hierarchy = PASS;
- concrete evaluated normalized beyond-Einstein correction tensor/residual = false;
- same-domain comparator residual = false;
- family terminal = false;
- D7 authorized = false.

Classification:
`HIGH_VALUE_CFS_GEOMETRIC_LORENTZIAN_EINSTEIN_DERIVATION_AND_SYSTEMATIC_CORRECTION_HIERARCHY__CONCRETE_NORMALIZED_BEYOND_EINSTEIN_RESIDUAL_COMPARATOR_STILL_MISSING`

Interpretation: the obsolete weak sub-blocker "rank-two Einstein structure is only prospective" is removed. The decisive CFS blocker is now narrower: evaluate at least one explicit beyond-Einstein correction from the stated hierarchy into a normalized same-domain gravity observable/residual with comparator and propagated uncertainty.

## Other priority fronts
- Asymptotic Safety: stable public contact-complete Lorentzian `s+t+u+A4` package remains decisive external object.
- RQCP: all-band/background-independent autonomy plus Hilbert-cutoff/resource closure remains open.
- Other Tier-1 families reopen only on genuinely new status-changing authority/computation/reduction objects.

## Publication handoff
`recovery/PUBLICATION_IMPACT_LEDGER.md` is authoritative.
- Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`; Iter278–295 = `NOT_NEEDED` as additional rules except where already stated.
- Paper IV: Iter277–295 = `READY` with stated claim boundaries.

## Anti-idle compute policy
Whenever scientifically meaningful, nonduplicating tasks are independent, launch them immediately in parallel (`fail-fast:false`, highest safe practical runner parallelism). Dependent classification/aggregate stages wait behind explicit barriers. When runners are saturated, queue additional useful independent jobs rather than suppressing them. Never repeat saturated or duplicate calculations merely to manufacture activity. The active KMQGB auto-research automation is configured with the same mandatory rule.

## Exact next gate
`D7_S2_LQG_CAUSAL_LIFT_THROUGH_COMPLETE_STACK_AND_SAME_REALIZATION_UV_TO_REGGE_GR_TRANSPORT_CERTIFICATE`

Priority:
1. seek/compute an explicit lift of the generalized causal EPRL-KKL prescription through Han's complete face-multiplicity/`lambda_f` stack sum, then a same-realization stack-coupling/`gamma`/spin-scale transport from the Iter287 UV/entropy sector through Iter291 to the Iter290 causal Regge/Einstein endpoint with normalized observable/comparator/error transport;
2. evaluate an explicit CFS beyond-Einstein correction from the Iter294 hierarchy into a normalized same-domain gravity observable/residual with comparator and propagated uncertainty;
3. stable public AS contact-complete `s+t+u+A4`;
4. RQCP all-band/background-independent autonomy bridge;
5. other Tier-1 authority only when materially status-changing.
