# Model Audit — generalized bespoke dual-resonance UV amplitudes

Benchmark ID: KMQGB-T3-M01-BESPOKE-UV
Concrete research target: BESPOKE-DUAL-RESONANCE-UV-001
Role: broad same-domain UV amplitude adversary for string-like pole/residue fingerprints and future KG UV claims
State: ACTIVE / NONTERMINAL

## Frozen literature object

Use the Cheung–Remmen bespoke dual-resonance construction and its subsequent partial-wave unitarity audit as the primary target family.

Published properties relevant to the benchmark:

- explicit closed-form dual-resonant four-point amplitudes;
- an input construction allowing customizable mass spectra;
- simple-pole analyticity with polynomial residues in momentum transfer;
- UV behavior inherited through a transform of Veneziano/Koba–Nielsen structures;
- open parameter regions that deviate from ordinary string theory while satisfying partial-wave unitarity in the original construction;
- later unitarity analysis that rules out all studied asymptotically nonlinear Regge trajectories and restricts viable asymptotically linear subclasses;
- many unitary bespoke amplitudes fail Regge sum rules, while a smaller subclass with vanishing mass gap can satisfy stronger high-energy boundedness properties.

This is not yet frozen to one numerical bespoke parameter point because the purpose of T3-M01 is first to establish the correct **parent comparator family** and then choose the strongest admissible non-string point for the joint invariant test.

## Immediate consequence for the previous string pole-support test

Second-wave S2-M05 established only

`P_s^VS != P_s^HR-single-mass`.

That is a valid one-comparator result but not a global string-uniqueness result.

The bespoke construction shows why pole support by itself is too weak as a universal discriminator: the mass spectrum is an input degree of freedom of a much broader dual-resonance construction. Therefore a future comparator can in principle be chosen to reproduce a target pole-support pattern while differing elsewhere in residues, trajectories or sum-rule structure.

Current classification of **pole support alone**:

`INSUFFICIENT_FOR_GLOBAL_UV_IDENTIFICATION`.

This does not yet prove that a fully unitary non-string bespoke amplitude exactly reproduces every type-II Virasoro-Shapiro pole and residue simultaneously. That stronger statement remains open and must not be inferred.

## Stronger frozen target vector

Replace the scalar pole-support observable by the joint invariant vector

`I_UV = {P, R, S, C, Regge, B, EFT}`

with

- `P`: pole locations/support;
- `R`: residues and their spin/partial-wave decomposition;
- `S`: spin content / degeneracy pattern on each pole;
- `C`: crossing / dual-resonance relations among channels;
- `Regge`: asymptotic trajectory class;
- `B`: high-energy boundedness / Regge sum-rule behavior;
- `EFT`: correlated low-energy Wilson-coefficient expansion.

A string-specific or KG-specific UV residual is not accepted unless at least one component of this **joint vector** remains unmatched after profiling over a physically admissible unitary bespoke/UV family.

## F0-F7 current map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics/amplitude | PASS_FAMILY_LEVEL | explicit closed-form amplitude construction exists; exact benchmark point still to freeze |
| F1 IR/GR-like limit | PARTIAL | target applications can be chosen with controlled low-energy limit; exact gravitational external-state normalization must be frozen for the concrete point |
| F2 consistency | PARTIAL_UNITARITY_FILTER | partial-wave unitarity strongly constrains the family; nonlinear Regge trajectories are ruled out in the studied class, viable subclasses remain |
| F3 RQIR hierarchy | AMPLITUDE_SECTOR_ONLY | this is a UV S-matrix comparator, not a full source/noise/interface model |
| F4 distinction | POLE_SUPPORT_INSUFFICIENT | previous one-comparator string pole distinction is not globally robust against a spectrum-tunable parent family |
| F5 joint discriminator | ACTIVE | need exact `I_UV` comparison at a concrete admissible non-string point |
| F6 identifiability | BLOCKED | cannot precede exact F5 vector/profile |
| F7 resources | N/A_FOR_CURRENT_THEORY_LEVEL_AUDIT | no apparatus claim before F5/F6 |

## Candidate Gravity design lesson

The important reusable result is broader than string theory:

> Do not define KG novelty by one spectral/pole property if a physically admissible parent amplitude family can tune that property. Novelty should be expressed as an overconstrained relation among pole locations, residues/spins, crossing, Regge behavior, sum rules and low-energy coefficients — or, preferably for the interface problem, an even richer linked response/noise/noncommutativity hierarchy.

## Current first blocker

`BESPOKE_CONCRETE_UNITARY_POINT_AND_JOINT_VECTOR_FREEZE`:

1. select a concrete non-string bespoke amplitude point/subclass that survives the published unitarity restrictions;
2. determine whether its pole spectrum can be aligned with the type-II target while remaining genuinely non-string;
3. compare residues/spin decomposition, Regge trajectory, sum rules and low-energy expansion simultaneously;
4. record exactly which string-like properties are generic dual-resonance properties and which remain distinctive;
5. feed the resulting lesson into `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md`.

## Operational completion estimate

**45%**.

## Sources

1. C. Cheung and G. N. Remmen, *Bespoke dual resonance*, Phys. Rev. D 108, 086009 (2023): customizable mass spectra, dual resonance, UV behavior, and unitary non-string regions.
2. R. Bhardwaj, M. Spradlin, A. Volovich, H.-C. Weng, *Unitarity of bespoke amplitudes*, Phys. Rev. D 110, 106016 (2024): asymptotically nonlinear Regge trajectories ruled out in the analyzed bespoke class; constraints on asymptotically linear cases; Regge-sum-rule/high-energy restrictions.
3. Related generalized Veneziano/Virasoro and Coon-amplitude literature retained for the next concrete-point selection.
