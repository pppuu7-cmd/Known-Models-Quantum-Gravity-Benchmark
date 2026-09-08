#!/usr/bin/env python3
"""Executable witness for the exact finite-range local TT-projector no-go.

The theorem is analytic: a translation-invariant finite-range lattice operator has
a trigonometric-polynomial Fourier symbol and is continuous at k=0, while the
exact transverse/TT projector has a direction-dependent k->0 limit.

This script checks the direction-limit separation and the rank-2 spin-2 TT
projector algebra.  It is not a substitute for the proof in
protocol/LOCAL_TT_PROJECTOR_NO_GO.md.
"""

from __future__ import annotations

import numpy as np


def transverse_projector(k: np.ndarray) -> np.ndarray:
    k = np.asarray(k, dtype=float)
    norm = np.linalg.norm(k)
    if norm == 0:
        raise ValueError("transverse projector is undefined at k=0")
    n = k / norm
    return np.eye(3) - np.outer(n, n)


def tt_projector(k: np.ndarray) -> np.ndarray:
    p = transverse_projector(k)
    out = np.zeros((3, 3, 3, 3), dtype=float)
    for i in range(3):
        for j in range(3):
            for a in range(3):
                for b in range(3):
                    out[i, j, a, b] = (
                        0.5 * (p[i, a] * p[j, b] + p[i, b] * p[j, a])
                        - 0.5 * p[i, j] * p[a, b]
                    )
    return out


def self_test() -> None:
    # Directional limits are exactly independent of radius because the projectors
    # depend only on k/|k|.  The nonzero separation therefore survives eps->0.
    eps_values = [1.0, 1e-2, 1e-6, 1e-12]
    vector_separations = []
    tt_separations = []

    for eps in eps_values:
        kx = np.array([eps, 0.0, 0.0])
        ky = np.array([0.0, eps, 0.0])

        px = transverse_projector(kx)
        py = transverse_projector(ky)
        pix = tt_projector(kx)
        piy = tt_projector(ky)

        vector_separations.append(float(np.linalg.norm(px - py)))
        tt_separations.append(float(np.linalg.norm(pix - piy)))

        # The TT map is an orthogonal projector of rank two on symmetric tensors.
        m = pix.reshape(9, 9)
        assert np.allclose(m @ m, m, atol=1e-12)
        assert np.isclose(np.trace(m), 2.0, atol=1e-12)
        assert np.linalg.matrix_rank(m, tol=1e-10) == 2

    expected_vector = np.sqrt(2.0)
    expected_tt = np.sqrt(3.5)  # sqrt(7/2)

    assert np.allclose(vector_separations, expected_vector, atol=1e-12)
    assert np.allclose(tt_separations, expected_tt, atol=1e-12)
    assert min(vector_separations) > 1.0
    assert min(tt_separations) > 1.0

    print("local_tt_projector_no_go_reference: PASS")
    print("eps=", eps_values)
    print("vector_direction_limit_separation=", vector_separations)
    print("tt_direction_limit_separation=", tt_separations)
    print("interpretation=NO_CONTINUOUS_FINITE_RANGE_EXACT_TT_SYMBOL")


if __name__ == "__main__":
    self_test()
