# KMQGB Post-Freeze Paper-IV Closure Wave 02

**RQIR standard:** Core v1.0 FROZEN.  
**Frozen denominator:** 3 high-value closure objects.  
**Current authority:** Iter177.  
**Closure coverage:** **0/3 = 0%**.

| CW2 # | Object | Current state | Exact closure object |
|---|---|---|---|
| CW2-01 | O-AS | **OPEN / publication-triggered** | stable reproducible same-realization `A_s+A_t+A_u+A4` Lorentzian scalar scattering with common trajectory/normalisation/error/comparator certificate |
| CW2-02 | O-LQG | **OPEN / active analytic front** | `MULTISCALE_GAMMA_CERTIFICATE={M_same-realization,T_RG,C_observable}` |
| CW2-03 | O-CFS | **OPEN / correction generator found** | first explicit normalized CFS gravity correction tensor/coefficient vector + full comparator |

## CW2-01 / O-AS

Exact blocker:

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

Programme-level contact existence is public, but stable same-realization contact-complete authority is not yet frozen.

## CW2-02 / O-LQG

### Fixed observable structure

Define

`Delta_gamma = 2 f_GB^ren/f_CS^ren - (gamma - 1/gamma)`

and primordial

`q = (pi/8)(r+8 n_T)/Pi = 1/gamma - gamma - Delta_gamma`.

Area-metric birefringence on the positive-gamma branch gives

`gamma = -cot(4 psi)`

and therefore, after transport to a common matching scale,

`Delta_gamma = 2 cot(8 psi) - q`.

The pair `(q,psi)` is structurally full rank for `{gamma,Delta_gamma}`:

`det d(q,psi)/d(gamma,Delta_gamma)=1/[4(1+gamma^2)]>0`.

### RG structure

Let

`rho=2 f_GB^ren/f_CS^ren`.

The gamma-dual surface is preserved iff

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma`.

In observable coordinates the same identity is

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`.

Exact renormalized gamma-duality requires

`beta_q + 16 csc^2(8 psi) beta_psi = 0`.

Controlled breaking is allowed if the parent predicts a nonzero `beta_Delta` from a frozen matching condition:

`beta_q + 16 csc^2(8 psi) beta_psi = -beta_Delta_predicted`.

### Exact remaining certificate

`MULTISCALE_GAMMA_CERTIFICATE={M_same-realization,T_RG,C_observable}`

where:

- `M_same-realization` = microscopic EPRL/spinfoam -> area-metric realization map plus `gamma_micro -> gamma_AM(mu) -> gamma_EFT(mu)`;
- `T_RG` = same-realization parity projection, `beta_gamma`, `beta_rho`, `beta_Delta`, boundary condition and scale transport;
- `C_observable` = the fixed `Delta_gamma=2 cot(8 psi)-q` consistency relation and observable RG equation.

`C_observable` is now closed as mathematics/executable methodology. The missing scientific authority is `M_same-realization` and the parent-derived `T_RG`.

Current classification:

`PROMISING_ADAPT_EXISTING__MULTISCALE_GAMMA_FINGERPRINT_HAS_OBSERVABLE_RG_CLOSURE_EQUATION__SAME_REALIZATION_MAP_AND_BETA_DELTA_AUTHORITY_MISSING`.

## CW2-03 / O-CFS

Exact blocker:

`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`.

## Cross-school guardrail

Shared framework names, motivations, authors or parameter symbols do not establish one physical RQIR realization. This rule remains decisive for both O-AS and O-LQG.

## Decision discipline

`BLOCKED` is not closure and never counts as `NEW_REQUIRED` evidence.

## Provenance chronology

- Iter174 = area-metric gamma-running bridge;
- Iter175 = gamma-duality RG tangency;
- Iter176 = area-metric birefringence gamma holdout;
- Iter177 = observable-space RG transport.

See `recovery/PROVENANCE_CORRECTION_ITER174_CONCURRENT_COLLISION.md`.

## Compute policy

Heavy computation remains idle. The unresolved O-LQG pieces are a same-realization derivation and RG attribution problem; detector numerics are downstream.
