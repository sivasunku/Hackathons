#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    #h1 = [3, 2, 1, 1,1]
    #h2 = [4, 3, 2]
    #h3 = [1, 1, 4, 1]
    stacks = [h1,h2,h3]
    h1s = sum(h1)
    h2s = sum(h2)
    h3s = sum(h3)
    #print(h1,h1s)
    #print(h2,h2s)
    #print(h3,h3s)
    sums=[h1s,h2s,h3s]
    
    while(len(set(sums)) != 1):
      n = sums.index(max(sums))
      minRef = min(sums)
      counter = sums[n]
      sel = stacks[n]
      while ( counter > minRef):
        counter -= sel[0]
        del sel[0]
      sums[n] = counter
      #print(stacks)
      #print(sums)
    #print(sums[0])    
    return sums[0]
    

if __name__ == '__main__':
    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)

