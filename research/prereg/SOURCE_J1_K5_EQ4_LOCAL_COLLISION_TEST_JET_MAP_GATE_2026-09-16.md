# SOURCE_J1_K5_EQ4_LOCAL_COLLISION_TEST_JET_MAP — prospective freeze

Date: 2026-09-16
Status: PROSPECTIVELY_FROZEN_BEFORE_SUBSTANTIVE_SOURCE_MAP_RESULT

## HYPOTHESIS

For the same repaired highest-contact triangle realization used by terminal V8/V11, the actual source-defined Eq. (3)/(7) Toller data entering the physical Eq. (4) boundary amplitude may either determine a same-realization local collision chart and smooth remainder/test factor sufficiently to construct its complete local jet through total order 7, or may leave one or more required map fields source-underdetermined. Missing map data are BLOCKED, never zero.

## EXACT OBJECT

One source-faithful finite-i-epsilon Eq. (4) realization of arXiv:2601.23162v1, restricted to the same local highest-contact triangle collision object underlying terminal V8. The required output object is a source-authorized map from the physical Eq. (4) smooth remainder/test factor to local triangle coordinates `(x,y)` together with all derivatives needed to evaluate the eight terminal V8 invariant collision jets through total derivative order 7.

This gate constructs/audits the map only. It does not compute the physical action rank of the six V8 null directions.

## DEPENDENCY

- Terminal V8 counterterm-equivalence object: 8 invariant jets, rank 2, augmented rank 2, affine nullity 6.
- Terminal V10 primary-source audit: full primary sources do not supply a simultaneous-contact extension/finite-normalization selector.
- Terminal V11 physical-observable quotient gate: `PHYSICAL_OBSERVABLE_QUOTIENT_MAP_BLOCKED_SCOPED`, with `nullspace_action_rank = null`, explicitly localizing the blocker to the absent same-realization local collision/test-jet map.

## SOURCE / REALIZATION AUTHORITY

Frozen before substantive map extraction in `inputs/source_j1_k5_eq4_local_collision_test_jet_map_authority.json`:

- current main at freeze `960f30d276100d7cbfecc141f0c14e0b30bf7956`;
- terminal V11 result and authority ledger;
- terminal V8 canonical object;
- arXiv:2601.23162v1 causal-vertex structured snapshot and immutable full-primary PDF digest `cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713`;
- arXiv:2604.24945v1 Toller/Cartan full-primary PDF digest `f37659f5cb4674dd0c1b81a6e55f5d1dfd992c60b0e85cb2859322b860e22046` as auxiliary Toller authority only where same-realization mapping is explicit;
- terminal Iter453 only as a negative scope lock: its tensors are synthetic and cannot supply the physical map.

## FROZEN INPUTS / REQUIRED MAP FIELDS

A terminal validated map requires all of the following to be source-authorized and mutually consistent:

1. `EQ4_PARENT_IDENTITY`: exact Eq. (4) boundary-amplitude identity/version and contraction identity.
2. `TOLLER_INSERTION_IDENTITY`: explicit Eq. (3)/(7)-to-Eq. (4) insertion/variable/index relation for the same physical realization.
3. `LOCAL_COLLISION_CHART`: explicit local coordinates or an exact invertible map to the repaired triangle contact coordinates `(x,y)` with the three contact forms identified.
4. `SMOOTH_REMAINDER_OBJECT`: explicit source-defined smooth factor remaining after isolating the three highest-contact singular factors.
5. `PARAMETER_NORMALIZATION_LOCK`: all parameters, finite-i-epsilon prescription, normalization factors, magnetic/intertwiner contraction identity, and channel/source realization needed to identify that smooth factor.
6. `JET_ORDER_7_COMPLETENESS`: exact analytic expression or source-authorized derivative data sufficient to determine every derivative needed by the eight V8 invariant jets through total order 7.
7. `PERMUTATION_COORDINATE_CONSISTENCY`: chart and jet mapping preserve the frozen triangle permutation/source identity.

No missing field may be imputed, fitted, replaced by a synthetic tensor, Gaussian regulator test, arbitrary polynomial test, or set to zero.

## POSITIVE CONTROLS

1. Immutable source/blob/digest locks reproduce exactly.
2. Terminal V8 basis/nullspace/object digest locks reproduce exactly.
3. Terminal V11 map-blocker state reproduces before attempting the new construction.
4. A synthetic *control-only* complete map fixture with an explicit polynomial smooth remainder of degree <=7 must produce the exact known order-7 jet and classify the map machinery as constructible; its values are forbidden from the substantive result.
5. An exact coordinate-change fixture with a known invertible linear triangle chart must preserve the corresponding jet under symbolic chain-rule transport.
6. Lower-order derivative fixtures (orders 0,1,2) must match direct symbolic differentiation.

## NEGATIVE / ADVERSARIAL CONTROLS

1. A fixture missing any one required map field must classify BLOCKED, never infer zero derivatives.
2. A noninvertible/wrong collision chart must classify INVALID.
3. Synthetic Iter453 tensors must be rejected as substantive physical-map authority.
4. A wrong source/version/digest or source/channel mismatch must classify INVALID.
5. A complete but contradictory pair of source-authorized map statements must classify `EQ4_LOCAL_COLLISION_TEST_JET_MAP_SOURCE_INCONSISTENT_SCOPED`, not silently choose one.
6. A numerically evaluable but precision-unstable derivative construction must classify numerical-method BLOCKED rather than scientific FAIL.

## PASS

`EQ4_LOCAL_COLLISION_TEST_JET_MAP_CONSTRUCTED_SCOPED` iff all required map fields are source-authorized, same-realization identity is preserved, the complete order-7 jet is exactly or controlled-numerically constructed, and all positive/negative controls pass.

## BLOCKED

`EQ4_LOCAL_COLLISION_TEST_JET_MAP_SOURCE_BLOCKED_SCOPED` iff source/object locks pass but one or more required source map fields are absent or insufficiently explicit.

`EQ4_LOCAL_COLLISION_TEST_JET_MAP_NUMERICAL_METHOD_BLOCKED_SCOPED` iff the source map is complete enough in principle but the frozen numerical derivative/conditioning criteria fail.

## FAIL / INCONSISTENT / INVALID

`EQ4_LOCAL_COLLISION_TEST_JET_MAP_SOURCE_INCONSISTENT_SCOPED` iff same-realization source-authorized statements provide mutually inconsistent required map data under the frozen identity locks.

No model/science FAIL is authorized merely by missing map data.

`INVALID_IMPLEMENTATION` for wrong source/version/object, wrong chart identity, synthetic substantive substitution, failed exact fixtures, failed immutable locks, or post-hoc changes to this contract.

## INTERPRETATION CEILING

A PASS authorizes only later use of the constructed local test-jet map in a separately frozen physical-observable nullspace-action/rank gate. BLOCKED is a source/object availability statement, not physical zero action. This gate does not establish a physical quotient, distributional existence/nonexistence, full-K5/model/family failure, D7 closure, any terminal selector, or Candidate Gravity activation. RQIR Core v1.0 remains FROZEN.
