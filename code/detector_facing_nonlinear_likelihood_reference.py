"""KMQGB detector-facing nonlinear likelihood regression.

Methodology/reference code, not a Candidate Gravity model.

This ports the essential source-traceable RQIR Paper-III detector closure into a
small NumPy-only CI fixture.  It uses the physical phase-covariance construction
from ``detector_visible_residual_physical_covariance_reference.py`` and propagates
it through the measured atom-interferometer probability

    P = 1/2 [1 + C cos(Phi)]

with simultaneous phase, contrast and centered-readout nuisance profiling.

Source anchors inherited from the external audit:
- sigma_P ~= 3e-4 probability technical detection floor;
- sigma_phi = 2 sigma_P/C;
- near-1-mrad/shot detection sensitivity -> effective C ~= 0.6;
- same source-traceable SYRTE Fig.-8 colored phase covariance.

The covariance is frozen at each nominal/stress point and Fisher information is
computed from mean derivatives only, avoiding artificial information from
parameter-dependent noise covariance.
"""

from __future__ import annotations

from functools import lru_cache
import math
import numpy as np

from detector_visible_residual_physical_covariance_reference import (
    K_G,
    TC,
    REFERENCE_UG,
    SCIENCE_F_HZ,
    REFERENCE_F_HZ,
    accel_response,
    dense_toeplitz,
    total_covariance_lags,
)

SIGMA_P = 3.0e-4
DETECTION_PHASE_TARGET = 1.0e-3
C0 = 2.0 * SIGMA_P / DETECTION_PHASE_TARGET  # 0.6


def templates(nshot: int, science_modulated: bool = True) -> tuple[np.ndarray, ...]:
    t = np.arange(nshot, dtype=float) * TC
    x = np.linspace(-1.0, 1.0, nshot)
    if science_modulated:
        science = np.sin(2.0 * math.pi * SCIENCE_F_HZ * t)
        science *= float(accel_response(SCIENCE_F_HZ))
    else:
        science = np.ones(nshot)
    reference = np.sin(2.0 * math.pi * REFERENCE_F_HZ * t + 0.37)
    reference *= float(accel_response(REFERENCE_F_HZ))
    return x, science, reference


def detector_mean_jacobian(
    nshot: int,
    *,
    theta_ng: float = 1.0,
    alpha_ug: float = REFERENCE_UG,
    science_modulated: bool = True,
    use_reference: bool = True,
    reference_unknown: bool = True,
    gamma: float = 0.0,
    phase_offset: float = 0.0,
    phase_linear: float = 0.0,
    phase_quadratic: float = 0.0,
    contrast: float = C0,
    contrast_linear: float = 0.0,
    contrast_quadratic: float = 0.0,
    read_gain: float = 0.0,
    read_gain_linear: float = 0.0,
    read_offset: float = 0.0,
) -> tuple[np.ndarray, tuple[str, ...], np.ndarray]:
    x, science, reference = templates(nshot, science_modulated)
    if not use_reference:
        reference = np.zeros_like(reference)
        alpha_ug = 0.0

    theta_g = theta_ng * 1.0e-9
    alpha_g = alpha_ug * 1.0e-6

    physical_phase = K_G * (1.0 + gamma) * (
        theta_g * science + alpha_g * reference
    )
    phase = (
        math.pi / 2.0
        + physical_phase
        + phase_offset
        + phase_linear * x
        + phase_quadratic * x**2
    )

    contrast_shape = 1.0 + contrast_linear * x + contrast_quadratic * x**2
    shot_contrast = contrast * contrast_shape
    gain = 1.0 + read_gain + read_gain_linear * x

    fringe = 0.5 + 0.5 * shot_contrast * np.cos(phase)
    _mean = 0.5 + read_offset + gain * (fringe - 0.5)

    slope = -0.5 * gain * shot_contrast * np.sin(phase)
    trig = np.cos(phase)

    theta_column = slope * K_G * (1.0 + gamma) * 1.0e-9 * science
    gamma_column = slope * K_G * (theta_g * science + alpha_g * reference)

    columns = [
        theta_column,
        gamma_column,
        slope,
        slope * x,
        slope * x**2,
        gain * 0.5 * contrast_shape * trig,
        gain * 0.5 * contrast * x * trig,
        gain * 0.5 * contrast * x**2 * trig,
        fringe - 0.5,
        x * (fringe - 0.5),
        np.ones(nshot),
    ]
    names = [
        "theta_ng",
        "gamma",
        "phase_offset",
        "phase_linear",
        "phase_quadratic",
        "contrast",
        "contrast_linear",
        "contrast_quadratic",
        "read_gain",
        "read_gain_linear",
        "read_offset",
    ]

    if reference_unknown:
        alpha_column = slope * K_G * (1.0 + gamma) * 1.0e-6 * reference
        columns.append(alpha_column)
        names.append("alpha_ug")

    return np.column_stack(columns), tuple(names), slope


@lru_cache(maxsize=4)
def phase_covariance(nshot: int) -> np.ndarray:
    return dense_toeplitz(total_covariance_lags(nshot))


def detector_fisher(
    seconds: float = 60.0,
    *,
    reference_prior_fraction: float | None = None,
    **mean_kwargs,
) -> tuple[np.ndarray, tuple[str, ...]]:
    nshot = int(round(seconds / TC))
    jacobian, names, slope = detector_mean_jacobian(nshot, **mean_kwargs)

    cphi = phase_covariance(nshot)
    probability_covariance = (
        slope[:, None] * cphi * slope[None, :]
        + SIGMA_P**2 * np.eye(nshot)
    )

    cinv_j = np.linalg.solve(probability_covariance, jacobian)
    fisher = jacobian.T @ cinv_j
    fisher = 0.5 * (fisher + fisher.T)

    if reference_prior_fraction is not None:
        if "alpha_ug" not in names:
            raise ValueError("reference prior requested without alpha_ug nuisance")
        if reference_prior_fraction <= 0.0:
            raise ValueError("reference prior must be positive")
        i = names.index("alpha_ug")
        sigma_alpha = REFERENCE_UG * reference_prior_fraction
        fisher[i, i] += 1.0 / sigma_alpha**2

    return fisher, names


def estimability(fisher: np.ndarray, names: tuple[str, ...]) -> dict[str, object]:
    diagonal = np.sqrt(np.clip(np.diag(fisher), 1.0e-300, None))
    scale = np.diag(1.0 / diagonal)
    normalized = scale @ fisher @ scale
    normalized = 0.5 * (normalized + normalized.T)

    eigenvalues, eigenvectors = np.linalg.eigh(normalized)
    positive = eigenvalues > 1.0e-8
    null_vectors = eigenvectors[:, ~positive]

    theta_index = names.index("theta_ng")
    theta_overlap = (
        float(np.linalg.norm(null_vectors[theta_index, :]))
        if null_vectors.shape[1]
        else 0.0
    )
    theta_estimable = theta_overlap < 1.0e-6

    if theta_estimable:
        covariance = scale @ np.linalg.pinv(normalized, rcond=1.0e-8) @ scale
        sigma_theta = math.sqrt(
            max(float(covariance[theta_index, theta_index]), 0.0)
        )
    else:
        sigma_theta = math.inf

    return {
        "rank": int(np.sum(positive)),
        "dimension": int(fisher.shape[0]),
        "nullity": int(fisher.shape[0] - np.sum(positive)),
        "theta_estimable": bool(theta_estimable),
        "theta_null_overlap": theta_overlap,
        "sigma_theta_ng": sigma_theta,
    }


def campaign(
    seconds: float = 60.0,
    *,
    reference_prior_fraction: float | None = None,
    **mean_kwargs,
) -> dict[str, object]:
    fisher, names = detector_fisher(
        seconds,
        reference_prior_fraction=reference_prior_fraction,
        **mean_kwargs,
    )
    out = estimability(fisher, names)
    out["shots"] = int(round(seconds / TC))
    return out


def calibration_floor_scan(theta_ng: float = 100.0) -> list[dict[str, float]]:
    statistical = float(
        campaign(
            theta_ng=theta_ng,
            reference_unknown=True,
            reference_prior_fraction=1.0e-6,
        )["sigma_theta_ng"]
    )
    rows = []
    for fraction in (0.10, 0.03, 0.01, 0.003, 0.001):
        measured = float(
            campaign(
                theta_ng=theta_ng,
                reference_unknown=True,
                reference_prior_fraction=fraction,
            )["sigma_theta_ng"]
        )
        predicted = math.sqrt(statistical**2 + (theta_ng * fraction) ** 2)
        rows.append(
            {
                "fraction": fraction,
                "measured_sigma_theta_ng": measured,
                "quadrature_prediction_ng": predicted,
                "relative_error": abs(measured / predicted - 1.0),
            }
        )
    return rows


def structural_assertions() -> None:
    assert abs(C0 - 0.6) < 1.0e-12
    assert abs(2.0 * SIGMA_P / C0 - 1.0e-3) < 1.0e-15

    # Required negative controls.
    static = campaign(
        science_modulated=False,
        use_reference=True,
        reference_unknown=True,
        reference_prior_fraction=0.01,
    )
    assert not static["theta_estimable"]

    no_reference = campaign(
        science_modulated=True,
        use_reference=False,
        reference_unknown=False,
    )
    assert not no_reference["theta_estimable"]

    free_reference = campaign(
        science_modulated=True,
        use_reference=True,
        reference_unknown=True,
        reference_prior_fraction=None,
    )
    assert not free_reference["theta_estimable"]

    # Calibrated reference restores science estimability even though detector-only
    # contrast/readout null modes may remain.
    for fraction in (0.10, 0.01, 0.001):
        result = campaign(
            science_modulated=True,
            use_reference=True,
            reference_unknown=True,
            reference_prior_fraction=fraction,
        )
        assert result["theta_estimable"]
        assert result["rank"] < result["dimension"]
        assert math.isfinite(float(result["sigma_theta_ng"]))

    known_reference = campaign(
        science_modulated=True,
        use_reference=True,
        reference_unknown=False,
    )
    assert known_reference["theta_estimable"]
    # Reproduce the external 60-s detector-facing scale to a conservative 2%.
    assert abs(float(known_reference["sigma_theta_ng"]) / 5.73 - 1.0) < 0.02

    # Detector-state stress inside the source-described mid-fringe regime.
    stresses = [
        {"contrast": 0.48},
        {"contrast_linear": 0.10},
        {"contrast_quadratic": 0.10},
        {"read_gain_linear": 0.05},
        {"phase_offset": 0.20},
        {"phase_linear": 0.20},
        {
            "contrast": 0.48,
            "contrast_linear": 0.10,
            "contrast_quadratic": 0.05,
            "read_gain_linear": 0.05,
            "phase_offset": 0.15,
            "phase_linear": 0.10,
            "phase_quadratic": 0.05,
        },
    ]
    for stress in stresses:
        result = campaign(
            reference_unknown=True,
            reference_prior_fraction=0.01,
            **stress,
        )
        assert result["theta_estimable"]

    # The independently-prior-constrained reference creates the expected
    # irreducible calibration floor rather than unlimited 1/sqrt(N) scaling.
    for row in calibration_floor_scan(theta_ng=100.0):
        assert row["relative_error"] < 0.01


if __name__ == "__main__":
    structural_assertions()
    known = campaign(reference_unknown=False)
    calibrated = campaign(reference_unknown=True, reference_prior_fraction=0.01)
    print("effective_contrast", C0)
    print("known_reference_60s", known)
    print("calibrated_reference_60s", calibrated)
    print("calibration_floor_scan", calibration_floor_scan())
