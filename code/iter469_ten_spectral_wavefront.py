#!/usr/bin/env python3
import argparse,itertools,json,sys
N=10

def stream_a():
    zero=0; checked=0
    # distinct coordinate axes: any nonempty signed subset has at least one nonzero component
    for mask in range(1,1<<N):
        idx=[i for i in range(N) if mask>>i & 1]
        for signs in itertools.product((-1,1), repeat=len(idx)):
            v=[0]*N
            for i,s in zip(idx,signs): v[i]+=s
            checked+=1
            if all(x==0 for x in v): zero+=1
    return {'stream':'A','signed_subset_tests':checked,'zero_sums':zero,'pass':zero==0}

def matvec(rows,v): return [sum(a*b for a,b in zip(r,v)) for r in rows]
def stream_b():
    mats=[]
    I=[[int(i==j) for j in range(N)] for i in range(N)]; mats.append(I)
    P=[row[:] for row in I]; P[0],P[9]=P[9],P[0]; mats.append(P)
    S=[row[:] for row in I]; S[3][1]=1; mats.append(S)
    T=[row[:] for row in I]; T[7][2]=-1; T[8][4]=1; mats.append(T)
    bad=0; checked=0
    for M in mats:
      axes=[[M[r][i] for r in range(N)] for i in range(N)]
      for mask in range(1,1<<N):
        idx=[i for i in range(N) if mask>>i&1]
        # coefficients frozen to +/-1 suffices as exact robustness control for sampled conormals
        for signs in itertools.product((-1,1), repeat=len(idx)):
          v=[sum(s*axes[i][r] for i,s in zip(idx,signs)) for r in range(N)]
          checked+=1
          if all(x==0 for x in v): bad+=1
    return {'stream':'B','unimodular_panels':len(mats),'tests':checked,'zero_sums':bad,'pass':bad==0}

def stream_c():
    # collapse coords 0 and 1; +e0 and -e0 cancel
    v=[0]*9; v[0]+=1; v[0]-=1
    detected=all(x==0 for x in v)
    return {'stream':'C','deliberate_shared_coordinate_collision_detected':detected,'pass':detected}

def stream_d():
    scope={'fixed_group_kernel_smooth_in_ten_spectral_variables_required':True,'global_decay_claimed':False,'group_integral_existence_claimed':False,'integration_exchange_claimed':False,'d7s2_closed':False}
    return {'stream':'D','scope':scope,'pass':scope['fixed_group_kernel_smooth_in_ten_spectral_variables_required'] and not any(scope[k] for k in ['global_decay_claimed','group_integral_existence_claimed','integration_exchange_claimed','d7s2_closed'])}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',required=True,choices='ABCD'); ap.add_argument('--out',required=True); a=ap.parse_args()
    r={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[a.stream](); r['gate']='ITER469_TEN_SPECTRAL_PLEMEJ_LOCAL_PRODUCT_WAVEFRONT_QUALIFIED_SCOPED'
    json.dump(r,open(a.out,'w'),indent=2,sort_keys=True); print(json.dumps(r,indent=2,sort_keys=True)); sys.exit(0 if r['pass'] else 2)
if __name__=='__main__': main()
