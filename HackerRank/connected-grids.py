# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:20:58 2019

@author: siva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#Return max value of surrounding 8 blocks
def getMax(refm,i,j):
  maxN = max(refm[i-1][j-1],refm[i-1][j],refm[i-1][j+1])
  return maxN
# Complete the connectedCell function below.

def connectedCell(matrix,n,m):
  #Create a dummy refm of size (n+2,m+2). Extra ones are just padded 
  # with zeroes
  refm =[]
  for _ in range(n+2):
    refm.append([0] * (m+2))

  maxv = 0
  for i in range(1,n+1):
    for j in range(1,m+1):
      maxN = getMax(refm,i,j)
      if (matrix[i-1][j-1] == 1):
        if (j >= 2):
          left = matrix[i-1][j-2]
        else:
          left = 0
        refm[i][j] = maxN + left + 1
        if (refm[i][j] > maxv):
          maxv = refm[i][j]
    for x in range(1,n+1):
      print(refm[x][1:m+1])
    print()
      
  for i in range(n):
    print(matrix[i])
  print()

  return(maxv)
  
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix,n,m)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
