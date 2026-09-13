# Iter467 preregistration — Eq.(4) tangent group-difference pushforward lattice

Date: 2026-09-13
Status: prospectively frozen before implementation/results.

## Scientific question
Given the source-defined Eq.(4) complete-graph group arguments `g_b^{-1} g_a` and the Iter466 exact K5 incidence carrier, does the linearized/tangent group-difference map possess the exact root-, tree- and permutation-independent conservation/Jacobian structure required before defining a correlated non-transversal distributional pushforward?

## Frozen object and scope
Use the oriented complete graph K5 with one edge for every unordered wedge pair and incidence matrix `B` (5 vertices x 10 edges). The tangent group-difference map is the exact linear map represented by `B^T` up to the frozen global edge-orientation convention. This gate tests only its integer-lattice/conservation geometry. It does **not** assert that a Toller spectral label is itself a full Lie-algebra Fourier coordinate and does not implement the nonlinear SL(2,C) Haar integral.

## Frozen lanes
Matrix over each root `r in {0,1,2,3,4}` with `fail-fast:false`.

For every root lane:
1. Delete the root row to form `B_r` and require exact rank 4 / nullity 6.
2. Enumerate all 4-edge subsets. Require exactly 125 nonzero maximal minors (K5 spanning trees), every nonzero determinant exactly `+1` or `-1`; every zero minor must correspond to a non-tree.
3. For every spanning tree, treat six non-tree edges as free chord coordinates, solve tree coordinates exactly over rationals, construct the 10x6 cycle-kernel basis, and require `B*C=0` exactly with integer entries.
4. Require every change-of-cycle-basis matrix between the lane's canonical tree basis and every other spanning-tree basis to be integral unimodular with determinant `+1` or `-1`.
5. Apply all 120 vertex permutations and require rank/nullity and the multiset of absolute maximal minors to remain unchanged.

## Frozen negative controls
- Delete one edge: nullity must become 5 while rank stays 4.
- Duplicate one edge in place of a distinct edge: at least one frozen spanning-tree/minor correspondence or full permutation invariant must fail.
- Corrupt one incidence column to have equal endpoint signs rather than opposite signs: column-sum conservation must fail and at least one root/permutation predicate must fail.

## Frozen classification
Scientific PASS iff every positive predicate passes in all five root lanes and every negative control is detected:
`ITER467_EQ4_TANGENT_GROUP_DIFFERENCE_PUSHFORWARD_LATTICE_QUALIFIED_SCOPED`.

Otherwise, provided the implementation and controls are valid:
`SCIENTIFIC_FAIL_ITER467_TANGENT_GROUP_PUSHFORWARD_LATTICE`.

Infrastructure/import/runner failures are not scientific FAIL and may be minimally repaired without changing this preregistration.

## Interpretation lock
PASS would establish only that the Eq.(4) tangent group-difference carrier has a root/tree/permutation-independent unimodular pushforward lattice with four independent conservation constraints and six cycle coordinates. It would authorize the next prospectively frozen step that introduces a source-backed spectral/group contraction kernel. It would **not** close D7-S2, prove convergence/finiteness, define the full nonlinear SL(2,C) amplitude, or authorize any D7 terminal label or Candidate Gravity.
