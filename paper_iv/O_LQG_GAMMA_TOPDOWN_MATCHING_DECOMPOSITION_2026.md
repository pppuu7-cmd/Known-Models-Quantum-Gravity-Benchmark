# O-LQG γ Top-Down Matching Decomposition — 2026-09-10

**KMQGB iteration:** 172  
**RQIR standard:** Core v1.0 FROZEN  
**CW2 object:** CW2-02 / O-LQG

## Objective

Replace the vague instruction

`derive the gamma-dual EFT from spinfoams`

by the smallest sequence of independently falsifiable matching obligations capable of authorizing the observable gamma-duality fingerprint.

## Authority refresh

Bianchi & Rincon-Ramirez, arXiv:2403.06053v2 / Phys. Rev. D 113, 124013 (2026), establishes an exact gamma-duality property of the EPRL microscopic construction and then builds a gamma-dual semiclassical EFT. Crucially, it explicitly states that a top-down derivation of the effective action directly from the non-perturbative spinfoam dynamics `W_gamma` is still missing and assumes that gamma-duality survives at the semiclassical level without breaking effects.

Separately, Han, Phys. Rev. D 113, 084034 (2026), provides a concrete Lorentzian spinfoam-stack summation in which a triangulation-dependent normalization factor separates from a finite boundary-data-dependent part; after renormalization the finite amplitude is independent of the bulk 2-complex in the stated limit.

This does **not** derive the gamma-dual higher-curvature EFT. It does, however, show that one part of the old generic continuum objection — uncontrollable bulk triangulation normalization — can be isolated in a concrete amplitude construction.

## Minimal matching chain

Define the following bridge objects.

### G0 — microscopic duality authority

Input:

`W_gamma` with EPRL simplicity structure and exact microscopic duality rotation.

Status: **CLOSED as microscopic structural authority**.

This does not itself imply an identical duality relation for renormalized continuum Wilson coefficients.

### G1 — renormalized continuum/boundary amplitude

Required object:

`Z_gamma^ren[B]`

obtained from a controlled sum/refinement/coarse-graining of the microscopic dynamics with the physical boundary state `B`, normalization prescription and continuum trajectory frozen.

Han's 2026 spinfoam-stack result is strong evidence that such a renormalized boundary amplitude is possible in a nontrivial Lorentzian setting, but it is not yet a same-realization map from the gamma-dual EPRL observable sector to the inflationary EFT.

Status: **PARTIAL / METHOD AUTHORITY EXISTS, SAME-REALIZATION MATCHING OPEN**.

### G2 — continuum generating/effective functional

Required object:

`Gamma_gamma[g,phi; mu]`

or an equivalent connected/1PI functional extracted from `Z_gamma^ren[B]`, with field normalization, background/state map, scale `mu`, and analytic/Lorentzian prescription fixed.

Status: **OPEN**.

No full local derivative expansion is required merely to define this object, but the relevant parity-even/odd curvature response must be extractable from it.

### G3 — parity-even/odd Wilson projection

Project the quadratic-curvature response onto the same operator basis used by the phenomenological gamma-dual EFT:

`Gamma_gamma -> {f_GB^ren(phi,mu), f_CS^ren(phi,mu), ...}`.

The projection must distinguish true Wilson coefficients from field redefinitions, topological redundancies and scheme artifacts.

Status: **OPEN**.

### G4 — renormalized duality/parameter-identity gate

Define the renormalized duality residual

`Delta_gamma(mu,phi) = 2 f_GB^ren(phi,mu)/f_CS^ren(phi,mu) - [gamma_EFT(mu) - 1/gamma_EFT(mu)]`.

The strongest one-parameter RQIR fingerprint requires

`Delta_gamma = 0`

within a frozen theoretical uncertainty **and** a matching law

`gamma_EFT(mu) = Z_gamma(mu; trajectory,B,...) gamma_micro`

with `Z_gamma` derived, not assumed.

A proof of exact/non-anomalous duality covariance could authorize `Delta_gamma=0` and possibly `Z_gamma=1` without computing every Wilson coefficient separately. Conversely, a nonzero calculable `Delta_gamma` does not automatically kill LQG phenomenology; it enlarges the fingerprint and must be propagated as a derived correction/nuisance rather than silently setting it to zero.

Status: **OPEN — this is now the minimum decisive top-down object**.

### G5 — cosmological observable projection

Once G4 is authorized, project to

`1/gamma_EFT - gamma_EFT = (pi/8)(r+8 n_T)/Pi`

with cosmological nuisance and detector likelihood.

The algebraic relation and positive-gamma structural identifiability are already controlled by KMQGB; attribution to microscopic LQG remains conditional on G1–G4.

Status: **OBSERVABLE ALGEBRA CLOSED / MICROSCOPIC ATTRIBUTION OPEN**.

## New minimal closure theorem/proof obligation

CW2-02 does **not** require a complete derivation of every term in the continuum LQG effective action.

It is sufficient to supply a same-realization derivation of the renormalized parity-sector matching object

`{gamma_micro, trajectory, B} -> {gamma_EFT, Delta_gamma, sigma_match}`

such that

1. the renormalized amplitude/generating functional is physical and normalized;
2. the GB/CS projection is defined in one operator basis;
3. `Delta_gamma` is derived or bounded;
4. the micro-to-EFT gamma map is derived;
5. the resulting uncertainty is propagated to the observable relation.

This is strictly smaller than deriving the full EFT and is therefore the preferred analytic closure target.

## Why the 2026 summation result does not already close G1–G4

The cited triangulation-independence result is obtained in a specific spinfoam-stack limit in which the bulk localizes onto an SU(2)-flat critical manifold and the renormalized finite part depends on boundary data. That result establishes a strong renormalization/continuum mechanism but does not, by itself,

- extract the scalar-coupled GB/CS Wilson sector;
- prove preservation of gamma-duality under the same renormalization;
- identify `gamma_micro` with the coefficient parameter entering the EFT;
- produce `Delta_gamma` or its uncertainty.

Therefore it is a bridge-enabling authority, not a closure certificate.

## Updated CW2-02 classification

`PROMISING_ADAPT_EXISTING__RENORMALIZED_BOUNDARY_AMPLITUDE_ROUTE_EXISTS__MINIMAL_GAMMA_DUAL_WILSON_MATCHING_OBJECT_MISSING`.

Sharpened blocker:

`RENORMALIZED_GAMMA_DUALITY_MATCHING_TRIPLE_{gamma_EFT,Delta_gamma,sigma_match}`.

## Scientific consequence

The most efficient next LQG calculation is no longer a broad continuum reconstruction. It is a symmetry/matching calculation: determine whether the exact microscopic gamma-duality descends non-anomalously to the renormalized parity-even/odd curvature response, and determine the micro-to-EFT gamma matching law.

If this closes with a single shared gamma, the LQG route becomes much stronger because geometry and primordial-GW sectors are tied by a genuinely cross-representation parameter. If it fails through an uncontrolled or freely fitted `Delta_gamma`, the apparent one-parameter rigidity collapses before expensive detector forecasting.

## Compute policy

Heavy numerical computation remains **IDLE**. The next decisive work is analytic/coarse-graining/matching authority. Numerical likelihood work remains downstream of G4.
