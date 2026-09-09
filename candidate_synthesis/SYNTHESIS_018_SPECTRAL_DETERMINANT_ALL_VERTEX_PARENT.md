# SYNTHESIS-018 — Spectral / Functional-Determinant All-Vertex Parent

**Status:** interacting-generator positive control / rejected as novel P4 parent.  
**KMQGB iteration:** 131.  
**Purpose:** test whether one finite covariant operator can generate an all-point gravitational interaction hierarchy without introducing an independent function at each vertex order.

## 1. Parent capsule

Let `Delta[g]` be a covariant fluctuation/Hessian operator for a specified quantum field or graviton/ghost system on a metric background. Define the one-loop functional

`Gamma_1[g] = +/- 1/2 Tr log Delta[g]`

with the appropriate ghost/statistics factors and a frozen state/contour prescription.

Writing

`Delta[g] = Delta_0 + V[g]`,

one has formally

`Tr log(Delta_0+V) = Tr log Delta_0 + sum_(n>=1) (-1)^(n+1)/n Tr[(Delta_0^-1 V)^n]`.

Thus one operator generates an infinite sequence of metric vertices rather than requiring an independent `K_n` at every order.

## 2. A1 — explicit finite microscopic generator

Once

- the field/operator content;
- gauge/ghost complex;
- state/boundary conditions;
- Lorentzian or Euclidean contour;
- regularization/renormalization prescription

are fixed, the determinant is a concrete quantum object.

Recent heat-kernel/effective-action work continues to derive local and nonlocal gravitational form factors from such operators; gravitational path-integral work also uses functional determinants to fix semiclassical measures and prefactors.

Classification:

`A1 PASS_CONTROL__FINITE_OPERATOR_GENERATES_QUANTUM_METRIC_FUNCTIONAL`.

## 3. A2 — all-vertex generation succeeds, but renormalized local data remain

The logarithm expansion ties arbitrarily high metric insertions to the same `Delta[g]`. This is a genuine all-order compression mechanism.

The nonlocal finite pieces can be completely determined by the chosen operator and state. However ultraviolet divergences generate local covariant counterterms. In gravity these populate the allowed local curvature/EFT basis and require renormalization conditions unless another UV principle fixes them.

Therefore

`A2 PARTIAL_PASS_CONTROL__NONLOCAL_VERTEX_TOWER_DERIVED__LOCAL_RENORMALIZATION_DATA_REMAIN`.

The determinant does not remove full-C5 freedom by itself.

## 4. A3 — established comparator architecture

This construction is standard quantum-field-theory / induced-gravity / one-loop quantum-gravity architecture. Depending on `Delta`, it is contained by

- ordinary matter loops coupled to gravity;
- one-loop Einstein gravity and ghost determinants;
- heat-kernel/covariant perturbation theory;
- induced gravity/nonlocal effective actions;
- LQG/spinfoam coherent-state one-loop effective actions where analogous determinant structures occur.

Hence

`A3 FAIL_AS_NOVELTY_CERTIFICATE__FUNCTIONAL_DETERMINANT_QFT_COMPARATOR`.

A new choice of operator is not novel unless that operator is itself derived from a new gravity-native parent and produces comparator-orthogonal hard observables.

## 5. A4 — genuine interacting vertices, not new quantum gravity

Unlike the black-hole probe `G2` control of Iter127, the determinant can generate metric vertices of arbitrary order and therefore is a stronger all-point blueprint.

But those vertices are loop corrections of the already specified underlying theory. They do not supply a new primitive quantum-gravity hard datum independent of the operator input.

If `Delta` is a matter operator, attribution is C4/C6/known-sector quantum matter coupled to gravity.

If `Delta` is the Einstein graviton Hessian, the result is ordinary perturbative quantum GR.

Thus

`derived all-point vertices from known Delta != new parent`.

## 6. CTP lesson

The same determinant idea can be formulated on a closed-time path/in-in contour, yielding real-time influence/effective actions. This demonstrates that a finite microscopic generator can, in principle, provide both scattering/effective vertices and CTP observables.

But contour completeness does not repair comparator containment or local counterterm freedom.

## 7. Strong blueprint for future KG

This control shows a successful structural pattern:

`one finite microscopic operator`

`+ state/contour/measure`

`-> all-point effective interaction hierarchy`

`+ real-time continuation`.

A novel KG could use an analogous compression mechanism only if it independently derives a **new gravity-native interacting operator/process** and simultaneously fixes the local renormalization/null sector.

The new primitive may not be selected by simply writing a novel `Delta` by hand.

## 8. Score consequence

Positive all-point-generator control only. No P4/P5/P6 credit. R4 remains 45%.
