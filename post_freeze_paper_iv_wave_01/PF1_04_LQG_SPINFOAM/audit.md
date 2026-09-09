# PF1-04 — LQG / Spinfoam / Covariant Discrete Gravity under RQIR Core v1.0

**RQIR core:** `v1.0 FROZEN`  
**Terminal status:** `BLOCKED_MISSING_REQUIRED_OBJECT` with upgraded 2026 positive controls.

## 1. Anti-stale rule

This regression explicitly rejects an obsolete shortcut:

> “spinfoam/LQG has infinitely many triangulation choices, therefore it automatically fails finite-freedom/continuum requirements.”

Fresh 2026 work makes that claim too strong.

## 2. UV/continuum positive control

Muxin Han, *Ultraviolet Fixed Point in Covariant Loop Quantum Gravity*, arXiv:2602.18665, studies the complete Lorentzian covariant-LQG amplitude summed over 2-complexes using spinfoam stacks. The paper identifies a candidate small-spin UV fixed point and reports that, at the fixed point, the complete amplitude reduces at leading order to a topological theory while the infinite triangulation ambiguity reduces to a **finite set of boundary coefficients** associated with a finite boundary-block basis.

For RQIR this changes the benchmark materially:

- infinite triangulation freedom is no longer an admissible generic blocker for this construction;
- finite boundary data / candidate continuum organization receives a genuine positive-control status;
- novelty still cannot be inferred from finiteness alone.

## 3. Lorentzian causal-vertex positive control

Bianchi, Chen & Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162, introduce causal data at the spinfoam-vertex level. In the large-spin limit the construction selects Lorentzian Regge geometries compatible with those causal data and yields a single exponential `exp(+ i S_Regge / hbar)` rather than the usual phase ambiguity, giving a scoped causal rigidity result.

Thus another old shortcut is forbidden:

> “spinfoam has no controlled causal phase selection.”

At least at the vertex/large-spin level, a concrete causal selection mechanism now exists.

## 4. Frozen RQIR adapter

The correct adapter chain for a terminal Paper-IV claim must be

`spinfoam sum / UV fixed-point boundary data`

`-> continuum state/observable with regulator-independent normalization`

`-> Lorentzian relational, detector or asymptotic observable`

`-> same-domain GR/EFT and other QG comparator`

`-> covariance/nuisance/holdout where applicable`

`-> robust residual or scoped identity`.

The 2026 positive controls materially strengthen the first half of this chain but do not yet close the entire chain for the benchmark object we require.

## 5. Remaining blocker

A terminal beyond-comparator RQIR residual still requires a single compatible construction providing

1. continuum-limit authority for the chosen observable, not only formal amplitude organization;
2. physical Lorentzian state/boundary semantics;
3. absolute normalization;
4. relational/detector/asymptotic observable mapping;
5. same-domain GR/EFT/comparator completion;
6. regulator/triangulation stability for that observable;
7. a robust nonzero residual or a precise scoped comparator identity.

The audited 2026 fixed-point and causal-vertex results do not by themselves supply this full end-to-end observable package.

Classification:

`BLOCKED_MISSING_REQUIRED_OBJECT__CONTINUUM_NORMALIZED_LORENTZIAN_OBSERVABLE_COMPARATOR_PACKAGE`

## 6. What is positively closed

The following are now recorded as positive controls rather than blockers:

- candidate mechanism reducing infinite triangulation ambiguity to finite boundary data;
- candidate fundamental continuum organization via spinfoam-stack UV fixed point;
- causal local vertex with compatible Lorentzian Regge selection;
- single-phase large-spin asymptotics in the causal construction.

These upgrades strengthen LQG as a comparator and make the remaining RQIR request sharper.

## 7. Core-defect test

No RQIR Core defect. Spinfoam boundary/vertex objects can be represented through adapters into existing relational/transition/causal observable slots. The present difficulty is completion/normalization of the chosen physical observable, not an inability of Core v1.0 to express it.

No version change requested.

## 8. Paper-IV meaning

Terminal benchmark status for this declared scope remains `BLOCKED_MISSING_REQUIRED_OBJECT`.

This is **not** evidence for `NEW_REQUIRED` and is **not** a claim that LQG/spinfoam is inconsistent or scientifically exhausted.

Reopen immediately when one compatible construction closes the continuum-normalized Lorentzian observable/comparator chain above.