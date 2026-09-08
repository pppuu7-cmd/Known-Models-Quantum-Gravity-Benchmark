# External RQIR Check — Iter620 Projective Native-Bridge Audit

**KMQGB iteration:** 061  
**External authority:** `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`, Candidate Gravity Iteration 620.  
**Mode:** read-only authority synchronization; KMQGB does not alter RQIR Candidate Gravity scientific authority.

## External scientific state

RQIR `MODEL_READINESS` remains **24%**.

No active promotable ansatz and no robust comparator-subtracted residual are authorized.

## Progress since the previously observed Iter616

### Iter617 — missing normalization authority proved genuine

The existing RQIR authority fixes important local conventions and relative structures, including the connection outer phase, retarded gravitational-response convention, metric-source convention, source-internal relative factors, q2 identity and scalar endpoint amputation.

However, the repository contains no frozen equation that maps the scalar-endpoint-amputated MSSC probe response to the gravitational retarded/1PI `Gamma3` convention with an **absolute** phase/coupling normalization.

Therefore the remaining scalar

`N_native`

is not an arbitrary nuisance that can be guessed from prior conventions. It is

`BLOCKED__NOT_DERIVABLE_FROM_EXISTING_REPOSITORY_AUTHORITY`.

It must not be set to `1`, `+i`, `-i`, tuned per root/q2 bucket or fit from Candidate values.

### Iter618 — projective source shape

Because one common nonzero `N_native` multiplies the source-side six-root coefficient vector, all root-by-root ratios to a chosen nonzero anchor are invariant under that missing common normalization.

Using the pre-coefficient smallest-s root `D_b^-` as anchor, RQIR freezes five independent ratios:

- `-2.966563737084728`;
- `-0.7800526753639322`;
- `-5.158207913624242`;
- `+2.997420912767025`;
- `+8.57973421373656`.

The raw source sign pattern is

`[-,+,+,+,-,-]`.

These define a normalization-invariant projective source-shape certificate. They are diagnostic/non-promoting and do not close native binding.

### Iter619 — independent projective reproducibility

An independent representation of the Iter615 coefficients reproduces the Iter618 ratios at floating-point level:

- maximum absolute ratio difference `5.329070518200751e-15`;
- maximum relative ratio difference `6.211230307890725e-16`.

This is a reproducibility PASS, not a residual or normalization determination.

### Iter620 — projective conditioning

RQIR adds a threshold-free componentwise conditioning diagnostic

`M = |A_aggregate| / (|A_pair| + sum |A_K1cubed|)`,

`kappa = 1/M`.

Rootwise `kappa`:

`[1.227051600482995, 1.093790319820292, 1.0, 1.272764987610942, 2.45679285736057, 1.279568269456018]`.

Minimum cancellation margin:

`0.40703472293319004` at `D_b^+`.

Absolute projective coefficient dynamic range:

`10.998916463857647`.

This again is normalization-invariant and non-promoting.

## KMQGB methodological lesson

This external sequence provides a concrete case study for a general rule:

`unknown common normalization -> use projective invariants for corruption/reproducibility diagnostics, but do not promote an absolute residual`.

Let a nonzero source vector be

`a = (a_1,...,a_n)`

and native mapping be known only up to one common nonzero scalar

`a_native = N a`, `N != 0`.

Then projective coordinates such as

`r_i = a_i / a_j`

for a fixed nonzero anchor `a_j` are invariant under `N`, while any claim that depends on absolute scale/phase remains blocked.

This distinction is useful for KMQGB construction:

- projective ratios may validate identity preservation, routing, relative signs and implementation consistency;
- projective conditioning can expose cancellation-sensitive components;
- they cannot manufacture the missing absolute source-to-1PI/retarded normalization;
- comparator subtraction requiring absolute normalization must remain forbidden until an independent bridge exists.

## Anti-fit rule

A missing common normalization is an **authority blocker**, not a free parameter to be estimated from the same Candidate values whose residual is under test.

Using Candidate values to infer `N_native` and then declaring the normalized vector anomalous would introduce circularity and invalidate residual attribution.

## Compute decision

No heavy numerical job is justified by the current RQIR blocker.

The unresolved object is an absent algebraic/generating-functional normalization bridge. More floating-point evaluation cannot create that authority.

Normalization-invariant diagnostics are admissible; model-promoting native projection, Source/Born subtraction, comparator quotient, ansatz/Fisher/resource promotion are not.

## KMQGB scoring consequence

- R1 unchanged.
- R2 unchanged by this external synchronization alone.
- R3 remains externally controlled at **24%**.
- R4 unchanged.

The result strengthens guardrails and future corruption checks but does not provide a KMQGB P4 survivor.
