# D7-S2 K5 tangent gate — execution coverage repair freeze

Date: 2026-09-16
Status: EXECUTION-ONLY COVERAGE REPAIR FROZEN BEFORE REPAIRED PRODUCTION RUN

## Authority ordering

The pre-existing mainline preregistration `bc9aa01263df1172206eb211b456bf5d78fe1b1b` predates the later duplicate-compatible preregistration `32a2575ded77a938ed742526a9d62fe1e4756d41` and therefore governs the scientific acceptance criteria.

The first production implementation at workflow head `0918d64d559ab63f56debb7e305896c51656eb14` checked rank/nullity, all 625 tree/root minors, triangle restriction and all 600 S5/root transports, but did not emit two explicit checks required by the earlier preregistration:

1. an explicit six-vector integer cycle basis annihilating every `B_r` and having exact rank 6;
2. all root-to-root tangent-coordinate changes being integer unimodular (`|det|=1`).

The successful first run is retained as noncanonical partial execution evidence. It is not sufficient for terminal PASS under the older preregistration.

## Frozen repair scope

This repair may only add explicit exact verification of those two already-frozen criteria. It must not change:

- the source object `Y_ab=X_a-X_b`;
- the ten ordered wedges;
- gauge-root convention;
- rank/nullity expectations;
- tree enumeration/minor criteria;
- S5 orientation transport criteria;
- PASS/FAIL/BLOCKED/INVALID semantics;
- claim ceiling.

## Cycle-basis check

Use the six oriented triangle cycles `(1,i,j)` for `2 <= i < j <= 5`, with edge coefficients implementing

`Y_1i + Y_ij - Y_1j = 0`.

For every root `r`, verify exactly that all six integer vectors annihilate `B_r` from the left and that the 6x10 cycle matrix has exact rank 6. No outcome-selected cycle basis is permitted.

## Root-coordinate check

For every ordered pair of distinct roots `(r,s)`, represent the same vertex tangent class by subtracting the old coordinate value at `s` from every vertex value so that the new root satisfies `X'_s=0`. Build the resulting exact integer 4x4 coordinate-change matrix from the old free-vertex coordinates to the new free-vertex coordinates and require determinant `+1` or `-1`.

All 20 ordered root changes must pass.

## Terminalization rule

Only the repaired production run satisfying the original `bc9aa012...` criteria may be terminalized. No substantive value from a nonterminal repaired workflow may be consumed.
