# SOURCE_J1_K5_SCALAR_FOREST_OPERATOR_PILOT — prospective freeze

Date: 2026-09-15
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT

## HYPOTHESIS

A fully explicit, same-realization, S5-covariant KMQGB-derived Taylor forest operator can be defined for the auxiliary scalar Gaussian K5 witness before any expensive numerical P1 subtraction is attempted.

The purpose of this gate is operator definition and exact algebraic validation only. It does not test convergence/divergence after subtraction.

## OBJECT

Use five scalar vertex coordinates `q_0,...,q_4` modulo common translation, represented in the gauge `q_0=0` by the four-vector

`x=(q_1,q_2,q_3,q_4)`.

For each connected subset `S`, `2<=|S|<=5`, define the full-coordinate barycentric collapse by replacing every `q_v`, `v in S`, with

`m_S = (1/|S|) sum_{v in S} q_v`,

leaving vertices outside `S` unchanged, and then restoring the gauge by subtracting the transformed `q_0` from all vertices. This induces an exact rational `4x4` matrix `C_S` on `x`.

Define

`N_S = I - C_S`

and the normal-scaling family

`Gamma_S(lambda) = C_S + lambda N_S`.

For an analytic test function `f`, freeze the Taylor projector

`(T_S^r f)(x) = sum_{n=0}^r (1/n!) [d^n/dlambda^n f(Gamma_S(lambda)x)]_{lambda=0}`.

The scalar subtraction orders are fixed by the terminal same-realization repair:

- `r(S)=2` for `|S|=2`;
- `r(S)=7` for `|S|=3`;
- `r(S)=15` for `|S|=4`;
- full root `r(V)=26` for `|V|=5`.

## DEPENDENCY

Consume only:

- scalar collision-strata authority `2f6d3af60439af4bc8b7c62e6813c58fb21ec1f4` / terminal child `81094144184751770256ab3bb144bd9189a6a9ad`;
- exact full-collision radial action-space authority `5e95318f29e26f4ea954f269cbec2c69fa8089d8`, qualified by Critic `02f07832893d6d06e3b9d92efab1b2462e3ace51`;
- scalar laminar order/topology terminal repair result `results/SOURCE_J1_K5_SCALAR_LAMINAR_FOREST_ORDER_REPAIR_TERMINAL_2026-09-15.md`, terminal commit `16b6340a2bd78e350258636b226ac69adb8a40d2`;
- recovery delta `8ed002e1858393dd6a8db50132ae5c8993b8d24f`.

The historical prereg `a63df1f3c66dbadaec7bbaab2c916cffefb56813` is superseded and is not executable authority.

## PROPER-FOREST FORMULA

Let `F_prop` be the exact 236-member family of laminar forests made only from proper connected subsets `S proper subset V`, including the empty forest.

For a laminar forest `F`, define

`T_F = product_{S in F} T_S^{r(S)}`.

The implementation must prove exact order independence of this product from the commuting normal-scaling families for nested/disjoint subsets; it may not assume commutation from the forest label alone.

Freeze the proper-stratum subtraction operator

`W_prop = sum_{F in F_prop} (-1)^|F| T_F`.

Keep the full collision strictly separate and freeze the KMQGB-derived root operator

`W_full = (I - T_V^26) W_prop`.

This is a KMQGB-derived barycentric Taylor forest prescription for the auxiliary scalar witness. It is not claimed to be source-authorized Eq. (4) renormalization and is not claimed unique.

## FROZEN EXACT INPUTS

- vertices exactly `{0,1,2,3,4}`;
- gauge exactly `q_0=0`;
- all exact arithmetic via integers/rationals;
- proper connected subsets exactly sizes 2,3,4;
- proper-only forests exactly the topology independently re-enumerated by implementation;
- all 120 S5 relabelings;
- scalar orders exactly `{2:2,3:7,4:15}` and full root order `26`;
- no numerical Gaussian residuals enter this gate.

## POSITIVE CONTROLS

1. Every `C_S` is exactly idempotent.
2. `rank(C_S)=5-|S|` in the gauge-fixed four-dimensional scalar space; equivalently `rank(N_S)=|S|-1`.
3. Full collision has `C_V=0`, `N_V=I`, and root order 26.
4. For every permutation `p in S5`, the exact gauge representation `R_p` obeys
   `R_p C_S = C_{p(S)} R_p`.
5. Every nested or disjoint pair of proper subsets has commuting collapse matrices and commuting `Gamma` families.
6. For nested `S subset T`, exact composition satisfies `C_T C_S = C_S C_T = C_T`.
7. Every overlapping nonnested proper pair is excluded from a laminar forest and must fail the collapse-commutation control.
8. For every internal pair `a,b in S`, the normal linear form `ell_ab=q_a-q_b` obeys `ell_ab C_S=0` and `ell_ab N_S=ell_ab`; therefore `ell_ab(Gamma_S(lambda)x)=lambda ell_ab(x)` exactly.
9. The preceding identity must imply the exact Taylor fixture:
   - `T_S^r ell_ab^m = ell_ab^m` for `m<=r`;
   - `T_S^r ell_ab^(r+1) = 0`.
10. Proper-only forest census/histogram/orbit count must reproduce the terminal repair: 236 forests, histogram `{0:1,1:25,2:105,3:105}`, 12 S5 orbits.
11. The serialized operator specification must have a deterministic SHA256 digest reproducible on both Python configurations.

## NEGATIVE / ADVERSARIAL CONTROLS

1. A known overlapping nonnested pair `{0,1}` / `{1,2}` must not commute and must not be admitted to a forest.
2. Replacing scalar orders by historical three-normal-dimensional orders `0,3,9,18` must fail the scalar-order lock.
3. Admitting full `V` to `F_prop` must fail the proper-forest guard.
4. Replacing the barycentric collapse by a one-vertex anchoring collapse must fail at least the S5 covariance or rank/covariance signature.
5. A degree `r+1` normal monomial must survive `(I-T_S^r)`; an implementation that subtracts it is invalid.

## PASS

`SCALAR_K5_FOREST_OPERATOR_PILOT_CONFIRMED_SCOPED` iff all exact positive and adversarial controls pass, the operator specification is fully serialized, both independent Python lanes agree on all exact counts/digests, and no floating-point decision is used.

## FAIL

`SCALAR_K5_FOREST_OPERATOR_PILOT_CONTRADICTION` iff exact implementation is valid but the frozen barycentric/Taylor construction contradicts one of the same-realization algebraic identities above.

## BLOCKED / INVALID

`SCALAR_K5_FOREST_OPERATOR_PILOT_BLOCKED` iff exhaustive exact checks cannot complete for an identified resource reason.

`INVALID_IMPLEMENTATION` for any wrong gauge, wrong order table, wrong forest family, failed S5 covariance, admitted overlap, hard-coded scientific verdict, floating rank/commutation decision, or missing deterministic operator serialization.

## INTERPRETATION CEILING

PASS authorizes only a separately prospectively frozen numerical evaluation of this exact KMQGB-derived operator on the stable P1 auxiliary Gaussian witness. It does not establish forest-subtracted convergence/divergence, Eq. (4) existence/nonexistence, source authorization, uniqueness, model/family failure, D7 closure, a terminal selector, or Candidate Gravity activation.

The numerical successor must retain a high-precision replay, explicit cancellation/lost-digit audit, and the robust P1 premise only; it must not consume the Critic-invalidated historical P3 divergence claim.