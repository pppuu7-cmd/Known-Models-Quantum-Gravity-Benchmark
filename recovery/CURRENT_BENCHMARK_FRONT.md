# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **177**  
**Phase:** **RQIR Core v1.0 FROZEN / Paper-IV Closure Wave 02 / multiscale gamma front**.

## Stable metrics

- **R1 Repository readiness: 92%.**
- **R2 KMQGB methodology/material readiness: 90%.**
- **R3 external Candidate Gravity readiness: 24%.**
- **Legacy parent-search R4: 45% — PAUSED / CONDITIONAL ON PAPER IV.**
- **Post-freeze PF1 regression: 5/5 = 100% terminal.**
- **Closure Wave 02: 0/3 terminal.**

No readiness-score changes since Iter145.

## Frozen architecture

RQIR Core **v1.0 remains FROZEN**. KMQGB remains the active Paper-IV known-model proving ground. `BLOCKED` is not evidence for `NEW_REQUIRED`.

## Paper-IV global decision

**`NOT_YET_AUTHORIZED`**.

The evidence increasingly strengthens an `ADAPT_EXISTING` route but no terminal global category is yet authorized.

## CW2-01 — O-AS

Exact blocker remains

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

O-AS is publication-triggered; do not repeat absence audits until new stable contact authority appears.

## CW2-02 — O-LQG — active front

### Iter173 — structural degeneracy

`q = 1/gamma - gamma - Delta_gamma`

is rank-1 for `{gamma,Delta_gamma}` when used alone.

### Iter174 — area-metric bridge

A spin-foam-motivated area-metric programme supplies running Immirzi dynamics plus a Lorentzian parity/birefringence observable channel. The broad absence of a running-gamma observable route is therefore closed.

### Iter175 — RG tangency

For

`rho = 2 f_GB^ren/f_CS^ren`,

renormalized gamma-duality is preserved iff

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma = 0`

on the gamma-dual surface. `beta_gamma` alone is insufficient; the same realization must provide the parity-sector flow and therefore `beta_Delta`.

### Iter176 — independent gamma holdout

The positive-gamma area-metric birefringence relation is exactly invertible:

`gamma = -cot(4 psi)`.

Together with primordial `q`, it gives

`Delta_gamma = 2 cot(8 psi) - q`

after RG transport to a common scale, and

`det d(q,psi)/d(gamma,Delta_gamma) = 1/[4(1+gamma^2)] > 0`.

Thus a same-realization `(q,psi)` pair is structurally sufficient to separate gamma from duality breaking.

### Iter177 — observable-space RG transport

The Iter175 RG condition can now be written directly in observable coordinates:

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`.

For exact renormalized gamma-duality,

**`beta_q + 16 csc^2(8 psi) beta_psi = 0`.**

For controlled breaking,

`beta_q + 16 csc^2(8 psi) beta_psi = -beta_Delta_predicted`.

This is the fixed multiscale consistency equation that a future same-realization bridge must satisfy. It prevents the invalid shortcut of combining a running low-energy gamma/psi with a frozen primordial q unless the resulting `beta_Delta` is explicitly predicted.

## Exact O-LQG closure certificate

The active object is now compactly factorized as

**`MULTISCALE_GAMMA_CERTIFICATE = {M_same-realization, T_RG, C_observable}`**.

- `M_same-realization`: EPRL/spinfoam -> area-metric realization/provenance map and `gamma_micro -> gamma_AM(mu) -> gamma_EFT(mu)`.
- `T_RG`: same-realization parity projection, `beta_rho`, `beta_gamma`, `beta_Delta`, boundary condition and scale transport.
- `C_observable`: `Delta_gamma=2 cot(8 psi)-q` plus the observable RG transport equation.

`C_observable` is now fixed and executable. What remains genuinely missing is `M_same-realization` and the parent-derived `T_RG` authority.

Current classification:

`PROMISING_ADAPT_EXISTING__MULTISCALE_GAMMA_FINGERPRINT_HAS_OBSERVABLE_RG_CLOSURE_EQUATION__SAME_REALIZATION_MAP_AND_BETA_DELTA_AUTHORITY_MISSING`.

Authorities:

- `paper_iv/O_LQG_AREA_METRIC_GAMMA_RUNNING_BRIDGE_AUDIT_2026-09-10.md`;
- `paper_iv/O_LQG_GAMMA_DUALITY_RG_TANGENCY_GATE_2026.md`;
- `paper_iv/O_LQG_AREA_METRIC_BIREFRINGENCE_GAMMA_IDENTIFIABILITY_GATE_2026.md`;
- `paper_iv/O_LQG_MULTISCALE_OBSERVABLE_RG_TRANSPORT_GATE_2026.md`;
- `code/lqg_multiscale_observable_rg_transport_reference.py`.

## CW2-03 — O-CFS

Exact blocker remains

`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`.

## Provenance

Canonical chronology after the concurrent collision:

- Iter174 = area-metric gamma-running bridge;
- Iter175 = gamma-duality RG tangency;
- Iter176 = area-metric birefringence gamma identifiability;
- Iter177 = observable-space RG transport.

## Heavy compute

**IDLE.** The remaining blockers are same-realization derivation and RG attribution. Detector numerics cannot substitute for either.

## Exact next front

The next useful work is no longer additional identifiability algebra. Search for or construct the missing `M_same-realization`:

1. identify the precise spin-foam/area-metric coarse-graining map and common field/coupling basis;
2. determine whether the area-metric running Immirzi parameter descends from the same microscopic EPRL gamma;
3. derive the parity-sector projection needed for `beta_rho` and therefore `beta_Delta`;
4. only then attach resource/detector forecasting to the already-fixed observable closure equation.

Do not open another broad framework wave and do not count `BLOCKED` as `NEW_REQUIRED` evidence.
