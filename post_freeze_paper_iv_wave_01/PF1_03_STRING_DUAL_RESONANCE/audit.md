# PF1-03 — String / Dual-Resonance Gravity Amplitudes under RQIR Core v1.0

**RQIR core:** `v1.0 FROZEN`  
**Terminal status:** `PASS_RQIR_GATE__SCOPED_RIGIDITY_CONTROL`.

## 1. Frozen question

Do not test string theory using one attractive feature such as an infinite pole tower, dual resonance or UV softness. The RQIR object is the joint same-channel invariant package

`I_UV = {poles, residues/spins, crossing/duality, Regge trajectory, high-energy bounds/sum rules, low-energy coefficient correlations}`.

The regression asks which subset of this package is genuinely string-rigid after the strongest known same-channel amplitude comparators are admitted.

## 2. Bespoke dual-resonance comparator

Cheung & Remmen, *Bespoke Dual Resonance*, arXiv:2308.03833, construct closed-form dual-resonant amplitudes with an arbitrary user-defined mass spectrum, simple poles with polynomial residues, controlled UV behavior and open regions compatible with partial-wave unitarity. The construction generalizes to higher multiplicity through transformed Koba–Nielsen integrals.

Therefore the following are **not** globally unique string fingerprints by themselves:

- existence of an infinite resonance tower;
- special pole locations when the comparator family is allowed to tune its spectrum;
- dual resonance alone;
- meromorphic/simple-pole structure with local polynomial residues;
- generic tame UV behavior.

Bhardwaj, Spradlin, Volovich & Weng, arXiv:2406.04410, substantially restrict the bespoke class: asymptotically nonlinear Regge trajectories are ruled out by partial-wave unitarity, while asymptotically linear cases are constrained and only a smaller subclass has the strongest superpolynomial boundedness properties.

This narrows the comparator but does not restore uniqueness to pole support alone.

## 3. Scoped Virasoro–Shapiro rigidity

Cheung, Hillman & Remmen, *Uniqueness Criteria for the Virasoro-Shapiro Amplitude*, arXiv:2408.03362, study fully permutation-invariant gravitational amplitudes in a bootstrap framework. They find non-string deformations under weaker conditions, while superpolynomially soft Regge behavior in the stronger bootstrap package selects the Virasoro–Shapiro amplitude uniquely and produces the string spectrum as an output.

Thus RQIR records a real scoped rigidity boundary:

`crossing/permutation + required bootstrap structure + sufficiently strong Regge softness -> Virasoro-Shapiro`

within the stated assumptions.

The scientific content is the **overconstrained relation**, not any one coordinate of `I_UV`.

## 4. Fresh 2026 dispersive control

Y. Xu, *A Dispersive Bootstrap for the Virasoro-Shapiro Amplitude*, arXiv:2606.19283, imposes analyticity, crossing, partial-wave unitarity and Regge boundedness on the ten-dimensional maximally supersymmetric four-point problem. These generic constraints produce bounds/allowed regions. Adding a Virasoro-inspired nonlinear ansatz shrinks the allowed region toward a small island containing the Virasoro–Shapiro point.

This reinforces the frozen RQIR distinction:

- generic S-matrix consistency strongly constrains but does not automatically identify the string amplitude;
- extra string-like nonlinear/rigidity data are scientifically meaningful and must be declared rather than smuggled into the comparator definition.

## 5. RQIR terminal classification

### PASS

The framework supplies a concrete, normalized amplitude hierarchy and demonstrates a strong same-channel rigidity package that survives much broader comparators than pole support alone.

Classification:

`PASS_RQIR_GATE__SCOPED_RIGIDITY_CONTROL`

### Not promoted to a universal unique-QG residual

This audit does not claim that every observed deviation matching one string feature uniquely identifies string theory. A detector/asymptotic attribution claim would still need the full observable map, domain, nuisance/covariance treatment where applicable, and exclusion of all comparators satisfying the same measured subset.

## 6. Core-defect test

No RQIR Core defect. Generalized dual-resonance competitors fit naturally in the comparator registry; stronger string rigidity fits naturally as a multi-component overconstraint. No version change is requested.

## 7. Paper-IV meaning

The result supports the methodology statement:

> an existing framework can be highly rigid in a sufficiently rich observable vector even when every low-dimensional fingerprint is non-unique.

It does not by itself authorize overall `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`.

## 8. Reopen condition

Reopen for stronger attribution when a concrete accessible observable domain measures enough independent components of `I_UV` to distinguish the scoped Virasoro–Shapiro rigidity package from the surviving generalized amplitude class.