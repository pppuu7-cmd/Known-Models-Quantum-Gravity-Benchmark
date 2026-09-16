# SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_GATE — prospective freeze

Date: 2026-09-16
Status: PROSPECTIVELY_FROZEN_BEFORE_OUTCOME_SENSITIVE_SOURCE_EXTRACTION

## PURPOSE

Determine only whether the already-frozen primary authority explicitly defines the exact group argument used for each Eq. (4) triangle wedge `12`, `23`, `13` in one compatible same-realization convention. This is an object-identity gate. It does not compute a contact rank or infer transversality.

## PARENT

- Fresh main parent terminal: `SOURCE_J1_K5_EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_GATE`.
- Parent terminal commit: `48f59aa10203903b494bd33edb5e498be24bb24f`.
- Parent classification: `EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_BLOCKED_SCOPED` (BLOCKED, not FAIL).
- Target triangle is frozen exactly as ordered tuple `(12,23,13)`.

## ALLOWED PRIMARY AUTHORITY

Outcome-sensitive extraction is restricted to the following already-frozen primary records and their exact locked PDF versions:

1. `arXiv:2601.23162v1`, PDF SHA256 `cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713`, durable audit record `sources/arxiv_2601_23162v1_eq4_local_collision_map_expansion_v13.json`, blob `fdfb13f9974ebc891cb3f490ca553dd0991d9136`.
2. `arXiv:2604.24945v1`, PDF SHA256 `f37659f5cb4674dd0c1b81a6e55f5d1dfd992c60b0e85cb2859322b860e22046`, durable audit record `sources/arxiv_2604_24945v1_eq4_local_collision_map_expansion_v13.json`, blob `c742e8cab0648b8fbaef88f09876644c6c2c3077`.

No textbook reconstruction, generic group law, later version, unrelated paper, historical V8 auxiliary chart, or Toller-matrix representation composition may substitute for an absent identity. Any later authority escalation requires a new prospective gate.

## FROZEN IDENTITY GAUGE

The Eq. (4) realization is the source's gauge-fixed four-SL(2,C)-integration representation after fixing `g1` to the identity, exactly as locked by the primary source record. Variables belonging to representation labels, magnetic indices, Toller branch labels, Cartan decomposition coordinates, integration group variables, and wedge/contact scalar arguments are distinct object types unless the primary source explicitly identifies them.

## REQUIRED LEDGER FIELDS

For every wedge `ij` in `(12,23,13)`, freeze a machine-readable record with:

1. `wedge`;
2. source-defined integration variables entering the wedge factor;
3. exact multiplication order for `Gij`;
4. every inversion explicitly present;
5. orientation convention / ordered endpoint convention;
6. left/right action convention if material to the argument;
7. exact group element passed to the one-wedge contact scalar/distribution `B(z,g)` or equivalent source-defined one-wedge contact object;
8. exact primary citation location (page/section/equation or verbatim-symbol location);
9. provenance source ID and locked hash;
10. whether any equality is literal or only equivalent under dummy integration-variable renaming.

## DUMMY-VARIABLE EQUIVALENCE

Dummy-variable renaming is allowed only when it is a bijective renaming of integrated variables within the same source realization and leaves multiplication order, inversions, wedge orientation and the contact-scalar input unchanged after explicit substitution. Cyclic permutation, inversion, reorientation, left/right exchange, conjugation or use of a generic group identity is not treated as dummy renaming unless explicitly source-authorized.

## FROZEN ORIENTATION / ORDER RULE

No orientation, inversion or multiplication order is supplied by convention. If the source writes a wedge argument explicitly, that literal order is authoritative. If it does not, the field is `null`. Missing is never replaced by identity, inverse, zero, or a guessed conventional choice.

## PASS

`EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_PASS_SCOPED` iff all three wedges `12`, `23`, `13` have source-authoritative exact group arguments in one compatible same-realization convention, with multiplication order, inversions, orientation and contact-scalar input all pinned, and all provenance/identity controls pass.

## BLOCKED

`EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_BLOCKED_SCOPED` iff provenance controls pass but at least one essential required identity field for any of the three wedges is absent from the allowed primary authority. BLOCKED records the minimal missing authority object(s); it is not a physical or transversality FAIL.

## INVALID

`INVALID_IMPLEMENTATION` iff production requires any guessed textbook formula, unstated orientation/inversion/multiplication convention, historical V8 auxiliary relation (`B12=x`, `B23=y`, `B13=x+y`), Toller representation composition as a group-variable law, wrong source version/hash, non-bijective relabeling disguised as dummy renaming, post-hoc criteria mutation, or consumption of nonterminal artifacts.

## CONTROLS

Positive fixtures:

1. Three explicit literal maps on a synthetic same-realization tuple with order/inversions/orientation/contact arguments fully specified must PASS.
2. A pure bijective dummy-variable renaming that preserves the literal maps after substitution must remain PASS and produce an equivalent normalized ledger.

Negative fixtures:

1. Two explicit wedge maps plus one missing map must BLOCK with the missing wedge named and no rank value.
2. Three generic textbook-looking maps without primary citations must INVALID.
3. A map differing only by an unlicensed inversion or multiplication-order reversal must INVALID rather than be normalized away.
4. Historical V8 `x,y,x+y` injection must INVALID.
5. Replacing missing group argument by a Toller-matrix composition identity must INVALID.

## OUTCOME CEILING

PASS authorizes only construction of a later prospectively frozen common-local-Lie pullback/transverse-rank gate. BLOCKED authorizes only an authority-escalation gate for the minimal missing source object. No outcome here establishes rank deficiency, physical quotient degeneracy, smooth Eq. (4) remainder, order-7 jet, distributional existence/nonexistence, K5/model/family failure, D7 closure, selector status, Candidate Gravity activation, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, or `NEW_PHYSICS_FOUND`.

Governance locks remain: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selector labels remain unauthorized; Candidate Gravity inactive.
