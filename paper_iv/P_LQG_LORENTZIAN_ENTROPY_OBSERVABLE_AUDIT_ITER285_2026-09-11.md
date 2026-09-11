# Iter285 — LQG Lorentzian entropy observable audit
Date: 2026-09-11

Primary authority: Muxin Han, *Lorentzian spinfoam gravity path integral and geometrical area-law entanglement entropy*, Phys. Rev. D 113, 084044 (2026), DOI `10.1103/kbw3-m49g`, arXiv:2510.26925.

## Prospective audit
Four independent guards were frozen before classification and executed in parallel with `fail-fast: false`, `max-parallel: 4`:
1. Bekenstein–Hawking normalization identity;
2. coupling/Barbero–Immirzi selection boundary;
3. leading 2-complex independence versus subleading graph dependence;
4. compatibility with the Iter283 UV→GR observable-transport requirement.

Scientific workflow: `34557034125` — 4/4 independent jobs + aggregate `SUCCESS`.
Methodology CI: `34557034108` — preflight + 4/4 shards + aggregate/bundle `SUCCESS`.
Aggregate digest: `sha256:f86b1ac47148f9918a9efd46c6ab7efcea85e73208ea6ace9a224326ba24f7da`.

## Results
The published large-area structure is `S = beta*a + c*log(a) + O(1)` with LQG area `A = 4*pi*gamma*lP^2*a`. Therefore the Bekenstein–Hawking normalization `S=A/(4*lP^2)` requires the exact identity `beta = pi*gamma`; the independent numerical probe verified `S/(A/lP^2)=1/4` on gamma = 0.05, 0.10, 0.25, 0.50.

All four prospective guards passed:
- `PASS_SCOPED_BH_NORMALIZATION_IDENTITY_BETA_EQUALS_PI_GAMMA`;
- `PASS_SCOPED_BH_MATCH_REQUIRES_EXPLICIT_COUPLING_GAMMA_SELECTION`;
- `PASS_LEADING_AREA_COEFFICIENT_2COMPLEX_INDEPENDENT__SUBLEADING_GRAPH_DEPENDENCE_REMAINS`;
- `PASS_HIGH_VALUE_LORENTZIAN_GRAVITATIONAL_OBSERVABLE_ANCHOR__UV_IR_TRANSPORT_STILL_MISSING`.

Aggregate classification:
`HIGH_VALUE_LORENTZIAN_ENTROPY_OBSERVABLE_ANCHOR_WITH_BH_NORMALIZATION__COUPLING_SELECTION_AND_UV_IR_TRANSPORT_REMAIN_OPEN`

## Interpretation
This is a material strengthening of the LQG/spinfoam row: a Lorentzian dynamical gravitational observable anchor exists in the stack/path-integral sector and has the correct Bekenstein–Hawking normalization once the stated coupling–gamma relation is imposed. The leading area-law coefficient is positive and independent of the selected 2-complex in the source construction.

It is not family-level closure. The BH normalization is not parameter-free because the stack coupling must be related to `gamma`; the logarithmic correction may retain boundary-graph dependence; and no published same-realization certificate transports this normalized observable through the Iter283 small-spin UV endpoint to the large-spin/refinement Einstein endpoint with common comparator and propagated uncertainties.

LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS. The canonical blocker string remains unchanged until the full D7 decision stack can be synchronized atomically.
