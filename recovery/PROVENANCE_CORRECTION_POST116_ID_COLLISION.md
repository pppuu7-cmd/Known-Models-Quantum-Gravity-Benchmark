# Provenance Correction — Post-Iter116 Iteration-ID Collision

**Date:** 2026-09-09  
**Status:** permanent recovery/provenance authority.  
**Reason:** a race with already-committed Iter107–116 authority caused six later scientific commits to reuse historical iteration IDs 107–112 and, for four files, synthesis IDs 009–012.

No historical commit is rewritten or hidden. This note defines the authoritative attribution of the later files.

## 1. Pre-existing authority wins

Before the colliding commits were created, the repository already contained authoritative Iter107–116 research and recovery, culminating in Iter116 central authority.

Examples include

- original Iter107 hidden-zero cross-order nonuniqueness gate;
- original Iter108 BCFW infinity boundary origin-data gate;
- original Iter109 infinity-boundary recursive parent;
- original Iter110 eikonal causality selector-limit gate;
- original Iter111 multi-shift contact nullspace gate;
- original Iter112 Lorentzian contour-thimble origin gate;
- later Iter113–116 authority frozen in recovery/state.

Those historical IDs retain priority and are never reused.

## 2. Colliding commits and corrected attribution

The following later commits used stale iteration numbers. Their **commit messages remain historical facts**, but their scientific contents are reattributed as follows:

| Colliding commit SHA | Historical mistaken message | Correct authority |
|---|---|---|
| `f2835fa0b376dfac9e84e190221795e71b30e29a` | iteration107 hidden-zero degree/growth gate | **Iter117** `protocol/P4_HIDDEN_ZERO_DEGREE_GROWTH_ORIGIN_GATE.md` |
| `78ba3083e859c3a0d9146d7943b4f7558e080c74` | iteration108 boundary-at-infinity gate | **Iter118** `protocol/P4_BOUNDARY_AT_INFINITY_ORIGIN_DATA_GATE.md` |
| `e0a18d32271a491e5682b4e4d3eb2859188c378a` | iteration109 all-deformation synthesis | **Iter119 / SYNTHESIS-011** `candidate_synthesis/SYNTHESIS_011_ALL_DEFORMATION_BOUNDARY_CONSISTENCY.md` |
| `94bd59b027b669d82f3728daa7cc73ed76996ef8` | iteration110 growth-minimality synthesis | **Iter120 / SYNTHESIS-012** `candidate_synthesis/SYNTHESIS_012_COMPLEX_GROWTH_MINIMALITY_SELECTOR.md` |
| `c5eba681b6cdc69ceaa6720d1d51ceadd92b5d86` | iteration111 black-hole entropy-density synthesis | **Iter121 / SYNTHESIS-013** `candidate_synthesis/SYNTHESIS_013_BLACK_HOLE_ENTROPY_DENSITY_PARENT.md` |
| `b288264c25fa72c53c585be14e9f38a838dcda48` | iteration112 black-hole ETH synthesis | **Iter122 / SYNTHESIS-014** `candidate_synthesis/SYNTHESIS_014_BLACK_HOLE_ETH_MATRIX_PARENT.md` |

## 3. File corrections

- The two protocol files were updated in place to display Iter117 and Iter118.
- Four synthesis files were recreated under non-colliding synthesis IDs 011–014 and Iter119–122.
- The mistakenly named synthesis files were deleted from the current tree only after the corrected copies existed.
- Git history retains all original commits, so no provenance is lost.

## 4. Scientific score consequence

This is a provenance repair only.

- R1 remains 92%.
- R2 remains 89%.
- R3 remains 24% under external RQIR authority.
- R4 remains 45% because none of Iter117–122 produced a P4 survivor.

## 5. Future rule

Before assigning a new KMQGB iteration ID, read `recovery/state.json` and recent repository commits. The latest committed authority wins any chat-memory or stale-summary race. Never reuse an iteration ID even if the scientific file was created later in wall-clock time.
