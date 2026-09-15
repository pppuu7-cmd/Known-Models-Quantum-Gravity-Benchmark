# SOURCE_J1_K5_SCALAR_LAMINAR_FOREST_ORDER_REPAIR — terminal result

Date: 2026-09-15
Status: TERMINAL

## Authority

- Gate: `SOURCE_J1_K5_SCALAR_LAMINAR_FOREST_ORDER_REPAIR`
- Frozen preregistration: `research/prereg/SOURCE_J1_K5_SCALAR_LAMINAR_FOREST_ORDER_REPAIR_2026-09-15.md`
- Preregistration commit: `21af89b35639d0e4a854a53cf6cd3219437bd4b2`
- Implementation commit: `6c65db48570a638976d822cc1c68ae6d21101079`
- Workflow head: `eea26abe7b70c038e686078016acc17943f28c13`
- Authoritative run: `34990564375`
- Source-lock job: `104453810970` — success
- Python 3.11 job: `104453877848` — success
- Python 3.12 job: `104453877772` — success
- Python 3.11 artifact: ID `10405482268`, digest `sha256:6747dad1f1f3a1f054ac81baf9acfa7866e11dacd55517ffd13b15375a2a5917`
- Python 3.12 artifact: ID `10404989465`, digest `sha256:ac7ac0c8d26d5e8de171b34150c89228f042865c1fa9acec1de2e9ccba6a0488`

## Frozen terminal classification

`SCALAR_K5_LAMINAR_FOREST_ORDER_REPAIR_CONFIRMED_SCOPED`

Both independent Python lanes emitted the same exact scientific payload and all frozen controls passed.

## Exact same-realization certificate

For the auxiliary scalar Gaussian K5 realization:

`omega_scalar(S) = 3*C(|S|,2) - (|S|-1)`.

Therefore the exact subtraction orders are:

- `|S|=2 -> r=2`;
- `|S|=3 -> r=7`;
- `|S|=4 -> r=15`;
- `|S|=5 -> r=26`.

The full-collision value `26` independently matches the terminal full-collision radial action-space authority.

The historical three-normal-dimensional realization was reproduced as the mandatory negative control:

- `|S|=2 -> r=0`;
- `|S|=3 -> r=3`;
- `|S|=4 -> r=9`;
- `|S|=5 -> r=18`.

It is therefore explicitly distinguished from the scalar realization rather than silently transferred.

## Exact forest topology

The dimension-independent all-subset K5 topology was independently reconstructed and reproduced the earlier exact certificate:

- connected-subset census `{2:10,3:10,4:5,5:1}`;
- all forests including empty and allowing full `V`: `472`;
- all-forest cardinality histogram `{0:1,1:26,2:130,3:210,4:105}`;
- all-forest S5 orbit count: `24`;
- all-forest record digest: `sha256:e5aa8396667ba532c50f372b464083c9cf85ba46e2db2e91f30a0febce5d7616`.

Keeping full collision distinct gives the exact proper-only topology needed downstream:

- proper connected subsets: `25`;
- proper-only forests including empty: `236`;
- proper-only cardinality histogram `{0:1,1:25,2:105,3:105}`;
- proper-only S5 orbit count: `12`;
- proper-only orbit-size histogram `{1:1,5:1,10:3,15:2,20:1,30:3,60:1}`;
- proper-only forest record digest: `sha256:5d1e124067d8a4dec8e0dafeb84c3fa2cdcab51e34a4be7b6c0b85fe623b5273`.

Adding/removing the full set `V` was checked as an exact bijection between proper-only forests and forests containing `V`.

## Controls

All frozen controls passed, including:

- exact subset census;
- historical 472-forest topology lock;
- exact proper-only enumeration;
- full-set bijection;
- all/proper S5 orbit counts;
- all 120 relabeling invariance checks;
- scalar-order relabeling invariance;
- full-collision order-26 cross-lock;
- explicit three-normal-dimensional negative control;
- overlapping-nonnested rejection;
- disjoint-pair acceptance;
- full-set exclusion from proper-only forests.

## Consequence

The latest historical downstream preregistration

`research/prereg/SOURCE_J1_K5_FOREST_SUBTRACTION_P1_2026-09-15.md`

at commit `a63df1f3c66dbadaec7bbaab2c916cffefb56813` is **not executable scientific authority as written**. It mixed the scalar Gaussian object with the three-normal-dimensional order table `0,3,9,18` and referred to the 472 all-forest census while simultaneously requiring proper-stratum subtraction with full collision distinct.

That preregistration remains immutable historical provenance; it is superseded for future execution by the critical qualification at commit `0d683f0be541e4fed487a922a8569d3f730808bd` and this terminal repair.

## Interpretation ceiling

This result establishes only exact same-realization forest topology and subtraction-order metadata for the auxiliary scalar Gaussian K5 object. It does not:

- define or execute a forest subtraction operator;
- establish post-subtraction convergence or divergence;
- establish Eq. (4) existence/nonexistence;
- fail a QG model or family;
- close D7-S2/S3/S4;
- authorize `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`;
- activate Candidate Gravity.

## Next admissible gate

Prospectively define and exact-audit a **scalar K5 forest subtraction operator** before any expensive P1 numerical campaign. The operator gate must freeze:

1. the scalar normal-coordinate projection/contraction for every proper subset;
2. the Taylor projector and scalar orders `2/7/15`;
3. the separate full-collision root order `26`;
4. composition on nested/disjoint laminar subsets;
5. S5 covariance modulo the fixed gauge;
6. the exact proper-forest formula over the 236 proper-only forests.

Only a terminal operator-definition PASS may authorize a corrected numerical P1 forest-subtraction gate.

Governance remains unchanged: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors forbidden; Candidate Gravity inactive; KMQGB remains downstream of pinned DSIR authority.