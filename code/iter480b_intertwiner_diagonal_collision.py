#!/usr/bin/env python3
import itertools, json, pathlib, os
import mpmath as mp
import numpy as np
from sympy.physics.wigner import wigner_3j

mp.mp.dps = 70
MS = [-1, 0, 1]
EDGES = [(a,b) for a in range(5) for b in range(a+1,5)]
INC = {a:[EDGES.index(e) for e in EDGES if a in e] for a in range(5)}
SIGMAS = {
    '0to5': (1,1,1,1,1),
    '1to4': (-1,1,1,1,1),
    '2to3': (-1,-1,1,1,1),
}
GAMMAS = [7,8]
ZERO_RATIO_THRESHOLD = 1e-12
REINDEX_RTOL = 1e-10


def coeff(m, rho, plus=True):
    jx=mp.mpf(1); mx=mp.mpf(m); rx=mp.mpf(rho); ii=mp.j; N=3
    if plus:
        a=jx+mx+1; b=jx+1-ii*rx; c=1+mx-ii*rx
        pref=mp.gamma(4)*mp.gamma(ii*rx-mx)/(mp.gamma(jx-mx+1)*mp.gamma(jx+1+ii*rx))
    else:
        a=jx-mx+1; b=jx+1+ii*rx; c=1-mx+ii*rx
        pref=mp.gamma(4)*mp.gamma(-ii*rx+mx)/(mp.gamma(jx+mx+1)*mp.gamma(jx+1-ii*rx))
    return complex(pref*mp.gamma(c)*mp.gamma(N)/(mp.gamma(a)*mp.gamma(b)))


def intertwiner(i):
    T=np.zeros((3,3,3,3), dtype=np.complex128)
    for ms in itertools.product(MS, repeat=4):
        v=0j
        for m in range(-i,i+1):
            term = ((-1)**(i-m))*wigner_3j(1,1,i,ms[0],ms[1],m)*wigner_3j(i,1,1,-m,ms[2],ms[3])
            v += complex(term.evalf(40))
        T[tuple(x+1 for x in ms)] = v
    return T


def controls(tensors):
    support_ok=True
    for T in tensors:
        for idx in np.ndindex(T.shape):
            ms=tuple(i-1 for i in idx)
            if sum(ms)!=0 and abs(T[idx])>1e-14:
                support_ok=False
    gram=np.array([[np.vdot(tensors[i],tensors[j]) for j in range(3)] for i in range(3)])
    target=np.diag([1.0,1/3,1/5])
    gram_res=float(np.max(np.abs(gram-target)))
    return support_ok, gram_res, bool(support_ok and gram_res<1e-12)


def contract(channels, tensors, vecs, path):
    args=[]
    for a,ch in enumerate(channels):
        args += [tensors[ch], INC[a]]
    for e,v in enumerate(vecs):
        args += [v,[e]]
    args += [[]]
    return np.einsum(*args, optimize=path)


def build_path(tensors):
    args=[]
    for a in range(5): args += [tensors[0], INC[a]]
    for e in range(10): args += [np.ones(3,dtype=np.complex128), [e]]
    args += [[]]
    return np.einsum_path(*args, optimize='greedy')[0]


def reindexed_tensors(tensors):
    return [T[::-1,::-1,::-1,::-1].copy() for T in tensors]


def evaluate_panel(gamma, name, sig, tensors, path):
    vecs=[]
    for a,b in EDGES:
        plus=(sig[a]*sig[b]>0)
        vecs.append(np.array([coeff(m,gamma,plus) for m in MS],dtype=np.complex128))
    scale=float(np.prod([np.max(np.abs(v)) for v in vecs]))
    scale_ok=bool(np.isfinite(scale) and scale>0)
    channels=list(itertools.product(range(3),repeat=5))
    vals=np.array([contract(ch,tensors,vecs,path) for ch in channels],dtype=np.complex128)
    mags=np.abs(vals)
    ratios=mags/scale if scale_ok else np.full_like(mags,np.inf)
    nz=ratios>ZERO_RATIO_THRESHOLD
    max_idx=int(np.argmax(ratios))

    rtens=reindexed_tensors(tensors)
    rvecs=[v[::-1].copy() for v in vecs]
    rvals=np.array([contract(ch,rtens,rvecs,path) for ch in channels],dtype=np.complex128)
    sm=np.sort(mags); srm=np.sort(np.abs(rvals))
    multiset_scale=float(max(np.max(sm),np.max(srm),1e-300))
    reindex_res=float(np.max(np.abs(sm-srm))/multiset_scale)
    reindex_ok=bool(reindex_res<REINDEX_RTOL)

    zeros=[np.zeros(3,dtype=np.complex128) for _ in range(10)]
    zmax=max(abs(contract(ch,tensors,zeros,path)) for ch in channels)
    zero_ok=bool(zmax<1e-14)

    return {
        'gamma': gamma, 'causal_representative': name, 'scale': scale,
        'scale_finite_positive': scale_ok,
        'total_channels': len(channels), 'nonzero_witnesses': int(np.count_nonzero(nz)),
        'zero_or_below_threshold': int(len(channels)-np.count_nonzero(nz)),
        'max_ratio': float(ratios[max_idx]), 'max_abs_contraction': float(mags[max_idx]),
        'max_channel': list(channels[max_idx]),
        'witness_exists': bool(np.any(nz)),
        'reindex_relative_residual': reindex_res, 'reindex_control_pass': reindex_ok,
        'zero_vector_negative_max_abs': float(zmax), 'zero_vector_negative_pass': zero_ok,
    }


def main():
    gamma=int(os.environ.get('ITER480B_GAMMA','7'))
    name=os.environ.get('ITER480B_CLASS','0to5')
    if gamma not in GAMMAS or name not in SIGMAS:
        raise SystemExit('invalid frozen lane')
    tensors=[intertwiner(i) for i in range(3)]
    support_ok, gram_res, intertwiner_ok=controls(tensors)
    path=build_path(tensors)
    panel=evaluate_panel(gamma,name,SIGMAS[name],tensors,path)
    checks={
        'eq90_intertwiner_support_norm_orthogonality': intertwiner_ok,
        'scale_finite_positive': panel['scale_finite_positive'],
        'nonzero_witness': panel['witness_exists'],
        'reindex_control': panel['reindex_control_pass'],
        'zero_vector_negative': panel['zero_vector_negative_pass'],
    }
    ok=all(checks.values())
    out={
        'iteration':'480B','lane':f'g{gamma}-{name}',
        'classification':'ITER480B_SOURCE_INTERTWINER_CONTRACTION_NONZERO_WITNESS_SCOPED' if ok else 'FAIL_ITER480B_SOURCE_INTERTWINER_CONTRACTION',
        'scientific_pass':ok,'checks':checks,
        'intertwiner_gram_max_residual':gram_res,
        'dimensionless_nonzero_threshold':ZERO_RATIO_THRESHOLD,
        'panel':panel,
        'scope':'j=1 equal-spin diagonal-collision boundary-intertwiner contraction only; no angular U matrices, Haar/group integration, spectral integration, Jacobian or full K5 collision conclusion',
        'd7_s2':'NOT_CLOSED','d7_s3':'NOT_CLOSED','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED'
    }
    pathlib.Path('artifacts').mkdir(exist_ok=True)
    fn=f'artifacts/iter480b-g{gamma}-{name}.json'
    pathlib.Path(fn).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    raise SystemExit(0 if ok else 2)

if __name__=='__main__': main()
