# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:36:40 2019

@author: siva
"""

def obtuseAll(N,startA = 2,startCounts = 0):
  a = max(1,startA)
  Lima = N //3
  count = startCounts
  while (a < Lima):
    b = a
    while (b <= N//2):
      #print(a,b)
      lhs = a**2 + b**2 +1
      c = (lhs ** 0.5)
      if ( (c == int(c)) and (a + b + c <=N) ):
        count += 1
        print(a,b,c)
      b += 4
    a += 2
  return count

#Dictionary to have N, count
countDict = {15:1}
#Q = int(input())
#for i in range(Q):
#  N.append(int(input()))

NL = [10000]
s_NL = NL.copy()
s_NL.sort()
print(s_NL)
for N in s_NL:
  #seenN = max([x for x in list(countDict.keys()) if x < N])
  #dictC = countDict[seenN]
  #print("Calling N=",N,"start=",seenN,"C=",dictC)
  c = obtuseAll(N)
  countDict[N] = c
for N in NL:
  print(countDict[N])
