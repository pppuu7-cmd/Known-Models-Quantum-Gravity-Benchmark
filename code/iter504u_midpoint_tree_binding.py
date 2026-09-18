#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction


def _q(x):
    return Fraction(str(x))


def _node(depth, lo, hi):
    return (int(depth), _q(lo), _q(hi))


def binding_errors(case):
    errors = []

    for leaf in case.get('leaves', []):
        try:
            lo = _q(leaf['amp_lower_q'])
            hi = _q(leaf['amp_upper_q'])
            mid = _q(leaf['local_mid_q'])
            if mid != (lo + hi) / 2:
                errors.append('exact_local_midpoint')
        except Exception:
            errors.append('exact_local_midpoint_parse')

    try:
        root = _node(0, case['parent_amp_lower_q'], case['parent_amp_upper_q'])
    except Exception:
        return errors + ['tree_root_parse']

    incs = case.get('componentwise_parent_inclusion_records', [])
    child_nodes = set()
    edges = []
    for rec in incs:
        try:
            child = _node(rec['depth'], rec['amp_lower_q'], rec['amp_upper_q'])
            parent = _node(rec['parent_depth'], rec['parent_amp_lower_q'], rec['parent_amp_upper_q'])
            if child[0] != parent[0] + 1:
                errors.append('tree_depth_edge')
            p_lo, p_hi = parent[1], parent[2]
            c_lo, c_hi = child[1], child[2]
            p_mid = (p_lo + p_hi) / 2
            if (c_lo, c_hi) not in ((p_lo, p_mid), (p_mid, p_hi)):
                errors.append('tree_dyadic_child_interval')
            if child in child_nodes:
                errors.append('tree_duplicate_child')
            child_nodes.add(child)
            edges.append((child, parent))
        except Exception:
            errors.append('tree_record_parse')

    if len(child_nodes) != max(0, int(case.get('visited_node_count', 0)) - 1):
        errors.append('tree_visited_node_binding')

    parent_of = {}
    for child, parent in edges:
        parent_of[child] = parent
        if parent != root and parent not in child_nodes:
            errors.append('tree_parent_not_visited')

    for child in child_nodes:
        cur = child
        seen = set()
        while cur != root:
            if cur in seen:
                errors.append('tree_cycle')
                break
            seen.add(cur)
            if cur not in parent_of:
                errors.append('tree_disconnected_child')
                break
            cur = parent_of[cur]

    for leaf in case.get('leaves', []):
        try:
            node = _node(leaf['depth'], leaf['amp_lower_q'], leaf['amp_upper_q'])
            if node != root and node not in child_nodes:
                errors.append('tree_leaf_not_visited')
        except Exception:
            errors.append('tree_leaf_parse')

    return errors
