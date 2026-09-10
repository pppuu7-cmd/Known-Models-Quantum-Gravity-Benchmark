# Nonlocal QG Riemann/Weyl causality audit — Iter250

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `NONLOCAL_QG`

## Question
Can the materially distinct Riemann/Weyl weakly-nonlocal branch close the required full-momentum observable + causality + unitarity + error certificate, without importing results from the Ricci/scalar equivalence class?

## Primary authorities
1. Donà, Giaccari, Modesto, Rachwał & Zhu, *Scattering amplitudes in super-renormalizable gravity*, JHEP 08 (2015) 038, arXiv:1506.04589. Ricci/scalar weakly-nonlocal tree amplitudes can reduce to Einstein amplitudes under the field-redefinition theorem, whereas an independent Riemann form-factor sector can retain explicit form-factor dependence (with the stated dimensional/Gauss–Bonnet scope caveats).
2. Zhao, Modesto & Bambi, *Acausal exact vacuum solutions in nonlocal gravity*, Eur. Phys. J. C 86, 713 (2026), arXiv:2605.01413, DOI 10.1140/epjc/s10052-026-15963-y. The paper studies a special but large class of super-renormalizable/finite, unitary-compatible nonlocal form factors and proves that a subclass of Gödel-type metrics containing closed timelike curves is an exact vacuum solution. The authors explicitly state that renormalizability alone is insufficient to guarantee causal admissibility in vacuum and identify matter as the ingredient that may break the Minkowski/Gödel degeneracy.

## Result 1 — scoped causal obstruction exists
The 2026 peer-reviewed result supplies a genuine physical causality obstruction for a declared, special-but-large weakly-nonlocal form-factor subclass. This is stronger than a missing-object BLOCKED row: within that precise vacuum subclass, the causal-admissibility requirement is violated by exact solutions with closed timelike curves.

Scoped disposition:
`FAIL_SCOPED_CAUSALITY_GATE__WEAKLY_NONLOCAL_RIEMANN_RICCI_WEYL_FORM_FACTOR_SUBCLASS_ADMITS_EXACT_GODEL_TYPE_VACUA_WITH_CLOSED_TIMELIKE_CURVES`.

Scope discipline is mandatory. The authority does **not** establish that every Riemann/Weyl weakly-nonlocal action is acausal, so this result must not be promoted to `NONLOCAL_QG` family FAIL.

## Result 2 — unitarity/renormalizability does not close causality
The same authority explicitly frames the offending subclass as compatible with a well-defined quantum theory and with super-renormalizable/finite, unitarity-motivated form-factor constructions. Therefore the implication

`ghost-free/unitary/renormalizable => globally causal`

is rejected for this scoped subclass.

This prevents the benchmark from using pole/UV behavior alone as a causality surrogate.

## Result 3 — the viable branch now requires a degeneracy-evasion certificate
A surviving Riemann/Weyl candidate must show, in one fixed realization, how the exact-vacuum causal degeneracy is avoided or lifted, e.g. by a prospectively specified matter coupling or a form-factor/action restriction, while retaining the same realization's unitarity/UV properties and furnishing a normalized observable/comparator with propagated uncertainty.

The audited authority set does not yet provide the complete chain:

`fixed action/prescription -> no pathological exact causal-support sector in declared domain -> matter/interacting completion if required -> full-momentum physical observable -> common-domain GR/EFT comparator -> propagated theory/remainder error`.

Disposition:
`BLOCKED_MISSING_REQUIRED_OBJECT__NONLOCAL_RIEMANN_WEYL_CAUSALITY_SAFE_SAME_REALIZATION_WITH_MATTER_OR_DEGENERACY_EVASION_FULL_MOMENTUM_OBSERVABLE_UNITARITY_COMPARATOR_AND_PROPAGATED_ERROR`.

## Family consequence
`NONLOCAL_QG` remains `PARTIAL_SUBFAMILY_ONLY`; family residual remains `UNDEFINED`. The new scoped FAIL is not a family-level FAIL and cannot authorize `NEW_REQUIRED`.

D2 remains `NOT_CLOSED`; D4 remains `PARTIAL / globally NOT_CLOSED`; D7 remains `NOT_CLOSED` with decision `NOT_YET_AUTHORIZED`. Candidate Gravity remains inactive at R3=24%.

## Heavy compute
`IDLE`. The active obstruction is analytical/provenance/realization matching. Numerical work without a prospectively fixed surviving action and causal-domain certificate cannot change terminal classification.

## Exact next gate
`NONLOCAL_QG_RIEMANN_WEYL_RICCI_FLAT_OR_GODEL_DEGENERACY_EVASION_AND_MATTER_COUPLED_CAUSAL_COMPLETION_CERTIFICATE`.
