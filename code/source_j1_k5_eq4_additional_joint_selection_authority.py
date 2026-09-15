#!/usr/bin/env python3
import argparse
import ast
import hashlib
import json
from pathlib import Path

PREREG = Path('research/SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_PREREG_2026-09-15.md')
REPAIR_RESULT = Path('results/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_RESULT_2026-09-15.md')
REPAIR_HANDOFF = Path('recovery/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_HANDOFF_2026-09-15.md')
CRITIC = Path('recovery/CRITICAL_REVIEW_SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_REPAIR_2026-09-15.md')
IEPSILON = Path('research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md')
ONE_WEDGE = Path('research/SOURCE_J1_K5_ONE_WEDGE_UNIQUENESS_VS_JOINT_EXTENSION_RESULT_2026-09-15.md')
SCALING = Path('research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md')
ITER331 = Path('code/lqg_iter331_source_jet_normalization_audit.py')
ITER331_AGG = Path('code/lqg_iter331_aggregate.py')

FILES = [PREREG, REPAIR_RESULT, REPAIR_HANDOFF, CRITIC, IEPSILON, ONE_WEDGE, SCALING, ITER331, ITER331_AGG]

PASS_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_FORCES_DELTA_ZERO_SCOPED'
FAIL_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_PRESERVES_NONZERO_DELTA_SCOPED'
BLOCKED_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_NOT_PINNED_SCOPED'
INVALID_LABEL = 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_GATE_INVALID_IMPLEMENTATION'


def text(path):
    return path.read_text(encoding='utf-8')


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_sources_dict(path):
    tree = ast.parse(text(path), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'SOURCES':
                    return ast.literal_eval(node.value)
    raise RuntimeError('SOURCES literal not found in Iter331 audit')


def require(haystack, needle, name, controls):
    ok = needle in haystack
    controls[name] = ok
    return ok


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    p.add_argument('--raw-log', required=True)
    args = p.parse_args()

    missing = [str(x) for x in FILES if not x.exists()]
    if missing:
        result = {
            'classification': INVALID_LABEL,
            'reason': 'missing frozen input files',
            'missing': missing,
        }
        Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
        raise SystemExit(2)

    docs = {str(p): text(p) for p in FILES}
    controls = {}

    # Prospective freeze and exact object controls.
    require(docs[str(PREREG)], 'Status: `PROSPECTIVE_FROZEN`', 'prereg_frozen', controls)
    require(docs[str(REPAIR_RESULT)], 'SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED', 'repair_classification_present', controls)
    require(docs[str(REPAIR_HANDOFF)], 'Delta(kappa)=c(kappa) delta_N', 'delta_witness_present', controls)
    require(docs[str(CRITIC)], 'Verdict: `CONFIRMED_SCOPED`', 'critic_confirmed', controls)

    # Frozen positive controls: one-wedge/joint separation, scaling ambiguity, repaired witness.
    require(docs[str(IEPSILON)], 'SOURCE_CAUSAL_VERTEX_PUBLISHED_IEPSILON_IS_ONE_WEDGE_NOT_JOINT_COLLISION_REGULATOR_SCOPED', 'iepsilon_one_wedge_scope', controls)
    require(docs[str(IEPSILON)], 'no common positive `epsilon`', 'no_common_epsilon_in_displayed_eq4', controls)
    require(docs[str(ONE_WEDGE)], 'SOURCE_J1_K5_ONE_WEDGE_TOLLER_UNIQUENESS_INSUFFICIENT_FOR_JOINT_EXTENSION_SCOPED', 'one_wedge_uniqueness_insufficient', controls)
    require(docs[str(ONE_WEDGE)], '`genuinely_joint_source_condition_required_for_uniqueness = true`', 'joint_condition_required', controls)
    require(docs[str(SCALING)], '`sd_N = 30 > 12 = codim(N)`', 'scaling_30_vs_12', controls)
    require(docs[str(SCALING)], '`TEN_WEDGE_CORRELATED_COLLISION_PRODUCT = NOT_YET_JUSTIFIED`', 'joint_product_not_yet_justified', controls)
    require(docs[str(CRITIC)], '`32/1024` support', 'critic_nonzero_witness_control', controls)

    # Source-normalization matrix is extracted from the historical audit source itself,
    # rather than copied into this gate as a new scientific assertion.
    sources = extract_sources_dict(ITER331)
    source_facts = {k: v['facts'] for k, v in sources.items()}
    iter331_candidates = {
        'common_multiwedge_iepsilon_limit': any(v.get('common_multiwedge_iepsilon_limit') for v in source_facts.values()),
        'partial_diagonal_extension_prescription': any(v.get('partial_diagonal_extension_prescription') for v in source_facts.values()),
        'forest_compatible_gluing_normalization': any(v.get('forest_compatible_gluing_normalization') for v in source_facts.values()),
        'k4_first_normal_jet_values_fixed': any(v.get('k4_first_normal_jet_values_fixed') for v in source_facts.values()),
        'k3_second_normal_jet_values_fixed': any(v.get('k3_second_normal_jet_values_fixed') for v in source_facts.values()),
    }

    # Negative controls: these must not be promoted as genuinely joint selection authority.
    negative_controls = {
        'one_wedge_iepsilon_not_joint': controls['iepsilon_one_wedge_scope'] and controls['no_common_epsilon_in_displayed_eq4'],
        'one_wedge_uniqueness_not_joint': controls['one_wedge_uniqueness_insufficient'] and controls['joint_condition_required'],
        'generic_extension_theory_not_selection': controls['scaling_30_vs_12'] and controls['joint_product_not_yet_justified'],
        'iter331_rank_detector_not_physical_normalization': 'not source-defined physical normalization conditions' in docs[str(ITER331_AGG)] or 'source_defined_normalization_found' in docs[str(ITER331_AGG)],
    }

    candidate_matrix = []
    # Common/independent regulator authority.
    candidate_matrix.append({
        'candidate': 'correlated_or_independent_multiwedge_regulator_with_removal_rule',
        'status': 'SOURCE_PINNED_BUT_ACTION_UNDETERMINED' if iter331_candidates['common_multiwedge_iepsilon_limit'] else 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS',
        'evidence': {
            'published_iepsilon_scope_one_wedge_only': controls['iepsilon_one_wedge_scope'],
            'iter331_common_multiwedge_iepsilon_limit_any': iter331_candidates['common_multiwedge_iepsilon_limit'],
        },
        'action_on_delta': None,
    })
    candidate_matrix.append({
        'candidate': 'partial_diagonal_microlocal_product_or_extension_prescription',
        'status': 'SOURCE_PINNED_BUT_ACTION_UNDETERMINED' if iter331_candidates['partial_diagonal_extension_prescription'] else 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS',
        'evidence': {
            'iter331_partial_diagonal_extension_any': iter331_candidates['partial_diagonal_extension_prescription'],
            'scaling_audit_joint_product_not_yet_justified': controls['joint_product_not_yet_justified'],
        },
        'action_on_delta': None,
    })
    candidate_matrix.append({
        'candidate': 'forest_or_nested_stratum_gluing_normalization',
        'status': 'SOURCE_PINNED_BUT_ACTION_UNDETERMINED' if iter331_candidates['forest_compatible_gluing_normalization'] else 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS',
        'evidence': {'iter331_forest_compatible_gluing_any': iter331_candidates['forest_compatible_gluing_normalization']},
        'action_on_delta': None,
    })
    jet_any = iter331_candidates['k4_first_normal_jet_values_fixed'] or iter331_candidates['k3_second_normal_jet_values_fixed']
    candidate_matrix.append({
        'candidate': 'source_fixed_collision_normal_jet_values',
        'status': 'SOURCE_PINNED_BUT_ACTION_UNDETERMINED' if jet_any else 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS',
        'evidence': {
            'iter331_k4_first_normal_jet_values_fixed_any': iter331_candidates['k4_first_normal_jet_values_fixed'],
            'iter331_k3_second_normal_jet_values_fixed_any': iter331_candidates['k3_second_normal_jet_values_fixed'],
        },
        'action_on_delta': None,
    })
    candidate_matrix.append({
        'candidate': 'other_genuinely_joint_source_theorem_in_frozen_corpus',
        'status': 'NOT_SOURCE_PINNED_IN_FROZEN_CORPUS',
        'evidence': {
            'one_wedge_result_requires_genuinely_joint_condition': controls['joint_condition_required'],
            'critic_next_gate_requests_additional_authority': 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_GATE' in docs[str(CRITIC)],
        },
        'action_on_delta': None,
    })

    controls_ok = all(controls.values()) and all(negative_controls.values())
    acting = [r for r in candidate_matrix if r['status'] == 'SOURCE_PINNED_ACTS_ON_DELTA']
    pinned_undetermined = [r for r in candidate_matrix if r['status'] == 'SOURCE_PINNED_BUT_ACTION_UNDETERMINED']

    if not controls_ok:
        classification = INVALID_LABEL
        reason = 'one or more frozen positive/negative controls failed'
    elif any(r.get('action_on_delta') == 'FORCES_ZERO' for r in acting):
        classification = PASS_LABEL
        reason = 'a frozen genuinely joint source authority acts on Delta and forces its coefficient to zero'
    elif any(r.get('action_on_delta') == 'PRESERVES_NONZERO' for r in acting):
        classification = FAIL_LABEL
        reason = 'a frozen genuinely joint source authority acts on Delta and permits a nonzero coefficient'
    else:
        classification = BLOCKED_LABEL
        reason = 'the frozen validated corpus contains no genuinely joint source rule pinned strongly enough to decide the Delta coefficient'

    result = {
        'gate': 'SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_GATE',
        'classification': classification,
        'reason': reason,
        'object_scope': {
            'spin': 'j=1',
            'rho': 'nonzero real',
            'channel': '00000',
            'collision': 'full K5 collision N=SU(2)^4 in SL(2,C)^4',
            'witness': 'Delta(kappa)=c(kappa) delta_N; +i causal, -i global-negated causal, 0 otherwise',
        },
        'controls': controls,
        'negative_controls': negative_controls,
        'iter331_source_facts': source_facts,
        'candidate_matrix': candidate_matrix,
        'pinned_but_action_undetermined_count': len(pinned_undetermined),
        'source_pinned_acts_on_delta_count': len(acting),
        'frozen_input_sha256': {str(f): sha256(f) for f in FILES},
        'claim_ceiling': [
            'no base-extension existence/nonexistence claim',
            'no unconditional physical/global nonuniqueness claim',
            'no source authorization of Delta',
            'no impossibility claim for future source-compatible joint constructions',
            'no other-spin/channel/family/lower-stratum claim',
            'no D7-S2/S3/S4 closure',
            'no terminal D7 selector',
            'Candidate Gravity remains inactive',
        ],
    }

    raw_lines = [
        f"classification={classification}",
        f"reason={reason}",
        f"controls_ok={controls_ok}",
        f"source_pinned_acts_on_delta_count={len(acting)}",
        f"pinned_but_action_undetermined_count={len(pinned_undetermined)}",
    ]
    for row in candidate_matrix:
        raw_lines.append(f"candidate={row['candidate']} status={row['status']} action_on_delta={row['action_on_delta']}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.raw_log).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    Path(args.raw_log).write_text('\n'.join(raw_lines) + '\n', encoding='utf-8')
    print(json.dumps(result, sort_keys=True))

    if classification == INVALID_LABEL:
        raise SystemExit(3)


if __name__ == '__main__':
    main()
