"""Reference self-test for LQG gamma-duality breaking identifiability.

KMQGB Iter173.

If the renormalized parity-sector relation contains a duality-breaking residual

    Delta_gamma = 2 f_GB/f_CS - (gamma - 1/gamma),

then the primordial observable combination is represented as

    q = (pi/8) (r + 8 n_T) / Pi
      = 1/gamma_EFT - gamma_EFT - Delta_gamma.

This fixture demonstrates three structural facts:

1. q alone cannot identify both gamma_EFT and Delta_gamma;
2. an independently measured geometry observable a_* = K gamma restores rank
   only if the geometry gamma is already matched to gamma_EFT;
3. if gamma_geom is an independent parameter, q + a_* still leaves one
   unidentified direction.

This is an algebraic identifiability control, not a phenomenological forecast.
"""

from __future__ import annotations

import math
import numpy as np


def q_from_gamma_delta(gamma: float, delta_gamma: float) -> float:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return 1.0 / gamma - gamma - delta_gamma


def gamma_from_q_delta(q: float, delta_gamma: float) -> float:
    """Positive-gamma inverse when Delta_gamma is independently fixed."""
    x = q + delta_gamma
    return 0.5 * (math.sqrt(x * x + 4.0) - x)


def jacobian_q_only(gamma: float) -> np.ndarray:
    """Jacobian of q with respect to (gamma_EFT, Delta_gamma)."""
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return np.array([[-1.0 - 1.0 / gamma**2, -1.0]], dtype=float)


def jacobian_shared_geometry(gamma: float, k_area: float) -> np.ndarray:
    """Jacobian of (q, a_*) when the same gamma controls EFT and geometry."""
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return np.array(
        [
            [-1.0 - 1.0 / gamma**2, -1.0],
            [k_area, 0.0],
        ],
        dtype=float,
    )


def jacobian_unmatched_geometry(gamma_eft: float, k_area: float) -> np.ndarray:
    """Jacobian wrt (gamma_EFT, Delta_gamma, gamma_geom) without identity map."""
    if gamma_eft <= 0.0:
        raise ValueError("gamma_eft must be positive")
    return np.array(
        [
            [-1.0 - 1.0 / gamma_eft**2, -1.0, 0.0],
            [0.0, 0.0, k_area],
        ],
        dtype=float,
    )


def run_self_test() -> None:
    # Exact positive-gamma inversion once Delta_gamma is fixed.
    for gamma in (0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 10.0):
        for delta in (-0.3, -0.05, 0.0, 0.07, 0.4):
            q = q_from_gamma_delta(gamma, delta)
            recovered = gamma_from_q_delta(q, delta)
            if not math.isclose(recovered, gamma, rel_tol=1e-12, abs_tol=1e-12):
                raise AssertionError((gamma, delta, q, recovered))

    # q alone: one scalar constraint for two parameters => structural rank 1.
    for gamma in (0.1, 0.5, 1.0, 3.0):
        jq = jacobian_q_only(gamma)
        if np.linalg.matrix_rank(jq) != 1:
            raise AssertionError(("q-only rank", gamma, jq))

    # Shared gamma with an independent area observable makes the 2x2 Jacobian
    # full rank. Analytically det J = K, independent of gamma.
    for gamma in (0.1, 0.5, 1.0, 3.0):
        for k_area in (0.25, 1.0, 7.0):
            js = jacobian_shared_geometry(gamma, k_area)
            det = float(np.linalg.det(js))
            if not math.isclose(det, k_area, rel_tol=1e-12, abs_tol=1e-12):
                raise AssertionError(("determinant", gamma, k_area, det))
            if np.linalg.matrix_rank(js) != 2:
                raise AssertionError(("shared-geometry rank", gamma, k_area, js))

    # Negative control: no geometry sensitivity means the degeneracy remains.
    j0 = jacobian_shared_geometry(0.5, 0.0)
    if np.linalg.matrix_rank(j0) != 1:
        raise AssertionError(("zero-area-sensitivity negative control", j0))

    # Crucial parameter-identity control: if gamma_geom is not identified with
    # gamma_EFT, two observables constrain three parameters and rank stays 2.
    ju = jacobian_unmatched_geometry(0.5, 1.0)
    if np.linalg.matrix_rank(ju) != 2:
        raise AssertionError(("unmatched-geometry rank", ju))
    if ju.shape[1] != 3 or np.linalg.matrix_rank(ju) >= ju.shape[1]:
        raise AssertionError(("unmatched geometry should remain underidentified", ju))

    print("PASS: LQG gamma-duality breaking identifiability reference")
    print("q-only: rank 1 for {gamma_EFT, Delta_gamma}")
    print("shared geometry: rank 2 with det(J)=K")
    print("unmatched gamma_geom: rank 2 < 3 parameters")


if __name__ == "__main__":
    run_self_test()
