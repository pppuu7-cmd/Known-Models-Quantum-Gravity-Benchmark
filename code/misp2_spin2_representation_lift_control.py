#!/usr/bin/env python3
"""Exact free-sector MISP2 Q2 control.

Construct the + BCC Weyl automaton A(k), lift it to the spin-2 irrep through
Sym^4(C^2), and verify the exact unitary/eigenphase structure.  The physical
extreme m=±2 sectors inherit phases ±4*omega while the Weyl fundamental has
±omega on the same microscopic step.  Therefore the naive representation lift
fails the shared-clock/light-cone criterion by a factor four.

This is a control, not a Candidate Gravity parent.
"""

from __future__ import annotations

import itertools
import numpy as np

I2 = np.eye(2, dtype=complex)
SIGMA = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]


def bcc_weyl_plus(k: np.ndarray):
    """Return A_+(k), lambda(k), n(k) in the standard BCC convention."""
    k = np.asarray(k, dtype=float)
    c = np.cos(k / np.sqrt(3.0))
    s = np.sin(k / np.sqrt(3.0))
    cx, cy, cz = c
    sx, sy, sz = s

    n = np.array(
        [
            sx * cy * cz + cx * sy * sz,
            cx * sy * cz - sx * cy * sz,
            cx * cy * sz + sx * sy * cz,
        ],
        dtype=float,
    )
    lam = cx * cy * cz - sx * sy * sz
    A = lam * I2 - 1j * sum(n[i] * SIGMA[i] for i in range(3))
    return A, float(lam), n


def symmetric_dicke_isometry(n_qubits: int = 4) -> np.ndarray:
    """Columns are normalized Dicke states with excitation number r=0..n."""
    dim = 2**n_qubits
    cols = []
    for r in range(n_qubits + 1):
        v = np.zeros(dim, dtype=complex)
        indices = []
        for bits in itertools.product([0, 1], repeat=n_qubits):
            if sum(bits) != r:
                continue
            idx = 0
            for bit in bits:
                idx = 2 * idx + bit
            indices.append(idx)
        for idx in indices:
            v[idx] = 1.0 / np.sqrt(len(indices))
        cols.append(v)
    return np.column_stack(cols)


S4 = symmetric_dicke_isometry(4)


def tensor_power4(A: np.ndarray) -> np.ndarray:
    out = A
    for _ in range(3):
        out = np.kron(out, A)
    return out


def spin2_lift(A: np.ndarray) -> np.ndarray:
    return S4.conj().T @ tensor_power4(A) @ S4


def op_on_qubit(op: np.ndarray, q: int, n_qubits: int = 4) -> np.ndarray:
    ops = [I2.copy() for _ in range(n_qubits)]
    ops[q] = op
    out = ops[0]
    for item in ops[1:]:
        out = np.kron(out, item)
    return out


def collective_spin2_generators():
    """J_i on the symmetric four-spin-1/2 subspace (spin j=2)."""
    gens = []
    for sigma in SIGMA:
        full = sum(op_on_qubit(sigma, q) for q in range(4)) / 2.0
        gens.append(S4.conj().T @ full @ S4)
    return gens


J = collective_spin2_generators()


def sorted_principal_phases(U: np.ndarray) -> np.ndarray:
    return np.sort(np.angle(np.linalg.eigvals(U)))


def self_test() -> None:
    assert np.allclose(S4.conj().T @ S4, np.eye(5), atol=1e-13)

    # Generic BCC points: exact unitarity and spin-axis preservation.
    generic_points = [
        np.array([0.11, 0.03, -0.04]),
        np.array([0.21, -0.07, 0.05]),
        np.array([0.31, 0.12, 0.09]),
    ]
    for k in generic_points:
        A, lam, n = bcc_weyl_plus(k)
        U2 = spin2_lift(A)
        assert np.isclose(lam * lam + float(n @ n), 1.0, atol=1e-13)
        assert np.allclose(A.conj().T @ A, np.eye(2), atol=1e-13)
        assert np.allclose(U2.conj().T @ U2, np.eye(5), atol=2e-12)

        nhat = n / np.linalg.norm(n)
        Jn = sum(nhat[i] * J[i] for i in range(3))
        assert np.allclose(U2 @ Jn, Jn @ U2, atol=2e-12)
        assert np.allclose(np.linalg.eigvalsh(Jn), [-2, -1, 0, 1, 2], atol=2e-12)

    # Small momentum along one ray avoids phase wrapping.  The five Sym^4 phases
    # are -4w,-2w,0,+2w,+4w if the fundamental phases are -w,+w.
    eps_values = [1e-2, 1e-4, 1e-6]
    ratios = []
    phase_checks = []
    for eps in eps_values:
        A, _, _ = bcc_weyl_plus(np.array([eps, 0.0, 0.0]))
        U2 = spin2_lift(A)

        p1 = sorted_principal_phases(A)
        p2 = sorted_principal_phases(U2)
        w = float(p1[-1])
        expected = np.array([-4 * w, -2 * w, 0.0, 2 * w, 4 * w])
        assert np.allclose(p2, expected, atol=2e-12)

        ratio = float(p2[-1] / w)
        ratios.append(ratio)
        phase_checks.append((eps, w, float(p2[-1])))
        assert np.isclose(ratio, 4.0, atol=2e-9)

    # IR Weyl phase slope itself is |k|/sqrt(3) in this convention.
    eps = 1e-7
    A, _, _ = bcc_weyl_plus(np.array([eps, 0.0, 0.0]))
    w = sorted_principal_phases(A)[-1]
    weyl_slope = float(w / eps)
    assert np.isclose(weyl_slope, 1 / np.sqrt(3.0), rtol=1e-7, atol=1e-9)

    print("misp2_spin2_representation_lift_control: PASS")
    print("generic_unitarity_and_axis_preservation=PASS")
    print("phase_checks_(eps,w_spinhalf,w_spin2_extreme)=", phase_checks)
    print("spin2_to_weyl_phase_slope_ratios=", ratios)
    print("weyl_IR_slope=", weyl_slope)
    print("classification=FREE_SPIN2_CONTROL_PASS__SHARED_CLOCK_FAIL")


if __name__ == "__main__":
    self_test()
