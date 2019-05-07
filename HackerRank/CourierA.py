# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:45:27 2019

@author: siva
"""
def nearest10(n):
  n1 = (n // 10) * 10
  n2 = n1 + 10
  return (n2 if n - n1 > n2 - n else n1)
def cost(a,b):
  #Cost of travel from a -> b and b -> a are same.
  i,j = sorted([a,b])
  costs = []
  
  #Direct Bus
  costs += [5 * abs(i-j)]

  #Back to nearest Tram and travel
  iTramPos = nearest10(i)
  jTramPos = nearest10(j)
  tBetween = (jTramPos -iTramPos) // 10
  costs += [abs(i-iTramPos) * 5 + tBetween*25 + abs(j-jTramPos)*5]
  
  #Bus to next Tram and go
  iTramPos = (i//10)*10 + 10
  jTramPos = nearest10(j)
  tBetween = (jTramPos -iTramPos) // 10
  costs += [abs(i-iTramPos) * 5 + tBetween*25 + abs(j-jTramPos)*5]
  print(costs)
  return(min(costs))
  

input1 = list(map(int, input().rstrip().split()))
inp = [0] + input1
i = 1
sum = 0
while i < len(inp):
  t = cost(inp[i-1],inp[i])
  sum += t
  #print(t)
  i +=1
print(sum)