# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **200**  
**Phase:** **RQIR Core v1.0 FROZEN / LQG UV→IR path literature-limited / 4D CDT normalized gravity observable frozen / CDT continuum trajectory blocked**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- No scientific-readiness promotion in Iter200.

## Validation baseline

Canonical Iter199 main head `86cfc553f03c50ea229a382f621ce45353b13d1a` passed exact-head methodology-ci run `34466116419` and reproducibility-release run `34466173158`, both `success`.

Iter200 is prepared on `research/cdt-geon-observable-iter200` and is noncanonical until exact-head CI and integration complete.

## Paper-IV global gates

D1 PASS; D2A NOT_CLOSED; D2B NOT_CLOSED; D2 `NOT_CLOSED_COVERAGE_AND_OBJECTS`; D3 PARTIAL; D4 `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`; D5 PASS; D6 `PASS_RULE_TARGETS_OPEN`; D7 NOT_CLOSED; global decision **`NOT_YET_AUTHORIZED`**.

## Coverage status

- Tier-1 required rows: **14**.
- terminal family rows: **1/14**.
- nonterminal family rows: **13/14**.
- Tier-2 unresolved: **0**.
- defined scoped child residual/control rows: **10** after Iter200.
- No scoped child is promoted to family sufficiency/exclusion.

## Iter199 retained result — LQG topology escape

The EPRL/KKL UV path remains blocked after the topological-continuum escape constraint. No targeted same-realization authority was found that carries the Han small-spin UV stack through relevant deformation into the large-spin Regge/Area-Regge regime with Barbero–Immirzi ancestry. Effective-spin-foam and area-metric RG results remain surrogate/separate authorities and cannot be spliced into the Han realization.

LQG next gate remains:

`EPRL_KKL_UV_FIXED_POINT_TO_SEMICLASSICAL_AREA_REGGE_CROSSOVER_WITH_TOPOLOGY_ESCAPE_GAMMA_ANCESTRY_AND_ERROR_CERTIFICATE`.

## Iter200 — 4D CDT gravity observable

Maas, Plätzer and Pressler, *Hints for a Geon from Causal Dynamic Triangulations*, Phys. Lett. B 879 (2026) 140600 / arXiv:2504.11047v4, provide a fixed-realization four-dimensional CDT curvature-correlation measurement at `Delta=0.6`, `kappa_0=2.2`.

The normalized observable is

`D_OO(tau,s)=C_OO(tau,s)/C_11(tau,s)`

for curvature operators `Delta Q`, `Delta Q^2` and a reconstructed curvature scalar `R`. The intermediate-distance correlators exhibit a common exponential screening scale within the reported precision.

The final paper includes:

- operator-choice robustness;
- volumes 80k, 160k and 320k simplices;
- smearing-radius systematics, with stability above the lattice-artifact region;
- one-sigma fit bands;
- publicly archived stochastic samples on Zenodo record 20589545.

Scoped result:

`PASS_RQIR_GATE__CDT_4D_NORMALIZED_CURVATURE_CORRELATOR_PHYSICAL_OBSERVABLE_WITH_OPERATOR_VOLUME_SMEARING_SYSTEMATICS_AND_OPEN_DATA`.

This closes only the statement that no concrete 4D gravity-sector observable exists. The geon interpretation itself is not frozen as a discovery claim.

Authorities:

- `paper_iv/O_CDT_4D_GEON_GRAVITY_OBSERVABLE_SCOPE_AUDIT_2026-09-10.md`
- `post_freeze_paper_iv_wave_02/PF2_02B_CDT_4D_GEON_OBSERVABLE/result.json`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_200.json`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_200.json`

## Why CDT remains partial

The observable is measured at one bare point. The physical-unit mass conversion uses an external lattice-spacing estimate and is explicitly subject to discretization artifacts. No line of constant physics transports this observable toward `a -> 0`.

The CDT↔FRG critical-scaling programme identifies a concrete strategy for an IR/UV mapping, but its published conclusion is that present numerical precision is insufficient to decide whether the required CDT UV fixed point exists. Therefore finite-volume robustness of the geon correlator is not a substitute for a continuum extrapolation.

EDT is also not dispositioned by this CDT child result.

## Refined CDT gate

**`CDT_4D_LINE_OF_CONSTANT_PHYSICS_TO_UV_CONTINUUM_TRAJECTORY_PLUS_LATTICE_SPACING_SCALING_AND_GEON_CORRELATOR_COMPARATOR_ERROR_CERTIFICATE__EDT_DISPOSITION`**.

Required payload:

1. fixed multi-bare-coupling 4D CDT trajectory to a controlled critical surface/fixed point;
2. line-of-constant-physics or equivalent physical scale-setting prescription;
3. explicit `a -> 0` map and uncertainty;
4. normalized gravity observable transported/re-measured along that trajectory;
5. combined critical-scaling, finite-volume, discretization, smearing and fit error ledger;
6. same-domain GR/EFT/alternative-QG comparator predictions;
7. explicit EDT disposition.

## Heavy compute

**IDLE.** Re-fitting the public one-bare-point geon samples cannot close the continuum blocker. Heavy computation becomes justified if a prospectively frozen multi-coupling critical-scaling / line-of-constant-physics dataset is identified.

## Next order

1. exact-head CI-validate and integrate Iter200;
2. search for a published multi-coupling CDT critical-scaling dataset / line-of-constant-physics capsule that can transport the correlator toward `a -> 0`;
3. if absent, mark CDT literature/data-limited at this gate and rotate to causal sets or another family while the hourly auto-research is rechecked before each merge.
