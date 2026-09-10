#!/usr/bin/env python3
"""Synthetic RQIR functional-rigidity stress test for entire nonlocal form factors.

This is NOT a detector forecast and NOT a proof about the whole NONLOCAL_QG family.
It tests a mathematical question: can a finite polynomial-in-k^2 local-EFT surrogate,
fit only inside a calibration window, extrapolate the correlated entire-function shape
F_N(x)=exp[-(x^2)^N] into a disjoint holdout window?

Calibration domain: x in [0,0.8]
Holdout domain:    x in [0.8,1.6]
N in {1,2,3}; polynomial degree in {1,2,3,4,5,6,8,10}.

The constant polynomial coefficient absorbs a normalization nuisance. A horizontal
scale uncertainty is not separately counted here because an unconstrained polynomial
coefficient set already absorbs scale reparameterization inside the calibration
subspace. A future physical capsule must treat source/scale priors explicitly.
"""

import csv
import math
from pathlib import Path
import numpy as np
from numpy.polynomial import Chebyshev

CAL = (0.0, 0.8)
HOLD = (0.8, 1.6)
NS = (1, 2, 3)
DEGREES = (1, 2, 3, 4, 5, 6, 8, 10)
NPTS = 1000


def exact_shape(x: np.ndarray, n: int) -> np.ndarray:
    z = x * x
    return np.exp(-(z ** n))


def evaluate(n: int, degree: int):
    xc = np.linspace(CAL[0], CAL[1], NPTS)
    xh = np.linspace(HOLD[0], HOLD[1], NPTS)
    zc, zh = xc * xc, xh * xh
    fc, fh = exact_shape(xc, n), exact_shape(xh, n)

    # Chebyshev basis improves numerical conditioning but spans exactly the same
    # finite polynomial subspace in z=k^2 as a monomial local-EFT surrogate.
    poly = Chebyshev.fit(zc, fc, degree, domain=[CAL[0] ** 2, CAL[1] ** 2])
    pc, ph = poly(zc), poly(zh)

    cal_rmse = float(np.sqrt(np.mean((pc - fc) ** 2)))
    hold_rmse = float(np.sqrt(np.mean((ph - fh) ** 2)))
    hold_max = float(np.max(np.abs(ph - fh)))
    hold_rel = float(hold_rmse / np.sqrt(np.mean(fh ** 2)))
    return cal_rmse, hold_rmse, hold_max, hold_rel


def main():
    out = Path("paper_iv/NONLOCAL_FULL_SHAPE_EFT_HOLDOUT_STRESS_ITER233.csv")
    rows = []
    for n in NS:
        for degree in DEGREES:
            cal_rmse, hold_rmse, hold_max, hold_rel = evaluate(n, degree)
            rows.append({
                "N": n,
                "EFT_degree": degree,
                "calibration_RMSE": f"{cal_rmse:.12e}",
                "holdout_RMSE": f"{hold_rmse:.12e}",
                "holdout_max_abs": f"{hold_max:.12e}",
                "holdout_relative_RMSE": f"{hold_rel:.12e}",
            })

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(out)
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
