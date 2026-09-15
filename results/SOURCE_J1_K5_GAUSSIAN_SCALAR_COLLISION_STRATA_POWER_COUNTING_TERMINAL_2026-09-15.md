# SOURCE_J1_K5_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING — terminal result

Date: 2026-09-15
Status: TERMINAL

## Authority

- Gate: `SOURCE_J1_K5_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING_GATE`
- Frozen preregistration: `research/prereg/SOURCE_J1_K5_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING_2026-09-15.md`
- Frozen preregistration commit: `2f6d3af60439af4bc8b7c62e6813c58fb21ec1f4`
- Implementation commit: `e742afd2360d087be457b2b0bccc8f72da6e9175`
- Workflow head: `02a8ecb2ab7b90ddfc9f25b9a6da8bb4b821cd4d`
- Authoritative run: `34959350188`
- Job: `104348959518`
- Artifact: `scalar-collision-strata-power-counting`, ID `10391514486`
- Artifact digest: `sha256:abaf3129d9555eed4d78f9fcb4464a60fd6c022cad82224431c9a5157ab11320`

## Frozen terminal classification

`AUX_GAUSSIAN_K5_PROPER_COLLISION_SUBDIVERGENCES_PRESENT_SCOPED`

All frozen controls passed, including all 120 vertex relabelings, exact Bell/multiplicity checks, scalar-dimension identities, explicit distinction from the historical 3D formula, and a synthetic changed-edge-scaling control.

## Exact result

K5 has 52 set partitions, 51 nontrivial collision partitions, and 50 proper collision strata after excluding the single full-collision partition.

Under the frozen scalar uniform power count

`omega = 3 E_int - d_perp`,

**all 50/50 proper collision strata are superficially divergent** (`omega >= 0`).

| partition type | multiplicity | E_int | d_perp | omega |
|---|---:|---:|---:|---:|
| 2+1+1+1 | 10 | 1 | 1 | 2 |
| 2+2+1 | 15 | 2 | 2 | 4 |
| 3+1+1 | 10 | 3 | 2 | 7 |
| 3+2 | 10 | 4 | 3 | 9 |
| 4+1 | 5 | 6 | 3 | 15 |
| 5 | 1 | 10 | 4 | 26 |

The proper-stratum omega values are `{2,4,7,9,15}`; the full collision reproduces the parent `omega=26`.

## Scientific meaning

Combined with the previous two terminal gates:

1. the frozen full-collision order<=26 radial action space is complete and rank 14;
2. that complete full-collision action did not remove the P1/P3 held-out divergence;
3. every proper K5 collision stratum is itself superficially divergent under the same scalar uniform power counting.

Therefore a **full-collision-only subtraction is structurally incomplete as a forest/stratified renormalization analysis** for this auxiliary scalar Gaussian witness.

This does not yet prove that a forest subtraction exists or yields a regulator-path-independent finite extension. It identifies the missing renormalization structure prospectively rather than increasing the full-collision polynomial degree post hoc.

## Next admissible frontier

Construct an exact connected-collision / laminar-forest certificate for K5:

- connected collision subsets are vertex subsets `S` with `2<=|S|<=5`;
- freeze their scalar degrees from the same formula;
- enumerate all compatible laminar families (`A subset B`, `B subset A`, or `A cap B = empty` for every pair);
- identify maximal forest depth, orbit/type census, and required proper-stratum counterterm orders before any numerical forest subtraction is attempted.

Only after that exact combinatorial contract is frozen should a stratified Gaussian subtraction gate be implemented.

## Claim ceiling

No Eq. (4) existence/nonexistence statement, no source authorization, no physical model failure, no D7-S2/S3/S4 closure, no terminal selector, and no Candidate Gravity activation.

RQIR Core v1.0 remains FROZEN; KMQGB remains downstream of pinned DSIR authority.
