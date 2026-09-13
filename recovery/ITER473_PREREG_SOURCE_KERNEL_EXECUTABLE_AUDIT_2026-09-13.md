# Iter473 preregistration — source common-group kernel executable availability

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent: `main` after Iter469–472 recovery.

## Question
Does the tracked repository already contain a source-faithful executable or rigorous computable bound for the Iter468 common kernel
`C({rhot_e}) = int prod_{a=2}^5 dg_a prod_e D_e^(rhot_e,k_e)(g_b^-1 g_a)`
that depends on all ten distinct spectral variables, rather than only symbolic structure, one-/two-group reductions, fixed-label integrability, or wedge-local Toller factors?

## Frozen positive requirements
A candidate counts as an executable common-kernel implementation only if tracked code jointly provides: (1) ten distinct spectral inputs; (2) four nontrivial post-gauge-fix SL(2,C) group variables or an explicitly proved exact reduction of them; (3) numerical/analytic evaluation or rigorous bound of every source D/Toller factor as a function of spectral and group variables; (4) an actual integration/bounding operation producing a finite value/bound depending on the ten-variable input; and (5) validation/negative controls or an explicit theorem provenance.

Simple token matches, symbolic strings, fixed-label Kamiński citations, one-leg/two-leg radial envelopes, or a product of independent spectral factors do not satisfy the gate.

## Outcomes
- `EXECUTABLE_SOURCE_KERNEL_FOUND_SCOPED` only if at least one candidate satisfies all five requirements under manual-readable machine evidence.
- Otherwise `BLOCKED_SOURCE_KERNEL_EXECUTABLE_NOT_PRESENT_IN_TRACKED_REPO_SCOPED`.

Either outcome is a valid completed audit. BLOCKED means only absence from the tracked repository snapshot, not mathematical impossibility and not absence from the literature.

## Scope lock
No inference of full causal-vertex convergence/divergence; no claim that fixed-label Kamiński integrability is uniform in ten spectral labels; no invented shared spectral variable; no replacement regulator. D7-S2 stays open unless an independent closure theorem is proved.