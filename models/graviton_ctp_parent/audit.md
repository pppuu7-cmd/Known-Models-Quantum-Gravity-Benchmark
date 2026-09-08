# T6-02 Audit — quantized-GR CTP / influence-functional parent reference

Benchmark ID: `KMQGB-T6-M02-GRAVITON-CTP-NULL`

State: TERMINAL

## Frozen setup

Use linearized quantized GR about Minkowski, with a conserved matter/source stress tensor and interaction current

`J_mn=(kappa/2) T_mn`.

Integrating out a Gaussian graviton environment gives the standard Schwinger-Keldysh / Feynman-Vernon form, up to sign and normalization conventions,

`S_IF = int J^- D_R J^+ + (i/2) int J^- N J^-`.

Definitions:

- `D_R(x,y)=i theta(x0-y0)<[h(x),h(y)]>` in the projected/gauge-consistent spin-2 sector;
- `N(x,y)=(1/2)<{h(x),h(y)}>`;
- the commutator/spectral kernel is the antisymmetrized part underlying `D_R`;
- source conservation and gauge invariance provide the corresponding Ward structure.

## Benchmark consequence

This parent object already supplies the Gaussian core of

`K_rel={N_ij,C_ij,chi_R,causal support,...}`

for physical detector/source functionals of the graviton field. Therefore the existence of

- quantum noise;
- a nonzero graviton commutator/spectral function;
- retarded response;
- causal propagation;
- correlated detector fluctuations

is **not** beyond-C5 Candidate Gravity novelty. It is the null expectation of ordinary perturbative quantum GR in the appropriate regime.

## Relation to recent detector literature

Modern low-energy graviton calculations explicitly predict correlated detector noise and interferometer vacuum response, and influence-functional/open-system calculations derive non-Markovian graviton noise and dissipation. These observations support using this CTP object as a concrete C5 null reference rather than an abstract comparator label.

## Terminal classification

`EXACT_COMPARATOR_IDENTITY`

Comparator: `C5 perturbative quantum GR`, scoped to the Gaussian linearized graviton parent object.

## Candidate Gravity lesson

A future KG residual must enter through a component or forced relation **beyond this Gaussian C5 parent** and survive the exact C5 quotient. Candidate locations include higher CTP vertices, non-Gaussian ordered structures, nonperturbative/UV relations or state-dependent correlations that cannot be absorbed into C5 EFT/state freedom.

## References

- Feynman-Vernon / Schwinger-Keldysh influence-functional framework.
- Anastopoulos, *Quantum Theory of Non-Relativistic Particles Interacting with Gravity* (1995), graviton influence functional.
- Oniga & Wang, *Quantum gravitational decoherence of light and matter* (2016), gauge-invariant influence-functional/master-equation treatment.
- Parikh & Setti, Phys. Rev. D 111, 046004 (2025), graviton noise correlations in nearby detectors.
- Carney, Karydas & Sivaramakrishnan, Phys. Rev. D 113, 106002 (2026), low-energy quantum-gravity interferometer vacuum response.
