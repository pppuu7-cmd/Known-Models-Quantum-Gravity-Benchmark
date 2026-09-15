# Prospective preregistration — scalar K5 collision-strata power counting

Date: 2026-09-15
Gate: `SOURCE_J1_K5_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING_GATE`
Status: `PROSPECTIVELY_FROZEN`

## Parent authority

Consume the two terminal scoped results:

1. `results/SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_TERMINAL_2026-09-15.md`, commit `ae29ddbb41153e73d182173d6261e01f48a0bd00`, classification `AUX_GAUSSIAN_LOCAL_COUNTERTERM_ANSATZ_INSUFFICIENT_SCOPED`.
2. `results/SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS_TERMINAL_2026-09-15.md`, commit `5e95318f29e26f4ea954f269cbec2c69fa8089d8`, classification `AUX_GAUSSIAN_FULL_COLLISION_ORDER26_RADIAL_ACTION_SPACE_EXHAUSTED_SCOPED`.

Historical Iter461 branch `research/iter461-k5-collision-partitions` may be used only as an independent combinatorial cross-check. Its run `34748503239` is still queued/no-jobs and is not scientific authority. Its 3D local-dimension thresholds are forbidden in this scalar surrogate.

## HYPOTHESIS

The auxiliary aligned-K5 scalar Gaussian singular object has superficially divergent proper collision strata under the same naive uniform scaling model used for the parent full-collision order-26 count.

For a vertex partition with non-singleton blocks of sizes `s_1,...,s_r`:

- internal singular edges: `E_int = sum_i C(s_i,2)`;
- scalar normal dimension to the corresponding collision stratum: `d_perp = sum_i (s_i-1)`;
- each one-dimensional `delta''` edge factor has scaling degree 3;
- frozen superficial divergence degree:

`omega = 3 E_int - d_perp`.

This gate asks only whether the exact K5 partition lattice contains proper strata with `omega >= 0`, and records their exact multiplicities/degrees. It does not construct a forest subtraction.

## Frozen object

- K5 vertex set `{1,2,3,4,5}`;
- all set partitions of the five vertices, generated independently in main;
- exclude the all-singleton partition from collision strata;
- distinguish the full-collision partition `{1,2,3,4,5}` from proper collision strata;
- scalar dimension: one scalar coordinate per relative vertex displacement in a collision block;
- edge singularity scaling degree: exactly 3 per internal edge;
- no regulator-path numerical values enter the decision.

## Expected exact K5 combinatorics (source-lock / positive control)

Total set partitions: 52.
Nontrivial collision partitions: 51.
Partition-type multiplicities:

- `2+1+1+1`: 10
- `2+2+1`: 15
- `3+1+1`: 10
- `3+2`: 10
- `4+1`: 5
- `5`: 1

These values are independently recomputed; they are not copied as a terminal result from Iter461.

## Frozen scalar type table to be derived, not assumed

For each type compute exact `(E_int, d_perp, omega)` from the definitions above. The gate passes the scientific hypothesis only if all arithmetic identities and partition-level records agree with the type aggregation.

## Positive controls

1. Bell total = 52.
2. Nontrivial collision partitions = 51.
3. Exactly six collision partition types with the frozen multiplicities above.
4. For every partition, `E_int + E_cross = 10`.
5. For every partition, `d_perp = 5 - number_of_blocks`.
6. For each non-singleton block size s, its contribution is exactly `C(s,2)` internal edges and `s-1` scalar normal dimensions.
7. Full collision type `5` yields `(E_int,d_perp,omega)=(10,4,26)`, reproducing the parent power count.
8. All records with the same block-size type have identical `(E_int,d_perp,omega)`.

## Adversarial controls

1. Recompute the same partitions after all 120 permutations of vertex labels; the multiset of type/omega records must be invariant.
2. A synthetic 3D-dimension formula `d_perp=3*sum(s_i-1)` must produce at least one type table entry different from the scalar table, proving the implementation is not accidentally importing Iter461's 3D thresholds.
3. If edge scaling degree is synthetically changed from 3 to 1, at least one proper-stratum omega must change sign or reach a different value; otherwise the classifier is not using the frozen scaling degree.

## PASS classifications

### `AUX_GAUSSIAN_K5_PROPER_COLLISION_SUBDIVERGENCES_PRESENT_SCOPED`

iff all controls pass and at least one proper collision stratum has `omega >= 0`.

The result must additionally report whether **all** proper collision strata are superficially divergent (`omega >= 0`) or only a subset.

### `AUX_GAUSSIAN_K5_NO_PROPER_COLLISION_SUBDIVERGENCE_BY_FROZEN_COUNT_SCOPED`

iff all controls pass and every proper collision stratum has `omega < 0`.

## FAIL / INVALID

`SCIENTIFIC_FAIL_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING` iff exact enumeration is valid but the frozen hypothesis/derived identities fail in a way not covered by the two PASS branches.

`INVALID_IMPLEMENTATION` for source-lock failure, wrong partition count, wrong dimension formula, imported 3D thresholds, label dependence, or changed scaling degree.

## Consequence ceiling

A `...SUBDIVERGENCES_PRESENT...` result means only that **full-collision-only subtraction is not a complete forest/stratum analysis under the frozen scalar uniform power counting**. It does not prove that a stratified renormalized extension exists, nor that a specific forest formula is source-authorized.

It authorizes a subsequent prospectively frozen stratified/forest subtraction test on the auxiliary Gaussian object, with counterterms assigned to proper divergent collision strata according to exact inclusion/refinement structure.

No result here establishes Eq. (4) existence/nonexistence, model/family failure, D7 closure, a final selector, or Candidate Gravity activation.

Governance: RQIR Core v1.0 FROZEN; D7-S2/S3 not closed; D7-S4 partial; KMQGB downstream of pinned DSIR authority.
