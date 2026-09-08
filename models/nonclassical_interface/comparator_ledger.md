# T3-03 Comparator Ledger — nonclassical gravitational interface

Benchmark target: `KMQGB-T3-M03-NONCLASSICAL-INTERFACE`  
Primary setup: `NC-TWOMASS-BRANCH-MEDIATOR-001`  
Channel readout: `NC-OPTOMECH-GRAVITY-CHANNEL-001`  
Commutator readout: `NC-GRAV-UNSYM-NOISE-QUBIT-001`

## Frozen vector

`I_NC={Theta,E_AB,Q_channel,chi_R^grav,A_comm/rho_comm,N_grav,K3_plus,Ward/contact,mediator-null controls}`.

The entries are scoped to explicit comparator realizations. They are not claims about every imaginable hybrid model.

## Operational commutator coordinate

For a Hermitian gravity-sensitive generalized force `F`, define

`S_FF(omega)=integral dt exp(i omega t)<F(t)F(0)>`.

Freeze

`rho_comm(omega)=S_FF(+omega)-S_FF(-omega)`

and, for a weak narrow-band two-level probe,

`A_comm(Omega)=[Gamma_down-Gamma_up]/[Gamma_down+Gamma_up]`.

After detector/background calibration this equals

`[S(+Omega)-S(-Omega)]/[S(+Omega)+S(-Omega)]`

in the ideal weak-coupling convention.

A stationary real classical stochastic force has an even autocorrelation and hence symmetric autospectrum, so its intrinsic mediator contribution has

`rho_comm=0`, `A_comm=0`.

A raw optical sideband ratio is **not** accepted as this observable because measurement/backaction interference can mimic asymmetry classically.

## C2 — linear Gaussian stochastic gravity

Frozen scope: Einstein–Langevin / linear classical stochastic metric.

- `Theta`: can mimic mean gravitational phase.
- `chi_R`: nonzero.
- `N`: nonzero.
- intrinsic mediator `A_comm=0` for the stationary real classical metric-force autospectrum.
- `K3_plus=0` in the strictly linear Gaussian realization only.
- gravity-only local shared-classical-noise map is a mixture of conditioned local maps and cannot create probe entanglement from separable input in the frozen setup.
- no gravity-only non-EB quantum communication channel.

Thus C2 can mimic `{Theta,chi_R,N}` but not the combined gravity-only `{non-EB,A_comm!=0}` target in this scoped realization.

## C3 — KTM measurement-feedback gravity

Frozen scope: local continuous measurement plus classical feedback.

- mean Newtonian interaction / `Theta` can be reproduced;
- `chi_R` nonzero;
- compulsory decoherence/noise tied to interaction;
- no fundamental gravitational mediator operator commutator;
- ideal mediator-leg `A_comm=0` after detector/backaction subtraction;
- standard Gaussian realization has no connected higher cumulants beyond second order;
- mediator is measure-and-feed-forward / entanglement-breaking and non-entangling in the declared sector.

Therefore C3 predicts a classical-channel relation: interaction is accompanied by a minimum noise/decoherence burden and the mediator does not supply a non-EB quantum channel.

## C3b — covariant postquantum classical gravity

Frozen scope: Oppenheim–Weller-Davies 2026 covariant classical-field CQ path-integral construction.

- classical metric may have stochastic response/noise;
- no fundamental noncommuting metric operator;
- classical higher cumulants are not generically zero;
- intrinsic stationary classical mediator `A_comm=0` in the autospectral test;
- the 2026 path-integral theorem proves the classical field cannot create entanglement in the local CQ setting described by the source.

Consequently a **gravity-attributed** non-EB channel plus nonzero calibrated `A_comm` excludes this scoped C3b mediator, provided hidden C4/C6 quantum transfer is absent.

## C4 — ordinary quantum mediator / quantum matter nuisance

C4 can produce all of the apparently strongest individual quantum-looking components:

- entanglement;
- non-EB quantum communication;
- nonzero unsymmetrized spectral asymmetry / commutator;
- higher cumulants.

Therefore `{Q_channel non-EB,A_comm!=0}` is **not gravity-specific without mediator attribution**.

The required C4 ledger includes electromagnetic, optical, phononic/material, Casimir/patch, common-bath, control/readout and quantized-matter transfer channels.

## C6 — quantum source statistics + classical gravitational interface

Quantum source preparation can imprint nonclassical detector statistics while the gravitational interface remains classical. Source-coherence nulls and causal/inter-probe attribution are therefore mandatory.

## Terminal comparator result

The following lower-dimensional targets are rejected as sufficient KG fingerprints:

`{Theta}` alone — classical GR/C0 calibration can mimic.

`{Theta,chi_R,N}` — C2/C3/C3b can mimic substantial parts.

`K3_plus!=0` — nonlinear/non-Gaussian classical stochastic models can mimic.

`E_AB>0` or `Q_channel non-EB` — strong against pure local classical-spacetime mediation but can be produced by C4/C6.

`A_comm!=0` — strong against a stationary real classical mediator but can be produced by ordinary quantum C4 channels and can be spuriously inferred from detector backaction if the estimator is not calibrated.

The strongest architecture that survives the **pure classical-spacetime comparator quotient** is

`I_survive={Q_channel non-EB, A_comm/rho_comm, chi_R-N relation, Theta geometry, Ward/contact}`

plus explicit

`mediator attribution against C4/C6`.

## What has and has not been established

Established:

- there is a concrete multi-readout architecture whose non-EB + commutator-sensitive components cannot be supplied by the frozen C2/C3/C3b classical gravitational mediators;
- the architecture can be stated operationally without assuming a quantum metric at the definition stage;
- C4/C6 are identified explicitly as attribution adversaries rather than silently ignored.

Not established:

- no actual Candidate Gravity parent dynamics has yet predicted a nonzero value;
- no globally unique QG residual has been measured or derived;
- no finite experimental nuisance envelope for every C4/C6 channel has yet been demonstrated.

## Candidate Gravity design target

A future KG model should derive a rigid relation

`F(Theta,Q_channel,A_comm,chi_R,N,K3_plus,Ward/contact)=0`

from one parent dynamics, and that relation should remain inconsistent with all admissible C2/C3/C3b fits while C4/C6 are eliminated by mediator-attribution controls.

## Sources

1. Hu & Verdaguer, stochastic gravity / Einstein–Langevin framework.
2. Kafri, Taylor & Milburn, classical communication/noise bound for Newtonian gravity.
3. Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), covariant CQ path integral and no-entanglement theorem through the classical field.
4. Clerk et al., Rev. Mod. Phys. 82, 1155 (2010), unsymmetrized quantum noise spectroscopy.
5. Mari, Zippilli & Vitali, Phys. Rev. D 113, L021905 (2026), gravity-induced channel / entanglement-breaking criterion.
6. Børkje, Phys. Rev. A 94, 043816 (2016), detector dependence of sideband asymmetry.
7. Novotny et al., Phys. Rev. A 106, 043511 (2022), classical backaction/interference sideband mimic.
