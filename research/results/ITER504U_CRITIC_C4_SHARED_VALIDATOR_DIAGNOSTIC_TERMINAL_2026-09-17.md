# Iter504U Critic C4 shared-validator diagnostic — terminal methodology result

Date: 2026-09-17

## Status

`ITER504U_CRITIC_C4_FIXTURE_REPAIR_VALIDATED_SCOPED`

This is a methodology/control-layer result only. It is not an Iter504U scientific classification and it consumed no production science payload.

## Authority chain

- formal repair preregistration: `662e1b40c4584a5b1989b821cd7a5c334ef8fc44`
- diagnostic-only preregistration: `dd8ea4c0f6df3f0da6139e293d6b8fd5bea5d02a`
- diagnostic workflow commit: `7cd6c8110077362d227b5ebf869887d44d473c97`
- diagnostic workflow blob: `9675aa8176971cf13c03a6748a641eed2abece4f`
- diagnostic authority commit: `79e4a6a1e6ee100812f6247219fa79501c3720f3`
- single launch/head: `c0f45fb93a2298221fb0c60a2b2ee770a8bb8dc2`
- workflow run: `35252175158`, attempt 1, `completed/success`
- original Critic blob: `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`
- repaired wrapper blob actually source-locked and executed: `bcea2946a0f9676b50897dc4bbe74fa1122a9965`
- synthetic evaluator blob: `20a854869dbd0a61824b6c7e8a4f829507f5b126`

The diagnostic source-lock explicitly recomputed `git hash-object` for the original Critic, repaired wrapper and evaluator before replay. The wrapper identity above therefore supersedes any non-repository transcription of that hash.

## Shared-validator result

Both Python 3.11 and 3.13 replay lanes completed successfully. The aggregate required byte-for-byte equality of `result.json` and `returncode.txt` and passed.

The common `base.validate_all` path established:

- coherent baseline fixture accepted: `baseline_validation_errors=[]`;
- deterministic contradiction rejected exactly as `H0_AMP_LOW:C4_leaf_binding`;
- false-carrier variant rejected exactly as `H0_AMP_LOW:C4_leaf_binding`;
- repaired `C4_true_leaf_false_rho` negative control = `true`;
- all other repaired negative controls = `true`;
- `production_science_consumed=false`;
- `source_run_classified=false`;
- evaluator `errors=[]`;
- payload SHA256: `974114fb7fd1d062984846cb9c984d1ec0bed1df915fb2f25aac871f5ab7242f`.

## Immutable diagnostic artifacts

- Python 3.11: artifact `10510475771`, digest `sha256:583c1935ee815b7d4ba80e0396212d725933f6eabe4ac1f8fb4279f3a16ad0a1`
- Python 3.13: artifact `10510765344`, digest `sha256:f768f75cdc9794d70c4b5cced1ee8692c2fb8e38873094251baed9694c907cea`
- aggregate: artifact `10509679536`, digest `sha256:9df7eed7be9e89c0083d2cb6b0631f3d190b12085253b5786e8808ba70883880`

All three artifacts were non-expired at terminalization.

## Interpretation

The previously identified `C4_true_leaf_false_rho` issue is closed as a synthetic Critic/control-fixture implementation defect at this scoped methodology layer. It does not alter the producer evaluator, assembler, aggregate classifier, held-out cohort, source realization, precision, R/rho grids, threshold, robust floor, `MAX_DEPTH`, partition, local-D method, or PASS/INCONCLUSIVE scientific contract.

Historical failed/insufficient methodology attempts remain historical `INVALID_IMPLEMENTATION`; they are not scientific FAILs.

## Downstream rule

Run `35246605860` remains the one authoritative Iter504U production. Do not rerun producer science merely because of the historical Critic-fixture defect. Once that production is terminal, freeze the exact required artifact IDs/digests prospectively and run the repaired independent Critic closure against those immutable artifacts only.

Claim ceiling: Critic C4 synthetic fixture repair validated at the methodology/control layer only; no Iter504U scientific classification and no all-domain/global promotion.
