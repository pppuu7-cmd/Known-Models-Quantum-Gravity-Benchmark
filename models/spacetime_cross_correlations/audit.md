# T4-03 Audit — cross-detector spacetime-fluctuation geometry

Benchmark ID: `KMQGB-T4-M03-SPACETIME-CROSSCORR`  
Concrete observable ID: `SF-MULTIDETECTOR-TWOPOINT-GEOMETRY-001`  
Role: adversary for using spatial/baseline-dependent gravitational noise correlations as a Candidate Gravity quantumness witness  
State: **TERMINAL — `OPERATIONALLY_DEGENERATE`**

## Terminal question

Do a characteristic interferometric PSD, baseline dependence, orientation dependence, or multi-detector cross-correlation geometry by themselves establish that spacetime fluctuations are quantum?

**No.**

The 2026 Sharmila–Vermeulen–Datta framework maps broad classes of spacetime two-point correlation functions to interferometer output signals while being explicitly agnostic to whether the microscopic origin is quantum, semiclassical, or stochastic. Its correlation classes contain examples motivated by both quantum and semiclassical/classical-stochastic gravity.

Thus two-point correlation geometry can distinguish **correlation classes and model parameters**, but not the quantum/classical nature of the underlying mediator without additional ordered/noncommuting information.

## Frozen two-point spatial vector

For detector outputs `X_i`, freeze

`I_2space={S_ii(omega),S_ij(omega),baseline dependence,orientation dependence,phase/lag,correlation length,frequency scaling}`.

The Parikh–Setti graviton-noise calculation supplies a concrete quantum example with covariance depending on detector-arm angle and detector separation.

The Sharmila–Vermeulen–Datta framework demonstrates the broader point: comparable interferometric correlation signatures arise from generic correlation kernels whose microscopic origins can be quantum or semiclassical/stochastic.

Therefore

`I_2space`

is not a quantumness certificate by itself.

## Why this is still scientifically useful

The terminal degeneracy is about **quantumness attribution**, not detectability or model discrimination.

Multi-detector geometry can strongly help:

- reject local instrumental noise;
- constrain correlation length and fluctuation strength;
- distinguish factorized, inverse/power-law, and exponential correlation classes;
- exploit arm orientation and detector separation;
- test source/model-specific spatial covariance tensors.

Those are valuable nuisance-rejection and identifiability channels for future KG.

## Stronger frozen target

Upgrade from a symmetrized covariance matrix alone to a **frequency-resolved ordered spatial spectral matrix**:

`S^+_ij(omega)=1/2 [S_ij(omega)+S_ji(-omega)]`

`S^-_ij(omega)=1/2 [S_ij(omega)-S_ji(-omega)]`.

Schematically:

- `S^+`: symmetrized/classical-looking spatial noise geometry;
- `S^-`: antisymmetrized/commutator-sensitive spatial response geometry, after detector/backaction calibration.

The stronger KG vector becomes

`I_spaceQ={S^+,S^-,baseline,orientation,lag,Q_channel,Ward/contact,source scaling}`.

A classical stochastic field may possess a rich `S^+` covariance geometry. The intended quantum-specific pressure comes from requiring the **same parent dynamics** to predict both the spatial covariance and the ordered/commutator sector.

## Relation to GQuEST and nearby-detector proposals

GQuEST and related photon-counting/multi-interferometer concepts provide promising sensitivity to model-predicted spacetime fluctuations. They should be treated as experimental resource/readout architectures, not as proofs that any detected broadband stochastic signal is automatically quantum gravity.

Likewise, a predicted graviton cross-correlation pattern is evidence for that quantum model only after classical stochastic kernels capable of reproducing the same symmetrized covariance are profiled.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 observable geometry | PASS | multi-detector PSD/cross-spectrum geometry explicit |
| F1 experimental mapping | PASS_SCOPED | interferometer response mappings available |
| F2 consistency | N/A | observable/comparator target, not parent theory audit |
| F3 correlation discriminator | PASS | correlation classes/parameters can be distinguished |
| F4 quantum/classical distinction | **OPERATIONALLY_DEGENERATE** | two-point spatial correlations occur in quantum and semiclassical/stochastic models |
| F5 stronger ordered spatial target | DEFERRED | requires `S^-` / commutator-sensitive cross-spectral implementation |
| F6/F7 | MODEL_DEPENDENT | resources exist but no KG-specific residual yet |

## Terminal status

`OPERATIONALLY_DEGENERATE`

for the claim

`SYMMETRIZED_SPATIAL_CORRELATION_GEOMETRY_AS_QG_CERTIFICATE`.

## Candidate Gravity design lesson

Permanent rule:

> **Cross-correlation is not quantumness.** Baseline/orientation geometry is an excellent identifiability and noise-rejection tool, but it must be linked to an ordered/commutator-sensitive spatial spectral sector before being used as a quantum-gravity discriminator.

This directly strengthens T3-03:

`A_comm` should eventually be measured/defined not only locally but as a **cross-detector spectral matrix** whose baseline/orientation dependence is predicted together with `S^+`.

## Reopen/extension condition

A future wave may instantiate a concrete multi-detector `S^-` estimator or a full graviton cross-spectral matrix and compare it with non-Gaussian/nonlocal classical stochastic kernels.

## Terminal completion

**100% — operational degeneracy of the two-point spatial quantumness claim.**

## Sources

1. B. Sharmila, S. M. Vermeulen, A. Datta, Nature Communications 17, 701 (2026), correlation-class-to-interferometer mapping.
2. M. Parikh, F. Setti, Phys. Rev. D 111, 046004 (2025), quantum-gravitational noise correlations in nearby detectors.
3. S. M. Vermeulen et al., Phys. Rev. X 15, 011034 (2025), GQuEST photon-counting interferometer design.
