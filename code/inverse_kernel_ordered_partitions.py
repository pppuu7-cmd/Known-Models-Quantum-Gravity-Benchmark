"""Generate ordered-set-partition response terms for derivatives of G=K^{-1}.

Methodology helper for source/contact completeness. This is not Candidate Gravity dynamics.
"""

from __future__ import annotations

from itertools import permutations


def set_partitions(items):
    """Yield unordered set partitions as tuples of tuples, canonicalized by construction."""
    items = tuple(items)
    if not items:
        yield tuple()
        return

    first, rest = items[0], items[1:]
    for part in set_partitions(rest):
        # New singleton block first.
        yield ((first,),) + part
        # Insert `first` into each existing block.
        for i in range(len(part)):
            block = tuple(sorted((first,) + tuple(part[i])))
            new = list(part)
            new[i] = block
            # Canonicalize block order to suppress duplicates in unordered generator.
            new_sorted = tuple(sorted(new, key=lambda b: (min(b), len(b), b)))
            yield new_sorted


def unique_set_partitions(items):
    seen = set()
    for p in set_partitions(items):
        canon = tuple(sorted((tuple(sorted(b)) for b in p), key=lambda b: (min(b), len(b), b)))
        if canon not in seen:
            seen.add(canon)
            yield canon


def ordered_set_partitions(items):
    """Yield every ordered partition exactly once."""
    for p in unique_set_partitions(tuple(items)):
        for order in permutations(p):
            yield order


def response_terms(n: int):
    """Return symbolic ordered-partition terms for D_{1...n} G."""
    labels = tuple(range(1, n + 1))
    out = []
    for ordered in ordered_set_partitions(labels):
        k = len(ordered)
        sign = -1 if k % 2 else 1
        blocks = tuple(tuple(b) for b in ordered)
        out.append((sign, blocks))
    return out


def family_counts(n: int):
    counts = {}
    for sign, blocks in response_terms(n):
        k = len(blocks)
        counts[k] = counts.get(k, 0) + 1
    return counts


def format_term(sign, blocks):
    pieces = ["G"]
    for b in blocks:
        label = "".join(str(x) for x in b)
        pieces.extend([f"K_{label}", "G"])
    prefix = "+" if sign > 0 else "-"
    return prefix + " " + " ".join(pieces)


def self_test():
    expected = {
        1: {1: 1},
        2: {1: 1, 2: 2},
        3: {1: 1, 2: 6, 3: 6},
        4: {1: 1, 2: 14, 3: 36, 4: 24},
    }
    got = {n: family_counts(n) for n in expected}
    assert got == expected, (got, expected)
    return {
        "family_counts": got,
        "total_terms": {n: sum(got[n].values()) for n in got},
        "order3_terms": [format_term(*term) for term in response_terms(3)],
    }


if __name__ == "__main__":
    print(self_test())
