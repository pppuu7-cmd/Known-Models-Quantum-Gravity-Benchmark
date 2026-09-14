# Iter500 preregistration — compact-sandwich / factorized KAK enabling gate

Date frozen: 2026-09-14
Status: **FROZEN BEFORE IMPLEMENTATION / PRODUCTION**

## Parent authority
Iter499 terminal classification is `ITER499_NUMERICAL_METHOD_BLOCKER`.

Frozen parent provenance:
- Iter499 prereg `5fd8124af8edb374d6b48c2a5e2e66cd7b322e54`;
- Arb core `f16f3106925f13e6e1d847f2d555b5d8fedc5b4d`;
- evaluator `bd935a81c2d2b1a1f4db78e1355054d92d36760f`;
- aggregate `cde7d15e03dd6d9a0ac6a78d61b07da4ff3ec517`;
- workflow/head `33d4dacc705247ab5966f1c01083cd92ee8ab2c1`;
- run `34818229950`;
- aggregate job `103895072732`;
- aggregate artifact `10337765174`;
- digest `sha256:70006ae095cebcb82dddbcfa4af72d40da7c8d3845747411a50a28eecd7b9513`.

All 12 Iter499 jobs were present exactly once, but all 12 were numerical-method blocked before a valid max-envelope state existed. Iter500 is therefore an **enabling gate only**. It contains no NONDECAY, slope, drift, Haar-convergence or max-envelope classifier.

A diagnostic-only run (`34818721003`, artifact `10336829843`, digest `sha256:a1edf763095c80c512b5ef0776187124154fc17695e29a68715021742f71a85e`) showed that dependency-preserving factorization certifies every representative internal edge `1<=a<b<=4`, while generic interval KAK still fails for a boosted node and one `0b` edge at large R. Midpoint factorized/naive matrix equivalence passed on all tested edges/R values.

## Exact compact covariance used by this gate
For every escaped node `a>=1`, the frozen Iter499 geometry has the exact form

`g_a = L_a B G_a R_a`,

where `L_a,R_a in SU(2)`, `B=boost(R)`, and `G_a` is the fixed panel-C/strong base element.

If a middle matrix has KAK

`M = U1 A(beta) U2`,

then for any `K_L,K_R in SU(2)`,

`K_L M K_R = (K_L U1) A(beta) (U2 K_R)`.

Therefore left/right compact factors do not change singular values or beta.

### Nodes
Use the point middle matrix

`M_a^node = B G_a`.

Its KAK is amplitude-independent. The whole-box node KAK is constructed as

`U1_a = L_a U1(M_a^node)`,
`beta_a = beta(M_a^node)`,
`U2_a = U2(M_a^node) R_a`.

No generic eigensolver is applied to the full interval node ball.

### Root edges `(0,b)`
Because `g_0=1`,

`h_0b = g_b^{-1} = R_b^{-1} (G_b^{-1} B^{-1}) L_b^{-1}`.

Use the point middle matrix

`M_0b = G_b^{-1} B^{-1}`

and construct

`U1_0b = R_b^{-1} U1(M_0b)`,
`beta_0b = beta(M_0b)`,
`U2_0b = U2(M_0b) L_b^{-1}`.

No generic eigensolver is applied to the full interval `0b` ball.

### Internal edges `1<=a<b<=4`
Use the dependency-preserving exact factorization

`h_ab = R_b^{-1} M_ab R_a`,

with

`M_ab = G_b^{-1} B^{-1} L_b^{-1} L_a B G_a`.

Apply the frozen Iter499 closed-form 2x2 Arb KAK only to the **middle** interval matrix `M_ab`, then restore the compact factors:

`U1_ab = R_b^{-1} U1(M_ab)`,
`beta_ab = beta(M_ab)`,
`U2_ab = U2(M_ab) R_a`.

No determinant projection, midpoint substitution, SVD replacement, polar-factor substitution or box subdivision is allowed.

## Frozen state space
Reuse the complete Iter499 geometric state space, but remove redundant causal/rho duplication from the **interval KAK certification itself** because geometry/KAK does not depend on causal signs or rho:
- active coordinates `[0,1,3,5,6,11]`;
- the same eight six-coordinate directions frozen in Iter499;
- both signs `+1,-1`;
- the same 16 closed rational amplitude boxes `A_k=[(16+k)/12800,(17+k)/12800]`, `k=0,...,15`;
- `R={6,8,10,12}`;
- panel C / strong shared-node geometry.

This is `8 directions x 2 signs x 16 boxes x 4 R = 1024` geometric box/R states. Every state contains four escaped-node KAKs and ten edge KAKs.

## Frozen arithmetic
- CPython 3.12;
- `python-flint==0.9.0`;
- Arb/Acb `ctx.prec=384` bits;
- the exact-rational interval endpoints and `repr(float)` lifting convention from Iter499.

No precision escalation or adaptive subdivision belongs to Iter500.

## Frozen interval controls
For every geometric box/R state:
1. all four compact-sandwich node KAKs are finite and have `lower(beta)>0`;
2. all four `0b` compact-sandwich KAKs are finite and have `lower(beta)>0`;
3. all six internal factorized-middle KAKs pass the Iter499 positive/separated-eigenvalue and eigenvector-chart predicates;
4. for all 14 node/edge objects, entrywise `0` is contained in `U1*A(beta)*U2 - h`;
5. entrywise `0` is contained in `U1^dagger U1-I` and `U2^dagger U2-I`;
6. `1` is contained in `det(U1)` and `det(U2)`;
7. direct factorized edge matrices satisfy the exact frozen source geometry; no edge is replaced by an independent surrogate.

A failure to construct/certify an interval middle KAK is a numerical-method blocker, not a scientific failure.

## Frozen midpoint regression to established source object
For the midpoint of **every one of the 256 signed-direction amplitude boxes** and every R:
- construct the same high-precision source geometry with the established Iter491 `hp_nodes/hp_relatives/hp_kak` implementation at 100 decimal digits;
- compare all ten edge matrices against the compact/factorized construction with maximum relative matrix residual `<1e-9` (the established Iter491 source-object identity scale);
- compare every edge beta against the Iter491 high-precision beta with absolute error `<1e-10`.

Additionally, for every midpoint/R/edge, evaluate the full j=1 Toller magnetic matrices for **both branches** `T+` and `T-` at all four frozen rho witnesses `{0.35,0.9,1.6,2.7}` using:
1. the Iter500 compact/factorized KAK;
2. the established Iter491 high-precision KAK converted through the same source `full_from_kak` convention.

Require maximum relative matrix discrepancy `<1e-8`, with denominator `max(1,maxabs(reference))`.

This midpoint source regression is an implementation/convention control only. It does not replace whole-box interval KAK certification.

## Frozen negative control
For each R, also attempt the old Iter499 generic interval KAK on the full node-1 ball for direction 1, sign `+`, box `A0`. At least one of the already-observed large-R states `{R=10,R=12}` must remain uncertified by the old generic construction. This prevents the enabling PASS from being a vacuous rerun that silently changes the original method-blocker diagnosis.

## Frozen GitHub parallel matrix
Exactly four independent jobs:
- block 0: directions 1-2;
- block 1: directions 3-4;
- block 2: directions 5-6;
- block 3: directions 7-8.

Each job covers both signs, all 16 boxes and all four R values. Use `fail-fast:false`, `max-parallel:4`.

Aggregate must require all four job ids exactly once.

## Frozen classifier
Per job:
- `ITER500_COMPACT_SANDWICH_FACTORIZED_KAK_LANE_QUALIFIED_SCOPED` iff every whole-box interval control and every midpoint source regression passes;
- `SCIENTIFIC_FAIL_ITER500_COMPACT_KAK_COVARIANCE` only if arithmetic is finite/certified but the exact compact-sandwich reconstruction/covariance identity itself fails a frozen containment predicate;
- `ITER500_NUMERICAL_METHOD_BLOCKER` if any required interval middle KAK cannot be certified or the computation becomes nonfinite before the identity can be tested.

Aggregate:
- `ITER500_COMPACT_SANDWICH_FACTORIZED_KAK_QUALIFIED_SCOPED` iff all four lanes qualify and the negative control reproduces the old-method limitation;
- `SCIENTIFIC_FAIL_ITER500_COMPACT_KAK_COVARIANCE` iff any lane returns the scientific covariance failure;
- otherwise `ITER500_NUMERICAL_METHOD_BLOCKER`.

## Interpretation ceiling
A PASS establishes only that the frozen Iter499 geometry admits a validated compact-sandwich/factorized KAK/Toller representation across the full 16-box one-dimensional state space, with midpoint agreement to the established source object. It does **not** establish any NONDECAY interval, max-envelope bound, positive-measure neighborhood, Haar convergence/divergence theorem, spectral-integration result, D7-S2 closure, terminal D7 label or Candidate Gravity activation.

Only a PASS authorizes a new, separately preregistered direct max-envelope interval science gate.
