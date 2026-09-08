# T5-05 Audit — relational ordered cross-spectral geometry

Benchmark ID: `KMQGB-T5-M05-RELATIONAL-CROSS-SPECTRUM`  
Concrete methodological object: `REL-WORLDLINE-ORDERED-SPECTRUM-001`  
Role: combine T4 spatial correlation geometry, T4 QRF quotient, T5 locality and T3 commutator spectroscopy into one physical source-detector object  
State: **TERMINAL — `PASS_RQIR_GATE`**  
Objective: **`RELATIONAL_CAUSAL_ORDERED_KERNEL_ESTABLISHED`**

## Terminal question

Can the promising commutator-sensitive / cross-detector observable be defined without relying on coordinate labels and without accidentally treating acausal spacelike commutators as a “quantum signal”?

**Yes.**

Define the correlation/response objects relationally along physical detector worldlines and impose causal support as part of the observable.

## Frozen relational detector variables

Let detector `i` follow physical worldline `z_i(tau_i)` parametrized by its proper time `tau_i` and couple to a gauge/diffeomorphism-completed gravity-sensitive observable `F_i(tau_i)`.

The exact construction of `F_i` is model-dependent—it may be a tidal/geodesic-deviation observable, a dressed local field along the detector worldline, or another relationally defined source-response operator.

Crucially, it is **not** a bare metric component at coordinate `x`.

## Ordered and symmetrized kernels

Define

`N_ij(tau_i,tau_j)=1/2 <{delta F_i(tau_i),delta F_j(tau_j)}>`

and

`C_ij(tau_i,tau_j)=i <[F_i(tau_i),F_j(tau_j)]>`.

For stationary configurations where a relational time-translation variable is available, define frequency-space matrices

`S^+_ij(omega)` from the symmetrized kernel `N_ij`,

`S^-_ij(omega)` from the antisymmetrized/commutator kernel `C_ij`.

The exact Fourier clock must be declared operationally—e.g. one detector proper time plus a synchronized relational timing protocol—not a preferred background coordinate by fiat.

## Classical stochastic comparator

For commuting classical stochastic variables,

`F_i F_j = F_j F_i`

pointwise, so the fundamental stochastic commutator kernel is

`C_ij^cl = 0`.

The classical model can nevertheless have

- nonzero `N_ij` cross-covariance;
- retarded classical response;
- baseline/orientation dependence;
- non-Gaussian higher cumulants.

Thus the distinction is **not** “correlation versus no correlation.” It is the relation between a rich symmetrized spatial covariance hierarchy and an independent ordered/operator sector.

## Microcausality guardrail

For a local relativistic quantum mediator, relational observables associated with spacelike-separated local measurement regions must satisfy the appropriate microcausal commutator condition.

Therefore KMQGB explicitly rejects the false criterion

`nonzero cross commutator at spacelike separation => quantum gravity`.

Such a result would instead signal one of:

- a nonlocal/dressed observable whose support must be understood;
- detector overlap/shared ordinary quantum channel;
- gauge-dressing subtlety;
- or an actual locality/microcausality problem.

The desired quantum ordered kernel has **causal support consistent with the parent dynamics**.

## Frozen causal ordered vector

Use

`I_relord={N_ij,S^+_ij,C_ij,S^-_ij,retarded support,proper-time geometry,baseline/orientation,tensor polarization,source scaling,QRF invariance,Ward/contact}`.

The strongest KG target is not one component but a forced relation among

1. symmetrized spatial covariance;
2. commutator/ordered spectral density;
3. retarded response;
4. causal support;
5. tensor/spin-2 response geometry;
6. relational/QRF-invariant timing and separation.

## Operational pathway

Existing quantum-noise spectroscopy provides local transition-rate access to opposite-frequency spectra.

Recent single-shot qubit cross-spectroscopy demonstrates that cross-power spectra between two quantum probes can be reconstructed robustly from correlated readouts over wide frequency ranges.

These techniques do not by themselves measure a gravitational commutator; they show that the **multi-probe spectral-estimation layer is operationally meaningful**.

A future KG experiment would still require gravity-specific weak coupling, detector/backaction calibration and C4/C6 nulls.

## Relation to QRF redundancy

T4-04 established that branch coordinate locations are not physical novelty directions.

T5-05 therefore defines all spacetime correlation claims through

- physical worldlines;
- proper/relational timing;
- detector observables;
- source-detector coincidences/separations.

A QRF/diffeomorphism transformation may change the coordinate description, but the relational kernel is the object to be compared.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 relational observable | PASS_METHOD | detector-worldline/proper-time object defined |
| F1 symmetrized cross geometry | PASS | `N_ij/S^+_ij` explicit |
| F2 ordered quantum sector | PASS_METHOD | `C_ij/S^-_ij` explicit |
| F3 locality | PASS_REQUIREMENT | microcausal/retarded support is part of the frozen object |
| F4 QRF/coordinate quotient | PASS | bare coordinate labels excluded |
| F5 combined discriminator architecture | **PASS_RQIR_GATE** | one relational causal ordered kernel unifies prior independent guards |
| F6/F7 | DEFERRED | concrete KG prediction/resources absent |

## Terminal status

`PASS_RQIR_GATE`

objective:

`RELATIONAL_CAUSAL_ORDERED_KERNEL_ESTABLISHED`.

## Candidate Gravity design lesson

The current KG design can now be expressed more compactly.

Instead of separately postulating “noise”, “commutator”, “causal order” and “cross-correlation”, derive one relational two-point influence/response structure

`{N_ij, C_ij, chi_R, causal support}`

from the same parent dynamics, then link it to

`{Q_channel,Theta_static,spin2/tensor response,soft/Ward/contact,universality}`.

This is substantially more rigid than treating each observable as an independent parameter.

Permanent rule:

> **Ordered quantum structure must be causal and relational.**

## Reopen/extension condition

When a concrete Candidate Gravity parent object exists, instantiate `F_i` and calculate the full relational kernel, including gauge dressing/contact terms and its C2/C3/C3b/C4/C6 quotient.

## Terminal completion

**100% — relational causal ordered kernel established as a design object.**

## Sources

1. KMQGB T4-03 multi-detector spacetime-correlation audit.
2. KMQGB T4-04 quantum-reference-frame relational quotient.
3. KMQGB T5-03 unsymmetrized quantum-noise detector quotient.
4. Standard local QFT microcausality / retarded spectral-function structure.
5. PRX Quantum 7, 020351 (2026), single-shot cross-spectroscopy of correlated qubit noise, as operational cross-spectrum support.
