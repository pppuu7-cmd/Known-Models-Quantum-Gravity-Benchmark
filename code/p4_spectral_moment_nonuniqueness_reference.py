#!/usr/bin/env python3
"""Exact finite-moment nonuniqueness witness for KMQGB P4.

Two distinct positive discrete measures on omega={1,2,3,4,5}
share moments mu_k for k=0,1,2,3.  The difference vector
(1,-4,6,-4,1) is the fourth finite-difference stencil and annihilates
all polynomials of degree <4.
"""

from fractions import Fraction

OMEGA = [1, 2, 3, 4, 5]
NULL = [1, -4, 6, -4, 1]
BASE = [10, 10, 10, 10, 10]
W_PLUS = [b + d for b, d in zip(BASE, NULL)]
W_MINUS = [b - d for b, d in zip(BASE, NULL)]


def moment(weights, k):
    return sum(Fraction(w) * Fraction(x) ** k for x, w in zip(OMEGA, weights))


def main():
    assert W_PLUS != W_MINUS
    assert all(w > 0 for w in W_PLUS)
    assert all(w > 0 for w in W_MINUS)

    null_moments = [sum(Fraction(d) * Fraction(x) ** k for x, d in zip(OMEGA, NULL)) for k in range(4)]
    assert null_moments == [0, 0, 0, 0]

    plus = [moment(W_PLUS, k) for k in range(4)]
    minus = [moment(W_MINUS, k) for k in range(4)]
    assert plus == minus

    # The next moment differs, proving the measures are genuinely distinct
    # beyond the finite constraint set.
    assert moment(W_PLUS, 4) != moment(W_MINUS, 4)

    print("support=", OMEGA)
    print("w_plus=", W_PLUS)
    print("w_minus=", W_MINUS)
    print("shared_moments_k0_to_k3=", [int(v) for v in plus])
    print("moment4_plus=", int(moment(W_PLUS, 4)))
    print("moment4_minus=", int(moment(W_MINUS, 4)))
    print("PASS__FINITE_MOMENTS_DO_NOT_UNIQUELY_FIX_POSITIVE_SPECTRAL_MEASURE")


if __name__ == "__main__":
    main()
