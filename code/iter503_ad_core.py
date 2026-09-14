#!/usr/bin/env python3
"""Validated interval-AD helper for frozen Iter503."""
import numpy as np
from flint import arb, acb, ctx
import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
ctx.prec = 384
FLOOR = arb('1e-60')

def _ar(x):
    if isinstance(x, arb):
        return x
    if isinstance(x, int):
        return arb(x)
    if isinstance(x, str):
        return arb(x)
    return arb(repr(float(x)))


def _ac(x=0):
    if isinstance(x, acb):
        return x
    return acb(x)


class RD:
    __slots__ = ('v', 'd')
    def __init__(self, v=0, d=0):
        self.v = _ar(v)
        self.d = _ar(d)
    def __add__(self, other):
        if isinstance(other, CD):
            return other.__radd__(self)
        o = as_r(other)
        return RD(self.v + o.v, self.d + o.d)
    __radd__ = __add__
    def __sub__(self, other):
        if isinstance(other, CD):
            return as_c(self) - other
        o = as_r(other)
        return RD(self.v - o.v, self.d - o.d)
    def __rsub__(self, other):
        if isinstance(other, CD):
            return other - as_c(self)
        o = as_r(other)
        return RD(o.v - self.v, o.d - self.d)
    def __neg__(self):
        return RD(-self.v, -self.d)
    def __mul__(self, other):
        if isinstance(other, CD) or isinstance(other, acb):
            return as_c(self) * as_c(other)
        o = as_r(other)
        return RD(self.v * o.v, self.d * o.v + self.v * o.d)
    __rmul__ = __mul__
    def __truediv__(self, other):
        if isinstance(other, CD) or isinstance(other, acb):
            return as_c(self) / as_c(other)
        o = as_r(other)
        return RD(self.v / o.v, (self.d * o.v - self.v * o.d) / (o.v * o.v))
    def __rtruediv__(self, other):
        if isinstance(other, CD) or isinstance(other, acb):
            return as_c(other) / as_c(self)
        o = as_r(other)
        return o / self
    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError('RD power must be integer')
        if n == 0:
            return RD(1, 0)
        if n < 0:
            return RD(1, 0) / (self ** (-n))
        return RD(self.v ** n, n * (self.v ** (n - 1)) * self.d)
    def exp(self):
        ev = self.v.exp()
        return RD(ev, ev * self.d)
    def log(self):
        return RD(self.v.log(), self.d / self.v)
    def sin(self):
        return RD(self.v.sin(), self.v.cos() * self.d)
    def cos(self):
        return RD(self.v.cos(), -self.v.sin() * self.d)
    def sinh(self):
        return RD(self.v.sinh(), self.v.cosh() * self.d)
    def cosh(self):
        return RD(self.v.cosh(), self.v.sinh() * self.d)
    def sqrt(self):
        sv = self.v.sqrt()
        return RD(sv, self.d / (2 * sv))


class CD:
    __slots__ = ('v', 'd')
    def __init__(self, v=0, d=0):
        self.v = _ac(v)
        self.d = _ac(d)
    @property
    def real(self):
        return RD(self.v.real, self.d.real)
    @property
    def imag(self):
        return RD(self.v.imag, self.d.imag)
    def conjugate(self):
        return CD(self.v.conjugate(), self.d.conjugate())
    def __add__(self, other):
        o = as_c(other)
        return CD(self.v + o.v, self.d + o.d)
    __radd__ = __add__
    def __sub__(self, other):
        o = as_c(other)
        return CD(self.v - o.v, self.d - o.d)
    def __rsub__(self, other):
        o = as_c(other)
        return CD(o.v - self.v, o.d - self.d)
    def __neg__(self):
        return CD(-self.v, -self.d)
    def __mul__(self, other):
        o = as_c(other)
        return CD(self.v * o.v, self.d * o.v + self.v * o.d)
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = as_c(other)
        return CD(self.v / o.v, (self.d * o.v - self.v * o.d) / (o.v * o.v))
    def __rtruediv__(self, other):
        o = as_c(other)
        return o / self
    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError('CD power must be integer')
        if n == 0:
            return CD(1, 0)
        if n < 0:
            return CD(1, 0) / (self ** (-n))
        return CD(self.v ** n, n * (self.v ** (n - 1)) * self.d)
    def exp(self):
        ev = self.v.exp()
        return CD(ev, ev * self.d)


def as_r(x):
    if isinstance(x, RD):
        return x
    if isinstance(x, CD):
        raise TypeError('cannot coerce complex dual to real dual')
    return RD(x, 0)


def as_c(x):
    if isinstance(x, CD):
        return x
    if isinstance(x, RD):
        return CD(acb(x.v), acb(x.d))
    return CD(x, 0)


def iexp(x):
    x = as_r(x)
    return CD(acb(0, x.v), acb(0, x.d)).exp()


def dconj(z):
    return as_c(z).conjugate()


def dabs2(z):
    z = as_c(z)
    return z.real * z.real + z.imag * z.imag


def dmm(A, B):
    n = len(A); k = len(B); m = len(B[0])
    return [[sum((as_c(A[i][q]) * as_c(B[q][j]) for q in range(k)), CD(0))
             for j in range(m)] for i in range(n)]


def ddagger(M):
    return [[dconj(M[j][i]) for j in range(len(M))] for i in range(len(M[0]))]


def ddiag2(a, b):
    return [[as_c(a), CD(0)], [CD(0), as_c(b)]]


def promote_matrix(M):
    return [[as_c(z) for z in row] for row in M]


def value_matrix(M):
    return [[as_c(z).v for z in row] for row in M]


def drx(x):
    x = as_r(x); c = (x / 2).cos(); s = (x / 2).sin(); I = as_c(acb(0, 1))
    return [[as_c(c), -I * s], [-I * s, as_c(c)]]


def dry(x):
    x = as_r(x); c = (x / 2).cos(); s = (x / 2).sin()
    return [[as_c(c), as_c(-s)], [as_c(s), as_c(c)]]


def drz(x):
    x = as_r(x)
    return ddiag2(iexp(-x / 2), iexp(x / 2))


def dnorm2_pair(w):
    return dabs2(w[0]) + dabs2(w[1])


def dkak_ball(h):
    a = dabs2(h[0][0]) + dabs2(h[1][0])
    d = dabs2(h[0][1]) + dabs2(h[1][1])
    c = dconj(h[0][0]) * h[0][1] + dconj(h[1][0]) * h[1][1]
    t = (a + d) / 2
    delta = (a - d) / 2
    rad = (delta * delta + dabs2(c)).sqrt()
    lp = t + rad; lm = t - rad; sep = lp - lm
    if not (lm.v.lower() > arb(0) and sep.v.lower() > arb(0)):
        raise ArithmeticError('AD KAK eigenvalue positivity/separation not certified')
    wA = [c, as_c(lp - a)]
    wB = [as_c(lp - d), dconj(c)]
    nA2 = dnorm2_pair(wA); nB2 = dnorm2_pair(wB)
    loA = nA2.v.lower(); loB = nB2.v.lower()
    if not (loA > FLOOR or loB > FLOOR):
        raise ArithmeticError('AD KAK eigenvector chart norm not certified')
    w = wA if loA >= loB else wB
    chart = 'A' if loA >= loB else 'B'
    n = dnorm2_pair(w).sqrt()
    v = [w[0] / n, w[1] / n]
    V = [[v[0], -dconj(v[1])], [v[1], dconj(v[0])]]
    U2 = ddagger(V)
    beta = (lp.log() - lm.log()) / 2
    if not beta.v.lower() > arb(0):
        raise ArithmeticError('AD positive beta not certified')
    Ainv = ddiag2((-beta / 2).exp(), (beta / 2).exp())
    U1 = dmm(dmm(h, V), Ainv)
    return {'U1': U1, 'beta': beta, 'U2': U2, 'chart': chart,
            'chart_norm2_lower': loA if chart == 'A' else loB}


def promote_kak(k):
    return {'U1': promote_matrix(k['U1']), 'beta': RD(k['beta'], 0),
            'U2': promote_matrix(k['U2']), 'chart': k.get('chart')}


def value_kak(k):
    return {'U1': value_matrix(k['U1']), 'beta': as_r(k['beta']).v,
            'U2': value_matrix(k['U2'])}


def dwith_outer(km, left, right):
    return {'U1': dmm(left, km['U1']), 'beta': km['beta'], 'U2': dmm(km['U2'], right)}


def construct_dual_state(R, direction, sign, amp):
    B, Binv, _, _, G, Gi = enable.build_factors(R, direction, sign, arb(0))
    Bp = promote_matrix(B); Binvp = promote_matrix(Binv)
    Gp = [None if i == 0 else promote_matrix(G[i]) for i in range(5)]
    Gip = [None if i == 0 else promote_matrix(Gi[i]) for i in range(5)]
    d20 = [0] * 20
    for k, c in enumerate(core.COORDS):
        d20[c] = int(sign) * int(direction[k])
    eps = amp * ((-core.A(R)).exp())
    L = [promote_matrix(core.eye2()) for _ in range(5)]
    RR = [promote_matrix(core.eye2()) for _ in range(5)]
    for a in range(1, 5):
        q = [eps * d20[(a - 1) * 5 + j] for j in range(5)]
        L[a] = dmm(dmm(drx(q[0]), dry(q[1])), drz(q[2]))
        RR[a] = dmm(drx(q[3]), dry(q[4]))
    nodes = {}; nk = {}; edges = {}; ek = {}; checks = []
    for a in range(1, 5):
        middle_raw = core.mm(B, G[a])
        km = promote_kak(core.kak_ball(middle_raw))
        middle = promote_matrix(middle_raw)
        h = dmm(dmm(L[a], middle), RR[a])
        k = dwith_outer(km, L[a], RR[a])
        ok, detail = enable.validate_full(value_matrix(h), value_kak(k))
        checks.append(('node', a, ok, detail)); nodes[a] = h; nk[a] = k
    for a, b in core.EDGES:
        if a == 0:
            middle_raw = core.mm(Gi[b], Binv)
            km = promote_kak(core.kak_ball(middle_raw))
            middle = promote_matrix(middle_raw)
            left = ddagger(RR[b]); right = ddagger(L[b])
            h = dmm(dmm(left, middle), right)
            k = dwith_outer(km, left, right)
        else:
            middle = dmm(Gip[b], Binvp)
            middle = dmm(middle, ddagger(L[b])); middle = dmm(middle, L[a])
            middle = dmm(middle, Bp); middle = dmm(middle, Gp[a])
            km = dkak_ball(middle)
            left = ddagger(RR[b]); right = RR[a]
            h = dmm(dmm(left, middle), right)
            k = dwith_outer(km, left, right)
        ok, detail = enable.validate_full(value_matrix(h), value_kak(k))
        checks.append(('edge', [a, b], ok, detail)); edges[(a, b)] = h; ek[(a, b)] = k
    return {'nodes': nodes, 'node_kak': nk, 'edges': edges, 'edge_kak': ek, 'checks': checks}


def dspin1(U):
    a, b = U[0]; c, d = U[1]; q = as_r(arb(2).sqrt())
    return [
        [d * d, q * c * d, c * c],
        [q * b * d, a * d + b * c, q * a * c],
        [b * b, q * a * b, a * a],
    ]


def dsource_coeffs(m, rho, b):
    r = as_r(repr(float(rho))); den = r + r ** 3
    sh = b.sinh(); ch = b.cosh(); cs = 1 / sh; ct = ch / sh
    br = b * r; ep = iexp(br); em = iexp(-br)
    co = br.cos(); si = br.sin(); sh2 = (2 * b).sinh(); ch2 = (2 * b).cosh()
    e2 = (2 * b).exp(); I = as_c(acb(0, 1))
    if m == 0:
        dv = -12 * e2 * (((e2 - 1) * r * co - (e2 + 1) * si)) / ((e2 - 1) ** 3 * den)
        tp = -3 * ep * (as_c(r) + I * ct) * cs ** 2 / (2 * den)
        tm = -3 * em * (as_c(r) - I * ct) * cs ** 2 / (2 * den)
    elif m == -1:
        dv = 12 * (3 * b).exp() * (-si + ep * r * sh * (as_c(ch) - I * r * sh)) / ((e2 - 1) ** 3 * den)
        tp = 3 * ep * cs ** 3 * (I * (1 + r ** 2) + r * (as_c(sh2) - I * r * ch2)) / (4 * den)
        tm = -3 * I * em * cs ** 3 / (4 * den)
    elif m == 1:
        phase = b * (as_c(3) - I * r)
        dv = 6 * phase.exp() * (I * (ep ** 2 - r ** 2 - 1) + r * (I * r * ch2 + sh2)) / ((e2 - 1) ** 3 * den)
        tp = 3 * I * ep * cs ** 3 / (4 * den)
        tm = 3 * cs ** 3 * (I * co + si) * (-r ** 2 + r ** 2 * ch2 - I * r * sh2 - 1) / (4 * den)
    else:
        raise ValueError(m)
    return as_c(dv), as_c(tp), as_c(tm)


def dfull_toller(kak, rho, branch):
    U1, U2, b = kak['U1'], kak['U2'], kak['beta']
    ps = []; ms = []; additive = True
    for m in (-1, 0, 1):
        d, p, n = dsource_coeffs(m, rho, b)
        additive = additive and (p.v + n.v - d.v).contains(0)
        ps.append(p); ms.append(n)
    vals = ps if branch == 'p' else ms
    L = dspin1(U1); R = dspin1(U2)
    out = [[sum((L[i][k] * vals[k] * R[k][j] for k in range(3)), CD(0))
            for j in range(3)] for i in range(3)]
    return out, bool(additive)


def _dual_tstack():
    out = np.empty(core.TSTACK.shape, dtype=object)
    for idx in np.ndindex(out.shape):
        out[idx] = as_c(core.TSTACK[idx])
    return out


DTSTACK = _dual_tstack()


def dcontract_all(mats):
    args = []; outlabels = list(range(20, 25))
    for node in range(5):
        args += [DTSTACK, [20 + node] + core.ctrl.NODE_LABELS[node]]
    for ei, M in enumerate(mats):
        args += [np.asarray(M, dtype=object), core.ctrl.EDGE_LABELS[ei]]
    args += [outlabels]
    return np.einsum(*args, optimize=core.BALL_PATH)


def centered_channels(midvals, dualvals, delta):
    out = np.empty(midvals.shape, dtype=object)
    for idx in np.ndindex(midvals.shape):
        z0 = core.C(midvals[idx])
        dz = as_c(dualvals[idx]).d
        out[idx] = z0 + delta * dz
    return out
