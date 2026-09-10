# Paper IV Tier-2 classification audit

**Date:** 2026-09-10  
**Iteration:** 186  
**RQIR Core:** v1.0 FROZEN

## Purpose

Resolve the five Iter183 Tier-2 watchlist labels without using classification shortcuts to create exclusion evidence. A label is either reduced to an already admitted Tier-1 parent by an explicit representation/dynamics map, promoted to Tier-1 if it carries materially independent parent dynamics, or split if the label itself is not one theory.

## T2-01 — Supergravity / double copy

**Disposition:** `REDUCED_TO_TIER1_WITH_EXPLICIT_MAP`.

The watchlist label combined two different notions:

1. supergravity theories are gravity dynamics/EFTs and occur as low-energy limits or sectors of string/M-theory and as perturbative gravity theories;
2. color-kinematics/double-copy is a constructive amplitude/action map, not by itself a unique UV dynamics.

Carrasco and Zekioglu, arXiv:2511.01799, explicitly construct the Einstein effective action/operator expansion from double-copy-compatible gauge-theory amplitudes and extend the map to higher-derivative operators inspired by string amplitudes. Thus a result obtained solely by the double-copy map is assigned to the resulting gravity parent, not treated as an additional independent school.

Reduction map for this census:

- Einstein/supergravity output -> `GR_EFT` or `STRING_MTHEORY_HOLOGRAPHY` according to the declared UV parent;
- higher-derivative output -> `PERTURBATIVE_HIGHER_DERIVATIVE` or `STRING_MTHEORY_HOLOGRAPHY` according to ancestry;
- a future genuinely independent UV parent using double-copy structure must be promoted as its own Tier-1 row.

This classification gives **zero exclusion evidence**.

## T2-02 — Noncommutative spectral geometry

**Disposition:** `PROMOTED_TO_TIER1` as `NONCOMMUTATIVE_SPECTRAL_GEOMETRY`.

Reason: this is not merely a coordinate/representation trick. The spectral action principle defines dynamics from spectral data of a noncommutative geometry. Chamseddine–Connes spectral action yields the Standard Model coupled to Einstein plus Weyl gravity, and later reviews treat noncommutative geometry as a framework for modelling quantum spacetime.

Primary controls:

- Chamseddine & Connes, **The Spectral Action Principle**, arXiv:hep-th/9606001;
- Sakellariadou, **Noncommutative Spectral Geometry: A Short Review**, arXiv:1301.4687;
- Szabo, **Noncommutative Geometry of Gravity, Strings and Fields: A Panoramic Overview**, arXiv:2511.22672.

First-pass classification:

`PARTIAL_SUBFAMILY_ONLY__SPECTRAL_ACTION_GRAVITY_CONTROL`.

Exact blocker:

`NCG_SPECTRAL_ACTION_QUANTUM_DYNAMICS_PLUS_NORMALIZED_QG_OBSERVABLE_COMPARATOR_CERTIFICATE`.

The classical/asymptotic spectral action and phenomenological gravitational corrections are not yet a family-level quantum-gravity completion certificate.

## T2-03 — Twistor/amplitude programs

**Disposition:** `REDUCED_TO_TIER1_WITH_EXPLICIT_MAP` unless an independent parent is declared.

Adamo, arXiv:1308.2820, reviews twistor actions whose perturbation theory reproduces gauge/gravity amplitudes; the gravity construction uses an on-shell equivalence to recover Einstein gravity and yields an Einstein twistor action/MHV representation. Adamo & Mason, arXiv:1203.1026, obtain Einstein supergravity tree amplitudes from twistor-string constructions.

Therefore the label `twistor` alone is a representation/calculational architecture. Its physical result must be attributed to the corresponding Einstein, conformal/higher-derivative, string/supergravity or other explicit parent already covered in Tier-1. A future twistor model with genuinely independent dynamics is promoted separately.

This classification gives **zero exclusion evidence**.

## T2-04 — Canonical Wheeler-DeWitt geometrodynamics

**Disposition:** `PROMOTED_TO_TIER1` as `CANONICAL_WDW_GEOMETRODYNAMICS`.

The Wheeler-DeWitt programme is a materially distinct canonical quantization route for metric general relativity and cannot be silently identified with the LQG/spinfoam row. At the same time, the general framework does not supply one unique closed physical observable package: the probability/inner-product and problem-of-time issues remain realization/interpretation dependent. Kaya, arXiv:2211.11826, explicitly frames these as unresolved core issues and studies a relational embedding-field construction as one route.

First-pass classification:

`BLOCKED_MISSING_REQUIRED_OBJECT`.

Exact blocker:

`WDW_PHYSICAL_HILBERT_SPACE_CLOCK_OBSERVABLE_SEMICLASSICAL_GR_COMPARATOR_CERTIFICATE`.

Required payload: `{Hamiltonian/constraint realization, physical inner product, relational clock choice, anomaly/constraint closure, normalized Dirac observable, semiclassical GR map, state/ordering error ledger, same-domain comparator}`.

## T2-05 — Emergent / induced / graph-based gravity

**Disposition:** `SPLIT_CONCRETE_PARENT_PROMOTION_RULE`; concrete **Quantum Graphity** is promoted to Tier-1 as `QUANTUM_GRAPHITY`.

The old watchlist label was not one physical theory. Generic words such as emergent, induced or graph-based cannot receive either PASS or FAIL. The census rule is therefore: every concrete proposal with an explicit independent quantum parent, a gravity/emergence claim and materially distinct observables must be promoted and tested; purely effective mechanisms remain in their actual Tier-1 comparator family.

Quantum Graphity meets the promotion threshold because it has an explicit background-independent dynamical graph Hamiltonian and a claimed geometrogenesis mechanism. Konopka, Markopoulou & Severini, arXiv:0801.0861, give evidence for a low-energy ordered, low-dimensional, local phase. Wilkinson & Greentree, arXiv:1506.07588, show that the original Hamiltonian tends to favour disconnected subgraphs and introduce a hypervalence modification to obtain connected lattice-like graphs. Thus there is already both positive emergence evidence and a concrete negative model-selection control.

First-pass classification:

`PARTIAL_SUBFAMILY_ONLY__EMERGENT_LOCALITY_CONTROL`.

Exact blocker:

`QUANTUM_GRAPHITY_CONTINUUM_LORENTZIAN_GRAVITY_PLUS_NORMALIZED_OBSERVABLE_COMPARATOR_CERTIFICATE`.

The residual generic catch-all label is not treated as an untested theory and contributes no exclusion evidence. New concrete independent emergent parents trigger Tier-1 promotion by rule.

## Revised census consequence

Tier-1 increases from **11 to 14** rows by adding:

- `NONCOMMUTATIVE_SPECTRAL_GEOMETRY`;
- `CANONICAL_WDW_GEOMETRODYNAMICS`;
- `QUANTUM_GRAPHITY`.

The original five-entry Tier-2 classification watchlist becomes **0 unresolved** after explicit dispositions. This closes only the *classification watchlist*, not D2A: the promoted Tier-1 rows are nonterminal and must themselves be closed before D7.

## D7 safety

No Tier-2 resolution in this audit counts as evidence that a theory is wrong. Reduction means the physical result is judged under the mapped Tier-1 parent. Promotion means the new row increases the D7 burden. Category splitting means generic labels cannot be used to hide untested concrete parents.
