"""Linear-Gaussian predictive holdout reference for KMQGB rigidity tests.

Methodology only; not Candidate Gravity dynamics.
"""

from __future__ import annotations

import numpy as np


def pinv(a: np.ndarray, rcond: float = 1e-12) -> np.ndarray:
    return np.linalg.pinv(a, rcond=rcond)


def gls_training_map(j_t: np.ndarray, sigma_tt: np.ndarray, rcond: float = 1e-12) -> np.ndarray:
    w_t = pinv(sigma_tt, rcond=rcond)
    fisher = j_t.T @ w_t @ j_t
    return pinv(fisher, rcond=rcond) @ j_t.T @ w_t


def predictive_covariance(
    j_t: np.ndarray,
    j_h: np.ndarray,
    sigma_tt: np.ndarray,
    sigma_th: np.ndarray,
    sigma_hh: np.ndarray,
    rcond: float = 1e-12,
) -> np.ndarray:
    """Exact covariance of eps_H - J_H M eps_T for linear GLS training fit."""
    m = gls_training_map(j_t, sigma_tt, rcond=rcond)
    sigma_ht = sigma_th.T
    return (
        sigma_hh
        + j_h @ m @ sigma_tt @ m.T @ j_h.T
        - j_h @ m @ sigma_th
        - sigma_ht @ m.T @ j_h.T
    )


def predictive_residual(
    y_t: np.ndarray,
    y_h: np.ndarray,
    j_t: np.ndarray,
    j_h: np.ndarray,
    sigma_tt: np.ndarray,
    rcond: float = 1e-12,
):
    """Zero-intercept linear-model reference. Add a frozen baseline externally if needed."""
    m = gls_training_map(j_t, sigma_tt, rcond=rcond)
    theta_hat = m @ y_t
    return y_h - j_h @ theta_hat, theta_hat


def chi2(residual: np.ndarray, covariance: np.ndarray, rcond: float = 1e-12) -> float:
    return float(residual.T @ pinv(covariance, rcond=rcond) @ residual)


def self_test(seed: int = 20260908):
    rng = np.random.default_rng(seed)
    p, mt, mh = 2, 5, 3
    j_t = rng.normal(size=(mt, p))
    j_h = rng.normal(size=(mh, p))

    a = rng.normal(size=(mt + mh, mt + mh))
    sigma = a @ a.T + 0.5 * np.eye(mt + mh)
    sigma_tt = sigma[:mt, :mt]
    sigma_th = sigma[:mt, mt:]
    sigma_hh = sigma[mt:, mt:]

    pred = predictive_covariance(j_t, j_h, sigma_tt, sigma_th, sigma_hh)
    eigmin = float(np.min(np.linalg.eigvalsh((pred + pred.T) / 2)))
    assert eigmin > -1e-10

    # Independent-block limit should reduce to Sigma_HH + J_H Cov(theta_hat) J_H^T.
    zero_th = np.zeros_like(sigma_th)
    pred_ind = predictive_covariance(j_t, j_h, sigma_tt, zero_th, sigma_hh)
    w = pinv(sigma_tt)
    cov_theta = pinv(j_t.T @ w @ j_t)
    expected = sigma_hh + j_h @ cov_theta @ j_h.T
    err = float(np.linalg.norm(pred_ind - expected))
    assert err < 1e-9

    return {
        "predictive_covariance_min_eigenvalue": eigmin,
        "independent_limit_error": err,
    }


if __name__ == "__main__":
    print(self_test())
