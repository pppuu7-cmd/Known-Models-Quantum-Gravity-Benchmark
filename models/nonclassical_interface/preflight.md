# T3-03 Preflight — Nonclassical interface / mediator-attribution discriminator

Benchmark target: KMQGB-T3-M03-NONCLASSICAL-INTERFACE
Concrete setup ID: `NC-TWOMASS-BRANCH-MEDIATOR-001`
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

`I_NC = {Theta, E_AB, chi_R^grav, rho_comm^grav, N_grav, K3_plus, Ward/contact, mediator-null controls}`

with

- `Theta`: branch double-difference interaction phase;
- `E_AB`: entanglement/non-LOCC witness (concurrence/negativity as appropriate to the concrete detector model);
- `chi_R^grav`: calibrated retarded gravitational response obtained from a controlled source modulation;
- `rho_comm^grav`: commutator/ordered spectral component, schematically `i<h(x),h(y)>_comm`, or an operational detector statistic proven equivalent to it in the chosen model;
- `N_grav`: symmetrized metric/force noise covariance;
- `K3_plus`: at least one connected third-or-higher gravitational phase/force cumulant;
- `Ward/contact`: gauge/Ward/Bianchi/contact identities linking source, response and detector terms;
- `mediator-null controls`: explicit null channels and comparator fits excluding ordinary quantized matter, electromagnetic/Casimir transfer, source-state leakage and classical-feedback explanations.

The exact operator definition of `rho_comm^grav` remains to be chosen with the detector model; it is deliberately not replaced by `chi_R` alone because a classical dynamical field can possess a retarded response without possessing a noncommuting operator algebra.

## Comparator requirements

The same frozen source geometry must be evaluated under:

- **C2 stochastic gravity:** can reproduce classical stochastic mean/noise and retarded response; field operator commutator is absent as a fundamental metric algebra, but effective detector quantum statistics must still be profiled honestly.
- **C3 measurement-feedback gravity:** interaction plus compulsory decoherence/noise; standard local classical channel is non-entangling in its declared Gaussian realization.
- **C3b postquantum classical gravity:** stochastic spacetime modes and decoherence; no automatic assumption of zero higher statistics.
- **C4 ordinary quantum matter/non-gravitational mediator:** must be included because quantized matter can in principle transport quantum information even if gravity is classical.
- **C6 quantum source statistics + classical detector/interface:** branch quantum statistics can leak into detector correlations without a quantum gravitational mediator.

A KG-specific direction is admitted only if **one admissible comparator parent dynamics cannot reproduce the full vector simultaneously** after the same nuisance/source calibration.

## Operational null-control protocol — frozen structure

The theoretical benchmark requires the following controls before any mediator attribution claim:

1. **Branch-coherence null:** replace each coherent spatial superposition by the corresponding incoherent mixture while preserving branch populations and classical mass distribution as closely as the model permits. This tests whether the candidate statistic depends on source coherence rather than only classical branch occupancy.
2. **Local-phase quotient:** remove all phases expressible as independent functions of A-only or B-only branch labels; only double-difference/nonlocal combinations such as `Theta` survive.
3. **Non-gravitational mediator ledger:** every electromagnetic, Casimir/patch-potential, phononic, optical-control or shared-environment quantum channel must enter C4 rather than being assumed absent by wording.
4. **Mass/distance scaling control:** require the gravitational candidate channel to follow the frozen source-response scaling within its validity regime while nuisance channels are independently profiled.
5. **Ordered/noise cross-check:** fit symmetrized noise and retarded response first; then ask whether the ordered/commutator-sensitive statistic contains an independent component not reconstructible by the same positive classical stochastic kernel.
6. **Higher-statistics cross-check:** compare at least one connected `K3_plus` observable so agreement at the two-point level cannot close the audit.

These are benchmark requirements, not a claim that all six controls are experimentally easy with present hardware.

## Literature-driven strengthening

The 2025 paper *Beyond entanglement: Diagnosing quantum mediator dynamics in gravitationally mediated experiments* explicitly studies a three-oscillator mediator model and shows that different mediator regimes produce qualitatively different terminal entanglement dynamics. This supports using **time-dependent mediator fingerprints**, not a single final entanglement number.

The 2026 literature also sharpens the attribution issue: locality-based witness analyses defend the nonclassicality inference under their assumptions, while other analyses emphasize that apparent entanglement must not be assigned to gravity if a quantized matter interaction actually carries the transfer. The benchmark therefore keeps locality and mediator attribution as explicit assumptions/tests rather than slogans.

## Current F0-F7 style status

| Gate | State | Reason |
|---|---|---|
| setup freeze | PASS | explicit two-probe branch geometry and phase invariant frozen |
| comparator span | PASS_PARTIAL | C2/C3/C3b/C4/C6 required explicitly |
| mediator attribution | ACTIVE | null-control structure frozen; exact detector/operator implementation of `rho_comm^grav` remains open |
| ordered/noncommuting discriminator | ACTIVE | theoretical target defined; operational estimator still to freeze |
| higher statistics | ACTIVE | `K3_plus` mandatory but concrete estimator/model predictions not yet derived |
| identifiability | BLOCKED | cannot precede comparator predictions for full `I_NC` |
| resources | BLOCKED | no apparatus claim before identifiability |

## Candidate Gravity design consequence

A future KG model should make the components of `I_NC` **not independently tunable**. The model must derive their relations from one parent dynamics. This is the nonclassical-interface form of the `rigidity by overconstraint` principle found in T3-01.

## Exact next tasks

1. Choose an explicit detector coupling/observable for the commutator-sensitive `rho_comm^grav` component.
2. Derive the full `I_NC` predictions for C2 and C3 first, then C3b/C4/C6.
3. Determine whether time-order reversal/source-modulation protocols provide an operational estimator of the ordered component without importing a quantum-mediator assumption.
4. Freeze one higher-cumulant observable compatible with the same branch geometry.
5. Only after comparator profiling, promote any surviving direction into `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md` as more than a hypothesis.

## Operational preflight completion

**45%**.

## References

1. Marletto & Vedral, Phys. Rev. Lett. 119, 240402 (2017), two-mass entanglement witness.
2. Marletto & Vedral, Rev. Mod. Phys. 97, 015006 (2025), quantum-information methods for laboratory gravity tests.
3. Martín-Martínez & Perche, Phys. Rev. D 108, L101702 (2023), locality and what GME can establish.
4. Christopher & Shankaranarayanan, Phys. Rev. D 112, L081502 (2025), mediator dynamics beyond a single entanglement witness.
5. Marletto, Oppenheim, Vedral & Wilson, arXiv:2511.07348 (2025), mediator-attribution critique.
6. Feng, Vedral & Marletto, Phys. Rev. D 113, 104055 (2026), locality-based witness analysis for collapse/classical models.
7. Schneider, Huggett & Linnemann, Classical and Quantum Gravity (accepted/published 2026), Newton-Cartan mediator analysis.
