# P4 Nonlinear Moment-Recursion / Random-Matrix Positive Control

**Status:** exact A2 positive control / A3 comparator warning.  
**KMQGB iteration:** 126.  
**Purpose:** demonstrate that a finite nonlinear law can uniquely generate a continuous positive spectral measure, while separating this mathematical success from quantum-gravity novelty.

## 1. Catalan moment law

Take

`m_0 = 1`,

`m_(n+1) = sum_(k=0)^n m_k m_(n-k)`.

The unique sequence is the Catalan sequence

`1, 1, 2, 5, 14, 42, ...`.

Its ordinary generating function obeys the finite algebraic law

`M(z) = 1 + z M(z)^2`.

Thus an infinite moment tower is generated from a finite nonlinear rule with no independent coefficient at each order.

## 2. Continuous positive measure

The Catalan moments are the moments of the Marchenko-Pastur / free-Poisson law at unit parameter, a continuous positive measure with compact support on `[0,4]`.

Compact support makes the corresponding moment problem determinate: the full moment sequence fixes the measure uniquely.

Therefore this is an exact counterexample to the idea that

`finite rule -> only finite atomic spectrum`.

The atomic-collapse theorem of Iter125 applies specifically to finite **constant-coefficient linear** recurrences, not to nonlinear recurrences such as this one.

## 3. A2 classification

For the moment-selection problem alone,

`finite nonlinear recurrence + positivity + determinacy -> unique continuous spectral envelope`

is a genuine positive control.

Classification:

`A2 PASS_CONTROL__FINITE_NONLINEAR_LAW_CAN_FIX_CONTINUOUS_POSITIVE_SPECTRUM`.

## 4. A3 comparator containment

The same structure is canonical random-matrix/free-probability mathematics. Marchenko-Pastur is the limiting spectral law of Wishart/sample-covariance random matrices; Fuss-Catalan generalizations occur for products of random matrices and related structured ensembles.

KMQGB already treats matrix/random-matrix/JT/topological-recursion structures as strong comparators.

Therefore

`A3 FAIL_AS_NOVELTY_CERTIFICATE__RANDOM_MATRIX_FREE_PROBABILITY_CONTROL`.

The point is methodological: **nonlinear finite generation can solve functional freedom**, but a candidate must derive its recurrence from gravity-specific microscopic physics rather than borrow a known matrix combinatorics law.

## 5. Strong-gravity implication

After Iter123–125, a serious black-hole/ETH spectral route can in principle succeed if it derives a finite nonlinear rule for

- the positive-frequency graviton spectral moments or transform;
- the higher connected spectral cumulants;
- their channel/angular-momentum dependence;
- microscopic phases / unitary completion.

But using Catalan/Fuss-Catalan, loop-equation, topological-recursion or generic matrix-model laws without independent gravitational origin is comparator-contained.

## 6. Candidate checklist

For a proposed nonlinear moment law ask:

`N1` Is the recurrence derived before inspecting the desired spectrum?

`N2` Does it preserve spectral positivity?

`N3` Does a determinacy theorem or direct transform solution prove uniqueness?

`N4` Does it generate higher connected cumulants, not only `G2` moments?

`N5` Is it distinct from random-matrix/free-probability/topological-recursion/self-similar-chain/string comparators?

`N6` Does the same parent yield normalized hard graviton and CTP observables?

Only an N1–N6 survivor can use nonlinear moment rigidity as P4 evidence.

## 7. Score consequence

Positive methodological control only. R4 remains 45%.
