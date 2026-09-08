# T4-01 Audit — non-Gaussian stochastic gravity / higher-correlation comparator

Benchmark ID: `KMQGB-T4-M01-NONGAUSSIAN-STOCHASTIC`  
Concrete realization ID: `NGSG-MINK-SCALAR-HIGHER-MOMENTS-001`  
Role: adversary for the Candidate Gravity idea that `K3,K4,...` higher metric/force cumulants certify a quantum gravitational mediator  
State: **TERMINAL — `PASS_RQIR_GATE`**  
Objective: **`HIGHER_SYMMETRIZED_CUMULANTS_NOT_UNIQUE`**

## Terminal question

Does observing non-Gaussian gravitational noise / connected higher cumulants beyond the Einstein–Langevin two-point noise kernel establish a quantum gravitational mediator?

**No.**

Published non-Gaussian stochastic-gravity constructions explicitly extend a classical stochastic source so that its probability distribution incorporates higher moments of the quantum stress-energy fluctuations. The broader stochastic-gravity correlation-hierarchy program likewise treats second and higher stress-tensor correlations as progressively richer stochastic/correlation-noise inputs while the metric description can remain stochastic-classical.

Therefore

`K3_plus != 0`

is not by itself a comparator-resistant Candidate Gravity signature.

## Frozen realization

Use the Bates non-Gaussian stochastic-gravity construction for a free quantum scalar field in Minkowski spacetime as the concrete control.

Core properties:

- the source is a classical random stress/energy-density fluctuation field;
- its distribution is non-Gaussian;
- higher moments of quantum stress-tensor fluctuations are incorporated consistently in the stochastic construction;
- realizations are constructed using the Wightman-function data of the underlying quantum matter field;
- the resulting Minkowski energy-density fluctuation distribution is strongly non-Gaussian and approximately shifted-Gamma-like in the analyzed example.

This is a **classical stochastic metric/source comparator fed by quantum-matter statistics**, not a quantum metric operator algebra.

## Frozen observable hierarchy

Let a smeared gravity-sensitive observable be `X` and define connected cumulants

`K_n = <X^n>_c`.

The adversarial vector is

`I_NG={K2,K3,K4,..., ordering label, commutator/nested-commutator sector}`.

The critical distinction is between

1. **classical/symmetrized probability hierarchy** — moments/cumulants that can be represented by a positive classical random variable/process in the declared domain;
2. **ordered quantum hierarchy** — Wightman ordering, commutators, nested commutators, out-of-time/causal orderings and other information not encoded by one commuting probability distribution.

T4-01 establishes that the first hierarchy alone is insufficient.

## Relation to standard Gaussian C2

Standard Einstein–Langevin stochastic gravity uses a Gaussian stochastic tensor with covariance equal to the noise kernel, so connected cumulants above second order vanish in that **lowest Gaussian representation**.

That zero is an approximation property, not a fundamental classical-gravity theorem.

Bates supplies the counterexample: a non-Gaussian stochastic source can have nonzero higher cumulants while spacetime remains represented stochastically/classically.

Thus a KG proposal cannot defeat stochastic gravity merely by showing

`K3 != 0` or `K4 != 3 K2^2`.

## What the comparator does not automatically reproduce

The non-Gaussian stochastic construction does not thereby establish equivalence to the **full ordered quantum correlation hierarchy**.

A single classical stochastic probability distribution has commuting random variables. It does not by itself encode an independent operator commutator/nested-commutator algebra.

This leaves the T3-03 direction

`{A_comm/rho_comm, non-EB channel, ordered response}`

meaningfully stronger than `K3_plus` alone.

Important scope caveat: higher-point quantum correlations are mathematically subtler than simply assigning a positive stochastic measure. Correlation-noise/hierarchy methods do not imply that every ordered quantum correlator has a classical stochastic representation.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 comparator dynamics | PASS_SCOPED | explicit non-Gaussian stochastic construction exists |
| F1 mean/low-order limit | PASS_SCOPED | reduces to ordinary stochastic hierarchy at lower moments |
| F2 consistency | PASS_SCOPED | positive stochastic probability construction in the declared example; not a universal curved-spacetime theorem |
| F3 observable hierarchy | PASS | higher moments/cumulants explicit |
| F4 comparator attack | **PASS_RQIR_GATE** | nonzero higher cumulants can occur with classical stochastic gravity |
| F5 quantum-order distinction | OPEN_FOR_FUTURE_KG | ordered/commutator hierarchy not collapsed by this comparator result |
| F6/F7 | N/A | methodological comparator target |

## Terminal status

`PASS_RQIR_GATE`

objective:

`HIGHER_SYMMETRIZED_CUMULANTS_NOT_UNIQUE`.

## Candidate Gravity design lesson

Permanent rule:

> **Non-Gaussianity is not quantumness.** Higher symmetrized cumulants should be used to overconstrain a model, but they should not be the primary quantum-gravity witness.

The stronger KG target should mix both sectors:

`I_ordered={N_sym,K3_sym,K4_sym,...,rho_comm,nested_commutators,Q_channel}`.

The intended rigidity comes from requiring one parent dynamics to predict **both** the classical-looking probability hierarchy and the noncommuting/ordered hierarchy consistently.

This is directly analogous to T3-01: a feature becomes powerful only when an independently motivated extra condition collapses the comparator freedom.

## Reopen/extension condition

Future waves may test whether generalized non-Gaussian stochastic or nonlocal classical-CQ models can mimic a particular **ordered** detector statistic. That is a stronger adversary than the present higher-moment result.

## Terminal completion

**100% — terminal methodological PASS.**

## Sources

1. J. D. Bates, *Non-Gaussian Stochastic Gravity*, arXiv:1305.3755 (2013).
2. B. L. Hu & E. Verdaguer, stochastic-gravity reviews / correlation hierarchy.
3. N. G. Phillips & B. L. Hu, Phys. Rev. D 63, 104001 (2001), noise kernel and extension toward higher correlations.
4. B. L. Hu, correlation-hierarchy/non-Gaussian stochastic-gravity perspective (2017).
