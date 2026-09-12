#!/usr/bin/env python3
import argparse, json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--table', required=True)
p.add_argument('--metric', required=True)
p.add_argument('--si-percent', type=float, required=True)
p.add_argument('--dsi-percent', type=float, required=True)
p.add_argument('--reported-ratio', type=float, required=True)
p.add_argument('--si-decimals', type=int, required=True)
p.add_argument('--dsi-decimals', type=int, required=True)
p.add_argument('--reported-decimals', type=int, required=True)
p.add_argument('--output', required=True)
a = p.parse_args()

assert a.si_percent > 0 and a.dsi_percent > 0 and a.reported_ratio > 0
assert min(a.si_decimals, a.dsi_decimals, a.reported_decimals) >= 0
half_si = 0.5 * 10 ** (-a.si_decimals)
half_dsi = 0.5 * 10 ** (-a.dsi_decimals)
half_reported = 0.5 * 10 ** (-a.reported_decimals)
si_lo, si_hi = a.si_percent-half_si, a.si_percent+half_si
dsi_lo, dsi_hi = a.dsi_percent-half_dsi, a.dsi_percent+half_dsi
reported_lo, reported_hi = a.reported_ratio-half_reported, a.reported_ratio+half_reported
assert si_lo > 0 and dsi_lo >= 0 and reported_lo > 0
raw_ratio = a.dsi_percent / a.si_percent
ratio_min = dsi_lo / si_hi
ratio_max = dsi_hi / si_lo
relerr = abs(raw_ratio-a.reported_ratio)/a.reported_ratio
bins_overlap = max(ratio_min, reported_lo) <= min(ratio_max, reported_hi)
passed = bins_overlap and relerr < 0.05
out = {
  'record_type':'published_ratio', 'table':a.table, 'metric':a.metric,
  'si_percent':a.si_percent, 'dsi_percent':a.dsi_percent,
  'reported_ratio':a.reported_ratio, 'raw_ratio':raw_ratio,
  'relative_error_to_reported_ratio':relerr,
  'published_input_rounding_ratio_interval':[ratio_min, ratio_max],
  'published_reported_ratio_display_interval':[reported_lo, reported_hi],
  'rounding_bins_overlap':bins_overlap,
  'classification':'PASS_PUBLISHED_RATIO_REPRODUCED_WITH_MUTUAL_ROUNDING_ENVELOPE' if passed else 'FAIL_PUBLISHED_RATIO_REPRODUCTION'
}
Path(a.output).parent.mkdir(parents=True, exist_ok=True)
Path(a.output).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
print(json.dumps(out, sort_keys=True))
if not passed: raise SystemExit(2)
