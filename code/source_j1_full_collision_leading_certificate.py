#!/usr/bin/env python3
"""Exact-rational certificate for the j=1 K5 full-collision leading Toller network.

This is a reproducibility certificate for an analytic result, not an outcome-blind
science classifier.  It verifies the frozen spherical->Cartesian intertwiner map,
then contracts the cubic-pole quadrupoles on one fixed rational tangent
configuration.
"""
from fractions import Fraction as F
import itertools
import json
import numpy as np
import sympy as sp

import iter499_arb_core as core
import iter482_common_node_su2_control as ctrl


def delta(i, j):
    return F(int(i == j))


def cartesian_intertwiners():
    out = []
    for channel in range(3):
        T = np.empty((3, 3, 3, 3), dtype=object)
        for i, j, k, l in np.ndindex(T.shape):
            if channel == 0:
                v = F(1, 3) * delta(i, j) * delta(k, l)
            elif channel == 1:
                v = F(1, 6) * (delta(i, k) * delta(j, l) - delta(i, l) * delta(j, k))
            else:
                v = (
                    F(1, 10) * (delta(i, k) * delta(j, l) + delta(i, l) * delta(j, k))
                    - F(1, 15) * delta(i, j) * delta(k, l)
                )
            T[i, j, k, l] = v
        out.append(T)
    return out


def spherical_to_cartesian_control(cart):
    """Exact SymPy check against the frozen _SUPPORTS table in iter499."""
    q = sp.sqrt(2)
    I = sp.I
    # Columns are m=-1,0,+1 spherical basis vectors in Cartesian xyz coordinates.
    S = sp.Matrix([
        [1 / q, 0, -1 / q],
        [-I / q, 0, -I / q],
        [0, 1, 0],
    ])
    if sp.simplify(S.H * S - sp.eye(3)) != sp.zeros(3):
        return False
    ms = (-1, 0, 1)
    for c in range(3):
        sup = core._SUPPORTS[c]
        for inds in itertools.product(range(3), repeat=4):
            v = 0
            for midx in itertools.product(range(3), repeat=4):
                key = tuple(ms[x] for x in midx)
                sval = sup.get(key)
                if sval is None:
                    continue
                term = sp.Rational(sval)
                for leg in range(4):
                    term *= S[inds[leg], midx[leg]]
                v += term
            target = sp.Rational(cart[c][inds].numerator, cart[c][inds].denominator)
            if sp.simplify(v - target) != 0:
                return False
    return True


def Q(v):
    n2 = sum(x * x for x in v)
    if n2 == 0:
        raise ValueError('collision tangent points must be distinct')
    M = np.empty((3, 3), dtype=object)
    for i in range(3):
        for j in range(3):
            M[i, j] = delta(i, j) - F(3) * v[i] * v[j] / n2
    return M


def build_path(cart):
    dummy = np.ones((3, 3, 3, 3), dtype=np.float64)
    args = []
    for node in range(5):
        args += [dummy, ctrl.NODE_LABELS[node]]
    for ei in range(10):
        args += [np.ones((3, 3), dtype=np.float64), ctrl.EDGE_LABELS[ei]]
    args += [[]]
    return np.einsum_path(*args, optimize='greedy')[0]


def contract(cart, mats, channel, path):
    args = []
    for node, c in enumerate(channel):
        args += [cart[c], ctrl.NODE_LABELS[node]]
    for ei, M in enumerate(mats):
        args += [M, ctrl.EDGE_LABELS[ei]]
    args += [[]]
    result = np.einsum(*args, optimize=path)
    return result.item() if hasattr(result, 'item') else result


def main():
    cart = cartesian_intertwiners()
    norms = [sum(x * x for x in T.flat) for T in cart]
    expected_norms = [F(1), F(1, 3), F(1, 5)]
    basis_ok = spherical_to_cartesian_control(cart)

    # Fixed generic rational tangent points, x0 is the gauge root.
    X = [
        (F(0), F(0), F(0)),
        (F(1), F(0), F(0)),
        (F(0), F(1), F(0)),
        (F(0), F(0), F(1)),
        (F(1), F(1), F(1)),
    ]
    mats = []
    norm2 = []
    for a, b in core.EDGES:
        v = tuple(X[a][q] - X[b][q] for q in range(3))
        norm2.append(sum(x * x for x in v))
        mats.append(Q(v))

    path = build_path(cart)
    values = {}
    nonzero = 0
    for ch in itertools.product(range(3), repeat=5):
        v = contract(cart, mats, ch, path)
        values[''.join(map(str, ch))] = str(v)
        nonzero += int(v != 0)

    allzero = F(values['00000'])
    minus_edges = {}
    for cname, sig in ctrl.SIGMAS.items():
        nminus = sum(1 for a, b in core.EDGES if sig[a] * sig[b] < 0)
        minus_edges[cname] = nminus

    passed = bool(
        basis_ok
        and norms == expected_norms
        and allzero == F(11, 24)
        and nonzero == 224
        and minus_edges == {'0to5': 0, '1to4': 4, '2to3': 6}
        and all((n % 2) == 0 for n in minus_edges.values())
    )

    out = {
        'classification': 'SOURCE_J1_FULL_COLLISION_LEADING_CERTIFIED_SCOPED' if passed else 'SOURCE_J1_FULL_COLLISION_LEADING_CERTIFICATE_FAIL',
        'pass': passed,
        'spherical_to_cartesian_exact': basis_ok,
        'intertwiner_norms': [str(x) for x in norms],
        'expected_intertwiner_norms': [str(x) for x in expected_norms],
        'tangent_points': [[str(x) for x in p] for p in X],
        'edge_tangent_norm2': [str(x) for x in norm2],
        'channel_00000_leading_angular_coefficient': str(allzero),
        'nonzero_channels': nonzero,
        'total_channels': 243,
        'minus_edge_counts': minus_edges,
        'all_causal_leading_signs_equal': all((n % 2) == 0 for n in minus_edges.values()),
        'values': values,
        'scope': 'exact leading cubic-pole angular contraction only; absolute-divergence inference additionally uses the separate local normal-measure argument',
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
