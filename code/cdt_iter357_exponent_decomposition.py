#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument("--delta",type=float,required=True)
p.add_argument("--output",required=True)
a=p.parse_args()
pvals=[-0.40,-0.30,-0.25,-0.20,-0.10,-0.01]
rows=[]
for po in pvals:
    q=a.delta-2*po
    te=po+0.25
    if te>0: cls="DIVERGES"
    elif te<0: cls="SHRINKS"
    else: cls="CONSTANT"
    rows.append({"p_omega":po,"q_Gamma":q,"two_p_plus_q":2*po+q,"time_extension_exponent":te,"time_extension_class":cls})
valid=[r for r in rows if r["p_omega"]<0 and r["time_extension_class"]=="DIVERGES"]
invalid=[r for r in rows if r["p_omega"]<0 and r["time_extension_class"]!="DIVERGES"]
out={
 "iteration":357,
 "delta":a.delta,
 "relation":"2 p_omega + q_Gamma = delta",
 "source_limit_omega_to_zero_encoded_as":"p_omega < 0",
 "required_uv_time_extension":"p_omega + 1/4 > 0",
 "rows":rows,
 "has_same_product_scaling_with_valid_time_extension":bool(valid),
 "has_same_product_scaling_with_invalid_time_extension":bool(invalid),
 "product_exponent_alone_identifies_time_extension":False,
 "scope":"power-law identifiability audit; does not fit p_omega or q_Gamma from raw CDT data"
}
with open(a.output,"w") as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
