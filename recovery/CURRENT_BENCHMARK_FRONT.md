# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter274 Asymptotic Safety contact-complete external-authority reopen
Authoritative prior validated D7 infrastructure milestone: Iter272
Authoritative operational-saturation milestone: Iter270

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census remains 14 families: strict terminal 1/14, nonterminal 13/14.
- Tier-2 unresolved = 0.
- D1 = PASS.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3 = PARTIAL.
- D4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D5 = PASS.
- D6 = PASS_RULE_TARGETS_OPEN.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- D7-S0 = PASS.
- D7-S1 = PASS.
- D7-S2 = NOT_CLOSED.
- D7-S3 = NOT_CLOSED.
- D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D7-S5 = NOT_AUTHORIZED.
- D7-S6 = INACTIVE.
- Paper IV global decision = NOT_YET_AUTHORIZED.
- NEW_REQUIRED is not authorized.
- Candidate Gravity remains inactive at canonical R3 = 24%.
- Heavy compute = IDLE.

## Operational polygon status
Iter270 established:
- `OPERATIONAL_POLYGON_READINESS = 100%`
- `INTERNALLY_ACTIONABLE_UNRESOLVED_FRONTS = 0`

Iter272 established and validated D7 protocol infrastructure at 100%. Neither metric is scientific D7 closure.

## Iter273 material positive reopen — LQG/spinfoam

Muxin Han, *Ultraviolet fixed point in covariant loop quantum gravity*, Physical Review D 114, 044040 (2026), supplies a materially new complete Lorentzian EPRL/KKL summed-spinfoam continuum/fixed-point object. It remains nonterminal because the same-realization physical UV-to-IR/GR trajectory, normalized gravity observable, parameter/refinement transport and comparator/error certificate remain missing.

## Iter274 external-authority reopen — Asymptotic Safety

The frozen PF1-05 Asymptotic Safety blocker is a contact-complete approximation-controlled Lorentzian scalar-scattering certificate.

The stable public archival calculation, Chiesa-Pawlowski-Reichert arXiv:`2603.10168v1`, is a strong positive control: it reconstructs a non-perturbative Lorentzian graviton-mediated scalar-scattering amplitude/cross section, recovers GR in the IR and remains bounded/compatible with unitarity in the UV. But it explicitly omits the direct contact contribution `A4`; its forward-limit divergence requires `A4` for resolution.

A materially newer ERG2026 conference contribution dated 2026-09-03 reports a gravitational contact contribution resummed directly in Lorentzian signature and a UV-unitarity-compatible cross section. This directly attacks the frozen blocker.

Scoped result:

`HIGH_VALUE_NEAR_MISS__LORENTZIAN_CONTACT_TERM_REPORTED_AT_ERG2026_BUT_NOT_YET_FROZEN_IN_A_PUBLIC_REPRODUCIBLE_CONTACT_COMPLETE_SAME_REALIZATION_PACKAGE`

Family status remains:

`ASYMPTOTIC_SAFETY = BLOCKED_MISSING_REQUIRED_OBJECT`

Refined blocker:

`BLOCKED_PENDING_PUBLIC_CONTACT_COMPLETE_S_PLUS_T_PLUS_U_PLUS_A4_LORENTZIAN_SCATTERING_CERTIFICATE_WITH_FORWARD_LIMIT_TREATMENT_APPROXIMATION_UNCERTAINTY_BUDGET_AND_SAME_DOMAIN_COMPARATORS`

Therefore strict Tier-1 coverage remains `1/14`, not `2/14`. Conference progress is treated as an active watch trigger, not terminal authority. BLOCKED is not FAIL and no global outcome is authorized.

## Iter274 provenance
- `paper_iv/P_ASYMPTOTIC_SAFETY_CONTACT_COMPLETE_REOPEN_AUDIT_ITER274_2026-09-11.md`
- initial audit commit: `fb3d8dcfbc43d26357686b1ffde094ab31f2f856`
- updated family result commit: `005959124dcd7f4c9294be19ae484ef6bad44e53`
- `paper_iv/PAPER_IV_D7_READINESS_STATE.json` — Iter274 state, terminal count unchanged.
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_274.json`
- `recovery/RECOVERY_DELTA_274.md`

## Validation
Prior D7 infrastructure remains validated by Iter272 methodology-ci run `34545563636` = success.
The Iter274 synchronization head must be validated independently by its attached methodology-ci run before being described as a validated Iter274 state.

## Exact next gate
`D7_S2_EXTERNAL_AUTHORITY_WATCH__ASYMPTOTIC_SAFETY_CONTACT_COMPLETE_ARCHIVAL_PACKAGE_OR_OTHER_FAMILY_TERMINALIZATION_OBJECT`

Priority rule: do not repeat saturated broad scans. For Asymptotic Safety, wait only for a stable public same-realization `s+t+u+A4` package with forward-limit/crossing treatment, uncertainty/approximation controls, reproducibility artifacts and same-domain comparator capsule. If that object appears, ingest and validate it immediately. Otherwise continue D7-S2 only when another parked family acquires comparably material external authority capable of changing its strict family classification.
