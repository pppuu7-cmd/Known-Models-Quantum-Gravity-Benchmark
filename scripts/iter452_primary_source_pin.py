#!/usr/bin/env python3
import argparse, hashlib, json, sys
from pathlib import Path

SOURCE = Path('sources/arxiv_2601_23162v1_causal_vertex.json')
SOURCE_ID = 'arXiv:2601.23162v1'
LANES = {
    'toller_feynman_eq3',
    'causal_vertex_eq4',
    'boundary_domains',
    'eprl_controls_eq5_eq6',
    'cartan_magnetic_eq7',
}

def load_source():
    raw = SOURCE.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()

def audit_lane(name):
    s, digest = load_source()
    checks = {'source_identity': s.get('source_id') == SOURCE_ID}
    if name == 'toller_feynman_eq3':
        x = s.get('eq3_toller_feynman', {})
        checks.update({
            'equation_3': x.get('equation') == 3,
            'feynman_definition': x.get('definition_type') == 'Feynman_i_epsilon_spectral_integral',
            'full_real_spectral_domain': x.get('tilde_rho_domain') == '(-infinity,+infinity)',
            'branch_kernel': 'epsilon->0+' in x.get('branch_kernel','') and 'tilde_rho-rho' in x.get('branch_kernel',''),
            'gamma_factor': all(k in x.get('gamma_ratio','') for k in ['Gamma(-j-i*rho)', 'Gamma(l-i*tilde_rho+1)', 'Gamma(-j-i*tilde_rho)', 'Gamma(l-i*rho+1)']),
            'wigner_integrand': x.get('integrand_representation','').startswith('D^(tilde_rho,k)'),
        })
    elif name == 'causal_vertex_eq4':
        x = s.get('eq4_causal_vertex', {})
        checks.update({
            'equation_4': x.get('equation') == 4,
            'four_group_integrations': x.get('group_integrations') == ['g_2','g_3','g_4','g_5'],
            'gauge_fix': x.get('gauge_fix') == 'g_1=identity',
            'ten_wedges': x.get('wedge_domain') == '1<=a<b<=5' and x.get('wedge_count') == 10,
            'gamma_simple': x.get('gamma_simple') == '(rho,k)=(gamma*j_ab,j_ab)',
            'ordered_group_argument': 'g_b^{-1} g_a' in x.get('wedge_factor',''),
            'magnetic_indices': 'm_ba' in x.get('wedge_factor','') and 'm_ab' in x.get('wedge_factor',''),
        })
    elif name == 'boundary_domains':
        x = s.get('boundary_state', {})
        checks.update({
            'ten_spins': x.get('spin_count') == 10,
            'five_intertwiners': x.get('intertwiner_count') == 5,
            'magnetic_numbers': x.get('magnetic_labels') == 'm_ab',
            'basis_sum': 'sum_{m_ab}' in x.get('basis',''),
            'contraction_relation': 'Eq.(4)' in x.get('contraction_relation','') and 'intertwiner' in x.get('contraction_relation',''),
        })
    elif name == 'eprl_controls_eq5_eq6':
        a = s.get('eq5_additive_control', {})
        b = s.get('eq6_eprl_control', {})
        guards = s.get('scope_guards', {})
        checks.update({
            'equation_5': a.get('equation') == 5,
            'additive_identity': 'T^(+,rho,k)' in a.get('identity','') and 'T^(-,rho,k)' in a.get('identity','') and '=D^(rho,k)' in a.get('identity',''),
            'equation_6': b.get('equation') == 6,
            'unconstrained_wedge_sum': 'unconstrained' in b.get('sum_scope','') and 'kappa_ab=+/-1' in b.get('sum_scope',''),
            'toller_vertex_control': 'T^(kappa_ab' in b.get('fixed_wedge_factor',''),
            'no_modified_i_epsilon': guards.get('no_modified_i_epsilon') is True,
        })
    elif name == 'cartan_magnetic_eq7':
        x = s.get('eq7_cartan_magnetic', {})
        checks.update({
            'equation_7': x.get('equation') == 7,
            'cartan_su2': 'U_1,U_2 in SU(2)' in x.get('cartan',''),
            'two_wigner_factors': x.get('decomposition','').count('D^(') == 2,
            'reduced_toller': 't^(+/-;rho,k)' in x.get('decomposition',''),
            'finite_p_domain': x.get('finite_sum') is True and x.get('p_domain') == 'p=-min(j,l),...,min(j,l)',
        })
    else:
        raise ValueError(name)
    qualified = all(checks.values())
    return {
        'iteration': 452,
        'lane': name,
        'source_id': s.get('source_id'),
        'source_sha256': digest,
        'checks': checks,
        'qualified': qualified,
        'scope_guard': 'Source pinning only; not D7-S2 closure or a finiteness result.'
    }

def aggregate(paths):
    rows = [json.loads(Path(p).read_text()) for p in paths]
    expected = LANES
    names = {r.get('lane') for r in rows}
    structurally_valid = len(rows) == 5 and names == expected
    same_source = {r.get('source_id') for r in rows} == {SOURCE_ID}
    digests = {r.get('source_sha256') for r in rows}
    same_digest = len(digests) == 1
    all_qualified = structurally_valid and same_source and same_digest and all(r.get('qualified') is True for r in rows)
    classification = ('PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_PINNED_COMPLETE'
                      if all_qualified else
                      'BLOCKED_PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_STILL_INCOMPLETE')
    return {
        'iteration': 452,
        'classification': classification,
        'structurally_valid': structurally_valid,
        'same_source_id': same_source,
        'same_source_digest': same_digest,
        'source_id': SOURCE_ID,
        'source_sha256': next(iter(digests)) if same_digest and digests else None,
        'qualified_lanes': sum(r.get('qualified') is True for r in rows),
        'lane_count': len(rows),
        'lanes': sorted(rows, key=lambda r:r['lane']),
        'scope_guard': 'PASS is source-object qualification only; no convergence/finiteness/D7 terminal claim.'
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', choices=sorted(LANES))
    ap.add_argument('--aggregate', nargs='*')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    if bool(a.lane) == bool(a.aggregate is not None):
        raise SystemExit('choose exactly one of --lane or --aggregate')
    result = audit_lane(a.lane) if a.lane else aggregate(a.aggregate)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))
    if a.lane and not result['qualified']:
        sys.exit(2)

if __name__ == '__main__':
    main()
