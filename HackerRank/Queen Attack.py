#!/bin/python3


"""Queen Attack problem from hackerrank"""

import math
import os
import random
import re
import sys

isValid = lambda x,n: True if ( (x>=0) and (x<=n+1)) else False 
# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
  #Append the max possible obstacles

  #Adding a Zero row
  newObs = []
  diffrc = r_q - c_q
  sumrc  = r_q + c_q
  #For Zero row, tc - probable column
  newObs.append([0,c_q])
  tc = (0-diffrc)
  if isValid(tc,n):
    newObs.append([0,tc])
  tc = sumrc
  if isValid(tc,n):
    newObs.append([0,tc])

  #For Zero Column
  newObs.append([r_q,0])
  tr = diffrc
  if isValid(tr,n):
    newObs.append([tr,0])
  tr = sumrc
  if isValid(tr,n):
    newObs.append([tr,0])
  
  #For n+1 row
  newObs.append([n+1,c_q])
  tc = n+1 - diffrc
  if isValid(tc,n):
    newObs.append([n+1,tc])
  
  tc = sumrc -(n+1)
  if isValid(tc,n):
    newObs.append([n+1,tc])
  
  #For n+1 col
  newObs.append([r_q,n+1])
  tr = diffrc + (n+1)
  if isValid(tr,n):
    newObs.append([tr,n+1])

  tr = sumrc - (n+1)
  if isValid(tr,n):
    newObs.append([tr,n+1])
  
  obstacles = obstacles + newObs
  print(obstacles)
  
  #Get EW boundaries
  #Select Max col from obstacles where (col < c_q) and (row == r_q)
  #Select Min col from obstacles where (col > c_q) and (row == r_q)
  print([c[1] for c in obstacles if ( (c[0] == r_q) and (c[1] > c_q) )])
  eb = min([c[1] for c in obstacles if ( (c[0] == r_q) and (c[1] > c_q) )])
  wb = max([c[1] for c in obstacles if ( (c[0] == r_q) and (c[1] < c_q) )])
  ew = eb - wb - 2
  #Get NS boundaries
  nb = min([c[0] for c in obstacles if ( (c[1] == c_q) and (c[0] > r_q) )])
  sb = max([c[0] for c in obstacles if ( (c[1] == c_q) and (c[0] < r_q) )])
  ns = nb - sb - 2
  
  #Get SN boundaries
  swb = max([c[0] for c in obstacles if ( (c[0] - c[1] == diffrc) and (c[0] < r_q) )])
  neb = min([c[0] for c in obstacles if ( (c[0] - c[1] == diffrc) and (c[0] > r_q) )])
  nsd = neb - swb -3
  
  #Get NS boundaries
  print("Here")
  print([c[0] for c in obstacles if ( (c[0] + c[1] == sumrc) and (c[0] < r_q) )])
  nwb = min([c[0] for c in obstacles if ( (c[0] + c[1] == sumrc) and (c[0] > r_q) )])
  seb = max([c[0] for c in obstacles if ( (c[0] + c[1] == sumrc) and (c[0] < r_q) )])
  nss = nwb - seb -3
  
  return str(max(0,ew + ns + nsd + nss))
  
  #Get the boundaries Ew
  
  #For East - 
  # For all obstacles in same row, get east boundary & west boundary
  
if __name__ == '__main__':
    fptr = open("result.txt", 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()