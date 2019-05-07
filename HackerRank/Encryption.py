# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:33:46 2019

@author: siva
"""

#Encryption
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
  s = s.replace(" ","")
  L = len(s)
  rows,rem = divmod(L**0.5,1)
  cols = int(rows)
  rows = int(rows)
  if (rem >0 ):
    cols += 1
  while ( cols * rows < L):
    if (rows < cols):
      rows += 1
    else:
      cols += 1

  res = []
  for i in range(cols):
    tmp = ""
    steps = cols
    curr = i
    while (curr < L):
      tmp = tmp + s[curr]
      curr += steps
    res.append(tmp)
    
  return " ".join(res)
  
if __name__ == '__main__':
    fptr = open("result.txt", 'w')
    s = input()
    result = encryption(s)
    fptr.write(result + '\n')
    fptr.close()
