# O-PURE-TENSOR — Enhanced/nonmelonic RG-to-gravity-observable gap audit

**Date:** 2026-09-10  
**Iteration:** 209  
**RQIR Core:** v1.0 **FROZEN**

## Question

Can the surviving enhanced/nonmelonic pure-random-tensor branch be promoted from BLOCKED by an authenticated same-realization object containing a controlled continuum/RG limit and a normalized 4D gravity observable/comparator with provenance and errors?

## Primary authority audited

A. Castro, A. Eichhorn, R. Gurau, *Towards a quantitative characterization of gravitational universality classes for order-4 random tensor models*, JHEP 05 (2026) 117, DOI 10.1007/JHEP05(2026)117, arXiv:2602.09257. Version of record: 2026-05-12. The article supplies an ancillary Mathematica notebook (`beta_fcts8.nb`) and an explicit regulator-parameter sensitivity analysis.

Primary links:
- https://arxiv.org/abs/2602.09257
- https://doi.org/10.1007/JHEP05(2026)117

## Same-realization object audit

The audited realization is a real order-4 tensor with `O(N)^{\otimes 4}` symmetry and an effective-action truncation containing tensor invariants through order `T^8`. The pregeometric RG scale is tensor size `N`. This is a genuine reproducible continuum-candidate analysis in the discrete/pregeometric sense; it is not merely an analogy to continuum RG.

The paper reports three fixed-point candidates under a two-parameter regulator family. Only one remains real across the full scanned regulator range. At the minimum-sensitivity region that candidate has two relevant directions. The authors contrast this with the likely three-dimensional critical surface of the Reuter fixed point and conclude that the simple combinatorial tensor realization and the Reuter universality class are most likely different.

This supports the scoped structural disposition:

`PASS_STRUCTURAL_GATE__ORDER4_ON4_T8_PREGEOMETRIC_RG_FIXED_POINT_CANDIDATE_WITH_EXPLICIT_REGULATOR_SENSITIVITY_AND_REPRODUCIBLE_BETA_FUNCTION_NOTEBOOK_EXISTS`

It does **not** support a family-level scientific PASS or FAIL.

## Why the RQIR gravity comparator remains undefined

The required RQIR chain is:

`microscopic tensor realization -> controlled critical/continuum trajectory -> emergent extended 3+1/4D geometry -> Lorentzian/physical gravity observable -> normalized common-domain GR/EFT + alternative-QG comparator -> propagated truncation/regulator/continuum error ledger`.

The 2026 authority supplies the first two links at candidate level and a regulator-sensitivity study. It does not supply, in that same realization:

1. an emergent Lorentzian 3+1 metric/causal sector;
2. a normalized gravitational observable (e.g. scattering, invariant correlator, relational curvature response, or comparator-ready metric observable);
3. a same-domain GR/EFT comparator normalization;
4. a propagated error quotient from the pregeometric `T^8` truncation and regulator variation through an emergent gravity observable.

The paper itself states that for `d>2` it is not yet clear whether random tensors exhibit a continuum limit corresponding to a viable physical theory. Its fixed-point result therefore cannot be promoted into the missing physical-object certificate by interpretation alone.

## Universality result — scope discipline

The two-relevant-direction candidate is negative evidence against identifying this **specific audited realization/truncation** with the Reuter universality class. Because the authors phrase the universality conclusion probabilistically ("most likely") and because the calculation remains truncation/regulator dependent, this audit does **not** encode a scientific FAIL of all enhanced/nonmelonic tensor models and does not encode a family-level exclusion.

No scoped child PASS/FAIL is promoted to `GFT_TENSOR_MODELS` family level.

## Disposition

Enhanced/nonmelonic pure random tensors remain:

`BLOCKED_MISSING_REQUIRED_OBJECT__PURE_RANDOM_TENSOR_ENHANCED_NONMELONIC_PREGEOMETRIC_RG_CONTINUUM_TO_NORMALIZED_LORENTZIAN_4D_GRAVITY_OBSERVABLE_COMPARATOR_WITH_PROPAGATED_ERROR`

This is **BLOCKED, not FAIL** and has no defined family residual.

The stable real fixed-point candidate is retained as positive structural evidence that the branch cannot be dismissed as merely melonic/branched-polymer behavior. Conversely, its likely mismatch with the Reuter critical-surface dimension prevents using asymptotic-safety universality as an implicit comparator shortcut.

## Compute decision

Heavy compute remains **IDLE**. Re-running or extending the published beta-function notebook cannot by itself create the missing emergent Lorentzian gravity observable or same-realization comparator. A new numerical run is authorized only if a prospectively frozen physical observable map is first supplied and the run can change terminal classification.

## Global Paper-IV governance

- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`
- D4: `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`
- D7: `NOT_CLOSED`
- global decision: `NOT_YET_AUTHORIZED`
- Candidate Gravity activation: false
- Candidate Gravity R3: 24%

No `NEW_REQUIRED` inference is permitted from this missing object.

## Exact next gate

`PURE_RANDOM_TENSOR_ENHANCED_NONMELONIC_EMERGENT_GEOMETRY_TO_NORMALIZED_GRAVITY_OBSERVABLE_AUTHORITY_SEARCH`

The next search should target an explicit physical-map authority from a nonmelonic/enhanced rank-4 tensor critical regime to an extended 4D geometric observable. If none exists after material-branch exhaustion, park this branch as BLOCKED and move to the next Tier-1 family rather than weakening the comparator.
