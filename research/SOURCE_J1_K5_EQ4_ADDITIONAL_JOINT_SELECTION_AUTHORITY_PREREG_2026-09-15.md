# Preregistration — source j=1 K5 Eq. (4) additional joint-selection authority gate

Date: 2026-09-15
Lane: KMQGB Research / Closure
Status: `PROSPECTIVE_FROZEN`

## HYPOTHESIS

Within the exact validated repository source-authority chain frozen below, there exists at least one genuinely joint Eq. (4) selection rule — not reducible to ten separate one-wedge Toller definitions/uniqueness conditions — whose action on the confirmed full-collision homogeneous witness `Delta(kappa)=c(kappa) delta_N` is source-pinned strongly enough to decide whether its coefficient must vanish.

This gate tests that hypothesis. It does not assume that such authority exists.

## OBJECT

Exactly the object confirmed by the immediately preceding repaired gate and Critic:

- source-order gauge-fixed K5 causal vertex;
- fixed `j=1`;
- fixed nonzero real edge `rho` convention;
- intertwiner channel `00000`;
- full K5 collision stratum `N=K^4`, `K=SU(2)`, inside gauge-fixed `G^4`, `G=SL(2,C)`;
- homogeneous witness `Delta(kappa)=c(kappa) delta_N` with `c=+i` on the 16 constrained causal sign patterns, `c=-i` on their 16 global negatives, and `c=0` otherwise.

The witness is used only as a discriminator of joint selection authority. This gate neither assumes nor proves existence of a base joint extension `E`.

## DEPENDENCY

Required validated dependencies, all immutable before this preregistration:

1. repaired witness result `results/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_RESULT_2026-09-15.md`, terminal result commit `9e4627fd02204b27be3f211660db4c689776d808`;
2. repaired handoff `recovery/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_HANDOFF_2026-09-15.md`, commit `2eb0da9c987eb706df29971ccea29f65928005d7`;
3. independent Critic `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_REPAIR_2026-09-15.md`, commit `97a4821f85f13e6f5c6d41356612c88939d45f2c`, verdict `CONFIRMED_SCOPED`;
4. published i-epsilon scope result `research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md`, terminal source-audit commit `8c6582371d6e763e4f37b30fbe42f67684edcdb7`;
5. one-wedge uniqueness-vs-joint result `research/SOURCE_J1_K5_ONE_WEDGE_UNIQUENESS_VS_JOINT_EXTENSION_RESULT_2026-09-15.md`, terminal result commit `4b8abb10d89e36801012972ec84f34eb722a5b49`;
6. full-collision scaling/extension audit `research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md`, commit `048692cb497ec91a6aa7709e221dc5051a10225f`;
7. historical Iter331 source jet-normalization audit code `code/lqg_iter331_source_jet_normalization_audit.py`, commit `a59b6bdd08c9fd416dd81df32dfe1d612b5f0d9b`, and aggregate `code/lqg_iter331_aggregate.py`, commit `8c0502b7e892354a89d5387c5e789514e1d2a9d9`.

Current-front reconciliation before this preregistration is commits `8def62a58a716e25f33c3f8ce292c0fc3dd5cd18` and `b9d6e680fe62906a628ab02dd9af84dd64f13bc2`.

## SOURCE / REALIZATION AUTHORITY

The scientific source authority for this gate is **only the validated repository source chain above**. No new external paper, secondary summary, private note or unstored chat assertion may be introduced after freezing.

Candidate joint-authority classes to be audited are frozen to exactly:

1. correlated/common multiwedge regulator-removal prescription at Eq. (4);
2. independent multiwedge regulator prescription together with a source-pinned path/order-independence theorem;
3. microlocal product/pullback/extension theorem applying to the correlated ten-wedge source object at the full collision;
4. vertex-level normalization or boundary condition fixing collision-supported terms;
5. nested/forest-compatible collision-stratum gluing condition acting on the full-collision extension;
6. any other explicit source theorem in the frozen corpus that is genuinely joint and whose action on `Delta` is stated or derivable without adding new model data.

One-wedge `i epsilon`, one-wedge Ruhl/Toller uniqueness, the already-tested EPRL independent-sign sum rule, the already-tested fixed-channel conjugation covariance, and coefficient/sign-pattern K5 relabeling are **not** admissible as new joint authority by themselves.

## FROZEN INPUTS

The audit must consume the seven dependency records above at the exact pre-prereg repository state. It must also record fresh status of the independent registered workflows Iter504 `34907349374` and Iter461 `34748503239`, but must not consume partial substantive values from either non-terminal run.

No candidate authority may be added after the audit begins. If a genuinely new source record is discovered outside this frozen corpus, this gate returns a blocker/invalid outcome and a new prospectively frozen gate is required.

## POSITIVE CONTROLS

The audit must correctly recover all of the following already-validated facts:

1. published Eq. (3) `i epsilon` authority is one-wedge, while the displayed Eq. (4) has no already-pinned common ten-wedge regulator/removal path in the audited source result;
2. one-wedge Toller uniqueness leaves the joint collision-extension question open;
3. off-collision fixed-channel data have scaling degree `30` in collision codimension `12`, hence same-scaling local extension ambiguity is not removed by off-stratum data alone;
4. the repaired `Delta` witness is nonzero and survives the already-tested conjugation, coefficient/sign-pattern permutation, EPRL zero-sum, support and scaling constraints.

Failure to recover any positive control makes the audit `INVALID_IMPLEMENTATION`.

## NEGATIVE CONTROLS

The audit must reject each of these as sufficient new joint authority:

1. the one-wedge `i epsilon` prescription alone;
2. one-wedge Ruhl/Toller uniqueness alone;
3. a synthetic or merely proposed auxiliary regulator not source-pinned in the frozen corpus;
4. generic extension-theory existence/nonuniqueness statements that do not select a coefficient;
5. the historical Iter331 required-jet detector/rank statements themselves, because they identify missing normalization data but are not source-defined physical normalization conditions.

If any negative control is promoted to a source-pinned joint selection rule, the gate is `INVALID_IMPLEMENTATION`.

## PASS

Return

`SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_FORCES_DELTA_ZERO_SCOPED`

iff the frozen corpus contains a genuinely joint source-authoritative rule satisfying all of:

1. its source/realization identity is pinned;
2. it applies to the same fixed `j=1`, nonzero-real-rho, channel-`00000`, full-collision object;
3. its action on collision-supported additions is explicit or derivable without new model data;
4. applying it to the confirmed `Delta` witness forces the witness coefficient to exactly zero;
5. all controls pass.

## FAIL

Return

`SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_PRESERVES_NONZERO_DELTA_SCOPED`

iff the frozen corpus contains a genuinely joint source-authoritative rule satisfying items 1–3 above, its action is outcome-determining, and it permits a nonzero multiple of the confirmed `Delta` witness while all controls pass.

This FAIL is a failure of the hypothesis that the added source authority removes this scoped witness. It is **not** a model/family FAIL.

## BLOCKED / INVALID

Return

`SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_NOT_PINNED_SCOPED`

if no genuinely joint rule in the frozen corpus is source-pinned strongly enough to act on `Delta`. This is a source/object-definition blocker, not scientific falsification.

Return

`SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_GATE_INVALID_IMPLEMENTATION`

if source-lock/provenance fails, the frozen corpus is changed during execution, positive/negative controls fail, one-wedge authority is conflated with joint authority, partial non-terminal workflow values are consumed, or a candidate rule is invented after freezing.

## INTERPRETATION CEILING

No outcome of this gate may by itself establish:

- existence or nonexistence of a base Eq. (4) joint extension;
- unconditional physical/global nonuniqueness of the published causal vertex;
- source authorization of `Delta`;
- impossibility of constructing a new source-compatible joint regulator/product/normalization theorem;
- any result for other spins, channels, families, lower collision strata or arbitrary boundary recouplings;
- closure of `D7-S2`, `D7-S3` or `D7-S4`;
- any terminal D7 selector;
- Candidate Gravity activation;
- `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

Historical FAIL/BLOCKED/INVALID classifications remain preserved.

## EXECUTION PLAN

Use a deterministic repository-native authority matrix. Each candidate authority class must be traced to the frozen records and assigned one of: `SOURCE_PINNED_ACTS_ON_DELTA`, `SOURCE_PINNED_BUT_ACTION_UNDETERMINED`, or `NOT_SOURCE_PINNED_IN_FROZEN_CORPUS`. The terminal classification must be a pure function of that matrix and the frozen controls. If a workflow is used, source-lock and audit jobs must be separate and all scientific classification waits for terminal completion.