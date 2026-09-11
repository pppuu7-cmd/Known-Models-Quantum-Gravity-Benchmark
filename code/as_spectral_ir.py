#!/usr/bin/env python3
import argparse, math
from as_spectral_common import SOURCE,IR_A,IR_TAIL,write_json

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 derived=2*math.pi*IR_A
 write_json(a.output,{'probe':'as_spectral_ir_coefficient','source':SOURCE,'A_h_61_over_60pi':IR_A,'tail_onset_reported_61_over_30':IR_TAIL,'tail_onset_from_2pi_Ah':derived,'absolute_difference':abs(derived-IR_TAIL),'relative_difference':abs(derived-IR_TAIL)/IR_TAIL,'boundary':'Checks the published IR coefficient relation only; gauge dependence noted by the authors remains part of the claim boundary.'})
if __name__=='__main__': main()
