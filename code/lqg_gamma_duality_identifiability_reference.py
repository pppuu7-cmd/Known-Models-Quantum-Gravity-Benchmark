#!/usr/bin/env python3
"""Exact structural-identifiability control for the LQG gamma-duality relation.

This is a methodology/reference test, not a data fit and not evidence that the
microscopic EPRL -> EFT bridge is closed.
"""

from math import pi, sqrt, isclose


def q_from_gamma(gamma: float) -> float:
    assert gamma > 0.0
    return 1.0 / gamma - gamma


def gamma_from_q(q: float) -> float:
    # Unique positive root of gamma^2 + q gamma - 1 = 0.
    return (sqrt(q * q + 4.0) - q) / 2.0


def q_from_observables(r: float, n_t: float, pol: float) -> float:
    if pol == 0.0:
        raise ZeroDivisionError("Pi=0: gamma-duality observable channel is not identifiable")
    return (pi / 8.0) * (r + 8.0 * n_t) / pol


def main() -> None:
    # Exact invertibility over representative positive gamma values.
    for gamma in (0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 10.0):
        q = q_from_gamma(gamma)
        recovered = gamma_from_q(q)
        assert isclose(recovered, gamma, rel_tol=1e-12, abs_tol=1e-12), (gamma, q, recovered)

    # Monotonicity dq/dgamma = -1/gamma^2 - 1 < 0 implies uniqueness.
    grid = (0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 10.0)
    qs = [q_from_gamma(g) for g in grid]
    assert all(qs[i] > qs[i + 1] for i in range(len(qs) - 1))

    # Construct a synthetic observable triple satisfying the relation exactly.
    gamma = 0.25
    q = q_from_gamma(gamma)
    r = 0.01
    n_t = -0.001
    # Solve Pi from q=(pi/8)(r+8 n_t)/Pi.
    pol = (pi / 8.0) * (r + 8.0 * n_t) / q
    q_obs = q_from_observables(r, n_t, pol)
    assert isclose(q_obs, q, rel_tol=1e-12, abs_tol=1e-12)
    assert isclose(gamma_from_q(q_obs), gamma, rel_tol=1e-12, abs_tol=1e-12)

    # Required negative control: Pi=0 does not identify gamma.
    try:
        q_from_observables(r=0.01, n_t=-0.00125, pol=0.0)
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("Pi=0 negative control failed")

    print("gamma_duality_structural_identifiability=PASS")
    print("positive_gamma_solution_unique=True")
    print("Pi_zero_channel=NON_IDENTIFIABLE")


if __name__ == "__main__":
    main()
