# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:33:09 2019

@author: siva
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
  count = 0
  deletions = True
  while(deletions == True):
    #print("Count",count)
    #print(p)
    deletions = False
    i = len(p) - 1
    count +=1
    while (i>0):
      if (p[i] > p[i-1]):
        del p[i]
        deletions = True
      i -= 1
  #print(count-1)
  return(count-1)

    

if __name__ == '__main__':
    fptr = open("result.txt", 'w')
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = poisonousPlants(p)
    fptr.write(str(result) + '\n')
    fptr.close()
