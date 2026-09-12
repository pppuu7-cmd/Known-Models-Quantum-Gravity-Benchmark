#!/usr/bin/env python3
"""Iter437: source-backed Lorentzian-Regge boundary magnetic-closure audit.

Preregistered in recovery/ITER437_PREREG_SOURCE_LORENTZIAN_BOUNDARY_2026-09-12.md.
The boundary-spin pattern is frozen from Donà et al., PRD 100, 106003
(arXiv:1903.12624): four j=5 faces of the equilateral reference tetrahedron
and six j=2 faces, at primitive homogeneous scale lambda=1.

This is a necessary local SU(2) magnetic-closure diagnostic only. It is not a
full intertwiner/Haar contraction or a physical causal-vertex integrability
certificate.
"""
import argparse
import itertools
import json
import os

VERTICES = tuple(range(5))
EDGES = tuple((a, b) for a in VERTICES for b in VERTICES if a < b)


def source_spin(edge):
    """Published isosceles Lorentzian 4-simplex spin/area pattern at lambda=1."""
    return 5 if 0 in edge else 2


def twice(x):
    return int(round(2.0 * x))


def values_for_j(j):
    tj = twice(j)
    return [m2 / 2.0 for m2 in range(-tj, tj + 1, 2)]


def sector(index):
    if not 0 <= index < 16:
        raise ValueError("index must be 0..15")
    sigma = {0: 1}
    for k in range(4):
        sigma[k + 1] = 1 if ((index >> k) & 1) else -1
    kappa = {(a, b): sigma[a] * sigma[b] for a, b in EDGES}
    return sigma, kappa


def outgoing_m(edge, vertex, m_edge):
    a, b = edge
    if vertex == a:
        return m_edge
    if vertex == b:
        return -m_edge
    raise ValueError("vertex not incident to edge")


def exact_bruteforce_closure(fixed_outgoing, free_js):
    if not free_js:
        return abs(sum(fixed_outgoing)) < 1e-12
    target = -sum(fixed_outgoing)
    return any(abs(sum(vals) - target) < 1e-12
               for vals in itertools.product(*(values_for_j(j) for j in free_js)))


def interval_parity_closure(fixed_outgoing, free_js):
    target2 = -sum(twice(m) for m in fixed_outgoing)
    max2 = sum(twice(j) for j in free_js)
    parity = sum(twice(j) for j in free_js) % 2
    return (-max2 <= target2 <= max2) and (target2 % 2 == parity)


def invariant_admissible(js):
    """Necessary/sufficient singlet existence for four SU(2) spins."""
    tjs = [twice(j) for j in js]
    return max(tjs) <= sum(tjs) - max(tjs) and sum(tjs) % 2 == 0


def validate_source_pattern():
    pattern_ok = all(source_spin((0, b)) == 5 for b in range(1, 5))
    pattern_ok &= all(source_spin((a, b)) == 2 for a in range(1, 5) for b in range(a + 1, 5))
    nodes = {}
    for v in VERTICES:
        js = [source_spin(e) for e in EDGES if v in e]
        nodes[str(v)] = {"spins": js, "singlet_admissible": invariant_admissible(js)}
    return pattern_ok and all(x["singlet_admissible"] for x in nodes.values()), nodes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", type=int, required=True)
    ap.add_argument("--cluster-size", type=int, choices=(3, 4), required=True)
    args = ap.parse_args()

    source_valid, source_nodes = validate_source_pattern()
    sigma, kappa = sector(args.index)
    s = args.cluster_size
    boosted = set(range(1, s + 1))
    crossing = [e for e in EDGES if ((e[0] in boosted) != (e[1] in boosted))]

    edge_data = {}
    alphas = []
    for r, e in enumerate(crossing):
        j = source_spin(e)
        sign = kappa[e]
        m = -j if sign == 1 else j
        alpha = 1.0 + abs(j + sign * m)
        alphas.append(alpha)
        edge_data[e] = {
            "j": j, "m": m, "sign": sign, "fixed": True, "cross_index": r
        }

    expected_tail_lambda = 2.0 * s - sum(alphas)

    for e in EDGES:
        if e not in edge_data:
            edge_data[e] = {
                "j": source_spin(e), "m": None, "sign": kappa[e], "fixed": False
            }

    controls_valid = bool(source_valid and expected_tail_lambda >= 0.0)
    vertex_rows = []
    for v in VERTICES:
        incident = [e for e in EDGES if v in e]
        controls_valid &= len(incident) == 4
        fixed_out = []
        free_js = []
        edge_rows = []
        for e in incident:
            d = edge_data[e]
            if d["fixed"]:
                j, m = d["j"], d["m"]
                valid_m = abs(m) <= j + 1e-12 and ((twice(j) - twice(m)) % 2 == 0)
                controls_valid &= valid_m
                mout = outgoing_m(e, v, m)
                fixed_out.append(mout)
                edge_rows.append({
                    "edge": list(e), "j": j, "fixed_m_edge": m,
                    "m_out": mout, "fixed": True
                })
            else:
                free_js.append(d["j"])
                edge_rows.append({"edge": list(e), "j": d["j"], "fixed": False})

        brute = exact_bruteforce_closure(fixed_out, free_js)
        analytic = interval_parity_closure(fixed_out, free_js)
        agree = brute == analytic
        controls_valid &= agree
        vertex_rows.append({
            "vertex": v,
            "fixed_outgoing_sum": sum(fixed_out),
            "free_leg_spins": free_js,
            "bruteforce_closure_exists": brute,
            "interval_parity_closure_exists": analytic,
            "independent_checks_agree": agree,
            "edges": edge_rows,
        })

    all_vertices_allow = all(r["bruteforce_closure_exists"] for r in vertex_rows)
    if not controls_valid:
        classification = "CONTROL_INVALID"
    elif all_vertices_allow:
        classification = "SOURCE_BACKED_LORENTZIAN_BOUNDARY_ALLOWS_SLOW_EXTREMAL_PROFILE"
    else:
        classification = "SOURCE_BACKED_LORENTZIAN_BOUNDARY_EXCLUDES_SLOW_EXTREMAL_PROFILE"

    out = {
        "iteration": 437,
        "source": {
            "paper": "Dona-Fanizza-Sarno-Speziale, PhysRevD.100.106003, arXiv:1903.12624v3",
            "boundary_pattern": "four j=5 faces incident to reference node 0; six j=2 remaining faces",
            "homogeneous_scale": 1,
            "source_pattern_valid": source_valid,
            "node_singlet_admissibility": source_nodes,
        },
        "sector_index": args.index,
        "cluster_size": s,
        "sigma": {str(k): val for k, val in sigma.items()},
        "expected_tail_lambda": expected_tail_lambda,
        "iter435_slow_obstruction_reproduced": expected_tail_lambda >= 0.0,
        "crossing_edges": [list(e) for e in crossing],
        "edge_data": {f"{a}-{b}": d for (a, b), d in edge_data.items()},
        "vertices": vertex_rows,
        "all_vertices_allow_local_closure": all_vertices_allow,
        "controls_valid": controls_valid,
        "classification": classification,
        "scope_guard": (
            "Necessary local SU(2) magnetic-closure test under a published Lorentzian-Regge "
            "boundary-spin pattern only; not full Haar/intertwiner contraction, angular integration, "
            "causal-vertex divergence/finiteness, family promotion, or terminal D7."
        ),
        "d2": "NOT_CLOSED_COVERAGE_AND_OBJECTS",
        "d4": "PARTIAL_GLOBAL_NOT_CLOSED",
        "d7_s2": "NOT_CLOSED",
        "d7_s3": "NOT_CLOSED",
        "d7_s4": "PARTIAL_GLOBAL_NOT_CLOSED",
        "d7": "NOT_CLOSED / NOT_YET_AUTHORIZED",
        "candidate_gravity_authorized": False,
    }

    os.makedirs("build/lqg-iter437", exist_ok=True)
    path = f"build/lqg-iter437/sector_{args.index}_s{s}.json"
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not controls_valid:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
