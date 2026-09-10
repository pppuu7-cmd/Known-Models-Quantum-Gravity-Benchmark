# Nonlocal QG weak-field real-data domain and EFT-nuisance projection audit — Iter248

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `NONLOCAL_QG`  
**Fixed branch:** Sangy–Burzillà–Giacchini–de Paula Netto exponential weak-field models, `f_s(Box)=exp[(-Box/mu_s^2)^{N_s}]`.

## Question
Can the Iter232–234 finite-parameter/full-shape weak-field object be projected into an existing real-data likelihood while preserving the same realization, observable domain, local-EFT nuisance quotient, provenance, and propagated uncertainty?

## Authority refresh
Sangy et al., Phys. Rev. D 113, 104006 (2026), DOI 10.1103/8hdr-br8l, derives effective sources, mass functions, Newtonian potentials and leading logarithmic quantum corrections for the exponential `f_s` family. It supplies an analytic correlated radial shape and identifies oscillatory structure for `N_s>1`; it is a theory/phenomenology construction, not a published fit to a frozen experimental likelihood.

Beckering Vinckers, de la Cruz-Dombriz & Mazumdar, Class. Quantum Grav. 42, 065001 (2025), DOI 10.1088/1361-6382/adb08c, derives nonlocal single-graviton-exchange potentials/contact-term smearing and quotes the established short-distance Newtonian-potential bound on the nonlocal scale. This is useful evidence that a laboratory weak-field domain is physically relevant, but it does not provide the required GF_N full-shape likelihood with nuisance covariance and propagated model error.

Older IDG weak-field papers similarly provide potentials, Lense–Thirring effects, lensing/scattering or proposed table-top observables. They are not a substitute for a same-realization real-data full-shape data capsule.

IR nonlocal cosmology (e.g. inverse-d'Alembertian RR/RT/Deser-Woodard-type models) is a materially different branch. Cosmological data fits from that branch must not be spliced onto the UV/weak-field exponential GF_N realization without an explicit action/equivalence map.

## Frozen-domain finding
The current authority set therefore supports three distinct statements:

1. `PASS_SCOPED_ANALYTIC_FULL_SHAPE_WEAK_FIELD_OBJECT`: the fixed GF_N branch has a finite-parameter correlated radial weak-field shape.
2. `PASS_SCOPED_PHYSICAL_DOMAIN_EXISTS`: short-distance/table-top Newtonian tests provide a genuine physical observation domain for departures from the 1/r potential.
3. `BLOCKED_REAL_DATA_PROJECTION`: no audited published same-realization package was located that maps the GF_N full radial shape into raw/binned real data with the experiment response, covariance, local-EFT/background nuisance basis, prospectively fixed fit range, and propagated theory/remainder uncertainty.

The third statement is a bounded authority result through 2026-09-10, not a proof of nonexistence.

## EFT/nuisance quotient requirement
A decision-relevant fit must not compare the nonlocal shape against a bare GR curve only. At minimum it must freeze the measurement response and calibration model, the allowed local analytic/EFT nuisance basis, the covariance including correlated systematics, the fit window before looking at residual significance, and the truncation/remainder assigned to the weak-field approximation. The nonlocal residual is decision-relevant only after projection orthogonal to this nuisance span.

A one-number lower bound on `mu` is not equivalent to this full-shape quotient. It can be retained as a scoped parameter constraint but cannot close D4 for the branch.

## Same-realization discipline
No transfer is authorized from IR nonlocal cosmology fits, from a different entire-form-factor class, or from generic Yukawa fifth-force constraints unless the corresponding observable kernel is explicitly mapped to the fixed GF_N response. Such transfers would violate frozen D6.

## Iter248 disposition
`PARTIAL_STRONG_NONLOCAL_FULL_SHAPE_BRANCH__PHYSICAL_WEAK_FIELD_DOMAIN_IDENTIFIED__SAME_REALIZATION_REAL_DATA_RESPONSE_COVARIANCE_EFT_NUISANCE_AND_PROPAGATED_ERROR_CAPSULE_NOT_LOCATED`.

Family status remains `PARTIAL_SUBFAMILY_ONLY`; family residual remains `UNDEFINED`. This is not a scientific FAIL and does not authorize `NEW_REQUIRED`.

## Heavy compute
`IDLE`. Synthetic refinements cannot manufacture an authenticated experimental response/covariance or same-realization causality/unitarity certificate.

## Next gate
`NONLOCAL_QG_FULL_MOMENTUM_CROSS_ORDER_FUNCTIONAL_RIGIDITY_AND_MATERIAL_BRANCH_EXHAUSTION_CERTIFICATE`.

The next high-information pass should test whether the finite-dimensional weak-field shape survives cross-order/full-momentum completion within one action, and separately census materially distinct weakly-nonlocal branches. A failure in one branch must not be promoted to the family without scope proof.
