# Predictive / Holdout Rigidity for Future Candidate Gravity

**Status:** frozen methodology / pre-ansatz anti-overfitting rule.  
**Purpose:** test whether one shared parent dynamics predicts new response orders/configurations without post-hoc retuning.

## 1. Prospective split

Before inspecting the residual in the target blocks, partition complete physical observables/configurations/orders into

- training/calibration blocks `T`;
- held-out prediction blocks `H`.

The split and allowed local nuisance structure must be pre-registered.

Suitable holdouts include one response order, source/detector geometry, frequency/proper-time band, source species/composition, polarization/orientation, or state-preparation setting.

## 2. Fit only on training blocks

Fit shared dynamics/comparator parameters using only `T`:

`theta_hat_T = argmin_theta L_T(theta)`.

The held-out prediction is

`c_H^pred = c_H(theta_hat_T)`.

Shared parent parameters are **not** re-fitted on `H`.

Only explicitly declared holdout-local nuisance parameters may be profiled in `H`, and their existence/priors must come from the generative model rather than residual inspection.

## 3. Predictive residual

Define

`r_H^pred = y_H - c_H(theta_hat_T)`.

The predictive score must propagate both held-out noise and uncertainty/correlation induced by fitting the shared parameters on `T`.

For an independent-block linear-Gaussian model,

`Cov(theta_hat_T) = (J_T^T Sigma_TT^(-1) J_T)^+`

on the identified subspace and

`Sigma_pred,H = Sigma_HH + J_H Cov(theta_hat_T) J_H^T`.

Then

`chi2_pred = (r_H^pred)^T Sigma_pred,H^+ r_H^pred`.

## 4. Exact correlated linear-Gaussian reference

Let

`y_T = J_T theta + eps_T`,

`y_H = J_H theta + eps_H`,

with joint noise covariance blocks `Sigma_TT, Sigma_TH, Sigma_HT, Sigma_HH`.

For generalized least squares on training data, define

`M = (J_T^T Sigma_TT^(-1) J_T)^+ J_T^T Sigma_TT^(-1)`.

Then

`theta_hat_T = theta + M eps_T`

on the represented identifiable subspace, and the held-out prediction residual is exactly

`e_H = eps_H - J_H M eps_T`.

Therefore

`Sigma_pred,H = Sigma_HH`

`+ J_H M Sigma_TT M^T J_H^T`

`- J_H M Sigma_TH`

`- Sigma_HT M^T J_H^T`.

When `Sigma_TH=0`, this reduces to the familiar held-out noise plus propagated parameter covariance.

This formula shows that shared numerical/systematic noise can either increase or reduce predictive uncertainty through the cross terms. Do not claim independent holdout evidence while ignoring such correlations.

For nonlinear models or singular/complex hierarchical nuisance structures, derive the predictive distribution from the full joint generative model, validated linearization, bootstrap/Monte Carlo, or equivalent authority rather than forcing this linear formula outside its domain.

## 5. Predictive rigidity versus flexible retuning

A flexible comparator may fit the joint dataset only by effectively assigning separate shared-parameter values to different blocks.

Distinguish:

1. **predictive test:** shared parameters fixed by `T`, predict `H`;
2. **retuned fit:** allow the comparator to re-optimize shared parameters including `H`.

A large improvement available only after forbidden/shared-parameter retuning is evidence of weak parent rigidity, not evidence against a properly declared model with genuine local nuisances.

## 6. Leave-one-block-out validation

For blocks `a=1,...,A`, perform leave-one-configuration/order-out (LOCO) validation:

- fit shared parameters on all blocks except `a`;
- predict block `a` without shared-parameter retuning;
- compute its predictive residual/score with the full covariance model.

Aggregate diagnostics may include maximum standardized predictive residual, held-out predictive log scores where statistically valid, interval coverage, and stability of fitted shared parameters across folds.

## 7. Training identifiability prerequisite

A holdout test is weak if training data do not constrain the shared parameters.

Before interpreting `H`, audit the training projected/Fisher singular values or equivalent identifiability measure.

If a shared direction is unconstrained by `T`, broad holdout predictions are expected and the fold does not supply a sharp rigidity test.

## 8. Candidate Gravity use

The strongest future KG test is cross-order/cross-configuration prediction:

- fit a small number of KG parent parameters using lower-order/calibration blocks;
- predict higher-order/ordered/channel/tidal blocks;
- prohibit independent coefficient retuning for each predicted block.

A KG model with many independent coefficients that merely fits every block separately has low rigidity even if the global chi-square is good.

## 9. Comparator fairness

Apply the same predictive protocol to Candidate Gravity and every comparator.

- same training/holdout split;
- only genuinely shared/local parameters for each model;
- same physical observable/covariance authority;
- no undeclared extra retuning freedom for KG or artificial penalties for comparators.

## 10. Relation to COR/global profiling

Predictive holdout is complementary to residual-space geometry.

- COR asks whether a residual is locally outside the comparator tangent;
- holdout asks whether parameters fixed elsewhere predict the new block without retuning.

A strong future KG residual should ideally survive **both**.

## 11. Promotion guardrail

A good holdout score does not by itself promote Candidate Gravity. The full Candidate Gravity Promotion Gate remains mandatory.
