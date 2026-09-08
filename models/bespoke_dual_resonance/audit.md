# Model Audit — generalized bespoke dual-resonance UV amplitudes

Benchmark ID: KMQGB-T3-M01-BESPOKE-UV
Concrete research target: `BESPOKE-DUAL-RESONANCE-UV-001`
Role: broad same-domain UV amplitude adversary for string-like pole/residue fingerprints and future KG UV claims
State: ACTIVE / NONTERMINAL

## Frozen authority set

Use

1. Cheung–Remmen bespoke dual-resonance amplitudes;
2. Bhardwaj–Spradlin–Volovich–Weng partial-wave unitarity constraints;
3. Geiser–Lindwasser generalized Veneziano/Virasoro recursion and rigidity analysis;
4. Coon amplitudes as a concrete analytically controlled non-string deformation inside the generalized Veneziano branch.

Published properties relevant to the benchmark include customizable spectra, dual resonance, polynomial/simple-pole residue structure, tame UV behavior and non-string unitary regions. Later work excludes the analyzed asymptotically nonlinear Regge trajectories and sharply restricts asymptotically linear cases.

## Concrete non-string unitary point — frozen, but not yet the terminal closed-string comparator

To eliminate the vague phrase “there exist unitary deformations,” freeze the generalized-Veneziano **Coon point**

`q = 1/2`.

Geiser–Lindwasser report that the Coon subfamily in the range `0 < q <= 2/3` is unitary in any dimension in their analyzed generalized-Veneziano setting. Therefore `q=1/2` is a concrete non-string point well inside that published region.

This point is useful for the **rigidity audit** because it proves explicitly that analyticity/duality/unitarity do not by themselves isolate the ordinary Veneziano spectrum in the open/generalized-Veneziano problem.

However, it is **not** promoted as the terminal adversary for the type-II four-graviton Virasoro–Shapiro amplitude:

- the generalized Veneziano/Coon branch has different crossing/external-state structure from the closed-string four-graviton target;
- using it as if it were an exact same-channel gravitational comparator would violate the common-domain/external-state guardrail.

Therefore T3-01 remains open for a physically admissible **closed/same-channel** comparator or a proof that the stronger generalized-Virasoro assumptions already enforce rigidity there.

## Immediate consequence for string pole support

Second-wave S2-M05 established only

`P_s^VS != P_s^HR-single-mass`.

The bespoke construction shows why pole support alone is too weak globally: a wider parent amplitude can treat the mass spectrum as an input degree of freedom.

Current classification of **pole support alone**:

`INSUFFICIENT_FOR_GLOBAL_UV_IDENTIFICATION`.

This does not prove that a fully unitary non-string closed-string-like amplitude reproduces the full type-II Virasoro-Shapiro pole/residue data.

## Rigidity result

The generalized Veneziano/Virasoro analysis supplies the complementary result:

- generalized Veneziano admits nontrivial two-parameter families, including Coon-like deformations;
- under the generalized-Virasoro physical assumptions studied by Geiser–Lindwasser, the spectral constraints form an overdetermined nonlinear recursion system and the only consistent spectrum found is the string spectrum.

The scientific lesson is assumption-sensitive **rigidity by overconstraint**.

A broad family can make one fingerprint tunable; a stronger simultaneous constraint set can collapse the allowed solution space.

## Frozen joint UV vector

`I_UV = {P, R, S, C, Regge, B, EFT}`

with

- `P`: pole locations/support;
- `R`: residues and partial-wave decomposition;
- `S`: spin/degeneracy content at each mass level;
- `C`: crossing/dual-resonance relations among channels;
- `Regge`: asymptotic trajectory class;
- `B`: high-energy boundedness and Regge/superconvergence sum rules;
- `EFT`: correlated low-energy Wilson-coefficient expansion.

A string-specific or KG-specific UV residual is not accepted unless at least one component of the **joint vector** remains unmatched after profiling the widest physically admissible same-channel family.

## F0-F7 map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics/amplitude | PASS_FAMILY_LEVEL | explicit closed-form families plus concrete Coon `q=1/2` point |
| F1 IR/external-state match | PARTIAL | Coon point gives a concrete non-string unitary deformation but not the same closed four-graviton channel |
| F2 consistency | PASS_PARTIAL | `q=1/2` lies in published unitary generalized-Veneziano region; bespoke asymptotically-linear restrictions retained |
| F3 RQIR hierarchy | AMPLITUDE_SECTOR_ONLY | UV S-matrix comparator, not source/noise/interface model |
| F4 distinction | POLE_SUPPORT_INSUFFICIENT / VIRASORO_RIGIDITY_PROMISING | one-feature tuning exists in broader branches; closed-string assumptions may be rigid |
| F5 joint discriminator | ACTIVE | need same-channel closed/gravitational `I_UV` comparison or a rigorous rigidity boundary |
| F6 identifiability | BLOCKED | cannot precede F5 |
| F7 resources | N/A | theory-level amplitude audit |

## Candidate Gravity design lesson

The benchmark now has a concrete two-sided prototype:

- `q=1/2` Coon: a healthy non-string deformation exists when assumptions leave enough freedom;
- generalized Virasoro: stronger simultaneous constraints collapse the spectrum back to string.

Future KG should seek the second behavior: **observable/consistency relations should overdetermine the model**, not leave a large parent family able to tune each channel independently.

## Current blocker

`BESPOKE_CLOSED_CHANNEL_RIGIDITY_BOUNDARY`:

1. state exactly which generalized-Virasoro assumptions force the string spectrum;
2. identify whether a non-string closed/same-external-state amplitude survives after relaxing one assumption at a time while retaining unitarity/crossing/high-energy bounds;
3. compare the full `I_UV`, not just poles;
4. determine the minimal assumption set at which the solution space collapses from a family to the string point;
5. export that “minimal rigidity set” as a template for future KG model construction.

## Operational completion estimate

**70%**.

## Sources

1. C. Cheung, G. N. Remmen, Phys. Rev. D 108, 086009 (2023), bespoke dual resonance.
2. R. Bhardwaj et al., Phys. Rev. D 110, 106016 (2024), partial-wave unitarity and Regge constraints.
3. N. Geiser, L. W. Lindwasser, JHEP 04 (2023) 031, generalized Veneziano/Virasoro recursions; generalized-Virasoro string-spectrum rigidity; Coon unitary subregion.
