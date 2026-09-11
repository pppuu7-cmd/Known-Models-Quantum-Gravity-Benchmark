# Iter288 — LQG semiclassical hierarchy / entropy-domain overlap sensitivity audit
Date: 2026-09-11

Primary physics inputs:
- Han, *Semiclassical Analysis of Spinfoam Model with a Small Barbero-Immirzi Parameter*, Phys. Rev. D 88, 044051 (2013): semiclassical hierarchy `1 << gamma^-1 << lambda << gamma^-2`.
- Han, *Lorentzian spinfoam gravity path integral and geometrical area-law entanglement entropy*, Phys. Rev. D 113, 084044 (2026): Bekenstein–Hawking-compatible entropy sector with `0 < gamma ≲ 1/2` after the stated coupling selection.

## Prospective sensitivity rule
The asymptotic symbol `<<` has no unique numerical threshold. To avoid inventing one, Iter288 introduced a family of operational sensitivity separations `R>1`:
- `lambda >= R/gamma`,
- `lambda <= 1/(R*gamma^2)`.

A nonempty lambda window exists iff `gamma < 1/R^2`. This is a robustness/sensitivity diagnostic only, not a physical bound on `gamma`.

Four independent jobs evaluated `R = 2, 3, 5, 10` with `fail-fast:false`, `max-parallel:4`.
Scientific workflow `34557797109`: 4/4 probes + aggregate `SUCCESS`.
Methodology CI `34557797084`: `SUCCESS`.
Reproducibility release `34557875010`: `SUCCESS`.
Aggregate digest: `sha256:57986e696cfb7e139bcb75a9cdf9c3f48b65e0f4120b567b624aa4a6b5945f6a`.

## Results
Sensitivity critical values:
- `R=2` -> `gamma_critical=0.25`;
- `R=3` -> `gamma_critical=1/9 ≈ 0.1111111111`;
- `R=5` -> `gamma_critical=0.04`;
- `R=10` -> `gamma_critical=0.01`.

Aggregate classification:
`QUANTIFIED_SEMICLASSICAL_HIERARCHY_OVERLAP__BH_RANGE_CONTAINS_SMALL_GAMMA_SUBDOMAIN_WITH_REGGE_WINDOW_BUT_NO_UNIQUE_NUMERICAL_DOUBLE_LESS_THAN_THRESHOLD`

## Interpretation
The BH-compatible entropy range is not disjoint from the small-`gamma` Regge/Einstein asymptotic sector: for every tested hierarchy-separation convention there is a nonempty sufficiently small-`gamma` subdomain with an admissible `lambda` window. Stronger separation demands progressively smaller `gamma`.

This does **not** supply a physical transition scale, a unique threshold, a running law for `gamma`, or the missing controlled UV→IR trajectory. It therefore strengthens domain compatibility but does not close the LQG same-realization transport blocker.

LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS.
