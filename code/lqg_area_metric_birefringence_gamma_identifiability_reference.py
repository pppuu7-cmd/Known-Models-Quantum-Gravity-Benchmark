"""Area-metric birefringence / gamma identifiability reference.

KMQGB Iter176.

The Lorentzian area-metric GW route uses

    sinh(2 xi) = 1/gamma
    psi = -1/2 atan(tanh xi)

for positive gamma. Algebraically this implies

    gamma = -cot(4 psi),     psi in (-pi/8, 0),

and therefore

    d psi/d gamma = 1/[4(1+gamma^2)] > 0.

Combining this gamma-sensitive observable with the generalized primordial
relation

    q = 1/gamma - gamma - Delta_gamma

makes (gamma, Delta_gamma) structurally identifiable, provided a same-realization
parameter map establishes that the area-metric gamma is the gamma entering q.

The direct duality-breaking estimator is

    Delta_gamma = 2 cot(8 psi) - q.

This fixture tests those identities and the Jacobian-rank statement. It is not a
detector-sensitivity forecast.
"""

from __future__ import annotations

import math
import numpy as np


def psi_from_gamma(gamma: float) -> float:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    xi = 0.5 * math.asinh(1.0 / gamma)
    return -0.5 * math.atan(math.tanh(xi))


def gamma_from_psi(psi: float) -> float:
    if not (-math.pi / 8.0 < psi < 0.0):
        raise ValueError("positive-gamma branch requires -pi/8 < psi < 0")
    return -1.0 / math.tan(4.0 * psi)


def dpsi_dgamma(gamma: float) -> float:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return 1.0 / (4.0 * (1.0 + gamma**2))


def q_from_gamma_delta(gamma: float, delta_gamma: float) -> float:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return 1.0 / gamma - gamma - delta_gamma


def delta_from_q_psi(q: float, psi: float) -> float:
    """Direct Delta estimator after same-parameter identity is established."""
    gamma = gamma_from_psi(psi)
    return 1.0 / gamma - gamma - q


def delta_from_q_psi_closed(q: float, psi: float) -> float:
    """Equivalent closed form: Delta = 2 cot(8 psi) - q."""
    if not (-math.pi / 8.0 < psi < 0.0):
        raise ValueError("positive-gamma branch requires -pi/8 < psi < 0")
    return 2.0 / math.tan(8.0 * psi) - q


def joint_jacobian(gamma: float) -> np.ndarray:
    """Jacobian of (q, psi) wrt (gamma, Delta_gamma)."""
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return np.array(
        [
            [-1.0 - 1.0 / gamma**2, -1.0],
            [dpsi_dgamma(gamma), 0.0],
        ],
        dtype=float,
    )


def run_self_test() -> None:
    # Exact roundtrip between gamma and the birefringence-axis angle.
    for gamma in (0.01, 0.05, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0):
        psi = psi_from_gamma(gamma)
        recovered = gamma_from_psi(psi)
        if not math.isclose(recovered, gamma, rel_tol=1e-11, abs_tol=1e-12):
            raise AssertionError(("gamma/psi roundtrip", gamma, psi, recovered))

        # Finite-difference derivative control.
        eps = max(1e-8, gamma * 1e-6)
        num = (psi_from_gamma(gamma + eps) - psi_from_gamma(max(gamma - eps, gamma * 0.5))) / (
            (gamma + eps) - max(gamma - eps, gamma * 0.5)
        )
        ana = dpsi_dgamma(gamma)
        if not math.isclose(num, ana, rel_tol=2e-5, abs_tol=2e-8):
            raise AssertionError(("derivative", gamma, num, ana))

    # Joint q+psi structural identifiability and exact determinant.
    for gamma in (0.05, 0.1, 0.3, 1.0, 3.0, 10.0):
        j = joint_jacobian(gamma)
        det = float(np.linalg.det(j))
        expected = dpsi_dgamma(gamma)
        if not math.isclose(det, expected, rel_tol=1e-12, abs_tol=1e-12):
            raise AssertionError(("jacobian determinant", gamma, det, expected))
        if np.linalg.matrix_rank(j) != 2:
            raise AssertionError(("joint rank", gamma, j))

    # Direct Delta reconstruction.
    for gamma in (0.05, 0.2, 0.7, 1.0, 2.0, 8.0):
        psi = psi_from_gamma(gamma)
        for delta in (-0.4, -0.05, 0.0, 0.07, 0.5):
            q = q_from_gamma_delta(gamma, delta)
            d1 = delta_from_q_psi(q, psi)
            d2 = delta_from_q_psi_closed(q, psi)
            if not math.isclose(d1, delta, rel_tol=1e-11, abs_tol=1e-11):
                raise AssertionError(("delta reconstruction", gamma, delta, q, psi, d1))
            if not math.isclose(d2, delta, rel_tol=1e-11, abs_tol=1e-11):
                raise AssertionError(("closed delta reconstruction", gamma, delta, d2))

    # Conditioning warning: sensitivity to gamma decreases for large gamma but
    # never vanishes at finite positive gamma.
    if not dpsi_dgamma(100.0) > 0.0:
        raise AssertionError("finite positive gamma must remain structurally identifiable")
    if not dpsi_dgamma(100.0) < dpsi_dgamma(1.0):
        raise AssertionError("large-gamma angle should be more weakly conditioned")

    print("PASS: area-metric birefringence gamma identifiability reference")
    print("gamma = -cot(4 psi) on the positive-gamma branch")
    print("det d(q,psi)/d(gamma,Delta) = 1/[4(1+gamma^2)] > 0")
    print("Delta_gamma = 2 cot(8 psi) - q")
    print("large gamma remains structurally identifiable but becomes poorly conditioned")


if __name__ == "__main__":
    run_self_test()
