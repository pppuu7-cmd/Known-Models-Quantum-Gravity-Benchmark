# SOURCE_J1_K5_P1_S4_FOREST_ORBIT_REDUCTION — terminal result

Date: 2026-09-15
Status: TERMINAL

## Authority

- Frozen preregistration commit: `10e2baf2016f8c7a02cf40d0a96afee1849c2087`
- Implementation commit: `3c319a23537c158644452921e442b406695d6be8`
- Workflow head: `6c2b1b7805710ca0145e53f9d11e9a7f49ae6c48`
- Authoritative run: `34991740712`
- Source-lock job: `104457837547` — success
- Python 3.11 job: `104457873738` — success
- Python 3.12 job: `104457873718` — success
- Python 3.11 artifact: ID `10406335562`, digest `sha256:8d9ba93cc70260796bf800c4652706f606e4c40ff736a922896903aae4b7403d`
- Python 3.12 artifact: ID `10404979304`, digest `sha256:46ec66642d837d1f2a110881d0826cc4f32cb158f40f77609916446e40f8b988`

## Frozen classification

`P1_S4_FOREST_ORBIT_REDUCTION_CONFIRMED_SCOPED`

Both independent Python lanes emitted the same exact scientific payload.

## Exact P1 symmetry

P1 uses lexicographic K5 edge order

`(01,02,03,04,12,13,14,23,24,34)`

with regulator exponents

`(1,1,1,1,2,2,2,2,2,2)`.

The exact stabilizer fixing vertex `0` is `S4`, order `24`, and every group element preserves the P1 exponent map and the exact scalar forest operator modulo the fixed gauge.

## Exact forest reduction

The 236 proper-only forests split into exactly **29 P1 S4-orbits**.

Orbit-size histogram:

`{1:2, 3:2, 4:6, 6:6, 12:12, 24:1}`.

Representative-list digest:

`sha256:22184a85593831b3aba52d02517b8e1bf458d8c4aee5ac9044289655eca4d4ac`.

The forest sign `(-1)^|F|` is constant on every orbit.

An exact S4-invariant integer fixture gave the same full and orbit-weighted signed sum:

`-3696 = -3696`.

A deliberately non-invariant fixture gave different sums:

`-72 != -98`,

so representative weighting is not silently applied outside the frozen symmetry class.

## Exact workload reduction

For the structural jet-box count

`J(F)=product_{S in F}(r(S)+1)`

with scalar orders `2,7,15`, the full 236-forest total is

`32646`,

while one representative per P1 orbit requires

`2761`.

Thus the exact structural reduction factor is

`32646 / 2761 ≈ 11.8239768`.

This is a computational workload certificate, not a scientific observable.

## Consequence

A later P1 numerical forest-subtraction gate may evaluate 29 exact S4 representatives and weight them by orbit size instead of evaluating all 236 forests, provided the numerical kernel preserves the same P1 symmetry and includes an explicit symmetry replay control.

## Interpretation ceiling

This result is only an exact computational symmetry reduction. It does not establish forest-subtracted convergence/divergence, Eq. (4), model/family failure, D7 closure, any terminal selector, or Candidate Gravity activation.

Governance remains unchanged.