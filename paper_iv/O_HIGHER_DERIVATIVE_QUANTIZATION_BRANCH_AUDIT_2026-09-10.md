# Higher-derivative quantum gravity: quantization-branch audit

**Date:** 2026-09-10  
**KMQGB iteration:** 187  
**Family:** `PERTURBATIVE_HIGHER_DERIVATIVE`  
**RQIR authority:** Core v1.0 FROZEN

## Question

Can the higher-derivative family be given a family-level PASS/FAIL from the familiar massive spin-2 ghost pole, or must RQIR resolve materially distinct quantization prescriptions before D2/D4/D7 can use this family?

## 1. Common action-level structure

For four-dimensional local curvature-squared gravity, the renormalizable action contains the Einstein term plus quadratic curvature operators (equivalently an `R^2` and a Weyl-squared sector up to topological/redefinition choices). Around a flat or weakly curved background, the spin-2 inverse propagator is fourth order. Schematically, after the physical spin-2 projection,

`D_2(p) ~ 1/[p^2 (1 + p^2/m_2^2)]`

so that partial-fraction decomposition produces the massless graviton pole plus an additional massive spin-2 pole with the opposite bare residue (sign conventions can move overall signs but not the relative-pole fact).

This structural pole statement is common to the local four-derivative parent. It is **not by itself a family-level unitarity verdict**, because the literature contains inequivalent prescriptions for what the extra pole means physically and how it enters cuts/asymptotic states.

Primary background authorities:

- K. S. Stelle, *Renormalization of Higher-Derivative Quantum Gravity*, Phys. Rev. D 16, 953 (1977), DOI 10.1103/PhysRevD.16.953.
- A. Salvio, *Quadratic Gravity*, Front. Phys. 6, 77 (2018), arXiv:1804.09944.

## 2. Material quantization branches

### B1 — conventional bare/indefinite-metric ghost interpretation

The bare propagator contains an opposite-residue massive spin-2 mode. Under a naive stable positive-probability particle interpretation this is the standard ghost problem.

However, RQIR may not promote the bare-pole observation into a whole-family FAIL because later work treats the mode as unstable/dressed or changes the physical inner product/prescription. In particular, Antoniadis–Tomboulis argued that gauge-dependent complex dressed poles need not occur in the physical S-matrix, and Donoghue–Menezes later formulated an unstable-ghost resonance treatment.

Authorities:

- I. Antoniadis, E. T. Tomboulis, *Gauge invariance and unitarity in higher-derivative quantum gravity*, Phys. Rev. D 33, 2756 (1986), DOI 10.1103/PhysRevD.33.2756.
- J. F. Donoghue, G. Menezes, *Unitarity, stability and loops of unstable ghosts*, arXiv:1908.02416.

**KMQGB disposition:** `SCOPED_STRUCTURAL_GHOST_POLE_CONTROL__NOT_FAMILY_TERMINAL`.

### B2 — fakeon / purely-virtual spin-2 prescription

The fakeon construction uses a nonanalytic/average-continuation prescription so that the massive spin-2 degree of freedom is not an asymptotic state. The cited construction establishes perturbative unitarity under that prescription and retains power-counting renormalizability. The same framework has explicit inflationary observables for `R + R^2 + C^2` gravity.

It also predicts a modification/violation of ordinary microscopic causality above the fakeon scale. This cannot be silently replaced by ordinary local-QFT microcausality. RQIR G4 explicitly allows a *declared controlled-nonlocal replacement*, so this fact is not automatically a terminal FAIL; instead it creates a same-realization obligation to state the causal replacement, its domain, its error/remainder control, and the corresponding observable/comparator.

Authorities:

- D. Anselmi, *Fakeons and Lee-Wick Models*, arXiv:1801.00915.
- D. Anselmi, M. Piva, *Quantum Gravity, Fakeons And Microcausality*, arXiv:1806.03605.
- D. Anselmi, *Fakeons, Microcausality And The Classical Limit Of Quantum Gravity*, arXiv:1809.05037.
- D. Anselmi, E. Bianchi, M. Piva, *Predictions of quantum gravity in inflationary cosmology: effects of the Weyl-squared term*, arXiv:2005.10293.
- M. Piva, *Higher-Derivative Quantum Gravity with Purely Virtual Particles: Renormalizability and Unitarity*, arXiv:2305.12549.

**KMQGB disposition:** `SCOPED_RENORMALIZABILITY_UNITARITY_CONTROL__MICROCAUSALITY_REPLACEMENT_OPEN`.

### B3 — Lee-Wick / unstable complex-resonance interpretation

This branch cannot be assigned a terminal KMQGB unitarity verdict from literature authority alone because materially contradictory analyses exist.

Donoghue–Menezes argue that the unstable ghostlike resonance does not belong to the asymptotic spectrum and give an all-orders unitarity argument based on cuts through stable states. Kubo–Kugo, using an operator treatment of complex ghosts, argue instead that complex ghost states can be created and that unitarity is violated above a definite threshold (while remaining unitary below it).

Authorities:

- J. F. Donoghue, G. Menezes, arXiv:1908.02416.
- J. Kubo, T. Kugo, *Unitarity Violation in Field Theories of Lee-Wick's Complex Ghost*, arXiv:2308.09006.
- D. Anselmi, *On the quantum field theory of the gravitational interactions*, arXiv:1704.07728.

**KMQGB disposition:** `BLOCKED_CONTESTED_UNITARITY_AUTHORITY__SAME_REALIZATION_CUT_CERTIFICATE_REQUIRED`.

### B4 — PT-symmetric / modified-inner-product branch

A distinct line of work argues that a non-Hermitian but PT-symmetric Hamiltonian can possess a positive physical inner product and remove the usual negative-norm conclusion. A separate canonical/BRST analysis of conformal quantum gravity reports an indefinite physical spin-2 subspace and S-matrix unitarity violation.

These are not safely interchangeable implementations, and the disagreement cannot be collapsed into a parent-family PASS or FAIL without fixing the exact action, Hilbert-space construction, asymptotic states and observable.

Authorities:

- P. D. Mannheim, *Solution to the ghost problem in higher-derivative gravity*, arXiv:2109.12743.
- J. Kubo, J. Kuntz, *Analysis of Unitarity in Conformal Quantum Gravity*, arXiv:2202.08298.

**KMQGB disposition:** `BLOCKED_DISTINCT_HILBERT_SPACE_REALIZATIONS__NO_COMMON_TERMINAL_OBJECT`.

### B5 — Euclidean reflection-positive lattice construction

Tomboulis exhibited a Euclidean lattice formulation of the general fourth-order action that is bounded and reflection positive, implying a positive Hilbert space/Hamiltonian through the Osterwalder-Schrader construction in that formulation.

This is an important positive control, but KMQGB does not currently possess a same-realization map from that Euclidean lattice construction to the Lorentzian continuum scattering/cosmology object used by the other branches.

Authority:

- E. T. Tomboulis, *Unitarity in Higher-Derivative Quantum Gravity*, Phys. Rev. Lett. 52, 1173 (1984), DOI 10.1103/PhysRevLett.52.1173.

**KMQGB disposition:** `SCOPED_EUCLIDEAN_OS_POSITIVITY_CONTROL__LORENTZIAN_CONTINUUM_MATCH_OPEN`.

## 3. Causality is diagnostic-dependent

A further reason not to use one slogan as the family verdict is that different causality diagnostics probe different statements. For quadratic gravity, a shock-wave/CEMZ analysis found a positive, polarization-independent Shapiro time delay in its declared setting, while fakeon work explicitly predicts microscopic causal modification and other analyses emphasize quantum uncertainty of causal structure.

Authorities:

- J. D. Edelstein, R. Ghosh, A. Laddha, S. Sarkar, *Causality constraints in Quadratic Gravity*, arXiv:2107.07424.
- J. F. Donoghue, G. Menezes, *Causality and gravity*, arXiv:2106.05912.

Therefore `CEMZ time-delay PASS` and `ordinary microcausality modified` are not logical contradictions; they are different observables/domains. RQIR requires the exact causal observable and prescription to be part of the realization vector.

## 4. What Iter187 closes

The old blocker bundled two logically different tasks: (i) establish that the higher-derivative pole problem forks into materially distinct physical prescriptions, and (ii) obtain terminal same-realization objects for those prescriptions.

Iter187 closes the **first task at the major-branch taxonomy level**:

- the opposite-residue spin-2 pole is an action-level structural fact, not a family verdict;
- fakeon, Lee-Wick/unstable-resonance, PT/modified-inner-product and Euclidean OS constructions cannot be silently merged;
- causality must be attached to a declared diagnostic/domain;
- at least one live branch (Lee-Wick/unstable resonance) has directly conflicting unitarity claims in the literature, which by itself forbids a terminal family verdict from citation counting.

It does **not** close D2/D4 for the family.

## 5. Refined family-level closure certificate

Replace the vague requirement `HIGHER_DERIVATIVE_POLE_PRESCRIPTION_FAMILY_MAP_PLUS_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE` by the narrower post-audit obligation:

`HIGHER_DERIVATIVE_MATERIAL_QUANTIZATION_BRANCH_TERMINAL_DISPOSITION_PLUS_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE`

Minimum payload:

1. explicit branch identifier and fixed local higher-derivative action;
2. exact pole locations/residues after the declared dressing/renormalization order;
3. physical Hilbert space / asymptotic-state rule;
4. cut/optical-theorem or equivalent unitarity certificate under that same prescription;
5. declared causality notion or controlled-nonlocal replacement and its domain;
6. normalized physical observable generated by the same realization;
7. IR/GR map;
8. identical-domain comparator set;
9. error/remainder and scheme dependence;
10. explicit disposition/reduction map for the remaining material quantization branches.

## 6. D7 consequence

`PERTURBATIVE_HIGHER_DERIVATIVE` remains `PARTIAL_SUBFAMILY_ONLY` and contributes **zero** family-exclusion evidence toward `NEW_REQUIRED`.

The research progress is a reduction of ambiguity: the blocker is no longer “does a ghost pole exist?” but “which quantization branch is the physical theory, and does one fixed branch simultaneously satisfy unitarity, its declared causality replacement, GR recovery and a comparator-ready observable?”

No RQIR Core change is required.
