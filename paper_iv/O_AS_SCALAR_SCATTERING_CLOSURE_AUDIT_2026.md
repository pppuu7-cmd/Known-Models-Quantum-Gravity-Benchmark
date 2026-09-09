# O-AS — 2026 Lorentzian Scalar-Scattering Closure Audit

**KMQGB iteration:** 153  
**RQIR Core:** v1.0 FROZEN  
**Purpose:** determine whether current asymptotic-safety authority already supplies the full physical crossover observable demanded by PF1-05.

## 1. Major authority upgrade

Chiesa, Pawlowski & Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168 (2026), goes substantially beyond a propagator-only or Euclidean-flow result.

The work computes the full momentum dependence of the scalar–scalar–graviton 1PI vertex in Euclidean signature, reconstructs its timelike/Lorentzian branch, and obtains a non-perturbative graviton-mediated `phi phi -> phi phi` scattering amplitude and differential cross section.

The reported physical behavior is exactly the type of RQIR bridge PF1-05 asked for:

- low energy approaches the General Relativity result;
- the asymptotically safe UV scaling is visible in the physical amplitude;
- the cross section remains compatible with the stated unitarity bounds in the UV;
- several reconstruction methods are compared rather than relying on one analytic-continuation fit.

Therefore the old O-AS requirement

`obtain any Lorentzian physical crossover observable`

is **closed**.

## 2. Why the full PF1-05 block does not yet close

The same paper defines the identical-scalar amplitude as

`A = A_s + A_t + A_u + A_4`,

but explicitly states that the calculation focuses on the graviton-mediated diagrams and **neglects the direct contact term `A_4`**. The contact contribution is assigned to separate work.

Thus the published/preprint observable is a real physical scattering control but not yet the complete same-realization scalar amplitude required for a strongest comparator/attribution claim.

The paper also freezes several approximations, including

- identification of different Newton-coupling avatars in the flow;
- a momentum-factorisation approximation for loop dependence;
- quenched treatment in part of the graviton flow;
- `V_2(s)=V_0(s)` in the resolved vertex structure;
- reconstruction choices for the Lorentzian vertex.

Crucially, the quoted reconstruction uncertainty does not include all flow-approximation errors.

Therefore the remaining RQIR blocker is no longer generic scheme/truncation uncertainty. It is a much narrower certificate:

`CONTACT_COMPLETE + APPROXIMATION_CONTROLLED + SAME_REALIZATION LORENTZIAN SCALAR SCATTERING`.

## 3. Contact-sector evidence

Benjamin Knorr, *Asymptotically (un)safe scattering amplitudes from scratch: a deep dive into the IR jungle*, arXiv:2602.21285 (2026), computes leading-order quantum-gravity contributions to a scalar scattering amplitude in an analytically tractable asymptotic-safety setting and gives explicit contact form-factor contributions.

This is useful comparator/methodology evidence, but it may **not** be pasted into the Chiesa–Pawlowski–Reichert amplitude as if it were the missing `A_4` of the same realization.

The paper also demonstrates why that shortcut would be unsafe: an RG fixed point alone does not guarantee bounded amplitudes; derivative expansions and standard RG-improvement procedures can fail for the relevant momentum dependence.

Hence KMQGB requires the contact sector from the **same frozen realization/prescription** as the mediated amplitude, or an explicit matching theorem.

## 4. September 2026 conference evidence

The ERG2026 contribution by Chiesa reports that the mediated amplitude is complemented by a gravitational contact contribution resummed directly in Lorentzian signature and that the resulting cross section remains GR-compatible in the IR and unitary-compatible in the UV.

This is highly relevant **prospective closure evidence**.

However, for frozen Paper-IV authority KMQGB distinguishes

- a conference description/presentation claim, and
- a reproducible equation/data/uncertainty package sufficient for the same-domain comparator ledger.

Until the contact-complete calculation is available in a stable inspectable form with enough detail to bind the same realization and approximation budget, it is retained as `PROMISING_NONCANONICAL_AUTHORITY`, not used to flip the terminal PF1-05 status.

## 5. Updated O-AS status

Closed:

- Lorentzian physical scattering observable exists;
- non-perturbative momentum dependence is resolved for the mediated contribution;
- IR GR recovery is explicit;
- UV amplitude/cross-section behavior is tested;
- multiple Lorentzian reconstruction methods provide a robustness control.

Still open:

1. same-realization direct contact `A_4` contribution in the full amplitude;
2. complete `s+t+u+A_4` physical certificate with crossing/forward-limit treatment;
3. an error/robustness budget that includes the relevant flow/truncation/vertex-avatar approximations, not reconstruction error alone;
4. same-domain comparison against the full GR/EFT and applicable alternative-QG amplitude class.

New precise blocker:

`O-AS = CONTACT_COMPLETE_APPROXIMATION_CONTROLLED_LORENTZIAN_SCALAR_SCATTERING_CERTIFICATE`.

## 6. Terminal classification consequence

PF1-05 remains model-level

`BLOCKED_MISSING_REQUIRED_OBJECT`.

But this is a **material blocker contraction**, not a repeated negative result. The missing object has moved from a generic physical crossover observable to one identifiable contact-complete same-realization certificate.

No RQIR Core change is needed.

## 7. Compute triage

No new heavy KMQGB computation is justified yet.

The missing information is primarily authority/completion of the same AS realization. Once the contact-complete amplitude or reproducible presentation data is frozen, a numerical robustness/comparator audit may become useful.