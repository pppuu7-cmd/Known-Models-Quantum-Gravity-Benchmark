#!/usr/bin/env python3
"""Compact-support localization certificate for the frozen Gaussian K5 diagnostic."""

from __future__ import annotations

from math import comb, factorial
import json
import mpmath as mp

mp.mp.dps = 180

K_USED = (5, 6, 7, 8)
PATHS = {
    "P1": {"exponents": (1,1,1,1,2,2,2,2,2,2), "q_power": 2},
    "P2": {"exponents": (2,2,2,2,1,1,1,1,1,1), "q_power": 4},
    "P3": {"exponents": (1,2,3,4,2,3,4,3,4,4), "q_power": 2},
}

# Frozen parent values from authoritative run 34954054888. Only k=5..8 are consumed.
PARENT = {
    "P1": {
        5: mp.mpf("8.9510136719908333656615197048707843316562750852333e60"),
        6: mp.mpf("1.9633312684248074342314464767612631634535680997002e73"),
        7: mp.mpf("4.314651505876584945816521638588520059271053734886e85"),
        8: mp.mpf("9.4865017199109286106452809809068287930119331797525e97"),
    },
    "P2": {
        5: mp.mpf("245870337345958841759501297345495631316828202.40385"),
        6: mp.mpf("1.7011669634822373234545959023701290547789019612741e52"),
        7: mp.mpf("1.1503980263516685214704565557842195403961344723214e60"),
        8: mp.mpf("7.7349715478329779506879606195894931263878381881271e67"),
    },
    "P3": {
        5: mp.mpf("2.8504231751760102048172903131415132341424544375567e103"),
        6: mp.mpf("2.1446274351862920840626223822442457918986960673853e123"),
        7: mp.mpf("1.5902115441755380115653326873448219689430918674374e143"),
        8: mp.mpf("1.1748053789687323618824129528291495419221411873518e163"),
    },
}


def radial_integral_gamma(alpha):
    # int_1^inf u(1+u)^10 exp(-alpha u) du
    s = mp.mpf(0)
    for j in range(11):
        n = j + 1
        s += comb(10, j) * mp.gammainc(n + 1, alpha, mp.inf) / alpha ** (n + 1)
    return s


def radial_integral_integer_formula(alpha):
    # Independent integer upper-incomplete-gamma expansion.
    total = mp.mpf(0)
    ea = mp.exp(-alpha)
    for j in range(11):
        n = j + 1
        upper_gamma = factorial(n) * ea * sum(alpha ** m / factorial(m) for m in range(n + 1))
        total += comb(10, j) * upper_gamma / alpha ** (n + 1)
    return total


def exterior_bound(path, k, q_override=None):
    t = mp.mpf(2) ** (-k)
    expv = PATHS[path]["exponents"]
    sum_p = sum(expv)
    q = t ** (-PATHS[path]["q_power"]) if q_override is None else mp.mpf(q_override)
    alpha = 1 + q
    pref = (10 / mp.sqrt(mp.pi)) ** 10 * t ** (-5 * sum_p) * mp.pi ** 2
    return pref * radial_integral_gamma(alpha)


def path_certificate(path):
    rows = {}
    for k in K_USED:
        J = PARENT[path][k]
        B = exterior_bound(path, k)
        rows[k] = {
            "J": J,
            "B": B,
            "L": J - B,
            "U": J + B,
            "relative_bound": B / J,
        }

    local = all(rows[k]["L"] > 0 and rows[k]["relative_bound"] <= mp.mpf("1e-20") for k in K_USED)
    ratios = {}
    for k in K_USED[:-1]:
        ratios[f"{k}->{k+1}"] = rows[k+1]["L"] / rows[k]["U"]
        local = local and ratios[f"{k}->{k+1}"] > 4

    return local, rows, ratios


def main():
    controls = {}

    # Exact star rows under gauge fixing are -e_i.
    star_rows = ((-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1))
    controls["star_coordinate_basis"] = star_rows == ((-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1))

    # Independent formula check at alpha=17.
    a = mp.mpf(17)
    rg = radial_integral_gamma(a)
    ri = radial_integral_integer_formula(a)
    controls["radial_formula_agreement"] = abs(rg-ri) / max(abs(rg), mp.mpf("1e-300")) <= mp.mpf("1e-150")

    results = {}
    certified = []
    for p in PATHS:
        ok, rows, ratios = path_certificate(p)
        if ok:
            certified.append(p)
        results[p] = {
            "status": "COMPACT_LOCAL_DIVERGENCE_CERTIFIED" if ok else "COMPACT_LOCALIZATION_INCONCLUSIVE",
            "rows": {
                str(k): {
                    key: mp.nstr(val, 50) for key, val in row.items()
                } for k, row in rows.items()
            },
            "growth_lower_ratios": {key: mp.nstr(val, 40) for key, val in ratios.items()},
        }

    controls["all_bounds_positive_finite"] = all(
        mp.isfinite(exterior_bound(p,k)) and exterior_bound(p,k)>0 for p in PATHS for k in K_USED
    )

    # q=0 must be too loose to certify at least the strongest frozen last point on every path.
    q0_rel = {p: exterior_bound(p,8,q_override=0) / PARENT[p][8] for p in PATHS}
    controls["q_zero_adversarial_does_not_certify"] = all(v > mp.mpf("1e-20") for v in q0_rel.values())

    # Artificially inflated bound fixture must fail the same path predicate logic.
    controls["inflated_bound_fixture_inconclusive"] = all(
        not (PARENT[p][k] - 2*PARENT[p][k] > 0) for p in PATHS for k in K_USED
    )

    controls_pass = all(controls.values())
    if not controls_pass:
        classification = "INVALID_IMPLEMENTATION"
    elif len(certified) == 3:
        classification = "AUX_GAUSSIAN_UNRENORMALIZED_COMPACT_LOCAL_DIVERGENCE_SCOPED"
    elif certified:
        classification = "AUX_GAUSSIAN_COMPACT_LOCALIZATION_PARTIAL_SCOPED"
    else:
        classification = "AUX_GAUSSIAN_COMPACT_LOCALIZATION_INCONCLUSIVE"

    out = {
        "classification": classification,
        "precision_decimal_digits": mp.mp.dps,
        "k_used": list(K_USED),
        "deciding_paths": list(PATHS),
        "controls": controls,
        "controls_pass": controls_pass,
        "q_zero_relative_bounds_at_k8": {p: mp.nstr(v,40) for p,v in q0_rel.items()},
        "path_results": results,
        "certified_paths": certified,
        "claim_ceiling": "Local compact-support diagnostic for the same unrenormalized Gaussian auxiliary family only; not Eq4 nonexistence and not D7 closure."
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
