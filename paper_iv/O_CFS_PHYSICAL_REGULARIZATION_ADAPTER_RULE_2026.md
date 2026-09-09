# O-CFS Physical-Regularization Adapter Rule — 2026-09-10

**KMQGB iteration:** 164  
**RQIR standard:** Core v1.0 FROZEN and unchanged.

## Correction to the CFS adapter

A generic EFT/lattice benchmark often asks whether a regulator can be removed while observables converge. That wording is not automatically appropriate for Causal Fermion Systems.

In CFS, the UV regularization may have **physical significance**: the regularized local-correlation operators can encode microscopic spacetime structure at a fundamental length scale. The formal programme does not require every admissible prediction to survive `epsilon -> 0` as if the regulator were merely a computational artifact.

Therefore the Iter163 phrase `regulator scaling / removal test` must be interpreted through the CFS-native ontology rather than imposed literally.

## Frozen-RQIR-compatible adapter rule

For a CFS observable `O_CFS[epsilon, R]`, where `R` denotes the microscopic regularization prescription, the admissible closure test is:

1. **physical authority:** state why `epsilon`/`R` is fundamental, derived, selected by causal-action minimization, or externally fixed;
2. **no post-hoc fit:** `epsilon`/`R` is fixed before inspecting the target residual;
3. **admissible-family stability:** vary only the microscopic realizations that the CFS parent still regards as physically equivalent/admissible and propagate the induced uncertainty;
4. **continuum control:** in the regime where CFS is known to reproduce GR/QFT, recover the declared continuum comparator;
5. **microscopic prediction:** identify the first correction/effect that depends on the physical microscopic structure;
6. **shared parameters:** use the same microscopic law across more than one observable/configuration/holdout;
7. **comparator quotient:** remove ordinary GR/QFT/EFT effects before attributing any remaining structure to CFS.

The closure condition is **not** `epsilon -> 0` by definition. It is

`PHYSICAL_REGULARIZATION_LAW_FIXED_AND_PREDICTIVE`.

## Why this is not a Core change

RQIR Core v1.0 already requires declared model domain, normalization, nuisance/parameter discipline and comparator mapping. It does not require every microscopic length to be an unphysical regulator.

Thus this is a model-specific adapter clarification:

`CFS native regularization -> KMQGB adapter -> frozen RQIR parameter/domain discipline`.

No RQIR Core defect is present.

## Updated CW2-03 requirement

A non-continuum mass/quasilocal/curvature evaluation may close the regularization part of CW2-03 if its microscopic regularization is prospectively fixed by a physical CFS law and demonstrates predictive shared-parameter behavior. Literal regulator removal is unnecessary unless the claimed domain itself is a continuum limit.
