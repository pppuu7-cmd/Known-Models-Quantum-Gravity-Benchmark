# KMQGB Methods / Evidence Matrix

**Status:** publication-facing synthesis package  
**Introduced:** KMQGB Iter178  
**Machine companion:** `publication/claim_evidence_matrix.json`.

## 1. What KMQGB is allowed to claim

KMQGB is a benchmark and reconstruction infrastructure operating under **RQIR Core v1.0 FROZEN**. Its job is to translate framework-native objects into a common observable/comparator language, enforce same-realization and attribution rules, and preserve BLOCKED states instead of converting missing objects into scientific exclusions.

The repository may become **100% complete as infrastructure and methodology** while Paper IV and Candidate Gravity remain scientifically open. This distinction is part of the method, not a disclaimer added after the fact.

## 2. Reconstructing a KMQGB result

A publication-facing result should be reconstructed in this order:

1. **Freeze governance.** Read `protocol/RQIR_CORE_V1_BENCHMARK_FIREWALL.md`, `protocol/PAPER_IV_SAME_REALIZATION_COMPOSITION_GATE.md`, `protocol/READINESS_METRICS.md`, and `recovery/state.json`.
2. **Identify the physical object.** Use the relevant Paper-IV audit and the active Closure Wave record.
3. **Freeze the realization vector.** Check parent/state/boundary/gauge/regulator/truncation/signature/normalization/scale/source routing. Adjacent authorities are not composable until an explicit map exists.
4. **Freeze the comparator domain.** Candidate/framework and comparator must share observable definition, response order, state, background, routing and contact/amputation conventions.
5. **Run the relevant executable controls.** Critical scripts are registered in `protocol/EXECUTABLE_TEST_REGISTRY.json` and executed by `code/methodology_orchestrator.py`.
6. **Check the claim matrix.** The machine status in `publication/claim_evidence_matrix.json` determines whether wording is established, derived, reproduced, blocked, hypothetical or forbidden.
7. **Package the authority set.** `code/build_release_bundle.py` produces a deterministic archive containing the minimum restoration/reproduction authority and a SHA-256 manifest.

## 3. Evidence classes

### `ESTABLISHED_EXTERNAL`

An external paper/repository/programme authority establishes the stated fact. KMQGB may quote or paraphrase it within its actual scope but must not enlarge the scope.

### `DERIVED_KMQGB`

The relation is analytically derived inside KMQGB from declared inputs and frozen assumptions. A matching executable regression is preferred and is mandatory where the completion contract names one.

### `REPRODUCED_EXECUTABLE`

The repository contains a stable executable control and CI reproduces it.

### `OPEN_BLOCKED`

A required object is absent, not yet mapped into the same realization, or incomplete at the required normalization/domain. This is a valid scientific state and **not** a negative experimental result.

### `HYPOTHESIS_ONLY`

A search direction or parent principle is being explored but lacks the proof obligations required for promotion.

### `FORBIDDEN_OVERCLAIM`

The wording is incompatible with the frozen evidence. Examples include converting `BLOCKED` into “excluded” or converting R1/R2 infrastructure completion into “quantum gravity solved.”

## 4. Current high-value Paper-IV synthesis

### O-AS

The scalar-scattering programme has advanced to programme-level public evidence for a Lorentzian gravitational contact contribution. The stable reproducible same-realization `A4` plus common normalization/error/comparator certificate is still missing. Therefore the correct article language is **promising completion route / open reproducibility object**, not exclusion or closure.

### O-LQG

The active gamma-duality route has four logically distinct layers:

1. microscopic EPRL gamma-duality authority;
2. area-metric running-gamma and Lorentzian parity/birefringence adjacent authority;
3. KMQGB identifiability/RG algebra;
4. the missing same-realization EPRL -> area-metric -> EFT map.

KMQGB has derived and executable-tested:

`q = 1/gamma - gamma - Delta_gamma`,

q-only rank deficiency in `{gamma,Delta_gamma}`,

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma`,

`gamma = -cot(4 psi)` on the positive branch used by the area-metric adapter,

`Delta_gamma = 2 cot(8 psi) - q` after common-scale transport,

and

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`.

These relations establish what a valid composed bridge **must satisfy**. They do not establish that the adjacent EPRL and area-metric authorities already belong to one physical realization. The missing same-realization map and same-parent `beta_Delta` are therefore explicit future proof obligations.

### O-CFS

CFS has continuum/gravity authority and a systematic correction generator, but the first explicit normalized beyond-continuum gravity correction tensor/coefficient object with same-domain comparator remains open.

## 5. Methods package for a future Candidate Gravity proposal

A prospective proposal follows:

`protocol/BEYOND_C5_PARENT_PRINCIPLE_DECISION_PROCEDURE.md`

and is stored using:

`schemas/candidate_gravity_record_v1_3.schema.json`

plus

`templates/candidate_gravity_record_v1_3.template.json`.

The v1.3 validator requires explicit functional-freedom state, same-realization state, compute authorization and publication trace in addition to the historical G0-G10 promotion structure. A fully BLOCKED template is a **successful infrastructure state** because the repository can represent ignorance without fabrication.

## 6. Reproducibility package

The minimal publication/recovery bundle is frozen in `release/BUNDLE_CONTENTS.json`.

`code/build_release_bundle.py`:

- checks that every required path exists;
- SHA-256 hashes every source;
- writes the hashes and byte sizes into `MANIFEST.json`;
- normalizes ZIP timestamps, ordering and permissions;
- can rebuild twice and require byte identity.

CI uploads the resulting ZIP only after methodology, scaffold and repository-completion checks pass.

## 7. Limitations that must remain in any article

The following limitations are substantive and must not be omitted:

- Paper IV is not terminal while Closure Wave 02 remains open;
- framework `BLOCKED` states are missing-object/composition states, not observational falsifications;
- the O-LQG same-realization EPRL-to-area-metric renormalization map is not presently established by KMQGB;
- the O-AS stable contact-complete reproducibility package remains publication-triggered;
- the explicit normalized CFS correction tensor remains unavailable;
- Candidate Gravity scientific readiness is externally governed and is not increased by repository engineering;
- no heavy compute is scientifically useful while the decisive blocker is analytic/provenance/matching rather than numerical.

## 8. Publication-ready conclusion allowed at repository completion

Once the Iter178 completion CI passes, the strongest justified infrastructure statement is:

> KMQGB is complete as a reproducible benchmark/methodology repository for its declared frozen-core task: governance, recovery, candidate scaffolding, executable methodology, release packaging and claim/evidence discipline are all machine-checked. The remaining incompleteness is physical rather than infrastructural and is explicitly localized in the open Paper-IV closure objects and external Candidate Gravity programme.

The following stronger sentence is **not** authorized:

> KMQGB has completed quantum gravity.

That distinction is permanent and machine-enforced by the completion validator and claim/evidence matrix.
