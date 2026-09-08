"""Exhaustive small-library selector for KMQGB minimal discriminating test suites.

Methodology helper only; not Candidate Gravity dynamics or final resource estimation.
"""

from __future__ import annotations

from itertools import combinations
import numpy as np


def inv_sqrt(sigma: np.ndarray, rtol: float = 1e-12) -> np.ndarray:
    vals, vecs = np.linalg.eigh(sigma)
    vmax = float(np.max(np.abs(vals))) if vals.size else 0.0
    if vmax == 0.0:
        return np.zeros_like(sigma)
    keep = vals > rtol * vmax
    v = vecs[:, keep]
    return (v * (1.0 / np.sqrt(vals[keep]))) @ v.T


def metrics(sigma: np.ndarray, j_c: np.ndarray, j_kg: np.ndarray, rtol: float = 1e-12):
    w12 = inv_sqrt(sigma, rtol=rtol)
    a = w12 @ j_c
    pi = np.eye(a.shape[0]) - a @ np.linalg.pinv(a, rcond=rtol)
    b = pi @ w12 @ j_kg

    rank_c = np.linalg.matrix_rank(a, tol=rtol)
    svals = np.linalg.svd(b, compute_uv=False)
    if svals.size:
        keep = svals > rtol * svals[0]
        nz = svals[keep]
    else:
        nz = np.array([])

    return {
        "d_perp": int(sigma.shape[0] - rank_c),
        "rank_kg": int(nz.size),
        "sigma_min_plus": float(nz[-1]) if nz.size else 0.0,
    }


def _indices_for_subset(blocks, subset):
    idx = []
    for i in subset:
        idx.extend(blocks[i]["indices"])
    if len(set(idx)) != len(idx):
        raise ValueError("Reference exhaustive selector assumes disjoint observable blocks.")
    return np.array(idx, dtype=int)


def evaluate_subset(sigma, j_c, j_kg, blocks, subset, rtol=1e-12):
    idx = _indices_for_subset(blocks, subset)
    s = sigma[np.ix_(idx, idx)]
    jc = j_c[idx, :]
    jkg = j_kg[idx, :]
    out = metrics(s, jc, jkg, rtol=rtol)
    out["cost"] = float(sum(blocks[i]["cost"] for i in subset))
    out["blocks"] = [blocks[i]["name"] for i in subset]
    return out


def exhaustive_minimal_suite(
    sigma,
    j_c,
    j_kg,
    blocks,
    d_target=1,
    rank_target=1,
    sigma_min_target=0.0,
    rtol=1e-12,
):
    """Return cheapest feasible subset; tie-break by fewer blocks then larger sigma_min."""
    feasible = []
    n = len(blocks)
    for k in range(1, n + 1):
        for subset in combinations(range(n), k):
            m = evaluate_subset(sigma, j_c, j_kg, blocks, subset, rtol=rtol)
            if (
                m["d_perp"] >= d_target
                and m["rank_kg"] >= rank_target
                and m["sigma_min_plus"] >= sigma_min_target
            ):
                feasible.append((subset, m))
    if not feasible:
        return None
    feasible.sort(key=lambda x: (x[1]["cost"], len(x[0]), -x[1]["sigma_min_plus"]))
    return feasible[0][1]


def leave_one_block_robustness(sigma, j_c, j_kg, blocks, selected_names, rtol=1e-12):
    name_to_i = {b["name"]: i for i, b in enumerate(blocks)}
    selected = [name_to_i[n] for n in selected_names]
    folds = []
    for drop in selected:
        remain = tuple(i for i in selected if i != drop)
        if not remain:
            folds.append({"dropped": blocks[drop]["name"], "d_perp": 0, "rank_kg": 0, "sigma_min_plus": 0.0})
            continue
        m = evaluate_subset(sigma, j_c, j_kg, blocks, remain, rtol=rtol)
        m["dropped"] = blocks[drop]["name"]
        folds.append(m)
    return folds


def self_test():
    # Four disjoint 1D blocks; shared comparator parameter, one KG direction.
    sigma = np.eye(4)
    j_c = np.array([[1.0], [1.0], [1.0], [1.0]])
    j_kg = np.array([[1.0], [-1.0], [0.5], [-0.5]])
    blocks = [
        {"name": "A", "indices": [0], "cost": 1.0},
        {"name": "B", "indices": [1], "cost": 1.0},
        {"name": "C", "indices": [2], "cost": 2.0},
        {"name": "D", "indices": [3], "cost": 2.0},
    ]
    suite = exhaustive_minimal_suite(sigma, j_c, j_kg, blocks, d_target=1, rank_target=1)
    assert suite is not None
    folds = leave_one_block_robustness(sigma, j_c, j_kg, blocks, suite["blocks"])
    return {"suite": suite, "leave_one_block": folds}


if __name__ == "__main__":
    print(self_test())
