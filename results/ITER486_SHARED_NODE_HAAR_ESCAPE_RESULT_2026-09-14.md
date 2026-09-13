# Iter486 — shared-node full-network Haar escape envelope

Date recorded: 2026-09-14
Terminal classification: `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486`

## Frozen authority
- Haar source pin: `2cbfa37aea635bd76e1fb0291191b6efb32699cc`
- preregistration: `4e1098865dfdec5d4eebacb2d055c17a0a6f2b2c`
- implementation: `f3e8bfcbabddf5c2262eb2a98a04e76343aff3fe`
- aggregate classifier: `4774e98c5dfa7ed1f7f6cdefd2e101c7aed99266`
- initial workflow: `1cc85b617c936917155af0fb36a4f529dc6a8ba5`
- dependency-only repair / authoritative retry head: `3898fea010098b1ce3268669c72a0f9af2f01cc4`
- initial run `34789214904`: pre-science dependency failure (`sympy` missing); no scientific classification
- authoritative retry run: `34789259423`
- source-lock job: `103810316891`
- aggregate job: `103810617969`
- aggregate artifact: `10327790459`
- aggregate artifact digest: `sha256:6c7269bac6124e1736d07ca5d642a552e4fcda0a34ff7528363dbd0a18dc7892`

## Frozen aggregate
All 24/24 expected scientific lanes produced raw JSON. The aggregate nevertheless returns `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486` because 18/24 lanes fail a prospectively frozen validation control. The six `s=1` lanes are valid; all `s=2,3,4` lanes are invalid. Under the preregistration, any invalid lane prevents promotion of any scientific slope label.

Aggregate diagnostics:
- present lanes: `24/24`;
- valid decay lanes: `6` (`A/C x s=1 x all three causal patterns`);
- invalid lanes: `18` (all `s=2,3,4`);
- raw DECAY point count: `48`;
- raw NONDECAY point count: `29`;
- raw ASYMPTOTIC_INCONCLUSIVE point count: `19`;
- actual-envelope slope range across raw points: `[-2.0008639881649826, 4.0014273903933635]`;
- maximum slope drift: `0.04163031246044513`, below the frozen `0.05` stability ceiling.

## Exact reason for invalidation
The failing control is the inherited **absolute** Toller nonrepresentation mismatch at the escaped scale. The network matrices themselves decay exponentially in large-rapidity sectors, so the absolute quantity
`||T(g2 g1)-T(g2)T(g1)||`
can fall below the fixed `1e-5` activity threshold even when the relative nonrepresentation mismatch remains nonzero. This makes that negative control nonuniform in scale.

Example: lane `A-s4-2to3` has
- stable raw actual-envelope slopes approximately `3.99898, 4.00028, 4.00033, 4.00009` over the four frozen rho witnesses;
- maximum frozen slope drift well below `0.05`;
- independent-edge cycle-break control strongly active (`~51.99`);
- source KAK reconstruction `~6.6e-13`;
- source additive regression `~6.6e-15`;
- Haar bookkeeping residual `~3.6e-15`;
- but absolute Toller nonrepresentation mismatch only `~2.0e-09`, below the frozen `1e-5` threshold.

Therefore the `s=4` raw NONDECAY signal is scientifically interesting but **not promotable in Iter486**. The frozen criterion is not weakened or repaired post hoc.

## Diagnostic structure, not a promoted theorem
The valid `s=1` lanes show stable post-Haar DECAY with actual slopes near `-2`. Raw `s=3` lanes are near marginality (`actual slope ~0`) and mix inconclusive/nondecay points. Raw `s=4` lanes show strong stable growth near `+4`. These patterns motivate a new prospectively preregistered gate with a scale-normalized nonrepresentation control; they are not themselves an Iter486 scientific PASS/FAIL because the relevant lanes are invalid.

## Interpretation ceiling
Iter486 establishes no Haar divergence theorem, no physical causal-vertex divergence theorem, no conditional/PV or distributional conclusion, no ten-spectral-integral result, no D7-S2 closure, no terminal D7 classifier, and no Candidate Gravity authorization.

## Next permitted gate
A new prospective gate may repeat the exact same Haar-escape scientific object and slope thresholds while replacing only the scale-nonuniform validation control by a dimensionless relative nonrepresentation mismatch, plus an undeformed-base absolute nonrepresentation regression. This must be a new preregistered iteration, not a repair of Iter486.