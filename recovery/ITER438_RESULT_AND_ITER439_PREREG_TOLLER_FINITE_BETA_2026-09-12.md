# Iter438 result + Iter439 preregistration — 2026-09-12

## Frozen benchmark policy

RQIR Core v1.0 remains frozen. Missing objects/gates are blockers, not a no-go theorem. Candidate Gravity remains inactive. No terminal D7 label is authorized while D7-S2/S3/S4 remain open.

Canonical statuses remain:

- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S2: `NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`

## Iter438 result — exact invariant-projector support

The first Iter438 run, Actions run `34709760371` at head `12b8cc8b431078427d649acf0dc8d5748fc840bd`, was scientifically invalid because the source-pattern control incorrectly applied an integer-spin parity condition directly to `j`. In particular the admissible source node `[5,2,2,2]` was rejected. This run is classified as a control/implementation failure only and carries no scientific conclusion.

The validator was repaired without changing the frozen scientific gate: admissibility is now checked on doubled spins `2j`. The repair commit is `ae8e5a1590b29eb23f428a81658b34173108c0f6`.

Corrected Actions run `34709968631` completed successfully with all 12 Iter437 survivor profiles and the aggregate job valid. Aggregate artifact `lqg-iter438-summary`, artifact id `10302288437`, digest `sha256:945f6998dbfa9a4e21bf2317b8dc60ab1ad0fa486a9f369513081712f05cd087`, reports:

- lane count: 12
- controls valid: true
- surviving profiles: 0
- excluded profiles: 12
- classification: `SOURCE_BACKED_SLOW_OBSTRUCTION_KILLED_BY_EXACT_INVARIANT_PROJECTOR`

The 12 excluded profiles are exactly the 12 source-backed local-magnetic-closure survivors from Iter437:

`(10,3), (10,4), (11,3), (12,3), (12,4), (13,3), (14,3), (3,4), (5,4), (6,4), (9,3), (9,4)`.

### Iter438 scope guard

This result is an exact discrete SU(2) invariant-projector/global-magnetic support result for one frozen published Lorentzian boundary-spin completion only. It is **not** a proof of full Haar/angular causal-vertex finiteness, a causal-vertex divergence theorem, cutoff removal, family-wide promotion, or terminal D7 closure. D7-S2 therefore remains `NOT_CLOSED`.

The result does show that the Iter435 envelope-level slow profile can be removed by the exact invariant projector even where the weaker Iter437 local magnetic-sum closure allowed it. Therefore the next useful independent test must probe the source Toller functions themselves rather than repeat another local SU(2) support gate.

---

# Iter439 preregistration — source-faithful finite-beta Toller asymptotics

## Scientific question

Can the gamma-simple minimal-channel Toller functions used in causal EPRL be realized numerically from the exact published hypergeometric formula on a frozen finite-beta grid, with their branch-specific asymptotic exponents recovered independently from finite-beta data?

This gate validates the actual branch-level source formula and its large-rapidity realization before attempting any stronger noncompact causal-vertex integrability statement.

## Source lock

Primary source: E. Bianchi, C. Chen, M. Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945, published Phys. Rev. D 114, 046014 (2026).

Source facts frozen for Iter439:

1. The EPRL gamma-simple restriction is `k=j=l` and `rho=gamma*j`.
2. Eq. (46) gives, in this channel,

   `t^(±) = exp[-(j ∓ i rho ± m + 1) beta] * C_(±)(rho,j,m) * 2F1(j ± m + 1, j + 1 ∓ i rho; 1 ± m ∓ i rho; exp(-2 beta))`,

   with the gamma-function factor `C_(±)` independent of beta.
3. Therefore the branch magnitude exponents are frozen as

   - plus branch: `alpha_plus = j + m + 1`
   - minus branch: `alpha_minus = j - m + 1`.
4. The paper also establishes `T^(+) + T^(-) = D`; Iter439 does **not** use that identity as a pass condition because this gate isolates the branch-level finite-beta asymptotic realization and does not yet reconstruct every normalization/phase convention of the full matrix.

Boundary/source spin values remain those of the published Lorentzian completion used by Iter437/438: `j in {2,5}` (four `j=5` faces and six `j=2` faces; ratio 2/5, not `j=5/2`).

For a source-backed gamma cross-check, freeze `gamma in {7,8}`, the two values explicitly used for the Lorentzian Regge numerical comparison in P. Dona et al., *Numerical study of the Lorentzian EPRL spin foam amplitude*, Phys. Rev. D 100, 106003 (2019), arXiv:1903.12624.

Source URLs:
- https://arxiv.org/abs/2604.24945
- https://arxiv.org/abs/1903.12624

## Frozen matrix

Independent lanes are the Cartesian product:

- `gamma in {7.0, 8.0}`
- `j in {2,5}`
- every integer magnetic number `m=-j,...,+j`
- branch `plus` and `minus`

This gives `2 * [(5 + 11) * 2] = 64` lanes.

Frozen rapidity grid for every lane:

`beta = [2.0, 3.0, 4.0, 6.0, 8.0, 10.0]`.

## Numerical realization

To avoid irrelevant gamma-prefactor conditioning, Iter439 evaluates the beta-dependent normalized ratio

`R_branch(beta) = exp(alpha_branch * beta) * |t_branch(beta)| / |C_branch| = |2F1(a,b;c;exp(-2 beta))|`.

The Gauss hypergeometric function is evaluated directly by its power series recurrence

`term_n = term_(n-1) * (a+n-1)*(b+n-1)/((c+n-1)*n) * z`,

with `z=exp(-2 beta)`.

Two independently converged evaluations are required in every lane:

- standard: relative/absolute term target `1e-14`, max 20,000 terms;
- tight: relative/absolute term target `1e-16`, max 40,000 terms.

The two evaluations must agree to `<= 5e-12` in complex absolute difference on the full frozen beta grid. These are numerical controls only; changing them after seeing scientific output is forbidden.

## Frozen asymptotic controls

For every lane:

1. all source parameters are valid (`gamma>0`, `j in {2,5}`, integer `m` in `[-j,j]`);
2. every standard and tight hypergeometric series converges before its frozen term cap;
3. standard/tight complex values agree within `5e-12` at each beta;
4. `|R(10)-1| <= 1e-10`;
5. the effective magnitude exponent from the last two beta points,

   `alpha_eff(8,10) = alpha - [log R(10) - log R(8)] / 2`,

   satisfies `|alpha_eff-alpha| <= 1e-8`;
6. the late-tail correction decreases: `|R(10)-1| <= |R(8)-1|`.

These conditions validate numerical realization of the published branch asymptotic on the frozen grid. They are not physical convergence criteria for the complete causal vertex.

## Frozen classifications

Lane valid:

`SOURCE_TOLLER_FINITE_BETA_ASYMPTOTIC_REALIZED`

Any failed numerical/source control:

`CONTROL_INVALID`

Aggregate, only if all 64 lanes are valid:

`SOURCE_TOLLER_FINITE_BETA_ASYMPTOTIC_REALIZED_ON_FROZEN_GRID`

Otherwise:

`CONTROL_INVALID`

## Scope guard

Iter439 is a source-convention validation of the gamma-simple minimal-channel **individual Toller branches** and their finite-beta/large-beta asymptotic exponents on the frozen spin/gamma grid. It is not a proof of full K5 Haar/angular contraction, not a proof of causal-vertex absolute convergence or divergence, not an `i epsilon` collision-distribution theorem, not cutoff removal, not family promotion, and not terminal D7 authorization.

A successful Iter439 authorizes only the next noncompact gate: an explicitly preregistered complete projected/collision/integrability test that preserves the distinction between an individual Toller branch, their sum, and the full causal vertex.