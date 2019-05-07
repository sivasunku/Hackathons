# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:08:35 2019
Problem: https://www.hackerrank.com/challenges/merging-communities/problem
@author: siva
"""

def getSet(L,k1,k2):
  i,j = -1,-1
  lim = len(L)
  #print(L,k,lim)
  x = 0
  while (x < lim):
    if (k1 in L[i]):
      i = x
    if (k2 in L[i]):
      j = x
    if ((i != -1) and (j != -1)):
      return (i,j)
    x += 1
  return (i,j)

def Mfun(L,k1,k2):
  i,j = getSet(L,k1,k2)
  if ( i == -1):
    a = set()
    a.add(k1)
    L.append(a)
    i = len(L) - 1
  if (k1 == k2):
    j = i
  elif ( j == -1):
    a = set()
    a.add(k2)
    L.append(a)
    j = len(L) - 1
  #print("MFun J",L,k1,k2,i,j)
  if (i==j):
    pass
  else:
    L[i] = L[i].union(L[j])
    del L[j]
  return L

def Qfun(L,k):
  #print("Q func:",L,k)
  for s in L:
    if k in s:
      return len(s)
  return 1

temp = input().split()
N = int(temp[0])
Q = int(temp[1])
L = []
for i in range(Q):
  temp = input().split()
  if (temp[0] == 'Q'):
    k = int(temp[1])
    print(Qfun(L,k))
  else:
    k1 = int(temp[1])
    k2 = int(temp[2])
    L = Mfun(L,k1,k2)
#for i in range(Q):
#  N.append(int(input()))

    
