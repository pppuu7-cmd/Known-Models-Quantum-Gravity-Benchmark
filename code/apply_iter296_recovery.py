#!/usr/bin/env python3
from pathlib import Path
import json

run_id = "34593061657"
methodology_run = "34593061667"
scientific_head = "079f94c11c0c222b5c8759b316538cfd12664c33"
summary_artifact = "10196412595"
artifact_digest = "sha256:7d1d4387def6de4921532e78d31f098c49f72e37a178619eeb4e2dc2ba9fab0b"
raw_summary_digest = "sha256:c80bb2d1d5fc7fe58f8bbe059c6e1e3bba0cac1ab1819b5c54ab8286d829cd67"
classification = "PASS_SCOPED_ORIENTATION_LEVEL_CAUSAL_LIFT_ACROSS_HAN_FACE_MULTIPLICITY_STACKS_BY_ROW_DUPLICATION__NO_CAUSAL_AMPLITUDE_SUM_FINITE_LAMBDA_TRANSPORT_OR_UV_IR_OBSERVABLE_CERTIFICATE"
blocker = "BLOCKED_MISSING_FINITE_NORMALIZED_GENERALIZED_CAUSAL_VERTEX_INSERTION_AND_LAMBDA_F_WEIGHTED_COMPLETE_STACK_AMPLITUDE_SUM_WITH_AREA_CUTOFF_CONTROL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR"

# Paper-IV audit
audit = Path("paper_iv/P_LQG_FACE_STACKING_CAUSAL_LIFT_AUDIT_ITER296_2026-09-11.md")
if not audit.exists():
    audit.write_text(f'''# Iter296 — LQG face-stacking causal-orientation lift audit

## Authorities and derivation status
- Muxin Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, Phys. Rev. D 113, 084034 (2026), DOI `10.1103/n76f-31gf`, arXiv:2510.26926.
- Carlos E. Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026).
- The Iter296 lift theorem is a source-grounded algebraic inference from the published definitions; it is not claimed verbatim by either source.

## Source-grounded algebraic bridge
Han's face-stacking operation holds the vertex/edge skeleton fixed while increasing the multiplicity of faces bounded by the same root loop. At a vertex, Beltrán encodes causal consistency by a GF(2) incidence system whose rows are wedge/face constraints and whose columns are edge-orientation variables.

Therefore stacking a root face duplicates the associated incidence row. If every duplicate inherits the same causal wedge bit as the root face (the diagonal lift), the stacked right-hand side duplicates the corresponding bit as well. Repeating identical equations cannot change the row space, rank, or solution set for the edge-orientation variables. Thus every causally solvable root assignment has an orientation-level lift to every positive face-multiplicity vector in the Han family. Independent conflicting causal bits on duplicate faces are not guaranteed to lift.

## Frozen machine audit
- Scientific run: `{run_id}` on head `{scientific_head}`.
- Four independent guards in parallel with `fail-fast:false`, `max-parallel:4`.
- Exhaustive guard: 1,885 three-link-connected simple graphs with 4–6 vertices; all preserve GF(2) rank/diagonal solution lift after deterministic face-row duplication.
- Multiplicity stress: K5 rank 4; 512 positive multiplicity vectors up to multiplicity 16; 32 edge-orientation assignments per vector; all lifts preserve the equations.
- Negative control: two copies of one incidence row with opposite causal bits have zero solutions.
- Aggregate = SUCCESS.
- Methodology run `{methodology_run}`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
- Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.

## Classification
`{classification}`

## Fail-closed boundary
This closes only existence/consistency of a diagonal causal-orientation lift across Han's face-multiplicity family. It does not establish finiteness or normalization of Beltrán's generalized causal vertex, insertion of that causal vertex into Han's `lambda_f`-weighted stack sum, removal/control of Han area cutoffs for the causal amplitude, or same-realization UV-to-Regge/GR parameter/observable/error transport. Beltrán explicitly leaves finiteness of the generalized causal vertex open. LQG/spinfoam remains `PARTIAL/BLOCKED`, not terminal; D7 remains unauthorized.

Refined active blocker:
`{blocker}`
''', encoding="utf-8")

# Decision delta
decision = Path("paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_296.json")
if not decision.exists():
    decision.write_text(json.dumps({
        "iteration": 296,
        "family": "LQG_SPINFOAM",
        "derivation_type": "SOURCE_GROUNDED_ALGEBRAIC_INFERENCE",
        "authorities": [
            "Han, Phys. Rev. D 113, 084034 (2026), DOI 10.1103/n76f-31gf, arXiv:2510.26926",
            "Beltran, arXiv:2603.22661v2 (2026)"
        ],
        "scientific_run": int(run_id),
        "scientific_head": scientific_head,
        "methodology_run": int(methodology_run),
        "summary_artifact": int(summary_artifact),
        "artifact_digest": artifact_digest,
        "raw_summary_digest": raw_summary_digest,
        "classification": classification,
        "orientation_level_causal_lift_across_positive_face_multiplicities": True,
        "three_link_connected_simple_graphs_n4_to_n6_tested": 1885,
        "k5_multiplicity_vectors_tested": 512,
        "k5_max_multiplicity_tested": 16,
        "edge_orientation_assignments_per_vector": 32,
        "conflicting_duplicate_rhs_solution_count": 0,
        "causal_vertex_amplitude_stack_sum_defined_and_proven_finite": False,
        "lambda_f_weighted_causal_stack_sum_transport_proven": False,
        "area_cutoff_removal_for_causal_stack_amplitude_proven": False,
        "same_realization_uv_to_regge_gr_parameter_observable_error_transport_proven": False,
        "family_terminal": False,
        "d7_authorized": False,
        "terminal_count": "1/15",
        "candidate_terminal_count": "0/14",
        "refined_blocker": blocker
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

# Recovery delta
recovery = Path("recovery/RECOVERY_DELTA_296.md")
if not recovery.exists():
    recovery.write_text(f'''# Recovery Delta 296 — LQG face-stacking causal-orientation lift

- Scientific head `{scientific_head}`.
- Scientific run `{run_id}`: 4/4 independent guards + aggregate SUCCESS.
- Methodology `{methodology_run}`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
- Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.
- Exhaustive exact validation: 1,885 three-link-connected simple graphs, n=4..6.
- K5 multiplicity stress: 512 vectors, multiplicity <=16, 32 edge-orientation assignments each.
- Negative control: conflicting duplicated-face causal bits -> zero GF(2) solutions.
- Result: `{classification}`.
- New positive: diagonal causal orientation has an algebraically exact lift through arbitrary positive face multiplicities at the orientation-consistency level.
- Still missing: finite/normalized generalized causal vertex and its insertion into the `lambda_f`-weighted complete stack amplitude with cutoff control, then same-realization UV→causal-Regge/GR observable/error transport.
- Refined blocker: `{blocker}`.
- Global D7 state unchanged: strict terminal `1/15`, candidate terminal `0/14`, D7 NOT_CLOSED / NOT_YET_AUTHORIZED, Candidate Gravity inactive at R3=24%.
- Paper III impact: NOT_NEEDED. Paper IV impact: READY.
''', encoding="utf-8")

# Publication ledger
ledger = Path("recovery/PUBLICATION_IMPACT_LEDGER.md")
text = ledger.read_text(encoding="utf-8")
if "## Iter296 — LQG face-stacking causal-orientation lift" not in text:
    marker = "\n## Standing rule\n"
    if marker not in text:
        raise SystemExit("fail-closed: publication standing-rule marker absent")
    block = f'''\n## Iter296 — LQG face-stacking causal-orientation lift
### Paper III — `NOT_NEEDED`
- **Type:** theory-specific algebraic/domain result; no new general sensing/resource-closure rule beyond Iter277.
### Paper IV — `READY`
- Add the source-grounded algebraic result that Han face stacking duplicates Beltrán GF(2) wedge constraints while preserving the vertex/edge skeleton. Under the diagonal assignment in which duplicate faces inherit the root causal bit, every causally solvable root assignment lifts to arbitrary positive face multiplicities without changing the edge-orientation solution set.
- Report exact validation on 1,885 three-link-connected simple graphs with 4–6 vertices and K5 stress over 512 multiplicity vectors up to 16 with all 32 edge-orientation assignments; include the conflicting-duplicate negative control with zero solutions.
- **Required boundary:** this is an orientation-level lift, not a causal-amplitude closure theorem. Beltrán leaves generalized causal-vertex finiteness open; no source proves its normalized insertion into Han's `lambda_f`-weighted stack sum, causal cutoff removal, or UV→Regge/GR observable/error transport.
- Result: `{classification}`.
- Provenance: scientific `{run_id}`; scientific head `{scientific_head}`; methodology `{methodology_run}`; summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.
'''
    ledger.write_text(text.replace(marker, block + marker), encoding="utf-8")

# Current front
front = Path("recovery/CURRENT_BENCHMARK_FRONT.md")
text = front.read_text(encoding="utf-8")
old_header = "Iteration: Iter295 Han-stack / generalized causal EPRL-KKL conditional domain overlap scoped; Iter294 CFS Einstein endpoint and earlier bridge refinements retained"
new_header = "Iteration: Iter296 Han face-stacking causal-orientation lift scoped; Iter295 conditional domain overlap, Iter294 CFS Einstein endpoint and earlier bridge refinements retained"
if old_header in text:
    text = text.replace(old_header, new_header, 1)
elif new_header not in text:
    raise SystemExit("fail-closed: unexpected current-front iteration header")

if "### Iter296 — face-stacking causal-orientation lift" not in text:
    marker = "\n## CFS front\n"
    if marker not in text:
        raise SystemExit("fail-closed: CFS marker absent")
    block = f'''\n### Iter296 — face-stacking causal-orientation lift
Source-grounded algebraic inference from Han PRD 113, 084034 (2026) and Beltrán arXiv:2603.22661v2.
Scientific run `{run_id}`: 4/4 independent guards + aggregate SUCCESS on `{scientific_head}`.
Methodology `{methodology_run}`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.

Aggregate:
- diagonal causal-orientation lift across positive Han face multiplicities = PASS_SCOPED;
- exhaustive exact validation = 1,885 three-link-connected simple graphs, n=4..6;
- K5 stress = 512 multiplicity vectors up to 16 × 32 edge-orientation assignments;
- conflicting duplicated-face RHS negative control = 0 solutions;
- causal generalized-vertex finiteness/normalization = open;
- `lambda_f`-weighted causal complete-stack amplitude transport = false;
- causal area-cutoff removal/control = false;
- same-realization UV→Regge/GR observable/error transport = false;
- family terminal = false; D7 authorized = false.

Classification:
`{classification}`

Interpretation: the orientation-consistency part of the Han-stack/Beltrán bridge now has an explicit lift through arbitrary positive face multiplicities. The decisive blocker moves from causal-structure existence to the actual causal amplitude and physical transport.

Refined blocker:
`{blocker}`
'''
    text = text.replace(marker, block + marker)

old_blocker = "`BLOCKED_MISSING_CAUSAL_VERTEX_LIFT_THROUGH_HAN_COMPLETE_STACK_SUM_FACE_MULTIPLICITIES_AND_LAMBDA_F_WEIGHTS_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`"
if old_blocker in text:
    text = text.replace(old_blocker, f"`{blocker}`", 1)

text = text.replace("Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`; Iter278–295 = `NOT_NEEDED` as additional rules except where already stated.",
                    "Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`; Iter278–296 = `NOT_NEEDED` as additional rules except where already stated.")
text = text.replace("Paper IV: Iter277–295 = `READY` with stated claim boundaries.",
                    "Paper IV: Iter277–296 = `READY` with stated claim boundaries.")
text = text.replace("`D7_S2_LQG_CAUSAL_LIFT_THROUGH_COMPLETE_STACK_AND_SAME_REALIZATION_UV_TO_REGGE_GR_TRANSPORT_CERTIFICATE`",
                    "`D7_S2_LQG_CAUSAL_AMPLITUDE_STACK_SUM_AND_SAME_REALIZATION_UV_TO_REGGE_GR_TRANSPORT_CERTIFICATE`")
text = text.replace("1. seek/compute an explicit lift of the generalized causal EPRL-KKL prescription through Han's complete face-multiplicity/`lambda_f` stack sum, then a same-realization stack-coupling/`gamma`/spin-scale transport from the Iter287 UV/entropy sector through Iter291 to the Iter290 causal Regge/Einstein endpoint with normalized observable/comparator/error transport;",
                    "1. construct or locate a finite/normalized generalized causal EPRL-KKL vertex compatible with the Iter296 diagonal orientation lift, insert it into Han's `lambda_f`-weighted complete stack amplitude with area-cutoff control, then establish same-realization stack-coupling/`gamma`/spin-scale transport from the Iter287 UV/entropy sector through Iter291 to the Iter290 causal Regge/Einstein endpoint with normalized observable/comparator/error transport;")
front.write_text(text, encoding="utf-8")
