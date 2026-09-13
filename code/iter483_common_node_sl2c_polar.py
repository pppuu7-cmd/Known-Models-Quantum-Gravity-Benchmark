#!/usr/bin/env python3
import json, math, os, pathlib, itertools
import numpy as np

PANELS={
 'A':[(0,0,0),(.17,.43,-.29),(-.38,.71,.52),(.61,.84,.33),(-.47,.58,-.76)],
 'B':[(0,0,0),(.93,.52,-.41),(-.74,1.03,.26),(-1.11,.67,.89),(.68,.92,-1.02)],
 'C':[(0,0,0),(.29,.36,.77),(-.83,.57,-.24),(.51,1.12,-.66),(-.42,.88,.95)],
 'D':[(0,0,0),(-.55,.49,.24),(.72,.81,-.37),(-.31,1.03,.68),(.88,.64,-.91)],
}
BOOSTS={'mild':[0,.16,.27,.34,.43],'strong':[0,.62,.91,1.17,1.39]}
EDGES=[(a,b) for a in range(5) for b in range(a+1,5)]
I2=np.eye(2,dtype=np.complex128)

def su2(a,t,g):
    ca=np.cos(t/2); sa=np.sin(t/2)
    rz1=np.diag([np.exp(-.5j*a),np.exp(.5j*a)])
    ry=np.array([[ca,-sa],[sa,ca]],dtype=np.complex128)
    rz2=np.diag([np.exp(-.5j*g),np.exp(.5j*g)])
    return rz1@ry@rz2

def boost(eta):
    return np.diag([np.exp(eta/2),np.exp(-eta/2)]).astype(np.complex128)

def nodes(panel,regime,compact=False):
    out=[]
    etas=BOOSTS[regime]
    for i,(a,t,g) in enumerate(PANELS[panel]):
        if i==0: out.append(I2.copy()); continue
        UL=su2(a,t,g); UR=su2(-.37*g,.73*t,.41*a)
        out.append(UL@boost(0 if compact else etas[i])@UR)
    return out

def relatives(gs):
    return {(a,b):np.linalg.inv(gs[b])@gs[a] for a,b in EDGES}

def cycle_res(rs):
    return max(float(np.max(np.abs(rs[(b,c)]@rs[(a,b)]-rs[(a,c)]))) for a,b,c in itertools.combinations(range(5),3))

def polar(h):
    A=h@h.conj().T
    ev,V=np.linalg.eigh(A)
    H=(V*np.sqrt(ev))@V.conj().T
    U=np.linalg.solve(H,h)
    he=np.linalg.eigvalsh(H)
    eta=float(np.log(he[-1]/he[0]))
    return H,U,he,eta

def evaluate(panel,regime):
    gs=nodes(panel,regime)
    rs=relatives(gs)
    node_det=max(abs(np.linalg.det(g)-1) for g in gs)
    edge_det=max(abs(np.linalg.det(h)-1) for h in rs.values())
    cyc=cycle_res(rs)
    G=su2(.22,.51,-.36)@boost(.47)@su2(-.17,.39,.28)
    rsg=relatives([G@g for g in gs])
    gauge=max(float(np.max(np.abs(rsg[e]-rs[e]))) for e in EDGES)
    herm=0.; minev=1e9; hdet=0.; uunit=0.; udet=0.; recon=0.; svrel=0.; inveta=0.; etas=[]
    for e,h in rs.items():
        H,U,he,eta=polar(h); etas.append(eta)
        herm=max(herm,float(np.max(np.abs(H-H.conj().T))))
        minev=min(minev,float(np.min(he)))
        hdet=max(hdet,float(abs(np.linalg.det(H)-1)))
        uunit=max(uunit,float(np.max(np.abs(U.conj().T@U-I2))))
        udet=max(udet,float(abs(np.linalg.det(U)-1)))
        recon=max(recon,float(np.max(np.abs(H@U-h))))
        sv=np.sort(np.linalg.svd(h,compute_uv=False)); he2=np.sort(he)
        svrel=max(svrel,float(np.max(np.abs(sv-he2))/max(float(np.max(sv)),1e-300)))
        _,_,_,ei=polar(np.linalg.inv(h)); inveta=max(inveta,abs(ei-eta))
    corrupt=dict(rs); corrupt[(0,1)]=boost(.31)@corrupt[(0,1)]
    corrupt_cycle=cycle_res(corrupt)
    rsc=relatives(nodes(panel,regime,compact=True))
    comp_eta=0.; comp_unit=0.
    for h in rsc.values():
        _,_,_,ee=polar(h); comp_eta=max(comp_eta,ee)
        comp_unit=max(comp_unit,float(np.max(np.abs(h.conj().T@h-I2))))
    finite_nonneg=all(np.isfinite(x) and x>=-1e-13 for x in etas)
    checks={
      'node_det':node_det<1e-11,'relative_det':edge_det<1e-11,'cycle':cyc<1e-11,'common_left_gauge':gauge<1e-11,
      'polar_hermitian':herm<1e-11,'polar_positive':minev>1e-10,'polar_det':hdet<1e-10,
      'unitary_factor':uunit<1e-10 and udet<1e-10,'reconstruction':recon<1e-10,
      'rapidity_consistency':finite_nonneg and svrel<1e-10,'inversion_rapidity':inveta<1e-10,
      'corrupt_negative':corrupt_cycle>1e-4,'compact_regression':comp_eta<1e-10 and comp_unit<1e-10,
    }
    ok=all(checks.values())
    return {'iteration':'483','lane':f'{panel}-{regime}','panel':panel,'regime':regime,'scientific_pass':ok,
      'classification':'ITER483_COMMON_NODE_SL2C_POLAR_GEOMETRY_QUALIFIED_SCOPED' if ok else 'FAIL_ITER483_COMMON_NODE_SL2C_POLAR_GEOMETRY',
      'checks':checks,'node_det_max':float(node_det),'edge_det_max':float(edge_det),'cycle_residual':cyc,'gauge_residual':gauge,
      'polar_hermiticity_max':herm,'polar_min_eigenvalue':minev,'polar_det_residual':hdet,'unitary_residual':uunit,'unitary_det_residual':udet,
      'reconstruction_residual':recon,'singular_value_relative_residual':svrel,'inversion_eta_residual':inveta,
      'eta_min':float(min(etas)),'eta_max':float(max(etas)),'corrupted_cycle_residual':corrupt_cycle,
      'compact_eta_max':comp_eta,'compact_unitarity_residual':comp_unit,
      'scope':'shared-node SL2C kinematic/polar prerequisite only; no source Toller KAK identification, Haar/spectral/full-vertex claim',
      'd7_s2':'NOT_CLOSED','d7_s3':'NOT_CLOSED','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED'}

def main():
    panel=os.environ['ITER483_PANEL']; regime=os.environ['ITER483_REGIME']
    out=evaluate(panel,regime); pathlib.Path('artifacts').mkdir(exist_ok=True)
    pathlib.Path(f'artifacts/iter483-{out["lane"]}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2)); raise SystemExit(0 if out['scientific_pass'] else 2)
if __name__=='__main__': main()
