# Iter487 / Iter489 — shared-node Haar escape result after numerical revalidation

Date: 2026-09-14

## Authoritative provenance
### Iter487 frozen science object
- prereg: `5a7bc8e909bfa7a0b9a865a372e112eebe81654f`
- evaluator: `8fd2ed5268180d7c26440b5dee4fa85b986a3e85`
- aggregate classifier: `54bfaef89f55be4dd636750af4c35bb2fd87d599`
- workflow/head: `2af59f62b841b3cdf2731040968105c2edaac4a5`
- run: `34789538305`
- aggregate artifact: `10327910402`
- digest: `sha256:a17235d63f4f645a81bd2dc7222245724847e5c02530ab26cacb6675a877b467`

Iter487 produced all 24 raw lanes. Its native aggregate remained `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487` because exactly five C-panel lanes marginally failed the inherited absolute `per_edge_kak_reconstruction < 1e-8` numerical control. G1/G2 scale-normalized nonrepresentation controls passed in those lanes.

### Iter488 diagnostic
Iter488 prereg `20d2869dc75944d57b324809dd75ddadbc7dbdd3`, implementation `6e1f28d7a35ea6e370c888cf545c318fa14f6ff4`, aggregate implementation `a70f31740be10ffa2701478108deffc5a9bfcdb1`, workflow `6834abb6be98c90e8500d8ff1a9871ce06335d7a`, run `34791234938`.

Iter488 demonstrated high-precision KAK reconstruction max `7.683988423157631e-10 < 1e-8` and beta relative agreement `3.6217442414342312e-12`, but its own prospectively frozen extra SU(2) determinant predicate `<1e-30` failed because the original double-precision edge matrices carry determinant roundoff about `2.7732216551785787e-12`. Iter488 is therefore retained as `NUMERICAL_OR_SOURCE_FAIL_ITER488_KAK_REVALIDATION`; its criteria are not changed post hoc.

### Iter489 authoritative numerical revalidation
- prereg: `5ccd329f786c785dfdc48f587c6aeb3d563caf7a`
- evaluator: `223c8076cbe6dcae6b9f2a0ca55cb44f2db48774`
- aggregate: `754a1c3ea6eda6fa24b66898f036d2bc6e2158e6`
- workflow/head: `8f8db82644a411d1f949010e89161a095874a856`
- run: `34791322555`
- source-lock job: `103815965889`
- C-s3 geometry job: `103815991452`
- C-s2 geometry job: `103815991538`
- aggregate job: `103816058873`
- C-s3 artifact: `10328596923`, digest `sha256:a2f7eced233e81cab9897baa8625cbb41939408f02b1e24b7b4eaf7bd4c7d13b`
- C-s2 artifact: `10328317703`, digest `sha256:f72a91bd0d2614b8a348c94916ea7f9317efed0d1af7043317392bf66b082875`
- aggregate artifact: `10328187668`, digest `sha256:897f4c4f9dc8927c3872f01ba6e678552367819f70aee342192f904b850b78fb`

Both unique invalid geometries pass the source-inherited numerical controls: high-precision KAK reconstruction max `7.683988423157631e-10`, SU(2) determinant residual max `2.7732216551785787e-12 < 1e-10`, unitarity residual max `7.85803831506564e-101`, beta relative error max `3.6217442414342312e-12`. Therefore all five formerly invalid Iter487 lanes are revalidated with no change to any Iter487 scientific observable or threshold.

## Scientific classification
Applying the unchanged frozen Iter487 aggregate rule to the original 96 raw `(lane,rho)` states yields:

`SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489`

There are valid stable NONDECAY witnesses. In particular all six frozen `s=4` lanes (`A/C` x three causal patterns) contain stable NONDECAY points with post-Haar actual slopes approximately `+4`, while `s=1` lanes decay and parts of `s=3` remain asymptotically marginal/inconclusive. This is a genuine negative result for the hypothesis that every prospectively frozen shared-node escape path has exponentially decaying absolute envelope.

## Interpretation ceiling
This result is only a one-dimensional escape-path obstruction in the frozen `j=1` full shared-node/intertwiner control layer. A path has zero angular measure. It is **not** yet an absolute Haar-divergence theorem and does not establish divergence/finiteness of the physical causal vertex. Before any absolute Haar conclusion, the NONDECAY witness must be thickened to a prospectively frozen positive-measure angular neighborhood with uniform lower-bound/stability controls. Ten source spectral integrations, conditional/PV cancellations, and distributional boundary values remain separate.

D7-S2 remains `NOT_CLOSED`; D7-S3 remains `NOT_CLOSED`; D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 classifier and all four terminal labels remain forbidden. Candidate Gravity remains inactive.
