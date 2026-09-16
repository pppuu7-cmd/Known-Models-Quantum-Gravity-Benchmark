# Preregistration — SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_GATE

Date: 2026-09-16

## Parent authority

This gate consumes only the source-locked local `j=1`, fixed-tangent K5 triangle highest-contact `delta''` realization and the terminal repaired V7 exact Gaussian regulator outputs. It does not alter V4/V5/V6/V7 history.

Authoritative repaired V7 run at freeze time: `35067251385` on head `b6f78151443dfc78c6ae07ceadf9977964a36df3`.

Frozen V7 exact scale-free diagnostics:

- A `(1,1,1)`: `1600/531441`;
- A4 `(4,4,4)`: `1600/531441`;
- B `(1,1,4)`: `204800/1162261467`;
- C `(1,2,3)`: `14400/19487171`.

The A/B/C inequality is consumed only as scoped Gaussian regulator-scheme dependence. It is not all-mollifier dependence, extension nonexistence, full-K5 failure, or model/family failure.

## Scientific question

Can the frozen relative-width dependence of the local `delta''` triangle be absorbed by a collision-supported local counterterm belonging to a source-authorized finite counterterm class, while preserving the off-collision object and the frozen permutation/covariance constraints?

## Frozen admissible counterterm class

Work in the same local normal coordinates `B12=x`, `B23=y`, `B13=x+y` used by V6/V7. The counterterm is supported only at the triple collision `x=y=0` and must not modify the off-collision distribution.

The implementation must construct the finite local jet basis allowed by the parent derivative order and frozen permutation symmetry, derive its action on the same normalized Gaussian test/regulator family used by V7, and solve the resulting exact rational linear system. No basis element may be added after observing the solve result.

The implementation must report separately:

1. `SOURCE_FIXED_UNIQUE_SCOPED` — source/prior authority fixes all finite local coefficients and the exact V7 A/B/C differences are absorbed uniquely;
2. `SOURCE_UNFIXED_FINITE_LOCAL_FREEDOM_SCOPED` — absorption is possible but at least one finite local coefficient is not fixed by existing source authority;
3. `COUNTERTERM_CLASS_INSUFFICIENT_SCOPED` — no exact solution exists in the prospectively frozen admissible local class;
4. `MISSING_AUTHORITY_BLOCKED` — required source information needed to define/fix the class is absent;
5. `INVALID_IMPLEMENTATION` — provenance, exact controls, symmetry controls, or independent-lane agreement fail.

These labels are scoped child-gate labels only. None authorizes terminal D7 classification or `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`.

## Mandatory exact controls

- Reproduce V7 A/A4/B/C exactly from the authoritative source-locked realization before solving any counterterm system.
- Common-rescaling control: A4 must equal A exactly.
- Off-collision identity control: every admissible counterterm basis element must vanish on test functions supported away from the collision.
- Permutation/covariance control: the frozen basis and solved coefficients must transform consistently under the triangle permutations admitted by the parent realization.
- Rank/nullity control: report exact rational matrix rank, augmented rank, nullity, and a canonical exact solution when one exists.
- Synthetic positive fixture: construct an outcome-independent synthetic regulator-difference vector known to lie in the frozen counterterm span and require exact recovery.
- Synthetic negative fixture: construct an outcome-independent vector outside the frozen span and require exact rejection.
- Provenance/source-lock control against the authoritative V4/V5/V7 records; do not infer missing authority from prose-string absence alone.

## Execution contract

Use exact rational/symbolic arithmetic for all decision-critical fields. Run independent Python 3.11 and Python 3.13 matrix lanes with `fail-fast:false` and safe parallelism, followed by an aggregate job that exact-compares classification, basis, rank/nullity, solution data, controls, source locks, and canonical JSON SHA256.

No tolerance relaxation, basis enlargement, regulator-family change, or interpretation-ceiling change is permitted after execution. Any implementation defect is repaired under this same contract and must not be relabeled as a scientific failure.

## Governance / claim ceiling

- `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED` at preregistration.
- Candidate Gravity remains inactive.
- This gate concerns only finite local counterterm equivalence for the frozen local `delta''` triangle within the V7 Gaussian regulator family.
- A unique solution is not a full-K5 theorem; finite freedom is not new physics; insufficiency of this finite class is not extension nonexistence or model failure.
