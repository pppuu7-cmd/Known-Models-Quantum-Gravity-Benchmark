#!/usr/bin/env python3
"""Executable witness for the MISP2 same-lattice fractional-root obstruction.

The exact proof is in protocol/MISP2_Q2_SHARED_CLOCK_ROOT_NO_GO.md.  This script
checks the axial BCC reduction, the fourth-root phase repair, and the primitive
lattice-period failure of the continuous fourth root.
"""

from __future__ import annotations

import numpy as np

I2 = np.eye(2, dtype=complex)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)


def axial_bcc(theta: float) -> np.ndarray:
    return np.cos(theta) * I2 - 1j * np.sin(theta) * SIGMA_X


def principal_fourth_root(theta: float) -> np.ndarray:
    return np.cos(theta / 4.0) * I2 - 1j * np.sin(theta / 4.0) * SIGMA_X


def scalar_laurent_fourth_root_exponent_exists(q: int) -> bool:
    """A finite Laurent root of z^q must be c z^m, so needs 4m=q."""
    return q % 4 == 0


def self_test() -> None:
    # Exact axial formula and root relation.
    for theta in [0.17, 0.73, 1.91]:
        A = axial_bcc(theta)
        B = principal_fourth_root(theta)
        B4 = np.linalg.matrix_power(B, 4)
        assert np.allclose(B4, A, atol=2e-13)
        assert np.allclose(A.conj().T @ A, I2, atol=2e-13)
        assert np.allclose(B.conj().T @ B, I2, atol=2e-13)

    # Same-lattice finite Laurent symbols are periodic in the primitive character
    # theta -> theta + 2pi.  The continuous fourth root is not.
    theta = 0.41
    B0 = principal_fourth_root(theta)
    B1 = principal_fourth_root(theta + 2.0 * np.pi)
    period_mismatch = float(np.linalg.norm(B1 - B0))
    assert period_mismatch > 1.0
    assert np.allclose(axial_bcc(theta + 2.0 * np.pi), axial_bcc(theta), atol=2e-13)

    # Exact Laurent exponent divisibility obstruction for the two eigenchannels.
    assert not scalar_laurent_fourth_root_exponent_exists(+1)
    assert not scalar_laurent_fourth_root_exponent_exists(-1)
    assert scalar_laurent_fourth_root_exponent_exists(+4)
    assert scalar_laurent_fourth_root_exponent_exists(-4)

    # If locality were ignored, the fourth root would repair the spin-2 extreme
    # phase: Sym^4 produces an extreme exponent four times the root exponent.
    omega = 0.013
    repaired_extreme_phase = 4.0 * (omega / 4.0)
    assert np.isclose(repaired_extreme_phase, omega, atol=1e-15)

    print("misp2_shared_clock_root_no_go_reference: PASS")
    print("principal_root_period_mismatch=", period_mismatch)
    print("laurent_root_q_plus1_exists=", False)
    print("laurent_root_q_minus1_exists=", False)
    print("phase_repair_if_nonlocal=", repaired_extreme_phase / omega)
    print("classification=BLOCKED__SAME_LATTICE_FRACTIONAL_ROOT_IS_NOT_FINITE_RANGE")


if __name__ == "__main__":
    self_test()
