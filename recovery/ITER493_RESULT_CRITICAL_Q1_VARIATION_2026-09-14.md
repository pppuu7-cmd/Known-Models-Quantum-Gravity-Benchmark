# Iter493 Result — Critical q=1 local variation

Date: 2026-09-14

## Authoritative provenance
- Preregistration: `c372ae3b662349203aa39501696ea57aceeb77b5`
- Evaluator: `bfed21574f3d5ea80f2695009561c22dc5efefea`
- Aggregate implementation: `7a1759bb3baafd7f585fdb1178230069bdeab129`
- Workflow/source-lock repair head: `38f67256aae6b778ad748baa2135340ad0968c1b`
- Run: `34797703185`
- Source-lock job: `103833913367`
- Aggregate job: `103834905468`
- Aggregate artifact: `10330606775`
- Aggregate digest: `sha256:9ee36ed509ccfe8c4e95f0e5529cd2a97abef3024a02aa779b944a7cdbc471bb`

## Terminal classification
`ITER493_CRITICAL_Q1_LOCAL_VARIATION_QUALIFIED_SCOPED`

All 12 scientific jobs are terminal success and the aggregate reports `valid=true`, `missing_jobs=[]`, `invalid_jobs=[]`, with 240 causal×coordinate×rho states.

## Measured response
- max |D| = `0.01004981469607813`, at causal `1to4`, coordinate 6, rho `0.35`, h=0.005;
- median |D| = `0.00020609675681626527`;
- max |Q| = `1.9784279772139257`, at causal `0to5`, coordinate 11, rho `2.7`, h=0.010;
- median |Q| = `2.417976929791621e-07`;
- first-variation sign stable count = `236`;
- max D scaled two-step discrepancy = `0.009900740244983552`;
- max Q scaled two-step discrepancy = `1.001460062345629`.

The per-coordinate response norm is strongly anisotropic. The largest coordinates include 6 (`0.016470714781515138`), 1 (`0.016242273463595223`), 5 (`0.015593487075849226`), and 0 (`0.013335011284272193`), while several coordinates are below `0.001`.

## Scientific interpretation
The q=1 shrinking boundary layer has a finite spanning-basis local response but is not isotropic. A single median or scalar local-response surrogate is therefore not sufficient for a uniform neighborhood certificate. The large second-variation extremum and large two-step Q discrepancy require explicit mixed/block curvature control before any Taylor/Lipschitz enclosure can be trusted.

This result is a finite-grid local first/second variation diagnostic only. It is not an interval proof, not an open-neighborhood or positive-measure theorem, not a Haar convergence/divergence theorem, and does not close D7-S2.

## Locks
D7-S2 remains `NOT_CLOSED`; D7-S3 remains `NOT_CLOSED`; D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 labels remain forbidden. Candidate Gravity remains inactive.
