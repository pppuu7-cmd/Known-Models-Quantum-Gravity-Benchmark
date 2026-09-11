"""Independent NumPy implementation of the declared RQCP fixed-band kernel.

This module is deliberately small and does not import the upstream RQCP code.
It reproduces the published two-mode Hamiltonian formulas for prospective
robustness probes only. It does not extend the external claim boundary or turn
a fixed-band diagnostic into family-level quantum-gravity evidence.
"""
from __future__ import annotations

import math
from functools import lru_cache

import numpy as np

BOX_LENGTH = 2.0 * math.pi
VOLUME = BOX_LENGTH**3
MASS_SQUARED = 0.24837697994841412
QUARTIC = 1.1614764267539648


@lru_cache(maxsize=None)
def operators(cutoff: int) -> tuple[np.ndarray, ...]:
    cutoff = int(cutoff)
    if cutoff < 3:
        raise ValueError("cutoff must be >= 3")
    annihilation = np.zeros((cutoff, cutoff), dtype=complex)
    for occupation in range(1, cutoff):
        annihilation[occupation - 1, occupation] = math.sqrt(occupation)
    creation = annihilation.conj().T
    q = (annihilation + creation) / math.sqrt(2.0)
    p = 1j * (creation - annihilation) / math.sqrt(2.0)
    ident = np.eye(cutoff, dtype=complex)
    q0 = np.kron(q, ident)
    q1 = np.kron(ident, q)
    p0 = np.kron(p, ident)
    p1 = np.kron(ident, p)
    return q0, q1, p0, p1


def hamiltonian(
    cutoff: int,
    *,
    quartic_value: float = QUARTIC,
    scale_factor: float = 1.0,
    source: float = 0.0,
    s: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    q0, q1, p0, p1 = operators(int(cutoff))
    p2 = p0 @ p0 + p1 @ p1
    q2 = q0 @ q0 + q1 @ q1
    q0sq = q0 @ q0
    q1sq = q1 @ q1
    q4 = q0sq @ q0sq + 6.0 * q0sq @ q1sq + 1.5 * q1sq @ q1sq
    a = float(scale_factor)
    H = (
        0.5 * a**-3 * p2
        + 0.5 * a**3 * MASS_SQUARED * q2
        + 0.5 * a * float(s) * q1sq
        + float(quartic_value) * a**3 / (math.factorial(4) * VOLUME) * q4
        - float(source) * q0
    )
    return H, q0


def spectral_geometry(cutoff: int, *, quartic_value: float = QUARTIC) -> dict[str, float]:
    H, _ = hamiltonian(cutoff, quartic_value=quartic_value)
    q0, q1, p0, p1 = operators(int(cutoff))
    p2 = p0 @ p0 + p1 @ p1
    q2 = q0 @ q0 + q1 @ q1
    q0sq = q0 @ q0
    q1sq = q1 @ q1
    q4 = q0sq @ q0sq + 6.0 * q0sq @ q1sq + 1.5 * q1sq @ q1sq

    energies, vectors = np.linalg.eigh(H)
    first = (
        -1.5 * p2
        + 1.5 * MASS_SQUARED * q2
        + 0.5 * q1sq
        + 3.0 * float(quartic_value) / (math.factorial(4) * VOLUME) * q4
    )
    second = (
        4.5 * p2
        + 4.5 * MASS_SQUARED * q2
        + 0.5 * q1sq
        + 9.0 * float(quartic_value) / (math.factorial(4) * VOLUME) * q4
    )
    transformed = vectors.conj().T @ first @ vectors
    gaps = energies[1:] - energies[0]
    if float(np.min(gaps)) <= 0.0:
        raise ValueError("ground state must be simple and gapped")
    weights = np.abs(transformed[0, 1:]) ** 2
    contact = float((vectors[:, 0].conj() @ second @ vectors[:, 0]).real)
    static = contact - 2.0 * float(np.sum(weights / gaps))
    kinetic = 2.0 * float(np.sum(weights / gaps**3))
    fourth = -2.0 * float(np.sum(weights / gaps**5))
    curvature = kinetic / (12.0 * VOLUME)
    newton = 1.0 / (16.0 * math.pi * curvature)
    gap = float(energies[1] - energies[0])
    return {
        "cutoff": int(cutoff),
        "hilbert_dimension": int(cutoff) ** 2,
        "quartic": float(quartic_value),
        "ground_energy": float(energies[0]),
        "mass_gap": gap,
        "static_geometry_kernel": static,
        "geometry_kinetic_coefficient_B": kinetic,
        "geometry_four_derivative_coefficient": fourth,
        "Einstein_Hilbert_coefficient_C_R": curvature,
        "Newton_response_G": newton,
        "dimensionless_gravity_number_G_gap2": newton * gap**2,
    }


def ground_energy_source_derivatives(
    H: np.ndarray,
    source_operator: np.ndarray,
    maximum_order: int = 2,
) -> tuple[float, ...]:
    energies, vectors = np.linalg.eigh(H)
    gaps = energies[1:] - energies[0]
    if float(np.min(gaps)) <= 0.0:
        raise ValueError("source derivatives require a simple gapped ground state")
    perturbation = vectors.conj().T @ source_operator @ vectors
    coefficients = [np.eye(len(energies), dtype=complex)[:, 0]]
    energy_coefficients: list[complex] = [complex(energies[0])]
    for order in range(1, int(maximum_order) + 1):
        energy_coefficient = complex((perturbation @ coefficients[order - 1])[0])
        rhs = -perturbation @ coefficients[order - 1]
        for lower_order in range(1, order):
            rhs += energy_coefficients[lower_order] * coefficients[order - lower_order]
        state = np.zeros(len(energies), dtype=complex)
        state[1:] = rhs[1:] / gaps
        coefficients.append(state)
        energy_coefficients.append(energy_coefficient)
    output = []
    for order, coefficient in enumerate(energy_coefficients):
        value = math.factorial(order) * coefficient
        if abs(value.imag) > 1.0e-10:
            raise ValueError("source derivative acquired a nonreal component")
        output.append(float(value.real))
    return tuple(output)


def mixed_response(
    cutoff: int,
    *,
    quartic_value: float = QUARTIC,
    sigma_step: float = 1.0e-3,
) -> dict[str, float]:
    step = float(sigma_step)
    if step <= 0.0:
        raise ValueError("sigma_step must be positive")

    def second_at_scale(scale: float) -> float:
        H, q0 = hamiltonian(
            cutoff,
            quartic_value=quartic_value,
            scale_factor=scale,
        )
        return ground_energy_source_derivatives(H, -q0, maximum_order=2)[2]

    def centered(h: float) -> float:
        return (
            second_at_scale(math.exp(h))
            - second_at_scale(math.exp(-h))
        ) / (2.0 * h)

    coarse = centered(step)
    fine = centered(0.5 * step)
    richardson = (4.0 * fine - coarse) / 3.0
    return {
        "cutoff": int(cutoff),
        "quartic": float(quartic_value),
        "sigma_step": step,
        "coarse_centered": coarse,
        "fine_centered": fine,
        "mixed_geometry_matter_response": richardson,
        "Richardson_error_estimate": abs(fine - coarse) / 3.0,
    }
