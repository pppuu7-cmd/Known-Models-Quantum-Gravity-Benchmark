# O-LQG Area-Metric Gamma-Running Bridge Audit

**Date:** 2026-09-10  
**KMQGB iteration:** 174  
**RQIR Core:** v1.0 FROZEN and unchanged.  
**Target:** CW2-02 / O-LQG `IDENTIFIABLE_RENORMALIZED_GAMMA_MATCH`.

## Question

Can the recent area-metric effective-gravity line supply the missing renormalized bridge between microscopic/spinfoam Immirzi structure and an observable Lorentzian low-energy parity-sensitive sector?

## New authority

Two recent works materially sharpen the route:

1. J. Borissova, B. Dittrich, A. Eichhorn, M. Schiffer, **Renormalization group flows in area-metric gravity**, arXiv:2507.02034 (2025): https://arxiv.org/abs/2507.02034
   - area-metric gravity is explicitly motivated by spin-foam quantum gravity;
   - the non-length/shape-mismatch sectors are evolved under RG flow;
   - parity symmetry does not generically emerge;
   - an RG flow for the Immirzi parameter is extracted, with beta-function zeros at vanishing and infinite Immirzi parameter.

2. B. Dittrich, **Gravitational wave signatures from area metric gravity**, arXiv:2608.16046 (2026): https://arxiv.org/abs/2608.16046
   - shift-symmetric linearized Lorentzian area-metric gravity is presented as arising in particular from spin foams and modified Plebanski theory;
   - the theory admits parity-violating terms controlled by the Barbero-Immirzi parameter;
   - gravitational-wave-like solutions and their electromagnetic detector coupling are derived;
   - polarized-light interferometry gives a detector-facing route to the parity/birefringence sector, though Planck-mass non-length modes make the nominal signal extremely weak.

The previously frozen microscopic authority remains Bianchi & Rincon-Ramirez, **Spinfoams, gamma-duality, and parity violation in primordial gravitational waves**, Phys. Rev. D 113, 124013 (2026), DOI 10.1103/qz89-26hk. It fixes an EPRL gamma-duality relation and a parity-sensitive primordial observable, while explicitly leaving the top-down derivation from the non-perturbative spinfoam amplitude to the effective action open.

## What is genuinely new

The area-metric line removes a stale version of the broad statement "there is no renormalized Immirzi flow or Lorentzian observable EFT route". There now exists a concrete effective programme with both:

`spin-foam-motivated area-metric RG -> running gamma`

and

`Lorentzian area-metric parity sector -> detector-facing GW/birefringence observable`.

Therefore the missing object should no longer be phrased as the existence of *any* gamma-running/effective-observable bridge.

## Same-realization firewall

This does **not** close CW2-02.

The frozen same-realization gate requires an explicit map between the realization supporting microscopic EPRL gamma-duality and the realization supporting the area-metric RG/detector sector. Shared use of the symbol `gamma`, shared spin-foam motivation, and parity sensitivity are insufficient.

The still-missing map must establish, with propagated uncertainty,

`M_EPRL->AM : {gamma_micro, W_gamma, boundary/state/regulator data} -> {gamma_AM(k), area-metric couplings, parity-sector normalization}`.

In particular, the audit does not find a published authority establishing that the running area-metric `gamma_AM(k)` is the same renormalized quantity as the `gamma_EFT` entering the Bianchi-Rincon-Ramirez GB/CS duality relation.

## Consequence for the Iter173 identifiability result

The Iter173 generalized observable

`q = 1/gamma_EFT - gamma_EFT - Delta_gamma`

remains rank-1 in `{gamma_EFT,Delta_gamma}`.

The area-metric programme supplies a plausible **independent theory prior/evolution law candidate** for gamma, and a separate Lorentzian observable channel, but it does not yet supply the parameter-identity theorem needed to insert that prior into the EPRL gamma-duality likelihood without a Frankenstein composition.

Thus no detector forecast is authorized yet.

## Updated minimum decisive object

The O-LQG closure object is sharpened to

`SAME_REALIZATION_EPRL_TO_AREA_METRIC_RENORMALIZED_GAMMA_MAP`

with the following required payload:

1. microscopic EPRL/spinfoam realization vector;
2. explicit coarse-graining/continuum map into the area-metric effective action;
3. parameter map `gamma_micro -> gamma_AM(k)` and scale convention;
4. parity-sector coefficient map connecting area-metric couplings to the GB/CS or equivalent frozen RQIR observable basis;
5. truncation/regulator/state uncertainty propagated through the map;
6. same-domain comparator after the composed observable is formed.

If this map is supplied, the area-metric RG and Lorentzian GW channel become high-value ingredients for `ADAPT_EXISTING`. If it is not supplied, they remain adjacent-programme evidence only.

## Classification

`PROMISING_ADAPT_EXISTING__AREA_METRIC_RUNNING_AND_LORENTZIAN_OBSERVABLE_BRIDGE_EXISTS__SAME_REALIZATION_EPRL_TO_AM_GAMMA_MAP_MISSING`

Status: **OPEN / BLOCKED_CROSS_AUTHORITY_COMPOSITION_NOT_YET_SAME_REALIZATION**.

This is not a scientific FAIL and is not evidence for `NEW_REQUIRED`.

## Compute decision

Heavy computation remains **IDLE**. The decisive missing object is an analytic/provenance/matching theorem. Running detector numerics before parameter identity is established would only sharpen an underidentified/composed object and cannot change the terminal classification.
