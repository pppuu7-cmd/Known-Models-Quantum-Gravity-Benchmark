# T3-05 Audit — concrete discrete/Lorentzian QG observable

Benchmark ID: KMQGB-T3-M05-CDT  
Concrete realization ID: `CDT-4D-CURVATURE-CORRELATOR-GEON-2026-001`  
Role: concrete nonperturbative/discrete quantum-gravity observable control  
State: **TERMINAL — `BLOCKED_MISSING_REQUIRED_OBJECT`**

## Terminal decision

The 2026 four-dimensional CDT curvature-correlator calculation is concrete and reproducible enough to establish a meaningful **finite-regulator subresult**:

- different curvature operators show a common exponential massive-like falloff over an intermediate distance window;
- the extracted masses agree between the operator choices within quoted errors;
- the authors report no statistically significant volume dependence across the tested ensembles for the averaged early-time masses;
- the mass changes during the rapid cosmological expansion phase, suggesting a real background/phase dependence rather than a universal constant mass in the explored ensembles.

However, the benchmark's hard discriminator requires a regulator/continuum and physical Lorentzian observable map. The published work does not provide a continuum extrapolation along a line of constant physics for this geon mass, nor a derivation identifying the Wick-rotated Euclideanized correlator falloff with a real-time Lorentzian asymptotic/spectral pole.

Therefore T3-05 is terminally classified

`BLOCKED_MISSING_REQUIRED_OBJECT`

at

`CDT_GEON_CONTINUUM_AND_LOR_REALTIME_MAP`.

This is not a failure of CDT and does not erase the finite-lattice geon-like evidence.

## Frozen realization and observable

Use Maas, Plätzer & Pressler, *Hints for a geon from causal dynamic triangulations*, Phys. Lett. B 879 (2026) 140600.

For curvature operators `O_i`, define the connected correlators in the published CDT distance convention,

`C_ij(r)=<O_i(x)O_j(y)>_c`.

The fitted intermediate-distance behavior is massive-like,

`C(r) ~ A(r) exp(-m_eff r)`.

The benchmark vector is

`I_CDT={massive_window,operator_independence,m_eff,volume_dependence,time/phase_dependence,continuum_scaling,Lorentzian_map}`.

## Published numerical subresult

The paper reports, averaging over the early cosmological-time window `0 <= tau < 12`, masses approximately

- for the `Q`-type correlator: `0.18(1), 0.16(1), 0.17(3)` for `N_simp = 80k,160k,320k`;
- for the `Q^2`-type correlator: `0.14(1), 0.17(1), 0.15(3)` for the same volumes.

The two operator families therefore overlap within quoted uncertainties, and the tested volumes show no statistically significant monotonic volume dependence in these averaged values.

The authors estimate the corresponding physical scale at roughly `~0.09 M_Pl` using their lattice-scale conversion, while explicitly describing the geon interpretation only as a **hint**.

They also find a pronounced change of the fitted mass during the rapid expansion phase of the simulated de-Sitter-like universe.

These are positive finite-regulator facts; they are not yet a continuum particle-state certificate.

## Reproducibility update

A 2026 Zenodo release supplies stochastic samples for the geon-propagator analysis across multiple volume data sets. This improves reproducibility of the finite-ensemble result.

It does **not** supply the missing continuum trajectory or Lorentzian spectral reconstruction, so it does not change the terminal blocking gate.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics/path integral | PASS_SCOPED | explicit causal CDT path integral / Monte Carlo construction |
| F1 classical limit | PASS_PARTIAL | extended de-Sitter-like macroscopic phase exists |
| F2 consistency | PASS_PARTIAL | causal construction/Wick rotation explicit; full continuum physical-state questions broader |
| F3 observable | PASS_SCOPED | explicit 4D curvature-correlator family measured |
| F4 distinction | PASS_PARTIAL_FINITE_REGULATOR | common massive window and operator agreement survive basic operator/volume checks in tested ensembles |
| F5 hard discriminator | **BLOCKED_MISSING_REQUIRED_OBJECT** | no continuum scaling + physical Lorentzian pole/map |
| F6 identifiability | BLOCKED | finite-regulator composite/lattice alternatives remain |
| F7 resources | N/A | numerical/theory benchmark |

## Why finite volume checks are not enough

The absence of significant differences between 80k/160k/320k simplices in one family of ensembles is encouraging but does not substitute for a continuum limit. A true continuum statement needs controlled lattice-spacing variation/renormalization and a line of constant physics, not merely larger four-volume at a fixed bare setup.

Similarly, CDT's microscopic histories are Lorentzian, but the Monte Carlo observable is evaluated after the theory's Wick rotation. A decaying Euclideanized correlator can define a correlation scale without automatically proving a real-time stable particle pole.

## Candidate Gravity design lesson

A numerical signal becomes a KG design prior only after its **regulator map is part of the observable definition**.

For future KG:

> operator independence and finite-volume stability are useful robustness checks, but they do not replace continuum scaling, physical-state reconstruction, or detector/real-time mapping.

This guards against promoting a regulator-stable artifact into a fundamental degree of freedom.

## Reopen condition

Reopen T3-05 when there is a public analysis that supplies at least one of the following in a form strong enough to close the benchmark vector:

1. continuum scaling of the same geon correlator/mass along a controlled CDT trajectory;
2. a justified reconstruction from the measured Wick-rotated correlator to a Lorentzian spectral/asymptotic-state statement;
3. an equivalent regulator-independent physical observable tied to the same state.

## Terminal completion

**100% — terminally classified as BLOCKED, with a positive finite-regulator subresult.**

## Sources

1. A. Maas, S. Plätzer, F. Pressler, Phys. Lett. B 879 (2026) 140600.
2. J. Ambjørn, R. Loll, arXiv:2604.05641 (2026), CDT framework review.
3. Maas–Plätzer–Pressler stochastic sample data release, Zenodo 2026.
