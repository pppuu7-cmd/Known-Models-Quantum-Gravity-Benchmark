# SOURCE_J1_K5_SCALAR_LAMINAR_FOREST_ORDER_REPAIR — prospective freeze

Date: 2026-09-15
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT

## HYPOTHESIS

The dimension-independent K5 laminar topology from run `34966138757` can be reused for the auxiliary **scalar** Gaussian realization, but the subtraction orders must be recomputed with one scalar normal coordinate per relative vertex displacement. A correct same-realization certificate should therefore preserve the forest topology while replacing the historical three-normal-dimensional order table by the scalar table.

## OBJECT

K5 vertex set `V={0,1,2,3,4}` with one scalar coordinate per free relative vertex. Every subset `S` with `2<=|S|<=5` is connected. A forest is a laminar family of such subsets: for every `A,B`, either `A subset B`, `B subset A`, or `A intersection B = empty`.

Two forest families must be kept distinct:

1. **all forests**, where the full set `V` may occur, used only to cross-check the historical topology certificate;
2. **proper-only forests**, built only from `S proper subset V`, which are the topology authorized for subsequent proper-stratum subtraction. Full-collision subtraction is not part of a proper-only forest.

## DEPENDENCY

- scalar collision-strata authority: prereg `2f6d3af60439af4bc8b7c62e6813c58fb21ec1f4`, terminal child `81094144184751770256ab3bb144bd9189a6a9ad`;
- exact full-collision radial action-space terminal authority `5e95318f29e26f4ea954f269cbec2c69fa8089d8`, which independently locks the scalar full-collision derivative-order cap to 26;
- dimension-independent laminar topology workflow head `36bc03c6886c761ada6257f3ce799584fbb6664c`, authoritative run `34966138757`;
- critical qualification `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_LAMINAR_FOREST_SCALAR_TRANSFER_2026-09-15.md`, commit `0d683f0be541e4fed487a922a8569d3f730808bd`.

The downstream prereg `SOURCE_J1_K5_FOREST_SUBTRACTION_P1_2026-09-15.md` is not executable authority until this repair closes.

## SOURCE / REALIZATION AUTHORITY

For the scalar Gaussian object freeze:

- edge scaling degree `sd_edge = 3`;
- scalar normal dimension `d_perp(S)=|S|-1`;
- internal edges `E_int(S)=C(|S|,2)`;
- superficial degree `omega_scalar(S)=3*E_int(S)-d_perp(S)`;
- subtraction order `r_scalar(S)=max(0, floor(omega_scalar(S)))`.

No 3D threshold or physical EPRL normal dimension may enter the deciding scalar table.

## FROZEN INPUTS

- vertices exactly `0..4`;
- connected subsets exactly all subsets of sizes 2,3,4,5;
- proper subsets exactly sizes 2,3,4;
- laminar compatibility exactly nested-or-disjoint;
- all 120 S5 relabelings for orbit/invariance checks;
- exact integer arithmetic only.

## POSITIVE CONTROLS

1. subset census `{2:10,3:10,4:5,5:1}`;
2. historical all-forest topology is independently recomputed as 472 with histogram `{0:1,1:26,2:130,3:210,4:105}`;
3. proper-only forest census is independently recomputed, not hard-coded as the deciding result;
4. adding/removing full `V` gives a bijection between proper-only forests and forests containing `V`;
5. all-forest S5 orbit count reproduces 24;
6. all scalar orders are invariant under all 120 relabelings;
7. full-collision scalar order is exactly 26, matching the independent full-collision parent authority;
8. direct formula and per-subset enumeration agree for every subset.

## NEGATIVE / ADVERSARIAL CONTROLS

1. replacing scalar normal dimension `|S|-1` by `3(|S|-1)` must reproduce the distinct historical order table `{2:0,3:3,4:9,5:18}` and therefore be detected as a different realization;
2. overlapping nonnested pair `{0,1}` and `{1,2}` must be rejected;
3. disjoint pair `{0,1}` and `{2,3}` must be accepted;
4. if full `V` is accidentally admitted into a proper-only forest, the proper-only census guard must fail.

## PASS

`SCALAR_K5_LAMINAR_FOREST_ORDER_REPAIR_CONFIRMED_SCOPED` iff all controls pass, exact all-forest topology agrees with the historical dimension-independent certificate, proper-only topology is separately enumerated, and scalar subtraction orders are exactly those derived from the frozen scalar formula.

## FAIL

`SCALAR_K5_LAMINAR_FOREST_ORDER_REPAIR_CONTRADICTION` iff exact enumeration/control logic is valid but the frozen scalar identities contradict the stated scalar parent authorities.

## BLOCKED / INVALID

`SCALAR_K5_LAMINAR_FOREST_ORDER_REPAIR_BLOCKED` iff exact exhaustive enumeration cannot complete for an identified computational reason.

`INVALID_IMPLEMENTATION` for wrong vertex set, wrong laminar relation, imported 3D order as scalar authority, failed topology lock, failed S5 invariance, hard-coded deciding census without reconstruction, or any floating-point decision.

## INTERPRETATION CEILING

PASS establishes only the exact same-realization forest topology/order metadata needed to define a later auxiliary scalar Gaussian forest-subtraction computation. It does not execute a forest subtraction, establish convergence/divergence after subtraction, prove Eq. (4) existence/nonexistence, fail a model/family, close D7, authorize a terminal selector, or activate Candidate Gravity.

A terminal PASS authorizes a **new corrected prospectively frozen P1 forest-subtraction gate**. That successor must define the actual subtraction operator/normal-coordinate projection before numerical execution and must keep full-collision subtraction distinct from proper-stratum forests.