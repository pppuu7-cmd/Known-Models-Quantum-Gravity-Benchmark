#!/usr/bin/env python3
import json,re,subprocess,pathlib

files=subprocess.check_output(['git','ls-files'],text=True).splitlines()
SELF='code/iter473_source_kernel_executable_audit.py'
code_files=[f for f in files if f.endswith('.py') and f!=SELF]
num_integrators=('mp.quad','quad(','nquad(','cubature','vegas','integrate.','quadrature')
numeric_special=('hyp2f1','hyper(','gamma(','wigner','toller','matrix_element')
control_tokens=('negative_control','controls','assert ','tolerance','residual','pass')
rows=[]
for fn in code_files:
    try: text=pathlib.Path(fn).read_text(encoding='utf-8')
    except Exception: continue
    low=text.lower()
    spectral=set(re.findall(r'rhot_[1-5][1-5]',text))
    ten_inputs=(len(spectral)>=10 or ('spectral_count' in low and '10' in low) or 'ten spectral' in low)
    four_groups=(('group_integral_count' in low and '4' in low) or all(f'g_{i}' in text for i in (2,3,4,5)))
    numeric_factor=any(t in low for t in numeric_special) and ('mp.' in low or 'numpy' in low or 'scipy' in low)
    actual_integrator=any(t in low for t in num_integrators)
    depends_ten=(len(spectral)>=10 or ('depends_on' in low and 'spectral' in low and '10' in low))
    validation=any(t in low for t in control_tokens)
    symbolic_only=('group_integral_count' in low and not actual_integrator) or ('formal_object' in low and not actual_integrator)
    req={'ten_distinct_spectral_inputs':ten_inputs,'four_group_or_exact_reduction':four_groups,'numeric_source_factor_eval':numeric_factor,'actual_group_integration_or_bound':actual_integrator,'ten_variable_output_dependency':depends_ten,'validation_or_controls':validation,'symbolic_only_flag':symbolic_only}
    score=sum(req[k] for k in ('ten_distinct_spectral_inputs','four_group_or_exact_reduction','numeric_source_factor_eval','actual_group_integration_or_bound','ten_variable_output_dependency','validation_or_controls'))
    if score or 'toller' in low or 'sl(2,c)' in low or 'sl2c' in low:
        rows.append({'file':fn,'score':score,'requirements':req})
rows.sort(key=lambda x:(-x['score'],x['file']))
qualified=[r for r in rows if all(r['requirements'][k] for k in ('ten_distinct_spectral_inputs','four_group_or_exact_reduction','numeric_source_factor_eval','actual_group_integration_or_bound','ten_variable_output_dependency','validation_or_controls')) and not r['requirements']['symbolic_only_flag']]
classification='EXECUTABLE_SOURCE_KERNEL_FOUND_SCOPED' if qualified else 'BLOCKED_SOURCE_KERNEL_EXECUTABLE_NOT_PRESENT_IN_TRACKED_REPO_SCOPED'
out={'iteration':473,'classification':classification,'audit_completed':True,'self_auditor_excluded':True,'tracked_python_files':len(code_files),'qualified_candidates':qualified,'top_candidates':rows[:25],'scope':'tracked-repository executable availability only; BLOCKED is not impossibility or literature absence; no convergence/divergence inference','d7_s2':'NOT_CLOSED'}
pathlib.Path('artifacts').mkdir(exist_ok=True); pathlib.Path('artifacts/iter473-summary.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
