"""Reference control for RG preservation of the LQG gamma-duality surface.

KMQGB Iter175.

Let
    rho = 2 f_GB / f_CS
    h(gamma) = gamma - 1/gamma
    Delta = rho - h(gamma)

The gamma-dual surface Delta=0 is preserved by an RG flow only when the beta
vector is tangent to that surface:

    beta_Delta = beta_rho - (1 + 1/gamma**2) beta_gamma = 0.

If the Wilson coefficients are nonzero and beta_E = eta_E f_GB,
beta_O = eta_O f_CS, then on Delta=0 this becomes

    h(gamma) (eta_E - eta_O)
      = (1 + 1/gamma**2) beta_gamma.

This fixture checks the exact identities and negative controls. It does not
assume any particular EPRL or area-metric coarse-graining beta functions.
"""

from __future__ import annotations

import math


def h(gamma: float) -> float:
    if gamma == 0.0:
        raise ValueError("gamma must be nonzero")
    return gamma - 1.0 / gamma


def h_prime(gamma: float) -> float:
    if gamma == 0.0:
        raise ValueError("gamma must be nonzero")
    return 1.0 + 1.0 / gamma**2


def delta_from_coefficients(gamma: float, f_gb: float, f_cs: float) -> float:
    if f_cs == 0.0:
        raise ValueError("f_cs must be nonzero")
    return 2.0 * f_gb / f_cs - h(gamma)


def beta_delta_direct(
    gamma: float,
    f_gb: float,
    f_cs: float,
    beta_gamma: float,
    beta_gb: float,
    beta_cs: float,
) -> float:
    if f_cs == 0.0:
        raise ValueError("f_cs must be nonzero")
    beta_rho = 2.0 * (beta_gb * f_cs - f_gb * beta_cs) / f_cs**2
    return beta_rho - h_prime(gamma) * beta_gamma


def beta_delta_multiplicative(
    gamma: float,
    beta_gamma: float,
    eta_gb: float,
    eta_cs: float,
) -> float:
    """beta_Delta evaluated on Delta=0 for multiplicative coefficient flows."""
    return h(gamma) * (eta_gb - eta_cs) - h_prime(gamma) * beta_gamma


def required_eta_difference(gamma: float, beta_gamma: float) -> float:
    """Required eta_GB-eta_CS for tangency away from gamma^2=1."""
    hg = h(gamma)
    if math.isclose(hg, 0.0, abs_tol=1e-15):
        raise ValueError("multiplicative ratio form is singular at gamma^2=1")
    return h_prime(gamma) * beta_gamma / hg


def duality_map(gamma: float, rho: float) -> tuple[float, float]:
    """Small/large-gamma involution compatible with rho=h(gamma)."""
    if gamma == 0.0:
        raise ValueError("gamma must be nonzero")
    return 1.0 / gamma, -rho


def run_self_test() -> None:
    # The gamma-dual constraint is equivariant under gamma -> 1/gamma,
    # rho -> -rho because h(1/gamma) = -h(gamma).
    for gamma in (0.1, 0.25, 0.5, 2.0, 4.0, 10.0):
        rho = h(gamma)
        gamma2, rho2 = duality_map(gamma, rho)
        if not math.isclose(rho2, h(gamma2), rel_tol=1e-13, abs_tol=1e-13):
            raise AssertionError(("duality equivariance", gamma, rho, gamma2, rho2))

    # Tangent multiplicative flows: choose eta difference from the exact condition.
    for gamma in (0.2, 0.5, 2.0, 5.0):
        for beta_gamma in (-0.03, 0.0, 0.07):
            eta_diff = required_eta_difference(gamma, beta_gamma)
            residual = beta_delta_multiplicative(gamma, beta_gamma, eta_diff, 0.0)
            if not math.isclose(residual, 0.0, rel_tol=1e-12, abs_tol=1e-12):
                raise AssertionError(("tangent flow", gamma, beta_gamma, residual))

    # Negative control: equal anomalous scaling does NOT preserve duality when gamma runs.
    for gamma in (0.2, 0.5, 2.0, 5.0):
        residual = beta_delta_multiplicative(gamma, 0.05, 0.02, 0.02)
        expected = -h_prime(gamma) * 0.05
        if not math.isclose(residual, expected, rel_tol=1e-12, abs_tol=1e-12):
            raise AssertionError(("running gamma negative control", gamma, residual, expected))
        if math.isclose(residual, 0.0, abs_tol=1e-12):
            raise AssertionError(("unexpected tangency", gamma))

    # If gamma is fixed, equal fractional running of GB and CS is sufficient.
    for gamma in (0.2, 0.5, 2.0, 5.0):
        residual = beta_delta_multiplicative(gamma, 0.0, -0.04, -0.04)
        if not math.isclose(residual, 0.0, abs_tol=1e-12):
            raise AssertionError(("fixed gamma common scaling", gamma, residual))

    # Direct gamma=1 gate: on Delta=0 we have f_GB=0 for finite nonzero f_CS.
    # Tangency requires 2 beta_GB/f_CS = 2 beta_gamma, i.e. beta_GB/f_CS=beta_gamma.
    gamma = 1.0
    f_cs = 3.0
    f_gb = 0.0
    beta_gamma = 0.07
    beta_gb = f_cs * beta_gamma
    beta_cs = -0.4
    residual = beta_delta_direct(gamma, f_gb, f_cs, beta_gamma, beta_gb, beta_cs)
    if not math.isclose(residual, 0.0, rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError(("gamma=1 direct tangency", residual))

    # Negative control at gamma=1.
    bad = beta_delta_direct(gamma, f_gb, f_cs, beta_gamma, 0.0, beta_cs)
    if math.isclose(bad, 0.0, abs_tol=1e-12):
        raise AssertionError("gamma=1 non-tangent negative control failed")

    print("PASS: LQG gamma-duality RG tangency reference")
    print("constraint equivariant under (gamma,rho)->(1/gamma,-rho)")
    print("Delta=0 preserved iff beta_Delta=0")
    print("running gamma requires matched relative GB/CS running")
    print("gamma=1 handled by direct, non-multiplicative tangency condition")


if __name__ == "__main__":
    run_self_test()
