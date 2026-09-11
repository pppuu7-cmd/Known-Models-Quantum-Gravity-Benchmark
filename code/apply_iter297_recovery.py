#!/usr/bin/env python3
from pathlib import Path
import json

run_id = "34593574762"
methodology_run = "34593574674"
scientific_head = "880b01f89488492c50deda7b315d02f425e0a3f4"
summary_artifact = "10260556884"
artifact_digest = "sha256:56e8aa47970c6bb29d11bd013466262b08495325d7b612aca5ba9d1374bb14c9"
raw_summary_digest = "sha256:d2886d62a8b590a6be83b4e9eb318f10f9454950a74abc3fa0afb505301af95a"
classification = "PASS_SCOPED_FORMAL_MEMBERWISE_CAUSAL_VERTEX_SUBSTITUTION_ON_ITER296_ADMISSIBLE_HAN_STACK_COMPLEXES_WITH_RETAINED_EXTERNAL_LAMBDA_MULTIPLICITY_BOOKKEEPING__NO_HALF_LINK_GLUE_EQUIVALENCE_FINITE_NORMALIZED_CAUSAL_STACK_SUM_CUTOFF_REMOVAL_OR_UV_IR_OBSERVABLE_CERTIFICATE"
blocker = "BLOCKED_MISSING_EXACT_HAN_HALF_LINK_GLUE_EQUIVALENCE_AND_FINITE_NORMALIZED_GENERALIZED_CAUSAL_VERTEX_STACK_AMPLITUDE_WITH_LAMBDA_F_WEIGHTED_AREA_CUTOFF_CONTROL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR"

# Audit
audit = Path("paper_iv/P_LQG_FORMAL_CAUSAL_STACK_COMPOSITION_AUDIT_ITER297_2026-09-11.md")
if not audit.exists():
    audit.write_text(f'''# Iter297 — formal causal-vertex composition on Han stack members

## Authorities and derivation status
- Muxin Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, Phys. Rev. D 113, 084034 (2026), DOI `10.1103/n76f-31gf`, arXiv:2510.26926.
- Carlos E. Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026).
- The Iter297 result is a source-grounded formal composition inference. It is not a claim that either source proves a finite causal Han-stack amplitude.

## Formal composition bridge
Han's stack sums generalized EPRL-KKL amplitudes over a face-multiplicity/spin-labelled family of 2-complexes and attaches external weights `prod_f lambda_f^p_f`. The multi-vertex amplitude is built by gluing local vertex amplitudes. Beltrán defines a causal alternative to the generalized EPRL-KKL vertex on arbitrary 2-complexes and explicitly proposes replacing the EPRL-KKL amplitude by the causal alternative at each vertex in multi-vertex discretizations.

Together with the Iter296 causal-orientation lift, this permits a formal causal amplitude to be assigned member-by-member on the admissible Han stack family by local vertex substitution while retaining the same member labels and external `lambda_f^p_f` multiplicity bookkeeping.

## Frozen machine audit
- Scientific run `{run_id}` on `{scientific_head}`: 4/4 independent guards + aggregate SUCCESS.
- Member-label preservation: 512 cases, up to 8 root faces and multiplicity 7.
- Exact-rational Han coupling identity: 1,792 cases covering 2..8 vertices, multiplicities 1..16, 16 seeds; `prod_v lambda_vf^p = (prod_v lambda_vf)^p` exactly in every case.
- Methodology run `{methodology_run}`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
- Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.

## Classification
`{classification}`

## Fail-closed boundary
Beltrán explicitly leaves finiteness of the generalized causal vertex open. The available sources also do not prove that the causal replacement is exactly identical to Han's special half-link/Haar gluing kernel representation, that Han's face-factorized analytic stack formula and large-cutoff localization survive the replacement, that the causal stack is normalized or cutoff-independent, or that a same-realization UV-to-causal-Regge/GR observable/error transport exists. Therefore this is a formal memberwise composition result only. LQG/spinfoam remains `PARTIAL/BLOCKED`, not terminal; D7 remains unauthorized.

Refined blocker:
`{blocker}`
''', encoding="utf-8")

# Decision delta
decision = Path("paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_297.json")
if not decision.exists():
    decision.write_text(json.dumps({
        "iteration": 297,
        "family": "LQG_SPINFOAM",
        "derivation_type": "SOURCE_GROUNDED_FORMAL_COMPOSITION_INFERENCE",
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
        "formal_memberwise_causal_vertex_substitution_exists": True,
        "same_member_multiplicity_and_spin_index_set_retained": True,
        "external_lambda_multiplicity_bookkeeping_retained_formally": True,
        "member_label_cases_checked": 512,
        "exact_rational_lambda_bookkeeping_cases": 1792,
        "exact_han_half_link_glue_equivalence_proven": False,
        "generalized_causal_vertex_finiteness_proven": False,
        "generalized_causal_vertex_normalization_proven": False,
        "causal_stack_cutoff_removal_proven": False,
        "causal_stack_large_cutoff_factorization_or_triangulation_independence_proven": False,
        "same_realization_uv_to_regge_gr_parameter_observable_error_transport_proven": False,
        "family_terminal": False,
        "d7_authorized": False,
        "terminal_count": "1/15",
        "candidate_terminal_count": "0/14",
        "refined_blocker": blocker
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

# Recovery delta
recovery = Path("recovery/RECOVERY_DELTA_297.md")
if not recovery.exists():
    recovery.write_text(f'''# Recovery Delta 297 — formal causal-vertex composition on Han stack members

- Scientific head `{scientific_head}`.
- Scientific run `{run_id}`: 4/4 independent guards + aggregate SUCCESS.
- Methodology `{methodology_run}`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
- Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.
- 512 member-label preservation checks passed.
- 1,792 exact-rational `lambda_f` multiplicity bookkeeping checks passed.
- Result: `{classification}`.
- New positive: a formal causal member amplitude can be defined on the Iter296-admissible Han stack member index set by per-vertex generalized EPRL-KKL causal substitution while retaining external multiplicity weights.
- Still missing: exact Han half-link gluing equivalence, finite/normalized generalized causal vertex, controlled causal stack cutoff removal/large-cutoff factorization, and same-realization UV→causal-Regge/GR observable/error transport.
- Refined blocker: `{blocker}`.
- Global D7 state unchanged: strict terminal `1/15`, candidate terminal `0/14`, D7 NOT_CLOSED / NOT_YET_AUTHORIZED, Candidate Gravity inactive at R3=24%.
- Paper III impact: NOT_NEEDED. Paper IV impact: READY.
''', encoding="utf-8")

# Publication ledger
ledger = Path("recovery/PUBLICATION_IMPACT_LEDGER.md")
text = ledger.read_text(encoding="utf-8")
if "## Iter297 — formal causal-vertex composition on Han stack members" not in text:
    marker = "\n## Standing rule\n"
    if marker not in text:
        raise SystemExit("fail-closed: publication standing-rule marker absent")
    block = f'''\n## Iter297 — formal causal-vertex composition on Han stack members
### Paper III — `NOT_NEEDED`
- **Type:** theory-specific formal composition/reproducibility result; no new general sensing/resource-closure rule beyond Iter277.
### Paper IV — `READY`
- Add the source-grounded formal composition result: on Iter296-admissible Han stack members, Beltrán's generalized causal EPRL-KKL alternative can be substituted per vertex on the same member 2-complex index set, while Han's external face-multiplicity weights retain the same `lambda_f^p_f` bookkeeping.
- Report 512 member-label preservation checks and 1,792 exact-rational coupling-bookkeeping identities.
- **Required boundary:** this does not prove exact identity with Han's half-link/Haar gluing representation, finiteness or normalization of the generalized causal vertex, preservation of Han's analytic face factorization after causal replacement, causal cutoff removal/triangulation independence, or UV→Regge/GR observable/error transport. Beltrán explicitly leaves generalized causal-vertex finiteness open.
- Result: `{classification}`.
- Provenance: scientific `{run_id}`; scientific head `{scientific_head}`; methodology `{methodology_run}`; summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.
'''
    ledger.write_text(text.replace(marker, block + marker), encoding="utf-8")

# Current front
front = Path("recovery/CURRENT_BENCHMARK_FRONT.md")
text = front.read_text(encoding="utf-8")
old_header = "Iteration: Iter296 Han face-stacking causal-orientation lift scoped; Iter295 conditional domain overlap, Iter294 CFS Einstein endpoint and earlier bridge refinements retained"
new_header = "Iteration: Iter297 formal causal-vertex composition on Han stack members scoped; Iter296 orientation lift and earlier bridge refinements retained"
if old_header in text:
    text = text.replace(old_header, new_header, 1)
elif new_header not in text:
    raise SystemExit("fail-closed: unexpected current-front iteration header")

if "### Iter297 — formal causal-vertex composition on Han stack members" not in text:
    marker = "\n## CFS front\n"
    if marker not in text:
        raise SystemExit("fail-closed: CFS marker absent")
    block = f'''\n### Iter297 — formal causal-vertex composition on Han stack members
Source-grounded formal composition inference from Han PRD 113, 084034 (2026) and Beltrán arXiv:2603.22661v2.
Scientific run `{run_id}`: 4/4 independent guards + aggregate SUCCESS on `{scientific_head}`.
Methodology `{methodology_run}`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.

Aggregate:
- formal memberwise causal vertex substitution on Iter296-admissible Han stack members = PASS_SCOPED;
- same member multiplicity/spin index set retained = true;
- external `lambda_f^p_f` bookkeeping retained formally = true;
- member-label checks = 512;
- exact-rational coupling-bookkeeping checks = 1,792;
- exact Han half-link glue equivalence = not proven;
- generalized causal-vertex finiteness/normalization = open;
- causal cutoff removal / large-cutoff factorization = not proven;
- same-realization UV→Regge/GR observable/error transport = not proven;
- family terminal = false; D7 authorized = false.

Classification:
`{classification}`

Interpretation: causal structure and a formal per-member causal amplitude are now composable across the Han face-multiplicity family at the abstract generalized-EPRL/KKL level. The decisive blocker moves to exact Han gluing compatibility, finite/normalized causal dynamics, cutoff control and physical transport.

Refined blocker:
`{blocker}`
'''
    text = text.replace(marker, block + marker)

old_blocker = "`BLOCKED_MISSING_FINITE_NORMALIZED_GENERALIZED_CAUSAL_VERTEX_INSERTION_AND_LAMBDA_F_WEIGHTED_COMPLETE_STACK_AMPLITUDE_SUM_WITH_AREA_CUTOFF_CONTROL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`"
if old_blocker in text:
    text = text.replace(old_blocker, f"`{blocker}`", 1)

text = text.replace("Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`; Iter278–296 = `NOT_NEEDED` as additional rules except where already stated.",
                    "Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`; Iter278–297 = `NOT_NEEDED` as additional rules except where already stated.")
text = text.replace("Paper IV: Iter277–296 = `READY` with stated claim boundaries.",
                    "Paper IV: Iter277–297 = `READY` with stated claim boundaries.")
text = text.replace("`D7_S2_LQG_CAUSAL_AMPLITUDE_STACK_SUM_AND_SAME_REALIZATION_UV_TO_REGGE_GR_TRANSPORT_CERTIFICATE`",
                    "`D7_S2_LQG_FINITE_NORMALIZED_CAUSAL_STACK_AMPLITUDE_AND_UV_TO_REGGE_GR_TRANSPORT_CERTIFICATE`")
text = text.replace("1. construct or locate a finite/normalized generalized causal EPRL-KKL vertex compatible with the Iter296 diagonal orientation lift, insert it into Han's `lambda_f`-weighted complete stack amplitude with area-cutoff control, then establish same-realization stack-coupling/`gamma`/spin-scale transport from the Iter287 UV/entropy sector through Iter291 to the Iter290 causal Regge/Einstein endpoint with normalized observable/comparator/error transport;",
                    "1. establish exact compatibility between Beltrán's causal vertex and Han's half-link/Haar gluing representation, then prove a finite/normalized `lambda_f`-weighted causal complete-stack amplitude with controlled area-cutoff removal/large-cutoff factorization and establish same-realization stack-coupling/`gamma`/spin-scale transport from the Iter287 UV/entropy sector through Iter291 to the Iter290 causal Regge/Einstein endpoint with normalized observable/comparator/error transport;")
front.write_text(text, encoding="utf-8")
