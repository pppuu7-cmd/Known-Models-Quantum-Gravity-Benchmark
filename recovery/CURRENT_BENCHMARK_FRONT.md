# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **176**  
**Phase:** **RQIR Core v1.0 FROZEN / Paper-IV Closure Wave 02 / three exact bridges**.

## Stable metrics

- **R1 Repository readiness: 92%.**
- **R2 KMQGB methodology/material readiness: 90%.**
- **R3 external Candidate Gravity readiness: 24%.**
- **Legacy parent-search R4: 45% — PAUSED / CONDITIONAL ON PAPER IV.**
- **Post-freeze PF1 regression: 5/5 = 100% terminal.**
- **Closure Wave 02: 0/3 terminal.**

No readiness-score changes since Iter145.

## Frozen architecture

RQIR Core **v1.0 remains FROZEN** and Papers I–III remain **100% scientific/material CLOSED**. KMQGB is the active Paper-IV proving ground. Candidate Gravity remains separate and cannot tune the judge.

## Paper-IV global decision

**`NOT_YET_AUTHORIZED`**.

None of `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` has met its proof obligation. `NEW_REQUIRED` remains forbidden because major known frameworks remain completion/attribution blocked rather than excluded on complete same-domain observables.

## Closure Wave 02

### CW2-01 — O-AS

Physical non-perturbative Lorentzian scalar scattering exists and the same programme publicly reports a Lorentzian-resummed gravitational contact contribution. The remaining blocker is stable same-realization authority:

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

O-AS remains the closest **publication-triggered** closure route, but no repeated absence audit is useful until a stable contact-amplitude preprint/revision/data package appears.

### CW2-02 — O-LQG — active analytic front

The gamma-duality route now has four distinct layers of control.

#### Iter173 — duality-breaking identifiability

Define

`Delta_gamma = 2 f_GB^ren/f_CS^ren - (gamma_EFT - 1/gamma_EFT)`

and

`q = (pi/8)(r+8 n_T)/Pi = 1/gamma_EFT - gamma_EFT - Delta_gamma`.

`q` alone has rank 1 for the two unknowns `{gamma_EFT,Delta_gamma}`. Detector precision cannot lift this structural degeneracy.

#### Iter174 — area-metric bridge

Recent area-metric gravity supplies both

- a spin-foam-motivated RG flow for the Immirzi parameter; and
- a Lorentzian parity-sensitive GW/birefringence detector-facing channel.

Therefore the existence of a running-gamma observable EFT route is no longer the blocker. What remains is the same-realization map from microscopic EPRL gamma-duality into that area-metric trajectory.

#### Iter175 — RG tangency gate

Let

`rho = 2 f_GB^ren/f_CS^ren`.

The gamma-dual surface is preserved under coarse-graining iff

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma = 0`

on `Delta_gamma=0`.

Thus knowing `beta_gamma` is insufficient. A running gamma is fully compatible with exact gamma-duality only if the parity-sector ratio runs in the required lockstep. The same realization must supply `beta_rho` or equivalent Wilson flows and therefore `beta_Delta`.

#### Iter176 — independent area-metric gamma holdout

For the positive-gamma Lorentzian area-metric birefringence branch,

`sinh(2 xi)=1/gamma`,

`psi=-(1/2) atan(tanh xi)`

imply exactly

`gamma = -cot(4 psi)`, `-pi/8 < psi < 0`,

with

`d psi/d gamma = 1/[4(1+gamma^2)] > 0`.

Combining `(q,psi)` gives a full-rank Jacobian for `{gamma,Delta_gamma}`:

`det d(q,psi)/d(gamma,Delta_gamma) = 1/[4(1+gamma^2)] > 0`.

After RG transport to a common scale and only after same-realization gamma identity is established, the duality-breaking residual is directly reconstructed as

`Delta_gamma = 2 cot(8 psi) - q`.

This is a new falsifiable cross-representation consistency statistic. It removes the need to rely only on an area-gap geometry holdout for structural identifiability.

## Current exact O-LQG blocker

The active minimum object is now

**`SAME_REALIZATION_MULTISCALE_GAMMA_CLOSURE`**.

Required payload:

1. explicit microscopic EPRL/spinfoam realization -> area-metric effective/RG trajectory map;
2. derived `gamma_micro -> gamma_AM(mu) -> gamma_EFT(mu)` identity/running law;
3. same-realization parity-sector projection into `f_GB^ren/f_CS^ren` or equivalent frozen RQIR basis;
4. `beta_gamma`, `beta_rho`, hence `beta_Delta`, with regulator/state/truncation uncertainty;
5. frozen boundary condition for `Delta_gamma` and RG transport between primordial and low-energy observables;
6. observable models for primordial `q` and area-metric `psi` without independent gamma refits.

Current classification:

`PROMISING_ADAPT_EXISTING__AREA_METRIC_BIREFRINGENCE_SUPPLIES_INDEPENDENT_GAMMA_HOLDOUT__SAME_REALIZATION_MULTISCALE_MAP_MISSING`.

This is a stronger `ADAPT_EXISTING` route than at Iter173, but it is still not terminal because the cross-authority realization map has not been derived.

Authorities:

- `paper_iv/O_LQG_AREA_METRIC_GAMMA_RUNNING_BRIDGE_AUDIT_2026-09-10.md`;
- `paper_iv/O_LQG_GAMMA_DUALITY_RG_TANGENCY_GATE_2026.md`;
- `paper_iv/O_LQG_AREA_METRIC_BIREFRINGENCE_GAMMA_IDENTIFIABILITY_GATE_2026.md`;
- `code/lqg_gamma_duality_rg_tangency_reference.py`;
- `code/lqg_area_metric_birefringence_gamma_identifiability_reference.py`.

### CW2-03 — O-CFS

CFS has native surface-layer observables, total/quasilocal mass, synthetic curvature, QFT/Fock limiting dynamics and a direct geometric Einstein derivation with a systematic correction generator.

Exact blocker remains

`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`.

## Provenance note

A concurrent write created two files initially labelled Iter174. Canonical chronology is:

- Iter174 = area-metric gamma-running bridge;
- Iter175 = gamma-duality RG tangency;
- Iter176 = area-metric birefringence gamma identifiability.

Authority: `recovery/PROVENANCE_CORRECTION_ITER174_CONCURRENT_COLLISION.md`.

## Heavy compute

**IDLE.**

The decisive blocker is still analytic/provenance/RG composition. Detector numerics before the same-realization multiscale map is established would only sharpen an unauthorized composed object.

## Exact next front

1. Search specifically for an EPRL/spinfoam -> area-metric coarse-graining or matching theorem that fixes the same gamma realization.
2. If none exists, construct the minimum matching theorem ourselves: define the common realization vector, scale convention, parity projection and `beta_Delta` transport law.
3. Convert the multiscale relation into observable-space RG transport only after the parameter map is frozen.
4. Keep O-AS publication-triggered and O-CFS third priority.

Do not open another broad framework wave and do not count `BLOCKED` as evidence for `NEW_REQUIRED`.
