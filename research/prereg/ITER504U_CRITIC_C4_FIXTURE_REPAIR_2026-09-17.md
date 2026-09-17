# ITER504U_CRITIC_C4_FIXTURE_REPAIR — prospective freeze

Date: 2026-09-17
Status: `PROSPECTIVELY_FROZEN_DURING_NONTERMINAL_RUN_BEFORE_CONSUMING_HELDOUT_SCIENCE`

## Parent execution

Active scientific run: `35246605860`.

At the time this repair is frozen, the run is nonterminal. Only workflow/job status has been inspected. No held-out slope, drift, certification, unresolved-leaf count, aggregate classification or Critic classification has been consumed to design this repair.

## Defect

The frozen Iter504U Critic negative control named `C4_true_leaf_false_rho` mutates only:

`leaf.per_rho[0].certified = False`

on the first leaf of the first held-out case.

That fixture is not guaranteed to create the intended contradiction. If the baseline leaf is already uncertified, or if its selected rho row is already false, the mutation can be a no-op with respect to the leaf/per-rho binding. The control can therefore fail for reasons that depend on the unknown scientific outcome.

This is an implementation defect in an adversarial synthetic fixture. It does not alter the producer science, held-out cohort, threshold, floor, precision, R/rho grids, channel count, partition rule, MAX_DEPTH, local-D construction, exact decision transport or PASS/INCONCLUSIVE definitions.

## Frozen repair

Replace only the synthetic C4 negative-control mutator with a deterministic fixture constructor that guarantees the intended structural contradiction independent of baseline science:

1. select the first leaf of `H0_AMP_LOW` only as a structural carrier;
2. set every `per_rho` row in that synthetic copy to a self-consistent certified state:
   - `slope_floor_satisfied = True`;
   - `drift_within_tolerance = True`;
   - `certified = True`;
3. then set exactly the first rho row in that synthetic copy to a self-consistent uncertified state:
   - `drift_within_tolerance = False`;
   - `certified = False`;
4. set the synthetic leaf top-level `certified = True`;
5. leave production objects untouched.

The resulting fixture has internally coherent per-rho booleans but violates exactly the required C4 binding:

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`.

The independent validator must reject it.

## Scope lock

Allowed changes:

- Critic synthetic negative-control construction only;
- methodology/self-test needed to prove the fixture is guaranteed to be rejected.

Forbidden changes:

- held-out case identities;
- producer evaluator;
- environment assembler;
- aggregate scientific classifier;
- base source realization;
- precision `384`;
- channels `243`;
- R `[6,8,10,12]`;
- rho `[0.35,0.9,1.6,2.7]`;
- threshold `1/20`;
- robust floor `1`;
- `MAX_DEPTH=3`;
- partition rule;
- local derivative recomputation;
- PASS/INCONCLUSIVE scientific meaning;
- using partial held-out output to choose a different repair.

## Authority use

Run `35246605860` remains immutable. Because its originally frozen Critic contains an outcome-dependent synthetic control, its eventual old-Critic result is not sufficient by itself for terminal scientific authority.

The preferred repair path is closure-only: preserve the immutable producer/assembly/aggregate artifacts from `35246605860` if they are structurally complete, and apply the prospectively repaired Critic to those exact artifacts without rerunning physics. A producer rerun is not authorized merely because this synthetic Critic fixture was defective.

If the immutable upstream artifacts are incomplete or implementation-invalid for an independent reason, no scientific inference follows and any further repair must be separately prospectively frozen.

## Interpretation ceiling

This repair concerns Critic fixture validity only. It cannot convert INCONCLUSIVE to PASS, alter any held-out scientific value, authorize all-Iter504 closure, D7 closure, model/family failure, Candidate Gravity, Paper IV or any global quantum-gravity conclusion.
