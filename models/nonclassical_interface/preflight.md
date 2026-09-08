# T3-03 Audit — nonclassical gravitational interface architecture

Benchmark ID: `KMQGB-T3-M03-NONCLASSICAL-INTERFACE`  
Primary setup: `NC-TWOMASS-BRANCH-MEDIATOR-001`  
Channel readout: `NC-OPTOMECH-GRAVITY-CHANNEL-001`  
Commutator readout: `NC-GRAV-UNSYM-NOISE-QUBIT-001`  
State: **TERMINAL — `PASS_RQIR_GATE`**  
Objective: **`CLASSICAL_SPACETIME_DISCRIMINATOR_ARCHITECTURE_ESTABLISHED`**

## Terminal result

T3-03 asked whether a concrete nonclassical-interface observable can be designed that is stronger than force/noise/decoherence and survives the frozen C2/C3/C3b classical-spacetime comparators.

The answer is **yes at architecture level**.

The frozen architecture combines:

1. gravitational branch-phase geometry `Theta`;
2. a gravity-induced channel test `Q_channel` classified as entanglement-breaking or non-entanglement-breaking;
3. a commutator-sensitive unsymmetrized-spectrum estimator `A_comm`/`rho_comm`;
4. ordinary retarded response `chi_R` and symmetrized noise `N`;
5. Ward/contact consistency and mediator-null controls;
6. higher cumulants as supporting rigidity information rather than a standalone quantum certificate.

The resulting vector is

`I_NC={Theta,E_AB,Q_channel,chi_R,A_comm/rho_comm,N,K3_plus,Ward/contact,mediator-null controls}`.

## Frozen phase coordinate

For two branch-superposed masses,

`phi_ab=G m_A m_B tau/(hbar d_ab)`

and

`Theta=phi_LL+phi_RR-phi_LR-phi_RL`.

The ideal pure branch-phase two-qubit calibration gives

`C_AB=|sin(Theta/2)|`.

Local single-probe phases are quotient directions.

## Frozen commutator-sensitive coordinate

For a Hermitian gravity-sensitive generalized force/operator `F`,

`S_FF(omega)=integral dt exp(i omega t)<F(t)F(0)>`.

Define

`rho_comm(omega)=S_FF(+omega)-S_FF(-omega)`.

A weak narrow-band two-level detector samples opposite-frequency spectra through excitation/relaxation rates, allowing

`A_comm(Omega)=[Gamma_down-Gamma_up]/[Gamma_down+Gamma_up]`

after calibrated dark/readout/backaction subtraction.

For a stationary real classical stochastic mediator autospectrum,

`S_cl(+Omega)=S_cl(-Omega)`

so the intrinsic mediator contribution has `A_comm=0`.

A raw optical sideband asymmetry is explicitly **not** accepted as this estimator because classical backaction/interference can mimic it.

## Comparator result

The detailed ledger is in `models/nonclassical_interface/comparator_ledger.md`.

### C2

Can mimic mean phase, retarded response and stochastic noise. The frozen real classical metric mediator does not provide a fundamental metric commutator or a gravity-only non-EB quantum channel.

### C3

Measurement-feedback can mimic Newtonian interaction but brings compulsory noise/decoherence. The mediator leg is classical/measure-and-feed-forward and does not provide a non-EB quantum channel in the standard realization.

### C3b

The 2026 covariant CQ path-integral framework is CP/covariant and allows classical stochastic gravity, but the source proves that entanglement cannot be generated via the local classical field. It likewise has no fundamental noncommuting metric operator.

Thus the joint gravity-only target

`{Q_channel non-EB, A_comm!=0}`

with calibrated `Theta,chi_R,N` is incompatible with the frozen pure C2/C3/C3b classical gravitational mediators.

## Why this is not yet a globally unique QG residual

C4/C6 remain essential attribution adversaries:

- ordinary quantized matter or electromagnetic/optical/phononic/common-bath channels can generate non-EB transmission and nonzero commutator spectra;
- quantum source preparation can imprint nonclassical statistics on detectors while the gravitational interface itself remains classical.

Therefore the architecture requires **mediator attribution**. This is a permanent design constraint, not an unresolved defect of the T3-03 architecture question.

No Candidate Gravity dynamics has yet been proposed or promoted on this basis.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| setup/dynamics for benchmark | PASS | explicit source geometry and readout definitions |
| comparator span | PASS_SCOPED | C2/C3/C3b plus C4/C6 attribution ledger frozen |
| channel discriminator | PASS_RQIR_GATE | non-EB gravity-only channel excludes frozen classical mediator classes |
| commutator discriminator | PASS_RQIR_GATE_SCOPED | unsymmetrized autospectrum estimator distinguishes stationary real classical mediator from noncommuting operator bath after calibration |
| joint hard discriminator architecture | **PASS_RQIR_GATE** | combined vector survives pure C2/C3/C3b quotient by construction |
| global QG uniqueness | NOT_CLAIMED | C4/C6 attribution and an actual KG parent dynamics remain future requirements |
| identifiability/resources | DEFERRED_TO_MODEL | cannot be computed before a concrete KG prediction exists |

## Terminal status

`PASS_RQIR_GATE`

objective:

`CLASSICAL_SPACETIME_DISCRIMINATOR_ARCHITECTURE_ESTABLISHED`.

This means KMQGB has established a **design architecture** for attacking classical-spacetime alternatives. It does not mean gravity has been shown to be quantum or that Candidate Gravity readiness increases.

## Candidate Gravity design lesson

The most promising current KG target is now narrower and stronger:

`{gravity-attributed non-EB channel + commutator-sensitive response + calibrated response/noise + exact Ward/contact linkage}`

with higher cumulants and branch phase as rigidity/supporting channels.

A future KG theory should derive a relation

`F(Theta,Q_channel,A_comm,chi_R,N,K3_plus,Ward/contact)=0`

from one parent dynamics, leaving little comparator/nuisance freedom.

## Reopen/extension condition

Future waves should attack this architecture with:

- non-Gaussian stochastic gravity;
- nonlocal classical-CQ kernels;
- C4/C6 quantum-matter mediator constructions;
- detector/backaction models capable of mimicking `A_comm`;
- relational/causal-process alternatives.

Those are adversarial extensions, not reasons to leave T3-03 nonterminal.

## Terminal completion

**100% — terminal methodological PASS.**

## Sources

1. Kafri, Taylor & Milburn, classical communication/noise bounds for Newtonian gravity.
2. Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), covariant CQ path integral and no-entanglement theorem through the local classical field.
3. Mari, Zippilli & Vitali, Phys. Rev. D 113, L021905 (2026), gravity-induced quantum channel / entanglement-breaking criterion.
4. Clerk et al., Rev. Mod. Phys. 82, 1155 (2010), unsymmetrized quantum noise spectroscopy.
5. Børkje, Phys. Rev. A 94, 043816 (2016), detector dependence of sideband asymmetry.
6. Novotny et al., Phys. Rev. A 106, 043511 (2022), classical sideband-asymmetry mimic via detector/backaction correlations.
