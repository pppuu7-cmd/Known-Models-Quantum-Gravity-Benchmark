#!/usr/bin/env python3
"""Common source-anchored formulas for NSF tree-amplitude claim-boundary audit.

The complete tree-level formula is taken from the abstract of arXiv:2605.24512:
M_tree = -kappa^2 s^3 / (4 t u), with kappa^2 = 32 pi G.
This module tests algebraic consequences only; it does not certify all-order quantum equivalence.
"""
import json, math
from pathlib import Path

SOURCE = {
    "part_I": "arXiv:2605.06961",
    "part_II": "arXiv:2605.19764",
    "part_III": "arXiv:2605.24512",
    "parent_formulation": "Null Surface Formulation of General Relativity",
}

def kappa2(G):
    return 32.0 * math.pi * G

def amplitude(s, t, u, G=1.0):
    return -kappa2(G) * s**3 / (4.0 * t * u)

def amplitude_G_form(s, t, u, G=1.0):
    return -8.0 * math.pi * G * s**3 / (t * u)

def write_json(path, payload):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
