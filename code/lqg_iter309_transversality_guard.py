#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter309_distribution_transversality.json'))
c=p['prospectively_frozen_claims']
ok=(c['generic_exact_direction_rank']==10 and c['collinear_direction_rank']==4 and c['collinear_left_nullity']==6 and
    (not c['full_row_rank_transversality_holds_everywhere_on_common_identity_support']) and
    (not c['standard_sufficient_delta_product_transversality_criterion_closes_vertex_distribution_product']))
out={'probe':'transversality_guard','pass':bool(ok),'iteration':309,
     'generic_rank':10,'collinear_rank':4,'collinear_rank_defect':6,
     'standard_sufficient_transversality_everywhere':False,
     'scientific_consequence':'wedge-level distributional definitions do not automatically establish a canonical ten-wedge product on the entire identity support',
     'non_consequence':'failure of a sufficient criterion is not a proof that no extended/renormalized product can be constructed'}
pathlib.Path('build/lqg-iter309').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter309/transversality_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
