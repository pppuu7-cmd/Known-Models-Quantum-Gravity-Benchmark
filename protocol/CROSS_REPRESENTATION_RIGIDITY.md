# Cross-Representation Rigidity

**Status:** frozen methodology / no Candidate Gravity promotion.  
**Purpose:** test one parent dynamics simultaneously across in-out scattering, in-in/CTP causal response and relational/quantum-channel observables without cloning shared physical parameters per representation.

## 1. Motivation

Amplitude-only parent-principle searches are repeatedly either

- too broad to select a low-dimensional hierarchy;
- too scoped to be a complete gravity parent; or
- already contained in string/bootstrap/dual-resonance comparator families.

A stronger test is to demand that **different representations of the same parent physics share the same dynamics parameters**.

Example representation blocks:

- `R_S`: in-out graviton scattering/helicity amplitude data;
- `R_CTP`: retarded, symmetric and ordered in-in kernels;
- `R_REL`: relational proper-time/phase/tidal/quantum-channel observables;
- optional `R_SOFT`: soft/tidal/universality gravity-attribution anchors.

Cross-representation consistency is not automatically KG novelty. It is a rigidity mechanism.

## 2. Shared versus representation-local parameters

Let the parent dynamics parameters be `theta`, shared by every representation in which the parent theory says they appear.

Each representation may also have legitimate local nuisance/state/detector/calibration parameters `phi_a`.

For block `a`, write the physical prediction

`c_a(theta, phi_a)`.

Forbidden: replace one shared `theta` by independent copies `theta_a` merely to improve the fit.

## 3. Stacked Jacobian

At a common expansion/profile point define

`S_a = partial c_a / partial theta`,

`L_a = partial c_a / partial phi_a`.

The correctly shared stacked comparator Jacobian is

`J_shared = [ S_1  L_1   0   ... ;
              S_2   0   L_2  ... ;
              ... ]`.

For diagnostic comparison, an artificially independent representation fit uses

`J_sep = blockdiag([S_1,L_1], [S_2,L_2], ...)`.

The shared tangent is a subspace of the independently retuned tangent.

## 4. Cross-representation shared-parameter gain

Define

`R_XR = rank(J_sep) - rank(J_shared) >= 0`.

For fixed stacked physical dimension `m`, the corresponding local comparator-complement gain is

`d_perp,shared - d_perp,sep = R_XR`.

Thus `R_XR>0` measures additional consistency directions created purely by requiring one parent parameter set to work across representations.

This is the representation analogue of cross-order shared-parameter rigidity.

## 5. Covariance and whitening

Use the full stacked covariance

`Sigma_XR = Cov(col(y_1,y_2,...))`,

including cross-representation correlations when the same numerical ensemble, source uncertainty, calibration, state preparation or detector model induces them.

Whiten and project exactly as in `RESIDUAL_SPACE_GEOMETRY.md`:

`A_XR = Sigma_XR^(-1/2) J_shared`,

`Pi_XR = I - A_XR A_XR^+`,

`COR_XR = Pi_XR Sigma_XR^(-1/2) r_XR`.

Do not infer extra significance by treating correlated representations as independent.

## 6. Representation-holdout test

A strong prospective split can use one representation for parameter calibration and another as a no-retuning prediction.

Examples:

- fit shared parent scale/coupling using selected four-graviton helicity blocks, predict a CTP response shape;
- fit low-energy causal response, predict a cross-regime scattering ratio;
- fit scattering plus CTP, hold out a relational quantum-channel observable.

Shared parent parameters may not be retuned on holdout. Use the predictive-covariance machinery from `PREDICTIVE_HOLDOUT_RIGIDITY.md`.

## 7. Representation-map completeness

Different representations are not assumed identical by notation.

Before stacking, each block must have a parent derivation that fixes

- renormalization convention and shared physical parameters;
- in-out versus in-in boundary/state prescription;
- analytic continuation or real-time contour where required;
- LSZ/amputation/contact conventions for scattering;
- detector/source integration for relational/channel blocks;
- kinematic projection/rank completion.

A missing map is `BLOCKED_REPRESENTATION_MAP`, not zero.

## 8. Generic-QFT relations are not KG fingerprints

The following are useful consistency checks but not gravity-specific novelty by themselves:

- optical theorem/unitarity cuts;
- Kallen-Lehmann positivity;
- Kramers-Kronig/retarded analyticity;
- KMS/FDR in an applicable equilibrium state;
- generic Schwinger-Keldysh normalization/causality identities.

A KG claim requires a **specific low-freedom cross-representation relation** that remains after full comparator profiling.

## 9. Comparator requirements

Apply cross-representation profiling to the strongest parent comparators able to define the same blocks:

- full C5 perturbative quantum GR/EFT;
- string/string-like UV completion where the representation exists;
- asymptotic-safety/fixed-point quantum effective action where the representation exists;
- ordinary quantum mediator/open-system C4/C6 alternatives;
- classical stochastic/CQ models for causal/noise blocks.

If a comparator lacks a required representation as a genuine missing object, mark that comparison `BLOCKED`; do not assume zero.

## 10. Candidate design implication

A promising future KG parent should aim for

`few shared theta -> many complete blocks across order x configuration x representation`.

The useful quantity is not the number of observables but the post-comparator dimension and conditioning after all shared parameters and legitimate local nuisances are accounted for.

## 11. Machine-record additions

Future records should include

- `representation_id` per observable block;
- `shared_parent_parameter_ids`;
- `representation_local_parameter_ids`;
- `representation_map_ref`;
- `cross_representation_covariance_ref`;
- `R_XR` or equivalent rank audit;
- representation-level training/holdout role.

## 12. Promotion status

Cross-representation rigidity is a methodology gate. It does not by itself promote a Candidate Gravity ansatz or change external RQIR readiness.
