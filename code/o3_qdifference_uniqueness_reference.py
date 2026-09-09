"""Executable control for the O3 q-difference uniqueness theorem.

This is a numerical regression witness, not a proof. The proof is frozen in
protocol/O3_QDIFFERENCE_QPOCHHAMMER_UNIQUENESS_CONTROL.md.
"""


def qproduct(z: complex, q: complex, a: complex, b: complex, n: int = 300) -> complex:
    out = 1.0 + 0.0j
    qj = 1.0 + 0.0j
    for _ in range(n):
        out *= (1.0 - a * qj * z) / (1.0 - b * qj * z)
        qj *= q
    return out


def main() -> None:
    q = 0.37
    a = 0.63
    b = -0.21
    z = 0.31 + 0.17j

    fz = qproduct(z, q, a, b)
    fqz = qproduct(q * z, q, a, b)
    rhs = ((1.0 - b * z) / (1.0 - a * z)) * fz

    abs_err = abs(fqz - rhs)
    rel_err = abs_err / max(1.0, abs(fqz), abs(rhs))

    # Fixed-point normalization control.
    f0 = qproduct(0.0, q, a, b)

    print(f"F(0)={f0}")
    print(f"F(z)={fz}")
    print(f"F(qz)={fqz}")
    print(f"recursion_rhs={rhs}")
    print(f"abs_err={abs_err:.3e}")
    print(f"rel_err={rel_err:.3e}")

    if abs(f0 - 1.0) > 1e-15:
        raise SystemExit("fixed-point normalization failed")
    if rel_err > 1e-12:
        raise SystemExit("q-difference recursion regression failed")

    print("O3 q-difference uniqueness control: PASS")


if __name__ == "__main__":
    main()
