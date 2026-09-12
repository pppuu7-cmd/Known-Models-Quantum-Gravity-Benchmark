# KMQGB front / ledger delta — Iter438-440 — 2026-09-12

This file is the authoritative delta to `recovery/CURRENT_BENCHMARK_FRONT.md` for the Iter438-440 causal-EPRL/Toller frontier. It does not alter RQIR Core v1.0 or authorize terminal D7.

## Canonical gate status

- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S2: `NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`
- Candidate Gravity: inactive / not authorized
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`: forbidden while S2-S4 remain open

## Iter438 corrected terminal result

Initial run `34709760371` was implementation/control-invalid only. Corrected source-admissibility validator commit: `ae8e5a1590b29eb23f428a81658b34173108c0f6`.

Corrected run `34709968631`; artifact `lqg-iter438-summary`, artifact id `10302288437`, digest `sha256:945f6998dbfa9a4e21bf2317b8dc60ab1ad0fa486a9f369513081712f05cd087`.

Result: 12/12 lanes valid, 0/12 globally supported exact invariant-projector magnetic assignments. Classification: `SOURCE_BACKED_SLOW_OBSTRUCTION_KILLED_BY_EXACT_INVARIANT_PROJECTOR`.

Interpretation: the Iter435/437 slow envelope obstruction does not survive the exact invariant projector for the one frozen source-backed Lorentzian boundary-spin completion. This materially narrows D7-S2 but is not full Haar/angular causal-vertex finiteness and does not close D7-S2.

## Iter439 terminal result

Frozen source object: gamma-simple minimal-channel individual Toller branches from Bianchi-Chen-Gamonal Eq. (46), `gamma in {7,8}`, source spins `j in {2,5}`, every allowed integer `m`, plus/minus branches, beta grid `[2,3,4,6,8,10]`.

The first workflow construction had a matrix-expansion infrastructure defect. Mechanical repair commit: `0f16e65ebad11b7ffa0512cf129dc40733fedaa5`; frozen science unchanged.

Authoritative repaired run `34710486745`; aggregate artifact id `10302933351`; digest `sha256:6fe5d72ffd5feb8a9cf42ce89d52125958ee680d58fbb0f90f450cb16772e9aa`.

Result: 64/64 lanes valid; classification `SOURCE_TOLLER_FINITE_BETA_ASYMPTOTIC_REALIZED_ON_FROZEN_GRID`. Maximum standard/tight complex difference `2.5735369674468285e-16`; maximum `|R(10)-1|=2.2672690169756038e-08`; maximum effective-exponent error `6.076071503713365e-07`.

Interpretation: branch-level published finite-beta/large-beta Toller source formula is numerically realized on the frozen grid. This validates a source-convention prerequisite, not collision-distribution theory or full-vertex convergence.

## Progress rubric delta relative to post-Iter437 baseline

Working research metric only, not formal gate state and not probability of a terminal classifier:

`D2 82% (Delta 0 pp) -> D4 68% (Delta 0 pp) -> D7 52% (Delta +4 pp) -> overall 65% (Delta +2 pp)`.

Rationale: +3 pp D7 credit for exact removal of all 12 frozen local-closure survivors by the corrected global invariant projector; +1 pp D7 credit for validated source-faithful finite-beta Toller asymptotics needed for the next noncompact gate. No D2/D4 credit because coverage/global-stack objects remain open.

## Iter440 active gate

Preregistration: `recovery/ITER439_RESULT_AND_ITER440_PREREG_TOLLER_RECOMBINATION_2026-09-12.md`.

Purpose: validate the full Eq. (45)/(46) finite-beta source normalization/phase and exact source identity `t^(+) + t^(-) = d`, which Iter439 did not test because it divided out beta-independent gamma prefactors.

Frozen production matrix: 32 lanes = `gamma in {7,8}` x `j in {2,5}` x every allowed integer `m`; each lane evaluates beta `[0.5,1,2,4,8]` at 80 and 120 decimal digits with frozen scaled identity threshold `1e-30` and cross-precision threshold `1e-35`.

Launch commit: `e7b675c21c39589bea6ba8c61312e52980980e88`.
Actions run: `34712981480`.
At launch the useful matrix is queued; no scientific classification is authorized before the aggregate.

## Next permitted dependent gate

Only if Iter440 terminally validates the full branch recombination identity, preregister a source-faithful projected Feynman-i-epsilon/collision-integrability diagnostic that keeps individual Toller branches, their sum, and the standard EPRL object distinct and preserves exact invariant-projector controls.

Do not replace the published spectral i-epsilon prescription by an artificial `beta+i*epsilon`, do not infer fixed-causal-sector cancellation from `T(+)+T(-)=D`, and do not launch terminal D7 or Candidate Gravity.
