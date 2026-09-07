# Model Audit — semiclassical Einstein gravity, scalar-field Minkowski linear-response realization

Benchmark ID: KMQGB-M03-SEMICLASSICAL
Concrete realization ID: SCG-MINK-SCALAR-LR-001
Role: source/backreaction control (C1)
State: ACTIVE / NONTERMINAL

## Declared realization

Four-dimensional classical metric `g_ab` coupled to a quantized free real scalar field through the renormalized expectation value of its stress tensor. The semiclassical equation is taken in the standard renormalized form

`G_ab[g] + Lambda g_ab - 2(alpha A_ab + beta B_ab)[g] = 8 pi G <T_ab^R[g]>`

with the matter field in the Minkowski vacuum for the flat-background linear-response control. `A_ab` and `B_ab` denote the conserved local curvature-counterterm tensors of the renormalized semiclassical theory.

This is a concrete low-curvature/linear-response control, not a claim about every semiclassical-gravity solution, cosmology or black-hole backreaction problem.

## Why this realization was selected

The RQIR comparator registry defines C1 as semiclassical gravity with representative structure `G_mn = 8 pi G <T_mn>` or an appropriate controlled semiclassical EFT formulation. The prior RQIR landscape audit classifies semiclassical mean gravity as a valid C1 baseline whose mean source `J` is central but which, as a mean-only closure, does not by itself supply an independent fundamental quantum-gravitational noise/operator hierarchy.

The Hu–Verdaguer Living Reviews treatment gives the explicit renormalized semiclassical Einstein equation including curvature counterterms and states that a solution consists of the metric, quantum field and physically acceptable state satisfying that equation. Anderson, Molina-París and Mottola analyze a free scalar field of arbitrary mass/curvature coupling in the Minkowski vacuum and formulate a gauge-invariant linear-response stability criterion for validity of the semiclassical approximation.

## Initial gate map

| Field | Current evidence | KMQGB state |
|---|---|---|
| Dynamics | renormalized semiclassical Einstein equation with classical metric and quantum-matter expectation source | F0 structurally supported |
| Required classical limit | setting quantum backreaction/counterterm corrections appropriately recovers classical Einstein dynamics | requires exact declared coupling/scheme statement before closure |
| Conservation/Bianchi | renormalized equation uses conserved geometric counterterm tensors and a covariantly compatible renormalized source | structurally supported |
| Causality/linear response | flat-space validity can be tested by gauge-invariant linear response; published Minkowski analysis exists | supported for chosen control domain |
| Source hierarchy | fundamental semiclassical metric source is the mean `J=<T>` | exact C1 feature |
| Independent metric noise | absent from mean semiclassical equation; stochastic extension adds noise kernel and is benchmarked separately as M04 | expected F3 limitation, not inconsistency |
| Q1–Q7 mapping | strongest direct relevance is Q3 backreaction/source rule; Q5 fluctuations expose the boundary toward stochastic gravity | PARTIAL |
| Comparator | C1 semiclassical gravity | likely identity at declared theory-class level; exact scope mapping still to freeze |
| Terminal status | not yet assigned | ACTIVE |

## Critical distinction

A mean-only semiclassical realization may be perfectly valid within its regime while still being insufficient to establish a quantum gravitational interface. The benchmark must therefore distinguish:

1. consistency of the semiclassical equation in its domain;
2. exact/operational identity with C1;
3. inability of mean-only closure to provide independent quantum metric noise/operator hierarchy;
4. any actual inconsistency, which would require a separate gate-level proof.

No general theory FAIL is allowed from item 3.

## Current first blocker

`SCG_REALIZATION_FREEZE`: pin the exact scalar-field mass/coupling choice, state, renormalization prescription/counterterm convention and the precise linear-response observable domain before assigning a terminal comparator relation.

This is a realization-definition blocker, not evidence against semiclassical gravity.

## Sources

1. B. L. Hu and E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Reviews in Relativity 11, 3 (2008), especially the semiclassical Einstein equation and its renormalization: https://link.springer.com/article/10.12942/lrr-2008-3
2. P. R. Anderson, C. Molina-París and E. Mottola, *Linear Response, Validity of Semi-Classical Gravity, and the Stability of Flat Space*, arXiv:gr-qc/0209075: https://arxiv.org/abs/gr-qc/0209075
3. RQIR prior landscape authority: external `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.

## Next action

Freeze one exact scalar-field/counterterm realization from the cited authority, map it literally to C1 and F0–F7, then decide whether the correct terminal KMQGB state is exact comparator identity, operational degeneracy, or a scoped blocker.
