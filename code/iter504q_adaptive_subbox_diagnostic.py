#!/usr/bin/env python3
"""Prospectively frozen Iter504Q adaptive subbox continuous-drift diagnostic.

Full 243-channel recomputation on every exact rational amplitude subbox.
No channel deletion, threshold change, or point substitution is permitted.
"""
from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from fractions import Fraction

from flint import arb, ctx

import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
import iter501_direct_max_envelope_interval as prev
import iter503_ad_core as ad
import iter504_centered_shard as parent

ctx.prec = 384

GATE = "ITER504Q_ADAPTIVE_SUBBOX_CONTINUOUS_DRIFT_NARROWING_DIAGNOSTIC_GATE"
PREREG = "881c804f56a9a9969f8c969ea3ccd1826da92846"
CAUSAL = "0to5"
BLOCK = 0
PATH = 2
ROOT_BOXES = (13, 14, 15)
MAX_DEPTH = 6
DRIFT_TOL = arb("0.05")
ROBUST_FLOOR = arb("1.0")
PASS = "ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_NARROWED_WITHIN_TOLERANCE_SCOPED"
INCONCLUSIVE = "ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_INCONCLUSIVE_SCOPED"
INVALID = "ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_INVALID"


def _bf(x, side):
    return core.bound_float(x, side)


def _arb_fraction(q: Fraction):
    return arb(q.numerator) / arb(q.denominator)


def _qtext(q: Fraction):
    return f"{q.numerator}/{q.denominator}"


def root_interval(k: int):
    if k not in ROOT_BOXES:
        raise ValueError(k)
    return Fraction(16 + k, 12800), Fraction(17 + k, 12800)


def centered_subbox(causal, direction, sign, lo_q: Fraction, hi_q: Fraction, depth: int, root_box: int):
    if not lo_q < hi_q:
        raise ValueError((lo_q, hi_q))
    lo = _arb_fraction(lo_q)
    hi = _arb_fraction(hi_q)
    amp = lo.union(hi)
    mid_q = (lo_q + hi_q) / 2
    half_q = (hi_q - lo_q) / 2
    mid = _arb_fraction(mid_q)
    half = _arb_fraction(half_q)
    delta = (-half).union(half)
    dual_amp = ad.RD(amp, 1)
    sig = core.SIGMAS[causal]

    controls = {
        "construction": True,
        "cycle": True,
        "source_additive": True,
        "finite_envelope": True,
        "center_regression": True,
    }
    perR = {}
    min_beta = None

    for R in core.R_GRID:
        ds = ad.construct_dual_state(R, direction, sign, dual_amp)
        controls["construction"] = controls["construction"] and all(x[2] for x in ds["checks"])
        controls["cycle"] = controls["cycle"] and prev.cycle_contains(
            {e: ad.value_matrix(M) for e, M in ds["edges"].items()}
        )

        raw = enable.construct_state(R, direction, sign, mid)
        reg = enable.source_regression(R, direction, sign, mid, raw)
        controls["center_regression"] = controls["center_regression"] and bool(reg["pass"])

        dlogH = ad.RD(0, 0)
        raw_logH = arb(0)
        for kk in ds["node_kak"].values():
            dlogH += 2 * kk["beta"].sinh().log()
            bl = kk["beta"].v.lower()
            min_beta = bl if min_beta is None or bl < min_beta else min_beta
        for kk in ds["edge_kak"].values():
            bl = kk["beta"].v.lower()
            min_beta = bl if min_beta is None or bl < min_beta else min_beta
        for kk in raw["node_kak"].values():
            raw_logH += 2 * kk["beta"].sinh().log()
        centered_logH = raw_logH + delta * dlogH.d

        rows = []
        for rho in core.RHOS:
            dmats, rmats = [], []
            addok = True
            for e in core.EDGES:
                branch = "p" if sig[e[0]] * sig[e[1]] > 0 else "m"
                dM, dok = ad.dfull_toller(ds["edge_kak"][e], rho, branch)
                rM, rok = core.full_toller(raw["edge_kak"][e], rho, branch)
                dmats.append(dM)
                rmats.append(rM)
                addok = addok and dok and rok
            controls["source_additive"] = controls["source_additive"] and addok
            dvals = ad.dcontract_all(dmats)
            rvals = core.contract_all(rmats)
            vals = ad.centered_channels(rvals, dvals, delta)
            L, U, possible = core.envelope_bounds(vals)
            finite = bool(L > arb(0) and U.is_finite())
            controls["finite_envelope"] = controls["finite_envelope"] and finite
            if not finite:
                raise ArithmeticError("nonfinite/nonpositive subbox max envelope")
            rows.append({
                "rho": rho,
                "_ylo": centered_logH.lower() + L.log().lower(),
                "_yhi": centered_logH.upper() + U.log().upper(),
                "possible_count": len(possible),
                "possible_indices": list(possible),
            })
        perR[R] = rows

    if not all(controls.values()):
        raise ArithmeticError(f"subbox controls failed: {controls}")

    per_rho = []
    certified = True
    max_drift = None
    min_s_lower = None
    for ir, rho in enumerate(core.RHOS):
        y6l, y6u = perR[6][ir]["_ylo"], perR[6][ir]["_yhi"]
        y8l, y8u = perR[8][ir]["_ylo"], perR[8][ir]["_yhi"]
        y10l, y10u = perR[10][ir]["_ylo"], perR[10][ir]["_yhi"]
        y12l, y12u = perR[12][ir]["_ylo"], perR[12][ir]["_yhi"]
        slo = (y12l - y8u) / 4
        shi = (y12u - y8l) / 4
        elo = (y10l - y6u) / 4
        ehi = (y10u - y6l) / 4
        du = max(abs(slo - ehi), abs(shi - elo))
        rho_cert = bool(slo >= ROBUST_FLOOR and du <= DRIFT_TOL)
        certified = certified and rho_cert
        dul = du.upper()
        max_drift = dul if max_drift is None or dul > max_drift else max_drift
        sl = slo.lower()
        min_s_lower = sl if min_s_lower is None or sl < min_s_lower else min_s_lower
        per_rho.append({
            "rho": rho,
            "certified": rho_cert,
            "S_lower": _bf(slo, "lower"),
            "S_upper": _bf(shi, "upper"),
            "E_lower": _bf(elo, "lower"),
            "E_upper": _bf(ehi, "upper"),
            "drift_upper": _bf(du, "upper"),
        })

    possible = []
    for R in core.R_GRID:
        for row in perR[R]:
            possible.append({
                "R": R,
                "rho": row["rho"],
                "count": row["possible_count"],
                "indices": row["possible_indices"],
            })

    return {
        "root_box": root_box,
        "depth": depth,
        "amp_lower_q": _qtext(lo_q),
        "amp_upper_q": _qtext(hi_q),
        "amp_mid_q": _qtext(mid_q),
        "controls": controls,
        "min_beta_lower": None if min_beta is None else _bf(min_beta, "lower"),
        "certified": certified,
        "max_drift_upper": None if max_drift is None else _bf(max_drift, "upper"),
        "min_S_lower": None if min_s_lower is None else _bf(min_s_lower, "lower"),
        "max_possible_count": max(x["count"] for x in possible),
        "possible_max": possible,
        "per_rho": per_rho,
    }


def exact_cover(root_box: int, leaves):
    lo0, hi0 = root_interval(root_box)
    spans = sorted((Fraction(x["amp_lower_q"]), Fraction(x["amp_upper_q"])) for x in leaves)
    if not spans:
        return {"valid": False, "reason": "empty"}
    valid = spans[0][0] == lo0 and spans[-1][1] == hi0
    gaps = []
    overlaps = []
    for i in range(len(spans) - 1):
        if spans[i][1] < spans[i + 1][0]:
            gaps.append([_qtext(spans[i][1]), _qtext(spans[i + 1][0])])
        if spans[i][1] > spans[i + 1][0]:
            overlaps.append([_qtext(spans[i + 1][0]), _qtext(spans[i][1])])
        valid = valid and spans[i][1] == spans[i + 1][0]
    return {
        "valid": bool(valid and not gaps and not overlaps),
        "root_lower_q": _qtext(lo0),
        "root_upper_q": _qtext(hi0),
        "leaf_count": len(spans),
        "gaps": gaps,
        "interior_overlaps": overlaps,
    }


def evaluate_box(root_box: int, direction, sign):
    lo0, hi0 = root_interval(root_box)
    stack = [(lo0, hi0, 0)]
    leaves = []
    node_count = 0
    root_diag = None

    while stack:
        lo_q, hi_q, depth = stack.pop()
        node = centered_subbox(CAUSAL, direction, sign, lo_q, hi_q, depth, root_box)
        node_count += 1
        if depth == 0:
            root_diag = {
                "max_drift_upper": node["max_drift_upper"],
                "min_S_lower": node["min_S_lower"],
                "max_possible_count": node["max_possible_count"],
            }
        if node["certified"]:
            node["leaf_status"] = "CERTIFIED"
            leaves.append(node)
        elif depth >= MAX_DEPTH:
            node["leaf_status"] = "UNRESOLVED_DEPTH6"
            leaves.append(node)
        else:
            mid_q = (lo_q + hi_q) / 2
            # right pushed first so deterministic traversal evaluates left child first
            stack.append((mid_q, hi_q, depth + 1))
            stack.append((lo_q, mid_q, depth + 1))

    leaves.sort(key=lambda x: Fraction(x["amp_lower_q"]))
    cover = exact_cover(root_box, leaves)
    return {
        "root_box": root_box,
        "node_count": node_count,
        "root_diagnostic": root_diag,
        "cover": cover,
        "leaves": leaves,
    }


def summarize(boxes):
    leaves = [leaf for b in boxes for leaf in b["leaves"]]
    valid_cover = all(b["cover"]["valid"] for b in boxes)
    all_controls = all(all(x["controls"].values()) for x in leaves)
    unresolved = [x for x in leaves if x["leaf_status"] != "CERTIFIED"]
    if not valid_cover or not all_controls:
        classification = INVALID
    elif unresolved:
        classification = INCONCLUSIVE
    else:
        classification = PASS

    worst = max(leaves, key=lambda x: x["max_drift_upper"])
    min_s = min(x["min_S_lower"] for x in leaves)
    per_rho = {}
    for rho in core.RHOS:
        rows = []
        for leaf in leaves:
            rr = next(x for x in leaf["per_rho"] if x["rho"] == rho)
            rows.append((rr["drift_upper"], leaf, rr))
        d, leaf, rr = max(rows, key=lambda x: x[0])
        per_rho[str(rho)] = {
            "max_drift_upper": d,
            "root_box": leaf["root_box"],
            "depth": leaf["depth"],
            "amp_lower_q": leaf["amp_lower_q"],
            "amp_upper_q": leaf["amp_upper_q"],
            "S_lower": rr["S_lower"],
            "certified": rr["certified"],
        }

    return {
        "iteration": "504Q",
        "gate": GATE,
        "preregistration_commit": PREREG,
        "classification": classification,
        "causal": CAUSAL,
        "block": BLOCK,
        "path": PATH,
        "root_boxes": list(ROOT_BOXES),
        "rhos": list(core.RHOS),
        "R_grid": list(core.R_GRID),
        "precision_bits": 384,
        "max_depth": MAX_DEPTH,
        "drift_threshold": 0.05,
        "robust_floor": 1.0,
        "full_channel_count": 243,
        "all_channels_recomputed_each_subbox": True,
        "channel_pruning_used_for_decision": False,
        "valid_cover": valid_cover,
        "all_controls": all_controls,
        "total_node_count": sum(b["node_count"] for b in boxes),
        "total_leaf_count": len(leaves),
        "certified_leaf_count": len(leaves) - len(unresolved),
        "unresolved_leaf_count": len(unresolved),
        "leaf_depth_histogram": dict(sorted(Counter(str(x["depth"]) for x in leaves).items())),
        "per_root_box_leaf_count": {str(b["root_box"]): len(b["leaves"]) for b in boxes},
        "root_max_possible_counts": {str(b["root_box"]): b["root_diagnostic"]["max_possible_count"] for b in boxes},
        "max_terminal_leaf_possible_count": max(x["max_possible_count"] for x in leaves),
        "max_terminal_leaf_drift_upper": worst["max_drift_upper"],
        "max_terminal_leaf_drift_witness": {
            "root_box": worst["root_box"],
            "depth": worst["depth"],
            "amp_lower_q": worst["amp_lower_q"],
            "amp_upper_q": worst["amp_upper_q"],
            "max_possible_count": worst["max_possible_count"],
            "leaf_status": worst["leaf_status"],
        },
        "minimum_terminal_leaf_S_lower": min_s,
        "per_rho_worst": per_rho,
        "covers": {str(b["root_box"]): b["cover"] for b in boxes},
        "boxes": boxes,
        "claim_ceiling": "known Iter504 crossing-region continuous diagnostic only; no full-domain continuous NONDECAY, Haar/divergence, D7 closure, selector, model/family or new-physics conclusion",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    direction, sign = parent.path_spec(BLOCK, PATH)
    if direction != [1, 1, 1, -1, -1, -1] or sign != 1:
        raise SystemExit("frozen path identity mismatch")

    try:
        boxes = [evaluate_box(k, direction, sign) for k in ROOT_BOXES]
        out = summarize(boxes)
    except Exception as exc:
        out = {
            "iteration": "504Q",
            "gate": GATE,
            "preregistration_commit": PREREG,
            "classification": INVALID,
            "error": repr(exc),
            "claim_ceiling": "invalid diagnostic execution only; no scientific conclusion",
        }

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps({k: v for k, v in out.items() if k != "boxes"}, indent=2, sort_keys=True))
    raise SystemExit(0 if out.get("classification") != INVALID else 2)


if __name__ == "__main__":
    main()
