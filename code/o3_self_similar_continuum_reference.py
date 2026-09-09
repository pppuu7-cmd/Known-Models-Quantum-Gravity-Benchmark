"""Executable witness for the self-similar continuum-kernel control.

The proof and interpretation are frozen in
protocol/O3_SELF_SIMILAR_CONTINUUM_KERNEL_CONTROL.md.
"""

from __future__ import annotations

import cmath
import math


def G(z: complex, m2: float, g: float) -> complex:
    x = z - m2
    root = cmath.sqrt(x * x - 4.0 * g * g)
    # Pick the branch continuously connected to root ~ x for large positive real x.
    # For the test points below this is the principal branch in the desired sheet.
    return (x - root) / (2.0 * g * g)


def rho(E: float, m2: float, g: float) -> float:
    x = E - m2
    inside = 4.0 * g * g - x * x
    if inside <= 0.0:
        return 0.0
    return math.sqrt(inside) / (2.0 * math.pi * g * g)


def trapz_density(m2: float, g: float, n: int = 200_000) -> float:
    lo = m2 - 2.0 * g
    hi = m2 + 2.0 * g
    h = (hi - lo) / n
    total = 0.5 * (rho(lo, m2, g) + rho(hi, m2, g))
    for i in range(1, n):
        total += rho(lo + i * h, m2, g)
    return total * h


def main() -> None:
    m2 = 1.7
    g = 0.43

    z = 5.0 + 0.2j
    gz = G(z, m2, g)
    residual = g * g * gz * gz - (z - m2) * gz + 1.0

    # Retarded boundary value inside the spectral band.
    E = m2 + 0.3 * g
    eps = 1e-10
    gr = G(E + 1j * eps, m2, g)
    rho_from_im = -gr.imag / math.pi
    rho_exact = rho(E, m2, g)

    norm = trapz_density(m2, g)

    print(f"quadratic_residual={abs(residual):.3e}")
    print(f"rho_from_im={rho_from_im:.12f}")
    print(f"rho_exact={rho_exact:.12f}")
    print(f"rho_abs_diff={abs(rho_from_im-rho_exact):.3e}")
    print(f"spectral_norm={norm:.12f}")

    if abs(residual) > 1e-11:
        raise SystemExit("self-similar resolvent identity failed")
    if abs(rho_from_im - rho_exact) > 1e-8:
        raise SystemExit("retarded spectral-density identity failed")
    if abs(norm - 1.0) > 2e-7:
        raise SystemExit("spectral density normalization failed")

    print("O3 self-similar continuum-kernel control: PASS")


if __name__ == "__main__":
    main()
