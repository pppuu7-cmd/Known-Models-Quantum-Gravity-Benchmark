# Canonical Wheeler-DeWitt geometrodynamics — first-pass closure audit (Iter216)

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `CANONICAL_WDW_GEOMETRODYNAMICS`  
**Gate:** `CANONICAL_WDW_PHYSICAL_HILBERT_SPACE_CLOCK_OBSERVABLE_SEMICLASSICAL_GR_COMPARATOR`

## Question

Does metric/canonical Wheeler-DeWitt geometrodynamics currently supply a fixed full-theory 3+1 quantum realization with all of:

`well-defined quantum constraints -> anomaly/constraint closure -> positive physical inner product -> relational clock -> normalized Dirac/relational observable -> semiclassical GR map -> same-domain comparator -> factor-ordering/state/approximation error ledger`?

## Scope guard

This audit distinguishes **full metric geometrodynamics** from loop-connection quantizations and from minisuperspace. A result in LQG or a finite cosmological truncation is retained as contextual/scoped evidence but cannot be promoted to full Wheeler-DeWitt metric-geometrodynamics closure without an explicit reduction/equivalence map.

## A. Formal full-theory WDW structure

Canonical metric quantization gives the Hamiltonian and momentum constraints, with the Wheeler-DeWitt equation carrying the dynamical content and the momentum constraints implementing spatial diffeomorphism invariance. The semiclassical Born-Oppenheimer/WKB expansion can recover an approximate functional Schrödinger equation for matter on a classical gravitational background and organize quantum-gravitational corrections.

This remains a strong structural and semiclassical control.

Classification:

`PASS_SCOPED_FORMAL_CONSTRAINT_AND_SEMICLASSICAL_GR_STRUCTURE`.

## B. Full-theory operator/constraint blocker

The modern quantum-geometrodynamics literature continues to stress that the metric Wheeler-DeWitt functional operator requires a mathematically controlled definition of coincident functional derivatives, regularization/renormalization and factor ordering. Without that control, a full anomaly-free quantum constraint algebra cannot simply be assumed.

Therefore the existence of the formal WDW equation is not enough to satisfy the RQIR `fixed realization` and `constraint closure` links.

Classification:

`BLOCKED_FULL_METRIC_WDW_REGULATOR_ORDERING_AND_CONSTRAINT_CLOSURE`.

## C. Physical inner product — genuine progress but scoped

A 2026 JHEP treatment clarifies canonical gravitational Hilbert spaces and shows how group averaging / BRST-BFV can construct physical inner products and relate apparently different gauge-fixed prescriptions. This materially narrows the old blanket statement that a physical inner product is conceptually unavailable.

However the paper deliberately uses one-dimensional/minisuperspace-type models as its simplest controlled setting for the detailed construction. It does not by itself provide a complete nonperturbative physical Hilbert space for the full metric 3+1 Wheeler-DeWitt theory together with all local constraints and physical observables.

Classification:

`PASS_SCOPED_GROUP_AVERAGING_BRST_PHYSICAL_INNER_PRODUCT__BLOCKED_FULL_3PLUS1_IMPLEMENTATION`.

## D. Relational time / clock

Relational and Page-Wootters-type constructions demonstrate consistent clock-conditioned dynamics in constrained systems and multiple quantum-cosmology models. These are real solutions of the time problem in declared reduced domains.

They do not select a unique globally valid clock for arbitrary full 3+1 superspace, and different clock choices can have limited patches or inequivalent practical domains. Thus a full-theory clock/observable package remains realization-dependent.

Classification:

`PASS_SCOPED_RELATIONAL_CLOCK_DYNAMICS__NO_UNIVERSAL_FULL_SUPERSPACE_CLOCK_CERTIFICATE`.

## E. Positive physical-observable controls

Several restricted Wheeler-DeWitt sectors now have substantially stronger Hilbert/observable structure than older summaries suggest:

- large-volume asymptotically de Sitter WDW solutions can be organized into a proposed Hilbert-space basis;
- minisuperspace models admit explicitly normalized wave packets, relational observables and positive inner products under declared prescriptions;
- recent flat-minisuperspace work can make a class of path-integral-consistent factor orderings physically equivalent.

These are retained as positive controls. Their scope is not full arbitrary 3+1 metric geometrodynamics.

## F. Comparator and error closure

The semiclassical WKB expansion provides a principled GR/Schrödinger recovery map, but a family-level RQIR residual would require one fixed quantum realization whose observable is transported through that map with:

- regulator/factor-ordering ancestry;
- state/boundary-condition dependence;
- clock dependence;
- approximation/WKB remainder;
- normalized identical-domain GR comparator.

No audited full-theory object was located that closes those items simultaneously.

## First-pass family result

The old shorthand `WDW has no physical Hilbert space or relational dynamics` is too strong. Modern group-averaging/BRST work and quantum-cosmology constructions provide genuine scoped progress.

The correct current school-level blocker is narrower:

`BLOCKED_WDW_NO_LOCATED_FIXED_FULL_3PLUS1_METRIC_REALIZATION_WITH_REGULATED_ANOMALY_CLOSED_CONSTRAINTS_POSITIVE_PHYSICAL_HILBERT_RELATIONAL_OBSERVABLE_AND_GR_COMPARATOR_ERROR_CHAIN`.

This is **not a scientific FAIL** of canonical geometrodynamics.

## Paper-III impact

No new general resource-closure class appears. Again the decisive issue is completion of one realization and its nuisance/normalization/provenance/error chain rather than a defect in frozen RQIR Core.

`PAPER_III_REOPEN = NO`.

## Heavy compute

`IDLE`.

The decisive blocker is analytic/definitional, not numerical. Computing additional minisuperspace wavefunctions cannot establish full-theory constraint closure or a physical Hilbert space.

## Next WDW gate

Advance to a bounded full-theory authority search:

`WDW_FULL_3PLUS1_REGULATED_CONSTRAINT_ALGEBRA_PHYSICAL_INNER_PRODUCT_AUTHORITY_SEARCH`.

The search must target metric/geometrodynamic (not merely loop) constructions that simultaneously give a controlled Hamiltonian constraint operator, regulator removal or renormalized definition, anomaly/closure statement and a physical inner product. If no such same-realization construction is located, park WDW on that precise missing certificate and advance to Quantum Graphity.
