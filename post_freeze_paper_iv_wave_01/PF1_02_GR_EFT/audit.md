# PF1-02 — GR + Controlled Low-Energy Gravitational EFT under RQIR Core v1.0

**RQIR core:** `v1.0 FROZEN`  
**Role:** baseline/control regression for Paper IV.  
**Terminal status:** `PASS_RQIR_GATE__BASELINE_CONTROL`.

## 1. Why this control is mandatory

A frozen reconstruction standard is only trustworthy if it does not misclassify established low-energy quantum-gravity effects as evidence for a new UV theory.

General relativity treated as an effective field theory is the canonical control for this question.

## 2. Frozen-core adapter

Native EFT objects map directly into RQIR:

`GR + allowed local higher-curvature operators + quantum loops`

`-> gauge-invariant / relational low-energy observables or on-shell amplitudes`

`-> declared EFT truncation/domain`

`-> RQIR baseline/comparator block`.

No Core extension is needed.

## 3. Scientific authority

Donoghue's EFT programme establishes that GR is a consistent quantum EFT at energies well below the UV completion scale. The long-distance/low-energy quantum effects associated with propagation of massless fields, including gravitons, appear in nonanalytic/nonlocal momentum dependence and can yield parameter-free low-energy predictions. See:

- J. F. Donoghue, *Quantum General Relativity and Effective Field Theory*, arXiv:2211.09902 (2022).
- J. F. Donoghue & B. R. Holstein, *Low Energy Theorems of Quantum Gravity from Effective Field Theory*, arXiv:1506.00946.
- J. F. Donoghue, *General Relativity as an Effective Field Theory: The Leading Quantum Corrections*, arXiv:gr-qc/9405057.

The same EFT framework also makes the limitation explicit: local analytic higher-curvature terms carry Wilson coefficients/renormalized parameters that are not fixed by low-energy GR alone and may encode UV information.

## 4. RQIR separation rule

The frozen benchmark must distinguish:

### Universal low-energy nonanalytic structure

Massless propagation can generate nonanalytic structures such as logarithms or threshold/nonlocal terms whose low-energy coefficients are determined by the known light spectrum/couplings in the declared EFT.

These are **existing comparator predictions** in their validity domain.

A measured nonzero effect matching such a term is not a unique UV/QG residual.

### Local analytic higher-curvature structure

Finite analytic corrections are represented by the allowed local EFT basis and its Wilson coefficients unless a stronger same-domain relation is derived.

A candidate UV completion does not earn a unique residual merely by choosing a nonzero point in this already-admissible coefficient space.

### Outside-EFT regime

The fact that low-energy EFT does not determine the full Planck/strong-gravity completion is a domain limit, not a failure of the RQIR methodology and not evidence by itself for `NEW_REQUIRED`.

## 5. Regression tests

A correct frozen RQIR application must return:

1. known GR tree/semiclassical predictions -> baseline/comparator;
2. universal controlled low-energy quantum nonanalytic corrections -> quantized-GR EFT comparator;
3. arbitrary local analytic higher-curvature coefficients -> EFT comparator freedom unless cross-order/UV relations reduce them;
4. a claim outside the declared EFT domain -> domain warning/block, not extrapolated residual;
5. no Paper-IV `NEW_REQUIRED` inference from EFT incompleteness alone.

All five conditions pass conceptually under Core v1.0.

## 6. Terminal result

`PASS_RQIR_GATE__BASELINE_CONTROL`

Scoped interpretation:

`EXISTING_SUFFICIENT_IN_DECLARED_LOW_ENERGY_EFT_DOMAIN`

This is **not** the overall Paper-IV decision. It says only that the existing GR+EFT framework is the correct comparator and predictive framework for its controlled domain.

## 7. Reopen / stronger test

A UV framework can exceed this control only by deriving a same-domain relation or observable that is not removable by

- the full allowed local EFT coefficient space;
- field-redefinition/reparameterization freedom;
- known massless-loop nonanalytic structure;
- other applicable known-framework comparators.

That stronger residual must then pass detector/identifiability and holdout checks under the frozen RQIR standard.

## 8. Core-change verdict

No RQIR Core defect. No version change requested.