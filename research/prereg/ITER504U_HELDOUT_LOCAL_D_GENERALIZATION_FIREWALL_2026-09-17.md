# ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL — prospective freeze

Date: 2026-09-17
Status: `PROSPECTIVELY_FROZEN_BEFORE_HELDOUT_IMPLEMENTATION_OR_OUTPUT`

## Purpose

Test whether the validated Iter504T local-derivative enclosure repair generalizes beyond its development cohort without refit, before any full Iter504-domain campaign is authorized.

This gate is required by the already-frozen outcome-blind successor toolkit, commit `81e0e94649a50cccc510dc2630456af45fd98e46`, section E (held-out generalization firewall).

The exact-run Iter504T authority premise is independently confirmed by:

- terminal canonicalization gate run `35245037403`;
- exact-run authority classification `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`;
- independent Critical Review commit `8624532254981fbea6f8fcfac09cd538e2066aa4`, verdict `CONFIRMED_SCOPED`.

The inherited bounded development-science statement is only:

`ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`

for development cohort `(causal=0to5, block=0, path=2, boxes=13,14,15)`.

No development case is a scientific test case in Iter504U.

## Frozen no-refit algorithm

Iter504U must preserve the validated Iter504T local-D method without scientific retuning:

- Arb/Acb precision: `384` bits;
- all `243` channels retained;
- no channel pruning;
- rhos exactly `[0.35,0.9,1.6,2.7]`;
- R grid exactly `[6,8,10,12]`;
- drift threshold exact `1/20`;
- robust slope floor exact `1`;
- deterministic rational dyadic midpoint subdivision;
- `MAX_DEPTH=3`;
- validated local derivative enclosure `D(J)` recomputed directly on every visited subinterval `J`;
- exact rational midpoint `m_J`;
- mean-value enclosure `f_i(J) subset f_i(m_J) + (J-m_J) D_i(J)`;
- analogous local-D construction for Haar/log contribution;
- producer exact-Arb predicates determine slope-floor, drift and certification decisions;
- serialized binary64 bounds are display-only;
- leaf certification is bound exactly to `all(rho.certified for rho in leaf.per_rho)`;
- exact rational dyadic cell identity and complete cover are required;
- Python `3.11` and `3.13` independent lanes;
- independent environment assembly, cross-environment aggregate and adversarial Critic.

The historical reusable C4 validator is **not** an authority path for this gate. Iter504U must use a new gate-local validator that explicitly enforces the leaf/per-rho binding above.

## Held-out selection rule

Selection is frozen using only pre-existing structural coordinates from the parent Iter504 grid. No held-out local-D value, drift, slope, possible-max multiplicity, PASS/INCONCLUSIVE outcome or runtime observation may be inspected or used to alter selection.

Development identity is:

`D = (causal=0to5, block=0, path=2, boxes={13,14,15})`.

The held-out cohort is the following six exact cases:

1. `H0_AMP_LOW = (causal=0to5, block=0, path=2, box=0)`
2. `H1_AMP_MID = (causal=0to5, block=0, path=2, box=8)`
3. `H2_CAUSAL_1 = (causal=1to4, block=0, path=2, box=8)`
4. `H3_CAUSAL_2 = (causal=2to3, block=0, path=2, box=8)`
5. `H4_DIRECTION = (causal=0to5, block=3, path=2, box=8)`
6. `H5_SIGN = (causal=0to5, block=0, path=3, box=8)`

Rationale frozen before output:

- H0 tests low-amplitude extrapolation under the original causal/direction/sign;
- H1 tests mid-domain amplitude transfer under the original causal/direction/sign;
- H2/H3 isolate transfer to both other authorized causal families at the same mid-domain amplitude and original geometric path;
- H4 changes the block/direction while retaining positive path sign;
- H5 flips the sign while retaining the development block and the same path-direction family (`path 2`/`path 3` share the second direction of block 0 and differ by sign).

Boxes `13,14,15` are excluded from the held-out cohort by construction.

Exact parent amplitude intervals are inherited from `core.box_amp(k)`:

- box 0: `[16/12800, 17/12800]`;
- box 8: `[24/12800, 25/12800]`.

No held-out substitution is permitted after any execution begins.

## Frozen case evaluator contract

For each held-out case and each environment independently:

1. Resolve `direction, sign = path_spec(block,path)` from the frozen parent mapping.
2. Start from the exact rational parent box interval.
3. Evaluate the whole current interval with a directly constructed interval dual amplitude `RD(J,1)`.
4. Recompute KAK/Toller/intertwiner/contraction local derivative enclosures for every R/rho/channel; do not reuse the development/root derivative enclosure.
5. Compute exact-Arb full-envelope and Haar/log bounds using the same late/early slope and drift formulas as Iter504T.
6. If all four rho rows certify slope floor and drift at a node, terminate that node as certified.
7. Otherwise bisect exactly at the rational midpoint until `MAX_DEPTH=3`.
8. At depth 3, preserve any unresolved valid leaf as unresolved. Do not deepen it.
9. Preserve all possible-max channel identities for provenance/diagnostics; they are not permitted to prune channels.
10. Serialize exact decision booleans and rational cell identities used by assembler/Critic.

## Exact scientific labels

PASS:

`ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`

iff every one of the six frozen held-out cases is valid, both environments agree on exact scientific decision projections, and total recomputed unresolved leaves across the held-out cohort are exactly zero.

INCONCLUSIVE:

`ITER504U_HELDOUT_LOCAL_D_INCONCLUSIVE_SCOPED`

iff all six cases are structurally/provenance valid and cross-environment exact decisions agree, but one or more valid terminal leaves remain unresolved at frozen depth 3.

INVALID:

`ITER504U_INVALID`

iff any authority/source/cohort identity changes, any selected case is substituted or omitted, any development case is inserted as a held-out test, any threshold/floor/R/rho/channel/precision/depth/partition rule changes, a derivative enclosure is replaced by midpoint/sampled truth, exact decision booleans are reconstructed from display floats, leaf/per-rho binding fails, dyadic cover/identity fails, channel pruning occurs, or the two environments disagree on the exact scientific projection.

A runtime or dependency failure that prevents production of the required complete objects is implementation-invalid/non-authoritative; it is not a scientific FAIL.

There is no scientific FAIL label in this bounded certificate gate: failure to certify by depth 3 is INCONCLUSIVE, not physical falsification.

## Required independent controls

The independent Critic must verify at least:

- exact six-case cohort identity and no development boxes 13–15;
- exact causal/block/path/box mapping;
- all 243 channels retained;
- exact R/rho grids;
- exact `1/20` threshold and `1` floor;
- exact `MAX_DEPTH=3`;
- exact rational dyadic-cell identity and complete cover per parent box;
- local derivative recomputation on every visited node;
- leaf certification equals conjunction of all four per-rho certifications;
- possible-max indices are complete/valid identities, not pruning authority;
- cross-environment equality of structural/exact-decision projections;
- changing a case identity -> INVALID;
- inserting a development box -> INVALID;
- changing threshold/floor/depth/channel count -> INVALID;
- float-reconstructed decision transport -> INVALID;
- non-dyadic/outcome-dependent partition -> INVALID;
- true leaf with any false per-rho certification -> INVALID;
- missing held-out case -> INVALID.

## Generalization interpretation

A PASS establishes only that the frozen local-D repair generalized across this prospectively selected six-case held-out cohort. It may authorize design of a prospectively frozen broader/full-domain campaign; it is **not** itself all-Iter504 closure.

An INCONCLUSIVE result means only that this fixed-depth held-out certificate did not close one or more cases. It does not falsify a model or the local-D mechanism.

## Claim ceiling

No outcome from this gate establishes all 1888 states, D7 closure, model/family failure, selector status, Candidate Gravity, Paper IV authorization, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
