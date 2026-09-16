# SOURCE_J1_K5_EQ4_TRIPLE_CONTACT_LOCAL_CHART_DERIVATION_GATE — prospective freeze

Date: 2026-09-16
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT

## HYPOTHESIS

For one fixed Eq. (4) wedge triangle `(12,23,13)`, the currently durable source-authorized Eq. (4) gauge-fixed parent variables plus the source one-wedge contact/Toller primitives may or may not be sufficient to DERIVE, without adding a new physical or coordinate-identification assumption, a common two-dimensional simultaneous-contact local chart. The gate must distinguish a genuinely source-derived chart from a rank-deficient explicit chart, a missing joint source object, and an invalid implementation.

## exact OBJECT

Exactly one same-realization local-chart question for the Eq. (4) triangle with wedge labels `12`, `23`, `13`.

The required derived object is a common local coordinate tuple `q=(q1,q2)` near one simultaneous collision point together with explicit source-authorized mappings

`B12(q), B23(q), B13(q)`,

such that the differential map has rank 2 at the collision. The chart must also carry the source measure/Jacobian normalization transport needed to compare contact distributions and an explicit S3 permutation action/transport on the same local coordinates/contact functions.

The historical V8 auxiliary coordinates `B12=x, B23=y, B13=x+y` are a BRIDGE TARGET ONLY. They are not promoted to source authority by this gate and may not be inserted as a production premise.

## DEPENDENCY

- terminal V13/V12 primary-source map-expansion result `EQ4_LOCAL_COLLISION_PRIMARY_SOURCE_MAP_AUTHORITY_BLOCKED_SCOPED` on current main;
- Eq. (4) causal-vertex parent and gauge fixing from frozen primary-source record `arXiv:2601.23162v1`;
- Appendix-D one-wedge contact argument/distribution from the same source;
- one-group Cartan/Toller reconstruction and one-wedge symmetries from frozen primary-source record `arXiv:2604.24945v1`;
- historical V8 auxiliary triangle only as the downstream bridge target.

## SOURCE/REALIZATION AUTHORITY

Only the prospectively committed authority ledger `inputs/source_j1_k5_eq4_triple_contact_local_chart_derivation_authority.json` and the immutable repository objects it locks are authoritative for this gate. No web source, synthetic production substitution, or unstated coordinate relation may enter the scientific decision.

The ledger locks:

- `sources/arxiv_2601_23162v1_eq4_local_collision_map_expansion_v13.json`, blob `fdfb13f9974ebc891cb3f490ca553dd0991d9136`, PDF SHA256 `cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713`;
- `sources/arxiv_2604_24945v1_eq4_local_collision_map_expansion_v13.json`, blob `c742e8cab0648b8fbaef88f09876644c6c2c3077`, PDF SHA256 `f37659f5cb4674dd0c1b81a6e55f5d1dfd992c60b0e85cb2859322b860e22046`;
- current terminal source-map expansion commit `115a33f7d131198d600c036d6d0df44079d0c723`.

## FROZEN INPUTS

Required chart fields, all conjunctive:

1. `COMMON_LOCAL_COORDINATES`: one common local coordinate tuple for all three contacts at one collision point;
2. `THREE_CONTACT_MAPS`: explicit mappings for `B12`, `B23`, `B13` on those common coordinates;
3. `RANK_TRANSVERSALITY`: exact differential/Jacobian rank 2 at the collision;
4. `JACOBIAN_NORMALIZATION_TRANSPORT`: explicit source-authorized measure/contact normalization transport under the chart;
5. `S3_COORDINATE_TRANSPORT`: explicit permutation action or equivalent coordinate/contact transport on the same chart.

A one-wedge contact function, one-group Cartan chart, parent gauge fixing, label symmetry, or representation-index symmetry does not satisfy these fields by itself. Missing object is not zero data.

## POSITIVE CONTROLS

1. Synthetic shared-chart fixture `B12=u`, `B23=v`, `B13=u+v`, with explicit identity Jacobian/normalization and the standard S3 transport, must classify as a constructed rank-2 chart.
2. An invertible rational change of local basis must preserve chart derivability and rank 2.
3. Locked source-record blob/PDF identities and parent terminal commit must match exactly.

## NEGATIVE CONTROLS

1. Three disjoint one-wedge variables with no source map to one common coordinate tuple must classify BLOCKED, not FAIL and not zero rank.
2. A fully explicit common-coordinate fixture with `B12=u`, `B23=2u`, `B13=3u` must expose rank deficiency and classify FAIL_SCOPED.
3. A rank-2 shared chart lacking normalization or S3 transport must classify BLOCKED/PARTIAL, not PASS.
4. Wrong source blob/PDF identity, historical V8 target inserted as source authority, or post-hoc frozen-contract change is `INVALID_IMPLEMENTATION`.

## PASS

`EQ4_TRIPLE_CONTACT_LOCAL_CHART_DERIVED_SCOPED` iff all five required chart fields are source-authorized/derived, the exact contact differential has rank 2, normalization transport and S3 coordinate transport are explicit, and all controls pass.

## FAIL

`EQ4_TRIPLE_CONTACT_LOCAL_CHART_TRANSVERSALITY_FAIL_SCOPED` iff a complete source-authorized common chart and transports are explicit but its exact three-contact differential has rank <2 or the explicit source mappings are algebraically inconsistent. This is a scoped local-chart failure only.

## BLOCKED / INVALID

`EQ4_TRIPLE_CONTACT_LOCAL_CHART_DERIVATION_BLOCKED_SCOPED` iff source/object controls pass but one or more required common-chart/mapping/normalization/permutation objects are not derivable from the frozen authority. Missing relations remain missing; their rank/action is undefined, not zero.

`INVALID_IMPLEMENTATION` for authority mismatch, wrong realization/triangle, synthetic production substitution, V8 bridge target promoted to authority, control failure, or post-hoc criterion change.

## INTERPRETATION CEILING

PASS establishes only a same-realization simultaneous-contact local chart for the fixed Eq. (4) triangle. FAIL is only a local-chart transversality/consistency result. BLOCKED is only missing derivation authority. No outcome establishes the smooth Eq. (4) remainder, complete order-7 jet, V8 physical nullspace-action rank/quotient, distributional existence/nonexistence, full-K5/model/family failure, D7 closure/selector, or Candidate Gravity.
