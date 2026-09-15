#!/usr/bin/env python3
"""Exact certificate for the frozen K5 aligned-contact cycle-space gate.

Authority:
  research/SOURCE_J1_K5_ALIGNED_CONTACT_CYCLESPACE_PREREG_2026-09-15.md

No floating-point arithmetic and no external dependencies are used.
"""

from fractions import Fraction
from itertools import combinations
import json

VERTICES = (1, 2, 3, 4, 5)
FREE_VERTICES = (2, 3, 4, 5)
EDGES = tuple(combinations(VERTICES, 2))
N0 = (0, 0, 1)
NORMAL_DIM = 12


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def scale(c, u):
    return tuple(c * a for a in u)


def lincomb(coeffs, rows):
    out = (0,) * len(rows[0])
    for c, row in zip(coeffs, rows):
        out = add(out, scale(c, row))
    return out


def is_zero(v):
    return all(x == 0 for x in v)


def exact_rank(rows):
    if not rows:
        return 0
    m = [[Fraction(x) for x in row] for row in rows]
    nr, nc = len(m), len(m[0])
    r = 0
    c = 0
    while r < nr and c < nc:
        pivot = next((i for i in range(r, nr) if m[i][c] != 0), None)
        if pivot is None:
            c += 1
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][c]
        m[r] = [x / p for x in m[r]]
        for i in range(nr):
            if i == r:
                continue
            f = m[i][c]
            if f != 0:
                m[i] = [x - f * y for x, y in zip(m[i], m[r])]
        r += 1
        c += 1
    return r


def incidence_row(a, b):
    """Gauge-fixed scalar incidence row for oriented edge a->b, a<b."""
    row = [0] * len(FREE_VERTICES)
    if a != 1:
        row[FREE_VERTICES.index(a)] += 1
    if b != 1:
        row[FREE_VERTICES.index(b)] -= 1
    return tuple(row)


def conormal_row(a, b):
    """dB_ab = (e_a-e_b) tensor n0 in the 12 boost-normal coordinates."""
    scalar = incidence_row(a, b)
    out = []
    for s in scalar:
        out.extend(s * n for n in N0)
    return tuple(out)


assert len(EDGES) == 10
assert NORMAL_DIM == len(FREE_VERTICES) * 3
assert N0 == (0, 0, 1)

incidence_rows = [incidence_row(*e) for e in EDGES]
conormal_rows = [conormal_row(*e) for e in EDGES]

incidence_rank = exact_rank(incidence_rows)
conormal_rank = exact_rank(conormal_rows)
cycle_nullity = len(EDGES) - conormal_rank

assert incidence_rank == 4
assert conormal_rank == 4
assert cycle_nullity == 6

# Frozen spanning tree star at gauge-fixed vertex 1.
TREE = ((1, 2), (1, 3), (1, 4), (1, 5))
tree_rows = [conormal_row(*e) for e in TREE]
tree_rank = exact_rank(tree_rows)
tree_nullity = len(TREE) - tree_rank
assert tree_rank == 4
assert tree_nullity == 0

# Every simple triangle a<b<c obeys dB_ab + dB_bc - dB_ac = 0.
triangle_controls = {}
for a, b, c in combinations(VERTICES, 3):
    lhs = sub(add(conormal_row(a, b), conormal_row(b, c)), conormal_row(a, c))
    key = f"{a}{b}{c}"
    triangle_controls[key] = list(lhs)
    assert is_zero(lhs)
assert len(triangle_controls) == 10

# Six explicit fundamental cycles relative to the star tree: each non-tree edge
# (a,b), 2<=a<b<=5, closes triangle (1,a,b).
NON_TREE_EDGES = tuple(combinations(FREE_VERTICES, 2))
assert len(NON_TREE_EDGES) == 6
fundamental_relations = {}
for a, b in NON_TREE_EDGES:
    # dB_1a + dB_ab - dB_1b = 0
    lhs = sub(add(conormal_row(1, a), conormal_row(a, b)), conormal_row(1, b))
    key = f"1{a}{b}"
    fundamental_relations[key] = list(lhs)
    assert is_zero(lhs)
assert len(fundamental_relations) == cycle_nullity

# Adversarial wrong-sign triangle relation must not vanish.
wrong_triangle = add(add(conormal_row(1, 2), conormal_row(2, 3)), conormal_row(1, 3))
assert not is_zero(wrong_triangle)

# The six relation coefficient vectors in R^10 are linearly independent.
edge_index = {e: i for i, e in enumerate(EDGES)}
relation_coeff_rows = []
for a, b in NON_TREE_EDGES:
    coeff = [0] * len(EDGES)
    coeff[edge_index[(1, a)]] = 1
    coeff[edge_index[(a, b)]] = 1
    coeff[edge_index[(1, b)]] = -1
    relation_coeff_rows.append(tuple(coeff))
    assert is_zero(lincomb(coeff, conormal_rows))
relation_basis_rank = exact_rank(relation_coeff_rows)
assert relation_basis_rank == 6

classification = "SOURCE_J1_K5_ALIGNED_CONTACT_CYCLESPACE_HORMANDER_OBSTRUCTION_SCOPED"

result = {
    "classification": classification,
    "vertices": list(VERTICES),
    "edges": [list(e) for e in EDGES],
    "n_vertices": len(VERTICES),
    "n_edges": len(EDGES),
    "ambient_normal_dimension": NORMAL_DIM,
    "bloch_vector": list(N0),
    "incidence_rank": incidence_rank,
    "conormal_rank": conormal_rank,
    "relation_space_dimension": cycle_nullity,
    "graph_cycle_dimension_E_minus_V_plus_1": len(EDGES) - len(VERTICES) + 1,
    "spanning_tree": [list(e) for e in TREE],
    "spanning_tree_rank": tree_rank,
    "spanning_tree_nullity": tree_nullity,
    "n_triangle_relations_checked": len(triangle_controls),
    "all_triangle_relations_zero": all(is_zero(tuple(v)) for v in triangle_controls.values()),
    "fundamental_cycle_basis_count": len(fundamental_relations),
    "fundamental_relation_coeff_rank": relation_basis_rank,
    "wrong_sign_triangle_relation_nonzero": not is_zero(wrong_triangle),
    "hormander_sufficient_criterion_globally_available_at_aligned_witness": False,
    "claim_ceiling": (
        "Exact aligned-spinor K5 conormal cycle-space statement only. It does not prove "
        "product nonexistence, generic-spinor rank 4, final-vertex nonuniqueness, or D7-S2 closure."
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))
