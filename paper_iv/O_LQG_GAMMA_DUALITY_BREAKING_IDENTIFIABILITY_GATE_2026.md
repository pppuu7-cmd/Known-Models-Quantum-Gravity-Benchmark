# O-LQG γ-Duality-Breaking Identifiability Gate — 2026-09-10

**KMQGB iteration:** 173  
**RQIR standard:** Core v1.0 FROZEN  
**CW2 object:** CW2-02 / O-LQG

## Purpose

Determine whether the Iter172 renormalized duality residual `Delta_gamma` can simply be absorbed as a theoretical uncertainty while retaining a one-parameter primordial-GW determination of the Barbero-Immirzi parameter.

Answer: **no**. Unless `Delta_gamma` is independently fixed or bounded, it is structurally degenerate with `gamma_EFT` in the cosmological relation.

## Generalized observable relation

Iter172 defines

`Delta_gamma = 2 f_GB^ren/f_CS^ren - (gamma_EFT - 1/gamma_EFT)`.

The original gamma-dual relation has

`q = (pi/8)(r+8 n_T)/Pi = 1/gamma_EFT - gamma_EFT`.

Allowing a renormalized duality-breaking correction therefore gives the generalized matching form

`q = 1/gamma_EFT - gamma_EFT - Delta_gamma`.

Equivalently,

`q + Delta_gamma = 1/gamma_EFT - gamma_EFT`.

If `Delta_gamma` is independently known, the positive-gamma inverse remains unique:

`gamma_EFT = [sqrt((q+Delta_gamma)^2+4) - (q+Delta_gamma)]/2`.

The problem is not algebraic invertibility at fixed `Delta_gamma`; it is joint identifiability when both `gamma_EFT` and `Delta_gamma` are unknown.

## q-only structural rank

For parameters

`theta = (gamma_EFT, Delta_gamma)`,

the observable gradient is

`dq/dtheta = ( -1 - 1/gamma_EFT^2, -1 )`.

This is one row for two parameters, so the Jacobian/Fisher information has rank at most one.

Therefore primordial observables entering only through `q` measure the combination

`1/gamma_EFT - gamma_EFT - Delta_gamma`,

not `gamma_EFT` and `Delta_gamma` separately.

Classification:

`STRUCTURAL_DEGENERACY_GAMMA_EFT_VS_DUALITY_BREAKING`.

No improvement in detector precision can remove this degeneracy by itself.

## Geometry holdout with a shared gamma

Let an independent geometric observable have the idealized form

`a_* = K gamma`,

with known nonzero normalization `K`.

If the parameter-identity bridge has already established that the same parameter controls both sectors,

`gamma_geom = gamma_EFT = gamma`,

then the joint Jacobian for `(q,a_*)` with respect to `(gamma,Delta_gamma)` is

`J = [[-1-1/gamma^2, -1], [K, 0]]`.

Its determinant is exactly

`det J = K`.

Thus for `K != 0` the pair is structurally full rank. The geometry block can separate `gamma` from a duality-breaking residual.

This gives a precise mathematical role to the cross-representation geometry holdout: it is not merely an additional consistency check; after parameter identity is established, it is an **identifiability-restoring observable**.

## Why parameter identity must come first

Suppose instead that geometry contains an independent parameter `gamma_geom` while cosmology contains `gamma_EFT`:

`q = 1/gamma_EFT - gamma_EFT - Delta_gamma`,

`a_* = K gamma_geom`.

The parameter vector is now

`theta = (gamma_EFT, Delta_gamma, gamma_geom)`.

The two-observable Jacobian has rank two but three columns. One direction remains unidentified.

Therefore an area-gap/geometry measurement cannot rescue the cosmological gamma-duality fingerprint unless a derived map first ties `gamma_geom` to `gamma_EFT` (and ultimately to `gamma_micro`).

This independently confirms the necessity of the Iter169 parameter-identity gate.

## Consequence for CW2-02

The Iter172 matching triple is now strengthened. A closure certificate must provide at least one of the following:

1. a symmetry/nonrenormalization theorem giving `Delta_gamma=0` within a frozen uncertainty;
2. a microscopic matching calculation predicting/bounding `Delta_gamma` independently of the primordial data;
3. a proven shared-parameter geometry relation that supplies an independent gamma observable and thereby restores full rank.

Option 3 still requires the `gamma_micro/gamma_EFT/gamma_geom` identity/running map; independently fitted gammas do not count.

## Sharpened minimum object

The minimum decisive object is therefore not just a number for `Delta_gamma`, but

`IDENTIFIABLE_RENORMALIZED_GAMMA_MATCH = {gamma_micro->gamma_EFT, Delta_gamma prior/prediction, optional gamma_geom map}`.

The desired strongest closure is

`Delta_gamma = 0` protected + `gamma_micro = gamma_EFT = gamma_geom` derived,

but RQIR also allows a nonzero predicted `Delta_gamma` if it is not freely refitted and the enlarged fingerprint remains identifiable.

## Executable control

Reference fixture:

`code/lqg_gamma_duality_breaking_identifiability_reference.py`.

It verifies:

- exact positive-gamma inversion at fixed `Delta_gamma`;
- rank-1 q-only degeneracy;
- full rank for q plus a shared-gamma geometry observable, with `det J = K`;
- negative control `K=0`;
- persistent underidentification when `gamma_geom` is left independent.

## Research priority after Iter173

The next analytic search should target protection/matching of gamma itself, not detector forecasting:

- does the microscopic duality define an exact transformation of the **renormalized** generating functional?
- is there a Ward identity or nonrenormalization statement constraining `Delta_gamma`?
- if not, can coarse-graining calculate its leading flow/breaking term and the corresponding `gamma_micro -> gamma_EFT` map?

Only after one of these is frozen does a high-cost cosmological likelihood campaign become scientifically discriminating.

## Status

CW2-02 remains **OPEN**, but the attribution failure mode is now algebraically localized.

Updated classification:

`PROMISING_ADAPT_EXISTING__GAMMA_DUALITY_BREAKING_DEGENERACY_EXPLICIT__IDENTIFIABLE_RENORMALIZED_MATCHING_NEEDED`.

No R1/R2/R3/R4 score change. Heavy compute remains idle.
