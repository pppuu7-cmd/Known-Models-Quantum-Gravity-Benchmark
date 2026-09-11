#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rqcp_fixed_band_probe_common import QUARTIC, spectral_geometry


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--factor", type=float, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    quartic_value = QUARTIC * float(args.factor)
    data = spectral_geometry(8, quartic_value=quartic_value)
    result = {
        "schema_version": "1.0",
        "probe_type": "quartic_coupling",
        "claim_scope": "exploratory fixed-band parameter robustness; no family-level promotion",
        "quartic_factor": float(args.factor),
        "result": data,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
