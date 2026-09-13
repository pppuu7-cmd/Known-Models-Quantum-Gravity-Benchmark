# Iter483 — common-node SL(2,C) polar geometry

Date recorded: 2026-09-14
Scientific classification: `ITER483_COMMON_NODE_SL2C_POLAR_GEOMETRY_QUALIFIED_SCOPED`

## Authority
- preregistration: `a745b14adc9e554e77c51eb5572fb34879990747`
- implementation: `9a2eb176f87124f0f87481b25f03202da522d89f`
- workflow launch: `cc1ffe237953728aa61d953c0a928cac3efaa09e`
- serialization-only repair / authoritative retry head: `9eb185779ab316591bb6383923182c0b4472883d`
- authoritative run: `34782171609`
- aggregate job: `103791079718`
- aggregate artifact: `10325219145`
- aggregate artifact digest: `sha256:4839a846ae235b3d5992e20739a94f35ed1d785e141a44c9432b1149483ed2b0`

## Raw artifacts consumed
- A-mild `10324703167`
- A-strong `10325353824`
- B-mild `10325187575`
- B-strong `10325635843`
- C-mild `10325635841`
- C-strong `10325553136`
- D-mild `10324849550`
- D-strong `10325538117`

## Frozen result
All 8/8 expected lanes are present and all 8/8 satisfy the preregistered scientific predicates. The aggregate classifier therefore returns `ITER483_COMMON_NODE_SL2C_POLAR_GEOMETRY_QUALIFIED_SCOPED`.

Across the lanes the K5 shared-node triangle-cycle residual is O(1e-16), polar reconstruction residual is O(1e-16), extracted rapidities are finite/nonnegative, and the deliberately corrupted relative-element control produces O(1e-1) cycle violation. The strong-regime panels reach edge rapidities up to about 1.67, so the qualification is not confined to an infinitesimal-boost panel.

## Scope lock
This result qualifies only shared-node noncompact `SL(2,C)` kinematics plus the specified positive-polar/rapidity machinery. It does **not** identify the source Toller KAK decomposition, prove the source boost-dependent magnetic kernel, establish Haar or spectral convergence, evaluate the full causal vertex, close D7-S2, authorize a terminal D7 classifier, or authorize Candidate Gravity.

The initial failed Iter483 production attempt remains an infrastructure/output-serialization event only; the authoritative retry changed NumPy-boolean serialization and did not alter the frozen science.

## Next permitted gate
A later gate must prospectively pin and test the source-faithful one-edge Toller/KAK factor on the already-qualified shared-node `SL(2,C)` elements, including exact convention/reconstruction and reversal/inversion controls, before any ten-edge boost-dependent network or Haar conclusion.
