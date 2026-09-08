# KMQGB Current Benchmark Front

**Updated:** 2026-09-08  
**KMQGB iteration:** 033  
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`  
**Branch:** `main`  
**Phase:** WAVES 1–10 TERMINALLY CLASSIFIED / KG PROMOTION GATE FROZEN / CROSS-ORDER RIGIDITY NEXT

## Coverage

- Wave 1: **9/9 = 100%** — immutable.
- Waves 2–10: **each 5/5 = 100%** — immutable after terminal closure.
- Globally authorized robust unique-QG residuals: **0**.
- Candidate Gravity ansatz promoted by KMQGB: **no**.
- External Candidate Gravity readiness: **24%**.

Benchmark coverage is finite methodology/model-audit coverage, not theory probability and not Candidate Gravity readiness.

## Wave 9 — optimal comparator-annihilating observables

Wave 9 is terminal `5/5`, all methodology `PASS_RQIR_GATE`.

Authoritative protocol:

`protocol/OPTIMAL_COMPARATOR_CONTRASTS.md`

Reference code:

`code/optimal_comparator_contrasts_reference.py`

Core results:

1. exact comparator-null contrasts satisfy `J_union^T w=0` in the physical basis;
2. for candidate signal `s`, covariance-optimal contrast has direction
   `w_opt proportional to Sigma^(-1/2) Pi_perp Sigma^(-1/2) s`;
3. maximum local post-comparator SNR is
   `||Pi_perp Sigma^(-1/2)s||`;
4. adding `k` physical observables changes local complement dimension by
   `Delta d_perp = k - Delta rank(J_union)`;
5. future source/detector designs should maximize comparator-orthogonal rank, projected singular values, or projected SNR — not raw sensitivity alone.

## Wave 10 — parent-response completeness

Wave 10 is terminal `5/5`, all methodology `PASS_RQIR_GATE`.

Authoritative protocol:

`protocol/PARENT_KERNEL_RESPONSE_COMPLETENESS.md`

Reference generator:

`code/inverse_kernel_ordered_partitions.py`

For `G=K^-1` and mixed derivative label set `S`, freeze

`D_S G = sum_k (-1)^k sum_(B1,...,Bk in OP(S,k)) G K_B1 G ... K_Bk G`.

Every ordered set partition appears once.

Term counts grow as ordered Bell/Fubini numbers:

- order 1: `1`;
- order 2: `3`;
- order 3: `13`;
- order 4: `75`;
- order 5: `541`.

Thus higher-order KG source/contact response must be generated algorithmically rather than by hand-selecting diagram families.

Frozen order:

`complete same-parent response -> origin/cut classification -> Ward/contact physical reduction -> matched observable -> comparator/COR quotient`.

## Candidate Gravity promotion gate

Created

`protocol/CANDIDATE_GRAVITY_PROMOTION_GATE.md`.

No KG ansatz may be promoted before all of the following are closed:

1. one explicit parent dynamics;
2. complete same-parent response at every used order;
3. exact Ward/Bianchi/contact/constraint physical reduction;
4. common-domain comparator definition;
5. full attribution stack;
6. full matched C5 and other comparator quotient;
7. nonzero local COR;
8. nonzero global/nonlinear comparator separation;
9. projected identifiability / optimal observable design;
10. rigidity / low remaining functional freedom.

Only after a robust nonzero algebraic residual may Fisher/resources be promoted.

## Residual-space geometry retained

For physical residual `r`, covariance `Sigma`, and union comparator Jacobian `J_C`:

`A=Sigma^(-1/2)J_C`,

`Pi_perp=I-AA^+`,

`COR=Pi_perp Sigma^(-1/2)r`.

Local signal survival fraction:

`eta(s)=||Pi_perp Sigma^(-1/2)s||/||Sigma^(-1/2)s||`.

A nonzero local COR/eta is only a prefilter; finite/global comparator profiling remains mandatory.

## External RQIR authority — read-only refresh

Latest directly observed scientific authority: **Iteration 590**.

Candidate Gravity `MODEL_READINESS = 24%`.

Key upstream progress:

- Iter424 physical gate `5/5 PASS`, unresolved set `[]`;
- Iter581 exact15 `Tr U1^2` raw-valid PASS;
- Iter582 q2-resolved `D_s Gamma_e2` PASS, still non-residual;
- Iter583–584 same-parent MSSC quadratic K2 and mixed `K2(h1,h2)` raw-valid;
- Iter586 proves off-shell source completion is required for the timelike buckets;
- Iter587 off-shell K1 routing/Ward term raw-valid;
- Iter588 exact fixture routing bound;
- Iter589 same-action K1/K2 normalization raw-valid;
- **Iter590 proves cubic source-response completeness requires three origin families: local K3, six K1/K2 placements, and six ordered K1^3 chains. K3 and K1^3 are nonzero on the frozen fixture.**

Therefore the six K1/K2 terms are not yet authorized as the complete discontinuity-bearing source block.

Exact external next gate:

1. prove/freeze hard-channel origin of local K3 and whether `D_s K3=0` in the frozen discontinuity convention;
2. separately classify K1^3 under the frozen linked cut/origin protocol;
3. only then close the complete nonlinear source Ward object and map to Iter582/comparator quotient.

KMQGB does not treat the three Iter582 buckets as residual data yet.

## RQIR-COR pre-registration retained

If the future matched residual is only a real/imaginary three-bucket physical vector, then

`d_perp = 3 - rank(A_union)`.

If `rank(A_union)=3`, increased numerical precision alone cannot produce a local novelty direction. Add a linked observable/order only when

`Delta d_perp = Delta m_phys - Delta rank(J_union) > 0`

or projected conditioning materially improves.

## Exact next KMQGB front — cross-order rigidity

The next methodology wave should stack multiple response orders from the **same parent dynamics** and test whether shared parameters produce more physical dimensions than comparator tangent dimensions.

Priority tasks:

1. define stacked multi-order observable/covariance/Jacobian notation;
2. forbid independent per-order retuning of a parameter that is shared by the parent dynamics;
3. derive cross-order comparator-null contrasts;
4. include cross-order covariance and common theoretical/systematic uncertainties;
5. freeze a cross-order rigidity certificate based on projected rank/singular values.

This is currently the most promising methodology direction for finding a residual relation without inventing a qualitative feature label.
