# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **173**  
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

RQIR Core **v1.0 remains FROZEN** and Papers I–III remain **100% scientific/material CLOSED**. KMQGB is the active Paper-IV proving ground. Candidate Gravity remains separate; its latest directly refreshed authority is Iter675 / 24% with no promotable ansatz or robust residual.

## Paper-IV global decision

**`NOT_YET_AUTHORIZED`**.

None of `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` has met its proof obligation. `NEW_REQUIRED` remains forbidden because major known frameworks are still completion/attribution blocked rather than excluded on complete same-domain observables.

## Closure Wave 02

Authority: `post_freeze_paper_iv_closure_wave_02/README.md`.

### CW2-01 — O-AS

Physical non-perturbative Lorentzian scalar scattering exists. Iter171 established that the same Chiesa/Reichert programme publicly reports a gravitational contact contribution resummed directly in Lorentzian signature, so programme-level contact existence is no longer the blocker.

Current classification:

`PROMISING_SAME_PROGRAMME_CONTACT_COMPLETE_PRESENTATION__REPRODUCIBLE_SAME_REALIZATION_CERTIFICATE_MISSING`.

Exact blocker:

**`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`**.

Authority: `paper_iv/O_AS_CONTACT_PUBLICATION_AUTHORITY_REFRESH_2026-09-10.md`.

### CW2-02 — O-LQG — active analytic front

The gamma-duality paper supplies exact microscopic EPRL duality structure and an identifiable primordial observable relation but explicitly states that direct top-down derivation of the effective action from non-perturbative `W_gamma` is missing.

Iter172 decomposed the missing bridge into `G0..G5` and reduced the broad top-down task to the renormalized matching triple

`{gamma_EFT, Delta_gamma, sigma_match}`

with

`Delta_gamma = 2 f_GB^ren/f_CS^ren - (gamma_EFT - 1/gamma_EFT)`.

Iter173 then proves a new structural result. The generalized primordial observable combination

`q = (pi/8)(r+8 n_T)/Pi = 1/gamma_EFT - gamma_EFT - Delta_gamma`

is rank-1 in the two unknowns `{gamma_EFT,Delta_gamma}`. Therefore no increase in primordial detector precision can identify both parameters without independent theoretical or geometric information.

If a geometry observable has `a_* = K gamma` and a prior matching theorem establishes a **shared gamma** across geometry and EFT, the joint Jacobian

`J = [[-1-1/gamma^2,-1],[K,0]]`

has

`det J = K`,

so the geometry block restores full structural identifiability for `K != 0`.

If instead `gamma_geom` is left independent from `gamma_EFT`, two observables constrain three parameters and underidentification remains. Thus the parameter-identity gate is mathematically necessary, not merely a bookkeeping requirement.

Current classification:

`PROMISING_ADAPT_EXISTING__GAMMA_DUALITY_BREAKING_DEGENERACY_EXPLICIT__IDENTIFIABLE_RENORMALIZED_MATCHING_NEEDED`.

Sharpened minimum object:

**`IDENTIFIABLE_RENORMALIZED_GAMMA_MATCH = {gamma_micro->gamma_EFT, Delta_gamma prior/prediction, optional gamma_geom map}`**.

Strongest closure route:

- prove non-anomalous renormalized gamma-duality / `Delta_gamma=0` with controlled uncertainty; and
- derive `gamma_micro -> gamma_EFT -> gamma_geom` identity/running map.

A nonzero predicted `Delta_gamma` is also acceptable if it is not freely refitted and the enlarged cross-representation fingerprint remains identifiable.

Authorities:

- `paper_iv/O_LQG_GAMMA_TOPDOWN_MATCHING_DECOMPOSITION_2026.md`;
- `paper_iv/O_LQG_GAMMA_DUALITY_BREAKING_IDENTIFIABILITY_GATE_2026.md`;
- `code/lqg_gamma_duality_breaking_identifiability_reference.py`.

### CW2-03 — O-CFS

CFS has native surface-layer observables, total/quasilocal mass, synthetic curvature, QFT/Fock limiting dynamics and a direct 2026 geometric derivation of Lorentzian Einstein equations from the causal action.

The latest paper supplies a **systematic correction generator** and classifies Planck-order, osculation/torsion, regularizing-vector and modified-measure corrections. But it states that these corrections still need to be worked out in detail.

Exact blocker:

**`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`**.

A generic local higher-curvature correction will be absorbed by full gravitational EFT/C5 unless CFS fixes a cross-coefficient/shared-background relation or a genuinely non-C5 structure.

## Cross-school composition rule

Authority: `protocol/PAPER_IV_SAME_REALIZATION_COMPOSITION_GATE.md`.

Neighbouring papers in one school are not one physical RQIR object until their realization vectors are identical or explicitly mapped. The same rule independently matters for AS contact completion and LQG gamma attribution.

## Heavy compute

**IDLE.**

Current blockers are analytic/authority/composition problems. Heavy numerical work is not authorized until one CW2 physical object is prospectively frozen and a computation can change its terminal classification.

## Exact next front

1. O-AS remains the closest publication-triggered closure target; re-audit only on a new stable contact-amplitude authority or data package.
2. Active research effort remains O-LQG: search for a renormalized duality Ward/nonrenormalization statement or derive the leading allowed `Delta_gamma`/gamma-running matching structure.
3. Do not start detector forecasting until `Delta_gamma` and parameter identity are independently controlled.
4. O-CFS remains third priority until a first explicit normalized correction tensor appears.

Do not open another broad framework wave and do not count `BLOCKED` as evidence for `NEW_REQUIRED`.
