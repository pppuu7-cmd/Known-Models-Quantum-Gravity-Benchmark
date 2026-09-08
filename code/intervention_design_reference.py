"""Reference scoring for KMQGB multi-configuration intervention rigidity.

Methodology only; not Candidate Gravity dynamics.
"""

from __future__ import annotations

import numpy as np


def psd_inv_sqrt(sigma: np.ndarray, rtol: float = 1e-12) -> np.ndarray:
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


def projected_geometry(sigma: np.ndarray, j_comp: np.ndarray, rtol: float = 1e-12):
    w12 = psd_inv_sqrt(sigma, rtol=rtol)
    a = w12 @ j_comp
    pi = np.eye(a.shape[0]) - a @ np.linalg.pinv(a, rcond=rtol)
    return w12, pi


def design_score(
    sigma: np.ndarray,
    j_comp: np.ndarray,
    j_kg: np.ndarray | None = None,
    signal: np.ndarray | None = None,
    rtol: float = 1e-12,
):
    """Return post-comparator rank/singular-value/SNR diagnostics for one design."""
    w12, pi = projected_geometry(sigma, j_comp, rtol=rtol)
    out = {
        "observable_dimension": int(sigma.shape[0]),
        "comparator_rank": int(np.linalg.matrix_rank(w12 @ j_comp, tol=rtol)),
    }
    out["d_perp"] = out["observable_dimension"] - out["comparator_rank"]

    if j_kg is not None:
        b = pi @ w12 @ j_kg
        svals = np.linalg.svd(b, compute_uv=False)
        if svals.size:
            tol = rtol * svals[0]
            nz = svals[svals > tol]
        else:
            nz = np.array([])
        out["kg_projected_rank"] = int(nz.size)
        out["kg_projected_singular_values"] = svals.tolist()
        out["kg_sigma_min_nonzero"] = float(nz[-1]) if nz.size else 0.0

    if signal is not None:
        out["projected_signal_snr"] = float(np.linalg.norm(pi @ (w12 @ signal)))

    return out


def self_test():
    # Two configurations share one dynamics parameter but have distinct signal response.
    sigma = np.eye(4)
    j_comp = np.array([[1.0], [2.0], [1.0], [2.0]])
    j_kg = np.array([[1.0], [0.0], [0.0], [1.0]])
    signal = j_kg[:, 0]
    score = design_score(sigma, j_comp, j_kg=j_kg, signal=signal)
    assert score["d_perp"] == 3
    assert score["kg_projected_rank"] == 1
    assert score["projected_signal_snr"] > 0.0
    return score


if __name__ == "__main__":
    print(self_test())
