# Model Audit — perturbative higher-curvature gravity EFT control

Benchmark ID: KMQGB-M08-HIGHER-CURVATURE
Concrete realization ID: GR-EFT-RIEMANN3-MINK-001
Role: EFT positive control / boundary against fundamental quadratic-gravity ghost overreach
State: CLOSED / TERMINAL
Terminal status: EXACT_COMPARATOR_IDENTITY

## Frozen EFT

Use four-dimensional weak-field gravity below a cutoff `Lambda` with the local EFT action

`S_EFT = ∫ d^4x sqrt(-g) [ (M_Pl^2/2) R + (d_3/Lambda^2) O_R3 + ... ]`,

where `O_R3` is one fixed parity-even cubic Riemann/Weyl curvature invariant basis element and `d_3` is a finite Wilson coefficient. The precise basis choice may be changed by allowed local field redefinitions, but the observable matching coefficient is retained.

Frozen regime:

- asymptotically Minkowski weak field;
- characteristic external momentum/curvature scale `Q << Lambda`;
- expansion truncated consistently at the first order in `d_3 Q^2/Lambda^2` required by the declared observable;
- higher-derivative terms are treated perturbatively as EFT insertions, **not resummed into a fundamental propagator**.

## Physical-state rule

The low-energy propagating gravitational degrees of freedom are those of the retained light theory: the massless spin-2 graviton (plus any explicitly retained light matter).

Extra roots that appear when a finite higher-derivative truncation is promoted beyond its perturbative order are not automatically physical EFT states. Such roots lie at or above the scale where the derivative expansion ceases to be controlled and are a signal not to extrapolate the truncated EFT as a fundamental theory.

This is the key distinction from M07 Stelle gravity, where the finite fourth-order action and standard quantization were deliberately promoted as a fundamental spectrum and the massive spin-2 pole was therefore a physical ghost.

## Why use a curvature-cubed operator

In four-dimensional pure gravity, curvature-squared operators are especially basis/redefinition-sensitive for on-shell vacuum graviton amplitudes. A six-derivative curvature-cubed operator supplies a clean independent local higher-curvature EFT direction while preserving the same low-energy light spectrum when treated perturbatively.

Recent EFT work explicitly demonstrates an action-based removal of spurious degrees of freedom for GR supplemented by a cubic Riemann term, reinforcing that higher derivatives in a truncated EFT must not automatically be interpreted as additional physical particles.

## Comparator relation

The frozen RQIR comparator C5 is perturbative quantum gravity / low-energy quantum GR. The repository's permanent C5 realization `ANSATZ-PQG-EFT-001` already includes symmetry-allowed EFT higher operators and their renormalized/matched coefficients.

Therefore `GR-EFT-RIEMANN3-MINK-001` is not a new theory class beyond C5. It is one concrete Wilson-coefficient slice of the same low-energy gravitational EFT architecture.

At a fixed nonzero `d_3`, an observable may differ from pure Einstein C0. But after the required C5 quotient that permits the corresponding higher-curvature Wilson coefficient, the theory-class residual is zero.

## F0–F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | explicit EFT action, cutoff and perturbative order frozen |
| F1 — required limits | PASS | `d_3 -> 0` or `Q/Lambda -> 0` recovers Einstein gravity; ordinary QFT/EFT limit maintained |
| F2 — consistency | PASS_EFT_SCOPED | no extra physical pole is admitted inside the controlled EFT spectrum merely by resumming a truncated equation |
| F3 — RQIR hierarchy | PASS/PARTIAL_C5 | response/higher correlators belong to the same perturbative low-energy QG/EFT framework |
| F4 — comparator distinction | EXACT_IDENTITY_C5_CLASS | higher-curvature Wilson operators are part of C5 EFT architecture |
| F5 | NOT_NOVEL | no independent model direction relative to C5 after Wilson-coefficient profiling |
| F6 | NOT_NOVEL | identifiability can constrain `d_3`, but not promote a new theory class versus C5 |
| F7 | NOT_REQUIRED_FOR_CLASS_IDENTITY | resource forecasts are separate from theory-class identity |

## Terminal decision

`EXACT_COMPARATOR_IDENTITY` with C5 at the low-energy EFT theory-class level.

Important residual distinction:

- versus C0/Einstein with `d_3=0`: generally nonzero for an observable sensitive to `O_R3`;
- versus C5 with the corresponding Wilson coefficient admitted: `0` at theory-class level.

This is not a consistency failure.

## Boundary lesson from M07 -> M08

A finite higher-derivative expression can mean two scientifically different things:

1. **fundamental/resummed theory** with extra poles in the physical spectrum — M07 standard Stelle, which fails the frozen positivity/unitarity gate because of its massive spin-2 ghost;
2. **ordered low-energy EFT expansion** below a cutoff — M08, where the higher-curvature term is a perturbative Wilson insertion and spurious high-scale roots are not promoted into the low-energy state space.

The benchmark must preserve this distinction or it would incorrectly reject ordinary gravitational EFT.

## Sources

1. J. F. Donoghue and standard gravitational EFT literature: general covariance organizes an energy/derivative expansion with higher-curvature Wilson coefficients while GR remains predictive at low energy.
2. D. Glavan, S. Mukohyama and T. Zlosnik, *Removing spurious degrees of freedom from EFT of gravity*, JCAP 01 (2025) 111, arXiv:2409.15989: explicit cubic-Riemann EFT treatment and removal of spurious higher-derivative degrees of freedom at the working order.
3. Existing RQIR `ANSATZ-PQG-EFT-001` / C5 authority: low-energy perturbative quantum GR including EFT higher operators.
