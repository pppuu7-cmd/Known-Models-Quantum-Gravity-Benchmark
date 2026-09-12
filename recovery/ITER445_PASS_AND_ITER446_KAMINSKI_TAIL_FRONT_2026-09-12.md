# KMQGB recovery delta — Iter445 PASS and Iter446 Kaminski tail-comparison front

Date: 2026-09-12

## Iter445 — terminal PASS: exact reach of the single-factor K5 escape-envelope proof

- Branch: `research/iter445-cut-cone-envelope-reach`
- Head: `2057a0a63392e19180fee62e59288ba10be5702b`
- Workflow run: `34718098637`
- Run conclusion: `success`
- Summary artifact: `iter445-summary`
- Artifact id: `10305991520`
- Artifact digest: `sha256:4777073debcce37e9a2dbe9eabb5aecd444fc6219b256ab86af8a7f9833dd92c`
- Controls: valid.

Exact common-shift K5 envelope table:

| escaping unfixed vertices k | crossing edges k(5-k) | Haar exponent 2k | net exponent k(k-3) | certificate |
|---:|---:|---:|---:|---|
| 1 | 4 | 2 | -2 | `SUFFICIENT_BY_THIS_BOUND` |
| 2 | 6 | 4 | -2 | `SUFFICIENT_BY_THIS_BOUND` |
| 3 | 6 | 6 | 0 | `UNRESOLVED_BY_THIS_BOUND` |
| 4 | 4 | 8 | 4 | `UNRESOLVED_BY_THIS_BOUND` |

Classification:
`EXACT_K5_SINGLE_FACTOR_ENVELOPE_CERTIFICATE_COVERS_K1_K2_ONLY__K3_K4_REQUIRE_STRONGER_CORRELATED_OR_ANGULAR_BOUND`.

Scientific interpretation: Iter443 plus this exact cut-cone audit shows that the conservative product of independent one-factor `M(beta)~exp(-beta)` envelopes is already sufficient for one- and two-variable common-shift escape classes, but mathematically insufficient to decide three- and four-variable simultaneous escape. The nonnegative k=3/k=4 exponents are **not** a divergence theorem, scientific FAIL, or no-go. They identify the exact point where a correlated graph-integral/angular/intertwiner bound is required.

Frozen state after Iter445:
- D7-S2: `BLOCKER_LOCALIZED_TO_K3_K4_CORRELATED_MULTI_GROUP_DIRECTIONS_BUT_NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S5: `NOT_AUTHORIZED`
- Candidate Gravity: inactive / not authorized.

## New source-backed correlated-bound route — Iter446

A stronger route is now preregistered on branch `research/iter446-kaminski-tail-comparison`.

Workflow run: `34718261533`.
Frozen contract: `benchmarks/lqg_iter446_kaminski_tail_comparison_contract.json`.
Implementation: `code/lqg_iter446_kaminski_tail_comparison.py`.

### Source logic

1. Kamiński's EPRL integrability proof does not decide the graph integral by multiplying independent radial asymptotics. It derives a uniform hyperbolic edge comparison kernel of the form
   `(cosh r_e)^(-(1-tau))`
   and proves the corresponding correlated graph integral finite for every 3-edge-connected graph.
2. For K5, `|E|=10`, hence the frozen comparison value is `tau=1/(2|E|)=0.05`, comparison exponent `1-tau=0.95`.
3. The 2026 Toller source gives an exact Cartan/KAK expression of every `T+/-` matrix element as a finite sum of compact SU(2) Wigner matrices multiplying reduced `t+/-_m(beta)` functions. Compact Wigner entries are bounded and the magnetic sums are finite at fixed labels.
4. The same source states the worst large-beta reduced Toller decay is `exp(-beta)`, strictly stronger than the required comparison exponent `exp(-0.95 beta)`.
5. Therefore, for every fixed collision exclusion `delta>0`, continuity on `beta>=delta` plus the stronger source asymptotic permits a finite label-dependent comparison constant `C_delta`. On the collision-excised K5 domain, the absolute fixed-label causal integrand can then be compared to the Kamiński 3-edge-connected hyperbolic kernel.

This is an explicit new comparison construction. It is **not** the invalid automatic transfer rejected by Iter304 and does not require pretending an individual Toller branch is an SL(2,C) representation.

### Critical scope lock

Iter446 intentionally excludes relative-rapidity collision loci `r_ab -> 0`. This is necessary because earlier KMQGB short-distance witnesses found potentially singular fixed-causal local objects, and the later invariant-projector audits did not constitute a full proof of collision integrability.

A PASS of Iter446 may therefore establish only:
`SOURCE_BACKED_CAUSAL_K5_COLLISION_EXCISED_DOMAIN_ABSOLUTELY_INTEGRABLE_BY_KAMINSKI_COMPARISON`.

It would localize the remaining fixed-label causal-vertex finiteness problem to pair/multi-pair collision neighborhoods. It may not be promoted to full causal-vertex finiteness, generalized-vertex normalization, spin/refinement-sum convergence, causal-stack cutoff removal, terminal D7, or Candidate Gravity activation.

## Concurrent Iter444 status

Iter444 remains the independent direct two-group source-envelope stress test. It is scientifically complementary to Iter446: Iter444 samples a controlled two-variable noncompact geometry, while Iter446 attempts the source-backed correlated graph-integral comparison needed to cover the k=3/k=4 asymptotic cones outside collision tubes.

Do not launch terminal D7 while S2-S4 remain open.
