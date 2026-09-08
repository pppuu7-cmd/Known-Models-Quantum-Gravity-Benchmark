# Model Audit — generalized bespoke dual-resonance UV amplitudes

Benchmark ID: KMQGB-T3-M01-BESPOKE-UV
Concrete research target: BESPOKE-DUAL-RESONANCE-UV-001
Role: broad same-domain UV amplitude adversary for string-like pole/residue fingerprints and future KG UV claims
State: ACTIVE / NONTERMINAL

## Frozen literature object

Use the Cheung–Remmen bespoke dual-resonance construction, the Bhardwaj–Spradlin–Volovich–Weng unitarity audit, and the Geiser–Lindwasser generalized Veneziano/Virasoro rigidity analysis as the current authority set.

Published properties relevant to the benchmark:

- explicit closed-form dual-resonant four-point amplitudes;
- an input construction allowing customizable mass spectra;
- simple-pole analyticity with polynomial residues in momentum transfer;
- UV behavior inherited through a transform of Veneziano/Koba–Nielsen structures;
- open parameter regions that deviate from ordinary string theory while satisfying partial-wave unitarity in the original bespoke construction;
- later unitarity analysis that rules out all studied asymptotically nonlinear Regge trajectories and restricts viable asymptotically linear subclasses;
- many unitary bespoke amplitudes fail Regge sum rules, while a smaller subclass with vanishing mass gap can satisfy stronger high-energy boundedness properties;
- under the distinct generalized-Virasoro assumptions studied by Geiser–Lindwasser, the spectral consistency conditions are overdetermined and the only consistent spectrum is the string spectrum.

The last point is not in tension with the bespoke construction: the two analyses impose different structural assumptions. Together they show exactly why a serious uniqueness claim must state the full assumption set.

## Immediate consequence for the previous string pole-support test

Second-wave S2-M05 established only

`P_s^VS != P_s^HR-single-mass`.

That is a valid one-comparator result but not a global string-uniqueness result.

The bespoke construction shows why pole support by itself is too weak as a universal discriminator: the mass spectrum can be treated as an input degree of freedom inside a broader dual-resonance construction. A comparator may therefore reproduce a target pole-support pattern while differing elsewhere in residues, trajectories or sum-rule structure.

Current classification of **pole support alone**:

`INSUFFICIENT_FOR_GLOBAL_UV_IDENTIFICATION`.

This does not prove that a fully unitary non-string bespoke amplitude exactly reproduces every type-II Virasoro-Shapiro pole and residue simultaneously. That stronger statement remains open and must not be inferred.

## New rigidity result

The generalized Veneziano/Virasoro analysis supplies the complementary lesson. Under its physical assumptions, the allowed spectra obey an overdetermined set of nonlinear recursion relations. The generalized Veneziano branch admits nontrivial families including Coon-like deformations, while the generalized Virasoro branch has only the string spectrum as a consistent solution.

Benchmark interpretation:

- a **single feature** such as pole locations can be tunable in a broad parent family;
- a sufficiently rich simultaneous constraint set can instead create **spectral rigidity**;
- therefore the useful uniqueness object is not one observable but the intersection of analyticity, crossing/duality, unitarity, residue/spin structure, Regge behavior, and low-energy matching.

This is a direct design prior for future Candidate Gravity: aim for a model whose observable relations are **overconstrained by independent consistency requirements**, so comparator freedom collapses rather than being fitted away one channel at a time.

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
| F0 dynamics/amplitude | PASS_FAMILY_LEVEL | explicit closed-form amplitude constructions exist; exact non-string benchmark point still to freeze |
| F1 IR/GR-like limit | PARTIAL | controlled low-energy limits exist in relevant constructions; exact gravitational external-state normalization must be frozen for the concrete point |
| F2 consistency | PARTIAL_UNITARITY_FILTER | partial-wave unitarity strongly constrains bespoke families; generalized-Virasoro recursion adds a separate rigidity result |
| F3 RQIR hierarchy | AMPLITUDE_SECTOR_ONLY | this is a UV S-matrix comparator, not a full source/noise/interface model |
| F4 distinction | POLE_SUPPORT_INSUFFICIENT / JOINT_RIGIDITY_PROMISING | one-comparator pole distinction is not globally robust; stronger simultaneous constraints may be rigid |
| F5 joint discriminator | ACTIVE | need exact `I_UV` comparison at a concrete admissible non-string point/subclass |
| F6 identifiability | BLOCKED | cannot precede exact F5 vector/profile |
| F7 resources | N/A_FOR_CURRENT_THEORY_LEVEL_AUDIT | no apparatus claim before F5/F6 |

## Candidate Gravity design lesson

The reusable result is now two-sided:

> Do not define KG novelty by one tunable spectral/response property. Instead search for **rigidity by overconstraint**: several independently required observable and consistency relations should be satisfied by one parent dynamics in such a way that broader comparator freedom cannot tune them independently.

For the interface problem this suggests an analogue of `I_UV` built from

`{J, N, retarded response, ordered/noncommuting response, higher cumulants, entanglement/non-LOCC witness, Ward/Bianchi/contact identities}`.

## Current first blocker

`BESPOKE_CONCRETE_UNITARY_POINT_AND_JOINT_VECTOR_FREEZE`:

1. select a concrete non-string bespoke amplitude point/subclass that survives the published unitarity restrictions;
2. determine whether its pole spectrum can be aligned with the type-II target while remaining genuinely non-string;
3. compare residues/spin decomposition, Regge trajectory, sum rules and low-energy expansion simultaneously;
4. state explicitly which assumptions trigger generalized-Virasoro string-spectrum rigidity and which broader bespoke assumptions relax it;
5. feed the resulting rigidity/non-rigidity lesson into `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md`.

## Operational completion estimate

**60%**.

## Sources

1. C. Cheung and G. N. Remmen, *Bespoke dual resonance*, Phys. Rev. D 108, 086009 (2023): customizable mass spectra, dual resonance, UV behavior, and unitary non-string regions.
2. R. Bhardwaj, M. Spradlin, A. Volovich, H.-C. Weng, *Unitarity of bespoke amplitudes*, Phys. Rev. D 110, 106016 (2024): asymptotically nonlinear Regge trajectories ruled out in the analyzed bespoke class; constraints on asymptotically linear cases; Regge-sum-rule/high-energy restrictions.
3. N. Geiser and L. W. Lindwasser, *Generalized Veneziano and Virasoro amplitudes*, JHEP 04 (2023) 031: generalized Veneziano families exist, while the generalized Virasoro consistency conditions select the string spectrum.
4. Coon-amplitude positivity/unitarity literature retained as an additional comparison branch.
