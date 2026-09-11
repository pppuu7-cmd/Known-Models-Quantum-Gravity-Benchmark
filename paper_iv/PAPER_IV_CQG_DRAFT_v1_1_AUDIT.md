# RQIR Paper IV — CQG Draft v1.1 audit

Date: 2026-09-11
Audited manuscript: `paper_iv/PAPER_IV_CQG_DRAFT_v1_1.md`
Manuscript commit: `74f7a9532b817585071c7ca41177356b9a05821e`
Coverage authority: Iter275 / 15 Tier-1 rows
D7 readiness authority: Iter276

## 1. Draft-level result

`PAPER_IV_CQG_DRAFT_v1_1.md` is the first continuous manuscript version assembled after the prospective expansion from 14 to 15 Tier-1 families.

The historical v1.0 file remains unchanged and retains its valid Iter274 / 14-family snapshot. No historical denominator was silently rewritten.

## 2. Quantitative consistency

Current v1.1 values used in Results, Discussion, Limitations and Conclusion:

- Tier-1 total = `15`;
- strict terminal rows = `1`;
- strict nonterminal rows = `14`;
- Tier-2 unresolved = `0`;
- internally actionable fronts = `0` in the Iter276 D7 readiness state;
- operational proving-ground readiness = `100%`;
- deterministic obstruction vector = `(5,6,1,1,1)`;
- bounded transport-first vector = `(2,9,1,1,1)`;
- bounded scope-maximal vector = `(6,5,1,1,1)`;
- robust structural aggregate C1+C2 = `11/14 = 78.6%`;
- D7 global scientific classifier = `NOT_AUTHORIZED`;
- `NEW_REQUIRED` = not authorized.

Historical `1/14` language is retained only where the manuscript explicitly explains the prospective census transition from Iter274 to Iter275.

`CURRENT_NUMERIC_SNAPSHOT_CONSISTENCY = PASS`.

## 3. RQCP prospective-coverage audit

v1.1 now treats RQCP as the fifteenth Tier-1 row because the Iter275 coverage contract applies the already-frozen `new_concrete_independent_parent_triggers_tier1_promotion` rule.

The manuscript preserves both sides of the evidence:

- positive scoped fixed-band same-family Einstein-response/reproducibility result;
- nonterminal family state because all-band/background-independent autonomous gravity and broader gravity-state/constraint/comparator closure remain open.

The manuscript explicitly uses the worsening of the terminal fraction from `1/14` to `1/15` as a prospective anti-selection-bias check, not as evidence against RQCP.

`RQCP_SCOPE_AND_PROMOTION_LANGUAGE = PASS`.

## 4. Obstruction-topology audit

The informal v1.0 split was replaced by the deterministic v1.1 assignments:

- C1: higher-derivative, Hořava–Lifshitz, nonlocal, string/M-theory/holography, RQCP = 5;
- C2: causal sets, CDT/EDT, LQG/spinfoams, GFT/tensor, noncommutative spectral geometry, Quantum Graphity = 6;
- C3: Asymptotic Safety = 1;
- C4: CFS = 1;
- C5: Wheeler–DeWitt = 1.

The manuscript no longer presents the exact C1/C2 split as uniquely physical. It instead promotes the projection-stable aggregate `11/14` as the stronger quantitative result.

It also explicitly forbids generalization of `78.6%` to all conceivable quantum-gravity theories in nature.

`OBSTRUCTION_ROBUSTNESS_LANGUAGE = PASS`.

## 5. Proposition 1 prior-art guardrail

The v1.1 manuscript states that Proposition 1 is **not** a new theorem of statistical model selection and cites partial-identification literature as a neighboring formal concept.

The claimed contribution is restricted to operationalizing non-promotion in a physical quantum-gravity benchmark using:

- realization-vector provenance;
- a defined common-domain residual;
- explicit family-scope promotion;
- execution over the current multi-framework census.

Broad priority claims such as “first theorem” or “first rigorous comparison of quantum-gravity theories” do not appear.

`PROPOSITION_PRIORITY_GUARDRAIL = PASS`.

## 6. LQG equation attribution and sign audit

The manuscript now separates direct source equations from KMQGB definitions/algebra.

Direct external relations are attributed to Bianchi–Rincon-Ramirez and the area-metric literature. KMQGB ownership is explicit for the residual coordinate `Delta_gamma`, the compact `gamma=-cot(4 psi)` reduction and the residual beta identities.

The previously implicit sign bridge is now explicit:

`q = -rho`

and therefore

`beta_q = -beta_rho`.

This makes

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma`

and

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`

algebraically compatible under the displayed gamma/psi map.

The manuscript repeatedly states that algebraic consistency does not establish the physical EPRL→area-metric→EFT same-realization bridge.

`LQG_ATTRIBUTION = PASS_FIRST_AUDIT`

`LQG_INTERNAL_SIGN_CONSISTENCY = PASS`.

## 7. Bibliography-key inventory

All citation keys intentionally introduced in v1.1 have corresponding entries in `paper_iv/references_cqg.bib`, including:

- broad QG positioning references;
- Phillips partial-identification reference;
- primary anchors for all 15 Tier-1 rows;
- Bianchi–Rincon-Ramirez, Dittrich–Kogios, area-metric RG, area-metric GW and Han 2026;
- both RQCP preprints;
- the 2026 Asymptotic Safety scattering preprint and ERG2026 conference record.

A full LaTeX compile/key-resolution test remains deferred until the IOP/CQG source is generated.

`BIBLIOGRAPHY_KEY_INVENTORY = PASS_FIRST_AUDIT`.

## 8. D7 synchronization state

The manuscript uses `paper_iv/PAPER_IV_D7_READINESS_STATE.json` Iter276 as the current D7 quantitative authority. It correctly reports `15/1/14` coverage and global `NOT_AUTHORIZED`.

The Iter276 D7 file itself states that fresh synchronization validation is pending. `recovery/CURRENT_BENCHMARK_FRONT.md` remains stale at Iter274 / 14 rows. The draft records this as a preparation/release qualification rather than using the stale file to override the newer D7 state.

Before submission this implementation note should be removed after a validated immutable article snapshot is frozen.

`D7_SCIENTIFIC_STATE_USE = PASS`

`ITER276_RELEASE_VALIDATION = PENDING`.

## 9. Remaining high-priority scientific/editorial work

### R1 — exact blocker-sentence primary citations — HIGH

Every family now has primary physics anchors, but many exact terminal-obstruction sentences still rely on KMQGB synthesis. Before submission, each material branch distinction, missing-map statement, normalization claim and comparator requirement should be connected to the relevant direct primary source or explicitly labeled as a KMQGB comparison requirement.

### R2 — deeper novelty / prior-art audit — HIGH

The first prior-art audit is sufficient to avoid an obvious overclaim but not to support broad priority language. Search model-comparison, theory-space, partial-identification and QG-methodology literature more deeply before freezing Introduction/Discussion novelty claims.

### R3 — figures — HIGH

Figures are specified but not rendered. The strongest planned set is:

1. frozen comparison architecture;
2. obstruction topology emphasizing robust `11/14` rather than the 5-versus-6 split;
3. prospective census expansion 14→15 via the pre-existing RQCP promotion rule;
4. D7 decision ecology.

### R4 — CQG/IOP source and compile — HIGH

Convert v1.1 to IOP-compatible LaTeX, resolve all bibliography keys, compile cleanly, inspect equation formatting and table width, and produce an archival PDF.

### R5 — immutable release — MEDIUM/HIGH

Freeze the exact article authority against a tagged release/DOI and deterministic bundle after the scientific snapshot and figures stabilize.

### R6 — article length and editorial focus — MEDIUM

The 15-row table and detailed case studies make v1.1 scientifically stronger but long. During v1.2, preserve the physical Results while moving repository-governance details and possibly the full claim/evidence table into appendices/supplementary material.

## 10. Readiness estimate after v1.1

- full v1.1 manuscript assembly task: **100%**;
- manuscript scientific content toward submission quality: **~60%**;
- CQG structural fit: **~85%**;
- family-level primary anchor coverage: **15/15 = 100% first-pass**;
- exact blocker-sentence citation/provenance completion: **~45%**;
- obstruction-topology robustness layer: **~80%**;
- LQG equation attribution layer: **~80%**;
- figures rendered: **0%**;
- IOP LaTeX / clean compile: **0%**;
- immutable archival article release: **0%**;
- overall submission readiness: **~40%**;
- Paper-IV D7 scientific authorization: **independent and still NOT_AUTHORIZED**.

## Audit conclusion

`PAPER_IV_CQG_DRAFT_v1_1 = CANONICAL_WORKING_MANUSCRIPT_CANDIDATE`

The draft is materially stronger than v1.0 and is safe to promote as the canonical working manuscript for cross-chat recovery, provided the recovery pointer records the Iter276 validation caveat and preserves v1.0 as an immutable historical snapshot.
