#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def load(root):
    fs=sorted(Path(root).rglob('*.json'))
    if len(fs)!=1: raise SystemExit(f'expected one json in {root}, got {len(fs)}')
    return json.loads(fs[0].read_text()), hashlib.sha256(fs[0].read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rref',required=True);ap.add_argument('--minors',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
    x,hx=load(a.rref);y,hy=load(a.minors)
    keys=['gate','classification','source_provenance_ok','raw_generator_matrix','raw_generator_rank','raw_group_real_dimension','raw_domain_dimension','raw_codomain_dimension','raw_total_rank','raw_domain_nullity','raw_codomain_left_nullity','generator_left_relation','s3_raw_ranks','raw_rank_controls_ok','missing_physical_authority_fields','physical_transverse_rank','rank_status','fixtures','scientific_boundary']
    agree=all(x.get(k)==y.get(k) for k in keys)
    expected=(x.get('classification')=='EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_BLOCKED_SCOPED' and x.get('raw_generator_rank')==2 and x.get('raw_total_rank')==12 and x.get('physical_transverse_rank') is None and len(x.get('missing_physical_authority_fields',[]))>0)
    cls=x.get('classification') if agree and expected else 'EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_INVALID'
    out={'gate':x.get('gate'),'classification':cls,'independent_methods_agree':agree,'rref_json_sha256':hx,'minors_json_sha256':hy,'rref_scientific_payload_sha256':x.get('scientific_payload_sha256'),'minors_scientific_payload_sha256':y.get('scientific_payload_sha256'),'raw_generator_rank':x.get('raw_generator_rank'),'raw_total_rank':x.get('raw_total_rank'),'raw_domain_nullity':x.get('raw_domain_nullity'),'raw_codomain_left_nullity':x.get('raw_codomain_left_nullity'),'generator_left_relation':x.get('generator_left_relation'),'missing_physical_authority_fields':x.get('missing_physical_authority_fields'),'physical_transverse_rank':x.get('physical_transverse_rank'),'rank_status':x.get('rank_status'),'downstream_physical_transversality_authorized':False,'scientific_boundary':x.get('scientific_boundary')}
    raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['aggregate_sha256']=hashlib.sha256(raw).hexdigest();Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 0 if cls!='EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_INVALID' else 2
if __name__=='__main__': raise SystemExit(main())
