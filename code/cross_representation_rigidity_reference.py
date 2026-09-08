"""Reference linear-algebra utilities for cross-representation rigidity.

Methodology only: this code does not establish physical truth or Candidate Gravity novelty.
"""

from __future__ import annotations

import numpy as np


def matrix_rank(a: np.ndarray, rtol: float = 1e-12) -> int:
    a = np.asarray(a, dtype=float)
    if a.size == 0:
        return 0
    s = np.linalg.svd(a, compute_uv=False)
    if s.size == 0 or s[0] == 0:
        return 0
    return int(np.sum(s > rtol * s[0]))


def build_shared_jacobian(shared_blocks, local_blocks):
    """Build J_shared with one common parent-parameter block and local nuisances.

    shared_blocks[a] has shape (m_a, p) for the same p shared parent parameters.
    local_blocks[a] has shape (m_a, q_a) for representation-local parameters.
    """
    if len(shared_blocks) != len(local_blocks):
        raise ValueError("shared_blocks and local_blocks must have equal length")
    if not shared_blocks:
        return np.zeros((0, 0))

    shared_blocks = [np.asarray(x, dtype=float) for x in shared_blocks]
    local_blocks = [np.asarray(x, dtype=float) for x in local_blocks]
    p = shared_blocks[0].shape[1]
    if any(s.shape[1] != p for s in shared_blocks):
        raise ValueError("all shared blocks must use the same parent-parameter dimension")
    if any(s.shape[0] != l.shape[0] for s, l in zip(shared_blocks, local_blocks)):
        raise ValueError("shared/local row counts must match within each representation")

    total_rows = sum(s.shape[0] for s in shared_blocks)
    total_local = sum(l.shape[1] for l in local_blocks)
    out = np.zeros((total_rows, p + total_local))

    row0 = 0
    local0 = p
    for s, l in zip(shared_blocks, local_blocks):
        m = s.shape[0]
        q = l.shape[1]
        out[row0:row0 + m, :p] = s
        if q:
            out[row0:row0 + m, local0:local0 + q] = l
        row0 += m
        local0 += q
    return out


def build_separate_jacobian(shared_blocks, local_blocks):
    """Diagnostic tangent when shared parent parameters are illegally cloned per representation."""
    if len(shared_blocks) != len(local_blocks):
        raise ValueError("shared_blocks and local_blocks must have equal length")
    combined = []
    for s, l in zip(shared_blocks, local_blocks):
        s = np.asarray(s, dtype=float)
        l = np.asarray(l, dtype=float)
        if s.shape[0] != l.shape[0]:
            raise ValueError("shared/local row counts must match")
        combined.append(np.hstack([s, l]))

    total_rows = sum(b.shape[0] for b in combined)
    total_cols = sum(b.shape[1] for b in combined)
    out = np.zeros((total_rows, total_cols))
    r0 = c0 = 0
    for b in combined:
        m, q = b.shape
        out[r0:r0 + m, c0:c0 + q] = b
        r0 += m
        c0 += q
    return out


def cross_representation_gain(shared_blocks, local_blocks, rtol: float = 1e-12):
    j_shared = build_shared_jacobian(shared_blocks, local_blocks)
    j_sep = build_separate_jacobian(shared_blocks, local_blocks)
    rank_shared = matrix_rank(j_shared, rtol)
    rank_sep = matrix_rank(j_sep, rtol)
    gain = rank_sep - rank_shared
    if gain < 0:
        raise AssertionError("shared tangent cannot have larger dimension than independently retuned tangent")
    return {
        "rank_shared": rank_shared,
        "rank_separate": rank_sep,
        "R_XR": gain,
        "J_shared": j_shared,
        "J_separate": j_sep,
    }


def self_test():
    # Two representations, each locally full rank if the same parent coupling is cloned.
    # Sharing that coupling removes one tangent direction and creates one consistency relation.
    s1 = np.array([[1.0], [2.0]])
    l1 = np.array([[1.0], [0.0]])
    s2 = np.array([[1.0], [-1.0]])
    l2 = np.array([[0.0], [1.0]])
    out = cross_representation_gain([s1, s2], [l1, l2])
    assert out["rank_separate"] == 4
    assert out["rank_shared"] == 3
    assert out["R_XR"] == 1
    return {k: v for k, v in out.items() if not k.startswith("J_")}


if __name__ == "__main__":
    print(self_test())
