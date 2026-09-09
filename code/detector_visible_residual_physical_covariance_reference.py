"""KMQGB detector-visible residual certificate with source-traceable covariance.

This is methodology/reference code, not a Candidate Gravity model.

The physical covariance fixture is the coarse passive-platform Fig.-8 ASD
used by the external RQIR Paper-III audit, sourced to Le Gouet et al.,
Appl. Phys. B 92, 133-144 (2008), arXiv:0801.1270.  The knots are an
approximate human-readable digitization, not raw experimental data and are
not amplitude-fitted to the integrated sensitivity.

Core detector-visibility definition for a local science direction r:

    I0 = r^T C^-1 r
    Iprof = I0 - r^T C^-1 N (N^T C^-1 N + P)^+ N^T C^-1 r
    eta_det = sqrt(max(Iprof,0)/I0)

C is the detector covariance, N the nuisance tangent matrix, and P an
optional externally-authorized nuisance-prior precision matrix.
"""

from __future__ import annotations

import math
import numpy as np

G0 = 9.80665
LAMBDA = 780e-9
K_EFF = 4.0 * math.pi / LAMBDA
T = 0.050
TC = 0.250
K_G = K_EFF * T**2 * G0

SCIENCE_F_HZ = 0.5
REFERENCE_F_HZ = 1.0
REFERENCE_UG = 1.0
OTHER_PHASE_RMS = 4e-3
REJECTION = 3.0

PSD_FREQ_HZ = np.array([
    0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.70, 1.0,
    2.0, 3.0, 5.0, 10.0, 20.0, 30.0, 50.0, 70.0, 100.0, 200.0,
])
PSD_ASD_G = np.array([
    1e-9, 3e-9, 1e-8, 4e-8, 1.2e-7, 1.7e-7, 1.3e-7, 5e-8,
    2e-8, 2e-8, 1.8e-8, 2e-8, 2.2e-8, 2.3e-8, 2.5e-8,
    4e-8, 7e-8, 1e-7, 1e-7,
])


def accel_response(f_hz: np.ndarray | float) -> np.ndarray:
    return np.sinc(np.asarray(f_hz, dtype=float) * T) ** 2


def passive_asd(f_hz: np.ndarray | float, crosstalk_boost: float = 1.0) -> np.ndarray:
    f = np.asarray(f_hz, dtype=float)
    clipped = np.clip(f, PSD_FREQ_HZ[0], PSD_FREQ_HZ[-1])
    base = 10.0 ** np.interp(
        np.log10(clipped), np.log10(PSD_FREQ_HZ), np.log10(PSD_ASD_G)
    )
    if crosstalk_boost <= 1.0:
        return base
    width = math.log(2.0)
    bump = 1.0 + (crosstalk_boost - 1.0) * np.exp(
        -0.5 * (np.log(np.maximum(f, 1e-12) / 2.0) / width) ** 2
    )
    return base * bump


def integration_grid() -> np.ndarray:
    low = np.linspace(0.0005, 0.05, 100, endpoint=False)
    high = np.geomspace(0.05, 500.0, 4000)
    return np.unique(np.r_[low, high])


def vibration_covariance_lags(
    nlags: int,
    *,
    rejection: float = REJECTION,
    crosstalk_boost: float = 1.0,
) -> np.ndarray:
    f = integration_grid()
    asd = passive_asd(f, crosstalk_boost=crosstalk_boost) / rejection
    sphi = (K_G * accel_response(f) * asd) ** 2
    lag = np.arange(nlags, dtype=float)[:, None]
    phase = 2.0 * math.pi * lag * (TC * f[None, :])
    return np.trapezoid(sphi[None, :] * np.cos(phase), f, axis=1)


def total_covariance_lags(
    nlags: int,
    *,
    crosstalk_boost: float = 1.0,
) -> np.ndarray:
    c = vibration_covariance_lags(nlags, crosstalk_boost=crosstalk_boost)
    c[0] += OTHER_PHASE_RMS**2
    return c


def dense_toeplitz(c: np.ndarray) -> np.ndarray:
    idx = np.abs(np.arange(len(c))[:, None] - np.arange(len(c))[None, :])
    return c[idx]


def mean_variance_from_lags(c: np.ndarray, n: int) -> float:
    val = n * c[0]
    for lag in range(1, n):
        val += 2.0 * (n - lag) * c[lag]
    return float(val / n**2)


def source_reproduction() -> dict[str, float]:
    uncorrected = vibration_covariance_lags(4, rejection=1.0)
    sigma_uncorrected = math.sqrt(mean_variance_from_lags(uncorrected, 4)) / K_G

    corrected = vibration_covariance_lags(4, rejection=REJECTION)
    corrected[0] += OTHER_PHASE_RMS**2
    sigma_corrected = math.sqrt(mean_variance_from_lags(corrected, 4)) / K_G

    return {
        "uncorrected_g_1s": sigma_uncorrected,
        "uncorrected_relerr": abs(sigma_uncorrected / 6.5e-8 - 1.0),
        "corrected_g_1s": sigma_corrected,
        "corrected_relerr": abs(sigma_corrected / 2.0e-8 - 1.0),
    }


def templates(nshot: int, science_modulated: bool) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
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


def local_science_and_nuisance(
    nshot: int,
    *,
    science_modulated: bool,
    use_reference: bool,
    reference_unknown: bool,
) -> tuple[np.ndarray, np.ndarray]:
    x, science, reference = templates(nshot, science_modulated)
    if not use_reference:
        reference = np.zeros_like(reference)

    theta_g = 1e-9
    alpha_g = REFERENCE_UG * 1e-6 if use_reference else 0.0

    science_direction = K_G * 1e-9 * science
    nuisance = [
        K_G * (theta_g * science + alpha_g * reference),  # common scale/gain
        np.ones(nshot),                                   # phase offset
        x,                                                # linear drift
        x**2,                                             # quadratic drift
    ]
    if reference_unknown:
        nuisance.append(K_G * 1e-6 * reference)
    return science_direction, np.column_stack(nuisance)


def profiled_information(
    covariance: np.ndarray,
    science_direction: np.ndarray,
    nuisance: np.ndarray,
    *,
    reference_prior_fraction: float | None = None,
) -> dict[str, float]:
    ci_r = np.linalg.solve(covariance, science_direction)
    ci_n = np.linalg.solve(covariance, nuisance)

    i0 = float(science_direction @ ci_r)
    ftn = science_direction @ ci_n
    fnn = nuisance.T @ ci_n

    if reference_prior_fraction is not None:
        if reference_prior_fraction <= 0.0:
            raise ValueError("reference prior must be positive")
        # The last nuisance coordinate is the reference amplitude in micro-g.
        fnn[-1, -1] += 1.0 / (REFERENCE_UG * reference_prior_fraction) ** 2

    correction = float(ftn @ np.linalg.pinv(fnn, rcond=1e-12) @ ftn.T)
    iprof = max(i0 - correction, 0.0)
    eta = math.sqrt(iprof / i0) if i0 > 0.0 else 0.0
    return {"I0": i0, "I_profiled": iprof, "eta_detector": eta}


def detector_case(
    *,
    science_modulated: bool,
    use_reference: bool,
    reference_unknown: bool = False,
    reference_prior_fraction: float | None = None,
    crosstalk_boost: float = 1.0,
    seconds: float = 60.0,
) -> dict[str, float]:
    nshot = int(round(seconds / TC))
    covariance = dense_toeplitz(
        total_covariance_lags(nshot, crosstalk_boost=crosstalk_boost)
    )
    r, n = local_science_and_nuisance(
        nshot,
        science_modulated=science_modulated,
        use_reference=use_reference,
        reference_unknown=reference_unknown,
    )
    return profiled_information(
        covariance,
        r,
        n,
        reference_prior_fraction=reference_prior_fraction,
    )


def structural_assertions() -> None:
    src = source_reproduction()
    assert src["uncorrected_relerr"] < 0.05
    assert src["corrected_relerr"] < 0.12

    static = detector_case(science_modulated=False, use_reference=True)
    no_ref = detector_case(science_modulated=True, use_reference=False)
    known_ref = detector_case(science_modulated=True, use_reference=True)
    free_ref = detector_case(
        science_modulated=True,
        use_reference=True,
        reference_unknown=True,
    )
    finite_ref = detector_case(
        science_modulated=True,
        use_reference=True,
        reference_unknown=True,
        reference_prior_fraction=1e-3,
    )

    assert static["eta_detector"] < 1e-6
    assert no_ref["eta_detector"] < 1e-6
    assert known_ref["eta_detector"] > 0.95
    assert free_ref["eta_detector"] < 1e-3
    assert finite_ref["eta_detector"] > 0.95

    for boost in (1.0, 2.0, 3.0, 5.0):
        stressed = detector_case(
            science_modulated=True,
            use_reference=True,
            reference_unknown=True,
            reference_prior_fraction=1e-3,
            crosstalk_boost=boost,
        )
        assert stressed["eta_detector"] > 0.90


if __name__ == "__main__":
    structural_assertions()
    src = source_reproduction()
    print("source_uncorrected_g_1s", src["uncorrected_g_1s"])
    print("source_corrected_g_1s", src["corrected_g_1s"])
    for name, kwargs in [
        ("static_known_ref", dict(science_modulated=False, use_reference=True)),
        ("modulated_no_ref", dict(science_modulated=True, use_reference=False)),
        ("modulated_known_ref", dict(science_modulated=True, use_reference=True)),
        ("modulated_free_ref", dict(science_modulated=True, use_reference=True, reference_unknown=True)),
        ("modulated_finite_ref", dict(science_modulated=True, use_reference=True, reference_unknown=True, reference_prior_fraction=1e-3)),
    ]:
        print(name, detector_case(**kwargs))
