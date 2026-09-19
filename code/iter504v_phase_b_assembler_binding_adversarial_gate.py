#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_ADVERSARIAL_GATE'
PREREG_COMMIT = '93670f89688d9ad673fe35274892701a43f818d9'
SOURCE_RUN = 35405065903
SOURCE_LAUNCH_HEAD = '31fcdacffcc394e96b73917083281edb90d6753c'
SOURCE_ASSEMBLER_BLOB = 'f93bea2c32ed383a054beebb4d4b1c64fcbbd2c1'
CANONICAL_SHA256 = '3cac282175830e795394dca5202f5368b27120817f2d4abd9eba54fc6c9f1e6f'
PASS_SOURCE = 'ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED'
INVALID_SOURCE = 'ITER504V_BROADER_DOMAIN_INVALID'
VERIFIED = 'ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECTS_VERIFIED_SCOPED'
PARTIAL = 'ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECT_PARTIAL_SCOPED'
REFUTED = 'ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_CANDIDATES_REFUTED_SCOPED'
BLOCKED = 'ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_BLOCKED_SCOPED'
INVALID = 'INVALID_IMPLEMENTATION'
RGRID = (6, 8, 10, 12)
RHOS = (0.35, 0.9, 1.6, 2.7)
QUARTILES = ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15))
SPECIAL_SID = '0to5|b0|p0|x00'


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_sha(obj) -> str:
    return sha256_bytes(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode())


def load_assembler():
    path = Path('code/iter504v_phase_b_assemble.py')
    spec = importlib.util.spec_from_file_location('phase_b_source_assembler', path)
    if spec is None or spec.loader is None:
        raise RuntimeError('cannot load exact source assembler')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def qt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'


def make_leaf(a: Fraction, b: Fraction, depth: int):
    return {
        'depth': depth,
        'amp_lower_q': qt(a),
        'amp_upper_q': qt(b),
        'local_mid_q': qt((a + b) / 2),
        'validated_local_derivative': True,
        'local_derivative_recomputed_here': True,
        'leaf_certification_binding': 'all_per_rho_exact',
        'scientific_decision_transport': 'exact_arb_booleans_float_bounds_display_only',
        'certified': True,
        'per_rho': [
            {
                'rho': rho,
                'slope_floor_satisfied': True,
                'drift_within_tolerance': True,
                'certified': True,
            }
            for rho in RHOS
        ],
        'possible_max': [
            {'R': R, 'rho': rho, 'indices': []}
            for R in RGRID
            for rho in RHOS
        ],
    }


def make_inclusion(child_a: Fraction, child_b: Fraction, child_depth: int,
                   parent_a: Fraction, parent_b: Fraction, parent_depth: int):
    return {
        'depth': child_depth,
        'amp_lower_q': qt(child_a),
        'amp_upper_q': qt(child_b),
        'parent_depth': parent_depth,
        'parent_amp_lower_q': qt(parent_a),
        'parent_amp_upper_q': qt(parent_b),
        'haar_log_inclusion_by_R': {str(R): True for R in RGRID},
        'channel_inclusion_rows': [
            {'R': R, 'rho': rho, 'componentwise_inclusion': [True] * 243}
            for R in RGRID
            for rho in RHOS
        ],
        'all_componentwise_parent_inclusion': True,
    }


def make_case(asm, sid: str, expected, split: bool = False):
    causal, block, path, box, direction, sign = expected[sid]
    lo, hi = asm.box_interval(box)
    if split:
        mid = (lo + hi) / 2
        leaves = [make_leaf(lo, mid, 1), make_leaf(mid, hi, 1)]
        incs = [
            make_inclusion(lo, mid, 1, lo, hi, 0),
            make_inclusion(mid, hi, 1, lo, hi, 0),
        ]
        visited = 3
    else:
        leaves = [make_leaf(lo, hi, 0)]
        incs = []
        visited = 1
    return {
        'gate': asm.GATE,
        'preregistration_commit': asm.PREREG,
        'design_authority_commit': asm.DESIGN_AUTHORITY,
        'design_static_critic_commit': asm.DESIGN_STATIC_CRITIC,
        'implementation_authority_commit': asm.IMPLEMENTATION_AUTHORITY,
        'terminal_parent_commit': asm.TERMINAL_PARENT,
        'campaign_design_commit': asm.CAMPAIGN_DESIGN,
        'campaign_manifest_blob': asm.MANIFEST_BLOB,
        'canonical_768_record_sequence_sha256': asm.CANONICAL_SHA256,
        'case_id': sid,
        'state_id': sid,
        'causal': causal,
        'block': block,
        'path': path,
        'box': box,
        'direction': direction,
        'sign': sign,
        'parent_amp_lower_q': qt(lo),
        'parent_amp_upper_q': qt(hi),
        'precision_bits': 384,
        'python_flint': '0.9.0',
        'full_channel_count': 243,
        'channel_pruning_used': False,
        'max_depth': 3,
        'partition_rule': 'deterministic_dyadic_midpoint',
        'local_derivative_recomputed_each_visited_node': True,
        'leaf_certification_binding': 'all_per_rho_exact',
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'r_cohort_consumed': list(RGRID),
        'rho_cohort_consumed': list(RHOS),
        'componentwise_parent_inclusion_record_count': len(incs),
        'componentwise_parent_inclusion_records': incs,
        'cover_valid': True,
        'visited_node_count': visited,
        'terminal_leaf_count': len(leaves),
        'unresolved_leaf_count': 0,
        'leaves': leaves,
        'claim_ceiling': 'Synthetic structural control only; no physical interpretation',
    }


def artifact_name(causal: str, block: int, path: int, quartile: int) -> str:
    return f'iter504v-phaseb-3.11-{causal}-b{block}-p{path}-q{quartile}'


def build_complete_inventory(root: Path, asm):
    ids, expected = asm.expected_map()
    if len(ids) != 768 or asm.sequence_sha(ids) != CANONICAL_SHA256:
        raise RuntimeError('canonical identity mismatch in gate fixture')
    for causal in asm.CAUSALS:
        for block in asm.BLOCKS:
            for path in asm.PATHS:
                for quartile, boxes in enumerate(QUARTILES):
                    d = root / artifact_name(causal, block, path, quartile) / 'cases'
                    d.mkdir(parents=True, exist_ok=True)
                    state_ids = []
                    for box in boxes:
                        sid = f'{causal}|b{block}|p{path}|x{box:02d}'
                        state_ids.append(sid)
                        obj = make_case(asm, sid, expected, split=(sid == SPECIAL_SID))
                        (d / f'case-{box:02d}.json').write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')
                    shard = {
                        'gate': asm.GATE,
                        'python_environment_external': True,
                        'execution_topology': 'four_independent_box_processes_within_frozen_quartile_shard',
                        'causal': causal,
                        'block': block,
                        'path': path,
                        'quartile': quartile,
                        'boxes': list(boxes),
                        'state_ids': state_ids,
                        'record_count': 4,
                        'invalid_count': 0,
                        'invalid_state_ids': [],
                        'canonical_768_record_sequence_sha256': CANONICAL_SHA256,
                    }
                    (d / 'shard.json').write_text(json.dumps(shard, indent=2, sort_keys=True) + '\n')
    return ids


def run_exact_assembler(root: Path, label: str):
    out = root.parent / f'{label}.json'
    cp = subprocess.run(
        [sys.executable, 'code/iter504v_phase_b_assemble.py', '--cases-root', str(root), '--out', str(out)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if not out.exists():
        return {
            'returncode': cp.returncode,
            'stdout_sha256': sha256_bytes(cp.stdout.encode()),
            'stderr_sha256': sha256_bytes(cp.stderr.encode()),
            'output_missing': True,
        }
    obj = json.loads(out.read_text())
    return {
        'returncode': cp.returncode,
        'classification': obj.get('classification'),
        'errors': obj.get('errors'),
        'total_cases': obj.get('total_cases'),
        'total_unresolved_leaves': obj.get('total_unresolved_leaves'),
        'counterexample_state_ids': obj.get('counterexample_state_ids'),
        'decision_projection_sequence_sha256': obj.get('decision_projection_sequence_sha256'),
        'assembly_payload_sha256': obj.get('assembly_payload_sha256'),
        'stdout_sha256': sha256_bytes(cp.stdout.encode()),
        'stderr_sha256': sha256_bytes(cp.stderr.encode()),
        'output_missing': False,
    }


def parent_oracle(case_obj):
    errors = []
    for i, rec in enumerate(case_obj.get('componentwise_parent_inclusion_records', [])):
        try:
            cd = int(rec['depth'])
            pd = int(rec['parent_depth'])
            ca = Fraction(rec['amp_lower_q'])
            cb = Fraction(rec['amp_upper_q'])
            pa = Fraction(rec['parent_amp_lower_q'])
            pb = Fraction(rec['parent_amp_upper_q'])
            if cd != pd + 1:
                errors.append(f'{i}:depth')
            if not (pa <= ca < cb <= pb):
                errors.append(f'{i}:containment')
            if cb - ca != (pb - pa) / 2:
                errors.append(f'{i}:half_width')
            mid = (pa + pb) / 2
            if not ((ca == pa and cb == mid) or (ca == mid and cb == pb)):
                errors.append(f'{i}:exact_half')
        except Exception as e:
            errors.append(f'{i}:parse:{type(e).__name__}')
    return errors


def shard_oracle(root: Path):
    errors = []
    seen = set()
    shard_count = 0
    for shard_path in sorted(root.rglob('shard.json')):
        shard_count += 1
        shard = json.loads(shard_path.read_text())
        d = shard_path.parent
        physical = []
        for p in sorted(d.glob('case-*.json')):
            physical.append(json.loads(p.read_text()).get('state_id'))
        declared = list(shard.get('state_ids', []))
        causal = shard.get('causal')
        block = int(shard.get('block'))
        path = int(shard.get('path'))
        quartile = int(shard.get('quartile'))
        boxes = list(QUARTILES[quartile]) if 0 <= quartile < 4 else []
        expected = [f'{causal}|b{block}|p{path}|x{x:02d}' for x in boxes]
        identity = (causal, block, path, quartile)
        if identity in seen:
            errors.append(f'duplicate_shard:{identity}')
        seen.add(identity)
        if declared != expected:
            errors.append(f'declaration:{identity}')
        if sorted(physical) != sorted(expected):
            errors.append(f'physical:{identity}')
        if int(shard.get('record_count', -1)) != 4:
            errors.append(f'record_count:{identity}')
    if shard_count != 192:
        errors.append(f'shard_count:{shard_count}')
    if len(seen) != 192:
        errors.append(f'unique_shards:{len(seen)}')
    return errors


def read_case(root: Path, sid: str):
    causal, b, p, x = sid.split('|')
    block = int(b[1:])
    path = int(p[1:])
    box = int(x[1:])
    q = box // 4
    return root / artifact_name(causal, block, path, q) / 'cases' / f'case-{box:02d}.json'


def result_classification(controls, a_survives, b_survives):
    if not all(controls.values()):
        return INVALID
    if a_survives and b_survives:
        return VERIFIED
    if a_survives or b_survives:
        return PARTIAL
    return REFUTED


def main():
    asm = load_assembler()
    controls = {}
    diagnostics = {}
    try:
        with tempfile.TemporaryDirectory(prefix='iter504v-binding-gate-') as td:
            t = Path(td)
            baseline = t / 'baseline'
            ids = build_complete_inventory(baseline, asm)
            baseline_oracle_parent = parent_oracle(json.loads(read_case(baseline, SPECIAL_SID).read_text()))
            baseline_oracle_shard = shard_oracle(baseline)
            base_run = run_exact_assembler(baseline, 'baseline')
            controls['baseline_exact_assembler_pass'] = (
                base_run.get('returncode') == 0
                and base_run.get('classification') == PASS_SOURCE
                and base_run.get('errors') == []
                and base_run.get('total_cases') == 768
                and base_run.get('total_unresolved_leaves') == 0
            )
            controls['baseline_parent_oracle_clean'] = baseline_oracle_parent == []
            controls['baseline_shard_oracle_clean'] = baseline_oracle_shard == []

            mut_a = t / 'mut_a'
            shutil.copytree(baseline, mut_a)
            a_path = read_case(mut_a, SPECIAL_SID)
            a_obj = json.loads(a_path.read_text())
            a_obj['componentwise_parent_inclusion_records'][0]['parent_depth'] = 1
            a_path.write_text(json.dumps(a_obj, indent=2, sort_keys=True) + '\n')
            a_oracle = parent_oracle(a_obj)
            a_run = run_exact_assembler(mut_a, 'mut_a')
            controls['candidate_a_oracle_detects'] = bool(a_oracle)
            a_survives = (
                a_run.get('returncode') == 0
                and a_run.get('classification') == PASS_SOURCE
                and a_run.get('errors') == []
            )

            mut_b = t / 'mut_b'
            shutil.copytree(baseline, mut_b)
            p0 = read_case(mut_b, '0to5|b0|p0|x00')
            p4 = read_case(mut_b, '0to5|b0|p0|x04')
            b0 = p0.read_bytes()
            b4 = p4.read_bytes()
            p0.write_bytes(b4)
            p4.write_bytes(b0)
            b_oracle = shard_oracle(mut_b)
            b_run = run_exact_assembler(mut_b, 'mut_b')
            controls['candidate_b_oracle_detects'] = bool(b_oracle)
            b_survives = (
                b_run.get('returncode') == 0
                and b_run.get('classification') == PASS_SOURCE
                and b_run.get('errors') == []
                and b_run.get('decision_projection_sequence_sha256') == base_run.get('decision_projection_sequence_sha256')
            )

            sens_dup = t / 'sens_dup'
            shutil.copytree(baseline, sens_dup)
            dup_path = read_case(sens_dup, '0to5|b0|p0|x01')
            dup_obj = json.loads(dup_path.read_text())
            dup_obj['state_id'] = '0to5|b0|p0|x00'
            dup_path.write_text(json.dumps(dup_obj, indent=2, sort_keys=True) + '\n')
            dup_run = run_exact_assembler(sens_dup, 'sens_dup')
            controls['duplicate_state_sensitivity'] = (
                dup_run.get('returncode') == 2
                and dup_run.get('classification') == INVALID_SOURCE
                and isinstance(dup_run.get('errors'), list)
                and 'duplicate_states' in dup_run.get('errors', [])
            )

            sens_leaf = t / 'sens_leaf'
            shutil.copytree(baseline, sens_leaf)
            leaf_path = read_case(sens_leaf, '0to5|b0|p0|x02')
            leaf_obj = json.loads(leaf_path.read_text())
            leaf_obj['leaves'][0]['certified'] = False
            leaf_obj['unresolved_leaf_count'] = 1
            leaf_path.write_text(json.dumps(leaf_obj, indent=2, sort_keys=True) + '\n')
            leaf_run = run_exact_assembler(sens_leaf, 'sens_leaf')
            controls['leaf_binding_sensitivity'] = (
                leaf_run.get('returncode') == 2
                and leaf_run.get('classification') == INVALID_SOURCE
                and any('leaf_per_rho_binding' in e for e in leaf_run.get('errors', []))
            )

            diagnostics = {
                'canonical_record_count': len(ids),
                'baseline': base_run,
                'candidate_a': {
                    'oracle_errors': a_oracle,
                    'assembler': a_run,
                    'survives_exact_assembler': a_survives,
                },
                'candidate_b': {
                    'oracle_error_count': len(b_oracle),
                    'oracle_errors_sha256': canonical_json_sha(b_oracle),
                    'assembler': b_run,
                    'survives_exact_assembler': b_survives,
                    'projection_unchanged_vs_baseline': b_run.get('decision_projection_sequence_sha256') == base_run.get('decision_projection_sequence_sha256'),
                },
                'sensitivity_duplicate': dup_run,
                'sensitivity_leaf_binding': leaf_run,
            }
            classification = result_classification(controls, a_survives, b_survives)
    except Exception as e:
        classification = BLOCKED
        diagnostics = {'exception_type': type(e).__name__, 'exception_repr': repr(e)}

    out = {
        'gate': GATE,
        'preregistration_commit': PREREG_COMMIT,
        'source_run_id': SOURCE_RUN,
        'source_launch_head': SOURCE_LAUNCH_HEAD,
        'source_assembler_blob': SOURCE_ASSEMBLER_BLOB,
        'production_science_consumed': False,
        'source_run_classified': False,
        'classification': classification,
        'controls': controls,
        'diagnostics': diagnostics,
        'claim_ceiling': 'Exact Phase-B source-assembler verifier binding only; no source-run science classification or broader closure',
    }
    decision = dict(out)
    out['decision_sha256'] = canonical_json_sha(decision)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
