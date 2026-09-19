#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

GATE = 'ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_ADVERSARIAL_GATE'
PREREG = '04a47f859323bea69472f142ec1a2f4b97e5df0b'
SOURCE_AGGREGATE = Path('code/iter504v_phase_b_aggregate.py')
SOURCE_AGGREGATE_BLOB = 'ae1932a7cdd98a1cc74f1b2f07bc295e0c097274'
SOURCE_RUN = 35405065903
SOURCE_HEAD = '31fcdacffcc394e96b73917083281edb90d6753c'

SOURCE_GATE = 'ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE'
SOURCE_PREREG = 'e42caf47f9201d79cd89b79dc72b90f696e3ec5d'
DESIGN_AUTHORITY = 'a4006f336a49f655534a2f76a443a3d60a47cd85'
DESIGN_STATIC_CRITIC = '722c7e09bf077c0cb29c3ac0ac2ed724b99290f4'
IMPLEMENTATION_AUTHORITY = '42a2f035a80c474ebc7e5f57934ad9ba78ce9937'
CANONICAL_SHA256 = '3cac282175830e795394dca5202f5368b27120817f2d4abd9eba54fc6c9f1e6f'
PASS = 'ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED'
INC = 'ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED'
INVALID = 'ITER504V_BROADER_DOMAIN_INVALID'

GATE_PASS = 'ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_DEFECTS_VERIFIED_SCOPED'
GATE_FAIL = 'ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_DEFECTS_NOT_REPRODUCED_SCOPED'
GATE_BLOCKED = 'ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_GATE_BLOCKED_SCOPED'
GATE_INVALID = 'INVALID_IMPLEMENTATION'

FOREIGN_PROJECTION_KEY = 'FOREIGN|b9|p9|x99'
FOREIGN_PROVENANCE_KEY = 'FOREIGN_PROVENANCE_KEY'


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode())


def sha_json(obj) -> str:
    return sha256_bytes(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode())


def canonical_state_ids() -> list[str]:
    return [
        f'{causal}|b{block}|p{path}|x{box:02d}'
        for causal in ('0to5', '1to4', '2to3')
        for block in range(4)
        for path in range(4)
        for box in range(16)
    ]


def base_assembly(classification: str = PASS, unresolved: bool = False) -> dict:
    ids = canonical_state_ids()
    projection = {sid: sha256_text('decision:' + sid) for sid in ids}
    unresolved_map = {sid: 0 for sid in ids}
    counterexamples = []
    total_unresolved = 0
    if unresolved:
        unresolved_map[ids[0]] = 1
        counterexamples = [ids[0]]
        total_unresolved = 1
    sequence = sha_json([[sid, projection[sid]] for sid in ids])
    return {
        'gate': SOURCE_GATE,
        'preregistration_commit': SOURCE_PREREG,
        'design_authority_commit': DESIGN_AUTHORITY,
        'design_static_critic_commit': DESIGN_STATIC_CRITIC,
        'implementation_authority_commit': IMPLEMENTATION_AUTHORITY,
        'canonical_768_record_sequence_sha256': CANONICAL_SHA256,
        'classification': classification,
        'errors': [],
        'state_ids': ids,
        'total_cases': 768,
        'case_file_sha256': {sid: sha256_text('case:' + sid) for sid in ids},
        'decision_projection_sha256_by_state': projection,
        'decision_projection_sequence_sha256': sequence,
        'unresolved_leaf_count_by_state': unresolved_map,
        'total_unresolved_leaves': total_unresolved,
        'counterexample_state_ids': counterexamples,
        'total_visited_nodes': 768,
        'total_terminal_leaves': 768,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'max_depth': 3,
        'channels': 243,
        'r_cohort': [6, 8, 10, 12],
        'rho_cohort': [0.35, 0.9, 1.6, 2.7],
    }


def oracle_semantics(obj: dict) -> list[str]:
    errors = []
    ids = canonical_state_ids()
    unresolved = obj.get('unresolved_leaf_count_by_state', {})
    total = obj.get('total_unresolved_leaves')
    cex = obj.get('counterexample_state_ids')
    expected_total = sum(int(unresolved.get(sid, 0)) for sid in ids)
    expected_cex = [sid for sid in ids if int(unresolved.get(sid, 0)) > 0]
    if total != expected_total:
        errors.append('unresolved_total_binding')
    if cex != expected_cex:
        errors.append('counterexample_binding')
    expected_class = PASS if expected_total == 0 else INC
    if obj.get('classification') != expected_class:
        errors.append('classification_unresolved_binding')
    return errors


def oracle_projection_keys(obj: dict) -> list[str]:
    return [] if set(obj.get('decision_projection_sha256_by_state', {})) == set(canonical_state_ids()) else ['projection_key_set']


def oracle_provenance_keys(obj: dict) -> list[str]:
    return [] if set(obj.get('case_file_sha256', {})) == set(canonical_state_ids()) else ['provenance_key_set']


def run_source_aggregate(label: str, a_obj: dict, b_obj: dict) -> dict:
    with tempfile.TemporaryDirectory(prefix='iter504v-agg-gate-') as td:
        root = Path(td)
        a_path = root / 'a.json'
        b_path = root / 'b.json'
        out_path = root / 'aggregate.json'
        a_path.write_text(json.dumps(a_obj, indent=2, sort_keys=True) + '\n')
        b_path.write_text(json.dumps(b_obj, indent=2, sort_keys=True) + '\n')
        cp = subprocess.run(
            [sys.executable, str(SOURCE_AGGREGATE), '--a', str(a_path), '--b', str(b_path), '--out', str(out_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        out = json.loads(out_path.read_text()) if out_path.exists() else None
        return {
            'label': label,
            'returncode': cp.returncode,
            'stdout_sha256': sha256_text(cp.stdout),
            'stderr_sha256': sha256_text(cp.stderr),
            'classification': None if out is None else out.get('classification'),
            'errors': None if out is None else out.get('errors'),
            'cross_environment_exact_decision_agreement': None if out is None else out.get('cross_environment_exact_decision_agreement'),
            'aggregate_payload_sha256': None if out is None else out.get('aggregate_payload_sha256'),
            'output_present': out is not None,
        }


def accepted_nominal(result: dict, expected_class: str) -> bool:
    return (
        result.get('returncode') == 0
        and result.get('classification') == expected_class
        and result.get('errors') == []
        and result.get('cross_environment_exact_decision_agreement') is True
    )


def rejected_invalid(result: dict) -> bool:
    return result.get('returncode') == 2 and result.get('classification') == INVALID and bool(result.get('errors'))


def main() -> int:
    if not SOURCE_AGGREGATE.is_file():
        result = {
            'gate': GATE,
            'preregistration_commit': PREREG,
            'classification': GATE_BLOCKED,
            'errors': ['source_aggregate_missing'],
            'production_science_consumed': False,
            'source_run_classified': False,
        }
        print(json.dumps(result, indent=2, sort_keys=True))
        return 3

    ids = canonical_state_ids()
    harness_errors = []
    if len(ids) != 768 or len(set(ids)) != 768:
        harness_errors.append('canonical_state_cardinality')
    if sha256_text('\n'.join(ids) + '\n') != CANONICAL_SHA256:
        harness_errors.append('canonical_state_sequence_hash')

    baseline_pass = base_assembly(PASS, False)
    baseline_inc = base_assembly(INC, True)

    r_baseline_pass = run_source_aggregate('positive_pass_zero_unresolved', baseline_pass, copy.deepcopy(baseline_pass))
    r_baseline_inc = run_source_aggregate('positive_inconclusive_one_unresolved', baseline_inc, copy.deepcopy(baseline_inc))

    c_class_a = base_assembly(PASS, False)
    c_class_b = base_assembly(INC, False)
    r_control_class = run_source_aggregate('negative_cross_environment_classification_disagreement', c_class_a, c_class_b)

    c_state_a = base_assembly(PASS, False)
    c_state_b = copy.deepcopy(c_state_a)
    c_state_b['state_ids'][0], c_state_b['state_ids'][1] = c_state_b['state_ids'][1], c_state_b['state_ids'][0]
    r_control_state = run_source_aggregate('negative_cross_environment_state_identity_disagreement', c_state_a, c_state_b)

    c_proj_a = base_assembly(PASS, False)
    c_proj_b = copy.deepcopy(c_proj_a)
    c_proj_b['decision_projection_sha256_by_state'][ids[0]] = sha256_text('mutated:' + ids[0])
    r_control_projection = run_source_aggregate('negative_cross_environment_projection_disagreement', c_proj_a, c_proj_b)

    cand_a = base_assembly(PASS, True)
    cand_a_oracle = oracle_semantics(cand_a)
    r_candidate_a = run_source_aggregate('candidate_A_pass_with_unresolved_evidence', cand_a, copy.deepcopy(cand_a))

    cand_b = base_assembly(PASS, False)
    v = cand_b['decision_projection_sha256_by_state'].pop(ids[0])
    cand_b['decision_projection_sha256_by_state'][FOREIGN_PROJECTION_KEY] = v
    cand_b_oracle = oracle_projection_keys(cand_b)
    r_candidate_b = run_source_aggregate('candidate_B_noncanonical_projection_keyset', cand_b, copy.deepcopy(cand_b))

    cand_c = base_assembly(PASS, False)
    v = cand_c['case_file_sha256'].pop(ids[0])
    cand_c['case_file_sha256'][FOREIGN_PROVENANCE_KEY] = v
    cand_c_oracle = oracle_provenance_keys(cand_c)
    r_candidate_c = run_source_aggregate('candidate_C_noncanonical_provenance_keyset', cand_c, copy.deepcopy(cand_c))

    controls = {
        'positive_pass_zero_unresolved': accepted_nominal(r_baseline_pass, PASS),
        'positive_inconclusive_one_unresolved': accepted_nominal(r_baseline_inc, INC),
        'negative_classification_disagreement_rejected': rejected_invalid(r_control_class),
        'negative_state_identity_disagreement_rejected': rejected_invalid(r_control_state),
        'negative_projection_disagreement_rejected': rejected_invalid(r_control_projection),
    }

    oracle_checks = {
        'candidate_A_independently_invalid': 'classification_unresolved_binding' in cand_a_oracle,
        'candidate_B_independently_invalid': cand_b_oracle == ['projection_key_set'],
        'candidate_C_independently_invalid': cand_c_oracle == ['provenance_key_set'],
    }

    candidate_acceptance = {
        'A_pass_with_unresolved_accepted_as_pass': accepted_nominal(r_candidate_a, PASS),
        'B_noncanonical_projection_keyset_accepted_as_pass': accepted_nominal(r_candidate_b, PASS),
        'C_noncanonical_provenance_keyset_accepted_as_pass': accepted_nominal(r_candidate_c, PASS),
    }

    if harness_errors or not all(controls.values()) or not all(oracle_checks.values()):
        classification = GATE_INVALID
    elif all(candidate_acceptance.values()):
        classification = GATE_PASS
    else:
        classification = GATE_FAIL

    source_blob_runtime = subprocess.run(
        ['git', 'hash-object', str(SOURCE_AGGREGATE)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    ).stdout.strip()
    if source_blob_runtime != SOURCE_AGGREGATE_BLOB:
        harness_errors.append('source_aggregate_blob_mismatch_runtime')
        classification = GATE_INVALID

    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'source_run': SOURCE_RUN,
        'source_launch_head': SOURCE_HEAD,
        'source_aggregate_blob_expected': SOURCE_AGGREGATE_BLOB,
        'source_aggregate_blob_runtime': source_blob_runtime,
        'classification': classification,
        'harness_errors': harness_errors,
        'controls': controls,
        'oracle_checks': oracle_checks,
        'candidate_oracle_errors': {
            'A': cand_a_oracle,
            'B': cand_b_oracle,
            'C': cand_c_oracle,
        },
        'candidate_acceptance': candidate_acceptance,
        'scenario_results': [
            r_baseline_pass,
            r_baseline_inc,
            r_control_class,
            r_control_state,
            r_control_projection,
            r_candidate_a,
            r_candidate_b,
            r_candidate_c,
        ],
        'production_science_consumed': False,
        'source_run_classified': False,
        'claim_ceiling': 'Phase-B source aggregate verifier/authority-path binding only; no scientific classification of source run 35405065903',
    }
    payload = dict(out)
    out['decision_sha256'] = sha_json(payload)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if classification in (GATE_PASS, GATE_FAIL) else 2


if __name__ == '__main__':
    raise SystemExit(main())
