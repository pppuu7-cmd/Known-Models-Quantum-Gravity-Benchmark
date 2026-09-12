# KMQGB front/ledger delta — Iter437 result and Iter438 launch

Date: 2026-09-12

## Iter437 terminal result
Authoritative commit `136e14e98fdf7578bda51ffe7b033abcd471af17`; run `34708436997`; aggregate job `103592822379`; summary artifact `10301998704`; artifact SHA256 `d4c9e12fad2c19ad4cb2891178bb4f37b3adea928bcaa5997a49ebac5586e947`.

Scientific classification: `SOURCE_BACKED_SLOW_OBSTRUCTION_SURVIVES_LOCAL_MAGNETIC_CLOSURE`.
Controls valid on all 32 lanes. Exactly 12 source-backed profiles survive the necessary local magnetic-closure filter; 20 are excluded. This narrows the causal-vertex obstruction but does not establish full invariant/Haar/angular survival or physical divergence.

## Iter438 active frontier
Frozen preregistration: `recovery/ITER438_PREREG_EXACT_INVARIANT_PROJECTOR_2026-09-12.md`.
Production code: `code/lqg_iter438_exact_invariant_projector.py`.
Launch commit: `12b8cc8b431078427d649acf0dc8d5748fc840bd`.
Authoritative workflow run: `34709760371`.

Iter438 is restricted to the 12 Iter437 survivors and asks whether at least one globally consistent assignment of free edge magnetic labels has exact nonzero 4-valent SU(2) invariant-projector support at all five K5 vertices. Two complete recoupling schemes are required to agree exactly as an independent control. No threshold tuning is permitted.

## Locked gate state
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S2: `NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`
- terminal classifier `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED`: forbidden
- Candidate Gravity: inactive / unauthorized

Stable working progress rubric after Iter437 remains: D2 82%, D4 68%, D7 48%, overall 63%. Iter438 compute launch alone does not change those percentages.

## Next permitted dependent gate
Only after terminal classification of Iter438: if a nonempty subset survives, preregister the full source-backed SU(2) Haar/intertwiner contraction/angular survival test on that subset; if all are excluded, preserve the scoped negative result and move to an independent finite-beta/Feynman-distributional causal-vertex collision gate rather than retuning boundary spins.