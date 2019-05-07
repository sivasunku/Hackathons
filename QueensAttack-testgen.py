# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:29:02 2019

@author: siva
"""

import random
#Read N - size of board, m -pieces to be generated
N,m = map(int,input().rstrip().split())
print(N,m)
pieces = []
coords = []
count = 1
while count <= m:
  i = random.randint(1,N)
  j = random.randint(1,N)
  if ([i,j] in coords):
    pass
  else:
    tmp = "Q" + str(count)
    pieces.append([i,j,tmp])
    coords.append([i,j])
    count +=1
for x in pieces:
  print(str(x[0]) + "," + str(x[1]) + "," + x[2])