# Cross-Order Rigidity for Future Candidate Gravity

**Status:** frozen methodology layer / pre-ansatz design rule.  
**Purpose:** exploit the fact that one parent dynamics must use the same physical parameters across multiple response orders, channels and attribution sectors.

## 1. Stacked observable

Let response/order/channel blocks be indexed by `ell=1,...,L`.

After exact physical constraints at each block, define

`y_stack = col(y_1,...,y_L)`

with full block covariance

`Sigma_stack = [[Sigma_11,...,Sigma_1L],...,[Sigma_L1,...,Sigma_LL]]`.

Cross-order covariance must be retained when the same source, simulation, calibration, parent coefficients or detector systematics affect several blocks.

## 2. Shared comparator parameter map

Let the comparator have truly shared parent parameters `theta_s` and possibly block-specific nuisances `theta_ell`.

The correct stacked comparator is

`c_stack(theta_s,theta_1,...,theta_L)=col(c_1,...,c_L)`.

Its Jacobian is built with **one column per genuinely shared parameter**, not one independent copy per order.

Artificially duplicating a shared coupling/Wilson coefficient/state parameter separately at every order enlarges the comparator manifold and destroys real cross-order consistency. Conversely, genuinely independent detector/calibration nuisances must not be forced to be shared.

Parameter incidence must therefore be frozen from the parent dynamics/generative model before profiling.

## 3. Cross-order complement dimension

For invertible whitening, rank is unchanged, so algebraically

`d_perp,stack = m_total - rank(J_stack)`.

Analyzing blocks separately would yield

`sum_ell d_perp,ell = m_total - sum_ell rank(J_ell)`.

Define the **shared-parameter rigidity gain**

`R_shared = d_perp,stack - sum_ell d_perp,ell`

`= sum_ell rank(J_ell) - rank(J_stack) >= 0`.

`R_shared>0` means the same comparator parameters cannot independently fit each response order; cross-order relations create additional comparator-orthogonal directions.

This is one of the most important positive design priors for future KG.

## 4. Local cross-order contrasts

Use the full stacked covariance and Jacobian in the existing COR/optimal-contrast machinery:

`A_stack = Sigma_stack^(-1/2) J_stack`,

`Pi_perp,stack = I - A_stack A_stack^+`.

A cross-order contrast `w` satisfies

`J_stack^T w=0`.

Its components may live in different perturbative orders/channels. This is desirable: it tests one parent relation rather than one isolated observable.

## 5. Exact global invariants when scaling is known

Some shared-parameter relations can be removed **globally**, not merely by local tangent projection.

### Example: one shared amplitude

If a comparator predicts

`c1 = a f1`,

`c2 = a^2 f2`,

then the exact invariant

`I = c2 f1^2 / (c1^2 f2) = 1`

is independent of the unknown shared amplitude `a`.

A measured/model value `I != 1` cannot be repaired by retuning `a`.

### General monomial parameter scaling

Suppose

`c_i = A_i product_j theta_j^(P_ij)`.

Then

`log(c_i/A_i) = sum_j P_ij log theta_j`.

For any vector `u` satisfying

`u^T P = 0`,

the multiplicative invariant

`I_u = product_i (c_i/A_i)^(u_i)`

is parameter-independent and equals its parent-predicted constant.

These exact invariants are preferred over local COR when the scaling assumptions are exact and the observable domain avoids zero/sign/branch ambiguities.

## 6. Cross-order covariance

Do not treat response orders as statistically independent by default.

Shared theory/numerical/systematic sources may induce cross-block covariance. Use the full `Sigma_stack`.

Deterministic common parameters belong in `J_stack`; stochastic shared uncertainty belongs in `Sigma_stack`. Do not double-count the same generative uncertainty in both without an explicit hierarchical model.

## 7. Cross-order Candidate Gravity identifiability

For future KG stacked Jacobian `J_KG,stack`, define

`B_KG,stack = Pi_perp,stack Sigma_stack^(-1/2) J_KG,stack`.

Useful design diagnostics:

- robust rank of `B_KG,stack`;
- smallest nonzero singular value;
- change relative to each order alone;
- principal angles to the union comparator tangent;
- exact global invariants when available.

A future KG architecture is especially promising when a **small number of shared KG parameters predicts many response blocks**, while comparator parameters are already constrained by lower orders.

## 8. Observable-addition rule across orders

Adding a new response-order block with `k` physical coordinates gives

`Delta d_perp = k - Delta rank(J_union)`.

Cross-order augmentation is preferred when shared comparator parameters make `Delta rank(J_union)` small.

Thus a new order/channel is valuable not because it is higher order, but because it contributes more physical dimensions than new comparator freedom.

## 9. Parent-response completeness remains mandatory

Every stacked order must first satisfy `protocol/PARENT_KERNEL_RESPONSE_COMPLETENESS.md`.

Do not create cross-order rigidity from comparing a complete lower-order response with an incomplete higher-order response.

Frozen pipeline:

`complete response at each order`

`-> exact physical/Ward/contact reduction`

`-> stack orders with shared parameter incidence`

`-> full covariance`

`-> full comparator quotient / exact invariants`

`-> global profiling`.

## 10. Candidate Gravity design consequence

A future KG ansatz should preferentially have a small set of shared parent couplings/functions that simultaneously predicts

- lower-order force/phase/response;
- ordered/noise structure;
- higher-order source/contact response;
- channel/tidal/soft gravity-attribution sectors.

The target novelty is a **cross-order consistency relation** that survives full C5 and comparator profiling, not a new independent coefficient at every order.

## 11. Promotion guardrail

This protocol does not promote an ansatz. It defines where a robust relation may be found and must be combined with the Candidate Gravity Promotion Gate.
