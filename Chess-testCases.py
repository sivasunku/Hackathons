# -*- coding: utf-8 -*-
"""
Creates the test Cases for chess problem
 N - size of the matrix
 m - No. of pieces (Q,B,R,K,N)
"""
#Create test cases for input Matrix
# Make an empty list
# Add random pairs in between (1,N),(1,N) (One of Piece)
# Sort and eliminate the duplicates 
# Print N
# Print each of the list element

import random 
#NOOFTESTCASES,MAXMATRIXSIZE = map(int, input().rstrip().split())
N,m = map(int, input().rstrip().split())
pieces = ['Q','R','B','K','N']
coords = []
mpairs = []
counter = 0
while(counter < m):
  i = random.randint(1,N)
  j = random.randint(1,N)
  p = random.choice(pieces)
  if ([i,j] in coords):
    pass
  else:
    coords.append([i,j])
    mpairs.append([i,j,p])
    counter += 1

print(str(N) + " " + str(m))
for x in mpairs:
  print(*x,sep=",")
