# KMQGB Tenth Wave — Parent-Response Completeness Layer

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–9:** terminal and immutable.  
**Status:** **TERMINAL 5/5 = 100%**.  
**Purpose:** ensure future Candidate Gravity and C5 source/contact responses are complete at every perturbative/source-response order before Ward reduction or comparator subtraction.

| # | Target | Terminal result | State |
|---|---|---|---|
| T10-01 | general inverse-kernel response identity | complete `D_S K^-1` is the sum over all ordered set partitions of the derivative labels | `PASS_RQIR_GATE` |
| T10-02 | algorithmic completeness generator | ordered-partition families are generated/count-checked automatically rather than selected diagrammatically | `PASS_RQIR_GATE` |
| T10-03 | channel-origin classifier | response completeness is separated from pole/cut/nonanalytic-origin classification | `PASS_RQIR_GATE` |
| T10-04 | Ward/contact completeness | exact Ward/physical reduction is performed only after all same-parent response families are included or independently proven null | `PASS_RQIR_GATE` |
| T10-05 | symmetric KG-vs-C5 order matching | Candidate Gravity and full matched C5 must each be complete at the same order/routing/domain before residual profiling | `PASS_RQIR_GATE` |

**Tenth-wave terminal coverage: 5/5 = 100%.**

## Authoritative protocol

`protocol/PARENT_KERNEL_RESPONSE_COMPLETENESS.md`

Reference generator:

`code/inverse_kernel_ordered_partitions.py`

## General identity

For `G=K^-1` and mixed derivative label set `S`,

`D_S G = sum_(k=1..|S|) (-1)^k sum_(B1,...,Bk in OP(S,k)) G K_B1 G ... K_Bk G`.

Every ordered set partition occurs once.

At order `n`, family count with `k` kernel blocks is

`k! S(n,k)`

and total term count is the ordered Bell/Fubini number.

Verified counts:

- `n=1`: 1;
- `n=2`: 3;
- `n=3`: 13;
- `n=4`: 75;
- `n=5`: 541.

This rapid growth makes algorithmic completeness mandatory for higher-order KG work.

## Third-order example

The complete third mixed response contains

1. one `K3` contact family;
2. six ordered `K1/K2` placements;
3. six ordered `K1^3` chains.

This matches the structural lesson independently exposed by external RQIR Iteration 590, where the omitted `K3` and `K1^3` families were nonzero on the frozen fixture.

## Frozen order of operations

`same-parent complete response`

`-> analytic/cut origin classification`

`-> Ward/contact cancellation and physical-basis reduction`

`-> channel discontinuity / matched observable`

`-> comparator residual geometry / COR`

Do not reorder these steps.

## Candidate Gravity consequence

A future KG residual is invalid if it depends on comparing

- an incomplete KG response with a complete comparator, or
- a complete KG response with an incomplete C5/comparator response.

Every future promoted response observable must therefore include its ordered-partition ledger and explicit origin/zero proofs for any removed family.

## Promotion guardrail

This wave is methodology only. No Candidate Gravity ansatz/readiness increase is authorized.
