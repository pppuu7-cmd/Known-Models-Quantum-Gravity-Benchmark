#!/usr/bin/env python3
"""Shared exact objects for Iter281 LQG spinfoam-stack Hessian audit.

The 6x6 matrix is the explicit 1-5 Pachner-move t-t block published in
Section VII.2 of Muxin Han, Phys. Rev. D 113, 084034 (2026),
arXiv:2510.26926v1. C0,C1,C2 follow the published Hessian formulas.
"""
import json
from fractions import Fraction
from pathlib import Path

SOURCE={
 "title":"Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG",
 "author":"Muxin Han",
 "journal":"Physical Review D 113, 084034 (2026)",
 "doi":"10.1103/n76f-31gf",
 "arxiv":"2510.26926v1",
 "published":"2026-04-14"
}

M=[
 [-3, 1, 1,-1,-1, 0],
 [ 1,-3, 1, 1, 0,-1],
 [ 1, 1,-3, 0, 1, 1],
 [-1, 1, 0,-3, 1,-1],
 [-1, 0, 1, 1,-3, 1],
 [ 0,-1, 1,-1, 1,-3],
]

# Non-tree edges [23,24,25,34,35,45] for K5 with spanning tree [12,13,14,15].
# Each row is the oriented boundary coefficient of one triangular face projected
# onto non-tree edges. With these conventions the published quadratic-form
# relation gives M=-B^T B.
B=[
 [1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,1,0,0,0],
 [0,0,0,1,0,0], [0,0,0,0,1,0], [0,0,0,0,0,1],
 [1,-1,0,1,0,0], [1,0,-1,0,1,0], [0,1,-1,0,0,1], [0,0,0,1,-1,1],
]

def transpose(a): return [list(x) for x in zip(*a)]
def matmul(a,b):
 bt=transpose(b)
 return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]
def scalar(a,c): return [[c*x for x in row] for row in a]

def det_bareiss(a):
 a=[list(map(int,row)) for row in a]; n=len(a); sign=1; prev=1
 if n==0: return 1
 for k in range(n-1):
  if a[k][k]==0:
   swap=next((i for i in range(k+1,n) if a[i][k]!=0),None)
   if swap is None: return 0
   a[k],a[swap]=a[swap],a[k]; sign*=-1
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])//prev
  prev=pivot
  for i in range(k+1,n): a[i][k]=0
 return sign*a[-1][-1]

def rank_fraction(a):
 a=[[Fraction(x) for x in row] for row in a]; m=len(a); n=len(a[0]); r=0
 for c in range(n):
  p=next((i for i in range(r,m) if a[i][c]),None)
  if p is None: continue
  a[r],a[p]=a[p],a[r]
  q=a[r][c]; a[r]=[x/q for x in a[r]]
  for i in range(m):
   if i!=r and a[i][c]:
    q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==m: break
 return r

def kron_identity3(a):
 n=len(a); out=[[0]*(3*n) for _ in range(3*n)]
 for i in range(n):
  for j in range(n):
   for q in range(3): out[3*i+q][3*j+q]=a[i][j]
 return out

def write_json(path,payload):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
