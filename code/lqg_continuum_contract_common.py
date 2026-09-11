#!/usr/bin/env python3
"""Shared source contract for Iter282 spin-foam continuum-limit compatibility audit."""
import json
from pathlib import Path

SOURCE = {
  "title": "Structure of the continuum limit of spin foams",
  "authors": ["Matteo Bruno", "Eugenia Colafranceschi", "Fabio M. Mele", "Carlo Rovelli"],
  "journal": "Physical Review D 114, 066005 (2026)",
  "doi": "10.1103/7493-9nb7",
  "arxiv": "2603.16999",
  "published": "2026-09-08"
}

CLAIMS = {
  "model_independent_framework": True,
  "theorem_5_1": {
    "hypothesis": "for each manifold M, the refinement net converges to an element of the inductive boundary Hilbert space",
    "consequence": "the continuum map defines a TQFT",
    "gravity_boundary": "a non-topological 4D gravity model cannot use this strong Hilbert-space convergence for every M"
  },
  "distributional_path": {
    "uses_gelfand_triple": True,
    "limit_in_algebraic_dual": True,
    "cylinder_defines_rigging_map": True,
    "rigging_antilinear": True,
    "rigging_reality": True,
    "rigging_positive_semidefinite": True,
    "physical_hilbert_quotient_completion": True
  },
  "model_specificity_boundary": {
    "explicit_constraint_relation_available": False,
    "specified_physical_observable_algebra_available": False
  },
  "han_stack": {
    "infinite_internal_area_cutoff_regime": "topological_scale_invariant",
    "semiclassical_regge_gr_regime": "finite_large_cutoff_small_gamma",
    "same_realization_physical_uv_ir_bridge_explicit": False
  }
}

def write_json(path, payload):
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n", encoding="utf-8")
