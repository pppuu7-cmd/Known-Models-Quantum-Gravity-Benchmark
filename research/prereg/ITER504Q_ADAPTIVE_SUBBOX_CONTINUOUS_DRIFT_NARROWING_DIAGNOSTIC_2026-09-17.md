# ITER504Q — adaptive subbox continuous-drift narrowing diagnostic

Date: 2026-09-17  
Status: PROSPECTIVELY FROZEN BEFORE ITER504Q SUBSTANTIVE OUTCOME

Gate:

`ITER504Q_ADAPTIVE_SUBBOX_CONTINUOUS_DRIFT_NARROWING_DIAGNOSTIC_GATE`

## Parent terminal authority

This gate is downstream of terminal Iter504P:

`ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED`.

Parent terminal commit: `162014c7566afa4828e646f77e52d91140dc8388`.  
Parent independent Critic: `f0844237cbf6ba1e042399d5a76dec8a4ab8b248`.

Iter504P established only that the frozen sampled point grid has no `D_point > 0.05` among 1584 decisive records. It did not prove continuous NONDECAY. Iter504 itself remains a valid continuous interval INCONCLUSIVE result because centered first-order max-envelope drift enclosures can exceed `0.05` in nonsmooth channel-competition regions.

## Method selection frozen before new outcome

Candidate rigorous approaches were compared using the required pre-outcome criteria:

1. **Uniform narrower boxes over the whole campaign** — low hidden-dependency risk but high compute cost because every box is subdivided regardless of need.
2. **Active-channel pruning without subdivision** — low compute cost but insufficient at genuine channel crossings because it does not itself tighten the shared amplitude dependency.
3. **Derivative-sign / exact channel-crossing localization** — potentially high enclosure reduction but materially higher implementation complexity and hidden chart/root/crossing proof risk.
4. **Higher-order dependency-preserving enclosure** — potentially high reduction, but high implementation and validation risk before first demonstrating that ordinary rigorous subboxing resolves the bottleneck.
5. **Deterministic adaptive amplitude bisection with full 243-channel recomputation on every subbox** — high expected enclosure reduction in crossing regions, compute concentrated only where the frozen classifier remains unresolved, and the lowest hidden channel-loss risk because no channel is discarded.

Selected method: **(5)**.

`possible_max_indices` are retained as diagnostics only. They do not authorize channel deletion. Every evaluated subbox recomputes all 243 contraction channels and applies the same validated envelope construction.

## Frozen diagnostic cohort

The cohort is chosen only from already-terminal Iter504 evidence, before any Iter504Q calculation.

Lane:

`0to5-b0`

Path:

`2`

Frozen path geometry inherited from Iter504:

- direction `[1,1,1,-1,-1,-1]`;
- sign `+1`.

Original Iter504 amplitude boxes:

- box `13`: `[29/12800, 30/12800]`;
- box `14`: `[30/12800, 31/12800]`;
- box `15`: `[31/12800, 32/12800]`.

All four frozen rhos are decisive for the diagnostic:

`[0.35, 0.9, 1.6, 2.7]`.

Frozen R grid:

`[6, 8, 10, 12]`.

This cohort is the terminally documented Iter504 nonsmooth crossing region: the parent result already reported 29–39 simultaneously possible maximizing channels at R=10/12 in these boxes. Selection is therefore a mechanism-stress diagnostic, not a post-hoc search for an easy PASS.

## Frozen arithmetic and physics

- `python-flint==0.9.0`;
- Arb/Acb precision: `384` bits;
- same source formulas, KAK construction, exact-rational intertwiners and 243-channel contraction as Iter504;
- same causal assignment, direction, sign, R grid and rho grid;
- same centered mean-value enclosure construction on each new subbox;
- same late slope definition from R=8,12;
- same early slope definition from R=6,10;
- same drift upper definition;
- same robust NONDECAY slope floor `+1.0`;
- same drift tolerance `0.05`.

No physical domain, threshold, slope definition, rho, R value, channel set or source formula may be changed after outcome.

## Frozen adaptive subdivision algorithm

Each original box starts at depth `0`.

For every current subbox `[a,b]`:

1. construct the exact Arb interval `a union b`;
2. use its exact midpoint and half-width;
3. recompute the full validated dual derivative enclosure over that subbox;
4. recompute the midpoint source realization;
5. recompute all `243` channel enclosures for every frozen `(R,rho)`;
6. compute the max-envelope lower/upper bounds and `possible_max_indices`;
7. compute late/early slope intervals and frozen drift upper bound for all four rhos.

A subbox is `CERTIFIED` iff for **every** frozen rho:

- all construction/cycle/source-additive/finite-envelope/center-regression controls pass;
- `S_lower >= +1.0`;
- `drift_upper <= 0.05`.

If not certified and depth `< 6`, bisect exactly at the rational midpoint and evaluate both children.

If not certified at depth `6`, retain it as an `UNRESOLVED_DEPTH6` leaf. Do not alter the tolerance or choose a different split point.

Maximum depth is frozen to `6`.

## Exact-cover controls

For each original box independently, terminal eligibility requires:

- every generated leaf endpoint is an exact rational descendant of the original box;
- leaves are sorted and adjacent with no gap;
- leaf interiors do not overlap;
- first leaf lower endpoint equals the original lower endpoint;
- last leaf upper endpoint equals the original upper endpoint;
- union of all leaves equals the full original box;
- no leaf is silently removed because of a bad result.

## Frozen terminal classifier

### PASS-type diagnostic localization

`ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_NARROWED_WITHIN_TOLERANCE_SCOPED`

iff:

- all three original boxes have exact valid leaf covers;
- all arithmetic/source controls pass;
- every terminal leaf is `CERTIFIED` before or at depth 6;
- no unresolved leaf remains.

Meaning: this specific known crossing diagnostic can be rigorously narrowed below the unchanged continuous `0.05` drift criterion by deterministic full-channel subboxing. It authorizes considering a scaled campaign; it does not certify the full Iter504 domain.

### Valid scientific INCONCLUSIVE

`ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_INCONCLUSIVE_SCOPED`

iff:

- exact cover and all source/arithmetic controls are valid;
- at least one leaf reaches depth 6 with `S_lower >= +1.0` but `drift_upper > 0.05`, or otherwise remains classifier-inconclusive without a method/provenance defect.

This is not scientific FAIL and not a decay witness.

### INVALID

`ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_INVALID`

iff any frozen source/provenance/coverage/control requirement fails, any leaf is missing/duplicated, the 243-channel set is changed, or the algorithm/threshold/cohort is changed.

## Required terminal evidence

Persist:

- total nodes and leaves;
- leaf depth histogram;
- certified vs unresolved leaf count;
- per-original-box leaf count;
- maximum terminal-leaf drift upper and exact witness;
- minimum terminal-leaf late-slope lower;
- maximum possible-max-channel count at root and leaves;
- per-rho worst terminal-leaf drift;
- exact coverage certificate for boxes 13,14,15;
- implementation commit, workflow head, run ID, artifact ID/digest and JSON SHA256;
- independent Critic replay of the leaf cover and terminal classifier.

## Scaling firewall

Do **not** launch a new full 3072-state / 1888-inconclusive-state campaign from this preregistration alone.

If this diagnostic PASSes, first use its terminal evidence to prospectively freeze a scaled campaign and its resource ceiling. If it remains INCONCLUSIVE, localize whether the residual width is due to still-unresolved channel competition, mean-value derivative width, or a depth/resource limitation before changing methods.

## Claim ceiling

No point-grid or diagnostic PASS is promoted to a continuous theorem on the full Iter504 q=1 domain. No positive-measure Haar theorem, absolute-Haar divergence theorem, cutoff removal, D7-S2 closure, selector authorization, model/family failure, Candidate Gravity activation, quantum-gravity solution or new-physics claim follows.
