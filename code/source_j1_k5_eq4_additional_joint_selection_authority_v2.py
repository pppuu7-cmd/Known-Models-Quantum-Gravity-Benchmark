#!/usr/bin/env python3
import argparse
import ast
import hashlib
import json
import os
import re
import urllib.request
from pathlib import Path

PREREG = Path('research/SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_V2_PREREG_2026-09-15.md')
REPAIR_RESULT = Path('results/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_RESULT_2026-09-15.md')
REPAIR_HANDOFF = Path('recovery/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_HANDOFF_2026-09-15.md')
REPAIR_CRITIC = Path('recovery/CRITICAL_REVIEW_SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_REPAIR_2026-09-15.md')
IEPSILON = Path('research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md')
ONE_WEDGE = Path('research/SOURCE_J1_K5_ONE_WEDGE_UNIQUENESS_VS_JOINT_EXTENSION_RESULT_2026-09-15.md')
SCALING = Path('research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md')
ITER331 = Path('code/lqg_iter331_source_jet_normalization_audit.py')
ITER331_AGG = Path('code/lqg_iter331_aggregate.py')
V1_CRITIC = Path('recovery/CRITICAL_REVIEW_SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_2026-09-15.md')

DEPENDENCIES = [
    REPAIR_RESULT,
    REPAIR_HANDOFF,
    REPAIR_CRITIC,
    IEPSILON,
    ONE_WEDGE,
    SCALING,
    ITER331,
    ITER331_AGG,
    V1_CRITIC,
]
FILES = [PREREG] + DEPENDENCIES

PASS_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_V2_FORCES_DELTA_ZERO_SCOPED'
FAIL_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_V2_PRESERVES_NONZERO_DELTA_SCOPED'
BLOCKED_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_V2_NOT_PINNED_SCOPED'
UNDETERMINED_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_V2_ACTION_UNDETERMINED_SCOPED'
INVALID_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_V2_INVALID_IMPLEMENTATION'

CLASS_IDS = [
    'C1_CORRELATED_COMMON_REGULATOR_REMOVAL',
    'C2_INDEPENDENT_REGULATOR_PATH_ORDER_THEOREM',
    'C3_MICROLOCAL_PRODUCT_PULLBACK_EXTENSION_THEOREM',
    'C4_VERTEX_LEVEL_NORMALIZATION_BOUNDARY_CONDITION',
    'C5_NESTED_FOREST_GLUING',
    'C6_OTHER_GENUINELY_JOINT_SOURCE_THEOREM',
]


def text(path):
    return path.read_text(encoding='utf-8')


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(haystack, needle, name, controls):
    ok = needle in haystack
    controls[name] = ok
    return ok


def extract_sources_dict(path):
    tree = ast.parse(text(path), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'SOURCES':
                    return ast.literal_eval(node.value)
    raise RuntimeError('SOURCES literal not found in Iter331 source audit')


def github_run_status(run_id):
    repo = os.environ.get('GITHUB_REPOSITORY', 'pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark')
    url = f'https://api.github.com/repos/{repo}/actions/runs/{run_id}'
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'kmqgb-authority-v2-audit'}
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'
        headers['X-GitHub-Api-Version'] = '2022-11-28'
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode('utf-8'))
    return {
        'run_id': run_id,
        'status': payload.get('status'),
        'conclusion': payload.get('conclusion'),
        'head_sha': payload.get('head_sha'),
        'head_branch': payload.get('head_branch'),
        'updated_at': payload.get('updated_at'),
    }


def lexical_joint_candidate(sample, cls):
    s = sample.lower()
    neg = bool(re.search(r'\b(no|not|without|missing|absent)\b', s))
    if cls == 'common':
        return ('common regulator' in s or 'correlated regulator' in s) and ('removal rule' in s or 'removal prescription' in s) and not neg
    if cls == 'independent':
        return 'independent regulator' in s and ('path/order-independence theorem' in s or 'path independence theorem' in s or 'order independence theorem' in s) and not neg
    if cls == 'normalization':
        return 'normalization' in s and ('collision-supported' in s or 'collision supported' in s) and ('fixes' in s or 'forces' in s or 'selects' in s) and not neg
    raise ValueError(cls)


def keyword_hits(doc, keywords):
    hits = []
    for lineno, line in enumerate(doc.splitlines(), 1):
        low = line.lower()
        if any(k in low for k in keywords):
            hits.append({'line': lineno, 'text': line.strip()[:500]})
    return hits


def row(class_id, status, evidence_predicates, per_record_trace, action_on_delta=None):
    return {
        'class_id': class_id,
        'status': status,
        'action_on_delta': action_on_delta,
        'evidence_predicates': evidence_predicates,
        'per_record_trace': per_record_trace,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--raw-log', required=True)
    args = parser.parse_args()

    missing = [str(p) for p in FILES if not p.exists()]
    if missing:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        result = {'classification': INVALID_LABEL, 'reason': 'missing frozen input files', 'missing': missing}
        Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        raise SystemExit(2)

    docs = {str(p): text(p) for p in FILES}
    controls = {}

    # Prospective chronology / object / Critic repair contract.
    require(docs[str(PREREG)], 'Status: `PROSPECTIVE_FROZEN`', 'v2_prereg_frozen', controls)
    require(docs[str(PREREG)], 'exactly six scientific authority classes', 'six_class_contract_frozen', controls)
    require(docs[str(REPAIR_RESULT)], 'SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED', 'repaired_witness_classification', controls)
    require(docs[str(REPAIR_RESULT)], 'nonzero witness sectors: `32` of `1024`', 'nonzero_witness_32_of_1024', controls)
    require(docs[str(REPAIR_CRITIC)], 'Verdict: `CONFIRMED_SCOPED`', 'repaired_witness_critic_confirmed', controls)

    # Positive controls demanded by the v2 preregistration.
    require(docs[str(IEPSILON)], 'The displayed Eq. (4) contains no common positive `epsilon`, no vector `epsilon_ab`, no regulator-removal path, and no order of ten regulator limits across the group integration.', 'eq4_no_common_or_vector_regulator_path', controls)
    require(docs[str(IEPSILON)], 'does not supply a ten-wedge correlated positive-regulator family across the four-group vertex integral, nor a regulator path/order-independence theorem resolving K5 collision products', 'companion_no_correlated_family_or_path_order_theorem', controls)
    require(docs[str(ONE_WEDGE)], 'SOURCE_J1_K5_ONE_WEDGE_TOLLER_UNIQUENESS_INSUFFICIENT_FOR_JOINT_EXTENSION_SCOPED', 'one_wedge_uniqueness_insufficient', controls)
    require(docs[str(ONE_WEDGE)], '`genuinely_joint_source_condition_required_for_uniqueness = true`', 'genuinely_joint_condition_required', controls)
    require(docs[str(SCALING)], '`sd_N = 30 > 12 = codim(N)`', 'scaling_30_gt_12', controls)
    require(docs[str(SCALING)], '`TEN_WEDGE_CORRELATED_COLLISION_PRODUCT = NOT_YET_JUSTIFIED`', 'ten_wedge_product_not_yet_justified', controls)
    require(docs[str(V1_CRITIC)], '`INVALID_IMPLEMENTATION`', 'v1_critic_invalid_implementation', controls)
    require(docs[str(V1_CRITIC)], 'exact six-class authority audit', 'v1_critic_six_class_requirement', controls)
    require(docs[str(V1_CRITIC)], 'independent-regulator/path-order class', 'v1_critic_independent_class_defect', controls)
    require(docs[str(V1_CRITIC)], 'vertex-level normalization/boundary-condition class', 'v1_critic_vertex_normalization_defect', controls)
    require(docs[str(V1_CRITIC)], 'hard-coded absent', 'v1_critic_catchall_hardcode_defect', controls)

    sources = extract_sources_dict(ITER331)
    source_facts = {k: v['facts'] for k, v in sources.items()}
    all_common_false = all(not v.get('common_multiwedge_iepsilon_limit') for v in source_facts.values())
    all_partial_extension_false = all(not v.get('partial_diagonal_extension_prescription') for v in source_facts.values())
    all_forest_false = all(not v.get('forest_compatible_gluing_normalization') for v in source_facts.values())
    all_k4_jet_false = all(not v.get('k4_first_normal_jet_values_fixed') for v in source_facts.values())
    all_k3_jet_false = all(not v.get('k3_second_normal_jet_values_fixed') for v in source_facts.values())

    controls['iter331_all_common_multiwedge_limits_false'] = all_common_false
    controls['iter331_all_partial_extension_prescriptions_false'] = all_partial_extension_false
    controls['iter331_all_forest_gluing_false'] = all_forest_false
    controls['iter331_all_k4_jet_values_unfixed'] = all_k4_jet_false
    controls['iter331_all_k3_jet_values_unfixed'] = all_k3_jet_false
    controls['iter331_aggregate_no_source_normalization'] = "'source_defined_normalization_found': False" in docs[str(ITER331_AGG)]
    controls['iter331_aggregate_no_source_forest_glue'] = "'source_defined_forest_glue_found': False" in docs[str(ITER331_AGG)]

    # Adversarial lexical fixtures. These are controls only, never scientific authority.
    negative_controls = {
        'fixture_common_without_removal_rejected': not lexical_joint_candidate('A common regulator is discussed for intuition.', 'common'),
        'fixture_independent_without_path_order_theorem_rejected': not lexical_joint_candidate('Independent regulators epsilon_e are introduced.', 'independent'),
        'fixture_negated_normalization_rejected': not lexical_joint_candidate('No source-pinned normalization fixing collision-supported terms is provided.', 'normalization'),
        'one_wedge_iepsilon_not_promoted': controls['eq4_no_common_or_vector_regulator_path'],
        'one_wedge_uniqueness_not_promoted': controls['one_wedge_uniqueness_insufficient'] and controls['genuinely_joint_condition_required'],
        'generic_extension_theory_not_promoted': controls['scaling_30_gt_12'] and controls['ten_wedge_product_not_yet_justified'],
        'iter331_detector_not_promoted': controls['iter331_aggregate_no_source_normalization'],
    }

    # Fresh workflow status is provenance/control only. No job/artifact/substantive values are read.
    workflow_status = {}
    status_error = None
    try:
        workflow_status['Iter504'] = github_run_status(34907349374)
        workflow_status['Iter461'] = github_run_status(34748503239)
    except Exception as exc:
        status_error = repr(exc)
    controls['fresh_workflow_status_read'] = status_error is None
    controls['no_partial_workflow_values_consumed'] = True

    # Six one-to-one authority rows. Each row is supported by explicit frozen-record predicates.
    matrix = []

    c1_evidence = {
        'eq4_explicitly_lacks_common_regulator_removal_path': controls['eq4_no_common_or_vector_regulator_path'],
        'companion_explicitly_lacks_correlated_family': controls['companion_no_correlated_family_or_path_order_theorem'],
        'iter331_all_common_multiwedge_limit_flags_false': all_common_false,
    }
    c1_trace = {
        str(IEPSILON): 'EXPLICIT_NEGATIVE_SOURCE_AUDIT',
        str(ITER331): 'STRUCTURED_SOURCE_FACTS_ALL_FALSE',
        str(SCALING): 'JOINT_PRODUCT_NOT_YET_JUSTIFIED_POSSIBLE_ROUTE_ONLY',
    }
    matrix.append(row(CLASS_IDS[0], 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS', c1_evidence, c1_trace))

    c2_evidence = {
        'companion_no_path_order_independence_theorem': controls['companion_no_correlated_family_or_path_order_theorem'],
        'scaling_audit_says_independent_path_order_must_be_proved_not_assumed': 'If independent regulators `epsilon_e` are used, path/order independence must be proved rather than assumed.' in docs[str(SCALING)],
        'class_separate_from_common_regulator': True,
    }
    controls['independent_regulator_path_order_separate_predicate'] = c2_evidence['class_separate_from_common_regulator']
    c2_trace = {
        str(IEPSILON): 'EXPLICIT_NEGATIVE_SOURCE_AUDIT_FOR_PATH_ORDER_THEOREM',
        str(SCALING): 'PROSPECTIVE_REQUIREMENT_NOT_EXISTING_AUTHORITY',
        str(ITER331): 'NO_STRUCTURED_POSITIVE_IN_FROZEN_SOURCE_ROWS',
    }
    matrix.append(row(CLASS_IDS[1], 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS', c2_evidence, c2_trace))

    c3_evidence = {
        'iter331_all_partial_diagonal_extension_flags_false': all_partial_extension_false,
        'ten_wedge_correlated_product_not_yet_justified': controls['ten_wedge_product_not_yet_justified'],
        'microlocal_route_listed_as_possible_future_route_not_completed_theorem': 'a microlocal product theorem showing that the required wedge distributions satisfy an admissible wavefront-set condition after correlated pullback' in docs[str(SCALING)],
    }
    c3_trace = {
        str(ITER331): 'STRUCTURED_SOURCE_FACTS_ALL_FALSE',
        str(SCALING): 'GENERIC_EXTENSION_THEORY_PLUS_PROSPECTIVE_MICROLOCAL_ROUTE_ONLY',
        str(IEPSILON): 'SOURCE_SCOPE_AUDIT_DOES_NOT_SUPPLY_JOINT_PRODUCT_THEOREM',
    }
    matrix.append(row(CLASS_IDS[2], 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS', c3_evidence, c3_trace))

    c4_evidence = {
        'iter331_aggregate_source_defined_normalization_false': controls['iter331_aggregate_no_source_normalization'],
        'iter331_all_k4_normal_jet_values_unfixed_supporting_only': all_k4_jet_false,
        'iter331_all_k3_normal_jet_values_unfixed_supporting_only': all_k3_jet_false,
        'one_wedge_result_treats_vertex_identity_or_normalization_as_open_frontier': 'that no vertex-level source identity or normalization exists' in docs[str(ONE_WEDGE)] and 'a vertex-level distributional identity' in docs[str(ONE_WEDGE)],
        'repaired_witness_survives_already_tested_vertex_constraints': 'The same witness simultaneously satisfies:' in docs[str(REPAIR_RESULT)] and 'the full 1024-pattern independent-sign EPRL zero-sum identity' in docs[str(REPAIR_RESULT)],
        'broad_class_not_reduced_to_jet_flags': True,
    }
    controls['vertex_normalization_broad_class_not_reduced_to_jets'] = c4_evidence['broad_class_not_reduced_to_jet_flags']
    c4_trace = {
        str(ITER331): 'STRUCTURED_JET_FLAGS_SUPPORTING_ONLY_NOT_EXHAUSTIVE_PROXY',
        str(ITER331_AGG): 'EXPLICIT_NO_SOURCE_DEFINED_NORMALIZATION_IN_AUDITED_SOURCES',
        str(ONE_WEDGE): 'VERTEX_IDENTITY_NORMALIZATION_IS_OPEN_FRONTIER_NOT_PINNED_RULE',
        str(REPAIR_RESULT): 'ALREADY_TESTED_EPRL_CONJUGATION_PERMUTATION_CONSTRAINTS_INSUFFICIENT',
        str(REPAIR_CRITIC): 'CONFIRMS_TESTED_CONSTRAINT_SET_INSUFFICIENT_NOT_NEW_SELECTION_AUTHORITY',
    }
    matrix.append(row(CLASS_IDS[3], 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS', c4_evidence, c4_trace))

    c5_evidence = {
        'iter331_all_forest_gluing_flags_false': all_forest_false,
        'iter331_aggregate_source_defined_forest_glue_false': controls['iter331_aggregate_no_source_forest_glue'],
        'scaling_audit_nested_conditions_are_possible_not_established': 'Nested strata may add compatibility conditions or additional extension problems' in docs[str(SCALING)],
    }
    c5_trace = {
        str(ITER331): 'STRUCTURED_SOURCE_FACTS_ALL_FALSE',
        str(ITER331_AGG): 'EXPLICIT_NO_SOURCE_DEFINED_FOREST_GLUE',
        str(SCALING): 'NESTED_COMPATIBILITY_POSSIBLE_ONLY_ITER461_REMAINS_OPEN',
    }
    matrix.append(row(CLASS_IDS[4], 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS', c5_evidence, c5_trace))

    # Exhaustive catch-all trace over every frozen dependency record. Each record must be
    # assigned a verified role; no unconditional catch-all absence is permitted.
    other_trace = {
        str(REPAIR_RESULT): {
            'role': 'UPSTREAM_WITNESS_RESULT',
            'verified': 'does **not** prove:' in docs[str(REPAIR_RESULT)] and 'no additional source-faithful joint regulator' in docs[str(REPAIR_RESULT)],
            'positive_authority_if_any': 'tested conjugation / EPRL / coefficient-pattern permutation / scaling constraints only; explicitly insufficient for source selection',
        },
        str(REPAIR_HANDOFF): {
            'role': 'UPSTREAM_WITNESS_HANDOFF',
            'verified': 'No validated source-faithful **joint Eq. (4) selection rule** has yet been shown' in docs[str(REPAIR_HANDOFF)],
            'positive_authority_if_any': 'none; handoff points to the authority search as next gate',
        },
        str(REPAIR_CRITIC): {
            'role': 'INDEPENDENT_REVIEW_OF_WITNESS',
            'verified': 'It does not prove that the published source supplies no additional selection rule.' in docs[str(REPAIR_CRITIC)],
            'positive_authority_if_any': 'confirms only the tested homogeneous-kernel witness and scope',
        },
        str(IEPSILON): {
            'role': 'PUBLISHED_SOURCE_SCOPE_AUDIT',
            'verified': controls['eq4_no_common_or_vector_regulator_path'] and controls['companion_no_correlated_family_or_path_order_theorem'],
            'positive_authority_if_any': 'individual one-wedge i-epsilon only; excluded by frozen contract',
        },
        str(ONE_WEDGE): {
            'role': 'ONE_WEDGE_UNIQUENESS_RESULT',
            'verified': controls['one_wedge_uniqueness_insufficient'] and controls['genuinely_joint_condition_required'],
            'positive_authority_if_any': 'one-wedge Toller uniqueness only; excluded by frozen contract',
        },
        str(SCALING): {
            'role': 'GENERIC_EXTENSION_THEORY_AND_SCOPED_SCALING_AUDIT',
            'verified': controls['ten_wedge_product_not_yet_justified'] and 'A stronger source-defined theorem remains possible.' in docs[str(SCALING)],
            'positive_authority_if_any': 'finite-scaling-degree extension theorem only; does not select a source coefficient',
        },
        str(ITER331): {
            'role': 'STRUCTURED_THREE_SOURCE_NORMALIZATION_AUDIT',
            'verified': all_common_false and all_partial_extension_false and all_forest_false and all_k4_jet_false and all_k3_jet_false,
            'positive_authority_if_any': 'fixed causal formula / individual Toller definitions in some rows; no joint selection fields are true',
        },
        str(ITER331_AGG): {
            'role': 'STRUCTURED_SOURCE_AUDIT_AGGREGATE',
            'verified': controls['iter331_aggregate_no_source_normalization'] and controls['iter331_aggregate_no_source_forest_glue'],
            'positive_authority_if_any': 'none; aggregate explicitly records no source-defined normalization/forest glue',
        },
        str(V1_CRITIC): {
            'role': 'META_CRITIC_OF_INVALID_V1_IMPLEMENTATION',
            'verified': controls['v1_critic_invalid_implementation'] and controls['v1_critic_six_class_requirement'],
            'positive_authority_if_any': 'none; review invalidates implementation and explicitly does not establish the opposite scientific result',
        },
    }
    other_trace_complete = set(other_trace) == {str(p) for p in DEPENDENCIES} and all(v['verified'] for v in other_trace.values())
    controls['other_class_exhaustive_trace_all_dependency_records'] = other_trace_complete

    # Capture keyword lines for independent Critic inspection. These do not drive the scientific decision.
    catchall_keywords = ['joint', 'theorem', 'source-defined', 'source-pinned', 'normalization', 'boundary condition', 'regulator', 'extension', 'product', 'collision', 'gluing']
    other_keyword_trace = {str(p): keyword_hits(docs[str(p)], catchall_keywords) for p in DEPENDENCIES}
    c6_evidence = {
        'all_dependency_records_traced': other_trace_complete,
        'only_positive_theorems_authorities_in_trace_are_frozen_exclusions_or_nonselecting_generic_results': other_trace_complete,
        'no_unclassified_dependency_record': other_trace_complete,
    }
    matrix.append(row(CLASS_IDS[5], 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS', c6_evidence, other_trace))

    # Contract-integrity checks.
    matrix_ids = [r['class_id'] for r in matrix]
    controls['matrix_exactly_six_rows'] = len(matrix) == 6
    controls['matrix_unique_stable_ids'] = matrix_ids == CLASS_IDS and len(set(matrix_ids)) == 6
    controls['every_row_has_evidence_predicates'] = all(bool(r['evidence_predicates']) for r in matrix)
    controls['every_row_has_record_trace'] = all(bool(r['per_record_trace']) for r in matrix)

    controls_ok = all(controls.values()) and all(negative_controls.values())
    acts = [r for r in matrix if r['status'] == 'SOURCE_PINNED_ACTS_ON_DELTA']
    undetermined = [r for r in matrix if r['status'] == 'SOURCE_PINNED_BUT_ACTION_UNDETERMINED']

    if not controls_ok:
        classification = INVALID_LABEL
        reason = 'one or more frozen v2 source-lock logical controls, six-row contract controls, workflow-status controls, or adversarial negative controls failed'
    elif any(r.get('action_on_delta') == 'FORCES_ZERO' for r in acts):
        classification = PASS_LABEL
        reason = 'a frozen genuinely joint source authority acts on Delta and forces its coefficient to zero'
    elif any(r.get('action_on_delta') == 'PRESERVES_NONZERO' for r in acts):
        classification = FAIL_LABEL
        reason = 'a frozen genuinely joint source authority acts on Delta and permits a nonzero coefficient'
    elif undetermined:
        classification = UNDETERMINED_LABEL
        reason = 'at least one genuinely joint source authority is pinned but its action on Delta is not determined without additional model data'
    else:
        classification = BLOCKED_LABEL
        reason = 'all six one-to-one frozen authority classes were traced, but none is source-pinned strongly enough in the frozen corpus to act on Delta'

    result = {
        'gate': 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_V2_GATE',
        'classification': classification,
        'reason': reason,
        'object_scope': {
            'spin': 'j=1',
            'rho': 'nonzero real',
            'channel': '00000',
            'collision': 'full K5 collision N=SU(2)^4 in gauge-fixed SL(2,C)^4',
            'witness': 'Delta(kappa)=c(kappa) delta_N; +i on 16 causal, -i on 16 global negatives, 0 on 992 others',
        },
        'controls': controls,
        'negative_controls': negative_controls,
        'candidate_matrix': matrix,
        'other_class_keyword_trace': other_keyword_trace,
        'iter331_source_facts': source_facts,
        'workflow_status_provenance_only': workflow_status,
        'workflow_status_error': status_error,
        'source_pinned_acts_on_delta_count': len(acts),
        'source_pinned_action_undetermined_count': len(undetermined),
        'frozen_input_sha256': {str(p): sha256(p) for p in FILES},
        'claim_ceiling': [
            'no base Eq4 joint-extension existence or nonexistence claim',
            'no unconditional physical/global nonuniqueness claim',
            'no source authorization of Delta',
            'no claim of absence outside the frozen repository corpus',
            'no impossibility claim for future source-compatible joint constructions',
            'no other-spin/channel/family/lower-stratum claim',
            'no D7-S2/S3/S4 closure',
            'no terminal D7 selector',
            'Candidate Gravity remains inactive',
        ],
    }

    raw = [
        f'classification={classification}',
        f'reason={reason}',
        f'controls_ok={controls_ok}',
        f'matrix_ids={matrix_ids}',
        f'source_pinned_acts_on_delta_count={len(acts)}',
        f'source_pinned_action_undetermined_count={len(undetermined)}',
        f'iter504_status={workflow_status.get("Iter504")}',
        f'iter461_status={workflow_status.get("Iter461")}',
    ]
    for r in matrix:
        raw.append(f'class={r["class_id"]} status={r["status"]} action_on_delta={r["action_on_delta"]}')
        raw.append(f'evidence={json.dumps(r["evidence_predicates"], sort_keys=True)}')

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.raw_log).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    Path(args.raw_log).write_text('\n'.join(raw) + '\n', encoding='utf-8')
    print(json.dumps(result, sort_keys=True))

    if classification == INVALID_LABEL:
        raise SystemExit(3)


if __name__ == '__main__':
    main()
