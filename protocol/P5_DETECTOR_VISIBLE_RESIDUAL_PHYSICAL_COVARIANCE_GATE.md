# P5 Detector-Visible Residual / Physical-Covariance Gate

**Status:** permanent pre-promotion identifiability gate.  
**KMQGB iteration:** 134.  
**Purpose:** prevent a comparator-orthogonal theoretical residual from being promoted when it is absorbed by detector nuisance directions under a source-traceable physical covariance.

## 1. Motivation from external RQIR

The external RQIR Paper-III branch now provides a source-traceable atom-gravimeter covariance derived from the published SYRTE vibration spectrum rather than a synthetic AR(1) family.

That audit establishes a valuable physical control:

- modulated science + calibrated reference -> estimable;
- static science + free offset -> not estimable;
- modulated science without calibrated reference -> absolute scale degeneracy;
- unconstrained reference amplitude -> not estimable;
- finite independent reference prior -> estimability restored;
- the PASS survives a strong 2-Hz crosstalk stress.

Therefore local theoretical novelty and detector-visible novelty must be kept distinct.

## 2. Definition

Let

- `r` be the detector-space science/residual tangent after the theory-to-observable map;
- `C` be the detector covariance on the declared data vector;
- `N` be the nuisance tangent matrix;
- `P_prior` be any independently-authorized nuisance-prior precision matrix.

Define

`I0 = r^T C^-1 r`

and the nuisance-profiled information

`Iprof = I0 - r^T C^-1 N (N^T C^-1 N + P_prior)^+ N^T C^-1 r`.

The detector-visible separation fraction is

`eta_det = sqrt(max(Iprof,0)/I0)`.

Equivalent whitened form when there is no finite prior:

`r_vis = (I-P_N) C^(-1/2) r`.

A locally nonzero comparator-orthogonal residual is not detector-identifiable if `eta_det=0`.

## 3. Mandatory P5/P6 rule

Before a candidate or comparator-orthogonal residual can be promoted beyond structural novelty, KMQGB requires prospectively:

1. **physical observable map:** the theory residual is mapped to an actual detector/readout quantity, not left as an abstract field amplitude;
2. **source-traceable covariance:** the covariance/noise model is measured, source-grounded, or explicitly labelled as a stress model with independent scale validation;
3. **complete nuisance tangent:** offset, scale/gain, drift, calibration/reference amplitudes and apparatus-specific nuisance directions are included if physically relevant;
4. **external priors only:** a nuisance prior may restore identifiability only when its origin and finite uncertainty are independent of the science data used to claim the residual;
5. **fail controls:** at least one known degenerate configuration must fail, preventing hidden regularization from manufacturing a PASS;
6. **stress robustness:** plausible covariance/crosstalk perturbations must not create or destroy the claimed science direction by arbitrary tuning;
7. **no post-hoc modulation:** source/reference modulation or channel choice may not be selected after seeing which option maximizes the candidate residual.

## 4. Source-traceable regression fixture

`code/detector_visible_residual_physical_covariance_reference.py` ports the external RQIR Fig.-8 physical-covariance control into standalone KMQGB methodology using NumPy only.

The fixture independently checks that the coarse PSD digitization reproduces

- published uncorrected vibration scale `6.5e-8 g @1s` to better than 5%;
- published typical corrected scale `2e-8 g @1s` to better than 12% after the reported factor-3 correction plus independent 4-mrad floor.

It then verifies the expected detector-identifiability pattern under the physical Toeplitz covariance.

This fixture is a methodology positive control, not a claim that the RQIR science signal is Candidate Gravity or that the coarse digitization is raw experimental data.

## 5. Relation to existing COR geometry

Existing KMQGB residual geometry defines

`COR = (I-AA^+) Sigma^(-1/2) r`

against a comparator tangent space.

The present gate adds a distinct downstream layer:

`theory/comparator orthogonality -> detector map -> physical covariance whitening -> apparatus nuisance profiling`.

Both must pass. A residual can be comparator-orthogonal yet detector-invisible, or detector-visible yet comparator-contained.

## 6. Calibration-floor rule

When identifiability depends on a finite calibration/reference prior, increasing sample count cannot legitimately drive the total uncertainty below the calibration floor unless the same experiment independently improves that calibration channel.

A candidate may not relabel calibration-limited information as unlimited statistical scaling.

## 7. Current limitation and score rule

The external RQIR fixture is still based on a phase-Gaussian local model. Its own next authority explicitly calls for detector-facing transition probability

`P = (1 + C cos Phi)/2`

with finite contrast, contrast drift, readout gain/detection noise and conservative reference-transfer uncertainty.

Therefore Iter134 materially strengthens executable identifiability methodology but **does not yet close** the frozen `residual/identifiability/rigidity 19/20` component.

R2 remains 89% until a detector-facing nonlinear/readout certificate or an equivalent end-to-end closure is incorporated.

## 8. Score consequence

- R1 unchanged.
- R2 unchanged at 89%.
- R3 unchanged at 24%.
- R4 unchanged at 45%.

This gate cannot substitute for the P4 novel-parent deliverable.