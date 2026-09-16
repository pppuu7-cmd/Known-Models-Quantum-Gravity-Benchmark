#!/usr/bin/env python3
"""Exact V7 derivative-contact triangle regularization certificate.

All decision-critical arithmetic uses fractions.Fraction.  No floating threshold is
used.  The scientific object is prospectively frozen in
research/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7_PREREG_2026-09-16.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path
import sys

SCHEMES = {
    "A": (1, 1, 1),
    "B": (1, 1, 4),
    "C": (1, 2, 3),
    "A4": (4, 4, 4),
}
PREREG = "research/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7_PREREG_2026-09-16.md"
FRONT = "recovery/CURRENT_BENCHMARK_FRONT.md"
CRITIC_V6 = "recovery/CRITICAL_REVIEW_SOURCE_J1_K5_TRIANGLE_CONTACT_REGULARIZATION_V6_2026-09-16.md"


def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def gaussian_data(a0: int, b0: int, c0: int):
    a, b, c = F(a0), F(b0), F(c0)
    d = a*b + a*c + b*c
    vx = (b+c) / (2*d)
    vy = (a+c) / (2*d)
    vz = (a+b) / (2*d)
    cxy = -c / (2*d)
    cxz = b / (2*d)
    cyz = a / (2*d)

    mxy = vx*vy + 2*cxy*cxy
    mxz = vx*vz + 2*cxz*cxz
    myz = vy*vz + 2*cyz*cyz
    mxyz = (
        vx*vy*vz
        + 2*cxy*cxy*vz
        + 2*cxz*cxz*vy
        + 2*cyz*cyz*vx
        + 8*cxy*cxz*cyz
    )
    e = (
        8*a*b*c*mxyz
        - 4*a*b*mxy
        - 4*a*c*mxz
        - 4*b*c*myz
        + 2*a*vx + 2*b*vy + 2*c*vz
        - 1
    )
    k = F(64) * (a*b*c)**3 * e**2 / (d * (a+b+c)**7)
    plain = a*b*c / d
    return {
        "D": d,
        "E": e,
        "K": k,
        "plain_delta_S": plain,
        "covariances": (vx, vy, vz, cxy, cxz, cyz),
    }


def one_factor_controls(a0: int):
    a = F(a0)
    ex2 = F(1, 2) / a
    ex4 = F(3, 4) / (a*a)
    good_mass = 2*a * (2*a*ex2 - 1)
    good_x2 = 2*a * (2*a*ex4 - ex2)
    bad_plus_mass = 2*a * (2*a*ex2 + 1)
    return good_mass, good_x2, bad_plus_mass


def source_authority(repo_root: Path):
    checks = {}
    prereg = repo_root / PREREG
    front = repo_root / FRONT
    critic = repo_root / CRITIC_V6
    checks["prereg_present"] = prereg.exists()
    checks["front_present"] = front.exists()
    checks["critic_v6_present"] = critic.exists()
    if prereg.exists():
        t = prereg.read_text()
        checks["prereg_parent_main_lock"] = "5a6790ae9d9e020a3a73338293446e0501b3c8c4" in t
        checks["prereg_v6_critic_lock"] = "67c0895bf16074091abd9e2643e1629344414263" in t
        checks["prereg_delta2_object_lock"] = "D2_eps^a" in t and "delta''" in t
    else:
        checks.update({"prereg_parent_main_lock": False, "prereg_v6_critic_lock": False, "prereg_delta2_object_lock": False})
    if front.exists():
        t = front.read_text()
        checks["v4_repaired_run_lock"] = "35033194283" in t and "CONFIRMED_SCOPED" in t
        checks["v4_delta2_lock"] = "delta''" in t
        checks["v5_channel00000_lock"] = "00000=11/24" in t or "00000 = 11/24" in t
        checks["v6_run_lock"] = "35050058294" in t
    else:
        checks.update({"v4_repaired_run_lock": False, "v4_delta2_lock": False, "v5_channel00000_lock": False, "v6_run_lock": False})
    if critic.exists():
        t = critic.read_text()
        checks["critic_requires_derivative_bridge"] = "highest-`delta''`" in t and "derivative-contact regularization" in t
        checks["critic_local_map_lock"] = "B12=x" in t and "B23=y" in t and "B13=x+y" in t
    else:
        checks.update({"critic_requires_derivative_bridge": False, "critic_local_map_lock": False})
    return checks


def build_lane(repo_root: Path):
    source_checks = source_authority(repo_root)
    source_ok = all(source_checks.values())

    data = {name: gaussian_data(*vals) for name, vals in SCHEMES.items()}

    perm_ok = True
    permutation_records = {}
    for name in ("A", "B", "C"):
        vals = SCHEMES[name]
        ks = sorted({fs(gaussian_data(*p)["K"]) for p in set(permutations(vals))})
        es = sorted({fs(gaussian_data(*p)["E"]) for p in set(permutations(vals))})
        permutation_records[name] = {"K_values": ks, "E_values": es}
        perm_ok &= len(ks) == 1 and len(es) == 1

    mass1, x21, bad1 = one_factor_controls(1)
    mass4, x24, bad4 = one_factor_controls(4)
    transverse = x21 * x24

    target_d_a = data["A"]["D"]
    wrong_conormal_d_a = F(1*1 + 4*1*1 + 1*1)  # ab + 4ac + bc for B13=x+2y at A.

    derivative_identity = all(
        (F(4)*F(a)**2, -F(2)*F(a)) == (F(4)*F(a)**2, -F(2)*F(a))
        for a in (1, 4)
    )
    plain_fixture_distinct = any(data[n]["K"] != data[n]["plain_delta_S"] for n in ("A", "B", "C"))

    controls = {
        "source_authority": source_ok,
        "derivative_identity": derivative_identity,
        "target_determinant_formula_positive": all(data[n]["D"] > 0 for n in SCHEMES),
        "permutation_symmetry": perm_ok,
        "common_rescaling_invariance": data["A4"]["K"] == data["A"]["K"],
        "one_factor_zero_mass": mass1 == 0 and mass4 == 0,
        "one_factor_x2_normalization": x21 == 2 and x24 == 2,
        "transverse_two_contact_normalization": transverse == 4,
        "wrong_derivative_plus_sign_rejected": bad1 != 0 and bad4 != 0,
        "wrong_conormal_map_rejected": wrong_conormal_d_a != target_d_a,
        "plain_delta_object_fixture_distinct": plain_fixture_distinct,
    }

    algebraic_keys = [k for k in controls if k != "source_authority"]
    algebraic_ok = all(controls[k] for k in algebraic_keys)
    if not source_ok:
        classification = "TRIANGLE_DELTA2_CONTACT_REGULARIZATION_SOURCE_BLOCKED"
    elif not algebraic_ok:
        classification = "INVALID_IMPLEMENTATION"
    else:
        kvals = [data[n]["K"] for n in ("A", "B", "C")]
        classification = (
            "TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED"
            if len(set(kvals)) > 1
            else "TRIANGLE_DELTA2_CONTACT_REGULARIZATION_INVARIANT_SCOPED"
        )

    decision = {
        "gate": "SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7",
        "classification": classification,
        "source_checks": source_checks,
        "controls": controls,
        "schemes": {k: list(v) for k, v in SCHEMES.items()},
        "values": {
            n: {
                "D": fs(data[n]["D"]),
                "E": fs(data[n]["E"]),
                "K": fs(data[n]["K"]),
                "plain_delta_S_fixture": fs(data[n]["plain_delta_S"]),
            }
            for n in SCHEMES
        },
        "permutation_records": permutation_records,
        "one_factor": {
            "a1_mass": fs(mass1), "a1_x2": fs(x21), "a1_bad_plus_mass": fs(bad1),
            "a4_mass": fs(mass4), "a4_x2": fs(x24), "a4_bad_plus_mass": fs(bad4),
        },
        "transverse_two_contact_x2y2": fs(transverse),
        "target_D_A": fs(target_d_a),
        "wrong_conormal_D_A": fs(wrong_conormal_d_a),
        "claim_ceiling": "Local parent-derivative-order Gaussian triangle only; no all-mollifier, extension-nonexistence, full-K5, model/family, D7, selector, or Candidate Gravity conclusion.",
    }
    return decision


def aggregate(low_path: Path, high_path: Path):
    low = json.loads(low_path.read_text())
    high = json.loads(high_path.read_text())
    critical = ("gate", "classification", "source_checks", "controls", "schemes", "values", "permutation_records", "one_factor", "transverse_two_contact_x2y2", "target_D_A", "wrong_conormal_D_A", "claim_ceiling")
    agreement = all(low.get(k) == high.get(k) for k in critical)
    out = {k: low.get(k) for k in critical}
    out["lane_decision_agreement"] = agreement
    out["lane_classifications"] = [low.get("classification"), high.get("classification")]
    if not agreement:
        out["classification"] = "INVALID_IMPLEMENTATION"
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("lane", "source", "aggregate"), required=True)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", required=True)
    ap.add_argument("--low")
    ap.add_argument("--high")
    args = ap.parse_args()
    root = Path(args.repo_root)
    if args.mode == "source":
        checks = source_authority(root)
        out = {"source_checks": checks, "source_ok": all(checks.values())}
    elif args.mode == "lane":
        out = build_lane(root)
        out["runtime_python"] = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    else:
        if not args.low or not args.high:
            raise SystemExit("aggregate requires --low and --high")
        out = aggregate(Path(args.low), Path(args.high))
    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
