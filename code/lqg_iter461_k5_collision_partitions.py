import argparse, json, os
from collections import defaultdict
from fractions import Fraction
from math import comb

EXPECTED={'2+1+1+1':10,'2+2+1':15,'3+1+1':10,'3+2':10,'4+1':5,'5':1}

def partitions(seq):
    if not seq:
        yield []
        return
    first,*rest=seq
    for p in partitions(rest):
        yield [[first]]+[b[:] for b in p]
        for i in range(len(p)):
            q=[b[:] for b in p]; q[i]=[first]+q[i]
            yield q

def canon(p):
    blocks=[tuple(sorted(b)) for b in p]
    return tuple(sorted(blocks,key=lambda b:(b[0],len(b),b)))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='iter461_summary.json'); a=ap.parse_args()
    uniq={canon(p) for p in partitions(list(range(5)))}
    nontrivial=[p for p in uniq if len(p)<5]
    groups=defaultdict(list); records=[]
    for p in sorted(nontrivial):
        sizes=sorted((len(b) for b in p),reverse=True); key='+'.join(map(str,sizes))
        internal=sum(comb(s,2) for s in sizes); cross=10-internal
        rel=sum(s-1 for s in sizes); dim=3*rel; crit=Fraction(dim,internal)
        rec={'partition':[list(b) for b in p],'type':key,'block_sizes':sizes,'internal_edges':internal,'cross_edges':cross,
             'relative_vectors':rel,'local_dimension':dim,'critical_pair_power_fraction':f'{crit.numerator}/{crit.denominator}',
             'critical_pair_power':float(crit),'boundary_rule':'p >= pcrit => UNRESOLVED_NEEDS_CORRELATED_COLLISION_BOUND'}
        records.append(rec); groups[key].append(rec)
    multiplicities={k:len(v) for k,v in groups.items()}; grouped={}
    for k,v in sorted(groups.items()):
        r=v[0]; grouped[k]={'multiplicity':len(v),'internal_edges':r['internal_edges'],'cross_edges':r['cross_edges'],
                            'relative_vectors':r['relative_vectors'],'local_dimension':r['local_dimension'],
                            'critical_pair_power_fraction':r['critical_pair_power_fraction'],'critical_pair_power':r['critical_pair_power']}
    tests={'bell_total':len(uniq)==52,'nontrivial_total':len(nontrivial)==51,'collision_type_count':len(groups)==6,
           'type_multiplicities':multiplicities==EXPECTED,'edge_identity':all(r['internal_edges']+r['cross_edges']==10 for r in records),
           'dimension_identity':all(r['local_dimension']==3*sum(s-1 for s in r['block_sizes']) for r in records)}
    ok=all(tests.values())
    out={'iteration':461,'tests':tests,'bell_total':len(uniq),'nontrivial_partitions':len(nontrivial),'type_multiplicities':multiplicities,
         'grouped_thresholds':grouped,'records':records,'classification':'ITER461_EXACT_K5_COLLISION_PARTITION_THRESHOLDS_QUALIFIED_SCOPED' if ok else 'SCIENTIFIC_FAIL_ITER461_K5_PARTITION_ENUMERATION',
         'pass':ok,'scope':'Naive pair-power threshold geometry only. Nonpositive margin is unresolved, never a divergence declaration. D7-S2 remains open.'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True); json.dump(out,open(a.out,'w'),indent=2); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
