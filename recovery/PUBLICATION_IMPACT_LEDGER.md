# Publication Impact Ledger

Purpose: preserve, for final manuscript preparation, every benchmark result that requires a change, check, or explicit non-change in an RQIR paper. This ledger is additive and does not modify frozen RQIR Core criteria.

Status vocabulary:
- `TODO` — manuscript change/check still required.
- `READY` — wording/evidence is sufficiently defined to be applied at final preparation.
- `APPLIED` — change has been incorporated into the manuscript and re-audited.
- `NOT_NEEDED` — checked and no manuscript change is warranted.

## Iter277 — RQCP multi-axis resource closure

### Paper III
- **Status:** `READY`
- **Impact:** methodological correction/strengthening is warranted.
- **What to add:** an explicit general rule that resource closure is axis-complete rather than single-axis. If a result depends on multiple independent regulator/truncation/domain/finite-volume/approximation axes, convergence or calibration along one axis cannot certify closure of the others. Every materially active independent axis must either (a) be taken to a controlled limit with uncertainty propagated into the normalized observable, or (b) be fixed by an independently justified physical principle with the induced uncertainty propagated.
- **Why:** Iter277 provides a concrete counterexample to single-axis closure. RQCP spatial refinement can be well controlled while an independent Hilbert-space cutoff materially shifts normalized quantities. In the independent audit, cutoff 8 -> 28 changes G_eff by about 7.32%, the gap by about 3.07%, and G_eff*gap^2 by about 1.36%, while the high-cutoff sequence 24 -> 28 is already extremely stable.
- **Where to apply:** methodology/resource-closure definition and the discussion/checklist for claiming apparatus/model closure. Keep the wording theory-agnostic; do not turn Paper III into an RQCP case study.
- **Do not change:** frozen RQIR Core criteria or previously certified detector-side nuisance/noise/calibration logic unless manuscript audit finds a direct contradiction.

### Paper IV
- **Status:** `READY`
- **Impact:** detailed benchmark evidence should be included.
- **What to add:** RQCP as a distinct nonterminal Tier-1 parent; four-environment semantic reproducibility result; the zero-frequency diagnostic defect as an implementation artifact; the 19-job robustness scan; extended Hilbert-cutoff scan through 28; and the refined blocker requiring independent closure/control of the Hilbert/domain truncation axis before any broader family-level sufficiency claim.
- **Interpretation constraint:** this is neither a family-level PASS nor a family-level FAIL. It is a scoped positive fixed-band result plus a newly quantified independent resource axis.

## Iter278 — Asymptotic Safety diffeomorphism-invariant PIRG reopen

### Paper III
- **Status:** `NOT_NEEDED`
- **Impact:** no additional general methodological rule is required beyond Iter277.
- **Reason:** the new PIRG result provides an independent example in which a robust structural conclusion (two relevant directions across all six published Table-III variants) coexists with materially larger scheme/procedure sensitivity in fixed-point coordinates and in the first critical exponent. This reinforces `MULTI_AXIS_RESOURCE_CLOSURE` and systematic-uncertainty separation, but does not establish a distinct failure mode.
- **Optional use:** cite or mention only as corroborating motivation if space and narrative benefit justify it; do not expand Paper III into an Asymptotic-Safety case study.

### Paper IV
- **Status:** `READY`
- **Impact type:** evidentiary + numerical.
- **What to add:** arXiv:2609.07829v1 as a material positive Asymptotic-Safety reopen; explain its diffeomorphism-invariant/background-independent PIRG construction and relevance-preserving aim; report the independent four-probe Table-III audit; state that all six variants retain two positive relevant directions, while theta2 is substantially more stable than theta1 and the fixed-point coordinates remain procedure/scheme sensitive.
- **Required boundary:** family status remains `BLOCKED_MISSING_REQUIRED_OBJECT`; the Iter274 public contact-complete `s+t+u+A4` Lorentzian scattering certificate is still missing. The PIRG object must not be used to bypass that same-realization observable blocker.
- **Provenance:** scientific workflow run `34552838082`; methodology CI run `34552838007`; audit `paper_iv/P_ASYMPTOTIC_SAFETY_PIRG_DIFFEO_INVARIANT_REOPEN_AUDIT_ITER278_2026-09-11.md`.

## Iter279 — Null Surface Formulation reduction and claim-boundary audit

### Paper III
- **Status:** `NOT_NEEDED`
- **Impact:** no new methodological rule beyond Iter277.
- **Reason:** Iter279 independently illustrates two already-required separations: an explicit reduction map prevents unnecessary Tier-1 proliferation, and closure of one claim domain (UV finiteness of a perturbative/integration construction) cannot be substituted for another claim domain (bounded fixed-angle amplitude, forward regularity, or all-order equivalence).
- **Optional use:** one sentence or footnote may be used as corroboration of `MULTI_AXIS_RESOURCE_CLOSURE` / claim-domain discipline if useful, but no NSF case study is required in Paper III.

### Paper IV
- **Status:** `READY`
- **Impact type:** taxonomy + evidentiary + numerical.
- **What to add:** NSF as a worked reduction-map case. The source lineage explicitly treats NSF as a formulation/quantization of GR and the 2026 trilogy reproduces the standard tree amplitude, so the present evidence supports `REDUCED_TO_EXISTING_GR_PARENT__NEW_REALIZATION_NOT_NEW_TIER1_PARENT` rather than creation of a 16th Tier-1 row.
- **Numerical claim-boundary check:** normalization and t/u symmetry agree exactly on the test set; fixed-angle amplitude scales as s^1; forward/collinear behavior is pole-like with fitted finite-grid exponent about -0.9794.
- **Required boundary:** do not convert this reduction decision into rejection of the NSF UV-finiteness claim. The audit does not independently prove or disprove all-loop finiteness; it only fixes taxonomy and separates the claim domains.
- **Provenance:** scientific workflow run `34553257781`; methodology CI run `34553257768`; audit `paper_iv/P_NSF_REDUCTION_AND_CLAIM_BOUNDARY_AUDIT_ITER279_2026-09-11.md`.

## Iter280 — Asymptotic Safety self-consistent Lorentzian graviton spectral function

### Paper III
- **Status:** `NOT_NEEDED`
- **Impact:** no new methodological rule is required beyond Iter277.
- **Reason:** the result independently confirms the importance of separating closure axes: spectral positivity and normalisability, physical-state/Hilbert-space status, diffeomorphism invariance, scattering unitarity and contact-complete observables are not interchangeable certificates.
- **Optional use:** one concise corroborating sentence may be added near the Iter277 multi-axis/resource-closure strengthening if helpful; no Asymptotic-Safety technical discussion is required in Paper III.

### Paper IV
- **Status:** `READY`
- **Impact type:** peer-reviewed evidentiary + numerical + reproducibility-boundary.
- **What to add:** Pawlowski–Reichert–Wessely, Physics Letters B 880 (2026) 140844, as a major positive Lorentzian Asymptotic-Safety result. State that the stated on-shell TT fluctuation-graviton calculation yields a positive normalisable spectral function and, after physical rescaling, unit total spectral weight.
- **KMQGB cross-checks to report:** `g*=0.9554263372261876`; Eq.23–25 trajectory consistency; analytic UV-tail sum-rule integrability; the decomposition implied by `z_spec≈1.486` (~67.29% pole and ~32.71% continuum after the stated rescaling); and the exact `2*pi*A_h=61/30` IR relation.
- **Required boundaries:** the authors explicitly state that the fluctuation-graviton states are not diffeomorphism invariant and are not part of the physical Hilbert space; the publisher exposes numerical data only on request and no article-specific public dataset/reference implementation was found, so the complete spectral curve was not independently reproduced in Iter280; the Iter274 contact-complete `s+t+u+A4` scattering blocker remains independent and active.
- **Provenance:** scientific workflow run `34553743544`; methodology CI run `34553743421`; audit `paper_iv/P_ASYMPTOTIC_SAFETY_LORENTZIAN_SPECTRAL_AUDIT_ITER280_2026-09-11.md`.

## Standing rule for subsequent iterations
For every scientifically relevant benchmark iteration, record here:
1. affected paper(s),
2. exact manuscript correction/addition/check required,
3. whether the change is methodological, numerical, evidentiary, taxonomy-related, reproducibility-related, or editorial,
4. status (`TODO/READY/APPLIED/NOT_NEEDED`),
5. an explicit note when no paper change is warranted.

This ledger is the manuscript handoff authority for final article preparation; chat-only reminders are not sufficient.
