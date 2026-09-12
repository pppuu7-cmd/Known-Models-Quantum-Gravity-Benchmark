# Iter439 result + Iter440 preregistration — 2026-09-12

## Frozen benchmark policy

RQIR Core v1.0 remains frozen. Candidate Gravity remains inactive. No terminal D7 classifier or `EXISTING_SUFFICIENT` / `ADAPT_EXISTING` / `HYBRID_REQUIRED` / `NEW_REQUIRED` label is authorized while D7-S2/S3/S4 remain open.

Canonical statuses remain:
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S2: `NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`

## Iter438 corrected result retained

The initial Iter438 run `34709760371` was control-invalid because source admissibility incorrectly applied parity to `j` rather than doubled spins `2j`; it carries no scientific conclusion. The frozen gate was repaired without changing the science at commit `ae8e5a1590b29eb23f428a81658b34173108c0f6`.

Corrected run `34709968631` completed with 12/12 valid lanes. Aggregate artifact `lqg-iter438-summary`, artifact id `10302288437`, digest `sha256:945f6998dbfa9a4e21bf2317b8dc60ab1ad0fa486a9f369513081712f05cd087`, reports 0 survivors / 12 excluded and classification `SOURCE_BACKED_SLOW_OBSTRUCTION_KILLED_BY_EXACT_INVARIANT_PROJECTOR`.

Scope: exact discrete SU(2) invariant-projector/global-magnetic support for one frozen published Lorentzian boundary-spin completion only; not full Haar/angular causal-vertex finiteness, divergence, cutoff removal, family promotion, or terminal D7 closure.

## Iter439 terminal result

The first workflow construction had a matrix-level infrastructure defect (`if` referenced matrix fields before job expansion). This was repaired mechanically by explicit matrix exclusions; no frozen scientific parameter or threshold changed. Repair/main commit: `0f16e65ebad11b7ffa0512cf129dc40733fedaa5`.

Authoritative repaired Actions run: `34710486745`.
Aggregate artifact: `lqg-iter439-summary`, artifact id `10302933351`, digest `sha256:6fe5d72ffd5feb8a9cf42ce89d52125958ee680d58fbb0f90f450cb16772e9aa`.

Terminal aggregate:
- expected lanes: 64
- realized lanes: 64
- invalid lanes: 0
- controls valid: true
- max standard/tight complex absolute difference: `2.5735369674468285e-16`
- max `|R(10)-1|`: `2.2672690169756038e-08`
- max late-tail effective-exponent absolute error: `6.076071503713365e-07`
- classification: `SOURCE_TOLLER_FINITE_BETA_ASYMPTOTIC_REALIZED_ON_FROZEN_GRID`

Scope: gamma-simple minimal-channel individual Toller-branch finite-beta/large-beta source-formula validation only. It is not a full K5 Haar/angular contraction, causal-vertex convergence/divergence theorem, i-epsilon collision theorem, cutoff removal, family promotion, or terminal D7 result.

---

# Iter440 preregistration — source Toller branch recombination identity

## Scientific question

Does the full source-faithful gamma-simple normalization and phase convention of the published reduced Toller branches numerically realize the exact source identity

`t^(+)(beta) + t^(-)(beta) = d(beta)`

on a frozen held finite-beta grid for the same source-backed spins and gammas used by Iter439?

Iter439 divided out the beta-independent gamma prefactors and therefore did not validate their normalization/phase or the cancellation/recombination between branches. Iter440 is a prerequisite before any stronger projected Feynman-i-epsilon collision/integrability gate.

## Source lock

Primary source: E. Bianchi, C. Chen, M. Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, Phys. Rev. D 114, 046014 (2026), arXiv:2604.24945.

Freeze the gamma-simple equations exactly as published:

- `k=j=l`, `rho=gamma*j`.
- Eq. (45):
  `d_jjm(beta) = exp[-(j - i rho + m + 1) beta] * 2F1(j+m+1, j+1-i rho; 2j+2; 1-exp(-2 beta))`.
- Eq. (46):
  `t_pm_jjm(beta) = exp[-(j ∓ i rho ± m + 1) beta] * Gamma(2j+2) Gamma(± i rho ∓ m) / [Gamma(j ∓ m +1) Gamma(j+1 ± i rho)] * 2F1(j ± m +1, j+1 ∓ i rho; 1 ± m ∓ i rho; exp(-2 beta))`.
- Exact identity from the source: `t^(+) + t^(-) = d`.

No artificial `beta+i*epsilon` substitution is permitted.

## Frozen matrix

Independent lanes:
- `gamma in {7.0, 8.0}`
- `j in {2,5}`
- every integer `m=-j,...,+j`

Total: `2 * (5+11) = 32` independent lanes.

Every lane evaluates the held finite-beta grid:
`beta = [0.5, 1.0, 2.0, 4.0, 8.0]`.

## Frozen numerical implementation

Use `mpmath` complex gamma and Gauss hypergeometric evaluation directly from Eq. (45)/(46), with two independent precision levels:
- standard: 80 decimal digits
- tight: 120 decimal digits.

For each beta and each precision compute `d`, `t_plus`, `t_minus`, and residual `r = t_plus + t_minus - d`.

Define scaled recombination residual
`eps = |r| / max(1, |d|, |t_plus| + |t_minus|)`.

Frozen controls:
1. all values finite;
2. standard/tight values for each of `d`, `t_plus`, `t_minus` agree after scaling to `<= 1e-35`;
3. source identity residual at both precisions satisfies `eps <= 1e-30` for every beta;
4. plus/minus branch values are evaluated independently, never inferred from `d` or from each other;
5. source parameter guards reproduce `rho=gamma*j`, integer `m`, and `-j<=m<=j`.

Thresholds are frozen before any Iter440 production result is inspected and must not be weakened post hoc.

## Frozen classifications

Per lane:
- all controls valid: `SOURCE_TOLLER_RECOMBINATION_IDENTITY_REALIZED`
- otherwise: `CONTROL_OR_IDENTITY_INVALID`

Aggregate:
- exactly 32 valid lanes and all realize the identity: `SOURCE_TOLLER_RECOMBINATION_IDENTITY_REALIZED_ON_FROZEN_GRID`
- otherwise: `ITER440_CONTROL_OR_RECOMBINATION_INVALID`

## Interpretation lock

A PASS validates the full Eq. (45)/(46) branch normalization/phase and their finite-beta recombination on this frozen grid. It authorizes a separately preregistered projected Feynman-i-epsilon/collision-integrability gate.

A FAIL is first a source-formula/numerical-convention discrepancy to diagnose; it is not a physical causal-vertex divergence result.

Even PASS is not full K5 Haar/angular contraction, not absolute convergence/finiteness, not a distributional collision theorem, not cutoff removal, not family promotion, and not terminal D7 closure.

## Next gate if PASS

Preregister a source-faithful projected collision/integrability diagnostic that uses the validated `t^(+)`, `t^(-)`, and `d` objects without replacing the published spectral i-epsilon by an artificial beta shift; retain exact invariant-projector constraints and explicit controls distinguishing individual branches, their sum, and the standard EPRL object.
