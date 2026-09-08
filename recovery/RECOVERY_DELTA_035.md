# RECOVERY DELTA 035 — Multi-Configuration / Intervention Rigidity

Date: 2026-09-08  
KMQGB iteration: 035

## New authority

Wave 12 terminally closed `5/5 = 100%`.

Created:

- `protocol/INTERVENTION_CONFIGURATION_RIGIDITY.md`;
- `code/intervention_design_reference.py`;
- `twelfth_wave/result.json`.

## Frozen design rule

Controlled source/detector variables are design variables when known, not free nuisance parameters.

Dynamics parameters remain shared across configurations; only physically justified configuration-local nuisances may vary independently.

Adding a configuration with `k` physical coordinates obeys

`Delta d_perp = k - Delta rank(J_union)`.

Interventions are selected prospectively by post-comparator rank, projected singular values or projected SNR.

## External RQIR K3 pre-check

Created `external_rqir_checks/iter590_k3_local_analyticity_precheck.md`.

KMQGB independent algebra indicates that the isolated local MSSC K3 coefficient, coming from a local minimally coupled scalar kernel with no internal propagator/nonanalytic form factor, should have zero standalone hard-channel branch discontinuity. This remains **non-authoritative for RQIR** until checked under the exact frozen RQIR routing/continuation.

The larger `G K3 G` composite and K1^3 linked-cut origin are not classified away by this pre-check.

## External state

RQIR authority remained Iter590/readiness `24%` during this iteration. No active/queued Actions were observed and no unjustified heavy KMQGB job was launched.
