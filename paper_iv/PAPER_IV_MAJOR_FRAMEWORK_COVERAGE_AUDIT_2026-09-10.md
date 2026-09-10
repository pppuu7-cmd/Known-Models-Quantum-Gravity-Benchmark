# Paper IV — Major-Framework Coverage Audit

**Date:** 2026-09-10  
**Iteration:** 183  
**RQIR authority:** Core v1.0 FROZEN  
**Scope:** KMQGB coverage completeness before any global terminal decision.

## Research question

KMQGB is intended to answer a stronger question than whether five selected benchmark rows can be evaluated: **after running the major known quantum-gravity schools through the same frozen RQIR funnel, is an existing/adapted/hybrid construction sufficient, or is a genuinely new Candidate Gravity model required?**

For that purpose, D2 must certify two different things:

1. **framework-set completeness** — no materially independent major school has been silently omitted; and
2. **object completeness** — every admitted school has a complete same-realization physical object suitable for a common comparator quotient.

Iteration 182 made item (2) explicit for the five then-active rows, but it did not yet prove item (1).

## External coverage authority

The 2024 *Handbook of Quantum Gravity*, edited by C. Bambi, L. Modesto and I. Shapiro (Springer, DOI `10.1007/978-981-99-7681-2`), describes itself as comprehensive coverage of the main approaches and contains dedicated sections for:

- Effective Quantum Gravity;
- Perturbative Quantum Gravity, including a dedicated Hořava-model chapter;
- Asymptotically Safe Quantum Gravity;
- Nonlocal Quantum Gravity;
- String Theories, including AdS/CFT;
- Causal Sets;
- Causal Dynamical Triangulations;
- Loop Quantum Gravity and Spinfoams.

KMQGB Iter182 had terminal-matrix rows only for GR/EFT, a scoped string/dual-resonance object, Asymptotic Safety, LQG/spinfoam and Causal Fermion Systems. Repository search found no dedicated benchmark records for CDT, causal sets, nonlocal gravity or Hořava-Lifshitz gravity.

Group Field Theory is retained as a separate coverage obligation rather than silently folded into LQG. Modern literature explicitly notes that, although GFT is tightly connected to spin foams and can generate spin-foam sums, covariant and canonical GFT formulations can carry distinct structures and dynamics; the relation to LQG/spinfoam therefore has to be **proved for the selected realization**, not assumed by family resemblance.

Causal Fermion Systems remains admitted because it is already an independent KMQGB branch with its own microscopic dynamics and gravity-continuum map, even though it is not one of the Handbook section headings above.

## Coverage correction

The Iter182 statement that the D2/D4 matrix had five required rows is now classified as a **provisional active-set statement**, not a complete census of major known schools.

The new contract `protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json` establishes 11 Tier-1 rows:

1. GR + controlled low-energy EFT — baseline/comparator;
2. perturbative renormalizable / higher-derivative quantum gravity;
3. Hořava-Lifshitz quantum gravity;
4. Asymptotic Safety;
5. nonlocal / infinite-derivative quantum gravity;
6. string / M-theory / holographic quantum gravity;
7. causal sets;
8. CDT/EDT;
9. LQG/EPRL-spinfoam;
10. GFT/tensor models;
11. Causal Fermion Systems.

This is **not** an assertion that 11 names exhaust every proposal ever published. It is a fail-closed major-family layer. A Tier-2 watchlist captures programs whose independence/classification must still be resolved before D7: supergravity/double-copy, noncommutative/spectral geometry, twistor/amplitude programs, canonical Wheeler-DeWitt geometrodynamics, and emergent/induced/graph-based programs.

A watchlist entry must either:

- be promoted to Tier-1;
- be merged into another row by an explicit reduction/equivalence map;
- or be excluded from the Paper-IV target by a written scope proof.

Silence is not a valid resolution.

## Strong anti-overclaim rule

A **single successful or failed representative realization does not establish a family-wide verdict** unless one of the following is supplied:

- a theorem/no-go whose assumptions cover the material family;
- an explicit equivalence-class argument showing the other variants do not add independent RQIR directions;
- or a documented audit of all materially distinct subfamilies.

This matters especially for the existing `STRING_DUAL_RESONANCE` result: the Virasoro–Shapiro/dual-resonance rigidity benchmark is a strong scoped result, but it is not equivalent to a full verdict on string/M-theory/holography.

Likewise, a GFT result may be merged into the LQG/spinfoam row only for a declared realization for which the map of state space, dynamics and observables is explicit.

## D2 consequence

Under the strengthened KMQGB objective, D2 now has a two-factor structure:

`D2 = D2A_framework_set_coverage AND D2B_complete_objects`.

At Iter183:

- `D2A_framework_set_coverage = NOT_CLOSED`;
- `D2B_complete_objects = NOT_CLOSED`;
- therefore `D2 = NOT_CLOSED`.

Only the GR/EFT baseline is presently in a terminal coverage state at the Tier-1 census level. The earlier string result is `PARTIAL_SUBFAMILY_ONLY`; AS/LQG/CFS are object-blocked; six additional Tier-1 candidate-family rows have not yet received a dedicated RQIR benchmark.

The percentage `2/5` used as an informal description of the Iter182 active matrix must therefore **not** be used as the completeness percentage for the stronger major-school D2 objective.

## D4 consequence

The Iter182 five-row comparator matrix remains valid for the rows it actually contains, but it is now explicitly a **partial active-set matrix**. It cannot become globally complete until the admitted coverage contract is resolved and every required Tier-1 candidate family either has a comparator-subtracted residual or a proved merge/scope disposition.

No missing school is assigned residual zero.

## D7 consequence

No global terminal decision is allowed while either:

- a Tier-1 row is nonterminal;
- or a Tier-2 classification remains unresolved.

In particular `NEW_REQUIRED` is forbidden because omitted/not-yet-benchmarked schools constitute **zero exclusion evidence**.

## Immediate research queue

The next benchmark wave should add the omitted major families rather than invent Candidate Gravity. Priority is based on availability of physical observables and discriminatory power:

1. **Nonlocal quantum gravity** — explicit propagator/form-factor/scattering structures make a comparator-ready hard-amplitude benchmark feasible.
2. **CDT/EDT** — invariant spectral/curvature/finite-size observables and an explicit continuum-limit programme make it a strong independent nonperturbative row.
3. **Hořava-Lifshitz** — distinctive anisotropic scaling/extra-mode structure allows clean consistency and propagation comparators.
4. **Causal sets** — strong causal/discrete observables but a more difficult dynamics-to-continuum attribution problem.
5. **Perturbative higher-derivative gravity** — important UV-completion family, with the physical pole/unitarity prescription itself part of the RQIR object.
6. **GFT/tensor models** — first resolve whether a chosen realization is independent of the already-tested spinfoam branch; if yes, benchmark its own continuum/condensate observable.

The three existing CW2 blockers (AS, LQG, CFS) remain open in parallel. Candidate Gravity remains inactive.

## Scientific conclusion

This audit makes the eventual inference `NEW_REQUIRED` harder but scientifically much stronger. KMQGB must first demonstrate that the known-theory search space was not artificially narrowed to a handful of convenient rows. The correction changes **KMQGB coverage governance only**; it does not reveal a semantic defect in RQIR Core v1.0 and therefore does not justify modifying the frozen RQIR methodology.
