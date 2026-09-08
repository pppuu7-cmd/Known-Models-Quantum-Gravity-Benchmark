"""Reference implementation for KMQGB optimal comparator-annihilating contrasts.

This is a methodology/self-test helper, not Candidate Gravity dynamics.
"""

from __future__ import annotations

import numpy as np


def psd_inv_sqrt(sigma: np.ndarray, rtol: float = 1e-12) -> np.ndarray:
    """Moore-Penrose inverse square root on the supported PSD subspace."""
    vals, vecs = np.linalg.eigh(sigma)
    if vals.size == 0:
        return np.zeros_like(sigma)
    vmax = float(np.max(np.abs(vals)))
    if vmax == 0.0:
        return np.zeros_like(sigma)
    keep = vals > rtol * vmax
    v = vecs[:, keep]
    lam = vals[keep]
    return (v * (1.0 / np.sqrt(lam))) @ v.T


def comparator_projector(sigma: np.ndarray, jacobian: np.ndarray, rtol: float = 1e-12):
    """Return symmetric whitening, whitened tangent, and orthogonal complement projector."""
    w12 = psd_inv_sqrt(sigma, rtol=rtol)
    a = w12 @ jacobian
    pi_perp = np.eye(a.shape[0]) - a @ np.linalg.pinv(a, rcond=rtol)
    return w12, a, pi_perp


def cor(sigma: np.ndarray, jacobian: np.ndarray, residual: np.ndarray, rtol: float = 1e-12):
    """Comparator-Orthogonal Residual in whitened coordinates."""
    w12, _, pi_perp = comparator_projector(sigma, jacobian, rtol=rtol)
    return pi_perp @ (w12 @ residual)


def optimal_contrast(
    sigma: np.ndarray,
    jacobian: np.ndarray,
    signal: np.ndarray,
    rtol: float = 1e-12,
):
    """Unit-variance comparator-null contrast maximizing local SNR for `signal`."""
    w12, _, pi_perp = comparator_projector(sigma, jacobian, rtol=rtol)
    direction = w12 @ pi_perp @ w12 @ signal
    variance = float(direction.T @ sigma @ direction)
    if variance <= rtol:
        return np.zeros_like(signal), 0.0
    w = direction / np.sqrt(variance)
    snr_max = float(np.linalg.norm(pi_perp @ (w12 @ signal)))
    return w, snr_max


def projected_kg_jacobian(
    sigma: np.ndarray,
    comparator_jacobian: np.ndarray,
    kg_jacobian: np.ndarray,
    rtol: float = 1e-12,
):
    """Projected Candidate-Gravity Jacobian after local comparator profiling."""
    w12, _, pi_perp = comparator_projector(sigma, comparator_jacobian, rtol=rtol)
    return pi_perp @ w12 @ kg_jacobian


def augmentation_gain(old_j: np.ndarray, new_j: np.ndarray, rtol: float = 1e-12):
    """Return exact algebraic Delta d_perp for adding rows/observables in `new_j`."""
    old_rank = np.linalg.matrix_rank(old_j, tol=rtol)
    stacked = np.vstack([old_j, new_j])
    new_rank = np.linalg.matrix_rank(stacked, tol=rtol)
    k = new_j.shape[0]
    return int(k - (new_rank - old_rank)), int(old_rank), int(new_rank)


def _self_test(seed: int = 20260908):
    rng = np.random.default_rng(seed)
    m, p = 10, 4
    b = rng.normal(size=(m, m))
    sigma = b @ b.T + 0.25 * np.eye(m)
    j = rng.normal(size=(m, p))
    s = rng.normal(size=m)

    w12, a, pi = comparator_projector(sigma, j)
    idem = np.linalg.norm(pi @ pi - pi)
    tangent_annihilation = np.linalg.norm(pi @ a)

    # Reparameterize comparator nuisance coordinates by an invertible matrix.
    q = rng.normal(size=(p, p))
    while abs(np.linalg.det(q)) < 1e-3:
        q = rng.normal(size=(p, p))
    _, _, pi2 = comparator_projector(sigma, j @ q)
    reparam = np.linalg.norm(pi2 - pi)

    w, snr = optimal_contrast(sigma, j, s)
    null_err = np.linalg.norm(j.T @ w)
    variance_err = abs(float(w.T @ sigma @ w) - 1.0) if np.linalg.norm(w) else 0.0
    snr_direct = abs(float(w.T @ s)) if np.linalg.norm(w) else 0.0
    snr_err = abs(snr_direct - snr)

    return {
        "projector_idempotence_error": float(idem),
        "tangent_annihilation_error": float(tangent_annihilation),
        "nuisance_reparameterization_error": float(reparam),
        "optimal_contrast_null_error": float(null_err),
        "optimal_contrast_variance_error": float(variance_err),
        "optimal_contrast_snr_error": float(snr_err),
    }


if __name__ == "__main__":
    print(_self_test())
