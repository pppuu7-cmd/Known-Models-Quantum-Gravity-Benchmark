# KMQGB Fourteenth Wave — Minimal Discriminating Test Suite

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–13:** terminal and immutable.  
**Status:** **TERMINAL 5/5 = 100%**.  
**Purpose:** choose the smallest pre-registered set of response/configuration blocks that retains comparator-orthogonal identifiability, attribution coverage and predictive robustness.

| # | Target | Terminal result | State |
|---|---|---|---|
| T14-01 | candidate block library | freeze admissible order/configuration/contrast block library before residual inspection | `PASS_RQIR_GATE` |
| T14-02 | relative design-cost metadata | separate pre-residual complexity costs from forbidden final resource claims | `PASS_RQIR_GATE` |
| T14-03 | threshold-first minimal subset | minimize relative cost subject to frozen post-comparator rank/conditioning constraints | `PASS_RQIR_GATE` |
| T14-04 | leave-one-block robustness | require selected suite not to depend on one fragile non-mandatory block | `PASS_RQIR_GATE` |
| T14-05 | attribution-preserving suite | prohibit minimizing away mediator/gravity/locality/relational evidence | `PASS_RQIR_GATE` |

**Fourteenth-wave terminal coverage: 5/5 = 100%.**

## Authoritative protocol

`protocol/MINIMAL_DISCRIMINATING_TEST_SUITE.md`

Reference code:

`code/minimal_test_suite_reference.py`

## Optimization form

For candidate block subset `S`, minimize

`sum_(b in S) c_b`

subject to pre-registered requirements such as

- `d_perp(S) >= d_target`;
- `rank[B_KG(S)] >= q_target`;
- `sigma_min_plus(S) >= tau_sigma`;
- predictive/holdout and attribution coverage constraints.

For small libraries, exhaustive subset search is preferred; greedy selection is only a heuristic unless global optimality is verified.

## Robustness requirement

Evaluate every non-mandatory block deletion `S\{b}`.

A suite whose projected rank/conditioning collapses when one fragile observable is removed is not a robust discriminator even if the full set looks strong.

## Resource guardrail

`c_b` is only relative design complexity for choosing a prospective suite. It is **not** experimental resource closure and does not authorize Fisher/resource readiness before a real comparator-subtracted residual exists.

## Candidate Gravity lesson

A future KG proposal should arrive with a **small, redundant, attribution-complete and predictive test suite**, not an unlimited menu from which a successful observable can be chosen after the result is known.

## Promotion guardrail

This wave is methodology only. No Candidate Gravity ansatz/readiness increase is authorized.
