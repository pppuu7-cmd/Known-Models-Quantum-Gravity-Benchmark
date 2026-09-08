# T4-05 Audit — quantum-matter / non-gravitational mediator attribution adversary

Benchmark ID: `KMQGB-T4-M05-C4C6-ATTRIBUTION`  
Concrete C4 adversary ID: `C4-MASSLESS-SCALAR-MASSCHARGE-001`  
Role: attack the T3-03 claim that Newtonian branch phase + non-EB channel + commutator-sensitive response identifies a quantum gravitational mediator  
State: **TERMINAL — `OPERATIONALLY_DEGENERATE`**

## Terminal question

Suppose an experiment observes, in the same two-mass geometry,

1. the Newtonian-looking branch phase `Theta`;
2. a non-entanglement-breaking quantum channel / entanglement capability;
3. nonzero unsymmetrized spectral asymmetry `A_comm`, indicating a noncommuting mediator degree of freedom.

Does that joint result by itself identify **gravity** as the quantum mediator?

**No.**

An ordinary quantized non-gravitational field can reproduce all three ingredients in the nonrelativistic two-probe sector.

## Explicit C4 counterexample — quantized massless scalar

Take an ordinary quantized massless scalar field `phi` and two nonrelativistic probes with couplings

`L_int = - g_A phi(x_A) - g_B phi(x_B)`.

In natural units, single massless-scalar exchange gives the static potential

`V_phi(r) = - g_A g_B/(4 pi r)`

for the attractive-sign convention.

Choose the scalar charges proportional to inertial masses,

`g_i = sqrt(4 pi G) m_i`.

Then

`V_phi(r) = - G m_A m_B/r`,

which exactly matches the Newtonian branch-energy dependence used in T3-03.

Hence for every branch pair,

`phi_ab^scalar = G m_A m_B tau/(hbar d_ab) = phi_ab^Newton`,

and therefore

`Theta_scalar = Theta_Newton`

for the frozen branch-phase observable.

The phase/distance/mass scaling alone therefore does **not** identify the mediator as spin-2 gravity.

## Quantum-information and commutator sector

Unlike C2/C3/C3b classical-spacetime mediators, `phi` is a genuinely quantized field:

- it has a nonzero field commutator;
- its unsymmetrized spectrum can be asymmetric, giving nonzero calibrated `A_comm`;
- appropriate detector/probe couplings can transmit quantum information and create entanglement / non-EB channels in principle.

Thus the reduced T3-03 core

`I_core={Theta,Q_channel non-EB,A_comm!=0}`

is **operationally degenerate** between

- a genuinely quantum gravitational mediator, and
- an ordinary quantum massless-scalar mediator whose charge is tuned to mass in the declared nonrelativistic sector.

This is an exact analytic counterexample at the level of the frozen reduced observable.

## Why this does not make the scalar field “gravity”

The scalar comparator does not generically reproduce the full structure of a massless spin-2 gravitational interaction.

Potential discriminator directions include

1. **tensor/spin content:** scalar versus helicity-2 response/polarization;
2. **universal stress-energy coupling:** gravity couples to the conserved stress tensor, not an arbitrary scalar charge;
3. **equivalence/universality:** inertial/passive/active mass relations and composition independence must arise from the parent dynamics rather than from hand-tuned `g_i proportional m_i`;
4. **gravitational Ward identities:** linearized diffeomorphism/gauge identities constrain source and propagator tensor structure;
5. **contact/seagull structure:** gauge completion links exchange and contact terms;
6. **relativistic source response:** pressure, momentum flow, light deflection/polarization, and relativistic probes distinguish scalar charge exchange from tensor gravity;
7. **multi-source consistency:** one set of couplings must work for all source compositions/kinematics, not only the two nonrelativistic masses used to tune the comparator.

Therefore the surviving Candidate Gravity target must include **mediator-spin/gauge attribution**, not merely quantum-channel attribution.

## Relation to the 2025–2026 GIE controversy

Aziz & Howl (Nature 2025) argue that when matter is treated in QFT, a classical-gravity framework can exhibit quantum communication/entanglement through virtual quantum-matter propagation. Marletto–Oppenheim–Vedral–Wilson dispute the claimed entanglement calculation and emphasize that any such entangling transfer would be carried by quantized matter rather than classical gravity. Di Biagio (PRD accepted 1 Sep 2026) argues more broadly that gravity-induced entanglement is not theory-independent across all classical-gravity/quantum-matter frameworks, while Feng–Vedral–Marletto show that specific collapse-based models do not violate the locality-based witness.

KMQGB does not need to adjudicate the full controversy to close T4-05. The explicit massless-scalar C4 counterexample already proves the narrower methodological point:

> a quantum-looking channel with Newtonian `1/r` phase is not automatically attributable to the gravitational field.

The dispute is retained as additional evidence that **mediator attribution is a physical modeling question, not a slogan**.

## C6 adversary

C6 adds a distinct loophole: quantum source-state statistics can enter detector correlations while the inter-probe gravitational interface remains classical.

Required nulls include

- coherent-source versus incoherent-mixture comparison;
- local source-readout randomization;
- causal/inter-probe channel isolation;
- verification that the nonclassical statistic disappears when the inter-probe gravitational coupling is disabled while local quantum-source operations remain unchanged.

C6 is not needed to prove the T4-05 degeneracy—the C4 scalar already does—but it remains part of the full attribution stack.

## Frozen attribution stack after T4-05

A future KG claim should satisfy all four layers:

1. **quantum attribution:** ordered/commutator-sensitive and non-EB behavior, not only symmetrized noise;
2. **mediator attribution:** exclude ordinary quantum C4/C6 channels;
3. **gravity attribution:** establish spin-2/tensor Ward/contact/universal stress-energy structure rather than a tuned scalar/vector quantum force;
4. **relational attribution:** formulate the result in QRF/diffeomorphism-invariant source-detector observables.

For causal/process claims add a fifth layer:

5. **geometry attribution:** distinguish gravitational geometry from ordinary quantum control/switch implementations.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 comparator dynamics | PASS | ordinary quantized massless scalar field is explicit |
| F1 low-energy phase match | PASS_EXACT_SCOPED | `g_i=sqrt(4 pi G)m_i` gives exact Newtonian `1/r` branch phase |
| F2 quantum-channel structure | PASS_SCOPED | quantized scalar has noncommuting field algebra and can mediate quantum information |
| F3 T3-03 reduced vector | PASS | `{Theta,Q_channel,A_comm}` can be mimicked in declared sector |
| F4 gravity attribution | **OPERATIONALLY_DEGENERATE** | reduced vector does not distinguish spin-2 gravity from ordinary quantum scalar mediator |
| F5 stronger tensor/Ward discriminator | OPEN_FOR_FUTURE_KG | requires parent-dynamics-specific tensor/gauge/contact relation |
| F6/F7 | DEFERRED | no concrete KG prediction/resources yet |

## Terminal status

`OPERATIONALLY_DEGENERATE`

for the claim

`NEWTONIAN_PHASE_PLUS_NON_EB_PLUS_COMMUTATOR_AS_GRAVITY_ATTRIBUTION`.

## Candidate Gravity design lesson

This is a major strengthening of the KG design prior:

> **Quantumness attribution is not gravity attribution.**

A future KG model should not merely predict a quantum channel and a gravitational-looking `1/r` phase. It should force the **spin-2/tensor, universal stress-energy, Ward/contact and relational structure** that makes the mediator specifically gravitational.

The preferred core bundle is therefore upgraded to

`I_KG*={Theta_rel,Q_channel,A_comm,S^-_ij,chi_R,N,spin2/tensor response,Ward/contact,universality/equivalence,mediator nulls,QRF invariance}`.

Higher cumulants and symmetrized spatial correlations remain supporting rigidity/identifiability coordinates.

## Reopen/extension condition

A future wave should profile stronger ordinary quantum mediators—massless scalar/vector fields, quantized matter exchange and composite/common-bath channels—against the **full tensor/Ward/contact** KG vector rather than the reduced nonrelativistic phase/channel vector.

## Terminal completion

**100% — operational degeneracy established for the reduced gravity-attribution claim.**

## Sources

1. J. Aziz & R. Howl, Nature 646, 813–817 (2025), classical-gravity/QFT-matter entanglement claim.
2. C. Marletto, J. Oppenheim, V. Vedral, E. Wilson, arXiv:2511.07348 (2025), critique and quantum-matter mediator attribution.
3. A. Di Biagio, Phys. Rev. D, accepted 1 Sep 2026, gravity-induced entanglement not theory-independent across all frameworks.
4. T. Feng, V. Vedral, C. Marletto, Phys. Rev. D 113, 104055 (2026), collapse-model witness analysis.
5. Standard QFT massless-scalar exchange potential and quantum-noise/operator algebra.
