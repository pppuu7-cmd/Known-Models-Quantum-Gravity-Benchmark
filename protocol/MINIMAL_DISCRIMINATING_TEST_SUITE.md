# Minimal Discriminating Test Suite for Future Candidate Gravity

**Status:** frozen methodology / pre-resource design rule.  
**Purpose:** choose the smallest prospectively defined set of response orders/configurations/contrasts that preserves comparator-orthogonal identifiability and predictive robustness.

## 1. Candidate block library

Define a finite pre-registered library `B` of candidate blocks. A block may be

- one response order;
- one source/detector configuration;
- one frequency/proper-time band;
- one polarization/orientation;
- one state-preparation/null setting;
- one exact comparator-null contrast;
- one held-out prediction block.

Every block must already have complete same-parent response, physical reduction and covariance/nuisance metadata.

## 2. Relative cost metadata

Assign each block a **relative design cost** `c_b >= 0` representing methodological complexity, compute burden, calibration burden, or prospective apparatus complexity.

These costs are only for pre-residual design comparison. They are **not** final experimental resource/Fisher claims and must not be promoted as such before a real residual exists.

## 3. Suite geometry

For subset `S subset B`, build the stacked

`Sigma(S)`, `J_C(S)`, and when available `J_KG(S)` or candidate signal `s(S)`.

Compute

`d_perp(S) = m(S) - rank[ Sigma(S)^(-1/2) J_C(S) ]`,

`B_KG(S) = Pi_perp(S) Sigma(S)^(-1/2) J_KG(S)`.

Useful suite metrics include

- `rank_KG(S)=rank(B_KG(S))`;
- `sigma_min_plus(S)`: weakest robust nonzero singular value;
- projected signal SNR for a pre-registered signal;
- predictive/holdout score where available.

## 4. Threshold-first minimal-suite problem

Prefer a threshold formulation over arbitrary weighted sums.

Freeze target requirements prospectively, e.g.

- `d_perp(S) >= d_target`;
- `rank_KG(S) >= q_target`;
- `sigma_min_plus(S) >= tau_sigma`;
- optional projected SNR / predictive thresholds;
- attribution-stack coverage requirements.

Then solve

`min_S sum_(b in S) c_b`

subject to the frozen constraints.

For a small block library, exhaustive subset enumeration is preferred because greedy selection need not be globally optimal.

## 5. Greedy heuristic for large libraries

If exhaustive enumeration is impractical, use a pre-registered greedy heuristic only as a search aid.

A defensible lexicographic gain can prioritize

1. increase in robust projected rank;
2. increase in `d_perp`;
3. increase in weakest projected singular value;
4. reduction in total relative cost.

Do not claim the greedy suite is globally minimal unless verified.

## 6. Leave-one-block robustness

A discriminator carried entirely by one fragile block is weak.

For selected suite `S`, evaluate each deletion `S\{b}`.

Define diagnostics such as

`rank_LOBO_min = min_b rank_KG(S\{b})`,

`sigma_LOBO_min = min_b sigma_min_plus(S\{b})`.

A robust suite should retain a pre-registered minimum level of identifiability when any one non-mandatory block is removed.

Mandatory anchor blocks, if any, must be declared before selection rather than protected after seeing the result.

## 7. Attribution coverage

The minimal suite must not minimize away the attribution stack.

Require explicit coverage of all attribution layers used in the novelty claim, such as

- quantum/channel/ordered response;
- mediator nulls;
- spin-2/tidal/Ward gravity attribution;
- locality/causal support;
- relational/QRF controls;
- detector/state controls.

A mathematically small suite that omits the evidence needed to call the mediator gravitational is not admissible.

## 8. Cross-order / intervention synergy

Suite selection should exploit blocks that share parent parameters across orders/configurations.

A block is particularly valuable when it

- adds physical coordinates;
- adds little or no new comparator nuisance rank;
- improves cross-order exact invariants;
- rotates KG signal away from comparator tangent;
- provides a strong held-out prediction.

## 9. No post-hoc block selection

The candidate library, relative costs, mandatory attribution coverage and selection objective must be frozen before inspecting the target residual.

After a candidate residual is observed, changing the block library or dropping inconvenient blocks is a protocol change and requires a new prospective benchmark iteration.

## 10. Candidate Gravity design consequence

A future KG proposal should ideally come with a **small, redundant and predictive test suite**, not an unlimited menu from which a successful observable can be selected after the fact.

This is another form of rigidity: the parent dynamics should be overconstrained by a compact set of measurements/observables.

## 11. Promotion guardrail

Relative test-suite cost is not final resource closure. Fisher/experimental resource promotion remains forbidden until a robust comparator-subtracted residual survives the full Candidate Gravity Promotion Gate.
