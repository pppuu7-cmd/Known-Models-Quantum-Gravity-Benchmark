#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import lqg_iter330_explicit_k5_jet_basis as i330


def filter_t(rows, allowed):
    out = []
    for row in rows:
        out.append({k: v for k, v in row.items() if k[0] in allowed})
    return out


def rank(rows):
    return i330.sparse_rank_q(rows)


def audit(kind):
    _, orbits, selected, basis_rank = i330.build_basis()
    assert basis_rank == 16 and len(selected) == 16
    if kind == 'k4':
        rows = i330.image_rows(selected, orbits, 'k4jet', 1)
        r0 = rank(filter_t(rows, {0}))
        r1 = rank(filter_t(rows, {1}))
        r01 = rank(filter_t(rows, {0,1}))
        assert (r0, r01) == (11, 16)
        increment = r01 - r0
        result = {
            'iteration': 332,
            'kind': 'k4',
            'k5_candidate_dimension': 16,
            'value_only_rank': r0,
            'first_jet_only_rank': r1,
            'value_plus_first_jet_rank': r01,
            'incremental_rank_from_first_jet_given_values': increment,
            'minimum_additional_independent_first_jet_constraints_after_full_value_data': increment,
            'classification': 'K4_REQUIRES_AT_LEAST_5_ADDITIONAL_INDEPENDENT_FIRST_NORMAL_JET_CONSTRAINTS_AFTER_VALUE_LAYER',
        }
    elif kind == 'k3':
        rows = i330.image_rows(selected, orbits, 'k3jet', 2)
        r0 = rank(filter_t(rows, {0}))
        r1 = rank(filter_t(rows, {1}))
        r2 = rank(filter_t(rows, {2}))
        r01 = rank(filter_t(rows, {0,1}))
        r012 = rank(filter_t(rows, {0,1,2}))
        assert (r0, r01, r012) == (4, 7, 16)
        d1 = r01-r0
        d2 = r012-r01
        result = {
            'iteration': 332,
            'kind': 'k3',
            'k5_candidate_dimension': 16,
            'value_only_rank': r0,
            'first_jet_only_rank': r1,
            'second_jet_only_rank': r2,
            'value_plus_first_jet_rank': r01,
            'value_plus_first_plus_second_jet_rank': r012,
            'incremental_rank_from_first_jet_given_values': d1,
            'incremental_rank_from_second_jet_given_lower_layers': d2,
            'minimum_additional_independent_first_jet_constraints_after_full_value_data': d1,
            'minimum_additional_independent_second_jet_constraints_after_full_value_and_first_jet_data': d2,
            'classification': 'K3_REQUIRES_AT_LEAST_3_FIRST_JET_AND_9_SECOND_JET_NEW_INDEPENDENT_DIRECTIONS_BEYOND_LOWER_LAYERS',
        }
    else:
        raise ValueError(kind)
    result['scope_guard'] = 'These are exact ranks of the centered-stratum candidate restriction maps from Iter330, not source-defined physical normalization conditions and not a physical counterterm count.'
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--kind',choices=['k4','k3'],required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    result=audit(a.kind)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__':
    main()
