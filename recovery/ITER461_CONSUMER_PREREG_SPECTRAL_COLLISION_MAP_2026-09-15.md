# Iter461 consumer preregistration — spectral collision map — 2026-09-15

## Status

Prospective, outcome-blind consumer contract written while authoritative Iter461 run `34748503239` is still queued and before any Iter461 artifact is available. This file does not execute or duplicate Iter461 and cannot upgrade a failed/invalid Iter461 output.

## Upstream authority

- Branch: `research/iter461-k5-collision-partitions`.
- Frozen head: `05c7f87c8519349057332bf90021f1128e1eefc3c`.
- Upstream contract: `benchmarks/lqg_iter461_k5_collision_partitions_contract.json`.
- Upstream implementation: `code/lqg_iter461_k5_collision_partitions.py`.
- Authoritative workflow run: `34748503239`.
- Expected artifact name: `iter461-summary` containing `iter461_summary.json`.

No rerun or duplicate enumeration is authorized by this consumer preregistration.

## Frozen acceptance checks

An Iter461 artifact is consumable by the spectral/correlated-kernel front only if all of the following hold simultaneously:

1. upstream workflow/job completes successfully and the artifact is attributable to the frozen head above;
2. `classification == ITER461_EXACT_K5_COLLISION_PARTITION_THRESHOLDS_QUALIFIED_SCOPED`;
3. `pass == true`;
4. every entry of the upstream `tests` object is true;
5. `bell_total == 52` and `nontrivial_partitions == 51`;
6. exactly six collision types are present with multiplicities
   - `2+1+1+1: 10`,
   - `2+2+1: 15`,
   - `3+1+1: 10`,
   - `3+2: 10`,
   - `4+1: 5`,
   - `5: 1`;
7. every record satisfies `internal_edges + cross_edges == 10`;
8. every record satisfies `relative_vectors == sum(block_size-1)` and `local_dimension == 3*relative_vectors`;
9. every exact threshold agrees with `critical_pair_power = local_dimension/internal_edges` before conversion to floating point;
10. the artifact retains the scope lock that a nonpositive naive margin is unresolved and never by itself a divergence declaration.

If any required item fails or the artifact is missing/incomplete, the consumer state is `ITER461_CONSUMER_INVALID_OR_BLOCKED`; no collision theorem may be inferred.

## Prospectively frozen grouped threshold table

The following table is derived algebraically from the already-frozen upstream formulas and is recorded before seeing the run output. It is a cross-check, not an independent replacement for the authoritative artifact.

| collision type | multiplicity | internal edges | cross edges | relative vectors | local dimension | exact naive `pcrit` |
|---|---:|---:|---:|---:|---:|---:|
| `2+1+1+1` | 10 | 1 | 9 | 1 | 3 | `3` |
| `2+2+1` | 15 | 2 | 8 | 2 | 6 | `3` |
| `3+1+1` | 10 | 3 | 7 | 2 | 6 | `2` |
| `3+2` | 10 | 4 | 6 | 3 | 9 | `9/4` |
| `4+1` | 5 | 6 | 4 | 3 | 9 | `3/2` |
| `5` | 1 | 10 | 0 | 4 | 12 | `6/5` |

The most restrictive naive local-power diagnostics are therefore prospectively ordered

`5`, `4+1`, `3+1+1`, `3+2`, then `2+1+1+1` / `2+2+1`.

This ordering is only a proof-priority heuristic. It is not a convergence/divergence classification.

## Consumption into the spectral admissibility front

After a valid Iter461 artifact is obtained, each exact partition record is mapped to one collision stratum entry in the spectral proof ledger. The consumer must preserve the explicit partition, type, edge counts, relative-vector count, local dimension, and exact rational threshold.

For every stratum the next status must be one of:

- `ABSOLUTE_ROUTE_CANDIDATE` — an integrable-majorant proof will be attempted;
- `MICROLOCAL_ROUTE_CANDIDATE` — a pullback/product/pushforward wavefront/transversality proof is required;
- `OPEN_BLOCKED` — neither sufficient route is presently proved.

These are planning statuses only. A stratum becomes `ABSOLUTE_JUSTIFIED` or `DISTRIBUTIONAL_JUSTIFIED` only after the corresponding theorem is actually proved under the separate spectral-admissibility scaffold.

## No-go rules

- Do not infer correlated convergence solely from `critical_pair_power`.
- Do not infer divergence from `p >= pcrit`.
- Do not use multiplicity or codimension counting as a substitute for a local correlated-kernel estimate.
- Do not infer legal exchange of boundary-value limits and group integration from separate-variable tensor-product existence.
- Do not silently replace conditional/PV/source-defined distributional convergence by absolute convergence.
- Do not select a Hörmander criterion until the actual operation (product, pullback, or pushforward) and its normal/conormal geometry are identified for that stratum.

## Global guards

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- No terminal D7 selector is authorized.
- Candidate Gravity remains inactive.
