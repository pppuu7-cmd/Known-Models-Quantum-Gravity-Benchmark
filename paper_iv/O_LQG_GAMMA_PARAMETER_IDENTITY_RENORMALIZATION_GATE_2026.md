# O-LQG γ Parameter-Identity / Renormalization Gate — 2026-09-10

**KMQGB iteration:** 169  
**RQIR standard:** Core v1.0 FROZEN  
**Closure-wave target:** CW2-02 / O-LQG.

## Problem

The gamma-duality route uses the same symbol `gamma` in several representations:

- the microscopic EPRL simplicity/duality structure;
- the LQG area spectrum / area gap;
- the gamma-dual continuum EFT coefficient relation;
- the primordial-GW observable relation.

A shared symbol is **not** sufficient authority that the renormalized physical parameter is identical across these layers.

## Why this matters

Renormalization/coarse-graining studies in first-order gravity explicitly allow a running Immirzi parameter. Meanwhile, spin-foam coarse-graining studies often keep `gamma` fixed as an input assumption in simplified models rather than deriving its invariance under the flow.

Therefore a complete cross-representation RQIR fingerprint must distinguish at least

`gamma_micro`, `gamma_coarse`, `gamma_EFT`, `gamma_geom`,

until an explicit map proves equality or a derived transformation law.

## Gate

The strong vector

`I_gamma = {2 f_GB/f_CS, Pi, r, n_T, a_*, spinfoam/entropy data}`

is authorized as a **one-parameter** rigidity vector only if the parent supplies

`gamma_EFT = Z_gamma[coarse-graining data] * gamma_micro`

and separately fixes whether

`gamma_geom = gamma_micro`,

`gamma_geom = gamma_EFT`,

or another derived relation applies.

The map may be trivial (`Z_gamma=1`), but triviality must be derived or protected by an exact symmetry/nonrenormalization statement, not assumed.

## Required checks

1. define the microscopic `gamma` entering EPRL amplitudes;
2. specify the continuum/coarse-graining trajectory;
3. derive the renormalized coefficient combination entering `f_GB/f_CS`;
4. propagate any running/matching uncertainty into the primordial relation;
5. define which `gamma` controls the independent area-gap/geometry block;
6. forbid independent refits of `gamma` in EFT, cosmology and geometry blocks;
7. use the geometry block as a holdout only after parameter identity is established.

## Failure classification

If the relation among the gamma parameters is not derived:

`BLOCKED_CROSS_REPRESENTATION_PARAMETER_IDENTITY`.

If independent gamma values are fitted per block, the claimed rigidity is lost and the result is not an RQIR fingerprint.

## Relation to current literature

The 2026 gamma-duality paper provides the observable/EFT relations but explicitly does not provide the full top-down derivation from nonperturbative spinfoam dynamics.

Existing coarse-graining literature demonstrates that keeping `gamma` fixed can be a modelling choice, while first-order gravity RG studies show that an Immirzi parameter can run. These do not prove that EPRL `gamma` runs in the desired continuum limit; they prove that **parameter identity is a scientific question that must be closed**.

## Current status

`GAMMA_OBSERVABLE_RELATION_IDENTIFIABLE__MICRO_TO_EFT_AND_PARAMETER_IDENTITY_BRIDGES_OPEN`.

CW2-02 remains open. No RQIR Core change and no readiness-score change.
