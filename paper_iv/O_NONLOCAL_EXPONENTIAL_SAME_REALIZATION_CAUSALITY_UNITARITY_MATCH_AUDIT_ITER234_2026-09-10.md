# Nonlocal exponential full-shape — same-realization causality/unitarity match audit — Iter234

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `NONLOCAL_QG`  
**Active branch:** Sangy–Burzillà–Giacchini–de Paula Netto exponential weak-field models

## Question

Can the scoped full-shape result from Iter232–233 be combined, without cross-realization splicing, with an existing nonlocal-gravity causality and interacting-unitarity certificate?

## Fixed full-shape realization

The 2026 Phys. Rev. D Newtonian-limit study uses spin-sector form factors

`f_s(Box) = exp[(-Box/mu_s^2)^{N_s}]`

and commonly studies the restricted `GF_N` case `N_0=N_2=N`, `mu_0=mu_2=mu`.

Because these entire form factors have no finite complex zeros, the linearized propagator does not acquire extra ghost poles from zeros of `f_s`. The paper derives regular weak-field potentials/effective sources and a correlated radial shape.

This supports:

`PASS_SCOPED_LINEARIZED_NO_EXTRA_FORM_FACTOR_ZERO_POLES_AND_FULL_SHAPE_WEAK_FIELD_CONTROL`.

It does **not** by itself establish a nonperturbative/interacting S-matrix unitarity certificate or global-causality theorem for the same model.

## Comparison with the 2026 Gödel/CTC result

Zhao, Modesto and Bambi (2026) study a different weakly nonlocal construction. Their quantum-renormalizable class is parameterized through functions `H_i` and in the explicit analysis uses

`H(x) = alpha * integral_0^{p(x)} dz [1-exp(-z^n)]/z`,

with polynomial `p(x)` and additional infrared/renormalizability constraints.

They show that Gödel-type vacuum solutions with closed timelike curves exist for a specific but large subset of these form factors, while other choices do not satisfy the corresponding existence conditions. In particular the result depends on the detailed `H_2`/polynomial class.

The audited authority does not provide an equivalence map identifying the Sangy et al. simple `f_s(Box)=exp[(-Box/mu_s^2)^{N_s}]` GF_N realization with the particular `H_2,p(x)` realization admitting the Gödel solution.

Therefore RQIR D6 forbids the inference:

`Sangy full-shape observable + Zhao Gödel causality status = one realization`.

Classification:

`BLOCKED_CROSS_REALIZATION_CAUSALITY_TRANSFER__NO_EXPLICIT_FORM_FACTOR_EQUIVALENCE_MAP`.

## What can be concluded about causality

Only a weaker family statement is justified:

- global causality is **not automatically guaranteed** by broad nonlocal renormalizability/unitarity conditions;
- different entire-form-factor realizations can have materially different causality behavior;
- therefore any physical full-shape branch must carry its own causality certificate or an explicit equivalence/reduction map to one.

This strengthens the need for form-factor-specific disposition but supplies no scientific FAIL for the GF_N branch.

## Interacting unitarity boundary

The absence of new linearized ghost poles is a propagator-spectrum control, not a complete interacting unitarity proof. The 2024 spectral/Källén–Lehmann analyses support positive spectral structure and standard local limits for important classes of entire form factors, but an explicit same-action map to the exact GF_N weak-field branch plus its full interacting gravity observable is not frozen here.

Hence:

`LINEARIZED_SPECTRUM_CONTROL = PASS_SCOPED`  
`INTERACTING_SAME_REALIZATION_UNITARITY = OPEN`

## Iter234 result

The Iter232–233 full-shape direction remains scientifically valid as a **scoped identifiability object**, but it cannot yet be promoted to a physically complete nonlocal residual because the exact same realization lacks a bound global-causality/interacting-unitarity/error certificate.

Status:

`PARTIAL_STRONG_NONLOCAL_FULL_SHAPE_BRANCH__SAME_REALIZATION_CAUSALITY_AND_INTERACTING_UNITARITY_NOT_BOUND`.

Exact missing certificate:

`GFN_EXPONENTIAL_FIXED_ACTION_GLOBAL_CAUSALITY_PLUS_INTERACTING_UNITARITY_PLUS_PHYSICAL_FULL_SHAPE_DATA_COMPARATOR_ERROR_CERTIFICATE`.

## Paper III impact

No new transferable Paper-III failure class appears. This is another instance of the already-frozen same-realization/provenance rule.

`PAPER_III_REOPEN = NO`.

## Heavy compute

`IDLE` for the family decision. Numerical refinement of the synthetic holdout test cannot prove causality or interacting unitarity.

## Next information-gain decision

The nonlocal branch has now been advanced until its next blockers require either a physical data capsule or new same-realization causality/unitarity authority. Park this branch and reselect among the remaining Tier-1 families.

Highest-priority candidate for the next sweep: `STRING_MTHEORY_HOLOGRAPHY`, because its family-level blocker is now dominated by **material subfamily coverage/equivalence**, a census problem that can be reduced analytically without heavy compute.
