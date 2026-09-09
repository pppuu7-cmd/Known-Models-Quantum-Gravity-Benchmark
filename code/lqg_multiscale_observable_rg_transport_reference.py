"""Observable-space RG transport control for the LQG/area-metric gamma route.

KMQGB Iter177.

On the positive-gamma area-metric branch,

    gamma = -cot(4 psi)
    F(psi) := 2 cot(8 psi) = 1/gamma - gamma

and the generalized primordial relation is

    Delta_gamma = F(psi) - q.

For RG scale t=ln(mu), therefore

    beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q.

Using

    beta_psi = beta_gamma / [4(1+gamma^2)],

this is exactly equivalent to

    beta_Delta = -(1+1/gamma^2) beta_gamma - beta_q,

which matches q = 1/gamma - gamma - Delta_gamma.

If ideal gamma-duality is RG preserved (beta_Delta=0), the observable-space
transport condition is

    beta_q + 16 csc^2(8 psi) beta_psi = 0.

This fixture checks the algebraic equivalence, direct finite-step reconstruction,
and negative controls. It is a matching/transport reference, not a detector forecast.
"""

from __future__ import annotations

import math


def gamma_from_psi(psi: float) -> float:
    if not (-math.pi / 8.0 < psi < 0.0):
        raise ValueError("positive-gamma branch requires -pi/8 < psi < 0")
    return -1.0 / math.tan(4.0 * psi)


def psi_from_gamma(gamma: float) -> float:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return -0.25 * math.atan(1.0 / gamma)


def f_of_psi(psi: float) -> float:
    if not (-math.pi / 8.0 < psi < 0.0):
        raise ValueError("positive-gamma branch requires -pi/8 < psi < 0")
    return 2.0 / math.tan(8.0 * psi)


def beta_psi_from_beta_gamma(gamma: float, beta_gamma: float) -> float:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return beta_gamma / (4.0 * (1.0 + gamma**2))


def beta_delta_observable(psi: float, beta_psi: float, beta_q: float) -> float:
    s = math.sin(8.0 * psi)
    return -16.0 * beta_psi / (s * s) - beta_q


def beta_delta_gamma_space(gamma: float, beta_gamma: float, beta_q: float) -> float:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return -(1.0 + 1.0 / gamma**2) * beta_gamma - beta_q


def required_beta_q_for_ideal_transport(psi: float, beta_psi: float) -> float:
    s = math.sin(8.0 * psi)
    return -16.0 * beta_psi / (s * s)


def run_self_test() -> None:
    # Closed-form identities between psi and gamma.
    for gamma in (0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 50.0):
        psi = psi_from_gamma(gamma)
        recovered = gamma_from_psi(psi)
        if not math.isclose(recovered, gamma, rel_tol=1e-12, abs_tol=1e-12):
            raise AssertionError(("roundtrip", gamma, psi, recovered))
        expected_f = 1.0 / gamma - gamma
        if not math.isclose(f_of_psi(psi), expected_f, rel_tol=1e-12, abs_tol=1e-12):
            raise AssertionError(("F identity", gamma, psi, f_of_psi(psi), expected_f))

    # Observable-space beta_Delta must equal gamma-space beta_Delta identically.
    for gamma in (0.05, 0.2, 0.7, 1.0, 2.0, 8.0):
        psi = psi_from_gamma(gamma)
        for beta_gamma in (-0.06, 0.0, 0.09):
            beta_psi = beta_psi_from_beta_gamma(gamma, beta_gamma)
            for beta_q in (-0.13, 0.0, 0.11):
                b_obs = beta_delta_observable(psi, beta_psi, beta_q)
                b_gam = beta_delta_gamma_space(gamma, beta_gamma, beta_q)
                if not math.isclose(b_obs, b_gam, rel_tol=1e-11, abs_tol=1e-11):
                    raise AssertionError(("beta equivalence", gamma, beta_gamma, beta_q, b_obs, b_gam))

    # Ideal-duality transport condition gives beta_Delta=0 exactly.
    for gamma in (0.1, 0.5, 1.0, 4.0):
        psi = psi_from_gamma(gamma)
        beta_gamma = 0.04
        beta_psi = beta_psi_from_beta_gamma(gamma, beta_gamma)
        beta_q = required_beta_q_for_ideal_transport(psi, beta_psi)
        residual = beta_delta_observable(psi, beta_psi, beta_q)
        if not math.isclose(residual, 0.0, rel_tol=1e-12, abs_tol=1e-12):
            raise AssertionError(("ideal transport", gamma, residual))

    # Negative control: if q is frozen while gamma/psi runs, ideal duality breaks.
    for gamma in (0.1, 0.5, 2.0, 6.0):
        psi = psi_from_gamma(gamma)
        beta_psi = beta_psi_from_beta_gamma(gamma, 0.03)
        residual = beta_delta_observable(psi, beta_psi, 0.0)
        if math.isclose(residual, 0.0, abs_tol=1e-12):
            raise AssertionError(("frozen-q negative control", gamma))

    # Finite-step consistency: Delta = F(psi)-q is exact at each endpoint.
    gamma0, delta0 = 0.6, 0.08
    gamma1, delta1 = 0.9, -0.03
    psi0, psi1 = psi_from_gamma(gamma0), psi_from_gamma(gamma1)
    q0 = 1.0 / gamma0 - gamma0 - delta0
    q1 = 1.0 / gamma1 - gamma1 - delta1
    rec0 = f_of_psi(psi0) - q0
    rec1 = f_of_psi(psi1) - q1
    if not math.isclose(rec0, delta0, rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError(("finite endpoint 0", rec0, delta0))
    if not math.isclose(rec1, delta1, rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError(("finite endpoint 1", rec1, delta1))

    print("PASS: multiscale observable RG transport reference")
    print("Delta_gamma = 2 cot(8 psi) - q")
    print("beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q")
    print("ideal duality transport: beta_q + 16 csc^2(8 psi) beta_psi = 0")


if __name__ == "__main__":
    run_self_test()
