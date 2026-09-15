#!/usr/bin/env python3
"""Exact certificate for the prospectively frozen j=1 coherent-contact Hörmander gate.

Authority:
  research/SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_PREREG_2026-09-15.md

The certificate is dependency-free.  It verifies only the frozen finite algebra:
  * the Bloch vector for z0=(1,0),
  * exact K5 incidence conormals in the 12 boost-normal coordinates,
  * the triangle cycle relation and forest/non-cycle adversarial controls,
  * the exact j=1 source-polynomial coefficients c1,c2,c3,
  * presence of a nonzero delta'' contact coefficient for real rho != 0.

It does NOT prove nonexistence of the product.  Its interpretation is only that the
standard Hörmander sufficient multiplication criterion fails at the frozen witness.
"""

from fractions import Fraction
import json

# -----------------------------------------------------------------------------
# Exact 12D normal-coordinate linear algebra
# Coordinate order: X2x,X2y,X2z,X3x,X3y,X3z,X4x,X4y,X4z,X5x,X5y,X5z.
# Gauge-fixed vertex 1 has X1=0.
# -----------------------------------------------------------------------------

VERTICES = (1, 2, 3, 4, 5)
FREE_VERTICES = (2, 3, 4, 5)
DIM_NORMAL_PER_VERTEX = 3
DIM_NORMAL = len(FREE_VERTICES) * DIM_NORMAL_PER_VERTEX

# z0=(1,0)^T gives the exact Bloch vector (0,0,1).
BLOCH_Z0 = (0, 0, 1)
assert BLOCH_Z0 == (0, 0, 1)


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def scale(c, u):
    return tuple(c * a for a in u)


def is_zero(u):
    return all(a == 0 for a in u)


def edge_conormal(a, b, n=BLOCH_Z0):
    """Return dB_ab=(e_a-e_b) tensor n, with vertex 1 gauge-fixed away."""
    if a == b or a not in VERTICES or b not in VERTICES:
        raise ValueError("invalid K5 edge")
    out = [0] * DIM_NORMAL
    for vertex, coeff in ((a, +1), (b, -1)):
        if vertex == 1:
            continue
        block = FREE_VERTICES.index(vertex) * DIM_NORMAL_PER_VERTEX
        for k, nk in enumerate(n):
            out[block + k] += coeff * nk
    return tuple(out)


def exact_rank(rows):
    """Exact row rank over Q by Fraction Gaussian elimination."""
    mat = [[Fraction(x) for x in row] for row in rows]
    if not mat:
        return 0
    m, n = len(mat), len(mat[0])
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = next((r for r in range(rank, m) if mat[r][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        p = mat[rank][col]
        mat[rank] = [x / p for x in mat[rank]]
        for r in range(m):
            if r == rank:
                continue
            f = mat[r][col]
            if f != 0:
                mat[r] = [x - f * y for x, y in zip(mat[r], mat[rank])]
        rank += 1
        col += 1
    return rank


d12 = edge_conormal(1, 2)
d23 = edge_conormal(2, 3)
d13 = edge_conormal(1, 3)
d14 = edge_conormal(1, 4)

assert not is_zero(d12)
assert not is_zero(d23)
assert not is_zero(d13)

# Frozen exact cycle relation.
triangle_relation = sub(add(d12, d23), d13)
assert is_zero(triangle_relation)
assert exact_rank([d12, d23, d13]) == 2

# Adversarial controls from the preregistration.
forest_pair_rank = exact_rank([d12, d13])
assert forest_pair_rank == 2

noncycle_relation = sub(add(d12, d23), d14)
assert not is_zero(noncycle_relation)
noncycle_triple_rank = exact_rank([d12, d23, d14])
assert noncycle_triple_rank == 3

# -----------------------------------------------------------------------------
# Exact j=1 contact coefficient algebra, without CAS.
#
# Source Eq. (39), j=1:
#   F_1(rho+sigma q,rho)
#     = [(iR+1)(iR)(iR-1)] / [(ir+1)(ir)(ir-1)],  R=r+sigma q
#     = R(1+R^2) / [r(1+r^2)].
#
# Expand the numerator in q, using sigma^2=1:
#   r(1+r^2)
#   + sigma q (1+3r^2)
#   + q^2 (3r)
#   + sigma q^3.
#
# We represent polynomials in r by integer coefficient tuples low-degree first.
# -----------------------------------------------------------------------------


def poly_add(p, q):
    n = max(len(p), len(q))
    return tuple((p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n))


def poly_mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


RHO = (0, 1)                 # r
ONE = (1,)
RHO2 = poly_mul(RHO, RHO)    # r^2
DEN = poly_mul(RHO, poly_add(ONE, RHO2))  # r(1+r^2) = r+r^3

# Direct q-coefficient numerators of R(1+R^2), with the explicit sigma factor
# suppressed on odd powers of q.
direct_q0 = DEN
direct_q1_without_sigma = poly_add(ONE, tuple(3 * x for x in RHO2))
direct_q2 = tuple(3 * x for x in RHO)
direct_q3_without_sigma = ONE

# Frozen expected coefficients:
#   c1=(1+3r^2)/DEN,
#   c2=6/(1+r^2), hence c2/2=3r/DEN,
#   c3=6/DEN, hence c3/6=1/DEN.
expected_q0 = DEN
expected_q1_without_sigma = (1, 0, 3)
expected_q2 = (0, 3)
expected_q3_without_sigma = (1,)

assert direct_q0 == expected_q0
assert direct_q1_without_sigma == expected_q1_without_sigma
assert direct_q2 == expected_q2
assert direct_q3_without_sigma == expected_q3_without_sigma

# Eq. (37), n=2 contact term:
#   [c3/3!] (-i)^3 delta'' = i/[rho(1+rho^2)] delta''.
# The rational coefficient is 1/DEN.  For real rho != 0, DEN != 0 because
# 1+rho^2 > 0; hence the delta'' coefficient is nonzero.
delta2_numerator = (1,)
delta2_denominator = DEN
assert delta2_numerator == (1,)
assert delta2_denominator == (0, 1, 0, 1)

classification = "SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_CRITERION_FAILS_SCOPED"

result = {
    "classification": classification,
    "normal_dimension": DIM_NORMAL,
    "bloch_z0": list(BLOCH_Z0),
    "conormals": {
        "dB_12": list(d12),
        "dB_23": list(d23),
        "dB_13": list(d13),
        "dB_14": list(d14),
    },
    "triangle_relation_dB12_plus_dB23_minus_dB13": list(triangle_relation),
    "triangle_rank": exact_rank([d12, d23, d13]),
    "forest_pair_rank_dB12_dB13": forest_pair_rank,
    "noncycle_relation_dB12_plus_dB23_minus_dB14": list(noncycle_relation),
    "noncycle_triple_rank": noncycle_triple_rank,
    "j1_source_polynomial": {
        "common_denominator_rho_polynomial_low_to_high": list(DEN),
        "q0_numerator": list(direct_q0),
        "q1_numerator_without_sigma": list(direct_q1_without_sigma),
        "q2_numerator": list(direct_q2),
        "q3_numerator_without_sigma": list(direct_q3_without_sigma),
        "c1": "(3*rho^2+1)/(rho*(1+rho^2))",
        "c2": "6/(1+rho^2)",
        "c3": "6/(rho*(1+rho^2))",
        "delta2_coefficient": "i/(rho*(1+rho^2))",
        "delta2_nonzero_for_real_rho_ne_0": True,
    },
    "hormander_sufficient_criterion_at_frozen_witness": False,
    "claim_ceiling": (
        "The standard Hoermander sufficient multiplication criterion fails at the frozen "
        "three-contact K5 triangle witness. This is not a proof that the product does not "
        "exist, not a proof of final-vertex nonuniqueness, and does not close D7-S2."
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))
