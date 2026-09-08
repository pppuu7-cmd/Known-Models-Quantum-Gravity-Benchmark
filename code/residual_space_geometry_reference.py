"""Reference implementation for KMQGB comparator residual-space geometry.

This is lightweight methodology code, not a Candidate Gravity model.

Core definitions:
    A = Sigma^{-1/2} J_C
    Pi_perp = I - A A^+
    COR = Pi_perp Sigma^{-1/2} r

The self-test checks:
- projector idempotence;
- annihilation of the comparator tangent space;
- Euclidean symmetry in whitened coordinates;
- invariance under an invertible reparameterization of comparator nuisance coordinates;
- exact-tangent signal separation eta ~ 0.
"""

from __future__ import annotations

import numpy as np


def symmetric_inverse_sqrt(covariance: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """Return the symmetric inverse square root of an SPD covariance matrix."""
    covariance = np.asarray(covariance, dtype=float)
    evals, evecs = np.linalg.eigh(covariance)
    if np.min(evals) <= tol:
        raise ValueError("covariance must be positive definite on the represented physical subspace")
    return evecs @ np.diag(1.0 / np.sqrt(evals)) @ evecs.T


def comparator_projector(covariance: np.ndarray, comparator_jacobian: np.ndarray):
    """Construct the whitened comparator tangent and orthogonal complement projector."""
    w_half = symmetric_inverse_sqrt(covariance)
    a = w_half @ np.asarray(comparator_jacobian, dtype=float)
    pi_perp = np.eye(a.shape[0]) - a @ np.linalg.pinv(a)
    return w_half, a, pi_perp


def comparator_orthogonal_residual(
    residual: np.ndarray,
    covariance: np.ndarray,
    comparator_jacobian: np.ndarray,
) -> np.ndarray:
    """Return COR=(I-AA^+) Sigma^{-1/2} residual."""
    w_half, _, pi_perp = comparator_projector(covariance, comparator_jacobian)
    z = w_half @ np.asarray(residual, dtype=float)
    return pi_perp @ z


def local_signal_separation(
    signal: np.ndarray,
    covariance: np.ndarray,
    comparator_jacobian: np.ndarray,
) -> float:
    """Return eta(s), the fraction of a signal outside the local comparator tangent span."""
    w_half, _, pi_perp = comparator_projector(covariance, comparator_jacobian)
    signal_w = w_half @ np.asarray(signal, dtype=float)
    norm = np.linalg.norm(signal_w)
    if norm == 0.0:
        return 0.0
    return float(np.linalg.norm(pi_perp @ signal_w) / norm)


def self_test(seed: int = 1234) -> dict[str, float]:
    """Run deterministic numerical integrity checks."""
    rng = np.random.default_rng(seed)
    m, p = 8, 3

    x = rng.normal(size=(m, m))
    covariance = x @ x.T + 0.5 * np.eye(m)
    jacobian = rng.normal(size=(m, p))

    _, a, pi_perp = comparator_projector(covariance, jacobian)

    # Invertible nuisance reparameterization: J -> J R must not change the tangent projector.
    rmat = rng.normal(size=(p, p))
    while abs(np.linalg.det(rmat)) < 0.1:
        rmat = rng.normal(size=(p, p))
    _, _, pi_reparam = comparator_projector(covariance, jacobian @ rmat)

    tangent_signal = a @ rng.normal(size=p)
    tangent_norm = np.linalg.norm(tangent_signal)

    return {
        "idempotence_error": float(np.linalg.norm(pi_perp @ pi_perp - pi_perp)),
        "tangent_annihilation_error": float(np.linalg.norm(pi_perp @ a)),
        "symmetry_error": float(np.linalg.norm(pi_perp - pi_perp.T)),
        "reparameterization_error": float(np.linalg.norm(pi_perp - pi_reparam)),
        "eta_exact_tangent": float(np.linalg.norm(pi_perp @ tangent_signal) / tangent_norm),
    }


if __name__ == "__main__":
    for key, value in self_test().items():
        print(f"{key}: {value:.16e}")
