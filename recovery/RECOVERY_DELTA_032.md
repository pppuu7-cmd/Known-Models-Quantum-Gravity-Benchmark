# RECOVERY DELTA 032 — Optimal Comparator-Null Observable Design

Date: 2026-09-08  
KMQGB iteration: 032

## New authority

Wave 9 terminally closed `5/5 = 100%`.

Created:

- `protocol/OPTIMAL_COMPARATOR_CONTRASTS.md`;
- `code/optimal_comparator_contrasts_reference.py`;
- `ninth_wave/result.json`.

## Frozen formulas

Exact comparator-null contrast:

`J_union^T w=0`.

Covariance-optimal signal contrast:

`w_opt proportional to Sigma^(-1/2)Pi_perp Sigma^(-1/2)s`.

Maximum local post-comparator SNR:

`||Pi_perp Sigma^(-1/2)s||`.

Observable augmentation:

`Delta d_perp = k - Delta rank(J_union)`.

## Design consequence

Future KG observables are selected by post-comparator dimension, projected conditioning and projected SNR rather than raw sensitivity.

No Candidate Gravity ansatz/readiness promotion.
