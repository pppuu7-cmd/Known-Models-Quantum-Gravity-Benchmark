# Preregistration — source j=1 K5 all-contact causal-sign cancellation gate

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN`

## HYPOTHESIS

In the source coherent realization of the causal K5 vertex, the formal highest-contact `j=1` component has the same causal-sign prefactor for every constrained causal structure `kappa_ab = sigma_a sigma_b`.

For K5,

`prod_{a<b} kappa_ab = +1`

for every assignment `sigma_a in {+1,-1}`. Therefore summing constrained causal structures cannot cancel the all-ten-wedge `delta''(B_ab)` component by the causal signs alone.

As an adversarial control, the unconstrained independent-wedge-sign sum used algebraically in the EPRL decomposition must cancel the same monomial sign:

`sum_{kappa in {+1,-1}^10} prod_e kappa_e = 0`.

This gate concerns only exact sign combinatorics of a formal contact component. It does not assume that the ten-fold contact distribution product is already defined.

## SOURCE / REALIZATION AUTHORITY

Primary source: Bianchi, Chen and Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026).

Freeze the source facts:

1. wedge sign `kappa_ab = sigma_a sigma_b`;
2. exact additive identity `T^(+) + T^(-) = D`;
3. coherent Toller factor

   `Theta_{kappa,rho,j}[B] = theta(kappa B) + kappa delta^(rho,j)(B)`;

4. for `j=1`, the separately certified source coefficient of `delta''(B)` is nonzero for real `rho != 0`:

   `i/[rho(1+rho^2)]`.

Repository authority:

- `research/SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_RESULT_2026-09-15.md`;
- `research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md`;
- `research/SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM_2026-09-15.md`.

## OBJECT

K5 on vertices `{1,2,3,4,5}` with all ten unoriented edges `(ab)`, `a<b`.

Enumerate exactly:

- all `2^5 = 32` vertex-sign assignments `sigma`;
- their induced constrained edge-sign assignments `kappa_ab=sigma_a sigma_b`;
- all `2^10 = 1024` independent edge-sign assignments for the EPRL adversarial control.

The formal source `j=1` all-contact monomial is

`C(rho) * [prod_{a<b} kappa_ab] * prod_{a<b} delta''(B_ab)`

with

`C(rho) = prod_{a<b} i/[rho_ab(1+rho_ab^2)]`.

Only the discrete causal-sign prefactor is classified here.

## EXACT GRAPH IDENTITY

Because every K5 vertex has degree four,

`prod_{a<b} (sigma_a sigma_b) = prod_a sigma_a^4 = +1`.

This is to be certified both symbolically by degree counting and exhaustively over all 32 vertex-sign assignments.

## POSITIVE CONTROLS

1. K5 has exactly 10 edges.
2. Every vertex degree is exactly 4.
3. All 32 `sigma` assignments induce all-contact sign `+1`.
4. Global reversal `sigma -> -sigma` leaves every `kappa_ab` unchanged.
5. The 32 vertex-sign assignments induce exactly 16 distinct constrained `kappa` patterns, each with multiplicity 2 due global reversal.
6. For every constrained pattern, `prod_e kappa_e=+1`.
7. The source `j=1` `delta''` coefficient is nonzero under the frozen assumption `rho_e != 0` real, so the tested contact component is not removed by a zero one-wedge coefficient.

## ADVERSARIAL / NEGATIVE CONTROLS

1. Enumerating all 1024 independent edge-sign assignments must give 512 patterns with `prod_e kappa_e=+1` and 512 with `-1`.
2. Their signed sum must be exactly zero.
3. The unconstrained sign sum must not be confused with the constrained causal-structure sum.
4. No conclusion about the existence of `prod_e delta''(B_e)` is permitted from sign algebra alone.

## PASS

Classify

`SOURCE_J1_K5_ALL_CONTACT_CAUSAL_SIGN_NONCANCELLATION_SCOPED`

iff all positive and adversarial controls pass exactly.

Interpretation ceiling:

- the all-ten-wedge highest `j=1` contact monomial has no cancellation mechanism coming solely from the constrained causal signs `kappa_ab=sigma_a sigma_b`;
- summing causal structures cannot mimic the independent-wedge sign cancellation of the EPRL decomposition for this formal monomial;
- any removal or canonical definition of the full-collision contact sector must therefore come from distributional extension/regulator structure, intertwiner/channel cancellation, integration identities, or another source-faithful mechanism, not from the bare constrained sign sum.

PASS does **not** establish that the ten-fold contact product exists, diverges as a distribution, or survives every channel contraction.

## FAIL

Classify

`SOURCE_J1_K5_ALL_CONTACT_CAUSAL_SIGN_CANCELLATION_FOUND`

iff the implementation is valid but at least one constrained causal assignment has `prod_e kappa_e=-1`, or the constrained sum of the all-contact sign vanishes.

## BLOCKED / INVALID

`INVALID_SOURCE_REALIZATION` if the implementation does not use exactly `kappa_ab=sigma_a sigma_b`, all ten K5 edges, or the frozen nonzero `j=1` contact component.

## CONSEQUENCE

A PASS sharpens, but does not replace, the authorized next source-order analytical front:

`SOURCE_J1_K5_JOINT_FEYNMAN_REGULATOR_EXTENSION_GATE`.

That gate must determine whether the source Feynman prescription supplies a joint correlated distributional limit despite the absence of ordinary absolute integrability and despite failure of the standard Hörmander sufficient multiplication criterion at a frozen contact witness.

## GOVERNANCE

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.
