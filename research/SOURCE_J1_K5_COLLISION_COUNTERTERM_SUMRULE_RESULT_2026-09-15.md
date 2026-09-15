# Terminal result — K5 collision-counterterm ambiguity versus EPRL sum rule

Date: 2026-09-15
Status: `TERMINAL_SCOPED`
Classification: `SOURCE_J1_K5_EPRL_SUMRULE_DOES_NOT_FIX_COLLISION_EXTENSION_SCOPED`

## Frozen authority

- preregistration: `research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_PREREG_2026-09-15.md`
- frozen prereg commit: `7e38d2a3aac339a7133e51b5589f3ba23b7f42c3`
- exact implementation: `code/source_j1_k5_collision_counterterm_sumrule_certificate.py`
- implementation commit: `4b7598cf6f2c2a7b8964b373e965d950eaafe26f`
- workflow head: `260fa3abd5290bf51a1ae6c72f64ad6bb7cf7c3c`

## Authoritative run

- workflow run: `34916367231`
- source-lock job: `104214750411`, success
- exact-certificate job: `104214778424`, success
- artifact: `10376212425`
- artifact name: `source-j1-k5-collision-counterterm-sumrule`
- artifact digest: `sha256:8a394c79c533f123d2d7913b5feb49e3c0258b7a7a8be3560010df7bccd4f7d6`

## Exact certified witness

K5 has ten wedge signs, hence `1024` independent sign patterns. The constrained causal image

`kappa_ab = sigma_a sigma_b`

contains exactly `16` distinct edge-sign patterns, each with exactly two `sigma` preimages related by global reversal. The complement therefore contains exactly `1008` patterns.

Freeze a local collision-supported zeroth-order counterterm `delta_N` and coefficients

- `+63` on every constrained causal pattern;
- `-1` on every unconstrained pattern.

The exact certificate verified:

- `16*63 + 1008*(-1) = 0`;
- full independent-sign counterterm sum = `0`;
- constrained distinct-pattern shift = `1008`;
- constrained sigma-counted shift = `2016`;
- all `5! = 120` K5 vertex permutations preserve constrained membership and the coefficient family;
- all `120*1024 = 122880` explicit permutation-pattern checks pass;
- `sd(delta_N)=12 <= 30`, so this zeroth-order counterterm lies inside the already certified same-scaling extension window;
- the uniform-nonzero adversarial family fails the EPRL zero-sum condition as required;
- the zero-constrained adversarial family has no causal shift as required.

## Scientific interpretation

The exact EPRL independent-sign decomposition, even supplemented by K5 permutation symmetry and the frozen same-scaling-degree ceiling, does **not** uniquely fix collision-supported extension coefficients of the causal sectors.

The explicit witness preserves the full EPRL sign sum exactly while shifting every constrained causal K5 sector by the same nonzero local collision term.

Therefore the one-wedge identity `T+ + T- = D` and the resulting EPRL sum rule cannot, by themselves, serve as a uniqueness condition for the causal full-collision extension.

Any uniqueness theorem for Eq. (4) must impose at least one additional source-faithful joint-limit/normalization condition that excludes this witness.

## Claim ceiling

This result does **not** prove:

- that the published causal vertex is ultimately nonunique;
- that `delta_N` is selected by the source;
- that every allowed symmetry/normalization condition leaves this ambiguity;
- that Eq. (4) fails to exist;
- that a source-faithful joint prescription cannot remove the ambiguity;
- closure of D7-S2, D7-S3 or D7-S4;
- any terminal selector.

It proves only that off-collision agreement + the frozen scaling ceiling + K5 permutation symmetry + the EPRL independent-sign sum rule are insufficient, in combination, to fix the scoped collision counterterm.

## Frontier consequence

`SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_GATE` must now explicitly identify the additional source condition, if any, that selects a unique collision extension. Merely citing Eq. (5)/(6) is no longer sufficient.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.
