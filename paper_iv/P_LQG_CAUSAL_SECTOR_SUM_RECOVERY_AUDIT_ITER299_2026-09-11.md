# Paper IV — LQG causal-sector sum recovery audit (Iter299)

Date: 2026-09-11
Status: SCOPED PASS / FAMILY NONTERMINAL / D7 NOT AUTHORIZED

## Frozen question

After Iter298 established that one fixed causal Toller sector is generically not identical to the full standard EPRL `D`-product, test the exact algebraic recovery route without assuming a physical causal measure:

`D_i = T_i^(+) + T_i^(-)` and therefore whether the unrestricted unit-weight sum over all local Toller sign assignments reconstructs `prod_i D_i`.

## Reproducible result

Scientific run: `34601894692`
Scientific head: `e0ec53785f312871b91307f8df854b4a8edd66c5`
Summary artifact: `10264955714` (`lqg-iter299-summary`)
Artifact digest: `sha256:7db47f3b76568e8de11832c6447c4cb27779bceec41318934a435e12ea178f34`
Raw summary digest: `sha256:5101d4ffce7b2307e035a1a5b64402527712ec90746d6ed47eb6ed1236f96f95`

Four independent guards ran with `fail-fast:false`, `max-parallel:4`, followed by an aggregate dependency barrier. All four guards and aggregate passed. The exact symbolic guard checked wedge counts 1..12, totaling 8,190 formal sector monomials with unit coefficient.

The machine classification is:

`PASS_SCOPED_EXACT_UNRESTRICTED_TOLLER_SECTOR_SUM_RECONSTRUCTS_STANDARD_D_PRODUCT__CAUSALLY_ADMISSIBLE_WEIGHTED_SECTOR_MEASURE_HAN_GLUE_FACTORIZATION_AND_UV_IR_TRANSPORT_REMAIN_UNPROVEN`

## Scientific interpretation

The distributive identity is exact:

`prod_i (T_i^(+) + T_i^(-)) = sum_sigma prod_i T_i^(sigma_i)`.

Thus the algebraic obstruction identified by Iter298 has an exact *formal unrestricted-sector-sum* recovery route. This narrows the remaining blocker: the missing object is no longer merely an unspecified sector sum, but a source-grounded physical theorem identifying the causally admissible sector set/measure and weights/normalization that are compatible with Han's half-link/Haar gluing and face factorization.

The proper-subset guard also confirms, at the generic formal polynomial level, that deleting a sector monomial prevents reconstruction of the full `D`-product unless additional relations/cancellations are proved. This is a generic algebraic witness only, not a no-go theorem for causal spinfoams.

## Fail-closed boundaries

This result does **not** prove:

- that causal consistency permits the unrestricted set of all local sign assignments;
- that the physical causal sector measure equals the unrestricted unit-weight measure;
- that causal-sector weights and normalization reconstruct Han's half-link kernel;
- preservation of Han's face factorization after causal-sector summation;
- finite/normalized `lambda_f`-weighted causal complete-stack amplitudes or cutoff removal;
- same-realization coupling/Immirzi/spin-scale transport from the UV stack sector to causal large-spin Regge/GR;
- a normalized common-domain observable/comparator with propagated uncertainty;
- family-level terminality or D7 authorization.

Missing objects remain `BLOCKED/undefined`, not FAIL.

## D7 consequence

Strict Tier-1 terminal coverage remains `1/15`. D7-S2 and D7-S3 remain open and D7-S4 remains partial. D7-S5 remains `NOT_AUTHORIZED`; Candidate Gravity remains inactive.

## Next permitted gate

`D7_S2_LQG_CAUSALLY_ADMISSIBLE_SECTOR_MEASURE_AND_WEIGHT_NORMALIZATION_COMPATIBLE_WITH_HAN_HALF_LINK_HAAR_GLUE_AND_FACE_FACTORIZATION__THEN_LAMBDA_F_STACK_CUTOFF_CONTROL_AND_SAME_REALIZATION_UV_TO_CAUSAL_REGGE_GR_TRANSPORT`
