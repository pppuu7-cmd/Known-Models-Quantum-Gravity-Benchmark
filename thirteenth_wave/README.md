# KMQGB Thirteenth Wave — Predictive / Holdout Rigidity

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–12:** terminal and immutable.  
**Status:** **TERMINAL 5/5 = 100%**.  
**Purpose:** test whether one shared parent dynamics predicts unseen orders/configurations without post-hoc shared-parameter retuning.

| # | Target | Terminal result | State |
|---|---|---|---|
| T13-01 | prospective train/holdout split | freeze prediction blocks before residual inspection | `PASS_RQIR_GATE` |
| T13-02 | no shared-parameter holdout retuning | shared parent parameters fit on training only; only declared local nuisance may vary | `PASS_RQIR_GATE` |
| T13-03 | predictive covariance | propagate parameter uncertainty and training/holdout cross-covariance | `PASS_RQIR_GATE` |
| T13-04 | leave-one-block-out validation | freeze LOCO/leave-one-order-out predictive stability test | `PASS_RQIR_GATE` |
| T13-05 | training identifiability / predictive certificate | require training to constrain shared parameters before interpreting holdout residuals | `PASS_RQIR_GATE` |

**Thirteenth-wave terminal coverage: 5/5 = 100%.**

## Authoritative protocol

`protocol/PREDICTIVE_HOLDOUT_RIGIDITY.md`

Reference code:

`code/predictive_holdout_reference.py`

## Central predictive rule

Fit shared parameters only on training blocks `T`:

`theta_hat_T = argmin L_T(theta)`.

Predict holdout `H` without shared-parameter retuning:

`r_H^pred = y_H - c_H(theta_hat_T)`.

Only pre-declared holdout-local nuisance may be profiled.

## Exact correlated linear-Gaussian reference

For linear blocks

`y_T=J_T theta+eps_T`,

`y_H=J_H theta+eps_H`,

with GLS map

`M=(J_T^T Sigma_TT^(-1)J_T)^+ J_T^T Sigma_TT^(-1)`,

held-out error is

`e_H=eps_H-J_H M eps_T`.

Therefore

`Sigma_pred,H = Sigma_HH`

`+ J_H M Sigma_TT M^T J_H^T`

`- J_H M Sigma_TH`

`- Sigma_HT M^T J_H^T`.

This explicitly handles shared training/holdout noise/systematics.

## Candidate Gravity design lesson

A genuinely rigid future KG model should fit a small number of shared parent parameters on lower-order/calibration blocks and **predict** higher-order/channel/tidal/other configurations without introducing fresh coefficients for each held-out block.

A good joint fit obtained only after re-tuning shared dynamics on every new block is weak evidence of one parent theory.

## Relation to COR

- COR tests local geometric separation from comparator tangents;
- predictive holdout tests out-of-sample parent rigidity.

The strongest future KG residual should survive both.

## Promotion guardrail

This wave is methodology only. No Candidate Gravity ansatz/readiness increase is authorized.
