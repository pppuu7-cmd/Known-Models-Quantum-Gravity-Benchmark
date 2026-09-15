# SOURCE_J1_K5_P1_FOREST_NUMERICAL_KERNEL_PILOT — prospective freeze

Date: 2026-09-15
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT

## HYPOTHESIS

The exact barycentric Taylor forest operator can be coupled reproducibly to the historical P1 auxiliary Gaussian pairing engine. Before evaluating 29 forest orbits, a small numerical kernel must reproduce the historical raw P1 pairing and stable size-2 Taylor jets across S4-related subsets and two independent precision lanes.

## OBJECT

Auxiliary scalar Gaussian K5 only.

Freeze:

- vertices `0..4`, gauge vertex `0`;
- lexicographic edges `(01,02,03,04,12,13,14,23,24,34)`;
- P1 exponents `(1,1,1,1,2,2,2,2,2,2)`;
- `t=2^-k`, `epsilon_e=t^p_e`;
- held-out Gaussian test parameter `alpha=0.55` only;
- barycentric collapse/Taylor operator exactly from operator spec digest `sha256:c3e0ca0c5a5357887db79b7b0a1c5a0a1042c450ca13f7e2599c7e3801ef8a9c`;
- size-2 Taylor order `r=2`.

For a size-2 subset `S`, define

`F_S(lambda;k)=<T_epsilon, exp[-alpha ||Gamma_S(lambda)x||^2]>`

using the same ten-edge Gaussian `delta_epsilon''` product and Wick pairing as the historical P1 gate.

Freeze

`T2_S(k)=F_S(0;k)+F'_S(0;k)+(1/2)F''_S(0;k)`

and diagnostic remainder

`R2_S(k)=F_S(1;k)-T2_S(k)`.

`R2` is a method diagnostic here, not a forest-subtracted scientific observable.

## DEPENDENCY

- terminal scalar operator `eccdbcce242c561cdf6ae831f48179a7ef3dfdd0`;
- terminal P1 S4 orbit-reduction result `results/SOURCE_J1_K5_P1_S4_FOREST_ORBIT_REDUCTION_TERMINAL_2026-09-15.md`;
- historical Gaussian local-counterterm terminal gate `ae29ddbb41153e73d182173d6261e01f48a0bd00`;
- historical P1 lane artifact ID `10391658175`, used only for frozen raw-value positive locks;
- Critic qualification invalidating historical P3 divergence is respected; no P3 value enters this gate.

## FROZEN WORKLOAD

### Precision lanes

Independent decimal precision lanes:

- `dps=180`;
- `dps=260`.

Taylor derivatives must use `mp.diff` step differentiation with `addprec=80`.

### k=5 symmetry census

Evaluate all ten size-2 subsets at `k=5`.

S4 orbit A (contains gauge vertex):
`{01,02,03,04}`.

S4 orbit B (internal):
`{12,13,14,23,24,34}`.

### k=6 conditioning replay

Evaluate only representatives:

- `{0,1}`;
- `{1,2}`.

This gate intentionally does not evaluate higher subset orders or full forests.

## HISTORICAL RAW POSITIVE LOCKS

From terminal historical P1 artifact `10391658175`, alpha=0.55:

- `k=5` raw:
  `8953480453605148739421807526213396902384171526002357485692921.7217856849500135172`
- `k=6` raw:
  `19634671178659322651698889425902050217223479786982932371734431590749946022.237244`

Because `Gamma_S(1)=I`, every generalized-kernel `F_S(1;k)` must match the corresponding historical raw value with relative-or-absolute error <= `1e-65`.

## POSITIVE CONTROLS

1. Exact construction verifies `C_S+N_S=I` before numerical evaluation.
2. Every `k=5` size-2 subset raw value passes the historical lock.
3. Both `k=6` representatives pass the historical lock.
4. Within each exact S4 orbit at `k=5`, the numerical tuples `(F(0),F'(0),F''(0),T2,R2)` agree to relative-or-absolute tolerance `1e-100` in each precision lane.
5. All evaluated values are finite mpmath numbers.
6. Cross-precision aggregate: for representatives `{0,1}` and `{1,2}` at `k=5,6`, every normalized field `(raw,F0,F1,F2,T2,R2)` from 180 and 260 digits must agree within `1e-110`.
7. No scientific classifier may inspect the sign or growth of `R2` in this gate.

## NEGATIVE / ADVERSARIAL CONTROLS

1. Raw-lock comparison must use the frozen historical artifact values above, not a duplicate current calculation as the sole authority.
2. A deliberately perturbed parent raw string by relative `1e-20` must fail the raw-lock predicate.
3. A deliberately permuted P1 exponent vector that breaks the star/internal pattern must fail the frozen exponent-map lock before expensive evaluation.
4. Cross-precision disagreement beyond `1e-110` must classify precision BLOCKED, not be rounded away.

## PASS

`P1_FOREST_NUMERICAL_KERNEL_CONFIRMED_SCOPED` iff both precision lanes are individually valid and the aggregate cross-precision controls pass.

## BLOCKED / INVALID

`P1_FOREST_NUMERICAL_KERNEL_PRECISION_BLOCKED` iff source/object controls pass but the two precision lanes disagree beyond the frozen tolerance or a derivative cannot be resolved stably.

`INVALID_IMPLEMENTATION` for raw-lock failure, wrong P1 map, wrong alpha/k/subset workload, S4 violation beyond tolerance, nonfinite output, use of historical P3 divergence, or post-hoc tolerance changes.

## INTERPRETATION CEILING

PASS validates only the numerical kernel needed for later forest-orbit evaluation. It does not show that proper forest subtraction stabilizes or fails to stabilize P1, does not establish Eq. (4) existence/nonexistence, does not fail a model/family, does not close D7, and does not authorize a terminal selector or Candidate Gravity.

A PASS may authorize a separately prospectively frozen multi-orbit P1 forest-subtraction diagnostic using the 29 exact P1 orbit representatives.