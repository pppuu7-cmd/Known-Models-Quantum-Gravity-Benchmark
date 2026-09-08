"""Reference helpers for KMQGB cross-order rigidity.

Methodology only; not Candidate Gravity dynamics.
"""

from __future__ import annotations

import numpy as np


def robust_rank(a: np.ndarray, rtol: float = 1e-12) -> int:
    s = np.linalg.svd(a, compute_uv=False)
    if s.size == 0:
        return 0
    tol = rtol * s[0]
    return int(np.sum(s > tol))


def shared_parameter_rigidity(jacobians: list[np.ndarray], rtol: float = 1e-12):
    """Compute stacked complement dimension and shared-parameter rigidity gain."""
    ranks = [robust_rank(j, rtol=rtol) for j in jacobians]
    m_total = sum(j.shape[0] for j in jacobians)
    j_stack = np.vstack(jacobians)
    rank_stack = robust_rank(j_stack, rtol=rtol)
    d_perp_stack = m_total - rank_stack
    d_perp_separate = sum(j.shape[0] - r for j, r in zip(jacobians, ranks))
    r_shared = sum(ranks) - rank_stack
    assert d_perp_stack - d_perp_separate == r_shared
    return {
        "block_ranks": ranks,
        "stack_rank": rank_stack,
        "d_perp_separate_sum": d_perp_separate,
        "d_perp_stack": d_perp_stack,
        "R_shared": r_shared,
    }


def monomial_log_nullspace(exponent_matrix: np.ndarray, rtol: float = 1e-12):
    """Return basis vectors u with P^T u = 0 for exact monomial nuisance invariants."""
    # Nullspace of P^T from SVD.
    a = exponent_matrix.T
    u, s, vh = np.linalg.svd(a, full_matrices=True)
    rank = 0 if s.size == 0 else int(np.sum(s > rtol * s[0]))
    return vh[rank:].T


def monomial_invariant(values: np.ndarray, amplitudes: np.ndarray, u: np.ndarray) -> float:
    """Evaluate product_i (values_i/amplitudes_i)^u_i in a positive-real domain."""
    ratio = np.asarray(values, dtype=float) / np.asarray(amplitudes, dtype=float)
    if np.any(ratio <= 0):
        raise ValueError("Reference invariant assumes positive-real ratios; freeze branch/sign conventions otherwise.")
    return float(np.exp(np.dot(u, np.log(ratio))))


def self_test():
    # Two blocks depend on the same single parent amplitude: stacking gains one
    # comparator-orthogonal direction compared with fitting blocks separately.
    j1 = np.array([[1.0], [2.0]])
    j2 = np.array([[3.0], [6.0]])
    rigidity = shared_parameter_rigidity([j1, j2])
    assert rigidity["R_shared"] == 1

    # Exact monomial example c1=a f1, c2=a^2 f2.
    # P=[[1],[2]], so u=(2,-1) is a left-null exponent vector.
    p = np.array([[1.0], [2.0]])
    basis = monomial_log_nullspace(p)
    u = basis[:, 0]
    u = u / u[0] * 2.0
    a = 1.7
    f = np.array([3.0, 5.0])
    c = np.array([a * f[0], a**2 * f[1]])
    inv = monomial_invariant(c, f, u)
    return {
        "rigidity": rigidity,
        "monomial_null_vector": u.tolist(),
        "monomial_invariant": inv,
    }


if __name__ == "__main__":
    print(self_test())
