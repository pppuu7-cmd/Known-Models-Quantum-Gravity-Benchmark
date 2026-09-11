# Iter302A — Peer-Reviewed Toller Authority Provenance Delta

Date: 2026-09-11

This is a provenance-only delta. It does **not** modify the prospectively frozen Iter302 claims, thresholds, scope rule, machine classification, or D7 status.

The Iter302 source object Bianchi–Chen–Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, originally frozen by arXiv identifier `2604.24945`, has a peer-reviewed journal version:

- Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, **Physical Review D 114, 046014**, published **13 August 2026**.
- DOI: `10.1103/v3kc-4n3n`.
- The journal abstract retains the central source identity used by Iter302: the Toller functions `T^(±)` satisfy `T^(+) + T^(-) = D`, with `D` the unitary irreducible `SL(2,C)` Wigner representation.

Disposition:
- authority level for the Iter302 source is upgraded from public preprint provenance to `PEER_REVIEWED`;
- frozen Iter302 result remains unchanged;
- no family-level PASS/FAIL follows;
- D2, D4 and D7 are unchanged;
- Candidate Gravity remains inactive.

The benchmark contract `benchmarks/lqg_iter302_toller_half_link_composition.json` is intentionally not rewritten after the scientific run; this delta prevents post-hoc modification of the prospectively frozen input while preserving exact later authority provenance.
