# T3-03 Preflight — Nonclassical interface / mediator-attribution discriminator

Benchmark target: KMQGB-T3-M03-NONCLASSICAL-INTERFACE
Concrete setup ID: `NC-TWOMASS-BRANCH-MEDIATOR-001`
Supplementary readout ID: `NC-OPTOMECH-GRAVITY-CHANNEL-001`
State: ACTIVE PREFLIGHT / NONTERMINAL
Purpose: design a Candidate-Gravity-facing discriminator that survives C2/C3/C3b and ordinary quantum-matter/interface nuisances.

## Why entanglement alone is not sufficient

The modern gravity-mediated-entanglement literature contains an active model/interpretation dispute. The benchmark therefore does not use final probe entanglement by itself as a universal certificate of a quantum gravitational mediator.

The stronger requirement is **mediator attribution**: any nonclassical transfer must be attributable to the gravitational interface after profiling ordinary quantized-matter/non-gravitational explanations and classical/stochastic gravity comparators.

## Frozen two-probe source/detector geometry

Use two neutral mesoscopic probes `A` and `B`, with masses `m_A,m_B`, each coherently prepared in two localized branches `L,R`.

Let the four branch separations be

`d_ab = |x_A^a-x_B^b|`,  `a,b in {L,R}`,

and let the isolated interaction interval be `tau`.

In the ideal weak-field Newtonian branch-phase benchmark,

`phi_ab = G m_A m_B tau/(hbar d_ab)`.

The local single-probe phases are nuisance directions. The entangling branch invariant is the double difference

`Theta = phi_LL + phi_RR - phi_LR - phi_RL`.

For the ideal initial product state `|+>_A |+>_B` with only branch-dependent phases applied, the two-qubit concurrence is

`C_AB = |sin(Theta/2)|`.

This relation is not declared a universal prediction of all quantum-gravity theories; it is the frozen calibration geometry used to define the source branches and the simplest interaction-phase observable.

## Mediator-attribution vector

The target is not `C_AB>0` alone. Freeze the linked vector

`I_NC = {Theta, E_AB, Q_channel, chi_R^grav, rho_comm^grav, N_grav, K3_plus, Ward/contact, mediator-null controls}`

with

- `Theta`: branch double-difference interaction phase;
- `E_AB`: entanglement/non-LOCC witness;
- `Q_channel`: nonclassical channel-capacity/entanglement-breaking diagnostic for a gravity-induced communication channel;
- `chi_R^grav`: calibrated retarded gravitational response obtained from a controlled source modulation;
- `rho_comm^grav`: commutator/ordered spectral component, or an operational detector statistic proven equivalent to it in the chosen model;
- `N_grav`: symmetrized metric/force noise covariance;
- `K3_plus`: at least one connected third-or-higher gravitational phase/force cumulant;
- `Ward/contact`: gauge/Ward/Bianchi/contact identities linking source, response and detector terms;
- `mediator-null controls`: explicit null channels and comparator fits excluding ordinary quantized matter, electromagnetic/Casimir transfer, source-state leakage and classical-feedback explanations.

The exact operator definition of `rho_comm^grav` remains to be chosen with the detector model; it is deliberately not replaced by `chi_R` alone because a classical dynamical field can possess a retarded response without possessing a noncommuting operator algebra.

## Supplementary operational channel readout

Mari, Zippilli & Vitali, Phys. Rev. D 113, L021905 (2026), provide a directly relevant complementary architecture:

- two optomechanical systems are assumed isolated except for a weak gravitational coupling;
- under a resonance condition, gravity induces a narrow-band optical transmission channel (“gravitationally induced transparency”);
- the scientific test is whether the induced optical channel is **entanglement-breaking**;
- a channel that is demonstrably not entanglement-breaking can preserve/transmit quantum information and therefore supplies a stronger channel-level nonclassicality witness than one final-state entanglement datum;
- in their quadratic-Hamiltonian model the effective link is a Gaussian thermal attenuator with a sharp noise-dependent transition between entanglement-breaking and nonclassical regimes.

KMQGB uses this as a **supplementary readout**, not as a replacement for the two-mass branch geometry. The two architectures test complementary aspects:

1. `NC-TWOMASS-BRANCH-MEDIATOR-001` freezes the gravitational source/branch phase and comparator quotient;
2. `NC-OPTOMECH-GRAVITY-CHANNEL-001` supplies an operational language for channel nonclassicality and quantum-information transmission.

A future KG model is stronger if the same parent dynamics predicts both branch-phase/response observables and channel-capacity/noise properties.

## Comparator requirements

The same frozen source geometry/readout assumptions must be evaluated under:

- **C2 stochastic gravity:** can reproduce classical stochastic mean/noise and retarded response;
- **C3 measurement-feedback gravity:** interaction plus compulsory decoherence/noise; standard local classical channel is non-entangling in its declared Gaussian realization;
- **C3b postquantum classical gravity:** stochastic spacetime modes and decoherence; no automatic assumption of Gaussianity;
- **C4 ordinary quantum matter/non-gravitational mediator:** must be included because quantized matter can in principle transport quantum information even if gravity is classical;
- **C6 quantum source statistics + classical detector/interface:** branch quantum statistics can leak into detector correlations without a quantum gravitational mediator.

For the channel readout, each comparator must also be classified as entanglement-breaking/non-entanglement-breaking under the same environmental-noise and calibration assumptions. A non-EB result is only gravity-attributable if C4/C6 and hidden shared quantum channels are excluded by the mediator ledger.

A KG-specific direction is admitted only if **one admissible comparator parent dynamics cannot reproduce the full vector simultaneously** after the same nuisance/source calibration.

## Operational null-control protocol — frozen structure

1. **Branch-coherence null:** replace coherent spatial superpositions by corresponding incoherent mixtures while preserving branch populations/classical mass distributions as closely as the model permits.
2. **Local-phase quotient:** remove all phases expressible as independent A-only/B-only branch functions; only double-difference/nonlocal combinations such as `Theta` survive.
3. **Non-gravitational mediator ledger:** electromagnetic, Casimir/patch-potential, phononic, optical-control and shared-environment quantum channels enter C4 rather than being assumed absent by wording.
4. **Mass/distance scaling control:** require the candidate gravitational channel to follow the frozen source-response scaling within its validity regime.
5. **Ordered/noise cross-check:** fit symmetrized noise and retarded response first; then ask whether the ordered/commutator-sensitive statistic contains an independent component not reconstructible by the same positive classical stochastic kernel.
6. **Higher-statistics cross-check:** compare at least one connected `K3_plus` observable.
7. **Channel EB threshold:** for the optomechanical readout, freeze the environmental/noise threshold at which the induced channel changes from entanglement-breaking to non-EB and require the same parent dynamics to predict that threshold together with the mechanical/gravitational response.

These are benchmark requirements, not a claim that all controls are experimentally easy with present hardware.

## Literature-driven strengthening

- Christopher & Shankaranarayanan (2025) show that different mediator regimes can produce qualitatively different entanglement dynamics, supporting time-dependent mediator fingerprints rather than one final entanglement number.
- Mari, Zippilli & Vitali (2026) sharpen the language further by treating gravity as an induced communication channel and testing its entanglement-breaking property.
- The 2025–2026 locality/mediator dispute shows that apparent entanglement must not be assigned to gravity if quantized matter or another quantum interaction actually carries the transfer.

## Current status

| Gate | State | Reason |
|---|---|---|
| two-mass setup freeze | PASS | explicit branch geometry and phase invariant frozen |
| channel readout freeze | PASS_SCOPED | explicit optomechanical gravity-induced channel and EB criterion available |
| comparator span | PASS_PARTIAL | C2/C3/C3b/C4/C6 required explicitly |
| mediator attribution | ACTIVE | null/control structure frozen; hidden quantum-channel exclusion remains central |
| ordered/noncommuting discriminator | ACTIVE | theoretical target defined; operational estimator still to freeze |
| higher statistics | ACTIVE | `K3_plus` mandatory but concrete estimator/model predictions not yet derived |
| identifiability | BLOCKED | cannot precede comparator predictions for full `I_NC` |
| resources | BLOCKED | no apparatus claim before identifiability |

## Candidate Gravity design consequence

A future KG model should make `Theta`, `E_AB`, `Q_channel`, response, noise, ordered structure and higher statistics **not independently tunable**. The model must derive their relations from one parent dynamics.

The strongest present KG direction is therefore a **gravity-attributed quantum channel with a rigid multi-observable fingerprint**, not merely an entangled output state.

## Exact next tasks

1. Choose an explicit detector coupling/observable for the commutator-sensitive `rho_comm^grav` component.
2. Derive `I_NC` for C2 and C3 first, then C3b/C4/C6.
3. Translate the Mari–Zippilli–Vitali Gaussian-channel EB condition into the same response/noise notation used for C2/C3 so the quotient is literal rather than verbal.
4. Freeze one higher-cumulant observable compatible with at least one of the two readout architectures.
5. Only after comparator profiling, promote a surviving direction into the Candidate Gravity design priors as more than a hypothesis.

## Operational preflight completion

**60%**.

## References

1. Marletto & Vedral, Phys. Rev. Lett. 119, 240402 (2017).
2. Marletto & Vedral, Rev. Mod. Phys. 97, 015006 (2025).
3. Martín-Martínez & Perche, Phys. Rev. D 108, L101702 (2023).
4. Christopher & Shankaranarayanan, Phys. Rev. D 112, L081502 (2025).
5. Mari, Zippilli & Vitali, Phys. Rev. D 113, L021905 (2026), gravitationally induced transparency and entanglement-breaking channel test.
6. Marletto, Oppenheim, Vedral & Wilson, arXiv:2511.07348 (2025).
7. Feng, Vedral & Marletto, Phys. Rev. D 113, 104055 (2026).
8. Schneider, Huggett & Linnemann, Classical and Quantum Gravity (2026).
