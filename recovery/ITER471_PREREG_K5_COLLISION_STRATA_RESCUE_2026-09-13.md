# Iter471 preregistration — exact K5 collision strata rescue

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION

## Motivation
The earlier Iter461 hosted job remained queued with zero jobs for hours. This rescue recomputes the exact finite combinatorial geometry on a hosted runner; it does not reuse a scientific result from the stalled run.

## Frozen object
Enumerate every set partition of five K5 vertices except the all-singleton partition. For each partition compute:
- block-size type;
- number E_int of K5 edges internal to collision blocks;
- relative collision dimension d=3*(5-number_of_blocks);
- simple uniform per-internal-edge power threshold pcrit=d/E_int.

For a model bound prod_internal r_e^-p, classify p<pcrit as SIMPLE_RADIAL_COMPARISON_INTEGRABLE, p=pcrit as MARGINAL_UNRESOLVED, and p>pcrit as SIMPLE_BOUND_INSUFFICIENT. The last class is not a divergence theorem.

## Frozen expectations
The 51 nontrivial partitions must group as:
- [2,1,1,1]: count 10, E_int=1, d=3, pcrit=3;
- [2,2,1]: count 15, E_int=2, d=6, pcrit=3;
- [3,1,1]: count 10, E_int=3, d=6, pcrit=2;
- [3,2]: count 10, E_int=4, d=9, pcrit=2.25;
- [4,1]: count 5, E_int=6, d=9, pcrit=1.5;
- [5]: count 1, E_int=10, d=12, pcrit=1.2.

## Frozen controls
Verify Bell(5)=52 including all singletons; permutation invariance; internal-edge count by both explicit edge enumeration and sum C(block_size,2); and exact rational thresholds. Audit p panel [1,1.2,1.5,2,2.25,3] with equality always MARGINAL_UNRESOLVED.

## PASS label
`ITER471_K5_COLLISION_STRATA_EXACT_GEOMETRY_QUALIFIED_SCOPED`.

## Scope guards
This gate supplies geometry/thresholds only. It does not assert that the physical Toller/EPRL contracted kernel has a uniform per-edge singularity power p, and no SIMPLE_BOUND_INSUFFICIENT result may be called divergence. D7-S2 remains open.