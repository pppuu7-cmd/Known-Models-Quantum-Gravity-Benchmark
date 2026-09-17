# Independent root-affine enclosure rigor check

Date: 2026-09-17
Scope: Iter504R / Iter504S full-D construction only

This note is independent of any Iter504S numerical outcome.

## Construction checked

For a frozen root interval `I=[l,u]` with midpoint `m`, Iter504R builds the dual geometry once with amplitude value ball `I` and dual seed derivative `1`:

`dual_amp = RD(I,1)`.

Every downstream arithmetic operation propagates value and first derivative by interval automatic differentiation. The contracted dual channel therefore has a value component and a derivative component whose derivative ball encloses the channel derivative over the entire root interval, subject to the already-frozen source/KAK/domain controls.

The root-affine child construction then uses the separately evaluated midpoint channel value `f(m)` and the unchanged full-root derivative enclosure `D(I)`:

`f(J) subset f(m) + (J-m) D(I)`.

In code, Iter504R obtains the derivative component through `iter503_ad_core.centered_channels`, which explicitly applies `as_c(dualvals[idx]).d`.

The Haar/log prefactor is treated analogously with the full-root derivative component `dlogH.d`.

## Inclusion proof

Let `f:I -> C` be continuously differentiable and suppose the validated complex interval `D(I)` contains `f'(t)` for every `t in I`. Treating real and imaginary components componentwise, for any exact `a in I`,

`f(a)-f(m) = integral_m^a f'(t) dt`.

Because an Arb/Acb interval enclosure is convex componentwise and contains every `f'(t)` on the integration segment, the average derivative

`(a-m)^(-1) integral_m^a f'(t) dt`

lies in `D(I)` when `a != m`; at `a=m` the claim is trivial. Hence

`f(a) in f(m) + (a-m)D(I)`.

For an interval `J subset I`, every `a in J` satisfies `a-m in J-m`, so interval multiplication/addition gives the set inclusion

`f(J) subset f(m) + (J-m)D(I)`.

Thus reusing the *same* full-root derivative enclosure on descendants is rigorous. Narrowing only `J-m` can reduce dependency width without requiring child-level derivative recomputation.

## Zero-width diagnostic consequence

At a degenerate child `J={a}`, child-width dependency disappears, but the enclosure can remain wide because `D(I)` itself is a ball. Therefore a nontrivial zero-width full-D drift is a clean diagnostic that further subdivision alone cannot eliminate the root-derivative contribution.

This is exactly the rigorous branch of Iter504S.

## Derivative-center control distinction

Replacing `D(I)` by the midpoint of the derivative ball is generally **not** an enclosure of all derivatives on `I`. It is therefore not a rigorous replacement for the full-D construction. Its only authorized role in Iter504S is prospective mechanism sensitivity: if the full-D zero-width excess disappears after derivative-radius collapse, the result localizes sensitivity to derivative-ball radius but does not by itself certify the continuous science state.

## Implementation audit consequence

`iter503_ad_core.dcontract_all()` returns full dual `CD` objects. The correct derivative object used in the affine inclusion is `as_c(z).d`, as performed by `centered_channels()`. Any consumer that multiplies the full dual `CD` object by displacement instead of extracting `.d` is a representation/implementation defect, not a different scientific method.

## Claim ceiling

This note establishes the set-inclusion logic of the frozen root-affine construction conditional on the validated AD derivative enclosure and source/domain controls. It does not establish the Iter504R or Iter504S numerical classifier outcome, a full Iter504 theorem, absolute-Haar divergence, D7 closure, model failure or quantum gravity.
