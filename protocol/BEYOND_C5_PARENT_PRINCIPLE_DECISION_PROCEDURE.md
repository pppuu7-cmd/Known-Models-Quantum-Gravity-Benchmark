# Beyond-C5 Parent-Principle Decision Procedure

**Status:** permanent fail-closed methodology authority  
**Introduced:** KMQGB Iter178  
**Purpose:** close the operational gap between the Beyond-C5 escape taxonomy, parent-principle search, candidate promotion gates, same-realization composition, residual geometry, predictive holdout and compute/publication authorization.

This procedure evaluates a proposal. It does not create a physical theory and does not convert missing derivations into PASS.

## 1. Inputs

A prospective parent proposal must supply a record containing at least:

- explicit parent object or constructive microscopic rule;
- declared physical domain and approximation regime;
- finite parameter / primitive list and selection law;
- at least one escape door `E1..E5`;
- the exact claim by which full matched C5 is supposedly escaped;
- same-realization provenance identifiers for every object intended to be composed;
- required observable/response blocks;
- comparator registry and common-domain definition;
- intended cross-order / cross-representation / cross-background holdout;
- compute authorization state;
- publication-claim state.

Absence is represented explicitly as `BLOCKED`, never by a guessed value.

## 2. Decision state vocabulary

Allowed methodological outcomes are:

- `PASS`: obligation explicitly satisfied with evidence;
- `BLOCKED`: required object is missing or not yet derivable;
- `FAIL`: supplied object contradicts a required consistency/comparator criterion;
- `N_A`: obligation demonstrably does not apply, with reason.

A proposal is scientifically allowed to remain BLOCKED indefinitely. `BLOCKED` is not evidence that new physics is required.

## 3. Stage P0 — freeze the realization vector

Define a realization vector

`R = {parent, state, boundary data, gauge, regulator, truncation, signature, normalization, scale convention, source/detector routing}`.

Every later ingredient must either share the same `R` or carry an explicit map

`M: R_a -> R_b`

with uncertainty propagation.

### Stop

If two ingredients merely share a framework name, author group or symbol but no identical realization or explicit map exists:

`BLOCKED_CROSS_AUTHORITY_COMPOSITION_NOT_YET_SAME_REALIZATION`.

No observable combination, parameter identity or likelihood composition is allowed downstream.

## 4. Stage P1 — explicit parent and upstream primitive closure

Freeze one parent object: action, Hamiltonian, amplitude-generating rule, path integral, causal action, transfer rule, CTP/influence functional or comparably constructive object.

For each load-bearing upstream primitive classify selection as:

- `DERIVED`;
- `FUNDAMENTAL_FINITE_CONSTANT`;
- `EXTERNAL_INPUT`;
- `BLOCKED`.

### Pass requirement

All load-bearing primitives used for a novelty claim must be derived or finite fundamental constants, or else their external-input nature must remove them from the claimed prediction.

### Stop

No explicit parent -> `BLOCKED_NO_PARENT_OBJECT`.

Arbitrary load-bearing external input -> `BLOCKED_UPSTREAM_PRIMITIVE_FREEDOM`.

## 5. Stage P2 — functional-freedom test

For a constraint set `P`, define the hard-deformation null space

`N_P(D)`

at increasing hard/EFT basis cutoff `D`, and track

`FF_D = dim N_P(D)`.

Classify:

- `FINITE`: bounded finite freedom with explicit bound;
- `SATURATED`: dimension becomes constant after a demonstrated cutoff and the remaining parameters are parent-fixed;
- `GROWING`: freedom grows with `D`;
- `UNKNOWN`: calculation not complete.

### Stop

`GROWING` -> `FUNCTIONAL_FREEDOM_BLOCKED`.

`UNKNOWN` -> `BLOCKED_FUNCTIONAL_FREEDOM_AUDIT`.

Only `FINITE` or `SATURATED` may proceed toward promotion.

## 6. Stage P3 — escape-door taxes

Use `protocol/BEYOND_C5_ESCAPE_TAXONOMY.md`.

For every declared door, all door-specific taxes remain cumulative.

### E1 nonlocal/nonanalytic

Require ordinary massless-loop quotient, on-shell/field-redefinition audit, parent-fixed form factor, retarded/causal construction and same-domain nonlocal comparator.

### E2 extra propagating sector

Require C4/modified-gravity quotient, ghost/tachyon/positivity audit and a gravity-attribution theorem rather than ordinary-force attribution.

### E3 nonperturbative/transseries

Require parent-derived weight/phase, Lorentzian observable continuation, state/topology quotient and a controlled measurable regime.

### E4 modified quantum/open law

Require separation from ordinary reduced dynamics, complete positivity/reality/energy-momentum consistency, no-signalling and generic-bath/CQ quotient.

### E5 modified symmetry/causal/kinematic structure

Require observed-limit recovery, constraint/DOF closure, relational/QRF audit, phenomenological bounds and causal consistency.

### Stop

A declared door with any mandatory tax missing remains `BLOCKED_DOOR_TAX_INCOMPLETE`.

A feature entirely reproduced by an existing comparator yields `COMPARATOR_CONTAINED_PRE_P4` or later `FAIL_COMPARATOR_CONTAINED`, not novelty.

## 7. Stage P4 — first derived rigid relation

Require at least one normalized nontrivial relation derived from the same parent, such as:

- hard four-/higher-point relation;
- spectral/retarded relation;
- cross-order coefficient relation;
- cross-representation shared-parameter relation;
- multiscale RG consistency relation.

The relation must state parameter incidence, conventions, approximation order and evidence path.

### Stop

No derived relation -> `BLOCKED_PARENT_HAS_NO_RIGID_PREDICTION`.

Independent free coefficient for every effect -> return to P2 and normally classify functional-freedom failure.

## 8. Stage P5 — response completeness and physical reduction

Generate every required same-parent response family and close:

- Ward/gauge identities;
- contact/seagull terms;
- conservation/Bianchi identities;
- physical-DOF reduction;
- normalization/signature/phase/routing conventions;
- repeated/coincident poles when applicable;
- causal/CTP prescription when applicable.

### Stop

Missing required family -> `BLOCKED_RESPONSE_INCOMPLETE`.

Ambiguity that changes the observable -> `BLOCKED_PHYSICAL_REDUCTION`.

Never zero-fill an unsupported term.

## 9. Stage P6 — common-domain comparator quotient

Freeze identical observable, order, state, background, routing and contact/amputation conventions for proposal and comparator union.

Profile every applicable C0-C6/full-C5 comparator and stronger benchmark-discovered comparator.

### Stop

If the proposed signal is reproduced after full same-domain profiling -> `FAIL_COMPARATOR_CONTAINED`.

If the comparator is not complete on the same domain -> `BLOCKED_COMPARATOR_DOMAIN`.

## 10. Stage P7 — local and global residual tests

Local test:

`COR = Pi_perp Sigma^(-1/2) r`.

A nonzero COR is necessary but not sufficient.

Then perform finite global/nonlinear profiling of the comparator manifold with preregistered tolerance and adversarial/boundary checks.

### Stop

`COR = 0` -> `FAIL_LOCALLY_ABSORBED`.

Finite comparator point absorbs the proposal -> `FAIL_GLOBALLY_ABSORBED`.

Incomplete covariance/Jacobian/domain -> `BLOCKED_RESIDUAL_OBJECT`.

## 11. Stage P8 — identifiability and shared-parameter rigidity

Stack orders, representations and backgrounds while keeping genuinely shared parameters shared.

Use projected singular values and shared-parameter rank deficit. Require at least one pre-registered holdout not used for fitting.

### Stop

Rank-saturated / structurally degenerate observable set -> `BLOCKED_IDENTIFIABILITY` unless an independent channel is derived.

Retuning shared parent parameters on holdout -> `FAIL_HOLDOUT_RETUNED`.

Each new block demanding a new arbitrary parameter -> return to P2.

## 12. Stage P9 — multiscale / RG transport when scales differ

If two claimed observables live at different scales, derive a common-scale transport object before composition.

For the current O-LQG gamma route, for example, the frozen observable relation is

`Delta_gamma = 2 cot(8 psi) - q`

only after common-scale transport, with

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`.

This example illustrates the general rule: a UV/primordial and an IR/detector observable cannot be combined by silently identifying running parameters.

### Stop

Missing same-realization RG/matching map -> `BLOCKED_MULTISCALE_TRANSPORT`.

## 13. Stage P10 — compute authorization

Classify the active blocker:

- `STRUCTURAL`: parent/provenance/same-realization/normalization/identity/analytic derivation missing;
- `NUMERICAL`: frozen equations exist and numerical evaluation can change a terminal classification;
- `STATISTICAL`: physical object is frozen and resource/likelihood analysis is now discriminating.

Heavy compute is allowed only for `NUMERICAL` or `STATISTICAL` blockers with:

- frozen input refs;
- preregistered success/fail thresholds;
- named output artifact;
- duplicate-run authority rule.

Structural blocker + heavy compute request -> `DENY_HEAVY_COMPUTE_STRUCTURAL_BLOCKER`.

## 14. Stage P11 — publication-claim authorization

Every article-facing statement must be assigned one of:

- `ESTABLISHED_EXTERNAL`;
- `DERIVED_KMQGB`;
- `REPRODUCED_EXECUTABLE`;
- `OPEN_BLOCKED`;
- `HYPOTHESIS_ONLY`;
- `FORBIDDEN_OVERCLAIM`.

Examples of forbidden transformations:

- `BLOCKED` -> “known model excluded”;
- repository R1/R2 = 100 -> “quantum gravity solved”;
- nonzero local COR -> “new physics discovered”;
- adjacent papers sharing `gamma` -> “same renormalized parameter proven”;
- conference existence claim -> “stable reproducible amplitude package”.

## 15. Promotion theorem for the workflow

A Candidate Gravity ansatz may be promoted only if:

- P0 same-realization provenance is PASS;
- P1 parent/primitives are closed;
- P2 freedom is FINITE/SATURATED;
- all declared P3 escape taxes PASS;
- P4 rigid derived relation exists;
- P5 response/physical reduction PASS;
- P6 complete comparator quotient PASS;
- P7 robust global residual survives;
- P8 identifiability/rigidity/holdout PASS;
- P9 multiscale transport PASS where applicable;
- no mandatory G0-G10 promotion gate is non-PASS.

Only after that may Fisher/resources be promoted.

## 16. Operational decision chain

`idea`

`-> same realization/provenance?`

`-> explicit parent + closed upstream primitives?`

`-> finite/saturated functional freedom?`

`-> all escape-door taxes paid?`

`-> rigid normalized prediction derived?`

`-> complete response + physical reduction?`

`-> same-domain full comparator quotient?`

`-> local residual? -> global residual?`

`-> identifiable / shared-parameter rigid / holdout?`

`-> RG/common-scale transport if needed?`

`-> compute authorization?`

`-> publication claim authorization?`

`-> promotion only after all mandatory obligations PASS`.

This chain is the complete Beyond-C5 parent-principle methodology for repository-readiness accounting. It deliberately leaves physical proposals BLOCKED when nature/the literature has not supplied the required object.