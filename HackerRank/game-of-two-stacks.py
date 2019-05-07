# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:32:37 2019

@author: siva
"""

#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    #
    # Write your code here.
    #
  runningSum = 0
  count = 0
  while (runningSum <= x):
    a1 = a[0]
    b1 = b[0]
    runningSum += min(a1,b1)
    if (a1 < b1):
      del a[0]
      count += 1
    else:
      del b[0]
      count += 1
  return (count-1)
  
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        #fptr.write(str(result) + '\n')
        print(result)

    #fptr.close()
