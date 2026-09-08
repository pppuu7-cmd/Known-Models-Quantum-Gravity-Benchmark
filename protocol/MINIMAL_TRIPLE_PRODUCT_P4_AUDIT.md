# Minimal One-Pole Triple-Product P4 Audit

**Status:** hard near-survivor audit / comparator-contained positive control.  
**KMQGB iteration:** 068.  
**Purpose:** preserve the closest low-freedom hard-amplitude candidate found in the current constructive search and record exactly why it does not qualify as a novel P4 parent.

## 1. General triple-product class

Huang and Remmen construct UV-complete four-graviton amplitudes of the form

`M4(s,t,u)=kappa^2 R^4 A(s) A(t) A(u)`

with a meromorphic one-variable factor schematically

`A(s)=1/s + sum_n g_n^2/(m_n^2-s)`

and a UV sum rule on the residues.

The broad class has arbitrary mass/residue spectral data `{m_n,g_n}` and therefore fails the KMQGB low-freedom requirement if that spectral data is treated as independent parent input.

Classification of the unrestricted class:

`A2 FUNCTIONAL_FREEDOM_BLOCKED__ARBITRARY_SPECTRAL_POLE_DATA`.

Reference: Y.-T. Huang and G. N. Remmen, *UV-complete gravity amplitudes and the triple product*, Phys. Rev. D 106, L021902 (2022), DOI 10.1103/PhysRevD.106.L021902.

## 2. Minimal nontrivial spectral-support restriction

Now impose a prospective **minimal-support** restriction inside that class:

- one massless graviton pole;
- exactly one additional simple massive pole in `A(s)`;
- no further independent massive pole data.

The UV residue condition fixes the single residue to unit magnitude in the normalized convention. With one mass scale `m`,

`A_1(s)=1/s + 1/(m^2-s)=m^2/[s(m^2-s)]`.

Thus

`M4_1pole = kappa^2 R^4 m^6 / [s t u (m^2-s)(m^2-t)(m^2-u)]`.

This is a genuine finite-data hard object: after the ordinary gravitational normalization, the deformation is controlled by one mass scale.

## 3. A2 — finite freedom

For this restricted object,

`A2 = PASS_IN_HARD_AMPLITUDE_SCOPE`.

There is no arbitrary function left at four points and no independent Wilson coefficient at every derivative order. The low-energy tower is generated from one `m`.

Relative to the Einstein four-graviton structure,

`M4_1pole / M4_GR = product_{x=s,t,u} (1-x/m^2)^(-1)`.

Using `s+t+u=0`, the order `m^-2` term cancels. The first local correction is fixed:

`1 + (s^2+t^2+u^2)/(2 m^4) + stu/m^6 + ...`,

with all higher coefficients linked by the same single scale.

This is exactly the type of rigidity that `P4_FUNCTIONAL_FREEDOM_NO_GO` is designed to preserve rather than reject.

## 4. A4 — explicit hard relation

At four points the object also satisfies the hard-data part of A4:

`A4 = PASS_IN_FOUR_POINT_AMPLITUDE_SCOPE`.

The pole locations, residues, UV softness and the complete `s,t,u` dependence are explicit and linked.

However, amplitude-level A4 by itself is not enough for KMQGB P4. The rubric also requires an explicit parent/constructive rule and a radiative/CTP/kinematic mapping plan.

## 5. A1 — historical status changed by later work

The original 2022 amplitude construction did not itself provide the microscopic/worldsheet parent needed by KMQGB.

A later result by Yu-Ping Wang supplies a chiral-string worldsheet construction for a subset of triple-product amplitudes:

Y.-P. Wang, *Triple product amplitude from chiral string*, JHEP 12 (2024) 112, DOI 10.1007/JHEP12(2024)112.

Under the twisted section-condition analysis, the nontrivial unitary rational triple-product case is

`F(s)=1/[s(s-1)] = 1/s + 1/(1-s)`

and

`M(s,t,u)=K_R K_L F(s)F(t)F(u)`.

After restoring the pole scale, this is precisely the one-mass-pole functional form above.

The same work provides a worldsheet/defect prescription, modified KLT construction and an explicit five-point chiral-string amplitude.

Therefore the minimal one-pole object is no longer merely an amplitude ansatz with no known constructive origin.

## 6. A3 — decisive comparator containment

The later worldsheet realization changes the KMQGB verdict decisively.

The one-pole minimal triple product belongs to a known **chiral-string / dual-resonance / worldsheet comparator architecture**.

Classification:

`A3 FAIL__CHIRAL_STRING_WORLD_SHEET_CONTAINED`.

This remains true even though the object is far more rigid than generic gravitational EFT and even though it has a clean hard amplitude. KMQGB novelty is defined relative to the strongest applicable comparator architecture, not relative to Einstein gravity alone.

## 7. Why this is an important positive control

This is the strongest constructive positive control found in the current search because it demonstrates all of the following simultaneously:

1. hard functional freedom can genuinely collapse to a one-scale family;
2. the resulting infinite EFT/Wilson tower can be rigidly predicted rather than independently fitted;
3. an explicit UV-soft four-graviton object can exist;
4. a later microscopic/worldsheet construction can explain the amplitude;
5. **the same success can eliminate novelty by revealing comparator containment**.

Thus the correct logic is

`A2 finite freedom + A4 hard relation + A1 constructive origin != KG novelty`

until A3/P5 comparator survival is passed.

## 8. Spectrum/escape classification

The massive pole carries an infinite higher-spin tower in the triple-product construction. The chiral-string realization likewise places the object in a string/higher-spin spectral sector.

Accordingly, any attempt to reinterpret the same amplitude as a new `E2` tower or `E1` nonlocal candidate without acknowledging the worldsheet comparator is forbidden.

A novel descendant would have to differ by a derived physical relation that is not reproduced by the chiral-string parent on the same hard domain.

## 9. No P4 score

Despite passing the low-freedom and hard-amplitude subtests, this object does **not** score P4 because the complete required deliverable asks for a novel parent outside known comparator architectures.

Current classification:

- A1: `PASS_KNOWN_WORLD_SHEET_PARENT`;
- A2: `PASS_ONE_SCALE_HARD_RIGIDITY`;
- A3: `FAIL_CHIRAL_STRING_CONTAINED`;
- A4: `PASS_FOUR_POINT_HARD_OBJECT`, with higher representation hierarchy known in the comparator rather than novel KG;
- P4: `NO_CREDIT`;
- P5: not applicable as a novel survivor.

## 10. Search lesson

The constructive search should not spend additional effort rediscovering one-pole triple products, twisted-string rational factors or close rescalings thereof.

The next hard candidate must either

- possess a finite-data nonanalytic/spectral rule outside known string/chiral-string/bootstrap/asymptotic-safety comparators, or
- derive a cross-representation/CTP relation not shared by those comparators.

This audit raises no readiness percentage by itself; it sharply identifies the current comparator boundary.
