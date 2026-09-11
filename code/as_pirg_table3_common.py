#!/usr/bin/env python3
"""Shared frozen Table III payload for arXiv:2609.07829 PIRG audit.

Values are transcribed from Table III of Ihssen et al., arXiv:2609.07829v1.
This module is descriptive only: it does not encode terminal PASS/FAIL thresholds.
"""

import json
from pathlib import Path

SOURCE = {
    "arxiv": "2609.07829v1",
    "title": "Diffeomorphism-invariant Approach to Asymptotically Safe Quantum Gravity",
    "submitted": "2026-09-07",
    "table": "III",
    "canonical_exponents": [4.0, 2.0],
}

ROWS = [
    {"id": "a_flow_back", "action": "a", "procedure": "flow", "g_completion": "back", "lambda": -0.142, "g": 1.830, "theta1": 3.86, "theta2": 1.95},
    {"id": "a_flow_fluc", "action": "a", "procedure": "flow", "g_completion": "fluc", "lambda": -0.224, "g": 2.956, "theta1": 4.00, "theta2": 2.05},
    {"id": "a_nielsen_back", "action": "a", "procedure": "nielsen", "g_completion": "back", "lambda": 0.135, "g": 1.130, "theta1": 6.68, "theta2": 1.87},
    {"id": "b_flow_back", "action": "b", "procedure": "flow", "g_completion": "back", "lambda": -0.473, "g": 2.369, "theta1": 4.66, "theta2": 1.89},
    {"id": "b_flow_fluc", "action": "b", "procedure": "flow", "g_completion": "fluc", "lambda": -0.638, "g": 3.339, "theta1": 4.83, "theta2": 2.07},
    {"id": "b_nielsen_back", "action": "b", "procedure": "nielsen", "g_completion": "back", "lambda": -0.031, "g": 1.551, "theta1": 3.70, "theta2": 1.81},
]


def write_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def symmetric_relative_difference(a, b):
    denom = 0.5 * (abs(a) + abs(b))
    return 0.0 if denom == 0 else abs(a - b) / denom
