# KMQGB Ninth Wave — Optimal Comparator-Annihilating Observable Design

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–8:** terminal and immutable.  
**Status:** **TERMINAL 5/5 = 100%**.  
**Purpose:** turn residual-space geometry into constructive observable/contrast design for future Candidate Gravity tests.

| # | Target | Terminal result | State |
|---|---|---|---|
| T9-01 | exact left-nullspace contrasts | comparator-null observables are exactly the left nullspace `J_union^T w=0` after physical constraints | `PASS_RQIR_GATE` |
| T9-02 | covariance-optimal contrast | `w_opt` maximizing local post-comparator SNR is frozen in the full covariance metric | `PASS_RQIR_GATE` |
| T9-03 | observable augmentation rank gain | exact rule `Delta d_perp = k - Delta rank(J_union)` is frozen | `PASS_RQIR_GATE` |
| T9-04 | correlated/common-mode rejection | correlated stochastic covariance and deterministic nuisance directions are separated and jointly quotiented without diagonal-error assumptions | `PASS_RQIR_GATE` |
| T9-05 | projected experimental-design criterion | future configurations are selected by projected rank/singular values or projected signal SNR, not raw sensitivity alone | `PASS_RQIR_GATE` |

**Ninth-wave terminal coverage: 5/5 = 100%.**

## Authoritative protocol

`protocol/OPTIMAL_COMPARATOR_CONTRASTS.md`

Reference implementation:

`code/optimal_comparator_contrasts_reference.py`

## Core formulas

For physical observable vector `y`, covariance `Sigma`, and union comparator Jacobian `J_C`, an exact local comparator-null contrast

`X_w=w^T y`

satisfies

`J_C^T w=0`.

For a pre-registered candidate signal `s`, with symmetric inverse square root `Sigma^(-1/2)`, define

`A=Sigma^(-1/2)J_C`,

`Pi_perp=I-AA^+`.

A covariance-optimal unit-variance contrast has direction

`w_opt proportional to Sigma^(-1/2) Pi_perp Sigma^(-1/2) s`,

and

`SNR_max=||Pi_perp Sigma^(-1/2)s||`.

If `SNR_max=0`, the proposed signal is locally absorbed by the union comparator tangent.

## Exact observable-augmentation rule

If `k` additional physical observables are added after Ward/contact/constraint reduction, then

`Delta d_perp = k - Delta rank(J_union)`.

Thus a new channel increases local novelty dimension only if it increases the physical observable dimension more than it increases the allowed comparator/nuisance tangent rank.

This is now a mandatory design rule for future Candidate Gravity observables.

## Correlated/common-mode guardrail

- stochastic correlated noise belongs in `Sigma`;
- deterministic/calibratable common-mode freedom belongs in `J_union`;
- singular covariance is treated on its supported subspace with a pseudoinverse square root;
- exact constraints are imposed before covariance/comparator profiling;
- no diagonal-covariance assumption is authorized unless derived.

## Future KG design criterion

For a future KG Jacobian `J_KG`, define

`B_KG=Pi_perp Sigma^(-1/2)J_KG`.

The useful design directions are the robust nonzero singular directions of `B_KG`.

A source/detector configuration should therefore be chosen to maximize, prospectively,

1. comparator-orthogonal rank;
2. the weakest robust nonzero projected singular value;
3. or, for a pre-registered single signal, projected SNR.

Raw sensitivity to a signal before comparator profiling is not the optimization target.

## Candidate Gravity consequence

Future KG model building must co-design dynamics and observables. An observable is preferred when

`Delta m_phys > Delta rank(J_union)`

or when it materially improves projected conditioning/SNR.

This favors linked cross-order/cross-attribution measurements whose comparator freedoms are already constrained by the same parent dynamics.

## Promotion guardrail

This wave is methodology only. No Candidate Gravity ansatz is promoted and external Candidate Gravity readiness is unchanged.
