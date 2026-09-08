# KMQGB Wave 26 — Cross-Representation Rigidity

**Frozen denominator:** 5 methodology targets.  
**Status:** terminal 5/5.  
**Purpose:** require one parent parameter set to predict multiple physical representations of the same dynamics instead of allowing independent retuning per representation.

| # | Target | Terminal result |
|---|---|---|
| T26-01 | shared-vs-local parameter incidence across representations | `PASS_RQIR_GATE` |
| T26-02 | cross-representation rank-gain metric `R_XR` | `PASS_RQIR_GATE` |
| T26-03 | full stacked covariance / correlated representation treatment | `PASS_RQIR_GATE` |
| T26-04 | representation-map completeness / fail-closed missing map | `PASS_RQIR_GATE` |
| T26-05 | representation-level prospective holdout | `PASS_RQIR_GATE` |

## Core rank relation

For one shared parent parameter block `theta` and representation-local nuisance blocks `phi_a`, build the honest shared tangent `J_shared` and the diagnostic independently-retuned tangent `J_sep`.

Define

`R_XR = rank(J_sep) - rank(J_shared) >= 0`.

`R_XR>0` measures extra consistency directions created solely by forcing the same parent dynamics to work across representations.

Use the full stacked covariance and ordinary COR geometry on the combined physical vector.

## Intended representation stack

Potential future blocks include

- in-out four-graviton scattering/helicity amplitudes;
- in-in/CTP retarded/symmetric/ordered kernels;
- relational/quantum-channel/tidal observables;
- soft/universality anchors.

This stacking is not KG novelty by itself. Full C5, string-like, asymptotic-safety and other comparators must be given the same shared-parameter treatment wherever their representations are defined.

## Executable reference

`code/cross_representation_rigidity_reference.py`.

Authoritative protocol: `protocol/CROSS_REPRESENTATION_RIGIDITY.md`.

No KG ansatz is promoted.