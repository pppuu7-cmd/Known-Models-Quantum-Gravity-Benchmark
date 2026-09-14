# Iter504 j=1 exact Laurent scalar reduction — 2026-09-14

Status: **exact derived audit from already-qualified Appendix-B source formulas; does not modify the frozen Iter504 workflow or verdict**.

## Source formulas

Use the j=1 reduced Toller formulas already frozen/qualified in `code/iter456_reduced_toller_appendixb.py`. Write

`den(rho)=rho+rho^3=rho(1+rho^2)`

and let beta approach zero from the positive side.

The standard expansions are

- `csch(beta)^3 = beta^-3 + O(beta^-1)`,
- `csch(beta)^2 = beta^-2 + O(1)`,
- `coth(beta) = beta^-1 + O(beta)`,
- `exp(±i rho beta)=1+O(beta)`,
- `sinh(2 beta)=2 beta+O(beta^3)`,
- `cosh(2 beta)=1+O(beta^2)`.

Define

`a(rho) = 3 i / (4 den(rho))`.

## Exact beta^-3 coefficients

For the source `T+` branch:

- `m=-1`: the bracket at beta=0 is `i(1+rho^2)-i rho^2=i`, hence `B^+_-1=a(rho)`;
- `m=0`: the `i coth(beta) csch(beta)^2` term gives `B^+_0=-3i/(2 den)=-2 a(rho)`;
- `m=+1`: directly `B^+_+1=3i/(4 den)=a(rho)`.

For the source `T-` branch:

- `m=-1`: `B^-_-1=-3i/(4 den)=-a(rho)`;
- `m=0`: `B^-_0=+3i/(2 den)=+2a(rho)`;
- `m=+1`: at beta=0 the factors are `i` and `-1`, giving `B^-_+1=-3i/(4 den)=-a(rho)`.

Therefore, exactly,

`diag(B^+_-1,B^+_0,B^+_+1) = a(rho) Q`,

`diag(B^-_-1,B^-_0,B^-_+1) = -a(rho) Q`,

with

`Q = diag(1,-2,1)`

in the Iter484 contraction basis `(-1,0,+1)`.

This is consistent with Iter477's hypergeometric normalization: its coefficient `C_m^(src)` multiplies `(1-exp(-2 beta))^-3`, and `B_m=C_m^(src)/8` because `1-exp(-2 beta)~2 beta`.

## Consequence for a full K5 collision tangent panel

For edge `e=(a,b)` with tangent difference `w_e`, `r_e=|w_e|`, direction section `U_e=U(w_e/r_e)` and causal branch sign `s_e=+1` for `T+`, `-1` for `T-`, the exact leading edge coefficient is

`L_e = s_e a(rho) r_e^-3 D^1(U_e) Q D^1(U_e)^dagger`.

For any fixed five-intertwiner channel `I`, ten-edge multilinearity gives

`C_I({L_e}) = [a(rho)^10 product_e s_e product_e r_e^-3] * G_I({n_e})`,

where `G_I` depends only on the ten edge directions and the already-fixed intertwiner/magnetic convention.

Thus:

1. for real nonzero rho, `a(rho)` is nonzero;
2. changing `rho` changes every channel only by the same nonzero scalar `a(rho)^10`;
3. changing the causal sign pattern changes every channel only by the same global sign `product_e s_e`;
4. multiplying individual edge distances changes every channel by the same nonzero factor `product_e r_e^-3` for a fixed panel;
5. therefore the **zero/nonzero channel pattern is exactly independent of rho, causal representative, and edge-distance scale**, and depends only on the edge directions plus the fixed intertwiner contraction;
6. the Iter504 dimensionless ratios `|C_I|/product_e maxabs(L_e)` are likewise exactly independent of rho and causal class. Their panel dependence is directional.

This explains, without fitting to production data, why already-completed frozen T0 lanes exhibit identical normalized ratios across rho/causal labels.

## Scope

This is an exact leading-coefficient algebraic reduction. It does not certify Iter504 because Iter504 prospectively included a separate finite-t regression control, and that control must be honored. It does not establish a uniform angular neighborhood, remainder domination, local absolute divergence, Haar divergence, ten-spectral pairing, or a physical causal-vertex theorem.

If Iter504 terminates BLOCKED solely because of its finite-t sampling scale, the principled repair is an independently preregistered gate that replaces that numerical source-normalization check by this exact Laurent identity; it must not loosen the scientific witness threshold or reinterpret the blocked Iter504 run.