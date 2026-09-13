#!/usr/bin/env python3
"""Iter450 prospectively frozen static source-object qualification audit.

This script does NOT evaluate a vertex amplitude. It asks whether repository material
uniquely specifies one executable complete source-defined coupled magnetic/intertwiner
contraction for the direct causal vertex, under status/ITERATION_450.md.
"""
from __future__ import annotations
import argparse, json, pathlib, re, hashlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXCLUDE_PARTS = {'.git', '.venv', 'venv', '__pycache__', 'node_modules'}
TEXT_SUFFIX = {'.md','.txt','.tex','.py','.yml','.yaml','.json','.toml'}
# Frozen at implementation, before production output is inspected.
SOURCE_RE = re.compile(r'(arxiv|doi\s*:|https?://|source|citation|paper|equation\s*\(?\d+|eq\.\s*\(?\d+)', re.I)
CAUSAL_RE = re.compile(r'(causal.{0,40}vertex|vertex.{0,40}causal|Toller)', re.I)
FORMULA_RE = re.compile(r'(\\sum|sum\s*\(|A[_^]?v|vertex\s*amplitude|T[_+\-\^]|T\^|integral|\\int|contract)', re.I)
INDEX_RE = re.compile(r'(magnetic|intertwiner|\bm\b|\bj\b|\bi\b|index|indices|summation|sum over|range|domain)', re.I)
WEIGHT_RE = re.compile(r'(weight|phase|normalization|normalisation|branch|coefficient|dimension|2j\+1|face amplitude)', re.I)
CONVENTION_RE = re.compile(r'(orientation|ordering|order reversal|permutation|convention|EPRL|noncausal|control)', re.I)
EXPLICIT_COMPLETE_RE = re.compile(r'(complete|full|exact|source-defined|published).{0,80}(contraction|vertex|formula)|(?:contraction|vertex|formula).{0,80}(complete|full|exact|source-defined|published)', re.I)


def files():
    for p in ROOT.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIX:
            continue
        rel = p.relative_to(ROOT)
        if any(x in EXCLUDE_PARTS for x in rel.parts):
            continue
        # Do not allow this gate's own prereg/implementation to bootstrap qualification.
        if str(rel) in {'status/ITERATION_450.md', 'scripts/iter450_source_contraction_qualification.py'}:
            continue
        yield rel, p


def scan():
    rows=[]
    for rel,p in files():
        try: text=p.read_text(encoding='utf-8', errors='ignore')
        except Exception: continue
        lines=text.splitlines()
        causal_hits=[]
        for n,line in enumerate(lines,1):
            if CAUSAL_RE.search(line): causal_hits.append(n)
        if not causal_hits: continue
        # Use +-12-line neighborhoods so evidence must be locally tied to causal/Toller discussion.
        covered=set()
        for n in causal_hits:
            lo=max(1,n-12); hi=min(len(lines),n+12)
            covered.update(range(lo,hi+1))
        local='\n'.join(lines[n-1] for n in sorted(covered))
        evidence={
            'source': bool(SOURCE_RE.search(local)),
            'formula': bool(FORMULA_RE.search(local)),
            'indices': bool(INDEX_RE.search(local)),
            'weights': bool(WEIGHT_RE.search(local)),
            'conventions': bool(CONVENTION_RE.search(local)),
            'explicit_complete': bool(EXPLICIT_COMPLETE_RE.search(local)),
        }
        anchors=[]
        for n in causal_hits[:12]:
            anchors.append({'line':n,'text':lines[n-1][:240]})
        rows.append({'path':str(rel),'evidence':evidence,'anchors':anchors,
                     'sha256':hashlib.sha256(text.encode()).hexdigest()})
    return rows


def lane_result(lane, rows):
    predicates={
      'formula_identity': lambda e: e['source'] and e['formula'] and e['explicit_complete'],
      'index_domains': lambda e: e['formula'] and e['indices'] and e['explicit_complete'],
      'weights_phases_norms': lambda e: e['formula'] and e['weights'] and e['explicit_complete'],
      'controls_conventions': lambda e: e['formula'] and e['conventions'] and e['explicit_complete'],
    }
    pred=predicates[lane]
    candidates=[r for r in rows if pred(r['evidence'])]
    return {
      'iteration':450,'lane':lane,'candidate_paths':[r['path'] for r in candidates],
      'candidate_count':len(candidates),'evidence':candidates,
      'lane_qualified': len(candidates)>0,
      'interpretation':'Evidence collection only; aggregate requires one common unique candidate path across all four lanes.'
    }


def aggregate(inputs):
    docs=[json.loads(pathlib.Path(x).read_text()) for x in inputs]
    expected={'formula_identity','index_domains','weights_phases_norms','controls_conventions'}
    got={d.get('lane') for d in docs}
    if got != expected:
        cls='INVALID_ITER450_AUDIT'; common=[]
    else:
        sets=[set(d['candidate_paths']) for d in docs]
        common=sorted(set.intersection(*sets)) if sets else []
        if len(common)==1:
            cls='SOURCE_CAUSAL_INVARIANT_CONTRACTION_OBJECT_QUALIFIED'
        elif len(common)==0:
            # Distinguish incomplete from ambiguity using whether every lane had >=1 candidate.
            if all(d.get('candidate_count',0)>0 for d in docs):
                cls='BLOCKED_SOURCE_CAUSAL_INVARIANT_CONTRACTION_OBJECT_AMBIGUOUS'
            else:
                cls='BLOCKED_SOURCE_CAUSAL_INVARIANT_CONTRACTION_OBJECT_INCOMPLETE'
        else:
            cls='BLOCKED_SOURCE_CAUSAL_INVARIANT_CONTRACTION_OBJECT_AMBIGUOUS'
    return {
      'iteration':450,'classification':cls,'common_candidate_paths':common,
      'lane_summaries':[{k:d.get(k) for k in ('lane','candidate_count','candidate_paths','lane_qualified')} for d in docs],
      'scope_guard':'Qualification only; never D7-S2 closure or causal-vertex finiteness.',
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane', choices=['formula_identity','index_domains','weights_phases_norms','controls_conventions']); ap.add_argument('--aggregate', nargs='*'); ap.add_argument('--out', required=True); a=ap.parse_args()
    if a.aggregate is not None:
        out=aggregate(a.aggregate)
    else:
        out=lane_result(a.lane, scan())
    pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
