# Frozen RQIR Protocol Reference Ledger

Purpose: point to literal RQIR authority. This file is a ledger, not a redefinition of the protocol.

## Authority snapshot

- Original benchmark branch base in RQIR: `02ad31e89f1df0d5515779e6b7526e8eb5505667` (Candidate Gravity Iteration 561 at branch creation).
- Migrated source benchmark HEAD: `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`.
- External RQIR repository: `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`.
- RQIR `main` observed for KMQGB-002: `5fed1f52c013e9e469be73596e2c80932289c725`.
- KMQGB repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.

## Literal authority recovered in KMQGB-002

### Q1–Q7 and base residual

External path: `README.md`
Blob SHA on observed RQIR main: `e431df35d929aa8b06b1b1369a2dc80352efe9e9`.

The repository literally defines the initial channels:
- Q1 quantum clocks / proper time;
- Q2 superposed sources;
- Q3 backreaction / source rule;
- Q4 gravity-mediated quantum information;
- Q5 geometry fluctuations;
- Q6 causal/process structure;
- Q7 low-energy quantum-gravity EFT.

It also defines the observable residual

`Delta_A = O_A^obs - O_A^baseline`

and requires the baseline attached to each observable to be stated explicitly.

The README calls the channel list provisional; KMQGB therefore treats these names as the recovered Q1–Q7 atlas authority, not as evidence that every later candidate-specific subgate is frozen by the README alone.

### Comparator registry

External path: `candidate_gravity/BASELINE_COMPARATORS.md`
Blob SHA on observed RQIR main: `a2b45188710c885f979123f77fa7aad2273b9983`.
Registry-introduction commit: `fa841b0f5c4dc9a3f17af52f0ec5477c00b1502a` (Iteration 130).

Applicable classes are C0–C6. For the present GR null control the decisive literal entry is:

`C0 — Classical GR / Newtonian gravity`, using the controlled classical limit appropriate to the experimental regime.

The registry requires per-model comparator state among `DISTINCT / DEGENERATE / BLOCKED / N/A` and says a model-specific difference is publishable only at the weakest level justified by the applicable comparator set.

A provenance snapshot is stored locally at `legacy_rqir/BASELINE_COMPARATORS_snapshot.md`.

### Existing-model funnel semantics

External path: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`
Blob SHA on observed RQIR main: `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.
Introduction commit: `af0d9c4bf5385cd788639208ac50367562c82d4d` (Iteration 137).

The audit defines:
- F0 dynamics;
- F1 required limits;
- F2 consistency;
- F3 RQIR hierarchy;
- F4 comparator distinction;
- F5 hard-constraint discriminator/calibration quotient;
- F6 statistical identifiability;
- F7 physical resources.

It explicitly distinguishes consistency failure, comparator/novelty failure, and operational blocking. It also records perturbative quantum-GR EFT as exactly comparator C5 by construction, establishing that exact-comparator identity is a legitimate retained negative/control result rather than a theory inconsistency.

### Current comparator-quotient preflight semantics

External current front: `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, blob observed `3b793e0ba2fe2a5a60d79a2e16472a50247e9271`.
Comparator-preflight introduction commit: `9af20b657eb89114a954b55b75b59bb3cf284777` (Iteration 504).

Current RQIR authority says the concrete Candidate-Gravity `Source/Ward/contact+K2` target and robust comparator-subtracted residual are not yet assembled. Therefore the Candidate-Gravity fixed comparator quotient is currently BLOCKED upstream; missing upstream target is not identity, FAIL, near-degeneracy or novelty failure.

This moving Candidate-Gravity blocker does not prevent a benchmark control that is literally one of the comparator definitions from being classified as comparator identity in the exact declared domain.

## GR null-control closure rule

The benchmark realization `RQIR7-M01-GR-EH-MINK` is four-dimensional classical Einstein–Hilbert GR, Lambda=0, weak-field Minkowski, with conserved ordinary matter source. In the overlapping controlled classical domain, this realization is the literal C0 comparator itself.

Therefore, for observables whose declared baseline is this C0 realization:

`O_A^model = O_A^C0`

and by the repository residual definition:

`Delta_A = O_A^model - O_A^C0 = 0`.

This is an analytic identity, not a tolerance-based numerical PASS. Its terminal KMQGB classification is `EXACT_COMPARATOR_IDENTITY`. It must not be reported as a consistency FAIL or as evidence that GR is generally wrong. Q7 quantum-EFT corrections and other domains outside the declared classical realization are outside this control's scope and require separate concrete realizations.

## Literal-authority table

| Object | Exact authority path | Commit/blob | Recovery state |
|---|---|---|---|
| Candidate Gravity current front | external RQIR: `candidate_gravity/recovery/CURRENT_QG_FRONT.md` | blob `3b793e0ba2fe2a5a60d79a2e16472a50247e9271` at observed main | RECOVERED / moving external authority |
| Q1–Q7 definitions + base residual | external RQIR: `README.md` | blob `e431df35d929aa8b06b1b1369a2dc80352efe9e9` | RECOVERED |
| Comparator registry C0–C6 | external RQIR: `candidate_gravity/BASELINE_COMPARATORS.md` | blob `a2b45188710c885f979123f77fa7aad2273b9983`; intro commit `fa841b0...` | RECOVERED |
| Existing-model F0–F7 funnel semantics | external RQIR: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md` | blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`; intro commit `af0d9c4...` | RECOVERED |
| Candidate fixed-comparator preflight taxonomy | Iteration-504 commit plus current front | commit `9af20b657eb89114a954b55b75b59bb3cf284777` | RECOVERED |
| Full candidate-specific Source/Ward/contact+K2 assembled target | external RQIR moving downstream chain | not assembled as of Iteration 563 | OPEN FOR CANDIDATE GRAVITY; NOT REQUIRED FOR C0 IDENTITY CONTROL |

## Search/index warning

GitHub text/code search has returned false negatives for terms known to exist in the RQIR repository. Zero code-search hits are not evidence that an authority artifact is absent. Recovery should prefer direct path reads, commit search, commit diffs and recursive tree/path inspection.

## Read-only external-authority rule

KMQGB may fetch/read RQIR authority but MUST NOT write to `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction` as part of benchmark work. If the frozen RQIR protocol itself needs a methodological change, that must be separately authorized/versioned in RQIR, never smuggled in as a benchmark write.

## No-memory rule

If this ledger is incomplete in a future session, do not infer missing definitions from prior chat summaries. Mark the exact item unresolved and continue repository recovery until literal authority is obtained.
