# KMQGB Critical Review — SOURCE_J1_K5_TRIANGLE_CONTACT_REGULARIZATION_V6

Date: 2026-09-16
Lane: independent Critical Review / Verification

## RESULT_REVIEWED

Exactly one latest terminal substantive Research execution is reviewed:

- gate `SOURCE_J1_K5_TRIANGLE_CONTACT_REGULARIZATION_V6`;
- preregistration `research/SOURCE_J1_K5_TRIANGLE_CONTACT_REGULARIZATION_V6_PREREG_2026-09-16.md`;
- preregistration commit `de880ad093d9d6d0c6978e81d3e69b33195b2b92`;
- implementation commit `97faed8a94315b7abc9c24ba8d44c24e30894653`;
- workflow head `4b2d716dc439f6388f3402884d2a3b9f774bfc8c`;
- authoritative Actions run `35050058294`, terminal `completed/success`;
- exact Python 3.11 job `104648273263`, success;
- exact Python 3.13 job `104648273388`, success;
- aggregate job `104654114127`, success;
- Python 3.11 artifact `10429341416`, digest `sha256:ca49d3508bb8debf380adf0d9106c058df767639f37315b5fcffc8c65ffcbd67`;
- Python 3.13 artifact `10429710311`, digest `sha256:38d1807d42f3d9750e7d39d5daec048ab48d0779dbc001d36ad45f2910e0dda0`;
- aggregate artifact `10429422363`, digest `sha256:65ff56f618b3e1ba85614586e5721d64db48a4a64db6330dff6d5fe51163a388`;
- terminal Research classification from the aggregate: `TRIANGLE_CONTACT_REGULARIZATION_DEPENDENT_SCOPED`;
- aggregate decision SHA256 `0308fae590691f29a1ccbdc6370ebffd422f833da7a33db1a3f568712ca1f3ac`.

There is no separate Research result commit at the reviewed head. Fresh terminal Actions state is therefore the substantive execution authority for this review.

## PREREG_CHECK

PASS.

The scientific object and classifier were prospectively frozen at `de880ad...` before implementation. Direct repository comparison from preregistration to workflow head is exactly two commits ahead and adds only:

1. `code/source_j1_k5_triangle_contact_regularization_v6.py`;
2. `.github/workflows/source-j1-k5-triangle-contact-regularization-v6.yml`.

No post-outcome modification of the preregistration was found.

The frozen contract is explicit:

- local normal form `B12=x`, `B23=y`, `B13=x+y`;
- normalized Gaussian approximate identity `delta_eps^a(t)` for positive rational `a`;
- exact local integral over `R^2`;
- exact statistic `S(a,b,c)=abc/(ab+ac+bc)`;
- frozen schemes A=`(1,1,1)`, B=`(1,1,4)`, C=`(1,2,3)`;
- no floating threshold;
- `DEPENDENT_SCOPED` iff controls pass and at least two exact S values differ;
- `INVARIANT_SCOPED` iff controls pass and all three exact S values agree;
- `INVALID_IMPLEMENTATION` iff a frozen control fails.

The interpretation ceiling is also prospectively narrow: local three-contact triangle, normalized Gaussian class only, no full K5 product theorem, no D7 closure, no family/model verdict.

## OBJECT_IDENTITY_CHECK

PASS for the explicitly frozen V6 mathematical object; QUALIFICATION for transfer to the parent highest-contact object.

The implemented object is exactly the preregistered plain approximate-identity product

`delta_eps^a(x) delta_eps^b(y) delta_eps^c(x+y)`.

This is a mathematically well-defined local two-coordinate surrogate and the implementation does not silently change it.

However, the current parent V4 authority is more specific: it established survival of the highest **`delta''` contact** leading homogeneous tensor in the frozen `j=1`, fixed-tangent, channel-`00000` realization. V6 replaces that derivative-contact object by three plain normalized delta approximate identities. The V6 preregistration does this prospectively, so it is not a post-hoc implementation mismatch. But the two objects are not the same distributional realization.

Therefore V6 can establish regulator-width dependence for its frozen plain-delta normal form, but it cannot by itself be consumed as a same-realization theorem about the actual V4 highest-`delta''` product.

## SOURCE/REALIZATION_CHECK

QUALIFIED.

The local conormal relation is frozen inside V6 as `B12=x`, `B23=y`, `B13=x+y`. Within that local normal form, the implementation and classifier are realization-consistent.

The important source/realization ceiling is derivative order. Parent V4 authority concerns highest `delta''` contacts; V6 uses plain `delta` approximate identities. Derivatives of approximate identities introduce different polynomial prefactors and different scale powers, so regulator dependence of the plain-delta product does not logically imply the same exact dependence statement for a triple `delta''` product.

This is not evidence that the `delta''` product is regulator-independent. It means only that V6 has not tested that object.

Any descendant that wishes to claim regulator dependence of the parent highest-contact sector must prospectively freeze and execute the corresponding derivative-contact regularization in the same realization. Retrofitting V6 to that object is forbidden.

## PROVENANCE_CHECK

PASS.

Actions run `35050058294` is terminal `completed/success` at workflow head `4b2d716...`. Both exact lanes and aggregate are terminal success.

The live artifact API and aggregate job log agree on all artifact IDs and digests:

- 3.11 `10429341416`, `sha256:ca49d3508bb8debf380adf0d9106c058df767639f37315b5fcffc8c65ffcbd67`;
- 3.13 `10429710311`, `sha256:38d1807d42f3d9750e7d39d5daec048ab48d0779dbc001d36ad45f2910e0dda0`;
- aggregate `10429422363`, `sha256:65ff56f618b3e1ba85614586e5721d64db48a4a64db6330dff6d5fe51163a388`.

The aggregate compares decision-critical fields across both exact lanes and records lane agreement. Green CI is used only as execution provenance; the scientific statement is checked analytically below.

## SAME_REALIZATION_CHECK

QUALIFIED.

Within V6 itself, both exact lanes use the same frozen local object and schemes, and they agree exactly.

Across the parent chain, same-realization transfer is incomplete: V4 highest-contact authority is for `delta''`; V6 is for `delta`. This distinction is material and must survive all downstream handoffs.

V5's finite channel census and its `00000=11/24` result do not repair this derivative-order mismatch. They identify a nonzero angular channel but do not convert a plain-delta contact product into the parent highest-derivative contact product.

## NUMERICAL/STATISTICAL_CHECK

PASS for the frozen V6 exact result; no statistical inference is involved.

Independent analytic replay:

For

`delta_eps^a(t)=sqrt(a)/(sqrt(pi) eps) exp(-a t^2/eps^2)`,

the three-factor prefactor is

`sqrt(abc)/(pi^(3/2) eps^3)`.

The exponent is the positive quadratic form

`a x^2 + b y^2 + c(x+y)^2`

with matrix

`Q=[[a+c,c],[c,b+c]]`

and determinant

`det Q = (a+c)(b+c)-c^2 = ab+ac+bc`.

The exact two-dimensional Gaussian integral is `pi eps^2/sqrt(det Q)`, hence

`I_eps(a,b,c)=sqrt(abc)/(sqrt(pi) eps sqrt(ab+ac+bc))`

and therefore

`S(a,b,c)=pi(eps I_eps)^2=abc/(ab+ac+bc)`.

This gives exactly:

- A `(1,1,1)`: `S=1/3`;
- B `(1,1,4)`: `S=4/9`;
- C `(1,2,3)`: `S=6/11`.

They are pairwise not all equal. Thus the terminal V6 classification is correct for the frozen object.

A common-rescaling counterexample does not explain the difference: all schemes keep the first width parameter fixed at `a=1` while changing relative widths, so B/C are not merely a global redefinition of epsilon applied to all three factors.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong Gaussian determinant.** Failed to refute. Direct expansion gives `ab+ac+bc` exactly.
2. **Scheme dependence caused only by floating-point error.** Failed. All quantities are exact rationals and both Python lanes agree.
3. **Permutation dependence.** Failed. `abc/(ab+ac+bc)` is exactly symmetric in `a,b,c`.
4. **Global epsilon reparameterization masquerading as regulator dependence.** Failed for the frozen schemes: relative widths change while one width stays fixed.
5. **Non-positive Gaussian quadratic form.** Failed for all frozen positive schemes; determinant is positive.
6. **Plain-delta result promoted to parent highest-`delta''` product.** Successful counterexample to the stronger interpretation: the frozen V6 integrand and parent V4 highest-contact distribution have different derivative order. The exact V6 computation does not contain the derivative polynomial factors of a `delta''` regularization. Therefore same-realization transfer is not established.
7. **Two-contact forest control independently validates the integration machinery.** Only partially supported. The implementation computes this control as the identity `ab/(ab)=1`; it is algebraically correct for normalized independent two-contact Gaussians but is a weak/tautological fixture rather than an independent replay through the same Gaussian integration routine. This does not overturn the main exact three-contact calculation, but future gates should harden it.
8. **Green CI promoted to science.** Rejected. The exact analytic calculation above independently reproduces the decision.

## OVERCLAIM_CHECK

The Research classification `TRIANGLE_CONTACT_REGULARIZATION_DEPENDENT_SCOPED` is acceptable only with the preregistered object and interpretation ceiling made explicit:

> For the frozen local plain-delta triangle `delta_eps^a(x) delta_eps^b(y) delta_eps^c(x+y)` and the three normalized Gaussian width schemes A/B/C, the leading `1/eps` coefficient depends on relative regulator widths.

The following stronger claims are not authorized by V6:

- regulator dependence of the actual parent highest-`delta''` contact product;
- nonexistence of a distributional extension;
- uniqueness/nonuniqueness under all mollifier classes;
- full ten-contact K5 product failure;
- complete vertex divergence;
- family/model failure;
- D7 closure or a terminal selector;
- Candidate Gravity activation.

The phrase in the preregistration that this is evidence about a `naive local product` is acceptable only for the frozen Gaussian plain-delta normal form. It must not be silently lifted to the derivative-contact parent.

## VERDICT

`QUALIFIED`

The exact V6 Gaussian calculation, Actions provenance, and terminal `TRIANGLE_CONTACT_REGULARIZATION_DEPENDENT_SCOPED` classification are independently confirmed **for the frozen plain-delta triangle normal form**.

The material qualification is same-realization/source transfer: current parent V4 authority is a highest-`delta''` contact sector, whereas V6 tests three plain delta approximate identities. V6 therefore cannot serve as terminal evidence that the parent highest-contact product itself has the same regulator dependence.

This is not `INVALID_IMPLEMENTATION`: the code matches its prospectively frozen V6 contract. It is not `INVALID_PROVENANCE`: the execution/artifact chain is durable and consistent. It is not a scientific FAIL.

## QUALIFICATIONS

1. Exact local V6 values `1/3`, `4/9`, `6/11` are confirmed.
2. `TRIANGLE_CONTACT_REGULARIZATION_DEPENDENT_SCOPED` is valid for the prospectively frozen normalized-Gaussian plain-delta object.
3. Parent V4 highest-contact authority is `delta''`; V6 does not establish same-realization transfer to that derivative-contact product.
4. The two-contact forest control is algebraically valid but weak because it is implemented as a tautological quotient rather than an independent integral replay.
5. No all-mollifier theorem, distributional nonexistence theorem, full-K5 result, family closure, D7 closure, selector, or Candidate Gravity activation follows.
6. Iter504 run `34907349374` and Iter461 run `34748503239` were freshly checked and remain `queued / conclusion=null`; no partial substantive values were consumed.

## UPDATED_STATE

- `SOURCE_J1_K5_TRIANGLE_CONTACT_REGULARIZATION_V6 = QUALIFIED` by independent Critic.
- exact frozen plain-delta Gaussian regulator dependence = confirmed scoped.
- transfer to V4 highest-`delta''` contact sector = not established.
- V5 `224/243` finite channel census remains qualified as before and is not a product theorem.
- V4 repaired highest-contact result remains scoped parent authority.
- governance unchanged: `RQIR Core v1.0 = FROZEN`, `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`, terminal selectors forbidden, Candidate Gravity inactive.

## NEXT_ADMISSIBLE_GATE

To test the parent highest-contact realization, a **new prospectively frozen gate is required** because changing V6 from plain `delta` to derivative-contact `delta''` regularizations changes the scientific object.

Freeze before execution:

- the exact parent derivative-contact factors and derivative order on the same coherent K5 triangle;
- an explicit normalized regularization for each `delta''` factor, including the derivative convention and epsilon power;
- the local conormal coordinate map and exact dependency on the parent V4/V5 realization;
- a dimensionless leading coefficient/statistic chosen before outcomes;
- at least three relative-width schemes plus a common-rescaling control;
- an independently evaluated transverse two-contact control using the same integration machinery;
- permutation/covariance controls and a synthetic negative fixture;
- exact PASS / invariant / BLOCKED / INVALID semantics;
- interpretation ceiling separating a local derivative-contact counterexample from full ten-factor product existence/nonexistence.

Do not rewrite V6 history. If the next gate instead changes the tangent, channel basis, source authority, or contact object beyond this derivative-realization bridge, freeze those changes prospectively as a distinct gate.
