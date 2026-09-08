# Model Audit — Kafri–Taylor–Milburn classical-channel gravity

Benchmark ID: KMQGB-S2-M03-CLASSICAL-CHANNEL
Concrete realization ID: KTM-OSCILLATOR-MEASUREMENT-FEEDBACK-001
Role: explicit C3 classical-channel / measurement-feedback control
State: TERMINAL
Final status: `EXACT_COMPARATOR_IDENTITY`

## Frozen realization

Use the Kafri–Taylor–Milburn (KTM) model for two gravitationally coupled harmonic oscillators. For small relative displacements around fixed separation `d`, the Newtonian interaction is reduced to a bilinear coupling

`H_qm = H_0 + K x_1 x_2`,

with

`K = 2 G m_1 m_2 / d^3`.

Instead of a direct quantum mediator, each mass position is continuously weakly measured and the classical stochastic measurement record is fed forward to the other mass as a reciprocal force.

For the symmetric minimal-noise choice the unconditional master equation is

`d rho/dt = -(i/hbar)[H_0,rho] -(i/hbar)K[x_1 x_2,rho] -(K/(2 hbar)) sum_k [x_k,[x_k,rho]]`.

The same interaction strength `K` fixes the minimum decoherence/noise strength. The resulting evolution is positivity preserving because it is constructed from continuous measurement plus feedback.

## Exact operational fingerprint

The model reproduces the desired Newtonian bilinear interaction at the master-equation level while necessarily adding decoherence/heating. For Gaussian systems the minimal symmetric KTM channel cannot generate entanglement between the two masses. Reducing the noise below the KTM threshold would allow entanglement and therefore leave the classical-channel construction.

The 2021 dissipative generalization shows that the original secular heating can be modified within a broader classical-channel family so the system thermalizes to a finite effective temperature; therefore secular heating is not used here as the defining universal C3 discriminator. The robust defining feature is classical measurement/feedback mediation plus its interaction-noise constraint and non-entangling character in the declared KTM Gaussian sector.

## Comparator classification

The frozen RQIR comparator registry defines C3 to include classical communication, measurement-feedback, stochastic classical metric and related hybrid constructions that can reproduce interaction plus decoherence/noise without a quantum gravitational mediator.

`KTM-OSCILLATOR-MEASUREMENT-FEEDBACK-001` is literally an explicit member of that comparator class. Therefore its comparator-subtracted residual against C3 is identically zero at theory-class level:

`Delta_C3 = 0`.

This is a successful comparator control, not a consistency failure.

## F0-F7 map

| Gate | Result | Reason |
|---|---|---|
| F0 dynamics | PASS | explicit stochastic measurement-feedback master equation |
| F1 required limit | PASS_SCOPED | reproduces the Newtonian bilinear interaction in the declared oscillator regime |
| F2 consistency | PASS_SCOPED | positivity-preserving measurement/feedback dynamics; classical channel construction explicit |
| F3 RQIR hierarchy | PASS/PARTIAL | interaction and compulsory channel noise are linked by the same open-system construction |
| F4 comparator distinction | EXACT_IDENTITY_C3 | model is an explicit C3 member |
| F5 hard discriminator | ZERO_VS_C3 | no model-specific residual against its own comparator class |
| F6 identifiability | NOT_APPLICABLE_AFTER_IDENTITY | no independent beta direction vs C3 |
| F7 resources | NOT_APPLICABLE_AFTER_IDENTITY | retained as comparator/control |

## RQIR lesson

Observation of gravitationally correlated decoherence, heating, or even nonzero quantum discord is not by itself a certificate of a quantum mediator. Classical measurement-feedback gravity can create interaction plus noise and may create discord while still failing to create entanglement in the declared standard KTM setting.

A stronger quantum-gravity discriminator must therefore survive the C3 quotient; a gravitationally generated entanglement witness is one candidate direction against the standard KTM classical channel, provided ordinary non-gravitational entangling nuisances are also excluded.

## Sources

1. D. Kafri, J. M. Taylor, G. J. Milburn, *A classical channel model for gravitational decoherence*, New J. Phys. 16 (2014) 065020, arXiv:1401.0946.
2. G. Di Bartolomeo, M. Carlesso, A. Bassi, *Gravity as a classical channel and its dissipative generalization*, Phys. Rev. D 104 (2021) 104027, arXiv:2106.13305.
3. F. Roccati et al., *Quantum correlations beyond entanglement in a classical-channel model of gravity*, Sci. Rep. 12 (2022) 17641, arXiv:2205.15333.
4. External RQIR comparator C3 authority retained read-only in `candidate_gravity/BASELINE_COMPARATORS.md`.
