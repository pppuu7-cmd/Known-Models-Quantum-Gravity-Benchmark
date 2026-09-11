# Asymptotic Safety self-consistent Lorentzian graviton spectral audit — Iter280

Date: 2026-09-11
Family: `ASYMPTOTIC_SAFETY`
RQIR Core: `v1.0 FROZEN`
D7 stage: `D7-S2 STRICT_TIER1_TERMINAL_COVERAGE`

## Primary object

Jan M. Pawlowski, Manuel Reichert, Jonas Wessely, **Self-consistent graviton spectral function in Lorentzian quantum gravity**, *Physics Letters B* **880** (2026) 140844, published 2026-08-13, DOI `10.1016/j.physletb.2026.140844`, arXiv:`2507.22169v1`.

This peer-reviewed work computes a self-consistent Lorentzian graviton spectral function using the spectral renormalisation group and on-shell renormalisation. The full non-perturbative spectral function, including the scattering continuum, is fed back into the diagrams in the stated approximation.

The reported result is a positive, normalisable graviton spectral function with a massless one-graviton peak plus a multi-graviton continuum. The ultraviolet scattering tail behaves as

`f_h(lambda) ~ c_UV / [lambda^2 log^3(lambda^2)]`,

and the reported unnormalised total spectral weight is `z_spec ≈ 1.486`. After the physical field rescaling, the spectral sum rule has unit total weight.

## Source-declared scope limits

The source itself prevents a family-level unitarity promotion:

- the calculation studies the transverse-traceless fluctuation graviton in the stated fluctuation-field setup;
- the vertices use an Einstein-Hilbert-type approximation;
- `Lambda_k=0` is used in the current computational scheme;
- the Newton-coupling flow is imported from a `p=0` three-point-function flow with a Litim regulator rather than derived in the same on-shell scheme;
- the authors explicitly state that the fluctuation-graviton states are **not diffeomorphism invariant and are not part of the physical Hilbert space**;
- scattering cross sections are presented as a future application rather than a completed observable in this paper;
- the publisher states that the numerical data are available on request, and no article-specific public numerical dataset or reference implementation was located in this audit.

Therefore positivity plus a unit spectral sum rule in this realization is a strong scoped unitarity/analyticity building block, but it is not by itself a complete proof of physical-Hilbert-space unitarity for the Asymptotic-Safety family.

## Parallel KMQGB computational audit

Workflow: `asymptotic-safety-spectral-unitarity-audit`
Run: `34553743544`
Compute head: `415eed1991ba5a289e6a26226de397fb301cf1c6`

Four independent probes were executed concurrently and aggregated only after their dependency barrier:

1. Eq. (23)–(25) Newton-coupling fixed-point / trajectory consistency;
2. UV spectral-tail integrability under the paper's spectral measure;
3. spectral-weight decomposition implied by reported `z_spec≈1.486`;
4. exact IR coefficient relation between `A_h=61/(60 pi)` and the `61/30` scattering-tail onset.

Result: **4/4 independent jobs SUCCESS + aggregate SUCCESS**.
Aggregate artifact digest: `sha256:a822813cd95a0a5987b79920fbcbed1f5cf3b5798ef2170f2f71c6b226a6a7f4`.

Methodology CI on the same compute head: run `34553743421`, preflight + 4/4 methodology shards + aggregate/bundle `SUCCESS`.

## Quantitative cross-checks

### RG fixed point and trajectory
The paper's beta function

`d_t g = 2 g - [2499/(380 pi)] g^2`

has the exact non-Gaussian fixed point

`g_* = 760 pi / 2499 = 0.9554263372261876`.

The fixed-point beta residual is exactly zero in double precision. A finite-difference check of the published trajectory

`g(k) = g_* k^2 / [k^2 + g_* M_pl^2]`

against the beta function over `k/M_pl = 10^-3 ... 10^3` gives maximum relative residual `1.6510330357476112e-06`, dominated by the numerical derivative rather than an equation mismatch.

### UV normalisability
For the paper's asymptotic tail `1/[lambda^2 log^3(lambda^2)]`, the spectral-weight measure reduces asymptotically to an integral proportional to

`∫ d lambda / [lambda log^3(lambda^2)]`,

which converges. With unit prefactor and lower scale `lambda=10`, the exact infinite-upper-limit tail integral is `0.011788231063225867`; truncating only at `10^32` already captures `0.9990234375` of that asymptotic tail contribution.

The corresponding simple-log alternative `1/[lambda^2 log(lambda^2)]` does not converge, reproducing the source's qualitative distinction.

### Spectral-weight decomposition
Using the reported `z_spec≈1.486`, the physical rescaling implies, algebraically,

- pole-weight fraction ≈ `0.6729475100942126`;
- continuum-weight fraction ≈ `0.32705248990578734`;
- total = `1.0`.

This is a consequence of the reported `z_spec`; it is **not** an independent numerical recomputation of the spectral integral that produced `1.486`.

### IR coefficient
The exact paper relation

`2 pi * [61/(60 pi)] = 61/30`

is reproduced with relative floating error `2.1840452943445704e-16`. Numerically, `A_h=0.32361505095352056` and the tail onset is `2.033333333333333`.

## Reproducibility boundary

The analytic/internal consistency layer is reproducible from the published equations. The complete numerical spectral curve is not independently reproduced in Iter280 because no public spectral dataset or article-specific reference implementation was located, while the publisher states data are available on request.

Current reproducibility classification for the full curve:

`BLOCKED_PUBLIC_NUMERICAL_DATA_OR_REFERENCE_IMPLEMENTATION_FOR_FULL_CURVE_REPRODUCTION`

This is a reproducibility limitation, not evidence that the published curve is wrong.

## Scoped result

`PASS_SCOPED_POSITIVE_NORMALISABLE_LORENTZIAN_TT_GRAVITON_SPECTRAL_FUNCTION_WITH_UNIT_WEIGHT__NOT_PHYSICAL_HILBERT_SPACE_NOT_CONTACT_COMPLETE_NOT_FULL_CURVE_INDEPENDENTLY_REPRODUCED`

Family-level status remains:

`BLOCKED_MISSING_REQUIRED_OBJECT`

The active terminalization blocker remains:

`BLOCKED_PENDING_PUBLIC_CONTACT_COMPLETE_S_PLUS_T_PLUS_U_PLUS_A4_LORENTZIAN_SCATTERING_CERTIFICATE_WITH_FORWARD_LIMIT_TREATMENT_APPROXIMATION_UNCERTAINTY_BUDGET_AND_SAME_DOMAIN_COMPARATORS`

## D7 consequence

- Tier-1 census remains `15`.
- strict terminal coverage remains `1/15`.
- candidate-family terminal coverage remains `0/14`.
- `ASYMPTOTIC_SAFETY` remains nonterminal.
- D7-S2 remains `NOT_CLOSED`.
- D7-S3 remains `NOT_CLOSED`.
- D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5 remains `NOT_AUTHORIZED`.
- Candidate Gravity remains inactive at canonical R3 `24%`.

## Methodological consequence

Iter280 does not require a new RQIR-Core rule. It independently corroborates Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` and claim-domain separation: spectral positivity, spectral normalisability, physical-state construction, diffeomorphism-invariant Hilbert-space membership, full scattering unitarity and contact-complete amplitudes are related but non-interchangeable closure axes.

## Publication handoff

- **Paper III:** `NOT_NEEDED` as a new rule. The result may serve as optional corroboration for the Iter277 multi-axis/claim-domain strengthening, but Paper III should not become an Asymptotic-Safety case study.
- **Paper IV:** `READY`. Add this peer-reviewed Lorentzian spectral result as a major positive Asymptotic-Safety sub-result; include the numerical consistency audit, explicitly state the physical-Hilbert-space and reproducibility boundaries, and preserve the independent Iter274 `s+t+u+A4` blocker.

## Conclusion

Iter280 materially strengthens Asymptotic Safety on the Lorentzian spectral/analyticity/unitarity-building-block axis without changing the terminal count. The strongest defensible statement is that a positive normalisable TT fluctuation-graviton spectral function with unit total weight has been obtained in the stated on-shell spectral-RG approximation; it is not yet a family-level physical unitarity certificate and does not close the contact-complete scattering gate.
