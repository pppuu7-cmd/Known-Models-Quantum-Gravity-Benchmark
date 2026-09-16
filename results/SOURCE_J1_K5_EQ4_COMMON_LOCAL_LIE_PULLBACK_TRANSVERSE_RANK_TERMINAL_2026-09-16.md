# SOURCE_J1_K5_EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_GATE — terminal result

Date: 2026-09-16
Status: TERMINAL

## Authority

- Preregistration: `2d6b2b8565a825e9864fbbd779c842cdedc60299`.
- Frozen source-authority audit: `40f4db6a75f6765dd8ce80077a0f3690abb804bc`.
- Exact classifier: `b9a486cace4133d66ab54384dae17f2cfe339ca2`.
- Aggregate: `413b4924b6184b6e1f8d70efecc20c6906a2890f`.
- Workflow head: `e4a373219aef548c64e1b689260f8dbc988b7746`.
- Actions run: `35146616833`, terminal `completed/success`.
- Jobs: source-lock `104964213008`; minors/Python3.13 `104964278021`; RREF/Python3.11 `104964278025`; aggregate `104964433409`.
- Artifacts: RREF `10467168692` / `sha256:d6815e77dc2354ce05d2c29bb52175377a469bd581da0708443943675b837ffb`; minors `10467412844` / `sha256:208b00d197d36971161a89220c7e07352f6edd076720f0db3c7be8b82c7469a0`; aggregate `10467007793` / `sha256:2d333d0c4b13a384f11616f2f9bd6a71c7f3768ec29ca3b265de8261d5b841e6`.
- Aggregate JSON SHA256 `7eeb379562c85d58783d771dc9bab29abae3f71c134ef4e08b6afdca295f3240`.
- Aggregate scientific digest `d185980c29db21a537c20815113619d0f4dc306f1dacef2182fa1bd56929f89c`.

## Terminal classification

`EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_BLOCKED_SCOPED`

**BLOCKED, not FAIL.**

## Exact raw Lie result

At `(g2,g3)=(1,1)`, using left-trivialized `X2,X3 in sl(2,C)` and the source-authorized maps:

`d(G12,G23,G13) = (-X2, X2-X3, -X3)`.

Per Lie generator the exact matrix is

`[[-1,0],[1,-1],[0,-1]]`,

with rank `2`. Since `SL(2,C)` has real Lie-algebra dimension `6`, the raw map is `12 -> 18` with exact rank `12`, domain nullity `0`, codomain left-nullity `6`. The exact left relation is `Y12 + Y23 - Y13 = 0` generator-wise.

Rational RREF and independent minor-based rank computation agree. Two invertible rational basis replacements preserve the generator rank, and all six raw triangle relabeling controls return rank `2`.

## Why physical transversality remains undefined

Frozen primary authority does not define:

- the physical transverse quotient;
- its projection;
- simultaneous contact-scalar pullback to that quotient;
- Jacobian/Haar/contact-normalization transport;
- S3/orientation coordinate transport on that quotient.

Therefore `physical_transverse_rank=null`, not `0` and not `12`. The exact full raw rank is a coordinate/local-group fact only and cannot be promoted to a physical quotient conclusion.

## Minimal blocker

The first causal blocker is the missing **source-authorized physical transverse quotient/projection for the same Eq.(4) realization**. Normalization and S3 transport are downstream of that definition.

## Claim ceiling

No transversality FAIL, distributional existence/nonexistence, K5/model/family failure, D7 closure, selector authority or Candidate Gravity conclusion follows.

Governance locks remain unchanged.
