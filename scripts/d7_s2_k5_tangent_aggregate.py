#!/usr/bin/env python3
import hashlib,json,sys
r=json.load(open(sys.argv[1])); t=json.load(open(sys.argv[2]))
rr=r['scientific']['roots']; tr=t['scientific']['roots']
roots_ok=all(rr[str(i)]=={'rank':4,'domain_nullity':0,'left_nullity':6} for i in range(1,6))
tree_ok=all(tr[str(i)]['tree_count']==125 and tr[str(i)]['all_unimodular'] and tr[str(i)]['rank_from_nonzero_4minor']==4 and tr[str(i)]['cycle_dimension_from_rank']==6 for i in range(1,6))
cycle_ok=(r['scientific']['cycle_basis_rank']==6 and all(r['scientific']['cycle_annihilates_all_roots'].values()))
root_change_ok=(r['scientific']['root_change_cases_checked']==20 and r['scientific']['root_changes_unimodular'] and all(abs(x)==1 for x in r['scientific']['root_change_determinants'].values()))
valid=(r['classification']=='PASS_SCOPED' and t['classification']=='PASS_SCOPED' and roots_ok and tree_ok and cycle_ok and root_change_ok and r['scientific']['triangle_match'] and r['scientific']['s5_exact_transport'] and r['scientific']['s5_root_transport_cases_checked']==600 and t['scientific']['total_tree_root_minors']==625 and t['scientific']['global_minor_values']==[-1,1] and r['scientific']['iter466_consistency'] and t['scientific']['iter466_consistency'])
scientific={
 'gate':'D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_GATE',
 'classification':'D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_PASS_SCOPED' if valid else 'D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_FAIL_SCOPED',
 'governing_preregistration':'bc9aa01263df1172206eb211b456bf5d78fe1b1b',
 'execution_coverage_repair':'c0f8500aee43d4ee5686fc8dfc7b313e94b299d5',
 'per_generator':{'domain_dimension':4,'codomain_dimension':10,'rank':4,'domain_nullity':0,'cycle_left_nullity':6},
 'full_real_sl2c':{'domain_dimension':24,'codomain_dimension':60,'rank':24,'domain_nullity':0,'cycle_left_nullity':36},
 'all_five_gauge_roots_agree':roots_ok,
 'explicit_integer_cycle_basis_rank':r['scientific']['cycle_basis_rank'],
 'cycle_basis_annihilates_all_roots':cycle_ok,
 'root_change_cases_checked':r['scientific']['root_change_cases_checked'],
 'all_root_changes_integer_unimodular':root_change_ok,
 'root_change_determinant_values':sorted(set(r['scientific']['root_change_determinants'].values())),
 'spanning_trees_per_root':125,
 'tree_root_minors_checked':625,
 'all_tree_minors_unimodular':tree_ok,
 'tree_minor_values':[-1,1] if tree_ok else t['scientific']['global_minor_values'],
 's5_root_transport_cases_checked':r['scientific']['s5_root_transport_cases_checked'],
 's5_exact_orientation_transport':r['scientific']['s5_exact_transport'],
 'triangle_parent_differential_match':r['scientific']['triangle_match'],
 'iter466_topology_consistency':r['scientific']['iter466_consistency'] and t['scientific']['iter466_consistency'],
 'independent_methods':['exact rational RREF + explicit cycle/root/S5 transport','independent spanning-tree enumeration + fraction-free determinant minors'],
 'd7_s2_layer_closed':'RAW_GROUP_VARIABLE_TANGENT_PUSHFORWARD_ONLY' if valid else 'NO',
 'claim_ceiling':'no distributional/contact pushforward; no physical quotient/rank; no Haar/contact normalization; no observable pushforward; no D7-S2 closure; no selector/model/family/new-theory conclusion'
}
b=json.dumps(scientific,sort_keys=True,separators=(',',':')).encode(); out={'valid':valid,'scientific':scientific,'scientific_sha256':hashlib.sha256(b).hexdigest(),'lane_sha256':{'rref':r['scientific_sha256'],'tree':t['scientific_sha256']}}
json.dump(out,sys.stdout,sort_keys=True,indent=2);print();sys.exit(0 if valid else 2)
