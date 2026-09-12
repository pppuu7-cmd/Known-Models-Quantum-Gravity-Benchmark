# Iter433 Recovery / Front / Publication-Ledger Delta

Date: 2026-09-12

## Iter433 — four-wedge single-group large-boost radial envelope
Authoritative workflow head: `7af1781783c67b538adf0d2f7fa8d42834360e92`
Authoritative compute commit: `ff41d2cf2d8898bf6872055e18159653202757db`
Authoritative run: `34698093631` (`lqg-iter433-toller-radial-envelope`)
Aggregate job: `103565404778`
Aggregate artifact: `10299108942` (`lqg-iter433-summary`)
Aggregate artifact digest: `sha256:66963307d98c1a156f8c4cdc54d2f6a5a7d154171e6ef7104df6103dea81d477`

All 24/24 profiles passed the prospectively frozen numerical/analytic gate. The minimum analytic exponential decay margin after the radial Haar factor was `2.0`; the least-negative final observed slope was `-1.9999999945666158`; the worst final-tail slope error was `1.5498905782705233e-08`, far below the frozen `2e-4` tolerance.

Scientific classification: `PASS_SINGLE_GROUP_LARGE_BOOST_RADIAL_ENVELOPE`.

This closes only the single-tetrahedral-group large-boost radial-tail obstruction for the validated gamma-simple Toller carrier. It is not a causal-vertex finiteness theorem. Finite-beta pole/collision structure, angular correlations, simultaneous multi-group escape rays, boundary-contracted normalized-vertex finiteness, complete-stack cutoff removal, and same-realization UV-to-causal-Regge/GR transport remain open.

## Global locks after Iter433
- D2 = `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D4 = `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7 = `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- D7-S2 = `NOT_CLOSED`.
- D7-S3 = `NOT_CLOSED`.
- D7-S4 = `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5 = `NOT_AUTHORIZED`; D7-S6 = `INACTIVE`.
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain forbidden.
- Candidate Gravity remains inactive.

## Next permitted frontier
The next independent S2 pre-gate is a simultaneous multi-group large-boost escape-ray audit on the same source-faithful Toller carrier. Gauge-fix one K5/4-simplex vertex, boost subsets of the remaining four vertices along a common collinear ray, include the radial Haar growth for every escaping group variable, and use exact gamma-simple Toller kernels on the crossing edges. This tests whether the single-group decay found in Iter433 survives correlated cluster escapes. A failure of the absolute exponential envelope is only an obstruction to that convergence bound; it is not by itself a physical divergence theorem because angular/boundary contractions and distributional/Feynman structure remain separate questions.