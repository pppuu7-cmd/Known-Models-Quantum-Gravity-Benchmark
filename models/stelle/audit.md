# Model Audit — standard Stelle quadratic gravity, Minkowski fundamental-theory control

Benchmark ID: KMQGB-M07-STELLE
Concrete realization ID: STELLE-MINK-STANDARD-FEYNMAN-001
Role: pathological massive-spin-2 pole / renormalizability-vs-unitarity control
State: CLOSED / TERMINAL
Terminal status: FAIL_RQIR_CONSISTENCY

## Frozen theory

Freeze the four-dimensional local quadratic-gravity action in the convention

`S = -(1/(2 kappa)) ∫ d^4x sqrt(-g) [ R + (gamma/2) R^2 - (alpha/2) C_abcd C^abcd ]`,

expanded about Minkowski spacetime, with `alpha>0`, `gamma>0` so the extra pole masses are real in the declared convention.

For a concrete symmetric benchmark choose a positive reference mass `mu` and

`alpha = 1/mu^2`,

`gamma = 1/(3 mu^2)`,

so that the linearized massive spin-2 and spin-0 scales are both finite and real (`M_2=mu`, `M_0=mu`) while remaining distinct by spin/projector structure.

The quantization prescription is deliberately frozen to the **standard perturbative Feynman/Hilbert-space interpretation** in which the propagating poles are treated as physical spectrum states. This audit does not silently import fakeon, Lee-Wick, PT/pseudo-Hermitian, Krein-space or other modified prescriptions.

## Spectrum around Minkowski

The local quadratic action propagates

1. the ordinary massless spin-2 graviton;
2. a massive scalar from the `R^2` sector;
3. a massive spin-2 mode from the Weyl-squared/Ricci-squared sector.

The spin-2 propagator has the schematic pole structure

`D_2(p) ∝ 1/(p^2+i0) - 1/(p^2-M_2^2+i0)`

up to the common spin-2 projector and normalization.

The opposite residue is not optional if the propagator is to have the improved `1/p^4` ultraviolet behavior. Thus the same structural feature that makes the theory power-counting renormalizable introduces a negative-residue massive spin-2 state in the standard interpretation.

## Weak-field fingerprint

For a pointlike nonrelativistic source the standard quadratic-gravity potentials have the form

`Phi(r) = -G M_s/r [1 + (1/3)e^(-M_0 r) - (4/3)e^(-M_2 r)]`,

`Psi(r) = -G M_s/r [1 - (1/3)e^(-M_0 r) - (2/3)e^(-M_2 r)]`.

The `+1/3` scalar Yukawa term is the same-sign healthy scalar type already familiar from pure `R+R^2`; the massive spin-2 contribution enters with the opposite-residue structure. The weak-field potential itself is a useful diagnostic but is not the terminal gate: the pole residue already supplies the sharper consistency test.

## F0–F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 — dynamics | PASS | exact local action and quantization convention frozen |
| F1 — required limits | PASS_SCOPED | Einstein behavior recovered below/away from the massive poles or as quadratic masses are decoupled |
| F2 — consistency | FAIL_STANDARD_UNITARITY_POSITIVITY | the massive spin-2 pole has residue opposite to the massless graviton; standard physical-state quantization contains a ghost / violates the positive-state requirement |
| F3 — RQIR hierarchy | NOT_PROMOTED | no reason to promote beyond a failed mandatory consistency gate |
| F4 — comparator distinction | NOT_REACHED | consistency failure precedes novelty testing |
| F5 | NOT_REACHED | forbidden after F2 failure |
| F6 | NOT_REACHED | forbidden after F2 failure |
| F7 | NOT_REACHED | forbidden after F2 failure |

## Why this is a real RQIR consistency failure

This differs from the earlier benchmark outcomes:

- M01-M04 were exact comparator controls;
- M05-M06 were observational/model-identification degeneracies without inconsistency;
- M07, as frozen here, has a mandatory physical-state problem already in its linearized spectrum.

For the standard quantization, the massive spin-2 mode cannot simultaneously be interpreted as an ordinary positive-residue physical particle while retaining the propagator structure that gives the `1/p^4` UV improvement. In conventional language it is the Stelle ghost.

Therefore the first terminal gate is F2, not F4/F6.

## Scope guardrails

`FAIL_RQIR_CONSISTENCY` applies only to the explicitly frozen **standard fundamental Stelle realization with the standard physical-state/Feynman interpretation**.

It does **not** establish that every use of curvature-squared operators is inconsistent:

- a low-energy EFT may include higher-curvature operators while keeping any extra pole above the EFT cutoff; that is a different M08-type realization;
- pure `R+R^2` lacks the massive spin-2 ghost and was audited separately as M05;
- fakeon/Lee-Wick/modified-inner-product or other nonstandard prescriptions change the physical-state/analytic structure and require separate audits rather than being credited to this standard model automatically;
- recent papers continue to explore such alternative prescriptions, so the benchmark retains them as possible separate future branches, not repairs assumed by fiat.

## Terminal decision

`FAIL_RQIR_CONSISTENCY`

First failing gate: `F2_STANDARD_MASSIVE_SPIN2_GHOST`.

This is the first queue item that fails a mandatory RQIR consistency gate rather than merely losing novelty or identifiability.

## Q1–Q7 consequence

Because F2 fails for the frozen fundamental quantization, no Q1–Q7 observational fingerprint may promote this realization to Candidate Gravity. Its weak-field and radiative signatures remain useful negative controls and design warnings, especially that UV power counting cannot substitute for physical-state positivity/unitarity.

## Sources

1. K. S. Stelle, classic higher-derivative gravity results: local curvature-squared gravity is perturbatively renormalizable and contains an additional massive spin-2 ghost in the standard formulation.
2. A. Salvio, *Quadratic Gravity*, Frontiers in Physics 6, 77 (2018), arXiv:1804.09944: spectrum, `1/p^4` UV behavior, opposite spin-2 residues and ghost discussion.
3. A. Hindawi, B. A. Ovrut and D. Waldram, Phys. Rev. D 53, 5583 (1996): second-order field-content representation and ghostlike massive spin-2 field around flat space.
4. Recent 2025-2026 literature exploring alternative ghost prescriptions or constrained quadratic-gravity radiation is retained as evidence that those are distinct prescription/model questions, not automatic repairs of the frozen standard realization.
