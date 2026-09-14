# Source-order K5 causal vertex — Haar-tail integrability away from collisions

Date: 2026-09-15
Status: `DERIVED_KMQGB` scoped theorem; collision regions and spin sums remain open

## Purpose

Separate the true noncompact-Haar problem from the K5 collision problem for the **source-order** causal vertex. This theorem does not use the reordered ten-spectral representation and does not infer convergence from a one-dimensional escape path.

## Source input

Bianchi–Chen–Gamonal define each Toller matrix first and then form the causal vertex as the four-group integral of the product of ten Toller matrices after one group is gauge fixed (arXiv:2601.23162, Eqs. (3)–(4)).

Their companion Toller paper (arXiv:2604.24945, Eq. (13) and the asymptotic statement immediately following it) gives, for fixed finite labels,

`|t^(±,rho,k)_{jlm}(beta)| ~ exp(-(1+|k±m|) beta)` as `beta -> infinity`.

In particular every magnetic term decays at least as `exp(-beta)` at large boost. The full Toller matrix is a finite sum of these reduced terms multiplied by compact `SU(2)` Wigner matrices.

The Cartan decomposition of `SL(2,C)` has radial Haar density proportional to `sinh(beta)^2 d beta`; therefore

`I_alpha = integral_G exp(-alpha beta(g)) dg < infinity`

for every `alpha > 2`.

## Collision-cutoff domain

Fix `delta > 0`. Let

`Omega_delta = { (g1,...,g4) in G^4 : beta(g_b^-1 g_a) >= delta for every K5 edge (a,b) }`

with `g0 = identity` and `G = SL(2,C)`.

This removes every pair-collision neighborhood but leaves all noncompact group directions completely unbounded.

## Lemma 1 — uniform edge bound on the cutoff domain

For fixed finite representation/magnetic labels and fixed real source parameters, there is a finite constant `C_delta` such that for every matrix entry of either causal Toller branch,

`|T^(±)(g)| <= C_delta exp(-beta(g))`

whenever `beta(g) >= delta`.

### Proof

For sufficiently large `beta`, the published asymptotics give the bound term by term because `1+|k±m| >= 1`. The compact `SU(2)` factors in the full KAK reconstruction are bounded and the magnetic sum is finite. On the remaining compact interval `delta <= beta <= B`, each fixed-label Toller entry is finite/continuous away from the removed collision point, hence `exp(beta)|T(g)|` has a finite supremum after the compact angular factors are included. Combining the two ranges gives `C_delta`. QED.

For the benchmark's finite `j=1` channel set and finite rho witness set one may take the maximum of finitely many such constants. No uniform-in-spin statement is claimed.

## Lemma 2 — K5 metric weight is integrable

Let

`S(g1,...,g4) = sum_{0 <= a < b <= 4} beta(g_b^-1 g_a)`.

Then

`integral_{G^4} exp(-S) dg1...dg4 < infinity`.

### Proof by spanning-tree averaging

The complete graph `K5` has `5^(5-2)=125` spanning trees. By symmetry, each of its 10 edges belongs to the same number of spanning trees. A tree has 4 edges, so the inclusion probability of a fixed edge under the uniform spanning-tree measure is

`4/10 = 2/5`.

For a spanning tree `T`, let

`L_T = sum_{e in T} beta_e`.

Averaging over all 125 trees gives exactly

`average_T L_T = (2/5) S`.

Hence at least one tree `T_*` satisfies

`L_T* <= (2/5) S`,

or equivalently

`S >= (5/2) L_T*`.

Therefore pointwise

`exp(-S) <= sum_T exp(-(5/2)L_T)`.

For any fixed tree, root it at the gauge-fixed node 0 and change variables from the four vertex group elements to the four tree-edge increments `h_e = g_parent^-1 g_child`. Haar invariance makes this a product-measure change of variables. Consequently

`integral_{G^4} exp(-(5/2)L_T) prod_i dg_i`

factorizes into

`[ integral_G exp(-(5/2) beta(h)) dh ]^4`.

The one-group factor is finite because the radial density is proportional to `sinh(beta)^2` and `5/2 > 2`. There are only 125 trees, so the finite sum is integrable. QED.

## Theorem — source-order noncompact tails are absolutely integrable away from collisions

For fixed finite external/intertwiner/representation labels, fixed causal assignment, and fixed `delta > 0`, the absolute value of the gauge-fixed K5 source-order causal-vertex integrand is integrable over `Omega_delta`.

### Proof

The intertwiner/boundary contraction contains only finitely many magnetic terms. By Lemma 1 every Toller edge matrix entry on `Omega_delta` is bounded by `C_delta exp(-beta_e)`. Taking absolute values before the finite sums therefore bounds the contracted integrand by

`C'_delta exp(-sum_e beta_e) = C'_delta exp(-S)`.

Lemma 2 supplies an integrable global majorant on `G^4`. Restricting to `Omega_delta` preserves integrability. QED.

## Immediate scientific consequence

The noncompact Haar tail and collision singularities are not equally open anymore for the fixed-label source-order object:

- `SOURCE_ORDER_HAAR_TAIL_AWAY_FROM_COLLISIONS = ABSOLUTE_JUSTIFIED_SCOPED`;
- `SOURCE_ORDER_COLLISION_REMOVAL = OPEN`;
- `SOURCE_ORDER_COLLISION_TAIL_COMPATIBILITY = OPEN`.

Thus any remaining fixed-label absolute-divergence obstruction must come from approaching collision strata, from failure of a uniform estimate needed when the collision cutoff is removed, or from an additional operation not included here. It cannot arise solely from sending collision-separated group configurations to noncompact infinity.

This is stronger than any one-dimensional escape-path observation: the proof integrates the full four-group noncompact domain outside collision neighborhoods and automatically accounts for the shrinking transverse volume of correlated/common-escape sectors.

## Relation to Iter504

Iter504 evaluates a prospectively frozen one-dimensional correlated q=1 escape family with the product of four individual Haar radial Jacobians. A NONDECAY result there remains a valid scoped statement about that frozen pathwise density/envelope, but it is **not** a contradiction to this theorem and cannot by itself imply absolute Haar divergence. A bounded-width tube around a correlated common-escape path need not have the product radial volume suggested by evaluating four Jacobians pointwise while keeping all relative group separations bounded.

Conversely, this theorem does not predict Iter504's classifier and was derived without consuming any Iter504 centered-shard or aggregate science outcome.

## What remains open

1. Remove `delta -> 0` by proving source-faithful local integrability/cancellation on every K5 collision stratum.
2. Determine whether the required collision estimates can be made compatible with noncompact escape uniformly, rather than only at fixed `delta`.
3. If an unbounded spin/representation sum is part of a later physical observable, control the label dependence of `C_delta`; no spin-sum theorem is claimed here.
4. Consume, rather than duplicate, the frozen Iter461 K5 collision-partition computation when it becomes terminal.

## Claim guards

- No collision-cutoff removal is claimed.
- No full causal-vertex finiteness theorem is claimed.
- No statement uniform in unbounded spin labels is claimed.
- No equality with a reordered ten-spectral/Fubini representation is claimed.
- No Iter504 DECAY/NONDECAY conclusion is inferred.
- `D7-S2 = NOT_CLOSED` pending the collision/compatibility obligations.
- `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- No terminal D7 selector is authorized.
- Candidate Gravity remains inactive.
