# Independent Critic — SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_GATE

Date: 2026-09-16
Verdict: `CRITIC_CONFIRMS_SCOPED_IDENTITY_PASS_NO_RANK_PROMOTION`

## Material independently checked

- Primary locked extraction `sources/arxiv_2601_23162v1_eq4_triangle_wedge_group_argument_identity_v15.json`, backed by PDF SHA256 `cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713`.
- Gate preregistration `ddf246b861d4e367af409e3ae5b6c97ccfd1ea7e`.
- Frozen authority `440c853516c2357029c848c83e48a7f6a39d0c86`.
- Classifier `1f48955a2f8b15a544121ab07675cdba8830907f` and aggregate `a4263330c207b5fdc048fa1996a3e64652490f72`.
- Authoritative repaired run `35145567502` and terminal canonical record `results/SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_CANONICAL_2026-09-16.json`.

## Adversarial checks

1. **Definition actually present, not reconstructed from textbook memory.** The locked primary record explicitly states the general identity `g_ab = g_b^{-1} g_a`, Eq.(4) ordering `1 <= a < b <= 5`, gauge fixing `g1=1`, and `B_ab=B(z_ab,g_b^{-1}g_a)`. Therefore the maps are primary-source identities, not inferred from the historical V8 chart.
2. **Variable classes not mixed.** `g2,g3` are Eq.(4) integration/group variables. `z_ab` remains the one-wedge scalar/distribution variable. No Toller/Cartan representation argument is substituted for a group integration variable.
3. **Exact maps.** In the same gauge-fixed realization: `G12=g_2^{-1}`, `G23=g_3^{-1}g_2`, `G13=g_3^{-1}`. Multiplication order and inversions follow the literal source formula.
4. **Orientation.** Ordered wedges use `a<b` and `kappa_ab=sigma_a sigma_b`; no extra inversion, cyclic convention, or S3 orientation transport is silently imposed.
5. **Historical V8 exclusion.** The source record and classifier explicitly reject V8 additive substitution; the production PASS does not consume it.
6. **Negative fixtures are outcome-sensitive.** Reversed multiplication, dropped inverse, wrong contact label, V8 substitution and guessed Toller composition are detected rather than accepted as equivalent.
7. **Rank hygiene.** The decision stores `transverse_rank=null` and `rank_status=null_not_computed_in_this_gate`. No missing/undefined rank is converted to zero, and no physical transversality conclusion is drawn.
8. **Execution repair did not change science.** The only post-failure change was `fetch-depth:0` so prereg/source ancestry checks could execute. Scientific payloads from Python 3.11 and 3.13 are byte-identical.

## Critic conclusion

No source-identity or hidden-convention defect was found in the terminal PASS. The result is valid only at the identity/object-definition scope: all three triangle group arguments are source-authoritatively pinned in one realization.

The Critic explicitly does **not** authorize a physical transverse rank. A future local-Lie gate must separately freeze the local tangent convention, quotient definition, permissible coordinate/basis replacements, S3/orientation differential transport and Jacobian/Haar/contact-normalization treatment. A raw differential rank may be recorded as a coordinate-level fact but may not be relabeled as a physical quotient rank without source authority.

Governance locks remain unchanged; no D7 or selector closure follows.
