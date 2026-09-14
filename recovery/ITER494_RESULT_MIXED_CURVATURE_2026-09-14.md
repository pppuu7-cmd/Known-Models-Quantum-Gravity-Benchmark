# Iter494 Result — Critical q=1 mixed-curvature audit

Date: 2026-09-14

## Authoritative provenance
- Preregistration: `ad699fe7f6bfadbafb11a79607fbaaa5aa2de517`
- Evaluator: `fe0c98b2a4f36b026401b3f6549eef7026b367a0`
- Aggregate implementation: `97a509a1330ed5e6296344611a090c260d3f31e9`
- Initial workflow head: `d37ea411509b1993ccf40898e791e10c36669872`
- Source-lock-only repair / authoritative production head: `f7570e994a4ac7919de66d7aa6918a71fb3296a7`
- Authoritative retry run: `34800831631`
- Source-lock job: `103843009836`
- Aggregate job: `103843648511`
- Aggregate artifact: `10331736755`
- Aggregate digest: `sha256:a04710304e7e9f4cf1e49c19ed6192ab5da7ea65be6b99bf3b78cebbc6cc9ed8`

The initial run `34800772592` is infrastructure/source-lock failure only: its literal source-lock assertion was case-sensitive and scientific lanes did not start. The repair changed only that text assertion; no frozen scientific equation, coordinate set, pair set, h value, threshold, or interpretation rule changed.

## Terminal classification
`ITER494_CRITICAL_Q1_MIXED_CURVATURE_QUALIFIED_SCOPED`

All 9 scientific jobs and source lock are terminal success. The aggregate consumed all 9 raw artifacts, reports `valid=true`, `missing_jobs=0`, `invalid_jobs=[]`.

## Measured mixed response
- max |M| = `1.9656594047123832`;
- median |M| = `0.00031101842767888854`;
- max scaled two-step discrepancy = `0.8247973630248762`;
- mixed-curvature sign stable count = `167/180`;
- extremum: causal `0to5`, pair `[5,11]`, rho `2.7`, h=`0.005`, M=`1.9656594047123832`.

Per-coordinate mixed-response norms on the frozen active set:
- coordinate 0: `3.404527266034276`;
- coordinate 11: `3.0664848676705594`;
- coordinate 5: `3.0099854947152385`;
- coordinate 1: `1.9891934011830081`;
- coordinate 6: `0.631774620483148`;
- low-response control coordinate 3: `0.008889221371979386`.

## Scientific interpretation
Mixed q=1 angular curvature is finite on the prospectively frozen active-pair set but is strongly anisotropic and in some channels of order unity. The result rules out treating the local q=1 response as diagonal or separable for a validated Taylor/Lipschitz envelope. The finite-grid data now justify a prospectively frozen multivariate Taylor-envelope stress/certification stage that explicitly includes diagonal and mixed terms and a separately bounded remainder.

This result is not itself an interval proof, open-neighborhood theorem, positive-Haar-measure theorem, Haar convergence/divergence theorem, or D7-S2 closure.

## Locks
D7-S2 remains `NOT_CLOSED`; D7-S3 remains `NOT_CLOSED`; D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 labels remain forbidden. Candidate Gravity remains inactive.
