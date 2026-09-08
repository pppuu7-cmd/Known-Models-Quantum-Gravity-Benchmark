# T3-03 Comparator Ledger — nonclassical gravitational interface

Benchmark target: `KMQGB-T3-M03-NONCLASSICAL-INTERFACE`  
Primary setup: `NC-TWOMASS-BRANCH-MEDIATOR-001`  
Supplementary channel readout: `NC-OPTOMECH-GRAVITY-CHANNEL-001`

## Purpose

Put the strongest comparator families into the same observable language before any Candidate Gravity ansatz is proposed.

Frozen vector:

`I_NC = {Theta, E_AB, Q_channel, chi_R^grav, rho_comm^grav, N_grav, K3_plus, Ward/contact, mediator-null controls}`.

The entries below are **scoped predictions** for explicit comparator realizations, not statements about every conceivable classical/quantum hybrid theory.

## C2 — linear Gaussian stochastic gravity / Einstein–Langevin control

Frozen scope: linearized metric response driven by a Gaussian classical stochastic source with covariance fixed by the stress-tensor noise kernel.

- `Theta`: can reproduce a classical/mean gravitational branch-dependent phase if the source geometry is supplied consistently.
- `chi_R^grav`: nonzero; retarded/dissipative response is present.
- `N_grav`: nonzero; this is one of the defining objects of stochastic gravity.
- `rho_comm^grav`: **no fundamental metric-operator commutator** because the metric perturbation is a classical stochastic field. A detector may still have quantum operator statistics, so the operational estimator must subtract detector-side commutators rather than assume zero total commutator signal.
- `K3_plus`: for the frozen **linear Gaussian** realization, connected metric/force cumulants above second order vanish. This zero is not transferable to nonlinear/non-Gaussian stochastic-gravity extensions.
- `E_AB`: if probes couple only locally to a shared externally classical stochastic metric, the conditioned map has the form `U_A[xi] tensor U_B[xi]`; averaging over classical `xi` gives a separable random-local-unitary channel and cannot create entanglement from a separable input. Any quantum common bath/source contribution belongs in C4/C6 rather than pure C2.
- `Q_channel`: gravity-only transfer is classical in this frozen scope; a genuinely non-entanglement-breaking A->B quantum communication channel is not supplied by the classical stochastic metric alone.

C2 therefore remains a strong mimic of `{Theta,chi_R,N}` but not of a gravity-attributed non-EB channel plus an independent metric commutator structure.

## C3 — KTM / measurement-feedback classical-channel gravity

Frozen scope: continuous local measurement of the two systems followed by reciprocal classical feedback, tuned to reproduce the Newtonian bilinear interaction in the standard Gaussian realization.

- `Theta`: mean interaction can be calibrated to reproduce the Newtonian branch-phase structure.
- `chi_R^grav`: nonzero effective response via measurement/feedback.
- `N_grav`: compulsory measurement/backaction/feedback decoherence-noise is tied to the interaction strength; it is not an optional nuisance that may simply be set to zero.
- `rho_comm^grav`: absent as a fundamental gravitational mediator operator algebra; the channel is implemented by measurement records and classical feedback.
- `K3_plus`: zero for the standard Gaussian monitoring/feedback realization after connected subtraction; nonlinear/non-Gaussian measurement schemes are a separate comparator extension.
- `E_AB`: the standard local classical-channel construction is non-entangling in its declared sector.
- `Q_channel`: a measure-and-feed-forward mediator is an entanglement-breaking/classical communication channel in the mediator leg. If a laboratory realization shows non-EB transfer, hidden optical/mechanical quantum links must be assigned to C4 rather than to C3.

The key C3 discriminator is therefore not interaction or decoherence separately but the **interaction/noise bound together with EB channel structure**.

## C3b — covariant postquantum classical gravity

Frozen scope: Oppenheim–Weller-Davies covariant classical-quantum path-integral class, with the classical spacetime field retained as classical and the 2026 CP/covariance result.

- `Theta`: classical gravitational interaction/backreaction can generate branch-dependent phases/correlations depending on the concrete matter coupling.
- `chi_R^grav`: classical dynamical gravitational response is allowed.
- `N_grav`: stochasticity/decoherence is required in the broader postquantum classical program.
- `rho_comm^grav`: no fundamental noncommuting metric operator is present because spacetime is classical.
- `K3_plus`: **not fixed to zero in the parent C3b class**; nonlinear/non-Gaussian stochastic path weights may generate higher classical cumulants.
- `E_AB`: the 2026 covariant path-integral construction explicitly proves that entanglement cannot be generated via the classical field.
- `Q_channel`: consequently a gravity-only channel that is demonstrably non-entanglement-breaking would falsify this scoped classical-field mediation mechanism, provided C4/C6 hidden quantum transfer channels are excluded.

This makes C3b substantially stronger than a Gaussian-noise strawman: `K3_plus != 0` would not by itself defeat C3b.

## C4 — ordinary quantum matter / non-gravitational quantum mediator nuisance

C4 is the principal **mediator-attribution adversary**.

A quantum electromagnetic, optical, phononic, material, shared-bath, or quantized-matter interaction can in principle provide:

- `E_AB > 0`;
- a non-EB quantum channel;
- nonzero operator commutators/ordered response;
- non-Gaussian higher cumulants.

Therefore none of these quantities is gravity-specific until the C4 ledger is experimentally/theoretically bounded in the same geometry.

Required nulls include shielding/scaling checks, independent electromagnetic/Casimir/patch-potential characterization, optical/control cross-talk tests, common-bath exclusion, and a source-mass/distance dependence inconsistent with the bounded C4 channels.

## C6 — quantum source statistics + classical gravitational interface

C6 is dangerous because quantum source preparation can imprint nonclassical statistics on a detector even when the gravitational interface itself is classical.

- branch coherence may affect conditional classical source records;
- detector statistics may inherit quantum-source correlations;
- apparent higher-order or ordered-looking detector correlations can therefore arise without a quantum metric mediator.

C6 must be attacked with source-state randomization/coherence nulls and with observables whose nonclassical component is causally attributed to the inter-probe gravitational channel rather than to local source preparation/readout.

## First frozen comparator quotient

The first useful reduced statement is now:

`{Theta,chi_R,N}` alone is **not** KG-specific because C2/C3/C3b can reproduce substantial parts of it.

`K3_plus != 0` alone is also **not** KG-specific because a nonlinear/non-Gaussian C3b or stochastic extension can reproduce classical higher cumulants.

`E_AB > 0` or `Q_channel non-EB` is stronger against pure C2/C3/C3b, but is **not gravity-attributed** until C4/C6 are excluded.

The highest-value surviving joint direction is therefore provisionally

`I_survive = {Q_channel non-EB, rho_comm-sensitive gravitational response, response/noise relation, mediator attribution, Ward/contact consistency}`

with `Theta` fixing gravitational geometry/calibration and `K3_plus` retained as a supporting rigidity channel rather than the primary discriminator.

## Candidate Gravity design consequence

A future KG parent dynamics should ideally force a relation of the schematic form

`F(Q_channel, rho_comm, chi_R, N, Theta, K3_plus, Ward/contact)=0`

with few or no freely tunable functions after consistency conditions.

The design target is **not** merely to predict all of these objects, but to predict a comparator-resistant relation among them.

## Open technical task

The next critical object is an operational estimator for `rho_comm^grav` that can be expressed using controlled source modulation / time ordering and detector observables without assuming a quantum mediator in its derivation.

After that estimator is frozen, the C2/C3/C3b entries above can be made algebraic rather than qualitative.

## Sources

1. Hu & Verdaguer, stochastic gravity / Einstein–Langevin framework.
2. Kafri, Taylor & Milburn classical-channel gravity and measurement-feedback literature.
3. Di Bartolomeo, Carlesso & Bassi, Phys. Rev. D 104, 104027 (2021), dissipative classical-channel generalization.
4. Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), covariant CP classical-quantum path integrals and proof that the classical field cannot generate entanglement.
5. Mari, Zippilli & Vitali, Phys. Rev. D 113, L021905 (2026), gravity-induced quantum-channel / entanglement-breaking criterion.
6. Toccacelo, Andersen & Brask, Phys. Rev. A 112, 022218 (2025), quantum communication benchmarks via gravity.
7. Yang et al., Phys. Rev. D 111, 104084 (2025), causal conditional classical-gravity feedback models and the need for stronger LOCC/null protocols.
