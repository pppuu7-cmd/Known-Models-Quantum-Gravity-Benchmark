# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal scientific execution

`ITER504R_ROOT_AFFINE_REUSE_CONTINUOUS_DRIFT_DIAGNOSTIC_GATE`

Classification:

`ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED`

Authority:

- preregistration `147d68f26ed3a14ce3cd1fd77fcd96d5fb329ec8`;
- implementation `f846820bae39963a48272deccb2e4a539100fce1`;
- authoritative run `35154724661`, terminal `completed/success`;
- terminal result `598ede26e0db448411537e9d5f813aa344f88d0f`;
- independent Critic `6e300294e6c9a470099776d1c30357eed3fa4b93`.

Exact terminal facts:

- total leaves `2916`;
- certified `24`;
- unresolved depth-10 `2892`;
- maximum `drift_upper = 0.6136407189670734`;
- minimum terminal `S_lower = 3.7043291995581735`;
- maximum possible-max count `46`.

Scientific localization: child-delta refinement alone, while retaining the same full-root derivative enclosure `D(I)`, is not sufficient on the frozen three-root continuous-drift diagnostic. Residual mechanism space is full-root derivative-enclosure width and/or nonsmooth max-channel competition/crossings, with possible fixed-channel nonstationarity. Do not increase depth blindly or promote this diagnostic to the full Iter504 domain.

## Active scientific gate — Iter504S exact-threshold repair required

Gate:

`ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR`

Scientific preregistration remains exactly:

`f6367456aa715fe6282ab70c1b2005971a4568c7`

Frozen science remains unchanged:

- `python-flint==0.9.0`;
- Arb/Acb precision `384` bits;
- all `243` channels retained, no pruning;
- causal `0to5`, block `0`, path `2`, direction `[1,1,1,-1,-1,-1]`, sign `+1`;
- roots `13,14,15`;
- rhos `[0.35,0.9,1.6,2.7]`;
- R grid `[6,8,10,12]`;
- robust floor exact `+1`;
- drift threshold exact `0.05 = 1/20`;
- exact preregistered LOW/MID/HIGH rational points only;
- center-D is control-only and is not a validated replacement enclosure.

Allowed terminal scientific classes remain only:

- `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`;
- `ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED`;
- `ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED`;
- `ITER504S_MIXED_MECHANISM_SCOPED`;
- `ITER504S_INVALID`.

## Initial Iter504S execution — terminal implementation-invalid

Initial run `35173442220`, workflow head `cb50a107b24232ef1b652baa9443e69fc3fa6ca1`, run number `1`, attempt `1`, is terminal `completed/failure`.

Source-lock succeeded. All six root jobs failed in the evaluator step with the same representation error family across Python 3.11 and 3.13:

`TypeError("cannot create acb from type <class 'iter503_ad_core.CD'>")`

Assembly never produced a valid scientific payload. Therefore this first execution is implementation-invalid and non-authoritative for scientific classification; it is not a scientific FAIL.

Durable record:

`f916873228f970844c775dbaaabeba999b432365`

## First repaired Iter504S execution — terminal diagnostic only

Execution-only repairs frozen before this run:

1. derivative-component extraction `88c92f86a765e9d8b441152674fc2c303f3f1ff3`;
2. fixed-channel drift-only competition semantics `4ef41c0f4ceed3082fd4d80930ef5d848f18802b`.

Repaired chain:

- evaluator `b20077e77b421a68f1a99135ff652e52a0d53227`;
- assembler `7dc689f9b4d7e4f768a677e2afc80668a15b73d9`;
- aggregate `b0347e225b986b63e079ef6ebf02cd928022eb39`;
- adversarial Critic `38c705865b0397c7cf664ad142ad232d3b0a312f`;
- execution authority `7931e10c31dc8f1db42215117ef2b1b15ac0ed6b`;
- workflow head `7e3b266def723dc332239990bac01f9298c17b4e`;
- Actions run `35175533159`.

Run `35175533159` is terminal `completed/success`: all six root jobs, both Python 3.11/3.13 independent assemblies, cross-environment aggregate and adversarial Critic completed successfully. The two environments produced identical root hashes and identical assembled SHA256. Critic reported no errors, cross-environment discrete agreement `true`, and all frozen negative/semantic controls passed.

Its **provisional diagnostic** classification is:

`ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`

This is strong mechanism evidence but is **not promoted to terminal science** because an outcome-blind post-launch static audit found a validated-decision transport defect before the terminal result was consumed for scientific promotion.

## Exact-threshold decision firewall

Authoritative firewall commit:

`77d42eb58c03eef2356aed7a25795562760de4e3`

File:

`research/prereg/ITER504S_EXECUTION_ONLY_EXACT_THRESHOLD_DECISION_FIREWALL_2026-09-17.md`

Defect: the repaired evaluator computes Arb enclosures, but several terminal mechanism predicates are reconstructed from binary64 summaries produced by `bound_float`, including derivative-radius drift comparisons, full/center violation tests, and fixed-channel competition threshold tests. The core module explicitly treats ordinary Arb-to-float conversion as display-only rather than a validated decision channel.

Python binary64 `0.05` is not exact `1/20`:

`0.05.as_integer_ratio() = 3602879701896397 / 72057594037927936`,

which exceeds exact `1/20` by `1 / 360287970189639680`.

Therefore no non-INVALID mechanism class from run `35175533159` is eligible for final scientific promotion. This authority rule was frozen outcome-blind and applies equally to every possible mechanism class.

The next scientific execution may change only decision transport/verification:

- evaluate full-envelope slope-floor and drift booleans directly in Arb;
- evaluate derivative-radius sensitivity from producer exact-Arb drift booleans;
- evaluate every fixed-channel drift boolean directly in Arb;
- transport explicit exact-decision booleans / violating-channel identities downstream;
- make binary64 bounds display-only;
- make assembler, aggregate and independent Critic classify solely from exact producer booleans plus structural/provenance identities;
- preserve every scientific threshold, point, channel, precision, source, cohort and classifier branch.

Exactly one repaired scientific execution is authorized only after its implementation hashes and workflow authority are prospectively frozen.

## Outcome-blind successor machinery

Generic successor mathematics was frozen before repaired Iter504S terminal outcome in:

`research/methodology/ITER504S_OUTCOME_BLIND_SUCCESSOR_TOOLKIT_2026-09-17.md`

commit:

`81e0e94649a50cccc510dc2630456af45fd98e46`.

It contains four generic routes without selecting any future witness/partition based on outcome:

- validated local derivative enclosure `D(J)` directly over child/subroot interval `J`, never midpoint derivative as truth;
- validated max-channel switching via `Q_ij=|f_i|^2-|f_j|^2` and dominance cells, never fitted crossings or artificial smoothing;
- direct source-faithful fixed-channel local-function Arb certificate;
- mixed case-level mechanism matrix and deterministic factorial discriminator.

Any successful three-root mechanism repair must pass a prospectively selected held-out representative cohort before full 1888-state expansion is considered.

## Next decision after exact-threshold Iter504S terminal result

- `ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED` -> prospectively freeze bounded `ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION` using validated `D(J)`;
- `CHANNEL_COMPETITION_NECESSARY_SCOPED` -> prospectively freeze switching-surface / dominance-cell certificate;
- `FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED` -> prospectively freeze direct fixed-channel local-function certificate;
- `MIXED_MECHANISM_SCOPED` -> prospectively freeze bounded case-level factorial discriminator;
- `INVALID` -> no science; localize exact minimal defect and do not change classifier.

Do not launch a full 1888-state campaign before bounded rigorous repair, independent Critic and representative held-out generalization.

## Iter504P retained baseline

`ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED` remains terminal. Maximum decisive sampled point drift is `0.009396862546624` with threshold margin `0.040603137453376`. Point-grid PASS is not a continuous theorem.

## D7 state retained

- `D7-S2 = NOT_CLOSED`;
- `D7-S3 = NOT_CLOSED`;
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- raw group-variable tangent pushforward is closed scoped;
- group-only simultaneous contact-covector object remains `BLOCKED_SCOPED` because no admissible primary authority defines the required `CP1 x SL(2,C) -> group tangent covector` map.

Do not repeat the K5 source hunt absent genuinely new admissible primary authority.

## Governance lock

- KMQGB benchmark/methodology infrastructure = `100% ready`; this is not a physics-completion claim.
- `RQIR Core v1.0 = FROZEN`.
- selector labels remain unauthorized.
- Candidate Gravity remains inactive.
- Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`.
- `BLOCKED != FAIL`.
- green CI != scientific PASS.
- point-grid PASS != continuous theorem.
- diagnostic localization != full-domain theorem.
- positive slope != absolute-Haar divergence theorem.
- no model/family/global/new-theory/new-physics conclusion follows.
