# Paper IV — Iter275 article transition authority

Date: 2026-09-11
Purpose: freeze the manuscript consequences of the RQCP Tier-1 promotion without rewriting the historical v1.0 manuscript snapshot.

## Version boundary

`paper_iv/PAPER_IV_CQG_FIRST_DRAFT_v1_0.md` is a valid historical Iter274 manuscript snapshot with:

- Tier-1 total = 14;
- strict terminal = 1/14;
- strict nonterminal = 13/14;
- obstruction baseline = `(4,6,1,1,1)`;
- robust C1+C2 aggregate = `10/13 = 76.9%` after the first robustness audit.

It must not be silently edited to contain Iter275 results.

The next manuscript, `PAPER_IV_CQG_DRAFT_v1_1.md`, is to use the Iter275 coverage contract, which now contains a fifteenth Tier-1 family:

`RELATIONAL_QUANTUM_CAUSAL_PROCESSES` / RQCP-QG.

The promotion is governed by the already-frozen rule

`new_concrete_independent_parent_triggers_tier1_promotion = true`.

The Iter275 RQCP audit found a concrete independent quantum parent with gravity/emergence claims and materially distinct observables and did not locate an explicit reduction/equivalence map to an existing Tier-1 family. Conservative coverage therefore requires promotion rather than omission.

## Iter275 coverage numbers

From `protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json` schema v1.3 / Iter275:

- Tier-1 total = 15;
- strict terminal = 1/15;
- strict nonterminal = 14/15;
- Tier-2 unresolved = 0;
- RQCP coverage status = `PARTIAL_SUBFAMILY_ONLY`.

The terminal denominator therefore becomes less favorable after increasing coverage. This is a desirable prospective behavior of a frozen benchmark: a newly discovered independent parent changes coverage rather than being ignored to preserve an earlier percentage.

## RQCP positive scoped result

Primary sources:

- Yipeng Xu, `Relational Quantum Causal Processes: Exact Models, Continuum Limits, and the Boundary of Emergent Gravity`, arXiv:`2607.26672`;
- Yipeng Xu, `Relational Quantum Causal Processes toward Quantum Gravity with Controlled Einstein Response`, arXiv:`2608.23117`.

The controlled August result supplies a same-family fixed-band construction connecting one finite-Hilbert interacting lineage to a Lorentzian excitation gap, nonlinear response, mixed matter/geometry response, a dynamic geometry kernel, an induced Newton coefficient in a prescribed covariant two-derivative FLRW sector, and semiclassical matter backreaction, with explicit regulator convergence controls.

The source explicitly limits this to a fixed-band/finite-cutoff/prescribed semiclassical sector and does not claim an all-band completed quantum gravity. KMQGB therefore records a positive scoped result without family-level terminal promotion.

## RQCP terminal blocker

The Iter275 audit leaves open a family-level/all-band autonomous gravitational parent and the corresponding gravity-state/constraint/topology/common-domain comparator structure. Therefore the row is nonterminal and must not be described as either a completed theory or a failed theory.

## Updated obstruction topology

Under the deterministic baseline projection used for v1.1, RQCP is assigned to C1 `FAMILY_OR_BRANCH_SCOPE`: the strongest positive result is a scoped fixed-band child while family-level exhaustion remains open.

This gives the Iter275 baseline:

`(C1,C2,C3,C4,C5) = (5,6,1,1,1)`.

Bounded alternative projections:

- transport-first: `(2,9,1,1,1)`;
- scope-maximal: `(6,5,1,1,1)`.

The robust aggregate becomes:

`C1+C2 = 11/14 = 78.6%`.

Thus the manuscript's robust qualitative conclusion survives the census expansion: most current nonterminal rows are blocked structurally at family/scope and/or same-realization transport before a terminal family-level residual is numerically evaluable.

## Important synchronization caveat

At the time of this article transition audit:

- the coverage contract is already Iter275 and contains 15 Tier-1 rows;
- `paper_iv/PAPER_IV_D7_READINESS_STATE.json` is still Iter274 and reports 14 rows;
- `recovery/CURRENT_BENCHMARK_FRONT.md` is still Iter274 and reports 14 rows.

Therefore the **coverage update is authoritative**, but the article must not call the whole Iter275 global D7 snapshot synchronized until those canonical D7/recovery state files are advanced and validated.

The logical D7 outcome is not loosened by the new row: there is still no basis for `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED` or `NEW_REQUIRED`. The next manuscript should phrase the quantitative global state carefully until synchronization is complete.

## Files controlling v1.1 after Iter275

- `protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json`
- `paper_iv/P_RQCP_NEW_PARENT_PROMOTION_AUDIT_ITER275_2026-09-11.md`
- `paper_iv/PAPER_IV_PRIMARY_LITERATURE_EVIDENCE_TABLE_v0_2.md`
- `paper_iv/PAPER_IV_OBSTRUCTION_TAXONOMY_v1_1.json`
- `paper_iv/PAPER_IV_LQG_EQUATION_ATTRIBUTION_AUDIT_v0_1.md`
- `paper_iv/PAPER_IV_PROPOSITION1_PRIOR_ART_AUDIT_v0_1.md`
- `paper_iv/references_cqg.bib`

## Assembly instruction

When building the full v1.1 manuscript:

1. preserve v1.0 unchanged;
2. replace every generic `14-family` statement with the Iter275 `15-family` statement;
3. replace `1/14` with `1/15` and `13/14` with `14/15` only where the sentence refers to Iter275 coverage;
4. add RQCP as the fifteenth result-matrix row and as a new positive scoped case in the prospective-update discussion;
5. replace the old robust obstruction aggregate `10/13 = 76.9%` with `11/14 = 78.6%`;
6. retain an explicit note that the D7 readiness snapshot is awaiting Iter275 synchronization if that remains true at assembly time;
7. re-check the canonical D7/recovery files immediately before finalizing v1.1 because they may advance asynchronously.
