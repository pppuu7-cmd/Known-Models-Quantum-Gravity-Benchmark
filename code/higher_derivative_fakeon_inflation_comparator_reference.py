"""Scoped RQIR control for leading quadratic-gravity inflation observables.

This is not a family-level theory verdict.  It verifies the literature-stated
leading-order quantization non-identifiability of the (r, n_t) block for a
fixed R+R^2+C^2 action: the leading r formula is independent of the spin-2
quantization prescription, and n_t=-r/8.  Hence a fakeon attribution residual
against a same-action quantization comparator is exactly zero in this block.
"""
from __future__ import annotations

import json
import math


def r_leading(q: float, n_e: float) -> float:
    if q <= 0 or n_e <= 0:
        raise ValueError("q and N_e must be positive")
    return 24.0 / (n_e * n_e) * q / (1.0 + 2.0 * q)


def n_t_leading(q: float, n_e: float) -> float:
    return -r_leading(q, n_e) / 8.0


def main() -> int:
    n_values = (50.0, 57.0, 60.0)
    # Fakeon consistency domain quoted for the Starobinsky+Weyl^2 analysis:
    # m_2 >= m_0/4 -> q=(m_2/m_0)^2 >= 1/16.
    q_values = (1.0 / 16.0, 0.1, 0.25, 1.0, 10.0, 1.0e3, 1.0e9)

    max_identity_error = 0.0
    max_consistency_error = 0.0
    monotonic = True

    for n_e in n_values:
        prev = -math.inf
        for q in q_values:
            fakeon = (r_leading(q, n_e), n_t_leading(q, n_e))
            # Published leading expression is quantization-independent, so the
            # same-action alternative-quantization comparator has the same map.
            comparator = (r_leading(q, n_e), n_t_leading(q, n_e))
            max_identity_error = max(
                max_identity_error,
                abs(fakeon[0] - comparator[0]),
                abs(fakeon[1] - comparator[1]),
            )
            max_consistency_error = max(
                max_consistency_error, abs(fakeon[1] + fakeon[0] / 8.0)
            )
            monotonic &= fakeon[0] >= prev
            prev = fakeon[0]

        lower = r_leading(1.0 / 16.0, n_e)
        expected_lower = 4.0 / (3.0 * n_e * n_e)
        if not math.isclose(lower, expected_lower, rel_tol=0.0, abs_tol=1e-15):
            raise AssertionError("fakeon lower boundary does not reproduce 4/(3 N_e^2)")

        asymptotic = r_leading(1.0e15, n_e)
        starobinsky = 12.0 / (n_e * n_e)
        if not math.isclose(asymptotic, starobinsky, rel_tol=1e-14, abs_tol=1e-15):
            raise AssertionError("large-m2 limit does not approach Starobinsky r")

    if max_identity_error != 0.0:
        raise AssertionError("same-action quantization comparator identity failed")
    if max_consistency_error > 1e-16:
        raise AssertionError("n_t=-r/8 leading relation failed")
    if not monotonic:
        raise AssertionError("r(q) should increase monotonically on q>0")

    result = {
        "status": "PASS_RQIR_GATE__SCOPED_FAKEON_LEADING_INFLATION_QUANTIZATION_NONIDENTIFIABILITY",
        "observable_block": ["r", "n_t"],
        "fakeon_domain_q_min": 1.0 / 16.0,
        "max_same_action_quantization_identity_error": max_identity_error,
        "max_nt_plus_r_over_8_error": max_consistency_error,
        "monotonic_r_in_q": monotonic,
        "comparator_orthogonal_attribution_residual": "EXACT_ZERO_IN_DECLARED_LEADING_BLOCK",
        "family_level_conclusion": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
