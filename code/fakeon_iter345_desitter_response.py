#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp

# Source object: Piva, Eur. Phys. J. Plus 138, 876 (2023),
# eqs. (5.28)-(5.32). The tree-level fakeon prescription averages
# retarded and advanced Green functions; eq. (5.31) gives the de Sitter G_f.
mp.mp.dps = 60


def fakeon_green(H: mp.mpf, mratio: mp.mpf, kratio: mp.mpf, t: mp.mpf, tp: mp.mpf) -> mp.mpc:
    n = mp.sqrt(mratio*mratio - mp.mpf('0.25'))
    dt = t - tp
    if dt == 0:
        return mp.mpc(0)
    sgn = mp.mpf(1) if dt > 0 else mp.mpf(-1)
    ck = kratio / mp.e**(H*t)
    ckp = kratio / mp.e**(H*tp)
    pref = 1j * mp.pi * sgn * mp.e**(-mp.mpf('1.5')*H*dt) / (4*H*mp.sinh(mp.pi*n))
    det = (mp.besselj(1j*n, ck)*mp.besselj(-1j*n, ckp)
           - mp.besselj(1j*n, ckp)*mp.besselj(-1j*n, ck))
    return pref*det


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--mratio', type=str, required=True)
    ap.add_argument('--output', required=True)
    a = ap.parse_args()
    H = mp.mpf('1')
    mratio = mp.mpf(a.mratio)
    if not (mratio > mp.mpf('0.5')):
        raise ValueError('require m_chi/H > 1/2 so n_chi is real in the frozen audit domain')
    kgrid = [mp.mpf('0.2'), mp.mpf('1.0'), mp.mpf('3.0')]
    dtgrid = [mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('1.0')]
    rows=[]
    future_sq = mp.mpf('0')
    past_sq = mp.mpf('0')
    min_future = mp.inf
    max_imag_fraction = mp.mpf('0')
    for k in kgrid:
        for dt in dtgrid:
            # Evaluate response at t=0. Future source point tp=+dt is forbidden
            # to an ordinary retarded response but is part of the fakeon kernel.
            gf_future = fakeon_green(H,mratio,k,mp.mpf('0'),dt)
            gf_past = fakeon_green(H,mratio,k,mp.mpf('0'),-dt)
            af = abs(gf_future); apast = abs(gf_past)
            future_sq += af*af; past_sq += apast*apast
            min_future = min(min_future,af)
            max_imag_fraction=max(max_imag_fraction,abs(mp.im(gf_future))/max(af,mp.mpf('1e-50')))
            rows.append({
                'k_over_H':float(k),'delta_t_H':float(dt),
                'fakeon_future_real':float(mp.re(gf_future)),
                'fakeon_future_imag':float(mp.im(gf_future)),
                'fakeon_future_abs':float(af),
                'fakeon_past_abs':float(apast),
                'retarded_future_abs':0.0,
            })
    assert min_future > mp.mpf('1e-8'), min_future
    assert max_imag_fraction < mp.mpf('1e-40'), max_imag_fraction
    out={
      'iteration':345,
      'source':'Piva EPJ Plus 138 (2023) 876, eqs. 5.28-5.32',
      'source_definition':'tree-level fakeon Green function = average of retarded and advanced Green functions; de Sitter kernel from eq. 5.31',
      'H_units':1.0,'m_chi_over_H':float(mratio),
      'probe_count':len(rows),'probes':rows,
      'future_support_L2':float(mp.sqrt(future_sq)),
      'past_support_L2':float(mp.sqrt(past_sq)),
      'minimum_future_support_abs':float(min_future),
      'maximum_imaginary_fraction':float(max_imag_fraction),
      'classification':'PASS_SCOPED_SOURCE_DEFINED_DESITTER_FAKEON_GREEN_FUNCTION_HAS_NONZERO_FUTURE_SOURCE_SUPPORT_WHERE_RETARDED_COMPARATOR_IS_ZERO',
      'scope_guard':[
        'SOURCE_DEFINED_LINEAR_FAKEON_RESPONSE_KERNEL',
        'EXPLICIT_DESITTER_MODE_RESPONSE_ONLY',
        'NONZERO_FUTURE_SUPPORT_CERTIFIES_CONTROLLED_MICROCAUSAL_RESPONSE_NOT_PATHOLOGY_BY_ITSELF',
        'NOT_A_NORMALIZED_GRAVITATIONAL_OBSERVABLE',
        'NOT_A_FULL_SAME_REALIZATION_COMPARATOR_PACKAGE',
        'NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION'
      ]
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__':
    main()
