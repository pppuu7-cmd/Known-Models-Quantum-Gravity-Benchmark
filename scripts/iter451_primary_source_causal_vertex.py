#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, html, json, pathlib, re, urllib.request

URL='https://arxiv.org/html/2601.23162v1'
UA='KMQGB-Iter451-source-audit/1.0'


def fetch():
    req=urllib.request.Request(URL, headers={'User-Agent':UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw=r.read()
    s=raw.decode('utf-8','replace')
    # Preserve MathML/alt text as ordinary text as much as possible, then normalize whitespace.
    s=re.sub(r'<script\b.*?</script>',' ',s,flags=re.I|re.S)
    s=re.sub(r'<style\b.*?</style>',' ',s,flags=re.I|re.S)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'\s+',' ',s)
    return raw,s


def has_all(text, pats):
    return all(re.search(p,text,re.I) for p in pats)


def audit(lane, text, digest):
    common={'iteration':451,'lane':lane,'source_url':URL,'source_sha256':digest}
    if lane=='eq4_vertex_object':
        checks={
          'eq4_vertex_definition': has_all(text,[r'vertex amplitude',r'Toller',r'g\s*b\s*-?1\s*g\s*a|g b - 1 g a|g b − 1 g a',r'Eq\.?\s*\(?4\)?|\(4\) defines the vertex']),
          'gamma_simple': has_all(text,[r'gamma.?simple',r'ρ\s*,\s*k|rho\s*,\s*k',r'γ\s*j|gamma\s*j']),
          'five_edges': bool(re.search(r'a\s*=\s*1\s*,?\s*…?\s*,?\s*5|a=1,\s*\.\.\.,?5|a=1,\ldots,5',text,re.I)),
          'wedge_range': bool(re.search(r'1\s*[≤<]=?\s*a\s*<\s*b\s*[≤<]=?\s*5|1\s*≤\s*a\s*<\s*b\s*≤\s*5',text,re.I)),
          'gauge_fix': has_all(text,[r'gauge.?fix',r'g\s*1\s*=\s*(?:1|𝟙|I)|g1\s*=\s*1',r'g\s*a|g_a']),
        }
    elif lane=='boundary_contraction_domains':
        checks={
          'boundary_state': bool(re.search(r'spin-network boundary state|spin network boundary state',text,re.I)),
          'ten_spins': bool(re.search(r'10\s+spins',text,re.I)),
          'five_intertwiners': bool(re.search(r'5\s+intertwin',text,re.I)),
          'magnetic_numbers': bool(re.search(r'magnetic (?:numbers|indices)',text,re.I)),
          'state_sum_relation': bool(re.search(r'boundary state.{0,700}(?:sum|∑).{0,400}intertwin',text,re.I)),
        }
    elif lane=='toller_source_definition':
        checks={
          'feynman_definition': has_all(text,[r'Toller',r'Feynman',r'i\s*ε|iε|i\s*varepsilon',r'\(3\)']),
          'cartan_decomposition': has_all(text,[r'Cartan decomposition',r'U\s*1|U1',r'U\s*2|U2',r'\(7\)']),
          'finite_magnetic_sum': has_all(text,[r'sum|∑',r'p\s*=\s*-?\s*min|−\s*min|minimum',r'min\s*\(\s*j\s*,\s*l\s*\)']),
          'branch_sign': bool(re.search(r'T\s*\(?\s*±|T\s*\^?\s*\(\s*±|sign\s*±|sign.*determined',text,re.I)),
        }
    elif lane=='eprl_control':
        checks={
          'additive_identity': has_all(text,[r'T\s*\(?\s*\+|T\s*\^?\s*\(\s*\+',r'T\s*\(?\s*-|T\s*\^?\s*\(\s*-',r'=\s*D',r'\(5\)']),
          'eprl_unconstrained_sum': has_all(text,[r'EPRL vertex amplitude',r'unconstrained sum over wedge signs',r'κ|kappa',r'\(6\)']),
        }
    else:
        raise ValueError(lane)
    qualified=all(checks.values())
    return {**common,'checks':checks,'lane_qualified':qualified,
            'classification':'LANE_SOURCE_QUALIFIED' if qualified else 'LANE_SOURCE_INCOMPLETE'}


def aggregate(paths):
    docs=[json.loads(pathlib.Path(p).read_text()) for p in paths]
    exp={'eq4_vertex_object','boundary_contraction_domains','toller_source_definition','eprl_control'}
    got={d.get('lane') for d in docs}
    same_source=len({d.get('source_sha256') for d in docs})==1
    if got!=exp or not same_source:
        cls='INVALID_ITER451_SOURCE_FETCH_OR_PARSE'
    elif all(d.get('lane_qualified') for d in docs):
        cls='PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_PINNED'
    else:
        cls='BLOCKED_PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_INCOMPLETE'
    return {'iteration':451,'classification':cls,'same_source_digest':same_source,
            'source_sha256':docs[0].get('source_sha256') if docs else None,
            'lanes':[{'lane':d.get('lane'),'qualified':d.get('lane_qualified'),'checks':d.get('checks')} for d in docs],
            'scope_guard':'Source pinning only; not D7-S2 closure or a finiteness result.'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--lane',choices=['eq4_vertex_object','boundary_contraction_domains','toller_source_definition','eprl_control'])
    ap.add_argument('--aggregate',nargs='*')
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.aggregate is not None:
        out=aggregate(a.aggregate)
    else:
        raw,text=fetch(); out=audit(a.lane,text,hashlib.sha256(raw).hexdigest())
    pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
