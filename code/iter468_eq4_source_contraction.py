#!/usr/bin/env python3
import argparse, itertools, json, math, sys

VERTICES=(1,2,3,4,5)
EDGES=tuple((a,b) for a in VERTICES for b in VERTICES if a<b)

def edge_name(e): return f"{e[0]}{e[1]}"
def rho_name(e): return f"rhot_{edge_name(e)}"

def base_object(root=1):
    groups=[a for a in VERTICES if a!=root]
    spectral=[rho_name(e) for e in EDGES]
    weights={rho_name(e):f"W_{edge_name(e)}({rho_name(e)})" for e in EDGES}
    d_factors={rho_name(e):f"D_{edge_name(e)}[{rho_name(e)}](g_{e[1]}^-1 g_{e[0]})" for e in EDGES}
    return {"root":root,"groups":groups,"spectral":spectral,"weights":weights,"d_factors":d_factors}

def stream_a():
    o=base_object(1)
    unique=len(set(o['spectral']))==10
    group_count=len(o['groups'])==4
    local=True
    for r in o['spectral']:
        local &= (r in o['weights'][r] and r in o['d_factors'][r])
        local &= all(r not in o['weights'][q] and r not in o['d_factors'][q] for q in o['spectral'] if q!=r)
    ok=(len(EDGES)==10 and unique and group_count and local)
    return {"stream":"A","edge_count":len(EDGES),"spectral_count":len(o['spectral']),"group_count":len(o['groups']),"unique_spectral":unique,"wedge_local_before_group_integration":local,"pass":ok}

def permute_edge(e,p):
    a,b=p[e[0]],p[e[1]]
    return tuple(sorted((a,b)))

def stream_b():
    checked=0; bad=[]
    for perm in itertools.permutations(VERTICES):
        p={VERTICES[i]:perm[i] for i in range(5)}
        pedges=[permute_edge(e,p) for e in EDGES]
        root=p[1]
        spectral=[rho_name(e) for e in pedges]
        ok=(len(set(pedges))==10 and len(set(spectral))==10 and len([v for v in VERTICES if v!=root])==4)
        if not ok: bad.append({"perm":perm,"root":root})
        checked+=1
    return {"stream":"B","permutations_checked":checked,"bad":bad,"pass":checked==120 and not bad}

def stream_c():
    o=base_object(1)
    weights=list(o['weights'].values()); ds=list(o['d_factors'].values())
    kernel_dependencies=sorted(o['spectral'])
    factorized=(len(weights)==10 and len(ds)==10 and len(set(kernel_dependencies))==10)
    all_depend=all(any(r in d for d in ds) for r in kernel_dependencies)
    expression={"spectral_measure_count":10,"weight_product":weights,"common_group_kernel":{"group_integral_count":4,"D_product":ds,"depends_on":kernel_dependencies}}
    return {"stream":"C","formal_object":expression,"unique_factorization_shape":factorized,"kernel_depends_on_all_ten":all_depend,"pass":factorized and all_depend}

def validate_candidate(spectral, group_count, d_count, artificial_constraints):
    return (len(spectral)==10 and len(set(spectral))==10 and group_count==4 and d_count==10 and not artificial_constraints)

def stream_d():
    good=[rho_name(e) for e in EDGES]
    controls={
      "shared_spectral":validate_candidate(["rhot_shared"]*10,4,10,False),
      "nine_spectral":validate_candidate(good[:9],4,10,False),
      "five_groups":validate_candidate(good,5,10,False),
      "missing_wedge":validate_candidate(good,4,9,False),
      "artificial_delta":validate_candidate(good,4,10,True),
    }
    ok=all(v is False for v in controls.values())
    return {"stream":"D","negative_controls_accepted":controls,"all_negative_controls_rejected":ok,"pass":ok}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A','B','C','D'],required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); f={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[a.stream]; res=f()
    res['gate']='ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED'
    with open(a.out,'w') as h: json.dump(res,h,indent=2,sort_keys=True)
    print(json.dumps(res,indent=2,sort_keys=True))
    return 0 if res['pass'] else 2
if __name__=='__main__': sys.exit(main())
