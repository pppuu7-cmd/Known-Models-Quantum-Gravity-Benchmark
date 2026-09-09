# KMQGB Post-Freeze Paper-IV Closure Wave 02

**RQIR standard:** Core v1.0 FROZEN.  
**Frozen denominator:** 3 high-value closure objects.  
**Current authority:** Iter176.  
**Closure coverage:** **0/3 = 0%**.

This wave contains the three exact end-to-end obligations preventing a global Paper-IV terminal decision.

| CW2 # | Object | Current state | Exact closure object |
|---|---|---|---|
| CW2-01 | O-AS | **OPEN / closest publication-triggered closure** | stable reproducible same-realization `A_s+A_t+A_u+A4` Lorentzian scalar scattering with common trajectory/normalisation/diffeo-error/comparator certificate |
| CW2-02 | O-LQG | **OPEN / active analytic front** | `SAME_REALIZATION_MULTISCALE_GAMMA_CLOSURE` tying EPRL gamma-duality, area-metric RG, `beta_Delta`, primordial `q` and birefringence `psi` in one realization |
| CW2-03 | O-CFS | **OPEN / correction generator found** | first explicit normalized CFS gravity correction tensor/coefficient vector from the causal-action expansion + full C5/GR/QFT comparator |

## CW2-01 / O-AS

Programme-level Lorentzian contact existence is no longer the unknown. The remaining exact blocker is

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

Until a stable contact-complete equation/data/error package appears, O-AS remains open and publication-triggered.

## CW2-02 / O-LQG

The preferred route is now a same-realization multiscale gamma closure.

### Primordial gamma-duality block

Define

`Delta_gamma = 2 f_GB^ren/f_CS^ren - (gamma_EFT - 1/gamma_EFT)`

and

`q = (pi/8)(r+8 n_T)/Pi = 1/gamma_EFT - gamma_EFT - Delta_gamma`.

`q` alone is structurally rank-1 in `{gamma_EFT,Delta_gamma}`.

### Area-metric RG block

A spin-foam-motivated area-metric programme now supplies a running Immirzi parameter and a Lorentzian parity-sensitive observable sector. This removes the old broad blocker that no running-gamma observable EFT route exists.

But the same-realization map from microscopic EPRL gamma-duality into this area-metric RG trajectory is still missing.

### RG preservation block

Let

`rho = 2 f_GB^ren/f_CS^ren`.

The gamma-dual surface is preserved by coarse-graining iff

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma = 0`

on `Delta_gamma=0`.

Thus `beta_gamma` alone is insufficient. The same realization must determine the parity-sector flow and therefore `beta_rho`/`beta_Delta`.

A calculable nonzero `beta_Delta` is allowed if a frozen boundary condition predicts `Delta_gamma(mu)` and the enlarged fingerprint remains identifiable; it may not be independently refitted.

### Area-metric birefringence holdout

For the positive-gamma Lorentzian branch,

`sinh(2 xi)=1/gamma`,

`psi=-(1/2) atan(tanh xi)`

give

`gamma = -cot(4 psi)`

and

`dpsi/dgamma = 1/[4(1+gamma^2)] > 0`.

Therefore, after same-realization identity and RG transport to a common scale, `(q,psi)` is structurally full rank for `{gamma,Delta_gamma}` with

`det d(q,psi)/d(gamma,Delta_gamma) = 1/[4(1+gamma^2)] > 0`.

The corresponding direct consistency diagnostic is

`Delta_gamma = 2 cot(8 psi) - q`.

This converts gamma-duality breaking into a falsifiable cross-representation observable rather than a free nuisance.

### Exact remaining O-LQG object

`SAME_REALIZATION_MULTISCALE_GAMMA_CLOSURE` must supply:

1. microscopic EPRL/spinfoam -> area-metric continuum/RG realization map;
2. `gamma_micro -> gamma_AM(mu) -> gamma_EFT(mu)` identity/running law;
3. parity-sector projection into `f_GB^ren/f_CS^ren` or an equivalent frozen RQIR basis;
4. `beta_gamma`, `beta_rho`, `beta_Delta` and uncertainty;
5. frozen `Delta_gamma` matching condition and scale transport;
6. primordial `q` and area-metric `psi` nuisance/observable models with no independent gamma refit.

Current classification:

`PROMISING_ADAPT_EXISTING__AREA_METRIC_BIREFRINGENCE_SUPPLIES_INDEPENDENT_GAMMA_HOLDOUT__SAME_REALIZATION_MULTISCALE_MAP_MISSING`.

## CW2-03 / O-CFS

The exact blocker remains

`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`.

The known correction generator is not yet an explicit normalized correction tensor/coefficient vector.

## Cross-school guardrail

Neighbouring papers or shared symbols are not one RQIR observable until their realization vectors are identical or explicitly mapped. This remains decisive for O-AS and O-LQG.

## Decision discipline

A CW2 target closes only if its missing object is supplied and terminally classified, or an explicit same-domain inconsistency is established without relying on missing calculations.

`BLOCKED` is not closure and never counts as `NEW_REQUIRED` evidence.

## Provenance

Canonical chronology after the concurrent Iter174 collision:

- Iter174: area-metric gamma-running bridge;
- Iter175: gamma-duality RG tangency;
- Iter176: area-metric birefringence gamma identifiability.

See `recovery/PROVENANCE_CORRECTION_ITER174_CONCURRENT_COLLISION.md`.

## Compute policy

Heavy computation remains idle. The active blocker is a same-realization analytic/RG/scale-composition problem. Detector forecasting becomes useful only after that bridge is frozen.
