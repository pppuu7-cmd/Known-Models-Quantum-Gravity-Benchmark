#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rqcp_fixed_band_probe_common import QUARTIC, mixed_response


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sigma-step", type=float, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    data = mixed_response(8, quartic_value=QUARTIC, sigma_step=args.sigma_step)
    result = {
        "schema_version": "1.0",
        "probe_type": "mixed_response_step",
        "claim_scope": "numerical robustness of the published fixed-band mixed response only",
        "result": data,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
