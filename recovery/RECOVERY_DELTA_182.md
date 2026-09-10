# KMQGB Recovery Delta 182

**Date:** 2026-09-10  
**Scope:** Paper-IV D2/D4/D7 global closure audit under RQIR Core v1.0 FROZEN.

## New result

The three global open gates were converted from qualitative blockers into an explicit executable dependency structure.

### D2

`NOT_CLOSED`.

Three mandatory major-framework rows remain incomplete:

- O-AS: complete same-realization `A_s+A_t+A_u+A4` amplitude + full error/comparator certificate missing;
- O-LQG: controlled EPRL/Regge -> Area-Regge/area-metric parity/gamma ancestry missing;
- O-CFS: first explicit normalized non-Einstein gravity correction tensor/coefficient vector missing.

### D4

Advanced from `NOT_CLOSED` to:

`PARTIAL_MATRIX_FROZEN__NOT_CLOSED`.

New authority:

- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json`
- `code/paper_iv_global_gate_validator.py`

The matrix explicitly represents undefined residual rows as undefined/BLOCKED. Zero-fill is forbidden. BLOCKED rows contribute zero exclusion evidence.

### D7

`NOT_CLOSED`.

The new validator enforces that no terminal Paper-IV decision can be authorized before D2 and D4 pass. It also forbids `NEW_REQUIRED` while any required framework remains BLOCKED or lacks complete exclusion evidence.

## Literature audit result

### AS

arXiv:2602.21285 supplies an explicit contact-amplitude sector, while arXiv:2603.10168 supplies the Lorentzian mediated scattering target and identifies the complete amplitude as `A_s+A_t+A_u+A4`. Cross-paper composition is still forbidden because a same-realization trajectory/normalization/truncation/error map is absent; the contact paper itself calls for a more complete momentum-dependent propagator/all-vertex treatment before a final amplitude verdict.

### LQG

Area-Regge/area-metric continuum and parity/RG machinery is strong. However arXiv:2507.02034 explicitly treats non-metric masses as independent because they are not currently computable from spin foams and assumes an intermediate EFT regime. This blocks a same-realization identification `gamma_EPRL = gamma_AM(mu)` without a derived coarse-graining/normalization map.

### CFS

arXiv:2605.30199 gives an Einstein-Dirac iff continuum result; arXiv:2607.13871 supplies a systematic regularization-length correction generator; arXiv:2507.09633 supplies a tensor hierarchy but states rank-two Einstein equations as expected rather than giving the required normalized first beyond-Einstein tensor. O-CFS therefore remains object-limited.

## Stable firewall

- R1 = 100%.
- R2 = 100%.
- R3 Candidate Gravity scientific readiness = 24% unchanged.
- legacy R4 = 45%, paused/conditional.
- PF1 = 5/5 terminal.
- Closure Wave 02 = 0/3 terminal.
- Paper IV = `NOT_YET_AUTHORIZED`.
- `NEW_REQUIRED` unauthorized.
- RQIR Core v1.0 unchanged.
- heavy compute IDLE; current blockers are analytic/provenance/normalization/composition.

## Exact continuation

The next closure event must be one of:

1. `O_AS_COMPLETE` same-realization amplitude certificate;
2. `O_LQG_COMPLETE` EPRL-to-area-metric parity/gamma ancestry certificate;
3. `O_CFS_COMPLETE` explicit normalized correction tensor plus comparator.

Until one of those objects becomes available or is derived, further numerical scanning cannot close D2/D4/D7.
