# O-LQG EPRL/KKL continuum-topology escape gate — 2026-09-10

**KMQGB iteration:** 199  
**RQIR Core:** v1.0 FROZEN  
**Parent:** `LQG_SPINFOAM`  
**Status:** structural narrowing only; no family-level promotion.

## Question

Given the Iter198 EPRL/KKL candidate UV fixed point and the 2026 model-independent spin-foam continuum theorem, what additional structural condition must any same-realization UV→IR completion satisfy before KMQGB can accept it as a physical gravity crossover rather than a topological continuum endpoint?

## Primary authorities

1. Muxin Han, *Ultraviolet fixed point in covariant loop quantum gravity*, Phys. Rev. D 114, 044040 (published 12 August 2026), arXiv:2602.18665. The complete covariant-LQG stack amplitude built from Lorentzian EPRL/KKL amplitudes has a candidate small-spin UV fixed point. At leading order the fixed-point amplitude becomes topological and the microscopic triangulation ambiguity is compressed into a finite set of boundary coefficients; the construction carries an explicit leading `O(A^-1)` remainder.
2. Matteo Bruno, Eugenia Colafranceschi, Fabio M. Mele, Carlo Rovelli, *Structure of the continuum limit of spin foams*, Phys. Rev. D 114, 066005 (published 8 September 2026), arXiv:2603.16999. In a model-independent ordered-triangulation framework, sufficiently strong convergence assumptions force the spin-foam continuum theory to be topological. The paper then develops a weaker distributional continuum notion in which the cylinder amplitude defines a rigging map and physical states can be constructed without imposing that strong topological limit.

## New combined inference

The two results must not be naively identified: Han studies a concrete EPRL/KKL stack construction, whereas Bruno et al. prove a model-independent theorem under stated convergence assumptions. KMQGB therefore records only the following **conditional structural consequence**.

If the EPRL/KKL UV→IR refinement path is claimed to satisfy the strong-convergence hypotheses that trigger the Bruno–Colafranceschi–Mele–Rovelli theorem, then simply taking that strong continuum limit cannot by itself recover a non-topological GR-like propagating gravitational sector: the resulting limit is topological under those hypotheses.

Consequently an admissible same-realization crossover from Han's topological leading UV fixed point to a semiclassical Regge/GR sector must explicitly provide at least one of:

- a **distributional / rigging-map continuum realization** of the EPRL/KKL amplitudes, together with the relevant deformation that carries the system into the semiclassical gravitational regime; or
- an explicit proof that the concrete EPRL/KKL flow violates or evades at least one strong-convergence assumption of the no-go theorem, with the replacement convergence/control notion stated and an error/remainder bound supplied.

This is not evidence that EPRL/KKL fails. It is a topology-escape obligation on any proposed UV→IR bridge.

## Structural gate

**`PASS_STRUCTURAL_GATE__LQG_UV_TO_IR_BRIDGE_REQUIRES_EXPLICIT_TOPOLOGICAL_CONTINUUM_ESCAPE_MECHANISM`**

The pass refers only to the logical constraint just derived. It is not a PASS of LQG as a complete family-level physical object.

## Refined same-realization chain

The Iter198 chain

`EPRL/KKL gamma_micro -> UV fixed-point boundary data -> relevant deformation / IR crossover -> semiclassical Regge/Area-Regge -> area-metric comparator`

is refined to

`EPRL/KKL gamma_micro -> topological UV fixed-point boundary data -> {relevant deformation + continuum-topology escape} -> semiclassical Regge/Area-Regge gamma ancestry -> area-metric observable comparator`.

Here `continuum-topology escape` is not a free label. It must be one of:

1. `DISTRIBUTIONAL_RIGGING_MAP_CONTINUUM_WITH_FIXED_EPRL_KKL_REALIZATION`, or
2. `EXPLICIT_STRONG_CONVERGENCE_ASSUMPTION_ESCAPE_WITH_REPLACEMENT_CONTROL`.

## Certificate required for the next physical gate

A future family-closing object must contain all of:

1. exact Lorentzian EPRL/KKL realization and stack/refinement prescription;
2. UV fixed-point boundary coefficient normalization and the inherited `O(A^-1)` remainder;
3. relevant deformation(s) away from the topological UV fixed point;
4. explicit continuum-topology escape mechanism as defined above;
5. crossover map into the large-spin semiclassical regime;
6. Barbero–Immirzi normalization and transport through that crossover;
7. Regge → Area-Regge / area-metric coupling ancestry in the same realization;
8. normalized common-domain physical observable and GR/EFT/alternative-QG comparator set;
9. propagated UV asymptotic + refinement + crossover + truncation error ledger.

## RQIR disposition

`LQG_SPINFOAM` remains `BLOCKED_MISSING_REQUIRED_OBJECT`.

The family residual remains undefined; it is not zero-filled. `D2`, `D4`, and `D7` remain open. `NEW_REQUIRED` remains unauthorized. Candidate Gravity remains inactive at R3=24%.

## Refined next gate

**`EPRL_KKL_UV_FIXED_POINT_TO_SEMICLASSICAL_AREA_REGGE_CROSSOVER_WITH_TOPOLOGY_ESCAPE_GAMMA_ANCESTRY_AND_ERROR_CERTIFICATE`**

## Compute decision

Heavy compute remains `IDLE`. The missing object is first a well-defined same-realization flow/convergence prescription. Numerical scans cannot decide which no-go hypothesis is escaped or manufacture a relevant deformation without such an authority.