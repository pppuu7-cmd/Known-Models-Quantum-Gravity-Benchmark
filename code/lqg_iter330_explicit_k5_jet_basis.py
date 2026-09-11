#!/usr/bin/env python3
"""Iter330: explicit K5 degree-8 invariant basis and centered-face jet audit.

This script upgrades the Iter323/329 dimension count to explicit polynomial
algebra.  Degree-8 O(3) scalars are degree-4 polynomials in Gram entries.
We enumerate all S5 orbit sums of degree-4 Gram monomials, impose centering
(sum_i y_i=0), and in four-vector coordinates quotient by the 4x4 Gram
determinant relation appropriate to vectors in R^3.

The K4/K3 tests are *candidate centered-stratum restrictions*, not a claim that
they are the physical/source-defined forest gluing maps.  We also compute
normal Taylor jets using integral rescalings that preserve centering:
  K4 face: y_i=a_i-t z (i=1..4), y_5=4 t z, sum a_i=0.
  K3 face: y_i=a_i-t(z4+z5) (i=1..3), y_4=3t z4, y_5=3t z5,
           sum a_i=0.
Thus t=0 is the centered lower stratum.  Ranks are exact over Q using sparse
Fraction Gaussian elimination after quotienting the Gram determinant relation.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

Exp = Tuple[int, ...]
GramPoly = Dict[Exp, int]
TGramPoly = Dict[Tuple[int, Exp], int]


def gram_pairs(n: int) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i, n)]


def degree_exponents(nvars: int, degree: int) -> Iterable[Exp]:
    for multiset in itertools.combinations_with_replacement(range(nvars), degree):
        e = [0] * nvars
        for k in multiset:
            e[k] += 1
        yield tuple(e)


def s5_orbits_degree4() -> Tuple[List[Tuple[int, int]], Dict[Exp, List[Exp]]]:
    pairs = gram_pairs(5)
    pidx = {p: i for i, p in enumerate(pairs)}
    maps: List[List[int]] = []
    for perm in itertools.permutations(range(5)):
        m = []
        for i, j in pairs:
            a, b = perm[i], perm[j]
            if a > b:
                a, b = b, a
            m.append(pidx[(a, b)])
        maps.append(m)

    def transform(e: Exp, m: Sequence[int]) -> Exp:
        out = [0] * len(e)
        for old, count in enumerate(e):
            if count:
                out[m[old]] += count
        return tuple(out)

    orbits: Dict[Exp, List[Exp]] = {}
    for e in degree_exponents(len(pairs), 4):
        images = sorted({transform(e, m) for m in maps})
        canonical = images[0]
        orbits.setdefault(canonical, images)
    return pairs, dict(sorted(orbits.items()))


def poly_add_term(poly: Dict, key, coeff: int) -> None:
    if coeff:
        poly[key] = poly.get(key, 0) + coeff
        if poly[key] == 0:
            del poly[key]


def determinant_relation_4() -> GramPoly:
    """det(H) for a symmetric 4x4 Gram matrix in 10 independent variables."""
    pairs = gram_pairs(4)
    pidx = {p: i for i, p in enumerate(pairs)}
    out: GramPoly = {}
    for perm in itertools.permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        coeff = -1 if inversions % 2 else 1
        e = [0] * len(pairs)
        for i, j in enumerate(perm):
            a, b = (i, j) if i <= j else (j, i)
            e[pidx[(a, b)]] += 1
        poly_add_term(out, tuple(e), coeff)
    return out

DET4 = determinant_relation_4()
DET4_PAIRS = gram_pairs(4)
DET4_PINDEX = {p: i for i, p in enumerate(DET4_PAIRS)}
DET4_PIVOT = tuple(1 if p in {(0, 0), (1, 1), (2, 2), (3, 3)} else 0 for p in DET4_PAIRS)
assert DET4[DET4_PIVOT] == 1


def reduce_det4(poly: GramPoly) -> GramPoly:
    """Canonical degree-4 representative modulo the one Gram determinant relation."""
    out = dict(poly)
    c = out.get(DET4_PIVOT, 0)
    if c:
        for e, d in DET4.items():
            poly_add_term(out, e, -c * d)
    assert out.get(DET4_PIVOT, 0) == 0
    return out


def const_coeff_vector(values: Sequence[int]) -> List[Dict[int, int]]:
    return [{0: v} if v else {} for v in values]


def t_coeff_vector(c0: Sequence[int], c1: Sequence[int]) -> List[Dict[int, int]]:
    out = []
    for a, b in zip(c0, c1):
        d: Dict[int, int] = {}
        if a:
            d[0] = a
        if b:
            d[1] = b
        out.append(d)
    return out


def dot_form_t(ci: Sequence[Dict[int, int]], cj: Sequence[Dict[int, int]]) -> Dict[Tuple[int, int], int]:
    """Return y_i.y_j as {(t_degree, Gram-variable-index): coefficient}."""
    n = len(ci)
    pairs = gram_pairs(n)
    pidx = {p: k for k, p in enumerate(pairs)}
    out: Dict[Tuple[int, int], int] = {}
    for a in range(n):
        for b in range(n):
            pa, pb = (a, b) if a <= b else (b, a)
            g = pidx[(pa, pb)]
            for da, ca in ci[a].items():
                for db, cb in cj[b].items():
                    poly_add_term(out, (da + db, g), ca * cb)
    return out


def dot_forms(vectors: Sequence[Sequence[Dict[int, int]]]) -> List[Dict[Tuple[int, int], int]]:
    return [dot_form_t(vectors[i], vectors[j]) for i, j in gram_pairs(5)]


def mul_tgram(a: TGramPoly, linear: Dict[Tuple[int, int], int], ngram: int, max_t: int) -> TGramPoly:
    out: TGramPoly = {}
    for (td, exp), c in a.items():
        for (dt, g), d in linear.items():
            nt = td + dt
            if nt > max_t:
                continue
            ee = list(exp)
            ee[g] += 1
            poly_add_term(out, (nt, tuple(ee)), c * d)
    return out


def expand_gram_monomial(e: Exp, forms: Sequence[Dict[Tuple[int, int], int]], ngram: int, max_t: int) -> TGramPoly:
    zero = (0,) * ngram
    poly: TGramPoly = {(0, zero): 1}
    for idx, count in enumerate(e):
        for _ in range(count):
            poly = mul_tgram(poly, forms[idx], ngram, max_t)
    return poly


def expand_orbit(orbit: Sequence[Exp], forms: Sequence[Dict[Tuple[int, int], int]], ngram: int, max_t: int) -> TGramPoly:
    out: TGramPoly = {}
    for e in orbit:
        piece = expand_gram_monomial(e, forms, ngram, max_t)
        for key, coeff in piece.items():
            poly_add_term(out, key, coeff)
    return out


def coefficient(poly: TGramPoly, tdeg: int) -> GramPoly:
    return {exp: c for (td, exp), c in poly.items() if td == tdeg and c}


def quotient_if_needed(poly: GramPoly, nbase: int) -> GramPoly:
    return reduce_det4(poly) if nbase == 4 else poly


def sparse_rank_q(rows: Sequence[Dict[object, int]]) -> int:
    """Exact sparse Gaussian rank over Q; row count is small (<=69)."""
    pivots: Dict[object, Dict[object, Fraction]] = {}
    ordered_pivots: List[object] = []
    for raw in rows:
        row: Dict[object, Fraction] = {k: Fraction(v) for k, v in raw.items() if v}
        for p in ordered_pivots:
            if p not in row:
                continue
            factor = row[p]
            prow = pivots[p]
            for k, v in prow.items():
                row[k] = row.get(k, Fraction(0)) - factor * v
                if row[k] == 0:
                    del row[k]
        if not row:
            continue
        p = min(row, key=repr)
        inv = Fraction(1, 1) / row[p]
        row = {k: v * inv for k, v in row.items()}
        pivots[p] = row
        ordered_pivots.append(p)
    return len(ordered_pivots)


def independent_basis(rows: Sequence[GramPoly], labels: Sequence[Exp]) -> Tuple[List[Exp], int]:
    pivots: Dict[object, Dict[object, Fraction]] = {}
    ordered_pivots: List[object] = []
    selected: List[Exp] = []
    for raw, label in zip(rows, labels):
        row: Dict[object, Fraction] = {k: Fraction(v) for k, v in raw.items() if v}
        for p in ordered_pivots:
            if p not in row:
                continue
            factor = row[p]
            prow = pivots[p]
            for k, v in prow.items():
                row[k] = row.get(k, Fraction(0)) - factor * v
                if row[k] == 0:
                    del row[k]
        if row:
            p = min(row, key=repr)
            inv = Fraction(1, 1) / row[p]
            row = {k: v * inv for k, v in row.items()}
            pivots[p] = row
            ordered_pivots.append(p)
            selected.append(label)
    return selected, len(ordered_pivots)


def desc(rep: Exp, pairs: Sequence[Tuple[int, int]]) -> str:
    factors: List[str] = []
    for idx, count in enumerate(rep):
        i, j = pairs[idx]
        factors.extend([f"g{i+1}{j+1}"] * count)
    return "*".join(factors) if factors else "1"


def configuration(kind: str) -> Tuple[int, List[List[Dict[int, int]]], int]:
    """Return nbase, five vector coefficient-polynomials, and max jet degree."""
    if kind == "k5":
        n = 4
        vecs = [const_coeff_vector([1 if a == i else 0 for a in range(n)]) for i in range(4)]
        vecs.append(const_coeff_vector([-1, -1, -1, -1]))
        return n, vecs, 0
    if kind == "k4face":
        n = 3
        vecs = [const_coeff_vector([1 if a == i else 0 for a in range(n)]) for i in range(3)]
        vecs += [const_coeff_vector([-1, -1, -1]), const_coeff_vector([0, 0, 0])]
        return n, vecs, 0
    if kind == "k3face":
        n = 2
        vecs = [const_coeff_vector([1, 0]), const_coeff_vector([0, 1]), const_coeff_vector([-1, -1]), const_coeff_vector([0, 0]), const_coeff_vector([0, 0])]
        return n, vecs, 0
    if kind == "k4jet":
        # base vectors: a1,a2,a3,z; a4=-(a1+a2+a3)
        n = 4
        vecs = [
            t_coeff_vector([1, 0, 0, 0], [0, 0, 0, -1]),
            t_coeff_vector([0, 1, 0, 0], [0, 0, 0, -1]),
            t_coeff_vector([0, 0, 1, 0], [0, 0, 0, -1]),
            t_coeff_vector([-1, -1, -1, 0], [0, 0, 0, -1]),
            t_coeff_vector([0, 0, 0, 0], [0, 0, 0, 4]),
        ]
        return n, vecs, 1
    if kind == "k3jet":
        # base vectors: a1,a2,z4,z5; a3=-(a1+a2)
        n = 4
        normal = [0, 0, -1, -1]
        vecs = [
            t_coeff_vector([1, 0, 0, 0], normal),
            t_coeff_vector([0, 1, 0, 0], normal),
            t_coeff_vector([-1, -1, 0, 0], normal),
            t_coeff_vector([0, 0, 0, 0], [0, 0, 3, 0]),
            t_coeff_vector([0, 0, 0, 0], [0, 0, 0, 3]),
        ]
        return n, vecs, 2
    raise ValueError(kind)


def build_basis() -> Tuple[List[Tuple[int, int]], Dict[Exp, List[Exp]], List[Exp], int]:
    pairs5, orbits = s5_orbits_degree4()
    nbase, vecs, _ = configuration("k5")
    forms = dot_forms(vecs)
    ngram = len(gram_pairs(nbase))
    rows: List[GramPoly] = []
    labels = list(orbits)
    for rep in labels:
        expanded = expand_orbit(orbits[rep], forms, ngram, 0)
        rows.append(reduce_det4(coefficient(expanded, 0)))
    selected, rank = independent_basis(rows, labels)
    return pairs5, orbits, selected, rank


def image_rows(selected: Sequence[Exp], orbits: Dict[Exp, List[Exp]], kind: str, through_jet: int) -> List[Dict[object, int]]:
    nbase, vecs, max_jet = configuration(kind)
    assert through_jet <= max_jet
    forms = dot_forms(vecs)
    ngram = len(gram_pairs(nbase))
    rows: List[Dict[object, int]] = []
    for rep in selected:
        expanded = expand_orbit(orbits[rep], forms, ngram, through_jet)
        flat: Dict[object, int] = {}
        for td in range(through_jet + 1):
            cp = quotient_if_needed(coefficient(expanded, td), nbase)
            for exp, c in cp.items():
                if c:
                    flat[(td, exp)] = c
        rows.append(flat)
    return rows


def run(mode: str) -> dict:
    pairs5, orbits, selected, basis_rank = build_basis()
    assert len(orbits) == 69
    assert basis_rank == 16
    assert len(selected) == 16

    basis_info = [{"representative": desc(r, pairs5), "orbit_size": len(orbits[r])} for r in selected]
    common = {
        "iteration": 330,
        "mode": mode,
        "degree_vector": 8,
        "degree_gram": 4,
        "s5_orbit_count_before_relations": len(orbits),
        "k5_exact_invariant_rank": basis_rank,
        "basis": basis_info,
    }

    if mode == "basis":
        common.update({
            "gram_relation": "det(Gram_4x4)=0 for four centered-coordinate vectors in R3",
            "result": "EXPLICIT_16_DIMENSIONAL_BASIS_SELECTED",
        })
    elif mode == "k4":
        face = sparse_rank_q(image_rows(selected, orbits, "k4face", 0))
        jet0 = sparse_rank_q(image_rows(selected, orbits, "k4jet", 0))
        jet1 = sparse_rank_q(image_rows(selected, orbits, "k4jet", 1))
        assert face == jet0 == 11
        assert jet1 == 16
        common.update({
            "face_value_rank": face,
            "face_value_kernel_dimension": 16 - face,
            "cumulative_normal_jet_ranks": {"0": jet0, "1": jet1},
            "first_jet_detects_full_k5_space": True,
        })
    elif mode == "k3":
        face = sparse_rank_q(image_rows(selected, orbits, "k3face", 0))
        jet0 = sparse_rank_q(image_rows(selected, orbits, "k3jet", 0))
        jet1 = sparse_rank_q(image_rows(selected, orbits, "k3jet", 1))
        jet2 = sparse_rank_q(image_rows(selected, orbits, "k3jet", 2))
        assert face == jet0 == 4
        assert jet1 == 7
        assert jet2 == 16
        common.update({
            "face_value_rank": face,
            "face_value_kernel_dimension": 16 - face,
            "cumulative_normal_jet_ranks": {"0": jet0, "1": jet1, "2": jet2},
            "second_jet_detects_full_k5_space": True,
        })
    else:
        raise ValueError(mode)

    common["scope"] = [
        "EXACT_POLYNOMIAL_ALGEBRA_OVER_Q",
        "CENTERED_STRATUM_RESTRICTION_MODEL",
        "NOT_SOURCE_DEFINED_FOREST_GLUING_MAP",
        "JET_DETECTABILITY_DOES_NOT_IMPLY_JET_NORMALIZATION",
        "NOT_PHYSICAL_COUNTERTERM_COUNT",
        "DOES_NOT_PROVE_UNIQUE_EXTENSION",
        "LQG_REMAINS_PARTIAL_BLOCKED",
        "D7_NOT_AUTHORIZED",
    ]
    return common


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["basis", "k4", "k3"], required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    result = run(args.mode)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
