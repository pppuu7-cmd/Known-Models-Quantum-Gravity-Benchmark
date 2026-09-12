# Iter417 — source-specific sigma-sector multi-collision parity audit

Date: 2026-09-12

Scientific workflow: `lqg-iter417-sigma-sector-collision-parity`
Run: `34668929784`
Head: `80151a3d8b3ad483609ab42867084e700b4e5c85`
Status: **16/16 lanes SUCCESS**

## Frozen question

For the K5 source-specific causal support

`kappa_ab = sigma_a sigma_b`, with the global sigma flip quotiented by fixing `sigma_0=+1`,

does exact summation over the 16 allowed sigma sectors cancel the leading homogeneous coefficient of a simultaneous k-vertex collision, assuming the scoped leading-residue relation

`R_- = - R_+`?

A perturbation scan also replaced this by

`R_- = -(1+epsilon) R_+`,

with `epsilon in {1e-6,1e-3,1e-1}`.

## Exact epsilon=0 result

All K5 vertex subsets were exhaustively enumerated.

| collision size k | subsets | C+ leading sum | C+ + C- leading sum | result |
|---|---:|---:|---:|---|
| 2 | 10 | 0 for all | 0 for all | exact cancellation |
| 3 | 10 | +16 for all | 0 for all | no cancellation inside C+; exact causal/co-causal cancellation |
| 4 | 5 | 0 for all | 0 for all | exact cancellation |
| 5 | 1 | +16 | +32 | **no leading cancellation** |

The k=5 result is the decisive scoped delta: the complete five-vertex K5 collision is not removed by the source-specific sigma-sector sum, nor by adding the co-causal partner, under the frozen leading-residue sign relation.

## Perturbation stress

The cancellation channels are not generic identities under arbitrary branch-residue mismatch. For example at `epsilon=1e-3`:

- k=3: `C+` remains O(1); the `C+ + C-` residual is tiny but nonzero (relative maximum about `1.25e-10` in this multiplicative mismatch model);
- k=5: both `C+` and `C+ + C-` remain O(1), with the combined relative coefficient essentially unity.

Thus the full K5 collision is robustly non-cancelled in this scoped model, while lower-k cancellations rely on the branch relation and/or source-support parity.

## Algebraic explanation

For a k-vertex collision subset S, the product of source edge signs is

`prod_{a<b in S} kappa_ab = prod_{a in S} sigma_a^(k-1)`.

Therefore source-sector summation gives:

- zero for even k<5 because at least one free sigma occurs to odd power;
- a coherent nonzero sum for odd k because every sigma occurs to even power.

For the co-causal partner each singular wedge flips sign, supplying an additional factor `(-1)^{k(k-1)/2}`. This cancels the k=3 coherent term but reinforces the k=5 term because k=5 has 10 singular wedges.

## Classification

`PASS_SCOPED_EXACT_K5_SOURCE_SIGMA_SUPPORT_PARITY_AUDIT__LOWER_COLLISION_LEADING_CANCELLATIONS_EXIST_BUT_FULL_FIVE_VERTEX_COLLISION_LEADING_TERM_SURVIVES_CAUSAL_AND_COCAUSAL_SUM__FULL_DISTRIBUTIONAL_VERTEX_FINENESS_REMAINS_OPEN`

## Scientific boundary

This is **not** a divergence theorem and **not** a no-go theorem for causal spinfoams.

It establishes only that one particular rescue route — exact leading-coefficient cancellation from the source-specific sigma-sector sum — is unavailable for the full k=5 collision under the frozen residue relation. A finite physical vertex could still arise from subleading structure, boundary/intertwiner contractions, angular integration, the full spectral `i epsilon` distributional prescription, or another source-backed cancellation mechanism.

## Consequence for D7-S2

D7-S2 remains `NOT_CLOSED`.

The next high-value object is now sharper:

`FULL_K5_MULTI_WEDGE_DISTRIBUTIONAL_INTERSECTION_CERTIFICATE_UNDER_THE_SOURCE_SPECTRAL_I_EPSILON_PRESCRIPTION_OR_AN_EQUIVALENT_DIRECT_FINITE_NORMALIZED_VERTEX_CERTIFICATE`.

No family promotion and no `NEW_REQUIRED` authorization follow from Iter417.
