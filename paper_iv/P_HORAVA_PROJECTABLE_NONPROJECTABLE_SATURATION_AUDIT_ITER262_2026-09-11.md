# Hořava gravity projectable/non-projectable saturation audit — Iter262

Date: 2026-09-11
Family: `HORAVA_LIFSHITZ`
RQIR Core: `v1.0 FROZEN`

## Question
Can the remaining Hořava-Lifshitz family blocker be reduced to explicit finite/external objects using the current 2025–2026 authority for both projectable and non-projectable branches?

## Prior state
Iter186 froze the family as `PARTIAL_SUBFAMILY_ONLY__PROJECTABLE_RENORMALIZATION_RG_CONTROL` with blocker:
`HORAVA_PROJECTABLE_UV_TO_IR_EXTRA_MODE_OBSERVABLE_CERTIFICATE_PLUS_NONPROJECTABLE_DISPOSITION`.

## Authorities checked
1. Barvinsky et al., *Renormalization of Hořava Gravity*, Phys. Rev. D 93, 064022 (2016): proof of perturbative renormalizability for projectable Hořava gravity.
2. Barvinsky, Kurov & Sibiryakov, *Renormalization group flow of projectable Hořava gravity in (3+1) dimensions*, Phys. Rev. D 111, 024030 (2025), arXiv:2411.13574: asymptotically-free fixed points and a distinguished trajectory family spanning the unitarity-compatible lambda range into the near-GR region.
3. Mukohyama, Radkovski & Sibiryakov, *Space vs time dependence in taming the infrared instability of projectable Hořava gravity*, Phys. Rev. D 114, 024039 (2026): confirms Minkowski IR instability in projectable 3+1 Hořava gravity and finds no acceptable static homogeneous/isotropic or planar low-average-curvature endpoint in the analyzed class; viability is pushed toward a time-dependent hiding scenario.
4. Blas, Del Porro, Herrero-Valea, Radkovski & Sibiryakov, *Quantizing nonprojectable Hořava gravity with Lagrangian path integral*, Phys. Rev. D 113, 106022 (2026): constructs the non-projectable quantum theory as a Lagrangian path integral with field-dependent measure; in a 2+1-dimensional one-loop case study verifies cancellation of dangerous frequency divergences and obtains a local divergent effective action and beta functions, while explicitly formulating the remaining questions required for a proof of perturbative renormalizability.

## Projectable branch

### UV/RG — scoped PASS
The projectable branch has a genuine perturbative-renormalizability theorem and a 3+1 RG trajectory from asymptotically-free UV fixed points into the unitarity-compatible near-GR lambda region.

Status:
`PASS_SCOPED_PROJECTABLE_UV_RENORMALIZATION_AND_NEAR_GR_RG_TRAJECTORY`.

### IR/extra scalar mode — explicit open viability blocker
The 2026 analysis states that Minkowski spacetime is infrared-unstable in projectable 3+1 Hořava gravity. It investigates whether higher-derivative spatial structure can provide a static low-curvature endpoint and reports that the studied static homogeneous/isotropic and planar (quasi)periodic classes cannot serve as such an endpoint. The remaining viability route considered is dynamical/time-dependent concealment by processes such as Hubble expansion/Jeans instability, which imposes an IR constraint on the RG flow.

Therefore the missing UV->IR certificate is no longer a generic literature gap. It contains an authority-explicit unresolved physical condition:
`BLOCKED_EXTERNAL_PHYSICAL_VIABILITY_OBJECT__PROJECTABLE_TIME_DEPENDENT_TAMING_OF_SCALAR_IR_INSTABILITY_ALONG_SAME_UV_RG_TRAJECTORY`.

A low-energy phenomenological observable from another Hořava parameterization cannot be spliced onto the UV trajectory without same-realization parameter transport.

## Non-projectable branch

### Quantum measure and one-loop locality — scoped PASS
The 2026 PRD work materially advances the branch: it provides a Lagrangian path integral, local auxiliary-field representation of the measure, and an explicit one-loop computation in 2+1 dimensions in which dangerous linear-frequency divergences cancel and the divergent quadratic effective action remains local.

Status:
`PASS_SCOPED_NONPROJECTABLE_LAGRANGIAN_QUANTIZATION_AND_2PLUS1_ONE_LOOP_LOCALITY_CONTROL`.

### Full renormalizability / 3+1 gravity observable — explicit open blocker
The same authority does not claim a full proof of perturbative renormalizability for non-projectable Hořava gravity; its abstract explicitly says that the questions needed for such a proof are formulated. The result is also a 2+1 case study rather than a 3+1 same-realization UV->IR observable/comparator package.

Remaining status:
`BLOCKED_EXTERNAL_OPEN_THEORY_OBJECT__NONPROJECTABLE_FULL_PERTURBATIVE_RENORMALIZABILITY_AND_3PLUS1_SAME_REALIZATION_OBSERVABLE_COMPARATOR_CERTIFICATE`.

This is `BLOCKED`, not scientific FAIL.

## Family disposition
The projectable and non-projectable branches remain materially distinct and cannot be merged. Current authority gives important scoped positive controls to both, but neither branch supplies the full KMQGB same-realization package required for family terminality.

`HORAVA_LIFSHITZ = PARTIAL_SUBFAMILY_ONLY`.

No family-level scientific FAIL and no `NEW_REQUIRED` inference are authorized.

## Operational saturation
The formerly broad two-part blocker is now reduced to two explicit authority-bounded endpoints:
1. projectable: same-trajectory time-dependent IR stabilization/phenomenology and comparator-ready observable;
2. non-projectable: full renormalizability/3+1 same-realization observable-comparator proof.

Generic literature expansion has low information gain until one of these objects appears. Operational status:
`PARKED_PENDING_PROJECTABLE_DYNAMIC_IR_VIABILITY_OR_NONPROJECTABLE_FULL_RENORMALIZATION_OBJECTS`.

## Governance
- D2: `NOT_CLOSED`.
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- Candidate Gravity R3: 24%.
- Heavy compute: `IDLE`.

## Polygon saturation
Operational known-school polygon saturation increases from ~96% to ~97%. This records that the Hořava family is now bounded by explicit external/open objects rather than an undifferentiated projectable/non-projectable search. It is not strict D7 completion or family exclusion.

## Next gate
Move to `ASYMPTOTIC_SAFETY` same-realization amplitude/comparator closure or another finite Tier-1 blocker. Do not repeat generic Hořava searches unless new authority closes one of the two explicit endpoints above.
