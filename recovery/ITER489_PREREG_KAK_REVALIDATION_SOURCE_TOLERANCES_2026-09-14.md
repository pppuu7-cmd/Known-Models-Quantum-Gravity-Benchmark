# Iter489 preregistration — KAK revalidation with source-inherited SU(2) tolerances

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Parent authority and causal failure
Iter487 run `34789538305` has exactly five invalid lanes because the inherited absolute KAK reconstruction residual marginally exceeded `<1e-8` in double precision. Iter488 preregistered an independent 100-digit recheck and established that the same edge matrices reconstruct with max residual `7.683988423157631e-10 < 1e-8` and beta agreement at about `3.62e-12`, but Iter488 itself cannot revalidate the lanes because it introduced a new, unnecessarily stronger SU(2) determinant predicate `<1e-30`. The observed determinant residual is about `2.77e-12`, inherited from representing the original double-precision edge matrices, not from KAK reconstruction failure.

Iter488 is therefore terminal `NUMERICAL_OR_SOURCE_FAIL_ITER488_KAK_REVALIDATION`; its preregistered `<1e-30` predicate is not weakened or retroactively changed.

## Purpose
Run a new prospective validation-only gate using the original Iter487 KAK reconstruction threshold and the already-qualified source Iter484 SU(2) numerical tolerance. No Iter487 scientific observable, path, panel, rho, causal pattern, Haar factor, slope threshold, or classifier changes.

## Frozen object
Exactly the same two unique invalid geometries `C-s2` and `C-s3`, covering the five Iter487 invalid lanes. Use the identical 100-decimal-digit complex-SVD/KAK calculation of Iter488 on the exact decimal representation of the same double-precision edge matrices at `R={6,8,10,12}`.

## Frozen predicates
A geometry passes iff:
1. high-precision absolute KAK reconstruction max residual `<1e-8` — exactly the Iter487 predicate;
2. high-precision U1/U2 unitarity residual `<1e-10`;
3. high-precision U1/U2 determinant residual `<1e-10` — inherited from the qualified Iter484 source KAK gate, not fitted to Iter488;
4. all 40 edge/R objects finite;
5. high-precision beta agrees with the original double KAK beta to relative or absolute error `<1e-10`.

No numerical threshold may be changed after production.

## Composite Iter487 rule
If both geometries pass, the five pinned Iter487 raw lanes are revalidated only with respect to their sole failed KAK control. Because all their other Iter487 controls already PASS, all 24 Iter487 lanes then count valid. Apply the unchanged Iter487 aggregate classifier to the original 96 raw slope states. A stable NONDECAY witness therefore yields `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489`.

If either geometry fails, Iter487 remains infrastructure/source-blocked.

## Interpretation ceiling
Even a promoted NONDECAY verdict is only a one-dimensional shared-node escape-path obstruction to exponential absolute-envelope decay in the frozen j=1 control layer. It is not an absolute Haar-divergence theorem. Positive-measure angular-neighborhood thickening remains mandatory before any such claim. Spectral integrations, conditional/PV cancellations, and distributional amplitudes remain separate. D7-S2 remains NOT_CLOSED; terminal D7 labels and Candidate Gravity remain forbidden/inactive.