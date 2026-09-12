#!/usr/bin/env python3
import argparse,itertools,json,math,os

V=tuple(range(5))
FIXED=0
UNFIXED=(1,2,3,4)
EDGES=tuple(itertools.combinations(V,2))


def crossing_edges(S):
    S=set(S)
    return [e for e in EDGES if (e[0] in S) ^ (e[1] in S)]


def main():
    p=argparse.ArgumentParser(); p.add_argument('--k',type=int,required=True); a=p.parse_args()
    if a.k not in (1,2,3,4): raise SystemExit('k must be 1..4')
    rows=[]
    for S in itertools.combinations(UNFIXED,a.k):
        cross=crossing_edges(S)
        expected=a.k*(5-a.k)
        haar=2*a.k
        decay=-len(cross)
        net=haar+decay
        rows.append({'subset':list(S),'crossing_edges':[list(e) for e in cross],'crossing_edge_count':len(cross),'expected_crossing_edge_count':expected,'haar_exponent':haar,'crossing_decay_exponent':decay,'net_common_shift_exponent':net,'count_valid':len(cross)==expected})
    expected_net=a.k*(a.k-3)
    all_valid=all(r['count_valid'] and r['net_common_shift_exponent']==expected_net for r in rows)
    certificate='SUFFICIENT_BY_THIS_BOUND' if expected_net<0 else 'UNRESOLVED_BY_THIS_BOUND'
    expected_cert={1:'SUFFICIENT_BY_THIS_BOUND',2:'SUFFICIENT_BY_THIS_BOUND',3:'UNRESOLVED_BY_THIS_BOUND',4:'UNRESOLVED_BY_THIS_BOUND'}[a.k]
    controls={'all_subsets_enumerated':len(rows)==math.comb(4,a.k),'all_cut_counts_exact':all(r['count_valid'] for r in rows),'net_exponent_exact':all(r['net_common_shift_exponent']==expected_net for r in rows),'certificate_matches_frozen_rule':certificate==expected_cert,'nonnegative_exponent_not_promoted_to_divergence':True}
    ok=all(controls.values())
    out={'iteration':445,'k':a.k,'subsets_tested':len(rows),'expected_subsets':math.comb(4,a.k),'rows':rows,'exact_net_common_shift_exponent':expected_net,'envelope_certificate':certificate,'controls':controls,'controls_valid':ok,'classification':'EXACT_K5_SINGLE_FACTOR_ENVELOPE_CARDINALITY_CLASS_VALID' if ok else 'CUT_CONE_DIAGNOSTIC_INVALID','scope_guard':'Classifies only the reach of the conservative one-factor envelope. UNRESOLVED_BY_THIS_BOUND is not divergence, FAIL, or a no-go theorem.','d7':'NOT_CLOSED / NOT_YET_AUTHORIZED','candidate_gravity_authorized':False}
    os.makedirs('build/lqg-iter445',exist_ok=True); fn=f'build/lqg-iter445/k{a.k}.json'; open(fn,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)

if __name__=='__main__': main()
