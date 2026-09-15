# Current Benchmark Front
Updated: 2026-09-15

## Authoritative main
Recovered main head at synchronization start: `811ddbe3591078970b48bd1023947d468f4d8b8c` (`recovery: advance index with source-order collision theorem`). The more recent immutable active-front authority is `recovery/CURRENT_ACTIVE_FRONT_INDEX_2026-09-15.md`; this file had lagged at Iter500 and is synchronized here before Critical Review.

## Active Research execution
Iter504 is prospectively frozen by `recovery/ITER504_PREREG_CENTERED_FULL_MAX_ENVELOPE_SCIENCE_2026-09-15.md`, prereg commit `1ab46b7add51b36b5499f866eb4579137838bfae`, production head `56362459a826e3e376c529446678f2fbcaa269ae`, workflow `iter504-centered-full-max-envelope-science`, run `34907349374`. At the latest consumed active-front snapshot the source lock and all 12 point-regression jobs had succeeded while the 96 centered box-shard matrix was still running/queued and no aggregate verdict existed. No partial Iter504 substantive values may be used and no competing Iter504 verdict may be created while that frozen run is non-terminal.

## Newest substantive Research result eligible for independent review
`research/SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM_2026-09-15.md`, result commit `bf43183b12799e217e452c6335edc1114e389352`, claims a scoped ordinary absolute-Haar divergence theorem for fixed j=1 intertwiner channel `00000` at the full K5 collision, for the three frozen causal signatures and nonzero real edge rho.

Its upstream local pole ledger is `research/SOURCE_J1_TOLLER_COLLISION_POLE_LEDGER_2026-09-15.md`, commit `b04229b36b9c5af1aaa9013184fb020c86484309`. Exact certificate code was added at `05483f61a719209ee65d8ef82b2da20880d5f85d`; workflow was added at `020f43695f16332d749f3d6d5c65dbd0b6a098d8`.

The registered exact-certificate run `34908370750` is terminal `failure`, job `104190138562`. Failure occurs in the certificate itself at `np.einsum(...).item()` because the exact object result is already a `fractions.Fraction` and has no `.item()` method. Artifact upload succeeded, but the substantive exact contraction did not complete. Therefore workflow color is not a scientific verdict, and the exact certificate is currently not reproducibly validated by Actions. The active-front index explicitly states that this failure is a reproducibility/code issue that must be resolved before promoting the certificate.

## Source-order analytical separation
`research/SOURCE_ORDER_K5_HAAR_TAIL_SPANNING_TREE_THEOREM_2026-09-15.md` gives a separate scoped theorem: for fixed finite labels and fixed collision cutoff `delta>0`, the source-order noncompact four-group Haar tails are absolutely integrable. It does not remove collision singularities. The new full-collision claim therefore concerns a distinct local mechanism and does not conflict with the tail theorem.

## Independent collision stream
Iter461 remains registered independently on branch `research/iter461-k5-collision-partitions`, head `05c7f87c8519349057332bf90021f1128e1eefc3`, run `34748503239`. Do not duplicate it. The full-collision theorem does not consume or replace Iter461 because the latter is still needed for the remaining collision strata/incidence map.

## Global governance lock
- RQIR Core v1.0 remains FROZEN.
- `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- Terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden while required subgates are open.
- Candidate Gravity remains inactive.
- BLOCKED/INVALID is not scientific FAIL.
- A finite/scoped certificate is not a universal theorem.
- Missing/cancelled objects are not zero residuals.
- Green or red CI is not by itself a physical verdict.

## Immediate review rule
Critical Review should inspect exactly the scoped j=1 full-collision absolute-divergence result. First repair only the non-contract certificate execution defect if possible, then adversarially test object identity, source/realization, basis/index conventions, local normal-measure argument, causal branch signs, open-cone uniformity, and scope ceiling. No threshold, object, hypothesis, channel, causal signature, or interpretation ceiling may be changed retroactively.
