# Iter504S — execution-only dual-derivative extraction repair

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN BEFORE ANY REPAIRED EXECUTION AND BEFORE CONSUMING ITER504S SUBSTANTIVE OUTPUT

Parent scientific preregistration remains unchanged:

`f6367456aa715fe6282ab70c1b2005971a4568c7`

Parent gate remains:

`ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR`

## Outcome-blind defect discovery

While the first Iter504S run `35173442220` was still in progress and before any root/assembly science artifact had been consumed, a static implementation audit found a representation error in `code/iter504s_mechanism_discriminator.py`.

`iter503_ad_core.dcontract_all()` returns the full dual contraction object (`CD`) in each channel. The established Iter504R construction obtains the rigorous derivative ball from each dual channel using `as_c(dualvals[idx]).d` inside `iter503_ad_core.centered_channels()`.

The first Iter504S implementation instead assigned the full `CD` objects to `dvals` and attempted to form

`rvals + dvals * delta`

without extracting the derivative component. Its derivative-center helper likewise attempted to midpoint the wrong representation rather than the `.d` Acb derivative ball.

This is an implementation/type-representation defect. It does not change any frozen scientific question or criterion.

## Frozen minimal repair

The only authorized scientific-code repair is:

1. convert every dual contraction entry `z` to the derivative ball `ad.as_c(z).d` before any root-affine point displacement is formed;
2. in the rigorous full-D treatment use that unchanged full-root derivative ball exactly as Iter504R does;
3. in the already-preregistered control-only derivative-radius-collapse sensitivity use the deterministic midpoint of that extracted derivative Acb ball;
4. make no other change to source geometry, KAK, Toller source, intertwiner, contraction, exact diagnostic points, roots, rho/R grids, precision, channel count, no-pruning rule, slope formulas, threshold, floor, mechanism flags, terminal classifier or claim ceiling.

The Haar/log derivative treatment is unchanged: rigorous full-D uses `mr['dlogH'].d`, center sensitivity uses the midpoint of that same derivative ball.

## Execution rule

Do not dispatch a repaired Iter504S scientific execution while run `35173442220` is queued/running.

After `35173442220` becomes terminal:

- if it fails at the predicted dual-derivative representation point, classify the first run as infrastructure/implementation failure, not science;
- apply exactly the repair above;
- update only source-lock implementation hashes as required;
- launch one repaired Iter504S execution;
- if the terminal failure is materially different, do not use this preregistration to hide it; localize the actual defect first.

No partial or failed Iter504S values may be used as scientific evidence.
