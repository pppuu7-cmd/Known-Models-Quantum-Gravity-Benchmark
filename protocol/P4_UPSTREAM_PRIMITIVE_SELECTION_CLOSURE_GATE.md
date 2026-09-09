# P4 Upstream Primitive Selection / Closure Gate

**Status:** permanent fail-closed parent-origin rule.  
**KMQGB iteration:** 142.  
**Purpose:** prevent a conditionally unique downstream generator from being mistaken for a complete parent when arbitrary dynamics remain hidden in its inputs.

## 1. General structure

Many strong KMQGB positive controls have the form

`X -> G[X] -> predicted hierarchy`,

where `G` is highly rigid once an upstream primitive `X` is supplied.

Examples include

- matter action -> constructive-gravity closure -> gravitational action;
- observable algebra + state -> modular automorphism flow;
- spectral triple -> geometry / spectral action;
- operator-valued measure -> causal-action minimization;
- covariant operator + state/contour -> `Tr log` all-point loop vertices;
- wave operator + causal boundary condition -> non-rational spectral function.

The downstream map may be unique even when the upstream primitive is not physically selected.

## 2. Parent-closure principle

For every upstream primitive `X_i` needed to evaluate the candidate, the record must declare

1. what `X_i` is;
2. whether it is **derived**, **external input**, or **blocked/unselected**;
3. the finite physical law that selects it if derived;
4. evidence for that selection;
5. its finite-cutoff functional/parameter freedom;
6. whether any remaining freedom is shared globally or retuned per observable.

The chain is P4-closed only when every load-bearing primitive is derived from the same finite parent or is an explicitly fundamental finite constant already admitted by the parent rubric.

## 3. Fail-closed rule

A candidate may remain a valid research record with unresolved primitives. Such a record is scientifically `BLOCKED`, not malformed.

However

`G0 parent explicit = PASS`

or any P4/promotion claim is inconsistent if a load-bearing primitive is marked

- `EXTERNAL_INPUT`;
- `BLOCKED`;
- missing selection evidence;
- or has a growing/unresolved functional-freedom audit.

This applies even when all downstream equations are deterministic.

## 4. Conditional uniqueness is not parent uniqueness

Formally,

`for fixed X, G[X] unique`

does not imply

`G is a unique physical parent`

unless the admissible set of `X` is itself finite/selected.

If `X` ranges over an infinite-dimensional class, the downstream family

`{G[X] : X in X_admissible}`

inherits that upstream freedom even if the map `X -> G[X]` is one-to-one or deterministic.

This is the operator/state generalization of the earlier `FF_D` amplitude-level functional-freedom gate.

## 5. Primitive examples that must be audited

Depending on architecture, upstream primitives can include

- matter Lagrangian/potential/couplings;
- Hilbert space and algebra representation;
- spectral triple or Dirac operator;
- operator-valued measure and causal-action parameters;
- state/density matrix;
- Lorentzian integration contour/thimbles/Stokes constants;
- process matrix / quantum comb;
- boundary conditions;
- regulator/profile function and renormalization constants;
- zero/pole sequence or spectral measure;
- detector reference/calibration priors if they are part of the physical claim.

The list is not exhaustive.

## 6. Machine-record schema

`code/kg_candidate_record_validator.py` schema v1.2 implements this gate through mandatory

- `upstream_primitives`;
- `primitive_selection_law`;
- `primitive_freedom_audit`.

A v1.2 record can be structurally valid while scientifically blocked. But `G0 PASS` is rejected unless all load-bearing primitives are selection-closed and the primitive freedom audit is PASS.

## 7. Comparator consequence

This gate is especially important when a candidate resembles a known conditional generator. Before novelty is assessed, ask whether the apparent novelty is simply a new choice of upstream primitive within

- constructive gravity;
- modular/AQFT dynamics;
- spectral action/noncommutative geometry;
- causal fermion systems;
- induced gravity / `Tr log`;
- asymptotic safety;
- string/matrix/discrete boundary data.

A different input to an existing generator is not a new origin law unless the input is itself derived by new physics.

## 8. Score consequence

This is methodology/executable hardening, not a P4 survivor.

- R1 unchanged.
- R2 unchanged pending broader end-to-end executable closure.
- R3 unchanged.
- R4 remains 45%.
