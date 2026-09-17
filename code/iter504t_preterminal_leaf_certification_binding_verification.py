#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, subprocess, sys, tempfile
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504T_PRETERMINAL_LEAF_CERTIFICATION_BINDING_VERIFICATION_GATE'
VERIFY = 'ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED'
REFUTE = 'ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_REFUTED_SCOPED'
BLOCKED = 'ITER504T_LEAF_CERTIFICATION_BINDING_VERIFICATION_BLOCKED_SCOPED'
INVALID = 'INVALID_IMPLEMENTATION'
ROOTS = (13, 14, 15)
RGRID = (6, 8, 10, 12)
RHOS = (0.35, 0.9, 1.6, 2.7)
SCI_PASS = 'ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED'
EXPECTED_BLOBS = {
    'research/prereg/ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION_2026-09-17.md': 'f648b0e0d6a960bf60c32d5c34694497a50b7e68',
    'code/iter504t_local_derivative_assemble.py': '62486912d9b930c12e8cddbb94999895fe8488df',
    'code/iter504t_local_derivative_critic.py': '779697e3c507d18be8ac9f377dfe0b5212ecc393',
    'code/iter504t_local_derivative_aggregate.py': 'd19edf62ae10edbaa5d9eecb76ca8004595120fb',
    'recovery/CRITICAL_PRETERMINAL_AUDIT_ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_2026-09-17.md': '49f62f5aea12e1a2637d8ffdc199910c46023d0a',
}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot import {path}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def qstr(q: Fraction) -> str:
    return f'{q.numerator}/{q.denominator}'


def inclusion_record(k: int, a: Fraction, b: Fraction) -> dict:
    lo = Fraction(16 + k, 12800)
    hi = Fraction(17 + k, 12800)
    rows = []
    for R in RGRID:
        for rho in RHOS:
            rows.append({'R': R, 'rho': rho, 'componentwise_inclusion': [True] * 243})
    return {
        'depth': 1,
        'amp_lower_q': qstr(a),
        'amp_upper_q': qstr(b),
        'parent_depth': 0,
        'parent_amp_lower_q': qstr(lo),
        'parent_amp_upper_q': qstr(hi),
        'haar_log_inclusion_by_R': {str(R): True for R in RGRID},
        'channel_inclusion_rows': rows,
        'all_componentwise_parent_inclusion': True,
    }


def leaf(k: int, a: Fraction, b: Fraction) -> dict:
    prs = [
        {'rho': rho, 'slope_floor_satisfied': True, 'drift_within_tolerance': True, 'certified': True}
        for rho in RHOS
    ]
    pm = [{'R': R, 'rho': rho, 'indices': [0]} for R in RGRID for rho in RHOS]
    return {
        'depth': 1,
        'amp_lower_q': qstr(a),
        'amp_upper_q': qstr(b),
        'scientific_decision_transport': 'exact_arb_booleans_float_bounds_display_only',
        'validated_local_derivative': True,
        'certified': True,
        'per_rho': prs,
        'possible_max': pm,
    }


def root_fixture(k: int) -> dict:
    lo = Fraction(16 + k, 12800)
    hi = Fraction(17 + k, 12800)
    mid = (lo + hi) / 2
    leaves = [leaf(k, lo, mid), leaf(k, mid, hi)]
    recs = [inclusion_record(k, lo, mid), inclusion_record(k, mid, hi)]
    return {
        'gate': 'ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION',
        'preregistration_commit': 'aa2b0256ce60d605574a18ec86c0bad5b5df1512',
        'repair_preregistration_commit': 'adc7bfb9df77a90455cac1b0f0cb7255d80c44d5',
        'parent_terminal_commit': '1b0004064575f046210383dc7b1ee22d4f25e66b',
        'root_box': k,
        'precision_bits': 384,
        'python_flint': '0.9.0',
        'full_channel_count': 243,
        'channel_pruning_used': False,
        'max_depth': 3,
        'partition_rule': 'deterministic_dyadic_midpoint',
        'local_derivative_recomputed_each_visited_node': True,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'r_cohort_consumed': list(RGRID),
        'rho_cohort_consumed': list(RHOS),
        'componentwise_parent_inclusion_record_count': 2,
        'componentwise_parent_inclusion_records': recs,
        'cover_valid': True,
        'visited_node_count': 3,
        'terminal_leaf_count': 2,
        'unresolved_leaf_count': 0,
        'leaves': leaves,
    }


def fixtures() -> dict[int, dict]:
    return {k: root_fixture(k) for k in ROOTS}


def write_roots(base: Path, roots: dict[int, dict], prefix: str) -> dict[int, Path]:
    out = {}
    for k in ROOTS:
        p = base / f'{prefix}_root{k}.json'
        p.write_text(json.dumps(roots[k], indent=2, sort_keys=True) + '\n')
        out[k] = p
    return out


def run_cmd(args: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(args, text=True, capture_output=True)
    return p.returncode, p.stdout, p.stderr


def exact_path_replay(repo: Path, roots_a: dict[int, dict], roots_b: dict[int, dict], work: Path, tag: str) -> dict:
    asm = repo / 'code/iter504t_local_derivative_assemble.py'
    agg = repo / 'code/iter504t_local_derivative_aggregate.py'
    critic = repo / 'code/iter504t_local_derivative_critic.py'
    pa = write_roots(work, roots_a, tag + '_a')
    pb = write_roots(work, roots_b, tag + '_b')
    aa = work / f'{tag}_a_assembled.json'
    bb = work / f'{tag}_b_assembled.json'
    ag = work / f'{tag}_aggregate.json'
    cr = work / f'{tag}_critic.json'
    base = [sys.executable, str(asm)]
    rc_a, so_a, se_a = run_cmd(base + [f'--root{k}={pa[k]}' for k in ROOTS] + [f'--out={aa}'])
    rc_b, so_b, se_b = run_cmd(base + [f'--root{k}={pb[k]}' for k in ROOTS] + [f'--out={bb}'])
    agg_rc, agg_so, agg_se = run_cmd([sys.executable, str(agg), f'--a={aa}', f'--b={bb}', f'--out={ag}']) if aa.exists() and bb.exists() else (99, '', 'missing assemblies')
    critic_args = [sys.executable, str(critic)]
    for lane, ps in (('a', pa), ('b', pb)):
        critic_args += [f'--{lane}-root{k}={ps[k]}' for k in ROOTS]
        critic_args += [f'--{lane}-assembled={aa if lane == "a" else bb}']
    critic_args += [f'--aggregate={ag}', f'--out={cr}']
    cr_rc, cr_so, cr_se = run_cmd(critic_args) if ag.exists() else (99, '', 'missing aggregate')
    def read(p: Path):
        return json.loads(p.read_text()) if p.exists() else None
    return {
        'assembler_a_returncode': rc_a,
        'assembler_b_returncode': rc_b,
        'aggregate_returncode': agg_rc,
        'critic_returncode': cr_rc,
        'assembler_a': read(aa),
        'assembler_b': read(bb),
        'aggregate': read(ag),
        'critic': read(cr),
        'stderr': {'a': se_a[-1000:], 'b': se_b[-1000:], 'aggregate': agg_se[-1000:], 'critic': cr_se[-1000:]},
    }


def replay_passed(replay: dict) -> bool:
    objs = [replay.get('assembler_a'), replay.get('assembler_b'), replay.get('aggregate'), replay.get('critic')]
    return (
        all(replay.get(k) == 0 for k in ('assembler_a_returncode', 'assembler_b_returncode', 'aggregate_returncode', 'critic_returncode'))
        and all(isinstance(o, dict) for o in objs)
        and replay['assembler_a'].get('classification') == SCI_PASS
        and replay['assembler_b'].get('classification') == SCI_PASS
        and replay['aggregate'].get('classification') == SCI_PASS
        and replay['critic'].get('classification') == SCI_PASS
        and replay['critic'].get('critic_errors') == []
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--authority', required=True)
    ap.add_argument('--repo-root', default='.')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    repo = Path(a.repo_root).resolve()
    authority = json.loads(Path(a.authority).read_text())

    identities = {}
    identity_ok = True
    for path, expected in EXPECTED_BLOBS.items():
        actual = subprocess.check_output(['git', 'hash-object', path], cwd=repo, text=True).strip()
        identities[path] = {'expected_blob_sha': expected, 'actual_blob_sha': actual, 'match': actual == expected}
        identity_ok &= actual == expected
    authority_ok = (
        authority.get('gate') == GATE
        and authority.get('repair_launch_head') == '10ae6bcc8447d14cecc6e550065504b23f792953'
        and authority.get('active_run_artifacts_forbidden') is True
    )
    prereg_text = (repo / 'research/prereg/ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION_2026-09-17.md').read_text()
    predicate_text_ok = all(s in prereg_text for s in (
        'rho_certified := slope_floor_satisfied AND drift_within_tolerance',
        'A node is certified iff all four rhos are certified.',
        'every terminal leaf is scientifically certified',
    ))

    assembler = load_module(repo / 'code/iter504t_local_derivative_assemble.py', 'iter504t_asm_binding_gate')
    critic = load_module(repo / 'code/iter504t_local_derivative_critic.py', 'iter504t_critic_binding_gate')
    base = fixtures()
    direct_positive_asm = all(assembler.validate(copy.deepcopy(base[k]), k) == [] for k in ROOTS)
    direct_positive_critic = all(critic.validate(copy.deepcopy(base[k]), k) == [] for k in ROOTS)

    with tempfile.TemporaryDirectory() as td:
        work = Path(td)
        positive = exact_path_replay(repo, copy.deepcopy(base), copy.deepcopy(base), work, 'positive')

        target_a = copy.deepcopy(base)
        target_b = copy.deepcopy(base)
        for roots in (target_a, target_b):
            r = roots[13]['leaves'][0]['per_rho'][0]
            r['slope_floor_satisfied'] = False
            r['drift_within_tolerance'] = True
            r['certified'] = False
            roots[13]['leaves'][0]['certified'] = True
            roots[13]['unresolved_leaf_count'] = 0
        target = exact_path_replay(repo, target_a, target_b, work, 'target_c4')

        bad_rho = copy.deepcopy(base)
        bad_rho[13]['leaves'][0]['per_rho'][0]['certified'] = False
        bad_rho_asm_errors = assembler.validate(bad_rho[13], 13)
        bad_rho_critic_errors = critic.validate(bad_rho[13], 13)

        bad_R = copy.deepcopy(base)
        bad_R[13]['leaves'][0]['possible_max'][0]['R'] = 7
        bad_R_asm_errors = assembler.validate(bad_R[13], 13)
        bad_R_critic_errors = critic.validate(bad_R[13], 13)

    positive_path_ok = replay_passed(positive)
    target_accepted = replay_passed(target)
    per_rho_control_ok = bool(bad_rho_asm_errors) and bool(bad_rho_critic_errors)
    r_control_ok = bool(bad_R_asm_errors) and bool(bad_R_critic_errors)

    controls = {
        'source_blob_identity': identity_ok,
        'authority_identity': authority_ok,
        'original_predicate_text_identity': predicate_text_ok,
        'direct_positive_assembler': direct_positive_asm,
        'direct_positive_critic': direct_positive_critic,
        'positive_full_path': positive_path_ok,
        'per_rho_boolean_relation_rejected_when_broken': per_rho_control_ok,
        'R_6_to_7_rejected': r_control_ok,
        'active_scientific_artifacts_consumed': False,
    }

    if not identity_ok or not authority_ok or not predicate_text_ok:
        classification = INVALID
    elif not all(v for k, v in controls.items() if k != 'active_scientific_artifacts_consumed'):
        classification = INVALID
    elif target_accepted:
        classification = VERIFY
    else:
        target_has_binding_error = any(
            replay.get('classification') == INVALID or replay.get('returncode', 0) not in (0, None)
            for replay in []
        )
        # A clean rejection anywhere in the exact path refutes C4; unexplained execution failure is BLOCKED.
        target_exec_ok = all(target.get(k) in (0, 2) for k in ('assembler_a_returncode','assembler_b_returncode','aggregate_returncode','critic_returncode'))
        classification = REFUTE if target_exec_ok else BLOCKED

    projection = {
        'gate': GATE,
        'classification': classification,
        'controls': controls,
        'authority_files': identities,
        'target_c4_exact_path_accepted': target_accepted,
        'target_c4': {
            'assembler_a_returncode': target['assembler_a_returncode'],
            'assembler_b_returncode': target['assembler_b_returncode'],
            'aggregate_returncode': target['aggregate_returncode'],
            'critic_returncode': target['critic_returncode'],
            'assembler_a_classification': target['assembler_a'].get('classification') if target['assembler_a'] else None,
            'assembler_b_classification': target['assembler_b'].get('classification') if target['assembler_b'] else None,
            'aggregate_classification': target['aggregate'].get('classification') if target['aggregate'] else None,
            'critic_classification': target['critic'].get('classification') if target['critic'] else None,
            'critic_errors': target['critic'].get('critic_errors') if target['critic'] else None,
            'cross_environment_exact_decision_agreement': target['aggregate'].get('cross_environment_exact_decision_agreement') if target['aggregate'] else None,
        },
        'positive_full_path_classifications': {
            'assembler_a': positive['assembler_a'].get('classification') if positive['assembler_a'] else None,
            'assembler_b': positive['assembler_b'].get('classification') if positive['assembler_b'] else None,
            'aggregate': positive['aggregate'].get('classification') if positive['aggregate'] else None,
            'critic': positive['critic'].get('classification') if positive['critic'] else None,
        },
        'per_rho_control_errors': {'assembler': bad_rho_asm_errors, 'critic': bad_rho_critic_errors},
        'r_cohort_control_errors': {'assembler': bad_R_asm_errors, 'critic': bad_R_critic_errors},
        'new_fact': 'Exact launch-head downstream path accepts a dual-lane synthetic payload with one internally consistent uncertified rho but top-level leaf.certified=true and unresolved count zero.' if target_accepted else 'Target malformed leaf is rejected by the exact launch-head path.',
        'claim_ceiling': authority.get('interpretation_ceiling'),
        'active_scientific_run_classified': False,
    }
    canonical = json.dumps(projection, sort_keys=True, separators=(',', ':'))
    projection['decision_sha256'] = hashlib.sha256(canonical.encode()).hexdigest()
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(projection, indent=2, sort_keys=True) + '\n')
    print(json.dumps(projection, sort_keys=True))
    return 0 if classification in (VERIFY, REFUTE, BLOCKED) else 2


if __name__ == '__main__':
    raise SystemExit(main())
