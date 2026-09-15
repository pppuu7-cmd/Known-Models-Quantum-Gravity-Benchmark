# KMQGB Critical Review — laminar-forest scalar transfer before P1

Date: 2026-09-15
Lane: independent Critical Review / Verification
Status: TERMINAL REVIEW

## RESULT_REVIEWED

Latest frozen successor chain:

- scalar Gaussian collision-strata power-count authority: prereg `2f6d3af60439af4bc8b7c62e6813c58fb21ec1f4`, terminal result `81094144184751770256ab3bb144bd9189a6a9ad`;
- exact K5 laminar-forest prereg: `206f662ffca58bb7fae81c0ca4fc650a9b0f9149`;
- laminar implementation/workflow head: `36bc03c6886c761ada6257f3ce799584fbb6664c`;
- authoritative laminar run: `34966138757`, terminal success;
- newest downstream prereg: `research/prereg/SOURCE_J1_K5_FOREST_SUBTRACTION_P1_2026-09-15.md`, commit `a63df1f3c66dbadaec7bbaab2c916cffefb56813`.

## PREREG_CHECK

The laminar gate was prospectively frozen and its implementation matched its own frozen formula. The downstream P1 gate was also prospectively frozen before implementation.

However, a cross-gate object-identity mismatch is present and must be resolved before P1 execution.

## OBJECT_IDENTITY_CHECK

The scalar Gaussian power-count gate freezes one scalar normal coordinate per relative vertex displacement:

`d_perp_scalar(S)=|S|-1`.

With edge scaling degree 3, its single-block superficial degree is

`omega_scalar(S)=3*C(|S|,2)-(|S|-1)`.

Therefore the exact scalar subtraction orders are:

- |S|=2: `r=2`;
- |S|=3: `r=7`;
- |S|=4: `r=15`;
- |S|=5: `r=26`.

The full-collision value `26` agrees with the independently terminal full-collision radial action-space authority.

By contrast, the laminar prereg freezes

`d_perp=3(|S|-1)`

and hence orders

`0,3,9,18`.

Those are a three-normal-dimensions-per-relative-vertex burden, not the frozen scalar Gaussian power count. The laminar combinatorics are valid, but its subtraction-order table is not same-realization authority for the scalar P1 calculation.

## FOREST-CENSUS CHECK

Authoritative run `34966138757` reports exactly:

- 26 connected subsets including full `V`;
- 472 laminar forests including the empty forest and forests containing `V`;
- histogram `{0:1,1:26,2:130,3:210,4:105}`;
- 24 S5 orbits.

Because the full set `V` is compatible with every proper forest, adjoining/removing `V` is a bijection between proper-only forests and forests containing `V`. Hence the exact proper-only census required when full-collision subtraction is kept distinct is:

- proper connected subsets: 25;
- proper-only forests: `472/2 = 236`;
- histogram `{0:1,1:25,2:105,3:105}`;
- S5 orbits: 12.

The downstream P1 prereg says both (i) subtraction over **proper** connected collision subsets with full collision distinct and (ii) expected upstream census 472. These cannot be the same forest family.

## SOURCE/REALIZATION_CHECK

`QUALIFIED`.

The 472-forest topology and S5 combinatorics survive as an exact K5 combinatorial certificate. The `0,3,9,18` order table is a different normal-dimension realization and must not be transferred into the scalar Gaussian P1 gate.

## PROVENANCE_CHECK

PASS. The discrepancy is visible directly in prospectively frozen repository authorities and authoritative Actions output; it is not inferred from partial/nonterminal values.

## COUNTEREXAMPLE_ATTEMPTS

1. **Could `3(|S|-1)` still describe the scalar Gaussian object?** No. The scalar parent explicitly freezes `d_perp=sum(s_i-1)` and treats importing 3D thresholds as an adversarial implementation error.
2. **Could 472 still be the proper-only forest count?** No. The authoritative 472 census includes `V`; exact deletion/adjoining of `V` gives proper-only count 236.
3. **Could this be only wording with no numerical effect?** No. The subtraction orders change from `0,3,9,18` to `2,7,15,26`, including the full-collision order already independently fixed as 26.

## OVERCLAIM_CHECK

No model/family conclusion follows. This is a same-realization/protocol qualification only.

## VERDICT

`REQUIRES_NEW_PREREGISTERED_GATE`

Do not execute `SOURCE_J1_K5_FOREST_SUBTRACTION_P1_2026-09-15.md` as written. Its forest topology can be reused, but the scalar subtraction-order authority and proper-only forest census must first be repaired prospectively.

## QUALIFICATIONS

- historical laminar combinatorial certificate remains valid for K5 topology;
- historical `0,3,9,18` orders remain valid only for the separately frozen 3-normal-dimensional burden encoded by that gate;
- they are not scalar Gaussian P1 subtraction orders;
- no historical file is rewritten.

## UPDATED_STATE

- scalar Gaussian proper-stratum forest subtraction: NOT YET AUTHORIZED;
- exact scalar orders required: `{2:2,3:7,4:15,5:26}`;
- exact proper-only forest count required: `236`;
- D7-S2 = NOT_CLOSED;
- D7-S3 = NOT_CLOSED;
- D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED;
- terminal selectors remain forbidden;
- Candidate Gravity remains inactive.

## NEXT_ADMISSIBLE_GATE

Prospectively freeze and execute a cheap exact `SCALAR_K5_LAMINAR_FOREST_ORDER_REPAIR` certificate that reuses only the dimension-independent K5 laminar topology, independently recomputes scalar orders and proper-only census, and cross-locks the full-collision order to 26. Only a terminal PASS may authorize a corrected numerical P1 forest-subtraction gate.