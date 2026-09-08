# T3-01 Audit — closed-channel dual-resonance / Virasoro-Shapiro rigidity boundary

Benchmark ID: `KMQGB-T3-M01-BESPOKE-UV`  
Frozen terminal comparator realization: `VS-DEFORM-LAMBDA2-D4-001`  
Role: same-channel adversary for string-like UV fingerprints and prototype of rigidity-by-overconstraint  
State: **TERMINAL — `PASS_RQIR_GATE`**  
Objective: **`CLOSED_CHANNEL_RIGIDITY_BOUNDARY_ESTABLISHED`**

## Terminal scientific question

Can physically sensible non-string amplitudes reproduce a large fraction of the closed-string four-point structure, and if so, what additional condition collapses that freedom back to the Virasoro–Shapiro point?

The answer is now concrete and two-sided:

1. **Yes under weaker assumptions.** Cheung–Hillman–Remmen construct a parameterized family of fully permutation-symmetric deformations of the Virasoro–Shapiro amplitude. In `D=4` the relevant partial-wave coefficients are nonnegative for `lambda >= 0` in the analyzed family, while `lambda=1` returns the Virasoro–Shapiro point. Thus there are same-channel non-string deformations satisfying crossing/level-truncation structure and the tested positivity condition.
2. **No after the stronger softness condition.** Requiring superpolynomially soft Regge behavior together with level truncation selects the Virasoro–Shapiro amplitude uniquely in this bootstrap class and yields the string spectrum as an output rather than an input.

Therefore the terminal result is not “string theory globally unique.” It is the sharper statement that a **minimal rigidity boundary has been exhibited inside a concrete same-channel bootstrap class**.

## Frozen concrete adversary

Choose

`lambda = 2`, `D = 4`

inside the Cheung–Hillman–Remmen closed-channel deformation family.

This is deliberately not the string point `lambda=1`.

Published family properties relevant to the benchmark:

- fully permutation-symmetric closed-string-like four-point structure;
- linear massive spectrum with a lambda-dependent shift/slope in the paper's normalization;
- level truncation;
- leading/subleading graviton soft behavior consistent with the displayed construction;
- nonnegative partial waves in `D=4` for `lambda >= 0` in the reported positivity analysis;
- generic deformations have gravitational Regge scaling no better than pure GR and are therefore not bona fide UV completions of gravity in the strong string-softness sense.

`lambda=2` is therefore a useful **same-external-state near-adversary**: it survives many lower constraints while failing the strongest stringy UV softness criterion.

## Frozen joint UV vector

Use

`I_UV = {P,R,S,C,Pos,Soft,Regge,EFT}`

with

- `P`: pole locations / mass spectrum;
- `R`: residues and their partial-wave decomposition;
- `S`: spin content / level truncation;
- `C`: full permutation/crossing structure;
- `Pos`: partial-wave positivity in the declared dimension;
- `Soft`: superpolynomial fixed-transfer Regge softness;
- `Regge`: ordinary Regge scaling class;
- `EFT`: correlated low-energy coefficient trajectory.

The important result is that the first several components do **not** by themselves isolate string theory. The decisive extra condition in this bootstrap class is `Soft`.

## Rigidity ladder

The benchmark now has a clean hierarchy:

### Weak fingerprint

`pole tower` alone — insufficient. Broader bespoke/dual-resonance families can tune spectral structure.

### Intermediate fingerprint

`{crossing, linear tower, level truncation, soft graviton behavior, positivity}` — still not sufficient. Closed-channel lambda-deformations survive.

### Strong rigidity set

`{level truncation + superpolynomial Regge softness}` within the Cheung–Hillman–Remmen fully permutation-symmetric bootstrap — selects Virasoro–Shapiro uniquely.

This is exactly the type of **overconstrained relation** KMQGB seeks as a design template for future Candidate Gravity.

## Relation to earlier T3-01 evidence

- Cheung–Remmen bespoke dual resonance showed that broad parent families can customize spectra.
- Bhardwaj–Spradlin–Volovich–Weng showed that unitarity sharply prunes those families.
- Geiser–Lindwasser showed assumption-sensitive generalized-Virasoro rigidity.
- The 2025 Cheung–Hillman–Remmen result supplies the missing same-channel closed-string deformation family and an explicit physical boundary at superpolynomial softness.

The previously frozen Coon `q=1/2` point remains useful as an open/generalized-Veneziano example of non-rigidity, but it is no longer needed as a surrogate closed-string comparator.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 amplitude object | PASS | explicit closed-form same-channel deformation family |
| F1 external-state / IR structure | PASS_SCOPED | massless/gravitational closed-channel setup and soft behavior frozen |
| F2 consistency | PASS_PARTIAL | D=4 partial-wave positivity for lambda>=0 in reported analysis; not a complete microscopic-theory unitarity proof |
| F3 hierarchy | AMPLITUDE_SECTOR_ONLY | S-matrix comparator, not full source/noise/interface theory |
| F4 comparator distinction | PASS | non-string lambda deformation survives many string-like lower constraints |
| F5 hard rigidity discriminator | **PASS_RQIR_GATE** | superpolynomial softness + level truncation isolates VS in the declared bootstrap class |
| F6 identifiability | N/A_FOR_METHOD_OBJECT | target is a theoretical rigidity boundary |
| F7 resources | N/A | no apparatus claim |

## Terminal status

`PASS_RQIR_GATE`

with objective

`CLOSED_CHANNEL_RIGIDITY_BOUNDARY_ESTABLISHED`.

This status means the **methodological comparator question is answered**, not that the lambda=2 deformation is promoted as a complete UV theory and not that all conceivable quantum-gravity amplitudes have been excluded.

## Candidate Gravity design lesson

This is one of the strongest reusable lessons of KMQGB:

> A robust KG signature should be selected by an intersection of independent physical requirements, not by one unusual observable. The useful feature is the point where adding one independently motivated condition collapses a previously continuous comparator family to a low-dimensional or isolated solution.

For the interface problem, the analogue is to search for a relation such as

`F(J,N,chi_R,rho_comm,Q_channel,K3_plus,Ward/contact,...)=0`

that a broad classical/stochastic/ordinary-quantum comparator family can satisfy only at isolated or forbidden parameter points.

Do **not** copy “superpolynomial softness” into KG blindly; copy the structural idea of **rigidity by independently motivated overconstraint**.

## Reopen condition

A future wave may challenge this result with a broader closed-channel amplitude class that violates one bootstrap assumption while retaining all physically required observables. That would refine the rigidity boundary but would not invalidate the present scoped result.

## Terminal completion

**100% — terminal methodological PASS.**

## Sources

1. C. Cheung, G. N. Remmen, Phys. Rev. D 108, 086009 (2023), bespoke dual resonance.
2. R. Bhardwaj et al., Phys. Rev. D 110, 106016 (2024), unitarity constraints on bespoke amplitudes.
3. N. Geiser, L. W. Lindwasser, JHEP 04 (2023) 031, generalized Veneziano/Virasoro rigidity structure.
4. C. Cheung, A. Hillman, G. N. Remmen, Phys. Rev. D 111, 086034 (2025), same-channel Virasoro–Shapiro deformations and uniqueness under superpolynomial softness + level truncation.
