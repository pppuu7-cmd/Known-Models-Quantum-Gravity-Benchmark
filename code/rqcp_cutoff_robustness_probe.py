#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rqcp_fixed_band_probe_common import QUARTIC, spectral_geometry


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    data = spectral_geometry(args.cutoff, quartic_value=QUARTIC)
    result = {
        "schema_version": "1.0",
        "probe_type": "hilbert_cutoff",
        "claim_scope": "exploratory robustness of the published fixed-band control only",
        "result": data,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
