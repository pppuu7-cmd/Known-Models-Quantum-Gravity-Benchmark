# Candidate Gravity Promotion Gate

**Purpose:** one-page authority checklist for deciding when benchmark/design work is mature enough to promote a concrete Candidate Gravity ansatz.  
**Status:** methodology only; no current ansatz is promoted.

A future Candidate Gravity proposal must pass the following order. Skipping/reordering a gate is not authorized.

## Gate 0 — one explicit parent dynamics

Provide one action, Hamiltonian/master equation, Schwinger-Keldysh/CTP functional, influence functional, or equivalent parent object.

All source, noise, response, contact and higher-order quantities used in the claim must be derivatives/projections of this same parent object or be explicitly identified external detector/source components.

## Gate 1 — same-parent response completeness

At every response order used in the observable, generate the complete parent response.

For `G=K^-1`, use the ordered-partition identity in `protocol/PARENT_KERNEL_RESPONSE_COMPLETENESS.md`.

No selected diagram/contact subset may be called the complete response without an explicit zero/origin proof for all omitted ordered-partition families.

## Gate 2 — exact physical constraints first

Close all applicable

- gauge/Ward identities;
- contact/seagull completion;
- Bianchi/conservation constraints;
- nonlinear Hamiltonian/momentum constraints where relevant;
- physical DOF/gauge reduction;
- exact routing/signature/convention matching.

Only then define the physical observable basis.

## Gate 3 — common-domain comparator definition

Freeze the same observable, source/detector routing, perturbative order, state sector and validity domain for Candidate Gravity and every applicable comparator.

No UV-vs-IR domain cheating. No missing contact/crossed pieces on either side.

## Gate 4 — full attribution stack

The candidate observable must survive, where relevant:

1. quantum attribution;
2. mediator attribution;
3. gravity / massless-spin-2 attribution;
4. locality/microcausality attribution;
5. relational/QRF attribution;
6. geometry attribution for causal/process claims;
7. detector/backaction attribution;
8. regulator/continuum attribution;
9. state-sector attribution.

## Gate 5 — full comparator / full-C5 matching

Use

`Gamma_parent = Gamma_C5,full_matched + DeltaGamma_KG`

only as a bookkeeping definition after the largest applicable same-order C5 nonlinear/loop/EFT/state/contact structure has been matched.

Profile C0-C6/C3b and stronger benchmark-discovered comparator classes in the same domain.

A qualitative label such as higher-point, squeezed, memory, chiral, nonanalytic, nonlocal or entangling is never `DeltaGamma_KG` by itself.

## Gate 6 — comparator-orthogonal residual

After exact constraints and nuisance blocks are frozen, compute the local Comparator-Orthogonal Residual using `protocol/RESIDUAL_SPACE_GEOMETRY.md`:

`A=Sigma^(-1/2)J_union`,

`COR=(I-AA^+)Sigma^(-1/2)r`.

If `COR=0`, the candidate is locally absorbed and is not promotable in that observable set.

A nonzero COR is only a local prefilter.

## Gate 7 — global/nonlinear separation

Perform finite parameter/state/detector/comparator profiling over the full prospective common domain.

The residual must remain bounded away from the comparator manifold under the pre-registered robustness tolerance.

## Gate 8 — observable design / identifiability

Use `protocol/OPTIMAL_COMPARATOR_CONTRASTS.md`.

For future KG Jacobian `J_KG`, evaluate

`B_KG=Pi_perp Sigma^(-1/2)J_KG`.

Require at least one robust nonzero singular direction after global profiling.

Prefer observable additions satisfying

`Delta d_perp = k - Delta rank(J_union) > 0`

or materially increasing the weakest projected singular value / projected SNR.

## Gate 9 — rigidity

Count remaining free functions/parameters after all consistency and comparator constraints.

The novelty claim should be a forced cross-order/cross-attribution relation from the parent dynamics, not a collection of independently tunable effects.

## Gate 10 — promotion and downstream statistics

Only after Gates 0-9 may a Candidate Gravity ansatz be **promoted** for model-level readiness accounting.

Only after a robust nonzero comparator-subtracted algebraic residual exists may Fisher/identifiability/resource calculations be promoted.

## Current verdict

As of KMQGB Iteration 033:

- no Candidate Gravity ansatz is promoted;
- globally authorized robust unique-QG residuals remain `0`;
- this document is a construction/promotion methodology, not evidence for new physics.
